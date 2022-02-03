import logging, re

from tthAnalysis.HiggsToTauTau.configs.analyzeConfig import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

class analyzeConfig_SVfit4tau(analyzeConfig):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_4l:
    lepton_selection: either `Tight`, `Loose` or `Fakeable`

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.

  """
  def __init__(self,
        configDir,
        localDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        samples,
        lepton_selection,
        hadTau_selection,
        SVfit4tau_logM_wMassConstraint_MarkovChain,
        SVfit4tau_logM_woMassConstraint_MarkovChain,
        SVfit4tau_logM_wMassConstraint_VAMP,
        modes,
        central_or_shifts,
        lep_mva_wp,
        jet_cleaning_by_index,
        gen_matching_by_index,
        max_files_per_job,
        era,
        use_lumi,
        lumi,
        check_output_files,
        running_method,
        num_parallel_jobs,
        verbose = False,
        dry_run = False,
        isDebug = False,
        use_home = False,
        keep_logs = keep_logs,
        submission_cmd = None,
      ):
    analyzeConfig.__init__(self,
      configDir                 = configDir,
      localDir                  = localDir,
      outputDir                 = outputDir,
      executable_analyze        = executable_analyze,
      channel                   = "SVfit4tau",
      samples                   = samples,
      jet_cleaning_by_index     = jet_cleaning_by_index,
      gen_matching_by_index     = gen_matching_by_index,
      central_or_shifts         = central_or_shifts,
      max_files_per_job         = max_files_per_job,
      era                       = era,
      use_lumi                  = use_lumi,
      lumi                      = lumi,
      check_output_files        = check_output_files,
      running_method            = running_method,
      num_parallel_jobs         = num_parallel_jobs,
      histograms_to_fit         = [],
      triggers                  = [],
      lep_mva_wp                = lep_mva_wp,
      verbose                   = verbose,
      dry_run                   = dry_run,
      isDebug                   = isDebug,
      use_home                  = use_home,
      keep_logs                 = keep_logs,
      template_dir              = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'multilepton', 'test', 'templates'),
      submission_cmd            = submission_cmd,
      apply_nc_correction       = None,
    )

    self.lepton_selection = lepton_selection
    self.hadTau_selection = hadTau_selection

    self.SVfit4tau_logM_wMassConstraint_MarkovChain = SVfit4tau_logM_wMassConstraint_MarkovChain
    self.SVfit4tau_logM_woMassConstraint_MarkovChain = SVfit4tau_logM_woMassConstraint_MarkovChain
    self.SVfit4tau_logM_wMassConstraint_VAMP = SVfit4tau_logM_wMassConstraint_VAMP

    self.modes = modes

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)

  def createCfg_analyze(self, jobOptions):
    """Create python configuration file for the analyze_SVfit4tau executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: hh->4tau signal MC sample
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/hhAnalysis/multilepton/bin/analyze_SVfit4tau.cc
    """
    lines = []
    ##lines.append("process.fwliteInput.fileNames = cms.vstring(%s)" % [ os.path.basename(inputFile) for inputFile in jobOptions['ntupleFiles'] ])
    lines.append("process.fwliteInput.fileNames = cms.vstring(%s)" % jobOptions['ntupleFiles'])
    lines.append("process.fwliteOutput.fileName = cms.string('%s')" % os.path.basename(jobOptions['histogramFile']))
    lines.append("process.analyze_SVfit4tau.process = cms.string('%s')" % jobOptions['sample_category'])
    lines.append("process.analyze_SVfit4tau.era = cms.string('%s')" % self.era)
    lines.append("process.analyze_SVfit4tau.mode = cms.string('%s')" % jobOptions['mode'])
    lines.append("process.analyze_SVfit4tau.leptonSelection = cms.string('%s')" % jobOptions['lepton_selection'])
    lines.append("process.analyze_SVfit4tau.hadTauSelection = cms.string('%s')" % jobOptions['hadTau_selection'])
    lines.append("process.analyze_SVfit4tau.SVfit4tau.logM_wMassConstraint_MarkovChain = cms.vdouble(%s)" % jobOptions['SVfit4tau_logM_wMassConstraint_MarkovChain'])
    lines.append("process.analyze_SVfit4tau.SVfit4tau.logM_woMassConstraint_MarkovChain = cms.vdouble(%s)" % jobOptions['SVfit4tau_logM_woMassConstraint_MarkovChain'])
    lines.append("process.analyze_SVfit4tau.SVfit4tau.logM_wMassConstraint_VAMP = cms.vdouble(%s)" % jobOptions['SVfit4tau_logM_wMassConstraint_VAMP'])
    lines.append("process.analyze_SVfit4tau.use_HIP_mitigation_mediumMuonId = cms.bool(%s)" % jobOptions['use_HIP_mitigation_mediumMuonId'])
    lines.append("process.analyze_SVfit4tau.isMC = cms.bool(%s)" % jobOptions['is_mc'])
    lines.append("process.analyze_SVfit4tau.central_or_shift = cms.string('%s')" % jobOptions['central_or_shift'])
    lines.append("process.analyze_SVfit4tau.lumiScale = cms.double(%f)" % jobOptions['lumi_scale'])
    lines.append("process.analyze_SVfit4tau.apply_genWeight = cms.bool(%s)" % jobOptions['apply_genWeight'])
    lines.append("process.analyze_SVfit4tau.fillGenEvtHistograms = cms.bool(True)")
    lines.append("process.analyze_SVfit4tau.isDEBUG = cms.bool(%s)" % self.isDebug)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      process_name = sample_info["process_name_specific"]
      for mode in self.modes:
        key_dir = getKey(process_name, mode)
        for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_RLES, DKEY_SYNC ]:
          if dir_type == DKEY_SYNC and not self.do_sync:
            continue
          initDict(self.dirs, [ key_dir, dir_type ])
          if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
            self.dirs[key_dir][dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel, "_".join([ mode ]), process_name)
          else:
            self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, "_".join([ mode ]), process_name)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT, DKEY_SYNC ]:
      if dir_type == DKEY_SYNC and not self.do_sync:
        continue
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.get_dir_type(dir_type), dir_type, self.channel)
      else:
        self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)
    ##print "self.dirs = ", self.dirs

    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
      else:
        create_if_not_exists(self.dirs[key])

    inputFileLists = {}
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    for mode in self.modes:
      for sample_name, sample_info in self.samples.items():
        if not sample_info["use_it"]:
          continue
        process_name = sample_info["process_name_specific"]
        logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))

        sample_category = sample_info["sample_category"]
        is_mc = (sample_info["type"] == "mc")

        for central_or_shift in self.central_or_shifts:

          inputFileList = inputFileLists[sample_name]
          for jobId in inputFileList.keys():

            # build config files for executing analysis code
            key_dir = getKey(process_name, mode)
            key_analyze_job = getKey(process_name, mode, central_or_shift, jobId)
            ntupleFiles = inputFileList[jobId]
            if len(ntupleFiles) == 0:
              logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
              continue

            self.jobOptions_analyze[key_analyze_job] = {
              'ntupleFiles' : ntupleFiles,
              'cfgFile_modified' : os.path.join(self.dirs[key_dir][DKEY_CFGS], "analyze_%s_%s_%s_%s_%i_cfg.py" % \
                (self.channel, process_name, mode, central_or_shift, jobId)),
              'histogramFile' : os.path.join(self.dirs[key_dir][DKEY_HIST], "%s_%s_%s_%i.root" % \
                (process_name, mode, central_or_shift, jobId)),
              'logFile' : os.path.join(self.dirs[key_dir][DKEY_LOGS], "analyze_%s_%s_%s_%s_%i.log" % \
                (self.channel, process_name, mode, central_or_shift, jobId)),
              'sample_category' : sample_category,
              'mode' : mode,
              'lepton_selection' : self.lepton_selection,
              'hadTau_selection' : self.hadTau_selection,
              'SVfit4tau_logM_wMassConstraint_MarkovChain' : self.SVfit4tau_logM_wMassConstraint_MarkovChain,
              'SVfit4tau_logM_woMassConstraint_MarkovChain' : self.SVfit4tau_logM_woMassConstraint_MarkovChain,
              'SVfit4tau_logM_wMassConstraint_VAMP' : self.SVfit4tau_logM_wMassConstraint_VAMP,
              'use_HIP_mitigation_mediumMuonId' : False,
              'is_mc' : is_mc,
              'central_or_shift' : central_or_shift,
              'lumi_scale' : 1.,
              'apply_genWeight' : sample_info["genWeight"] if (is_mc and "genWeight" in sample_info) else False,
            }
            self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job])

            # initialize input and output file names for hadd_stage1
            key_hadd_stage1 = getKey(process_name, mode)
            if not key_hadd_stage1 in self.inputFiles_hadd_stage1:
              self.inputFiles_hadd_stage1[key_hadd_stage1] = []
            self.inputFiles_hadd_stage1[key_hadd_stage1].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
            self.outputFile_hadd_stage1[key_hadd_stage1] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage1_%s_%s_%s.root" % \
              (self.channel, process_name, mode))

            # initialize input and output file names for hadd_stage2
            key_hadd_stage2 = getKey()
            if not key_hadd_stage2 in self.inputFiles_hadd_stage2:
              self.inputFiles_hadd_stage2[key_hadd_stage2] = []
            self.inputFiles_hadd_stage2[key_hadd_stage2].append(self.outputFile_hadd_stage1[key_hadd_stage1])
            self.outputFile_hadd_stage2[key_hadd_stage2] = os.path.join(self.dirs[DKEY_HIST], "histograms_harvested_stage2_%s.root" % \
              (self.channel))

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_hadd_stage2(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done")

    return self.num_jobs
