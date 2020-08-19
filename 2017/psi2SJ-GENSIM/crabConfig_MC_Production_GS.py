from CRABClient.UserUtilities import config
#from CRABClient import getUsername
config = config()

config.General.requestName = 'RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-GENSIM-psi2SJto4mu-v2'
config.General.workArea = 'crab_psi2SJ-GENSIM-v2'
config.General.transferOutputs = True
config.General.transferLogs = False

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'my_4muon_qqorggtopsi2sJ.py'
#config.JobType.inputFiles   = ['myBBartoJpsi.dec']
config.Data.outputPrimaryDataset = 'SPSTo4mu_psi2SJ'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 1000
NJOBS = 1000   # This is not a configuration parameter, but an auxiliary variable that we use in the next line.
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS

config.JobType.allowUndistributedCMSSW = True

config.Data.publication = True
#config.Data.outLFNDirBase = '/store/user/%s/Sample_Production/bbarTo4mu/GS/' % (getUsername())
#config.Data.ignoreLocality = True
config.Data.allowNonValidInputDataset = True

#config.section_('User')
#config.section_('Site')
config.Site.storageSite = 'T2_BE_IIHE'

config.User.voGroup     = 'becms'
config.Data.outLFNDirBase = '/store/user/xgao/samples-20200813-DiJpsi/psi2SJ'
