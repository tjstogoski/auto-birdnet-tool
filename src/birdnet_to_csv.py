# Import packages
import os
from pathlib import Path

from datetime import date, time
from birdnet import (SpeciesPredictions,
                     predict_species_within_audio_file
)
import pandas as pd





# Main program block
if __name__ == "__main__":
    # Establish empty dictionary to write results to
    result_dict = {}

    # Establish directory to obtain audio files from
    audio_data_path = '../data/raw/audio_data'

    for file in os.listdir(audio_data_path):
        # Generate file path
        file_path = Path(f'{audio_data_path}/{os.path.basename(file)}')
        # Run BirdNET artificial neural network
        result = SpeciesPredictions(predict_species_within_audio_file(
            file_path, min_confidence=0.50))
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
                                'Confidence': round(confidence, 2)}
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

    # Convert DataFrame to csv file
    result_species_df.to_csv(
        Path('../data/processed/clean_bird_data.csv'),
        index=False)