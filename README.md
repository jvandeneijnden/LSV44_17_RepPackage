# Analysis reproduction repository for "VLA monitoring of LS V +44 17 reveals scatter in the X-ray -- radio correlation of Be/X-ray binaries"

![Light curves](PaperFigures/lc.png?raw=true "Light curves")

## Based on Van den Eijnden et al. (2023), MNRAS accepted (30 October 2023).
The full paper, included updated versions can be found on https://arxiv.org/abs/ADDLINK (open access) and is included in this repository. 

This reproduction repository contains the following files:
- VLAscripts: scripts to flag, calibrate, and image all ten VLA radio observations, starting from the VLA data archive uncalibrated measurement sets. Includes a ReadMe with more detailed instructions.
- Xrays: the data files underlying the x-ray spectral analysis, including .xcm files of the final fitted XSPEC models. Includes a ReadMe with more detailed instructions.
- Jupyter notebooks to reproduce the calculations and fits in the paper, and to reproduce the figures shown in the paper.
- All data underlying the figures in the paper.
- A tarball containing all files to reproduce the paper from its TeX file. 

Please get in touch via email (jakob.van-den-eijnden [at] warwick.ac.uk) or via github with questions.

If this repository is useful for your own research, in addition to citing the original paper, please consider including a note to this repository as well, for instance via its Zenodo DOI. 

## Software requirements

To reproduce the analysis and figures, the notebook is written in Python 3. Conversion to python 2 should be straightforward but is not recommended.

The notebook uses the following packages:

- numpy
- matplotlib
- astropy
- aplpy









