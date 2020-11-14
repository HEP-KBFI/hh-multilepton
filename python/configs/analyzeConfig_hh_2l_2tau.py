import logging
import re

from hhAnalysis.multilepton.configs.analyzeConfig_hh import *
from tthAnalysis.HiggsToTauTau.jobTools import create_if_not_exists
from tthAnalysis.HiggsToTauTau.analysisTools import initDict, getKey, create_cfg, createFile, generateInputFileList

def get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight):
  lepton_and_hadTau_selection_and_frWeight = lepton_and_hadTau_selection
  if lepton_and_hadTau_selection.startswith("Fakeable"):
    if lepton_and_hadTau_frWeight == "enabled":
      lepton_and_hadTau_selection_and_frWeight += "_wFakeRateWeights"
    elif lepton_and_hadTau_frWeight == "disabled":
      lepton_and_hadTau_selection_and_frWeight += "_woFakeRateWeights"
  lepton_and_hadTau_selection_and_frWeight = lepton_and_hadTau_selection_and_frWeight.replace("|", "_")
  return lepton_and_hadTau_selection_and_frWeight

def getHistogramDir(category, lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight, leptonChargeSelection, hadTau_charge_selection, chargeSumSelection):
  histogramDir = category
  if leptonChargeSelection != "disabled":
    histogramDir += "_lep%s" % leptonChargeSelection
  if hadTau_charge_selection != "disabled":
    histogramDir += "_hadTau%s" % hadTau_charge_selection
  histogramDir += "_sum%s_%s" % (chargeSumSelection, lepton_selection)
  if lepton_selection.find("Fakeable") != -1 or hadTau_selection.find("Fakeable") != -1:
    if lepton_and_hadTau_frWeight == "enabled":
      histogramDir += "_wFakeRateWeights"
    elif lepton_and_hadTau_frWeight == "disabled":
      histogramDir += "_woFakeRateWeights"
  return histogramDir

class analyzeConfig_hh_2l_2tau(analyzeConfig_hh):
  """Configuration metadata needed to run analysis in a single go.

  Sets up a folder structure by defining full path names; no directory creation is delegated here.

  Args specific to analyzeConfig_hh_2l_2tau:
    hadTau_selection: either `Tight`, `Loose` or `Fakeable`
    hadTau_charge_selection: either `OS` or `SS` (opposite-sign or same-sign)

  See $CMSSW_BASE/src/tthAnalysis/HiggsToTauTau/python/analyzeConfig.py
  for documentation of further Args.

  """
  def __init__(self,
        configDir,
        outputDir,
        executable_analyze,
        cfgFile_analyze,
        samples,
        leptonChargeSelections,
        hadTau_selection,
        hadTau_charge_selections,
        applyFakeRateWeights,
        chargeSumSelections,
        central_or_shifts,
        lep_mva_wp,
        jet_cleaning_by_index,
        gen_matching_by_index,
        max_files_per_job,
        era,
        use_lumi,
        lumi,
        invert_ZbosonMassVeto,
        check_output_files,
        running_method,
        num_parallel_jobs,
        executable_addBackgrounds,
        executable_addBackgroundJetToTauFakes,
        executable_addFlips,
        histograms_to_fit,
        select_rle_output = False,
        verbose           = False,
        dry_run           = False,
        isDebug           = False,
        use_nonnominal    = False,
        hlt_filter        = False,
        use_home          = False,
        submission_cmd    = None,
      ):
    analyzeConfig_hh.__init__(self,
      configDir             = configDir,
      outputDir             = outputDir,
      executable_analyze    = executable_analyze,
      channel               = "hh_2l_2tau",
      samples               = samples,
      jet_cleaning_by_index = jet_cleaning_by_index,
      gen_matching_by_index = gen_matching_by_index,
      central_or_shifts     = central_or_shifts,
      max_files_per_job     = max_files_per_job,
      era                   = era,
      use_lumi              = use_lumi,
      lumi                  = lumi,
      check_output_files    = check_output_files,
      running_method        = running_method,
      num_parallel_jobs     = num_parallel_jobs,
      histograms_to_fit     = histograms_to_fit,
      triggers              = [ '1e', '1mu', '2e', '2mu', '1e1mu' ],
      lep_mva_wp            = lep_mva_wp,
      verbose               = verbose,
      dry_run               = dry_run,
      isDebug               = isDebug,
      use_home              = use_home,
      template_dir          = os.path.join(os.getenv('CMSSW_BASE'), 'src', 'hhAnalysis', 'multilepton', 'test', 'templates'),
      submission_cmd        = submission_cmd,
      use_dymumu_tau_fr     = True,
      apply_nc_correction   = False,
    )

    self.invert_ZbosonMassVeto = invert_ZbosonMassVeto
    self.lepton_and_hadTau_selections = [ "Tight", "Fakeable" ]
    self.lepton_and_hadTau_frWeights = [ "enabled", "disabled" ]
    self.hadTau_selection_part2 = hadTau_selection
    self.applyFakeRateWeights = applyFakeRateWeights
    self.leptonChargeSelections = leptonChargeSelections
    self.hadTau_charge_selections = hadTau_charge_selections

    self.lepton_genMatches = [ "2l2f0g0j", "2l1f0g0j", "2l0f0g0j", "1l1f1g0j", "1l1f0g1j", "1l0f1g0j", "1l0f0g1j", "0l0f2g0j", "0l0f1g1j", "0l0f0g2j" ]
    self.hadTau_genMatches = [ "2t0e0m0j", "1t1e0m0j", "1t0e1m0j", "1t0e0m1j", "0t2e0m0j", "0t1e1m0j", "0t1e0m1j", "0t0e2m0j", "0t0e1m1j", "0t0e0m2j" ]
  
    self.apply_leptonGenMatching = None
    self.apply_hadTauGenMatching = None
    if self.applyFakeRateWeights == "4L":
      self.apply_leptonGenMatching = True
      self.apply_hadTauGenMatching = True
      if self.run_mcClosure:
        self.lepton_and_hadTau_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m", "Fakeable_mcClosure_t" ])
      self.central_or_shifts_fr = systematics.FR_all
    elif applyFakeRateWeights == "2lepton":
      self.apply_leptonGenMatching = True
      self.apply_hadTauGenMatching = False
      if self.run_mcClosure:
        self.lepton_and_hadTau_selections.extend([ "Fakeable_mcClosure_e", "Fakeable_mcClosure_m" ])
      # in this regime data-to-MC SFs of jet-to-tau FR are applied and therefore the relevant systematics have to be preserved
      self.central_or_shifts_fr = systematics.FR_all
    elif applyFakeRateWeights == "2tau":
      self.apply_leptonGenMatching = False
      self.apply_hadTauGenMatching = True
      if self.run_mcClosure:
        self.lepton_and_hadTau_selections.extend([ "Fakeable_mcClosure_t" ])
      self.central_or_shifts_fr = systematics.FR_t
    else:
      raise ValueError("Invalid Configuration parameter 'applyFakeRateWeights' = %s !!" % applyFakeRateWeights)
    self.pruneSystematics()
    self.internalizeSystematics()

    self.chargeSumSelections = chargeSumSelections

    self.executable_addBackgrounds = executable_addBackgrounds
    self.executable_addFakes = executable_addBackgroundJetToTauFakes
    self.executable_addFlips = executable_addFlips

    self.nonfake_backgrounds = [ "ZZ", "WZ", "WW", "TT", "TTW", "TTWW", "TTZ", "DY", "W", "Other", "VH", "TH", "TTH", "TTWH", "TTZH", "ggH", "qqH" ] 

    self.cfgFile_analyze = os.path.join(self.template_dir, cfgFile_analyze)
    self.inputFiles_hadd_stage1_6 = {}
    self.outputFile_hadd_stage1_6 = {}
    self.cfgFile_addFlips = os.path.join(self.template_dir, "addBackgroundLeptonFlips_cfg.py")
    self.jobOptions_addFlips = {}
    self.histogramDir_prep_dcard = "hh_2l_2tau_sumOS_Tight"
    self.make_plots_backgrounds = ["DY", "ZZ", "WZ", "WW", "TT", "TTW", "TTZ", "Other", "VH", "TTH", "TH", "TTWW", "W" ] + [ "Convs", "data_fakes", "flips_mc" ]
    self.cfgFile_make_plots = os.path.join(self.template_dir, "makePlots_hh_2l_2tau_cfg.py")
    self.cfgFile_make_plots_mcClosure = os.path.join(self.template_dir, "makePlots_mcClosure_hh_2l_2tau_cfg.py")

    self.select_rle_output = select_rle_output
    self.use_nonnominal = use_nonnominal
    self.hlt_filter = hlt_filter

    self.categories = [
      "hh_2l_2tau", 
      #"hh_2lSS_2tau", 
      #"hh_2lOS_2tau", 
      "hh_2e_2tau", 
      "hh_1e1mu_2tau", 
      "hh_2mu_2tau",
      #"hh_2eSS_2tau", 
      #"hh_2eOS_2tau", 
      #"hh_1e1muSS_2tau", 
      #"hh_1e1muOS_2tau", 
      #"hh_2muSS_2tau", 
      #"hh_2muOS_2tau",
      #"hh_2lOS_2tau_wChargeFlipWeights", 
      #"hh_2eOS_2tau_wChargeFlipWeights", 
      #"hh_2muOS_2tau_wChargeFlipWeights", 
      #"hh_1e1muOS_2tau_wChargeFlipWeights"
    ]  ## N.B.: Inclusive category is a member of this list 
    self.category_inclusive = "hh_2l_2tau"

  def set_BDT_training(self, hadTau_selection_relaxed):
    """Run analysis with loose selection criteria for leptons and hadronic taus,
       for the purpose of preparing event list files for BDT training.
    """
    self.lepton_and_hadTau_selections = [ "forBDTtraining" ]
    self.lepton_and_hadTau_frWeights  = [ "disabled" ]
    super(analyzeConfig_hh_2l_2tau, self).set_BDT_training(hadTau_selection_relaxed)

  def createCfg_analyze(self, jobOptions, sample_info, lepton_and_hadTau_selection):
    """Create python configuration file for the analyze_hh_2l_2tau executable (analysis code)

    Args:
      inputFiles: list of input files (Ntuples)
      outputFile: output file of the job -- a ROOT file containing histogram
      process: either `TT`, `TTW`, `TTZ`, `EWK`, `Rares`, `data_obs`, or `signal`
      is_mc: flag indicating whether job runs on MC (True) or data (False)
      lumi_scale: event weight (= xsection * luminosity / number of events)
      central_or_shift: either 'central' or one of the systematic uncertainties defined in $CMSSW_BASE/src/hhAnalysis/multilepton/bin/analyze_hh_2l_2tau.cc
    """
    lepton_and_hadTau_frWeight = "disabled" if jobOptions['applyFakeRateWeights'] == "disabled" else "enabled"

    jobOptions['histogramDir'] = getHistogramDir(self.category_inclusive,
      lepton_and_hadTau_selection, jobOptions['hadTauSelection'], lepton_and_hadTau_frWeight,
      jobOptions['leptonChargeSelection'], jobOptions['hadTauChargeSelection'], jobOptions['chargeSumSelection']
    )
    if 'mcClosure' in lepton_and_hadTau_selection:
      self.mcClosure_dir['%s_%s_%s' % (lepton_and_hadTau_selection, jobOptions['chargeSumSelection'], jobOptions['hadTauChargeSelection'])] = jobOptions['histogramDir']

    self.set_leptonFakeRateWeightHistogramNames(jobOptions['central_or_shift'], lepton_and_hadTau_selection)
    jobOptions['leptonFakeRateWeight.inputFileName'] = self.leptonFakeRateWeight_inputFile
    jobOptions['leptonFakeRateWeight.histogramName_e'] = self.leptonFakeRateWeight_histogramName_e
    jobOptions['leptonFakeRateWeight.histogramName_mu'] = self.leptonFakeRateWeight_histogramName_mu
    jobOptions['hadTauFakeRateWeight.inputFileName'] = self.hadTauFakeRateWeight_inputFile
    graphName = 'jetToTauFakeRate/%s/$etaBin/jetToTauFakeRate_mc_hadTaus_pt' % self.hadTau_selection_part2
    jobOptions['hadTauFakeRateWeight.lead.graphName'] = graphName
    jobOptions['hadTauFakeRateWeight.sublead.graphName'] = graphName
    fitFunctionName = 'jetToTauFakeRate/%s/$etaBin/fitFunction_data_div_mc_hadTaus_pt' % self.hadTau_selection_part2
    jobOptions['hadTauFakeRateWeight.lead.fitFunctionName'] = fitFunctionName
    jobOptions['hadTauFakeRateWeight.sublead.fitFunctionName'] = fitFunctionName
    if "mcClosure" in lepton_and_hadTau_selection:
      jobOptions['hadTauFakeRateWeight.applyGraph_lead'] = True
      jobOptions['hadTauFakeRateWeight.applyGraph_sublead'] = True
      jobOptions['hadTauFakeRateWeight.applyFitFunction_lead'] = False
      jobOptions['hadTauFakeRateWeight.applyFitFunction_sublead'] = False
      if self.applyFakeRateWeights not in [ "4L", "2tau" ] and not self.isBDTtraining:
        # We want to preserve the same logic as running in SR and applying the FF method only to leptons [*]
        jobOptions['hadTauFakeRateWeight.applyFitFunction_lead'] = True
        jobOptions['hadTauFakeRateWeight.applyFitFunction_sublead'] = True
    if jobOptions['hadTauSelection'].find("Tight") != -1 and self.applyFakeRateWeights not in [ "4L", "2tau" ] and not self.isBDTtraining:
      # [*] SR and applying the FF method only to leptons
      jobOptions['hadTauFakeRateWeight.applyGraph_lead'] = False # FR in MC for the leading tau
      jobOptions['hadTauFakeRateWeight.applyGraph_sublead'] = False
      jobOptions['hadTauFakeRateWeight.applyFitFunction_lead'] = True # data-to-MC SF for the leading tau
      jobOptions['hadTauFakeRateWeight.applyFitFunction_sublead'] = True
      jobOptions['apply_hadTauFakeRateSF'] = True

    lines = super(analyzeConfig_hh_2l_2tau, self).createCfg_analyze(jobOptions, sample_info)
    lines.append("process.analyze_hh_2l_2tau.invert_ZbosonMassVeto   = cms.bool(%s)" % self.invert_ZbosonMassVeto)
    create_cfg(self.cfgFile_analyze, jobOptions['cfgFile_modified'], lines)


  def addToMakefile_backgrounds_from_data_withFlips(self, lines_makefile, make_target = "phony_addFlips", make_dependency = "phony_hadd_stage1"):
     self.addToMakefile_addBackgrounds(lines_makefile, "phony_addBackgrounds", "phony_hadd_stage1", self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
     self.addToMakefile_hadd_stage1_5(lines_makefile, "phony_hadd_stage1_5", "phony_addBackgrounds")
     self.addToMakefile_addBackgrounds(lines_makefile, "phony_addBackgrounds_sum", "phony_hadd_stage1_5", self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
     self.addToMakefile_addFakes(lines_makefile, "phony_addFakes", "phony_hadd_stage1_5")
     self.addToMakefile_hadd_stage1_6(lines_makefile, "phony_hadd_stage1_6", "phony_addFakes")
     self.addToMakefile_addFlips(lines_makefile, "phony_addFlips", "phony_hadd_stage1_6")
     if make_target != "phony_addFlips":
       lines_makefile.append("%s: %s" % (make_target, "phony_addFlips"))
       lines_makefile.append("")
     self.make_dependency_hadd_stage2 = " ".join([ "phony_addBackgrounds_sum", make_target])

  def accept_systematics(self, central_or_shift, is_mc, lepton_and_hadTau_selection, chargeSumSelection, sample_info):
    if central_or_shift != "central":
      isFR_shape_shift = (central_or_shift in self.central_or_shifts_fr)
      if not ((lepton_and_hadTau_selection == "Fakeable" and isFR_shape_shift) or lepton_and_hadTau_selection == "Tight"):
        return False
      if isFR_shape_shift and lepton_and_hadTau_selection == "Tight" and \
          not (self.applyFakeRateWeights == "2lepton" and central_or_shift in systematics.FR_t and is_mc):
        # If the FRs are applied only to the leptons, the tau FR is compensated with data-to-MC SF, even in the SR
        return False
      if not is_mc and not isFR_shape_shift:
        return False
      if not self.accept_central_or_shift(central_or_shift, sample_info):
        return False
    return True

  def create(self):
    """Creates all necessary config files and runs the complete analysis workfow -- either locally or on the batch system
    """

    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue

      sample_category = sample_info["sample_category"]
      is_mc = (sample_info["type"] == "mc")
      process_name = sample_info["process_name_specific"]

      logging.info("Building dictionaries for sample %s..." % process_name)
      for leptonChargeSelection in self.leptonChargeSelections:
        for hadTau_charge_selection in self.hadTau_charge_selections:
          for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
            for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
              if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
                continue
              if lepton_and_hadTau_frWeight == "disabled" and not lepton_and_hadTau_selection in [ "Tight", "forBDTtraining" ]:
                continue

              lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)
              for chargeSumSelection in self.chargeSumSelections:
                central_or_shift_extensions = ["", "hadd", "addBackgrounds"]
                central_or_shift_dedicated = self.central_or_shifts if self.runTHweights(sample_info) else self.central_or_shifts_external
                central_or_shifts_extended = central_or_shift_extensions + central_or_shift_dedicated
                for central_or_shift_or_dummy in central_or_shifts_extended:
                  process_name_extended = [ process_name, "hadd" ]
                  for process_name_or_dummy in process_name_extended:
                    if central_or_shift_or_dummy in [ "hadd", "addBackgrounds" ] and process_name_or_dummy in [ "hadd" ]:
                      continue

                    if central_or_shift_or_dummy not in central_or_shift_extensions and not self.accept_systematics(
                        central_or_shift_or_dummy, is_mc, lepton_and_hadTau_selection, chargeSumSelection, sample_info
                    ):
                      continue

                    key_dir = getKey(process_name_or_dummy, leptonChargeSelection, hadTau_charge_selection,
                      lepton_and_hadTau_selection_and_frWeight, chargeSumSelection, central_or_shift_or_dummy)
                    lepton_and_hadTau_charge_selection = ""
                    if leptonChargeSelection != "disabled":
                      lepton_and_hadTau_charge_selection += "_lep%s" % leptonChargeSelection
                    if hadTau_charge_selection != "disabled":
                      lepton_and_hadTau_charge_selection += "_hadTau%s" % hadTau_charge_selection
                    lepton_and_hadTau_charge_selection += "_sum%s" % chargeSumSelection
                    for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_RLES, DKEY_SYNC ]:
                      if dir_type == DKEY_SYNC and not self.do_sync:
                        continue
                      initDict(self.dirs, [ key_dir, dir_type ])
                      if dir_type in [ DKEY_CFGS, DKEY_LOGS ]:
                        self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel,
                          "_".join([ lepton_and_hadTau_selection_and_frWeight + lepton_and_hadTau_charge_selection ]), process_name_or_dummy, central_or_shift_or_dummy)
                      else:
                        self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel,
                          "_".join([ lepton_and_hadTau_selection_and_frWeight + lepton_and_hadTau_charge_selection ]), process_name_or_dummy, central_or_shift_or_dummy)

    for subdirectory in [ "addBackgrounds", "addBackgroundLeptonFakes", "addBackgroundLeptonFlips", "prepareDatacards", "addSystFakeRates", "makePlots" ]:
      key_dir = getKey(subdirectory)
      for dir_type in [ DKEY_CFGS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
        initDict(self.dirs, [ key_dir, dir_type ])
        if dir_type in [ DKEY_CFGS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT ]:
          self.dirs[key_dir][dir_type] = os.path.join(self.configDir, dir_type, self.channel, subdirectory)
        else:
          self.dirs[key_dir][dir_type] = os.path.join(self.outputDir, dir_type, self.channel, subdirectory)
    for dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_HIST, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT, DKEY_SYNC ]:
      if dir_type == DKEY_SYNC and not self.do_sync:
        continue
      initDict(self.dirs, [ dir_type ])
      if dir_type in [ DKEY_CFGS, DKEY_SCRIPTS, DKEY_LOGS, DKEY_DCRD, DKEY_PLOT, DKEY_HADD_RT ]:
        self.dirs[dir_type] = os.path.join(self.configDir, dir_type, self.channel)
      else:
        self.dirs[dir_type] = os.path.join(self.outputDir, dir_type, self.channel)

    numDirectories = 0
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        numDirectories += len(self.dirs[key])
      else:
        numDirectories += 1
    logging.info("Creating directory structure (numDirectories = %i)" % numDirectories)
    numDirectories_created = 0;
    frac = 1
    for key in self.dirs.keys():
      if type(self.dirs[key]) == dict:
        for dir_type in self.dirs[key].keys():
          create_if_not_exists(self.dirs[key][dir_type])
        numDirectories_created += len(self.dirs[key])
      else:
        create_if_not_exists(self.dirs[key])
        numDirectories_created = numDirectories_created + 1
      while 100*numDirectories_created >= frac*numDirectories:
        logging.info(" %i%% completed" % frac)
        frac = frac + 1
    logging.info("Done.")        

    inputFileLists = {}
    for sample_name, sample_info in self.samples.items():
      if not sample_info["use_it"]:
        continue
      logging.info("Checking input files for sample %s" % sample_info["process_name_specific"])
      inputFileLists[sample_name] = generateInputFileList(sample_info, self.max_files_per_job)

    for leptonChargeSelection in self.leptonChargeSelections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        for lepton_and_hadTau_selection in self.lepton_and_hadTau_selections:
          lepton_selection = lepton_and_hadTau_selection
          hadTau_selection = lepton_and_hadTau_selection
          electron_selection = lepton_selection
          muon_selection = lepton_selection

          if self.applyFakeRateWeights == "2tau":
            lepton_selection = "Tight"
            electron_selection = "Tight"
            muon_selection = "Tight"
          elif self.applyFakeRateWeights == "2lepton":
            hadTau_selection = "Tight"
          hadTau_selection = "|".join([ hadTau_selection, self.hadTau_selection_part2 ])

          if "forBDTtraining" in lepton_and_hadTau_selection :
            electron_selection = "Loose"
            muon_selection = "Loose"
            hadTau_selection = "Tight|%s" % self.hadTau_selection_relaxed
          elif lepton_and_hadTau_selection == "Fakeable_mcClosure_e":
            electron_selection = "Fakeable"
            muon_selection = "Tight"
            hadTau_selection = "Tight"
            hadTau_selection = "|".join([hadTau_selection, self.hadTau_selection_part2])
          elif lepton_and_hadTau_selection == "Fakeable_mcClosure_m":
            electron_selection = "Tight"
            muon_selection = "Fakeable"
            hadTau_selection = "Tight"
            hadTau_selection = "|".join([hadTau_selection, self.hadTau_selection_part2])
          elif lepton_and_hadTau_selection == "Fakeable_mcClosure_t":
            electron_selection = "Tight"
            muon_selection = "Tight"
            hadTau_selection = "Fakeable"
            hadTau_selection = "|".join([hadTau_selection, self.hadTau_selection_part2])

          for lepton_and_hadTau_frWeight in self.lepton_and_hadTau_frWeights:
            if lepton_and_hadTau_frWeight == "enabled" and not lepton_and_hadTau_selection.startswith("Fakeable"):
              continue
            if lepton_and_hadTau_frWeight == "disabled" and not lepton_and_hadTau_selection in [ "Tight", "forBDTtraining" ]:
              continue
            lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_selection, lepton_and_hadTau_frWeight)

            for chargeSumSelection in self.chargeSumSelections:

              for sample_name, sample_info in self.samples.items():
                if not sample_info["use_it"]:
                  continue
                process_name = sample_info["process_name_specific"]
                logging.info("Creating configuration files to run '%s' for sample %s" % (self.executable_analyze, process_name))
                inputFileList = inputFileLists[sample_name]

                sample_category = sample_info["sample_category"]
                is_mc = (sample_info["type"] == "mc")
                use_th_weights = self.runTHweights(sample_info)

                central_or_shift_dedicated = self.central_or_shifts if use_th_weights else self.central_or_shifts_external
                for central_or_shift in central_or_shift_dedicated:
                  if not self.accept_systematics(
                      central_or_shift, is_mc, lepton_and_hadTau_selection, chargeSumSelection, sample_info
                  ):
                    continue

                  central_or_shifts_local = []
                  if central_or_shift == "central" and not use_th_weights:
                    for central_or_shift_local in self.central_or_shifts_internal:
                      if self.accept_systematics(
                          central_or_shift_local, is_mc, lepton_and_hadTau_selection, chargeSumSelection, sample_info
                      ):
                        central_or_shifts_local.append(central_or_shift_local)

                  logging.info(" ... for '%s' and systematic uncertainty option '%s'" % (lepton_and_hadTau_selection_and_frWeight, central_or_shift))

                  # build config files for executing analysis code
                  key_analyze_dir = getKey(process_name, leptonChargeSelection, hadTau_charge_selection,
                    lepton_and_hadTau_selection_and_frWeight, chargeSumSelection, central_or_shift)

                  for jobId in inputFileList.keys():
                    
                    analyze_job_tuple = (process_name, leptonChargeSelection, hadTau_charge_selection,
                      lepton_and_hadTau_selection_and_frWeight, chargeSumSelection, central_or_shift, jobId)
                    key_analyze_job = getKey(*analyze_job_tuple)
                    ntupleFiles = inputFileList[jobId]
                    if len(ntupleFiles) == 0:
                      logging.warning("No input ntuples for %s --> skipping job !!" % (key_analyze_job))
                      continue

                    cfgFile_modified_path = os.path.join(self.dirs[key_analyze_dir][DKEY_CFGS], "analyze_%s_%s_%s_%s_%s_%s_%i_cfg.py" % analyze_job_tuple)
                    logFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_LOGS], "analyze_%s_%s_%s_%s_%s_%s_%i.log" % analyze_job_tuple)
                    rleOutputFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_RLES], "rle_%s_%s_%s_%s_%s_%s_%i.txt" % analyze_job_tuple) \
                                         if self.select_rle_output else ""
                    histogramFile_path = os.path.join(self.dirs[key_analyze_dir][DKEY_HIST], "analyze_%s_%s_%s_%s_%s_%s_%i.root" % analyze_job_tuple)
                    applyFakeRateWeights = self.applyFakeRateWeights  \
                      if self.isBDTtraining or not (lepton_selection == "Tight" and hadTau_selection.find("Tight") != -1) \
                      else "disabled"

                    self.jobOptions_analyze[key_analyze_job] = {
                      'ntupleFiles'              : ntupleFiles,
                      'cfgFile_modified'         : cfgFile_modified_path,
                      'histogramFile'            : histogramFile_path,
                      'logFile'                  : logFile_path,
                      'selEventsFileName_output' : rleOutputFile_path,
                      'leptonChargeSelection'    : leptonChargeSelection,
                      'electronSelection'        : electron_selection,
                      'muonSelection'            : muon_selection,
                      'apply_leptonGenMatching'  : self.apply_leptonGenMatching,
                      'hadTauChargeSelection'    : hadTau_charge_selection,
                      'hadTauSelection'          : hadTau_selection,
                      'apply_hadTauGenMatching'  : self.apply_hadTauGenMatching,
                      'chargeSumSelection'       : chargeSumSelection,
                      'applyFakeRateWeights'     : applyFakeRateWeights,
                      'central_or_shift'         : central_or_shift,
                      'central_or_shifts_local'  : central_or_shifts_local,
                      'apply_hlt_filter'         : self.hlt_filter,
                      'useNonNominal'            : self.use_nonnominal,
                      'selectBDT'                : self.isBDTtraining,
                      'fillGenEvtHistograms'     : True,
                    }
                    self.createCfg_analyze(self.jobOptions_analyze[key_analyze_job], sample_info, lepton_and_hadTau_selection)

                    # initialize input and output file names for hadd_stage1
                    key_hadd_stage1_dir = getKey(process_name, leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                    hadd_stage1_job_tuple = (process_name, leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                    key_hadd_stage1_job = getKey(*hadd_stage1_job_tuple)
                    if not key_hadd_stage1_job in self.inputFiles_hadd_stage1:
                      self.inputFiles_hadd_stage1[key_hadd_stage1_job] = []
                    self.inputFiles_hadd_stage1[key_hadd_stage1_job].append(self.jobOptions_analyze[key_analyze_job]['histogramFile'])
                    self.outputFile_hadd_stage1[key_hadd_stage1_job] = os.path.join(self.dirs[key_hadd_stage1_dir][DKEY_HIST],
                                                                                    "hadd_stage1_%s_%s_%s_%s_%s.root" % hadd_stage1_job_tuple)

                if self.isBDTtraining:
                  continue

                # add output files of hadd_stage1 to list of input files for hadd_stage1_5
                key_hadd_stage1_job = getKey(process_name, leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                key_hadd_stage1_5_dir = getKey("hadd", leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                hadd_stage1_5_job_tuple = (leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                key_hadd_stage1_5_job = getKey(*hadd_stage1_5_job_tuple)
                if not key_hadd_stage1_5_job in self.inputFiles_hadd_stage1_5:
                  self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job] = []
                self.inputFiles_hadd_stage1_5[key_hadd_stage1_5_job].append(self.outputFile_hadd_stage1[key_hadd_stage1_job])
                self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job] = os.path.join(self.dirs[key_hadd_stage1_5_dir][DKEY_HIST],
                                                                            "hadd_stage1_5_%s_%s_%s_%s.root" % hadd_stage1_5_job_tuple)

              if self.isBDTtraining:
                continue

              # sum fake background contributions for the total of all MC sample
              # input processes: TT_fake, TTW_fake, TTWW_fake, ...
              # output process: fakes_mc
              key_hadd_stage1_5_job = getKey(leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_addBackgrounds_dir = getKey("addBackgrounds")
              addBackgrounds_job_fakes_tuple = ("fakes_mc", leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_addBackgrounds_job_fakes = getKey(*addBackgrounds_job_fakes_tuple)
              sample_categories = []
              sample_categories.extend(self.nonfake_backgrounds)
              processes_input = []
              for sample_category in sample_categories:
                processes_input.append("%s_fake" % sample_category)
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
                'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_%s_cfg.py" % addBackgrounds_job_fakes_tuple),
                'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s_%s_%s.root" % addBackgrounds_job_fakes_tuple),
                'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s_%s_%s.log" % addBackgrounds_job_fakes_tuple),
                'categories' : [ getHistogramDir(category, lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight,
                  leptonChargeSelection, hadTau_charge_selection, chargeSumSelection) for category in self.categories ],
                'processes_input' : processes_input,
                'process_output' : "fakes_mc"
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes])

              # sum fake background contributions for the total of all MC sample
              # input processes: TT_flip, TTW_flip, TTWW_flip, ...
              # output process: flips_mc
              addBackgrounds_job_flips_tuple = ("flips_mc", leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_addBackgrounds_job_flips = getKey(*addBackgrounds_job_flips_tuple)
              sample_categories = []
              sample_categories.extend(self.nonfake_backgrounds)
              processes_input = []
              for sample_category in sample_categories:
                processes_input.append("%s_flip" % sample_category)
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_flips] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],                
                'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_%s_cfg.py" % addBackgrounds_job_flips_tuple),
                'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s_%s_%s.root" % addBackgrounds_job_flips_tuple),
                'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s_%s_%s.log" % addBackgrounds_job_flips_tuple),
                'categories' : [ getHistogramDir(category, lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight,
                  leptonChargeSelection, hadTau_charge_selection, chargeSumSelection) for category in self.categories ],
                'processes_input' : processes_input,
                'process_output' : "flips_mc"
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_flips])

              # sum conversion background contributions for the total of all MC sample
              # input processes: TT_Convs, TTW_Convs, TTWW_Convs, ...
              # output process: Convs
              addBackgrounds_job_Convs_tuple = ("Convs", leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_addBackgrounds_job_Convs = getKey(*addBackgrounds_job_Convs_tuple)
              sample_categories = []
              sample_categories.extend(self.nonfake_backgrounds)
              processes_input = []
              for sample_category in self.convs_backgrounds:
                processes_input.append("%s_Convs" % sample_category)
              self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs] = {
                'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
                'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_%s_cfg.py" % addBackgrounds_job_Convs_tuple),
                'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s_%s_%s.root" % addBackgrounds_job_Convs_tuple),
                'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s_%s_%s.log" % addBackgrounds_job_Convs_tuple),
                'categories' : [ getHistogramDir(category,  lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight,
                  leptonChargeSelection, hadTau_charge_selection, chargeSumSelection) for category in self.categories ],
                'processes_input' : processes_input,
                'process_output' : "Convs"
              }
              self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs])

              # sum signal contributions from HH->4tau ("tttt"), HH->2W2tau ("wwtt"), and HH->4W ("wwww"),
              # separately for "nonfake" and "fake" contributions
              genMatch_categories = [ "nonfake", "fake" ]
              for genMatch_category in genMatch_categories:
                for signal_base, signal_input in self.signal_io.items():
                  addBackgrounds_job_signal_tuple = (leptonChargeSelection, hadTau_charge_selection,
                    lepton_and_hadTau_selection_and_frWeight, chargeSumSelection, signal_base, genMatch_category)
                  key_addBackgrounds_job_signal = getKey(*addBackgrounds_job_signal_tuple)
                  if key_addBackgrounds_job_signal in self.jobOptions_addBackgrounds_sum.keys():
                    continue
                  processes_input = signal_input
                  process_output = signal_base
                  if genMatch_category == "fake":
                    processes_input = [ process_input + "_fake" for process_input in processes_input ]
                    process_output += "_fake"
                  self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal] = {
                    'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
                    'cfgFile_modified' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_CFGS], "addBackgrounds_%s_%s_%s_%s_%s_%s_cfg.py" % addBackgrounds_job_signal_tuple),
                    'outputFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_HIST], "addBackgrounds_%s_%s_%s_%s_%s_%s.root" % addBackgrounds_job_signal_tuple),
                    'logFile' : os.path.join(self.dirs[key_addBackgrounds_dir][DKEY_LOGS], "addBackgrounds_%s_%s_%s_%s_%s_%s.log" % addBackgrounds_job_signal_tuple),
                    'categories' : [ getHistogramDir(category, lepton_selection, hadTau_selection, lepton_and_hadTau_frWeight,
                                       leptonChargeSelection, hadTau_charge_selection, chargeSumSelection) for category in self.categories ],
                    'processes_input' : processes_input,
                    'process_output' : process_output
                  }
                  self.createCfg_addBackgrounds(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal])
                  key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                  if not key_hadd_stage2_job in self.inputFiles_hadd_stage2:
                    self.inputFiles_hadd_stage2[key_hadd_stage2_job] = []
                  if lepton_and_hadTau_selection == "Tight":
                    self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_signal]['outputFile'])

              # initialize input and output file names for hadd_stage2
              key_hadd_stage1_5_job = getKey(leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_hadd_stage2_dir = getKey("hadd", leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              hadd_stage2_job_tuple = (leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
              key_hadd_stage2_job = getKey(*hadd_stage2_job_tuple)
              if not key_hadd_stage2_job in self.inputFiles_hadd_stage2:
                self.inputFiles_hadd_stage2[key_hadd_stage2_job] = []
              if lepton_and_hadTau_selection == "Tight":
                self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'])
                self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_flips]['outputFile'])
                self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_Convs]['outputFile'])              
              self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job])
              self.outputFile_hadd_stage2[key_hadd_stage2_job] = os.path.join(self.dirs[key_hadd_stage2_dir][DKEY_HIST],
                                                                              "hadd_stage2_%s_%s_%s_%s.root" % hadd_stage2_job_tuple)

    if self.isBDTtraining:
      if self.is_sbatch:
        logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
        self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
        self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating Makefile")
      lines_makefile = []
      self.addToMakefile_analyze(lines_makefile)
      self.addToMakefile_hadd_stage1(lines_makefile)
      self.targets.extend(self.phoniesToAdd)
      self.addToMakefile_validate(lines_makefile)
      self.createMakefile(lines_makefile)
      logging.info("Done.")
      return self.num_jobs

    logging.info("Creating configuration files to run 'addBackgroundFakes'")
    for category in self.categories:
      for leptonChargeSelection in self.leptonChargeSelections:
        for hadTau_charge_selection in self.hadTau_charge_selections:
          for chargeSumSelection in self.chargeSumSelections:
            key_hadd_stage1_5_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Fakeable", "enabled"), chargeSumSelection)
            key_addFakes_dir = getKey("addBackgroundLeptonFakes")
            addFakes_job_tuple = (category, leptonChargeSelection, hadTau_charge_selection, chargeSumSelection)
            key_addFakes_job = getKey("data_fakes", *addFakes_job_tuple)
            category_sideband = None
            if self.applyFakeRateWeights == "2lepton":
              category_sideband = getHistogramDir(category, "Fakeable", "Tight", "enabled", leptonChargeSelection, hadTau_charge_selection, chargeSumSelection)
            elif self.applyFakeRateWeights == "4L":
              category_sideband = getHistogramDir(category, "Fakeable", "Fakeable", "enabled", leptonChargeSelection, hadTau_charge_selection, chargeSumSelection)
            elif self.applyFakeRateWeights == "2tau":
              category_sideband = getHistogramDir(category, "Tight", "Fakeable", "enabled", leptonChargeSelection, hadTau_charge_selection, chargeSumSelection)
            else:
              raise ValueError("Invalid Configuration parameter 'applyFakeRateWeights' = %s !!" % self.applyFakeRateWeights)
            self.jobOptions_addFakes[key_addFakes_job] = {
              'inputFile' : self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job],
              'cfgFile_modified' : os.path.join(self.dirs[key_addFakes_dir][DKEY_CFGS], "addBackgroundLeptonFakes_%s_%s_%s_%s_cfg.py" % addFakes_job_tuple),
              'outputFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_HIST], "addBackgroundLeptonFakes_%s_%s_%s_%s.root" % addFakes_job_tuple),
              'logFile' : os.path.join(self.dirs[key_addFakes_dir][DKEY_LOGS], "addBackgroundLeptonFakes_%s_%s_%s_%s.log" % addFakes_job_tuple),
              'category_signal' : getHistogramDir(category, "Tight", "Tight", "disabled", leptonChargeSelection, hadTau_charge_selection, chargeSumSelection),
              'category_sideband' : category_sideband
              }
            self.createCfg_addFakes(self.jobOptions_addFakes[key_addFakes_job])
            key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
            self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])

    #--------------------------------------------------------------------------
    # CV: add histograms in OS and SS regions,
    #     so that "data_fakes" background can be subtracted from OS control region used to estimate charge flip background
    for leptonChargeSelection in self.leptonChargeSelections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        for chargeSumSelection in self.chargeSumSelections:
          key_hadd_stage1_5_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
          key_hadd_stage1_6_dir = getKey("hadd", leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
          hadd_stage1_6_job_tuple = (leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
          key_hadd_stage1_6_job = getKey(*hadd_stage1_6_job_tuple)
          if key_hadd_stage1_6_job not in self.inputFiles_hadd_stage1_6:
            self.inputFiles_hadd_stage1_6[key_hadd_stage1_6_job] = []
          for category in self.categories:      
            key_addFakes_job = getKey("data_fakes", category, leptonChargeSelection, hadTau_charge_selection, chargeSumSelection)
            self.inputFiles_hadd_stage1_6[key_hadd_stage1_6_job].append(self.jobOptions_addFakes[key_addFakes_job]['outputFile'])          
          self.inputFiles_hadd_stage1_6[key_hadd_stage1_6_job].append(self.outputFile_hadd_stage1_5[key_hadd_stage1_5_job])
          self.outputFile_hadd_stage1_6[key_hadd_stage1_6_job] = os.path.join(self.dirs[key_hadd_stage1_6_dir][DKEY_HIST],
                                                                              "hadd_stage1_6_%s_%s_%s_%s.root" % hadd_stage1_6_job_tuple)
    #--------------------------------------------------------------------------

    logging.info("Creating configuration files to run 'addBackgroundFlips'")
    for leptonChargeSelection in self.leptonChargeSelections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        for chargeSumSelection in self.chargeSumSelections:
          if not chargeSumSelection in [ "SS", "disabled" ]:
            continue
          for category_signal in self.categories:
            if not category_signal.find("SS_") != -1:
              continue
            key_hadd_stage1_6_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
            key_addFlips_dir = getKey("addBackgroundLeptonFlips")
            addFlips_job_tuple = (category_signal, leptonChargeSelection, hadTau_charge_selection, chargeSumSelection)
            key_addFlips_job = getKey("data_flips",  *addFlips_job_tuple)
            self.jobOptions_addFlips[key_addFlips_job] = {
              'inputFile' : self.outputFile_hadd_stage1_6[key_hadd_stage1_6_job],
              'cfgFile_modified' : os.path.join(self.dirs[key_addFlips_dir][DKEY_CFGS], "addBackgroundLeptonFlips_%s_%s_%s_%s_cfg.py" % addFlips_job_tuple),
              'outputFile' : os.path.join(self.dirs[key_addFlips_dir][DKEY_HIST], "addBackgroundLeptonFlips_%s_%s_%s_%s.root" % addFlips_job_tuple),
              'logFile' : os.path.join(self.dirs[key_addFlips_dir][DKEY_LOGS], "addBackgroundLeptonFlips_%s_%s_%s_%s.log" % addFlips_job_tuple),
              'category_signal' : "%s_sumSS_Tight" % category_signal,
              'category_sideband' : "%s_sumSS_Tight" % category_signal.replace("SS_2tau", "OS_2tau_wChargeFlipWeights")
            }
            self.createCfg_addFlips(self.jobOptions_addFlips[key_addFlips_job])
            key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
            self.inputFiles_hadd_stage2[key_hadd_stage2_job].append(self.jobOptions_addFlips[key_addFlips_job]['outputFile'])


    logging.info("Creating configuration files to run 'prepareDatacards'...")
    for category in self.categories:
      if category == self.category_inclusive:
        self.central_or_shifts.extend(["EigenVec_1Up",  "EigenVec_1Down", "EigenVec_2Up", "EigenVec_2Down", "fit_bias_Syst", "FitSystUp", "FitSystDown", "original"]) ## these systematics only for the inclusive case
      for leptonChargeSelection in self.leptonChargeSelections:
        for hadTau_charge_selection in self.hadTau_charge_selections:
          lepton_and_hadTau_charge_selection = ""
          if leptonChargeSelection != "disabled":
            lepton_and_hadTau_charge_selection += "_lep%s" % leptonChargeSelection
          if hadTau_charge_selection != "disabled":
            lepton_and_hadTau_charge_selection += "_tau%s" % hadTau_charge_selection
          for histogramToFit in self.histograms_to_fit:
            logging.info(" ...  for category %s, charge selection %s, histogram %s" % (category, lepton_and_hadTau_charge_selection, histogramToFit))
            prep_dcard_HH = set()
            for sample_name, sample_info in self.samples.items():
              if not sample_info["use_it"]:
                continue
              sample_category = sample_info["sample_category_hh"]
              masses_to_exclude = ["3000", "2500", "2000", "1750", "1500", "1250"]
              if sample_category.startswith("signal"):
                doAdd = False
                if "BDTOutput" in histogramToFit:
                  if ("SM" in histogramToFit or "BM" in histogramToFit) and 'nonresonant' in sample_category:
                    doAdd = True
                  if "spin0" in histogramToFit and "spin0" in sample_category and histogramToFit[9:13] in sample_category:
                    doAdd = True
                  if "spin2" in histogramToFit and "spin2" in sample_category and histogramToFit[9:13] in sample_category:
                    doAdd = True
                  for mass in masses_to_exclude:
                    if mass in sample_category: doAdd = False
                else:
                  doAdd = True
                if doAdd:
                  if "wwww" in sample_category:
                    prep_dcard_HH.add(sample_category.replace("wwww", "zzzz"))
                    prep_dcard_HH.add(sample_category.replace("wwww", "wwww"))
                    prep_dcard_HH.add(sample_category.replace("wwww", "zzww"))
                  elif "wwtt" in sample_category:
                    prep_dcard_HH.add(sample_category.replace("wwtt", "ttzz"))
                    prep_dcard_HH.add(sample_category.replace("wwtt", "ttww"))
                  elif "tttt" in sample_category:                  
                    prep_dcard_HH.add(sample_category)
                  else:
                    raise ValueError("Failed to identify relevant HH decay mode(s) for 'sample_category' = %s !!" % sample_category)
            prep_dcard_HH = list(prep_dcard_HH)
            prep_dcard_H = []
            prep_dcard_other_nonfake_backgrounds = []
            for process in self.nonfake_backgrounds:
              if process in [ "VH", "TH", "TTH", "TTWH", "TTZH", "ggH", "qqH" ]:
                prep_dcard_H.append("%s_hww" % process)
                prep_dcard_H.append("%s_hzz" % process)
                prep_dcard_H.append("%s_htt" % process)
              else:
                prep_dcard_other_nonfake_backgrounds.append(process)
            self.prep_dcard_processesToCopy = [ "data_obs" ] + prep_dcard_HH + prep_dcard_H + prep_dcard_other_nonfake_backgrounds + [ "Convs", "data_fakes", "fakes_mc" ]
            key_prep_dcard_dir = getKey("prepareDatacards")
            if "OS" in self.chargeSumSelections:
              key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "OS")
              prep_dcard_job_tuple = (self.channel, category, lepton_and_hadTau_charge_selection, "OS", histogramToFit)
              key_prep_dcard_job = getKey(category, leptonChargeSelection, hadTau_charge_selection, "OS", histogramToFit)
              self.jobOptions_prep_dcard[key_prep_dcard_job] = {
                'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
                'cfgFile_modified' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_CFGS], "prepareDatacards_%s_%s_%s_sum%s_%s_cfg.py" % prep_dcard_job_tuple),
                'datacardFile' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_DCRD], "prepareDatacards_%s_%s_%s_sum%s_%s.root" % prep_dcard_job_tuple),
                'histogramDir' : getHistogramDir(category, "Tight", "Tight", "disabled", leptonChargeSelection, hadTau_charge_selection, "OS"),
                'histogramToFit' : histogramToFit,
                'label' : '2l+2tau_{h}',
                }
              self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])

              if "SS" in self.chargeSumSelections:
                key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "SS")
                prep_dcard_job_tuple = (self.channel, category, lepton_and_hadTau_charge_selection, "SS", histogramToFit)
                key_prep_dcard_job = getKey(category, leptonChargeSelection, hadTau_charge_selection, "SS", histogramToFit)
                self.jobOptions_prep_dcard[key_prep_dcard_job] = {
                  'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
                  'cfgFile_modified' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_CFGS], "prepareDatacards_%s_%s_%s_sum%s_%s_cfg.py" % prep_dcard_job_tuple),
                  'datacardFile' : os.path.join(self.dirs[key_prep_dcard_dir][DKEY_DCRD], "prepareDatacards_%s_%s_%s_sum%s_%s.root" % prep_dcard_job_tuple),
                  'histogramDir' : getHistogramDir(category, "Tight", "Tight", "disabled", leptonChargeSelection, hadTau_charge_selection, "SS"),
                  'histogramToFit' : histogramToFit,
                  'label' : '2l+2tau_{h} SS',
                }
                self.createCfg_prep_dcard(self.jobOptions_prep_dcard[key_prep_dcard_job])

              # add shape templates for the following systematic uncertainties:
              #  - 'CMS_ttHl_Clos_norm_e'
              #  - 'CMS_ttHl_Clos_shape_e'
              #  - 'CMS_ttHl_Clos_norm_m'
              #  - 'CMS_ttHl_Clos_shape_m'
              #  - 'CMS_ttHl_Clos_norm_t'
              #  - 'CMS_ttHl_Clos_shape_t'
              for chargeSumSelection in self.chargeSumSelections:
                key_prep_dcard_job = getKey(category, leptonChargeSelection, hadTau_charge_selection, chargeSumSelection, histogramToFit)
                key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), chargeSumSelection)
                key_add_syst_fakerate_dir = getKey("addSystFakeRates")
                add_syst_fakerate_job_tuple = (self.channel, category, lepton_and_hadTau_charge_selection, chargeSumSelection, histogramToFit)
                key_add_syst_fakerate_job = getKey(category, leptonChargeSelection, hadTau_charge_selection, chargeSumSelection, histogramToFit)
                self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job] = {
                  'inputFile' : self.jobOptions_prep_dcard[key_prep_dcard_job]['datacardFile'],
                  'cfgFile_modified' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_CFGS], "addSystFakeRates_%s_%s_%s_sum%s_%s_cfg.py" % add_syst_fakerate_job_tuple),
                  'outputFile' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_DCRD], "addSystFakeRates_%s_%s_%s_sum%s_%s.root" % add_syst_fakerate_job_tuple),
                  'category' : category,
                  'histogramToFit' : histogramToFit,
                  'plots_outputFileName' : os.path.join(self.dirs[key_add_syst_fakerate_dir][DKEY_PLOT], "addSystFakeRates.png")
                }
                histogramDir_nominal = getHistogramDir(category, "Tight", "Tight", "disabled", leptonChargeSelection, hadTau_charge_selection, chargeSumSelection)
                for lepton_and_hadTau_type in [ 'e', 'm', 't' ]:
                  lepton_and_hadTau_mcClosure = "Fakeable_mcClosure_%s" % lepton_and_hadTau_type
                  if lepton_and_hadTau_mcClosure not in self.lepton_and_hadTau_selections:
                    continue
                  lepton_and_hadTau_selection_and_frWeight = get_lepton_and_hadTau_selection_and_frWeight(lepton_and_hadTau_mcClosure, "enabled")
                  key_addBackgrounds_job_fakes = getKey("fakes_mc", leptonChargeSelection, hadTau_charge_selection, lepton_and_hadTau_selection_and_frWeight, chargeSumSelection)
                  histogramDir_mcClosure = self.mcClosure_dir['%s_%s_%s' % (lepton_and_hadTau_mcClosure, chargeSumSelection, hadTau_charge_selection)]
                  self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job].update({
                    'add_Clos_%s' % lepton_and_hadTau_type : ("Fakeable_mcClosure_%s" % lepton_and_hadTau_type) in self.lepton_and_hadTau_selections,
                    'inputFile_nominal_%s' % lepton_and_hadTau_type : self.outputFile_hadd_stage2[key_hadd_stage2_job],
                    'histogramName_nominal_%s' % lepton_and_hadTau_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_nominal, histogramToFit),
                    'inputFile_mcClosure_%s' % lepton_and_hadTau_type : self.jobOptions_addBackgrounds_sum[key_addBackgrounds_job_fakes]['outputFile'],
                    'histogramName_mcClosure_%s' % lepton_and_hadTau_type : "%s/sel/evt/fakes_mc/%s" % (histogramDir_mcClosure, histogramToFit)
                  })
                self.createCfg_add_syst_fakerate(self.jobOptions_add_syst_fakerate[key_add_syst_fakerate_job])

    logging.info("Creating configuration files to run 'makePlots'")
    for leptonChargeSelection in self.leptonChargeSelections:
      for hadTau_charge_selection in self.hadTau_charge_selections:
        lepton_and_hadTau_charge_selection = ""
        if leptonChargeSelection != "disabled":
          lepton_and_hadTau_charge_selection += "_lep%s" % leptonChargeSelection
        if hadTau_charge_selection != "disabled":
          lepton_and_hadTau_charge_selection += "_tau%s" % hadTau_charge_selection
        key_makePlots_dir = getKey("makePlots")
        if "OS" in self.chargeSumSelections:
          key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "OS")
          key_makePlots_job = getKey(leptonChargeSelection, hadTau_charge_selection, "OS")
          self.jobOptions_make_plots[key_makePlots_job] = {
            'executable' : self.executable_make_plots,
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_%s_%s_cfg.py" % (self.channel, lepton_and_hadTau_charge_selection)),
            'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_%s_%s.png" % (self.channel, lepton_and_hadTau_charge_selection)),
            'histogramDir' : getHistogramDir(self.category_inclusive, "Tight", "Tight", "disabled", leptonChargeSelection, hadTau_charge_selection, "OS"), ## We are making plots only for the inclusive category
            'label' : '2l+2tau_{h}',
            'make_plots_backgrounds' : self.make_plots_backgrounds
          }
          self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
        if "SS" in self.chargeSumSelections:
          key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "SS")
          key_makePlots_job = getKey(leptonChargeSelection, hadTau_charge_selection, "SS")          
          self.jobOptions_make_plots[key_makePlots_job] = {
            'executable' : self.executable_make_plots,
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_%s_%s_sumSS_cfg.py" % (self.channel, lepton_and_hadTau_charge_selection)),
            'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_%s_%s_sumSS.png" % (self.channel, lepton_and_hadTau_charge_selection)),
            'histogramDir' : getHistogramDir(self.category_inclusive, "Tight", "Tight", "disabled", leptonChargeSelection, hadTau_charge_selection, "SS"), ## We are making plots only for the inclusive category
            'label' : "2l+2tau_{h} SS",
            'make_plots_backgrounds' : self.make_plots_backgrounds
          }
          self.createCfg_makePlots(self.jobOptions_make_plots[key_makePlots_job])
        if "Fakeable_mcClosure" in self.lepton_and_hadTau_selections: #TODO
          key_hadd_stage2_job = getKey(leptonChargeSelection, hadTau_charge_selection, get_lepton_and_hadTau_selection_and_frWeight("Tight", "disabled"), "OS")
          key_makePlots_job = getKey("Fakeable_mcClosure", leptonChargeSelection, hadTau_charge_selection, "OS")          
          self.jobOptions_make_plots[key_makePlots_job] = {
            'executable' : self.executable_make_plots_mcClosure,
            'inputFile' : self.outputFile_hadd_stage2[key_hadd_stage2_job],
            'cfgFile_modified' : os.path.join(self.dirs[key_makePlots_dir][DKEY_CFGS], "makePlots_mcClosure_%s_%s_cfg.py" % (self.channel, lepton_and_hadTau_charge_selection)),
            'outputFile' : os.path.join(self.dirs[key_makePlots_dir][DKEY_PLOT], "makePlots_mcClosure_%s_%s.png" % (self.channel, lepton_and_hadTau_charge_selection))
          }
          self.createCfg_makePlots_mcClosure(self.jobOptions_make_plots[key_makePlots_job])

    if self.is_sbatch:
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_analyze)
      self.sbatchFile_analyze = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_analyze_%s.py" % self.channel)
      self.createScript_sbatch_analyze(self.executable_analyze, self.sbatchFile_analyze, self.jobOptions_analyze)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addBackgrounds)
      self.sbatchFile_addBackgrounds = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds, self.jobOptions_addBackgrounds)
      self.sbatchFile_addBackgrounds_sum = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addBackgrounds_sum_%s.py" % self.channel)
      self.createScript_sbatch_addBackgrounds(self.executable_addBackgrounds, self.sbatchFile_addBackgrounds_sum, self.jobOptions_addBackgrounds_sum)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addFakes)
      self.sbatchFile_addFakes = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addFakes_%s.py" % self.channel)
      self.createScript_sbatch_addFakes(self.executable_addFakes, self.sbatchFile_addFakes, self.jobOptions_addFakes)
      logging.info("Creating script for submitting '%s' jobs to batch system" % self.executable_addFlips)
      self.sbatchFile_addFlips = os.path.join(self.dirs[DKEY_SCRIPTS], "sbatch_addFlips_%s.py" % self.channel)
      self.createScript_sbatch(self.executable_addFlips, self.sbatchFile_addFlips, self.jobOptions_addFlips)

    logging.info("Creating Makefile")
    lines_makefile = []
    self.addToMakefile_analyze(lines_makefile)
    self.addToMakefile_hadd_stage1(lines_makefile)
    self.addToMakefile_backgrounds_from_data_withFlips(lines_makefile)
    self.addToMakefile_hadd_stage2(lines_makefile)
    self.addToMakefile_prep_dcard(lines_makefile)
    self.addToMakefile_add_syst_fakerate(lines_makefile)
    self.addToMakefile_make_plots(lines_makefile)
    self.addToMakefile_validate(lines_makefile)
    self.createMakefile(lines_makefile)

    logging.info("Done.")

    return self.num_jobs
