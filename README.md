# Automating Audio File Processing Through BirdNET


[![DOI](https://zenodo.org/badge/976995645.svg)](https://doi.org/10.5281/zenodo.15332056)
---

## Description

This project seeks to use the (https://github.com/birdnet-team/birdnet)[birdnet] python library to process multiple WAV audio files into a CSV file of the recorded bird species. It is being completed to assist the research of the USDA and Colorado State University at Rocky Mountain Biological Laboratory Field Station to asses changes to occupancy and biodiversity in relation to pyrodiversity. Acoustic monitoring provides a non-invasive method to estimate bird densities and abundances with results comparable to human surveys (Pérez-Granados & Traba, 2021). Automating the processing of the data avoids having to feed files through the (https://github.com/birdnet-team/BirdNET-Analyzer)[BirdNET Analyzer] individually. The end result is a CSV file of predicted bird species and the relevant metadata that the staff are able to use for their analyses.

---

## Data Description

WAV Audio Files: Audio files are recorded in the field by stationary acoustic monitors and were provided by the project partner. They provide the recordings of bird calls to be analyzed and fill the CSV file.



--- 

## Instructions

A python version between 3.9 but older than 3.12 is required to run the notebooks.

The notebooks are dependent on the BirdNET package which can be installed with the command:  ```pip install birdnet```

---

## Citations

Kahl, Stefan and Wood, Connor M and Eibl, Maximilian and Klinck, Holger. "BirdNET: A deep learning solution for avian diversity monitoring." Ecological Informatics vol. 61 (2021): 101-236. Elsevier.

Pérez-Granados, Cristian, and Juan Traba. “Estimating Bird Density Using Passive Acoustic Monitoring: A Review of Methods and Suggestions for Further Research.” Ibis 163, no. 3 (July 2021): 765–83. https://doi.org/10.1111/ibi.12944.


