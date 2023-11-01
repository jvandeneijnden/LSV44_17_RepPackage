# Readme for the VLA data analysis scripts.

For each of the observations, download the data via data.nrao.edu by searching for the program code of this observing program, i.e. VLA/22B-051. Select the observation(s) and download the raw data, not the pipeline (i.e. calibrated) data. 

The scripts can be used in CASA and have been tested in CASA v6.4.1 running on Ubuntu 22.04.3 LTS. To run the script, use execfile('observations1_analysis.py') [changed to the correct observation number]. 

The final stage creates images at X and C band. To measure the RMS or use imfit to measure the source flux density, we refer to the standard casa/VLA tutorials (as we applied these interactively without scripting). 

! These scripts are not intended as a tutorial for VLA data analysis, for which we recommend the official NRAO/VLA tutorials, but to aid reproduction of our results !