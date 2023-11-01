### The commands below can be used for each of the analysed NICER ObsIDs to reduce the data, extract spectra and light curves, and to prepare the spectra for analysis in XSPEC using grppha. These commands were run in HEASOFT v6.31.1.

### The start point for this analysis are the data folders as downloaded from the HEASARC.

### We note that this log contain the commands to load and reproduce the fits and flux measurements. However, this log does not serve as a replacement for an XSPEC tutorial; we refer to the extensive XSPEC documentation for the further use and interpretation of xspec outcomes.

### Reduction and extraction using nicerl2 and nicerl3 per ObsID:
 
nicerl2 indir=./5203610110 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610110 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610110 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610113 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610113 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610113 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610115 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610115 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610115 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610117 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610117 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610117 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610121 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610121 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610121 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610124 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610124 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610124 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610134 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610134 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610134 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610139 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610139 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610139 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610148 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610148 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610148 clobber=YES pirange=30:800 timebin=10.0

nicerl2 indir=./5203610155 clobber=YES filtcolumns=NICERV3

nicerl3-spect indir=./5203610155 bkgmodeltype=3c50 bkgformat=file clobber=YES

nicerl3-lc indir=./5203610155 clobber=YES pirange=30:800 timebin=10.0

### For each of the extracted spectra, the command below can be used to link it to its background spectrum and response files. Note that these need to be run one by one in a folder containing either these files, or symbolic links to these files (created using 'ln -s <target file path> <symbolic link folder path>'.

grppha infile='ni5203610110mpu7_sr.pha' outfile='ni5203610110mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610110mpu7_bg.pha&chkey ancrfile ni5203610110mpu7.arf&chkey respfile ni5203610110mpu7.rmf&exit'

grppha infile='ni5203610113mpu7_sr.pha' outfile='ni5203610113mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610113mpu7_bg.pha&chkey ancrfile ni5203610113mpu7.arf&chkey respfile ni5203610113mpu7.rmf&exit'

grppha infile='ni5203610115mpu7_sr.pha' outfile='ni5203610115mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610115mpu7_bg.pha&chkey ancrfile ni5203610115mpu7.arf&chkey respfile ni5203610115mpu7.rmf&exit'

grppha infile='ni5203610117mpu7_sr.pha' outfile='ni5203610117mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610117mpu7_bg.pha&chkey ancrfile ni5203610117mpu7.arf&chkey respfile ni5203610117mpu7.rmf&exit'

grppha infile='ni5203610121mpu7_sr.pha' outfile='ni5203610121mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610121mpu7_bg.pha&chkey ancrfile ni5203610121mpu7.arf&chkey respfile ni5203610121mpu7.rmf&exit'

grppha infile='ni5203610124mpu7_sr.pha' outfile='ni5203610124mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610124mpu7_bg.pha&chkey ancrfile ni5203610124mpu7.arf&chkey respfile ni5203610124mpu7.rmf&exit'

grppha infile='ni5203610134mpu7_sr.pha' outfile='ni5203610134mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610134mpu7_bg.pha&chkey ancrfile ni5203610134mpu7.arf&chkey respfile ni5203610134mpu7.rmf&exit'

grppha infile='ni5203610139mpu7_sr.pha' outfile='ni5203610139mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610139mpu7_bg.pha&chkey ancrfile ni5203610139mpu7.arf&chkey respfile ni5203610139mpu7.rmf&exit'

grppha infile='ni5203610148mpu7_sr.pha' outfile='ni5203610148mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610148mpu7_bg.pha&chkey ancrfile ni5203610148mpu7.arf&chkey respfile ni5203610148mpu7.rmf&exit'

grppha infile='ni5203610155mpu7_sr.pha' outfile='ni5203610155mpu7_sr_linked.pha' chatter=0 comm='chkey backfile ni5203610155mpu7_bg.pha&chkey ancrfile ni5203610155mpu7.arf&chkey respfile ni5203610155mpu7.rmf&exit'

### The resulting spectra, backgrounds, and response files, as analysed for the paper, are also included in this data reproduction package.

### In xspec, the analysis can be repeated by using the commands:

@reproduce_fits.xcm

fit

query yes

error 1. 1-90

### The 0.5-10 keV unabsorbed fluxes and their 1-sigma errors can be measured using the commands:

@reproduce_fluxes.xcm

fit

query yes

error 1. 4 16 28 40 52 64 76 88 100 112


