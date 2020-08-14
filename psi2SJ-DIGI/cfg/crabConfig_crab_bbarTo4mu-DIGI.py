from CRABClient.UserUtilities import config
from CRABClient.UserUtilities import getUsername
username = getUsername()
config = config()
config.section_('General')
config.General.workArea = 'crab_SPSTo4mu_psi2SJ-DIGI'
config.General.requestName = 'crab_SPSTo4mu_psi2SJ-DIGI'
config.General.transferOutputs = True
config.General.transferLogs=True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'BPH-RunIIAutumn18DRPremix-01798_DPS_cfg.py'
config.JobType.maxMemoryMB = 5000
config.JobType.allowUndistributedCMSSW = True
config.Data.inputDBS = 'phys03'
config.Data.inputDataset = '/SPSTo4mu_psi2SJ/xgao-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-GENSIM-psi2SJto4mu-v2-33d1047b13ecd100745eb841c62eaabb/USER'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 2
config.Data.outputDatasetTag = 'RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-DIGI_psi2SJ'

config.Data.publication = True
#config.Data.outLFNDirBase = '/store/group/l1upgrades/%s/MC2020/Sample_Production/bbarTo4mu/bbarTo4mu-DIGI/'%username
config.Data.outLFNDirBase = '/store/user/xgao/samples-20200813-DiJpsi/psi2SJ-DIGI'
config.section_('User')
config.section_('Site')
#config.Site.storageSite = 'T3_US_FNALLPC'
#config.Site.whitelist = ['T2_US_*']
config.Site.storageSite = 'T2_BE_IIHE'
config.User.voGroup     = 'becms'
