# Import packages
import os
from pathlib import Path

from datetime import date, time
from birdnet import (SpeciesPredictions,
                     predict_species_within_audio_file,
                     predict_species_at_location_and_time
)
import pandas as pd




# Main program block
if __name__ == "__main__":

    # Generate species set to filter possible results based on lat/lon
    species_list = predict_species_at_location_and_time(40,-105)
    species_set = set(species_list.keys())

    # Establish directory to obtain audio files from
    # Files will be obtained from all subdirectories as well
    base_dir = Path('.')

    # Generate list of paths to all .wav audio files
    wav_files = list(base_dir.rglob('*.wav'))

    # Establish empty dictionary to write results to
    result_dict = {}

    # Loop through .wav files
    for file_path in wav_files:
        # Run BirdNET artificial neural network
        result = SpeciesPredictions(predict_species_within_audio_file(
            file_path, 
            min_confidence=0.50,
            species_filter=species_set))
        # File name for metadata
        file_name = os.path.basename(file_path)
        # Add to dictionary
        result_dict[f'{file_name}'] = result


    results_temp = []

    # Unpack result dictionary
    for file, result in result_dict.items():
        # Loop through first tier OrderedDict
        for time_interval, pred_dict in list(result.items()):
            # Loop through second tier OrderedDict
            for species, confidence in pred_dict.items():
                species_dict = {'source': file,
                                'Burn_unit': file[:2],
                                'Burn_Severity': file[2],
                                'Survey_Location': int(file[4:7]),
                                'date': date.fromisoformat(file[8:16]),
                                'time': time.fromisoformat(file[17:23]),
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

    # Convert DataFrame to csv file and save to same folder as script
    result_species_df.to_csv(
        Path('.clean_bird_data.csv'),
        index=False)