# Import Packages: Standard Library
import os
import logging
import warnings
from datetime import date, time
from pathlib import Path
# Third Party
import pandas as pd
from birdnet import (SpeciesPredictions,
                     predict_species_within_audio_file,
                     predict_species_at_location_and_time)
from tqdm import tqdm # Progress meter widget

# Ignore warnings
warnings.filterwarnings('ignore')
logging.basicConfig(level=logging.ERROR)

def gen_species_set():
    """
    Generates a set of bird species based off user inputted lat/lon.

    Parameters
    ----------
    lat : float
        Latitude value ranging from -180 to 180 with one decimal place.
    lon : float
        Longitude value ranging from -180 to 180 with one decimal place.
    Returns
    -------
    species_set : set
        Set of bird species name and common names found at location.
    """
    lat = round(float(
        input("Enter the latitude to filter species (e.g. 40.0) ")), 1)
    lon = round(float(
        input("Enter the longitude to filter species (e.g. -105.0): ")), 1)
    species_list = predict_species_at_location_and_time(lat, lon)
    species_set = set(species_list.keys())

    return species_set

# Main program block
if __name__ == "__main__":

    # Generate species set to filter possible results based on lat/lon
    species_set = gen_species_set()

    # Establish directory to obtain audio files from
    # Files will be obtained from all subdirectories as well
    base_dir = Path('.')

    # Establish path to result csv
    clean_bird_path = Path('clean_bird_data.csv')
    columns = ['source', 'Burn_unit', 'Burn_Severity', 'Survey_Location',
           'date', 'time', 'ScientificName', 'CommonName', 'Start(s)',
           'End(s)', 'Confidence']
    
    # Load existing data if exists
    if os.path.exists(clean_bird_path):
        clean_bird_df = pd.read_csv(clean_bird_path, usecols=['source'])
        # For file tracking to avoid reanalyzing
        analyzed_files = set(clean_bird_df['source'])
    else:
        # Create empty set for file tracking and csv header
        analyzed_files = set()
        pd.DataFrame(columns=columns).to_csv(clean_bird_path, index=False)

    # Generate list of paths to all .wav audio files
    wav_files = [
        f for f in base_dir.rglob('*.wav')
        # Exclude Bat Audio files (Project specific)
        if "Data" not in f.parts and "Data2" in f.parts
    ]

    # Establish empty dictionary to write results to
    result_dict = {}

    # Loop through .wav files
    for file in tqdm(wav_files):
        # Check if file has been analyzed already
        if file.name in analyzed_files:
            continue

        # Run BirdNET artificial neural network
        result = SpeciesPredictions(predict_species_within_audio_file(
            file, 
            min_confidence=0.50,
            species_filter=species_set))
        
        # Add to dictionary
        result_dict[file] = result

        # Unpack result dictionary
        for file, result in result_dict.items():
            results_temp = []
            # Loop through first tier OrderedDict
            for time_interval, pred_dict in list(result.items()):
                # Loop through second tier OrderedDict
                for species, confidence in pred_dict.items():
                    species_dict = {'source': file.name,
                                    'Burn_unit': file.name[:2],
                                    'Burn_Severity': file.name[2],
                                    'Survey_Location': int(file.name[4:7]),
                                    'date': date.fromisoformat(file.name[8:16]),
                                    'time': time.fromisoformat(file.name[17:23]),
                                    'ScientificName': species.split('_')[0],
                                    'CommonName': species.split('_')[1],
                                    'Start(s)': int(time_interval[0]),
                                    'End(s)': int(time_interval[1]),
                                    'Confidence': confidence}
                    results_temp.append(species_dict)

        # Build DataFrame from results
        result_species_df = pd.DataFrame(results_temp, 
                                        columns=['source',
                                                    'Burn_unit',
                                                    'Burn_Severity',
                                                    'Survey_Location',
                                                    'date',
                                                    'time',
                                                    'ScientificName', 
                                                    'CommonName',
                                                    'Start(s)',
                                                    'End(s)',
                                                    'Confidence'])
        
        result_species_df.to_csv(
            clean_bird_path, mode='a', header=False, index=False
        )