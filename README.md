# BirdNET to CSV

## An alternative to BirdNET Analyzer to process WAV files of bird calls into a CSV of identified species.


[![DOI](https://zenodo.org/badge/976995645.svg)](https://doi.org/10.5281/zenodo.15332056)
---

## Description

This project seeks to use the [birdnet](https://github.com/birdnet-team/birdnet) python library to process multiple WAV audio files into a CSV file of the recorded bird species. It is being completed to assist the research of the USDA and Colorado State University at Rocky Mountain Biological Laboratory Field Station to asses changes to occupancy and biodiversity in relation to pyrodiversity. Acoustic monitoring provides a non-invasive method to estimate bird densities and abundances with results comparable to human surveys (Pérez-Granados & Traba, 2021). Automating the processing of the data avoids having to feed files through the [BirdNET Analyzer](https://github.com/birdnet-team/BirdNET-Analyzer) in multiple jobs. The end result is a CSV file of predicted bird species and the relevant metadata that the staff are able to use for their analyses.

---

## Data Description

WAV Audio Files: Audio files are recorded in the field by stationary acoustic monitors and were provided by the project partner. They provide the recordings of bird calls to be analyzed and fill the CSV file. A zip file containing the two audio files used as an example in 02process_wavs.ipynb is available [here](https://github.com/tjstogoski/bird-automation/releases/download/v.1.0/audio_data.zip)

--- 

## Instructions

### Executable Tool

The BirdNET to CSV tool is available for download in the releases section of this repository. Download birdnet_to_csv.exe to the directory containing the WAV files you wish to analyze and double-click to run. In the terminal that will appear, enter the latitude and longitude that the recording was taken at to filter the possible species results.

### Notebooks

Clone the repository to your machine and ensure the [conda](https://www.anaconda.org/anaconda/conda) package manager is installed on your machine. A minimalist installation is available in [miniconda](https://www.anaconda.com/download/success).

In a bash terminal, change directories to the project directory. Create the project environment from the environment.yml file with ```conda env create -f environment.yml```. Activate the environment with ```conda activate bird-geospatial-env```.

The three notebooks can be run in a Jupyter notebook type interactive environment such as [VS Code](https://code.visualstudio.com/download). They can be ran in any order:

* 01site_map.ipynb : Generates an interactive map of the site of the Cameron Peak 2020 fire. (Optional)
* 02process_wavs.ipynb : Example usage of looping through and processing audio files.

---

## Citations

Kahl, S., Wood, C. M., Eibl, M., & Klinck, H. (2021) BirdNET: A deep learning solution for avian diversity monitoring. Ecological Informatics, 61, 101236. https://doi.org/10.1016/j.ecoinf.2021.101236

McTigue, L. (2025). CP1-007 [Audio Recordings]. Retrieved from https://github.com/tjstogoski/bird-automation/releases/download/v.1.0/audio_data.zip

Pérez-Granados, Cristian, and Juan Traba. “Estimating Bird Density Using Passive Acoustic Monitoring: A Review of Methods and Suggestions for Further Research.” Ibis 163, no. 3 (July 2021): 765–83. https://doi.org/10.1111/ibi.12944.
