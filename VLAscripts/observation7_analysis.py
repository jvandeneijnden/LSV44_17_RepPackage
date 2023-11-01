# Analysis script of the 7th VLA epoch of LS V +44 17. 
# Due to the faintness of the target, all analysis is performed manually. The authors attempted to use the VLA pipeline and improve the images by applying residual manual flagging, but found that a fully manual analysis yielded better sensitivity. 
# -------------------------------------------------------------------------------
# ! These scripts are not intended as a tutorial for VLA data analysis, for which we recommend the official NRAO/VLA tutorials, but to aid reproduction of our results !
# -------------------------------------------------------------------------------
# This script can be called in the casa command line via:
#
# execfile('observation7_analysis.py')
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
myvis='22B-051.sb43582537.eb43587508.59975.02695987269.ms'
mylabel='RXJ0440.obs7.59975'
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
flagdata(vis=myvis, spw='16:8~12')
flagdata(vis=myvis, spw='16:20~40')
flagdata(vis=myvis, spw='16:50~55')
flagdata(vis=myvis, spw='18~33', antenna='ea24')
flagdata(vis=myvis, spw='18~33', antenna='ea17')
flagdata(vis=myvis, spw='19~21', antenna='ea02')
flagdata(vis=myvis, spw='18~33', antenna='ea05&ea23')
flagdata(vis=myvis, spw='18~33', antenna='ea14&ea23')
flagdata(vis=myvis, spw='19', antenna='ea23')
flagdata(vis=myvis, spw='16')
flagdata(vis=myvis, spw='15:47~62')
flagdata(vis=myvis, spw='18~33', antenna='ea14&ea27')
flagdata(vis=myvis, spw='18~22', antenna='ea27')
flagdata(vis=myvis, spw='18~22', antenna='ea10&ea22')
flagdata(vis=myvis, spw='19')
flagdata(vis=myvis, spw='20:20~40')
flagdata(vis=myvis, spw='21:0~22')
flagdata(vis=myvis, spw='33:13~28')
flagdata(vis=myvis, spw='2~3', antenna='ea27')
flagdata(vis=myvis, spw='5:18~27')
flagdata(vis=myvis, spw='17:50~63')
flagdata(vis=myvis, spw='18:20~40')
flagdata(vis=myvis, spw='21:20~30')
flagdata(vis=myvis, spw='21:62~63')
flagdata(vis=myvis, spw='29:50~63')
flagdata(vis=myvis, spw='30', antenna='ea05&ea06')
flagdata(vis=myvis, spw='28:30~63')
flagdata(vis=myvis, spw='44:31~63')
flagdata(vis=myvis, spw='47:25~40')
flagdata(vis=myvis, spw='48:0~10')
flagdata(vis=myvis, spw='48:30~40')
flagdata(vis=myvis, spw='34:0~10')
flagdata(vis=myvis, spw='47')
flagdata(vis=myvis, spw='48')
flagdata(vis=myvis, antenna='ea04&ea23', spw='59~65')
flagdata(vis=myvis, antenna='ea15&ea16', spw='59~65')
flagdata(vis=myvis, antenna='ea06&ea27', spw='59~65')
flagdata(vis=myvis, scan='16', spw='59~65')
flagdata(vis=myvis, spw='63:0~22')
flagdata(vis=myvis, spw='63:50~56')
#
# -------------------------------------------------------------------------------
# STEP 2: Calibration
# -------------------------------------------------------------------------------
#
# First, split the data into two measurement sets: one per band. 
#
split(vis=myvis, outputvis=mylabel+'.Xband.ms', spw='34~65', datacolumn='DATA')
split(vis=myvis, outputvis=mylabel+'.Cband.ms', spw='2~33', datacolumn='DATA')
#
# Then, switch to X band for calibration:
#
SPW = '0~31'
myvis=mylabel+'.Xband.ms'

setjy(vis=myvis, field='0', modimage='3C48_X.im', standard='Perley-Butler 2013', usescratch=False, scalebychan=True, spw='')
gaincal(vis=myvis, caltable=mylabel+'.Xband'+'.G0all', field='0,1', refant='ea05', spw=SPW+':10~50', gaintype='G', calmode='p', solint='int', minsnr=5, append=False)
gaincal(vis=myvis, caltable=mylabel+'.Xband'+'.G0', field='0', refant='ea05', spw=SPW+':10~50', calmode='p', solint='int', minsnr=5)
gaincal(vis=myvis,caltable=mylabel+'.Xband'+'.K0', gaintable=[mylabel+'.Xband'+'.G0'], field='0',spw=SPW+':1~61',gaintype='K', refant='ea05', combine='scan', solint='inf', minsnr=3)

bandpass(vis=myvis,caltable=mylabel+'.Xband'+'.B0', gaintable=[mylabel+'.Xband'+'.G0',mylabel+'.Xband'+'.K0'], field='0', spw=SPW, refant='ea05',solnorm=True, bandtype='B', combine='scan', solint='inf')
gaincal(vis=myvis, caltable=mylabel+'.Xband'+'.G1', gaintable=[mylabel+'.Xband'+'.K0',mylabel+'.Xband'+'.B0'], field='0', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G', calmode='ap', append=False)
gaincal(vis=myvis,caltable=mylabel+'.Xband'+'.G1', gaintable=[mylabel+'.Xband'+'.K0', mylabel+'.Xband'+'.B0'], field='1', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G',calmode='ap', append=True)
myscaleXreal=fluxscale(vis=myvis, caltable=mylabel+'.Xband'+'.G1', fluxtable=mylabel+'.Xband'+'.fluxscale1', reference='0', transfer='1')

applycal(vis=myvis, gaintable=[mylabel+'.Xband'+'.K0', mylabel+'.Xband'+'.fluxscale1', mylabel+'.Xband'+'.B0'], parang=False, field='0', gainfield=['','0',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.Xband'+'.K0', mylabel+'.Xband'+'.fluxscale1', mylabel+'.Xband'+'.B0'], parang=False, field='1', gainfield=['','1',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.Xband'+'.K0', mylabel+'.Xband'+'.fluxscale1', mylabel+'.Xband'+'.B0'], parang=False, field='2', gainfield=['','1',''], interp=['','linear',''], calwt=False, spw=SPW)
# 
# Repeat for C band
#
SPW = '0~31'
myvis=mylabel+'.Cband.ms'

setjy(vis=myvis, field='0', modimage='3C48_C.im', standard='Perley-Butler 2013', usescratch=False, scalebychan=True, spw='')
gaincal(vis=myvis, caltable=mylabel+'.Cband'+'.G0all', field='0,1', refant='ea05', spw=SPW+':10~50', gaintype='G', calmode='p', solint='int', minsnr=5, append=False)
gaincal(vis=myvis, caltable=mylabel+'.Cband'+'.G0', field='0', refant='ea05', spw=SPW+':10~50', calmode='p', solint='int', minsnr=5)
gaincal(vis=myvis,caltable=mylabel+'.Cband'+'.K0', gaintable=[mylabel+'.Cband'+'.G0'], field='0',spw=SPW+':1~61',gaintype='K', refant='ea05', combine='scan', solint='inf', minsnr=3)

bandpass(vis=myvis,caltable=mylabel+'.Cband'+'.B0', gaintable=[mylabel+'.Cband'+'.G0',mylabel+'.Cband'+'.K0'], field='0', spw=SPW, refant='ea05',solnorm=True, bandtype='B', combine='scan', solint='inf')
gaincal(vis=myvis, caltable=mylabel+'.Cband'+'.G1', gaintable=[mylabel+'.Cband'+'.K0',mylabel+'.Cband'+'.B0'], field='0', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G', calmode='ap', append=False)
gaincal(vis=myvis,caltable=mylabel+'.Cband'+'.G1', gaintable=[mylabel+'.Cband'+'.K0', mylabel+'.Cband'+'.B0'], field='1', refant='ea05', solnorm=False, spw=SPW+':1~61', solint='inf', gaintype='G',calmode='ap', append=True)
myscaleXreal=fluxscale(vis=myvis, caltable=mylabel+'.Cband'+'.G1', fluxtable=mylabel+'.Cband'+'.fluxscale1', reference='0', transfer='1')

applycal(vis=myvis, gaintable=[mylabel+'.Cband'+'.K0', mylabel+'.Cband'+'.fluxscale1', mylabel+'.Cband'+'.B0'], parang=False, field='0', gainfield=['','0',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.Cband'+'.K0', mylabel+'.Cband'+'.fluxscale1', mylabel+'.Cband'+'.B0'], parang=False, field='1', gainfield=['','1',''], interp=['','nearest',''], calwt=False, spw=SPW)
applycal(vis=myvis, gaintable=[mylabel+'.Cband'+'.K0', mylabel+'.Cband'+'.fluxscale1', mylabel+'.Cband'+'.B0'], parang=False, field='2', gainfield=['','1',''], interp=['','linear',''], calwt=False, spw=SPW)
#
# -------------------------------------------------------------------------------
# STEP 3: Imaging
# -------------------------------------------------------------------------------
# 
# The below commands image both C and X band non-interactively
#
# First, split of the calibrated target field:
#
myvis=mylabel+'.Xband.ms'

split(vis=myvis, outputvis=mylabel+'.Xband.split.ms', datacolumn='corrected', field='2')
#
# Image X band:
#
myvis = mylabel+'.Xband.split.ms'

tclean(vis=myvis, imagename=mylabel+'.im1', imsize=2048, cell='0.15arcsec', stokes='I', specmode='mfs',deconvolver='hogbom', robust=1., weighting='briggs', niter=2000, cycleniter=200, interactive=False, threshold='0.025 mJy')
#
# Repeat for C band:
#
myvis=mylabel+'.Cband.ms'

split(vis=myvis, outputvis=mylabel+'.Cband.split.ms', datacolumn='corrected', field='2')
#
# Image C band:
#
myvis = mylabel+'.Cband.split.ms'
tclean(vis=myvis, imagename=mylabel+'.im1', imsize=4096, cell='0.25arcsec', stokes='I', specmode='mfs',deconvolver='hogbom', robust=0., weighting='briggs', niter=4000, cycleniter=200, interactive=False, threshold='0.015 mJy')
#
# -------------------------------------------------------------------------------
# FINISHED
# -------------------------------------------------------------------------------
#








