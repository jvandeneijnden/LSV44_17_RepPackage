# Analysis script of the 10th VLA epoch of LS V +44 17. 
# Due to the faintness of the target, all analysis is performed manually. The authors attempted to use the VLA pipeline and improve the images by applying residual manual flagging, but found that a fully manual analysis yielded better sensitivity. 
# -------------------------------------------------------------------------------
# ! These scripts are not intended as a tutorial for VLA data analysis, for which we recommend the official NRAO/VLA tutorials, but to aid reproduction of our results !
# -------------------------------------------------------------------------------
# This script can be called in the casa command line via:
#
# execfile('observation10_analysis.py')
#
# Each of the ten epochs has its own analysis script. The measurement set from the VLA archive needs to be located in the same folder as the script. 
# While each observation's files are labeled by observation number, the authors recommend analysing each observation in a separate folder due to the number of output files and folder.
# -------------------------------------------------------------------------------
# This analysis script, and the equivalently structured ones for the other epochs, perform the following steps:
# 1) flag setup scans and spectral windows, apply standard data flags, and flag out manually identified RFI. 
# 2) calibrate the C and X band data separately.
# 3) image the C and X band data separately.
# For brevity, the script only executes these steps and does not produce diagnostic plots for flagging and calibration. The measurement set and calibration tables can be inspected after running the script using plotms. 
#
# -------------------------------------------------------------------------------
# STEP 0: definitions
# -------------------------------------------------------------------------------
# 
myvis="22B-051.sb43655597.eb43657562.59997.034916585646.ms"
mylabel='RXJ0440.obs10.59997'
#
# -------------------------------------------------------------------------------
# STEP 1: data flagging
# -------------------------------------------------------------------------------
# 
# Flagging the setup scans for both C and X band, as well as the C band dummy setup spws. Note that these don't exist for X band as X band is directly set up in its appropriate instrument configuration. 
#
flagdata(vis=myvis,timerange='',spw='', antenna='', scan='1~3')
flagdata(vis=myvis,timerange='',spw='', antenna='', scan='12~13')
flagdata(vis=myvis,timerange='',spw='0~1', antenna='')
#
# Standard flagging steps: autocorrelations, shadows, first 3 seconds of each scan, hanningsmoothing. 
#
flagdata(vis=myvis, autocorr=True)
flagdata(vis=myvis, mode='shadow')
flagdata(vis=myvis, mode='quack', quackinterval=3.0, quackmode='beg')
hanningsmooth(vis=myvis,datacolumn='all', outputvis=mylabel+'.hs.ms')
myvis=mylabel+'.hs.ms'
#
# Manual flagging based on inspection of flux calibrator, phase calibrator, and target in plotms():
#
flagdata(vis=myvis, spw='16')
flagdata(vis=myvis, spw='19')
flagdata(vis=myvis, spw='63:0~30')
flagdata(vis=myvis, spw='44:31~62')
flagdata(vis=myvis, antenna='ea02', spw='18~33')
flagdata(vis=myvis, antenna='ea17', spw='18~33')
flagdata(vis=myvis, spw='47:32~38')
flagdata(vis=myvis, spw='47:48~52')
flagdata(vis=myvis, spw='48:11~16')
flagdata(vis=myvis, spw='48:24~28')
flagdata(vis=myvis, spw='48:39~43')
flagdata(vis=myvis, spw='48:51~56')
flagdata(vis=myvis, spw='49:0~10')
flagdata(vis=myvis, spw='2~3', antenna='ea05&ea06')
flagdata(vis=myvis, spw='5:18~30')
flagdata(vis=myvis, spw='11:22~32')
flagdata(vis=myvis, spw='15:50~62')
flagdata(vis=myvis, spw='17:17~32')
flagdata(vis=myvis, spw='18:20~40')
flagdata(vis=myvis, spw='20:19~35')
flagdata(vis=myvis, spw='21:0~30')
flagdata(vis=myvis, spw='33:12~34')
flagdata(vis=myvis, spw='28:55~61')
flagdata(vis=myvis, spw='48:62')
flagdata(vis=myvis, spw='47~49')
#
# -------------------------------------------------------------------------------
# STEP 2: Calibration
# -------------------------------------------------------------------------------
#
# First, split the data into two measurement sets: one per band. 
#
split(vis=myvis, outputvis=mylabel+'.REALXband.ms', spw='34~65', datacolumn='DATA')
split(vis=myvis, outputvis=mylabel+'.FullCband.ms', spw='2~33', datacolumn='DATA')
#
# Then, switch to X band for calibration:
#
SPW = '0~31'
myvis=mylabel+'.REALXband.ms'

setjy(vis=myvis, field='0', modimage='3C48_X.im', standard='Perley-Butler 2013', usescratch=False, scalebychan=True, spw='')
gaincal(vis=myvis, caltable=mylabel+'.REALXband'+'.G0all', field='0,1', refant='ea05', spw=SPW+':10~50', gaintype='G', calmode='p', solint='int', minsnr=5, append=False)
gaincal(vis=myvis, caltable=mylabel+'.REALXband'+'.G0', field='0', refant='ea05', spw=SPW+':10~50', calmode='p', solint='int', minsnr=5)
gaincal(vis=myvis,caltable=mylabel+'.REALXband'+'.K0', gaintable=[mylabel+'.REALXband'+'.G0'], field='0',spw=SPW+':1~61',gaintype='K', refant='ea05', combine='scan', solint='inf', minsnr=3)

bandpass(vis=myvis,caltable=mylabel+'.REALXband'+'.B0', gaintable=[mylabel+'.REALXband'+'.G0',mylabel+'.REALXband'+'.K0'], field='0', spw=SPW, refant='ea05',solnorm=True, bandtype='B', combine='scan', solint='inf')
gaincal(vis=myvis, caltable=mylabel+'.REALXband'+'.G1', gaintable=[mylabel+'.REALXband'+'.K0',mylabel+'.REALXband'+'.B0'], field='0', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G', calmode='ap', append=False)
gaincal(vis=myvis,caltable=mylabel+'.REALXband'+'.G1', gaintable=[mylabel+'.REALXband'+'.K0', mylabel+'.REALXband'+'.B0'], field='1', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G',calmode='ap', append=True)
myscaleXreal=fluxscale(vis=myvis, caltable=mylabel+'.REALXband'+'.G1', fluxtable=mylabel+'.REALXband'+'.fluxscale1', reference='0', transfer='1')

applycal(vis=myvis, gaintable=[mylabel+'.REALXband'+'.K0', mylabel+'.REALXband'+'.fluxscale1', mylabel+'.REALXband'+'.B0'], parang=False, field='0', gainfield=['','0',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.REALXband'+'.K0', mylabel+'.REALXband'+'.fluxscale1', mylabel+'.REALXband'+'.B0'], parang=False, field='1', gainfield=['','1',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.REALXband'+'.K0', mylabel+'.REALXband'+'.fluxscale1', mylabel+'.REALXband'+'.B0'], parang=False, field='2', gainfield=['','1',''], interp=['','linear',''], calwt=False, spw=SPW)
# 
# Repeat for C band
#
SPW = '0~31'
myvis=mylabel+'.FullCband.ms'

setjy(vis=myvis, field='0', modimage='3C48_C.im', standard='Perley-Butler 2013', usescratch=False, scalebychan=True, spw='')
gaincal(vis=myvis, caltable=mylabel+'.FullCband'+'.G0all', field='0,1', refant='ea05', spw=SPW+':10~50', gaintype='G', calmode='p', solint='int', minsnr=5, append=False)
gaincal(vis=myvis, caltable=mylabel+'.FullCband'+'.G0', field='0', refant='ea05', spw=SPW+':10~50', calmode='p', solint='int', minsnr=5)
gaincal(vis=myvis,caltable=mylabel+'.FullCband'+'.K0', gaintable=[mylabel+'.FullCband'+'.G0'], field='0',spw=SPW+':1~61',gaintype='K', refant='ea05', combine='scan', solint='inf', minsnr=3)

bandpass(vis=myvis,caltable=mylabel+'.FullCband'+'.B0', gaintable=[mylabel+'.FullCband'+'.G0',mylabel+'.FullCband'+'.K0'], field='0', spw=SPW, refant='ea05',solnorm=True, bandtype='B', combine='scan', solint='inf')
gaincal(vis=myvis, caltable=mylabel+'.FullCband'+'.G1', gaintable=[mylabel+'.FullCband'+'.K0',mylabel+'.FullCband'+'.B0'], field='0', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G', calmode='ap', append=False)
gaincal(vis=myvis,caltable=mylabel+'.FullCband'+'.G1', gaintable=[mylabel+'.FullCband'+'.K0', mylabel+'.FullCband'+'.B0'], field='1', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G',calmode='ap', append=True)
myscaleXreal=fluxscale(vis=myvis, caltable=mylabel+'.FullCband'+'.G1', fluxtable=mylabel+'.FullCband'+'.fluxscale1', reference='0', transfer='1')

applycal(vis=myvis, gaintable=[mylabel+'.FullCband'+'.K0', mylabel+'.FullCband'+'.fluxscale1', mylabel+'.FullCband'+'.B0'], parang=False, field='0', gainfield=['','0',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.FullCband'+'.K0', mylabel+'.FullCband'+'.fluxscale1', mylabel+'.FullCband'+'.B0'], parang=False, field='1', gainfield=['','1',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.FullCband'+'.K0', mylabel+'.FullCband'+'.fluxscale1', mylabel+'.FullCband'+'.B0'], parang=False, field='2', gainfield=['','1',''], interp=['','linear',''], calwt=False, spw=SPW)
#
# -------------------------------------------------------------------------------
# STEP 3: Imaging
# -------------------------------------------------------------------------------
# 
# The below commands image both C and X band non-interactively
#
# First, split of the calibrated target field:
#
myvis=mylabel+'.REALXband.ms'

split(vis=myvis, outputvis=mylabel+'.REALXband.split.ms', datacolumn='corrected', field='2')
#
# Image X band:
#
myvis = mylabel+'.REALXband.split.ms'

tclean(vis=myvis, imagename=mylabel+'.im1', imsize=2048, cell='0.15arcsec', stokes='I', specmode='mfs',deconvolver='hogbom', robust=1., weighting='briggs', niter=2000, cycleniter=200, interactive=False, threshold='0.015 mJy')
#
# Repeat for C band:
#
myvis=mylabel+'.FullCband.ms'

split(vis=myvis, outputvis=mylabel+'.FullCband.split.ms', datacolumn='corrected', field='2')
#
# Image C band:
#
myvis = mylabel+'.FullCband.split.ms'

tclean(vis=myvis, imagename=mylabel+'.im1', imsize=4096, cell='0.25arcsec', stokes='I', specmode='mfs',deconvolver='hogbom', robust=0., weighting='briggs', niter=4000, cycleniter=200, interactive=False, threshold='0.015 mJy')
#
# -------------------------------------------------------------------------------
# FINISHED
# -------------------------------------------------------------------------------
#








