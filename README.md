First of all, you need to setup the enviroment at lxplus
step1:

	cmsrel CMSSW_10_2_5
	cd CMSSW_10_2_5/src
	cmsenv

Then, copy the SPSpsi2SJ for git to the src/:
	git clone git@github.com:fdzyffff/SPSpsi2SJ.git

There are three steps to generate the private full-SIM events.

step1: GENSIM

	cd psi2SJ-GENSIM

	There are 2 scripts (.py file), 
		one name is: "my_4muon_qqorggtopsi2sJ.py", we put generation setting here, such as the process, the filter et al.
		one name is: "crabConfig_MC_Production_GS.py", we use it to submit the job to crab, which mean that the "my_4muon_qqorggtopsi2sJ.py" will be run in the background in the queue.

		1) edit the "my_4muon_qqorggtopsi2sJ.py", make sure it run well locally.
		2) edit the "crabConfig_MC_Production_GS.py", change following variables as you preference:
				config.General.requestName = 'xxx'
				config.General.workArea = 'xxxx'
				config.Data.outputPrimaryDataset = 'xxxx'
			change the number of jobs and number of event to be produced in each job:
				config.Data.splitting = 'EventBased'
				config.Data.unitsPerJob = 100000
				NJOBS = 1000 
				config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
			change the site to run your jobs and change the output path to the destination site where the output files will be stored:
				config.Site.storageSite = 'xxxx'
				config.User.voGroup     = 'xxxx'
				config.Data.outLFNDirBase = 'xxxx'
		3) submit the job with the command:
			crab submit -c crabConfig_MC_Production_GS.py
		4) after submission, you can use following command to check the status:
			crab status -d your_output_name(set in the config.General.workArea)
		5) once the jobs are finished, you can use the "crab status -d /your_crab_workarea" cmd to get the output dataset, it looks like:
			Output dataset:			/bbarTo4mu_13TeV_pythia8_20200701/xgao-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-GENSIM-DPSTo4mu-60d463bda7f67e1183e39467e9418b48/USER

step2: DIGI

	cd psi2SJ-DIGI

	There are 2 scripts (.py file), 
		one name is: "BPH-RunIIAutumn18DRPremix-01798_DPS_cfg.py", we put DIGI setting here, no need to edit.
		one name is: "crabConfig_crab_bbarTo4mu-DIGI.py", we use it to submit the job to crab, which mean that the "BPH-RunIIAutumn18DRPremix-01798_DPS_cfg.py" will be run in the background in the queue.

		1) edit the "crabConfig_crab_bbarTo4mu-DIGI.py, change the "config.Data.inputDataset" to your Output dataset, which can be got in step1-5
		2) change the number of input files and output parameters as you preference:
			config.Data.unitsPerJob = xx (in general, 1 means one DIGI job read one GENSIM file, but DIGI is quite faster than GENSIM, so you can put for example 2 or 5 or even 10. which mean 2 or 5 or 10 GENSIM will be run in one DIGI job and gives one output.root)
			
			config.Data.outputDatasetTag = 'xxx'
			config.Data.outLFNDirBase = 'xxx'

		3) submit the job with the command:
			crab submit -c crabConfig_crab_bbarTo4mu-DIGI.py
		4) after submission, you can use following command to check the status:
			crab status -d your_output_name(set in the config.General.workArea)
		5) once the jobs are finished, you can use the "crab status -d /your_crab_workarea" cmd to get the output dataset, it looks like:
			Output dataset:			/bbarTo4mu_13TeV_pythia8_20200701/xgao-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-GENSIM-DPSTo4mu-60d463bda7f67e1183e39467e9418b48/USER

step3: RECO

	cd psi2SJ-RECO

	There are 2 scripts (.py file), 
		one name is: "BPH-RunIIAutumn18DRPremix-01798_DPS_cfg_2.py", we put RECO setting here, no need to edit.
		one name is: "crabConfig_crab_bbarTo4mu-RECO.py", we use it to submit the job to crab, which mean that the "BPH-RunIIAutumn18DRPremix-01798_DPS_cfg_2.py" will be run in the background in the queue.

		1) edit the "crabConfig_crab_bbarTo4mu-RECO.py", change the "config.Data.inputDataset" to your Output dataset, which can be got in step2-5
		2) change the number of input files and output parameters as you preference:
			config.Data.unitsPerJob = xx 
			config.Data.outputDatasetTag = 'xxx'
			config.Data.outLFNDirBase = 'xxx'
		3) submit the job with the command:
			crab submit -c crabConfig_crab_bbarTo4mu-RECO.py
		4) after submission, you can use following command to check the status:
			crab status -d your_output_name(set in the config.General.workArea)
		5) once the jobs are finished, you can use the "crab status -d /your_crab_workarea" cmd to get the output dataset, it looks like:
			Output dataset:			/bbarTo4mu_13TeV_pythia8_20200701/xgao-crab_RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1-GENSIM-DPSTo4mu-60d463bda7f67e1183e39467e9418b48/USER