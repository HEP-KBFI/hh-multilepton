#!/usr/bin/env python

from hhAnalysis.multilepton.configs.analyzeConfig_hh_2l_2tau import analyzeConfig_hh_2l_2tau
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging, load_samples_hh_multilepton as load_samples

import os
import sys
import getpass

# E.g.: ./test/hhAnalyzeRun_hh_2l_2tau.py -v 2017Dec13 -m default -e 2017

mode_choices     = [ 'default', 'forBDTtraining' ]
sys_choices      = [ 'full', 'internal' ] + systematics.an_extended_opts_hh
systematics.full = systematics.an_extended_hh
systematics.internal = systematics.an_internal_no_mem

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_jet_cleaning()
parser.add_gen_matching()
parser.add_sideband()
parser.add_tau_id()
parser.enable_regrouped_jec()
parser.add_split_trigger_sys()
args = parser.parse_args()

# Common arguments
era                = args.era
version            = args.version
dry_run            = args.dry_run
no_exec            = args.no_exec
auto_exec          = args.auto_exec
check_output_files = not args.not_check_input_files
debug              = args.debug
sample_filter      = args.filter
num_parallel_jobs  = args.num_parallel_jobs
running_method     = args.running_method

# Additional arguments
mode              = args.mode
systematics_label = args.systematics
use_preselected   = args.use_preselected
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
files_per_job     = args.files_per_job
use_home          = args.use_home
tau_id_wp         = args.tau_id_wp
sideband          = args.sideband
tau_id            = args.tau_id
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jec       = args.enable_regrouped_jec
split_trigger_sys = args.split_trigger_sys

if regroup_jec:
  if 'full' not in systematics_label:
    raise RuntimeError("Regrouped JEC was enabled but not running with full systematics")
  systematics.full.extend(systematics.JEC_regrouped)
if split_trigger_sys == 'yes':
  for trigger_sys in systematics.triggerSF:
    del systematics.internal[systematics.internal.index(trigger_sys)]
    del systematics.full[systematics.full.index(trigger_sys)]
if split_trigger_sys in [ 'yes', 'both' ]:
  systematics.internal.extend(systematics.triggerSF_2lss)
  systematics.full.extend(systematics.triggerSF_2lss)

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
lumi = get_lumi(era)
jet_cleaning_by_index = (jet_cleaning == 'by_index')
gen_matching_by_index = (gen_matching == 'by_index')

if sideband == 'disabled':
  chargeSumSelections = [ "OS" ]
elif sideband == 'enabled':
  chargeSumSelections = [ "OS", "SS" ]
elif sideband == 'only':
  chargeSumSelections = [ "SS" ]
else:
  raise ValueError("Invalid choice for the sideband: %s" % sideband)

hadTauWP_map = {
  'dR03mva' : 'Medium',
  'deepVSj' : 'Medium',
}
hadTau_selection = tau_id + hadTauWP_map[tau_id]

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
elif mode == "forBDTtraining":
  if use_preselected:
    raise ValueError("Producing Ntuples for BDT training from preselected Ntuples makes no sense!")
  samples = load_samples(era, suffix = "BDT_2l_2tau")
  hadTauWP_map_relaxed = {
    'dR03mva' : 'Loose',
    'deepVSj' : 'Loose',
  }
  if args.tau_id_wp:
    tau_id = args.tau_id[:7]
  hadTau_selection_relaxed = tau_id + hadTauWP_map_relaxed[tau_id]
else:
  raise ValueError("Internal logic error")

if __name__ == '__main__':
  logging.info(
    "Running the jobs with the following systematic uncertainties enabled: %s" % \
    ', '.join(central_or_shifts)
  )
  if not use_preselected:
    logging.warning('Running the analysis on fully inclusive samples!')

  if sample_filter:
    samples = filter_samples(samples, sample_filter)

  if args.tau_id_wp:
    logging.info("Changing tau ID working point: %s -> %s" % (hadTau_selection, args.tau_id_wp))
    hadTau_selection = args.tau_id_wp

  analysis = analyzeConfig_hh_2l_2tau(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_2l_2tau",
    cfgFile_analyze                       = "analyze_hh_2l_2tau_cfg.py",
    samples                               = samples,
    leptonChargeSelections                = [ "disabled" ],
    hadTau_selection                      = hadTau_selection,
    hadTau_charge_selections              = [ "disabled" ],
    applyFakeRateWeights                  = "4L",
    chargeSumSelections                   = chargeSumSelections,
    central_or_shifts                     = central_or_shifts,
    jet_cleaning_by_index                 = jet_cleaning_by_index,
    gen_matching_by_index                 = gen_matching_by_index,
    max_files_per_job                     = files_per_job,
    era                                   = era,
    use_lumi                              = True,
    lumi                                  = lumi,
    check_output_files                    = check_output_files,
    running_method                        = running_method,
    num_parallel_jobs                     = num_parallel_jobs,
    executable_addBackgrounds             = "addBackgrounds",
    executable_addBackgroundJetToTauFakes = "addBackgroundLeptonFakes",
    executable_addFlips                   = "addBackgroundLeptonFlips",
    histograms_to_fit                     = {
      "EventCounter"                      : {},
      #"numJets"                           : {},
      "mTauTauVis"                        : {},
      "dihiggsVisMass"                    : {},
      "dihiggsMass"                       : {},
      "HT"                                : {},
      "STMET"                             : {},
      "BDTOutput_1000"                    : {},
      "BDTOutput_250"                    : {},
      "BDTOutput_400"                    : {},
      "BDTOutput_700"                    : {},
      "BDTOutput_300"                    : {},
      "BDTOutput_500"                    : {},
      "BDTOutput_800"                    : {},
      "NNOutput_1000"                    : {},
      "NNOutput_250"                    : {},
      "NNOutput_400"                    : {},
      "NNOutput_700"                    : {},
      "NNOutput_300"                    : {},
      "NNOutput_500"                    : {},
      "NNOutput_800"                    : {}
    },
    select_rle_output                     = True,
    dry_run                               = dry_run,
    isDebug                               = debug,
    use_nonnominal                        = use_nonnominal,
    hlt_filter                            = hlt_filter,
    use_home                              = use_home,
    submission_cmd                        = sys.argv,
  )

  if mode.find("forBDTtraining") != -1:
    analysis.set_BDT_training(hadTau_selection_relaxed)

  job_statistics = analysis.create()
  for job_type, num_jobs in job_statistics.items():
    logging.info(" #jobs of type '%s' = %i" % (job_type, num_jobs))

  if auto_exec:
    run_analysis = True
  elif no_exec:
    run_analysis = False
  else:
    run_analysis = query_yes_no("Start jobs ?")
  if run_analysis:
    analysis.run()
  else:
    sys.exit(0)
