# Automating Audio File Processing Through BirdNET


[![DOI](https://zenodo.org/badge/976995645.svg)](https://doi.org/10.5281/zenodo.15332056)
---

## Description

This project seeks to use the [birdnet](https://github.com/birdnet-team/birdnet) python library to process multiple WAV audio files into a CSV file of the recorded bird species. It is being completed to assist the research of the USDA and Colorado State University at Rocky Mountain Biological Laboratory Field Station to asses changes to occupancy and biodiversity in relation to pyrodiversity. Acoustic monitoring provides a non-invasive method to estimate bird densities and abundances with results comparable to human surveys (Pérez-Granados & Traba, 2021). Automating the processing of the data avoids having to feed files through the [BirdNET Analyzer](https://github.com/birdnet-team/BirdNET-Analyzer) individually. The end result is a CSV file of predicted bird species and the relevant metadata that the staff are able to use for their analyses.

---

## Data Description

WAV Audio Files: Audio files are recorded in the field by stationary acoustic monitors and were provided by the project partner. They provide the recordings of bird calls to be analyzed and fill the CSV file. (Awaiting permission from project partner to publish and preferred citation details.)



--- 

## Instructions

Download the project files and ensure the [conda](https://www.anaconda.org/anaconda/conda) package manager is installed on your machine. A minimalist installation is available in [miniconda](https://www.anaconda.com/download/success).

In a bash terminal, change directories to the project directory. Create the project environment from the environment.yml file with ```conda env create -f environment.yml```. Activate the environment with ```conda activate bird-geospatial-env```.

The three notebooks can be run in any order:

* 00site_map.ipynb : Generates an interactive map of the site of the Cameron Peak 2020 fire.
* 01birdnet_exploration.ipynb : Exploration of the functions of the birdnet python package and trials to process audio files.
* 02process_wavs.ipynb : Streamlined workflow of looping through and processing audio files.

---

## Citations

Kahl, Stefan and Wood, Connor M and Eibl, Maximilian and Klinck, Holger. "BirdNET: A deep learning solution for avian diversity monitoring." Ecological Informatics vol. 61 (2021): 101-236. Elsevier.

Pérez-Granados, Cristian, and Juan Traba. “Estimating Bird Density Using Passive Acoustic Monitoring: A Review of Methods and Suggestions for Further Research.” Ibis 163, no. 3 (July 2021): 765–83. https://doi.org/10.1111/ibi.12944.


