#!/usr/bin/env python

from hhAnalysis.multilepton.configs.analyzeConfig_hh_1l_3tau import analyzeConfig_hh_1l_3tau
from tthAnalysis.HiggsToTauTau.jobTools import query_yes_no
from tthAnalysis.HiggsToTauTau.analysisSettings import systematics, get_lumi
from tthAnalysis.HiggsToTauTau.runConfig import tthAnalyzeParser, filter_samples
from tthAnalysis.HiggsToTauTau.common import logging
from tthAnalysis.HiggsToTauTau.common import load_samples_hh_multilepton as load_samples
from tthAnalysis.HiggsToTauTau.common import load_samples_stitched
import os
import sys
import getpass

# E.g.: ./test/hhAnalyzeRun_1l_3tau.py -v 2017Dec13 -m default -e 2017 -t deepVSj

mode_choices     = [ 'default', 'forBDTtraining' ]
sys_choices      = [ 'full', 'internal' ] + systematics.an_opts_hh_multilepton
systematics.full = systematics.an_hh_multilepton
systematics.internal = systematics.an_internal_no_mem

parser = tthAnalyzeParser()
parser.add_modes(mode_choices)
parser.add_sys(sys_choices)
parser.add_preselect()
parser.add_rle_select()
parser.add_lep_mva_wp(default_wp = 'hh_multilepton') # alternative: hh_multilepton
parser.add_nonnominal()
parser.add_tau_id_wp()
parser.add_hlt_filter()
parser.add_files_per_job()
parser.add_use_home()
parser.add_jet_cleaning()
parser.add_gen_matching()
parser.add_sideband()
parser.add_tau_id()
parser.enable_regrouped_jerc()
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
rle_select        = os.path.expanduser(args.rle_select)
use_nonnominal    = args.original_central
hlt_filter        = args.hlt_filter
lep_mva_wp        = args.lep_mva_wp
files_per_job     = args.files_per_job
use_home          = args.use_home
sideband          = args.sideband
tau_id            = args.tau_id
jet_cleaning      = args.jet_cleaning
gen_matching      = args.gen_matching
regroup_jerc      = args.enable_regrouped_jerc
split_trigger_sys = args.split_trigger_sys

if regroup_jerc:
  if 'full' not in systematics_label:
    raise RuntimeError("Regrouped JEC or split JER was enabled but not running with full systematics")
  systematics.full.extend(systematics.JEC_regrouped + systematics.JER_split)
if split_trigger_sys == 'yes':
  for trigger_sys in systematics.triggerSF:
    del systematics.internal[systematics.internal.index(trigger_sys)]
    del systematics.full[systematics.full.index(trigger_sys)]
if split_trigger_sys in [ 'yes', 'both' ]:
  systematics.internal.extend(systematics.triggerSF_0l2tau + systematics.triggerSF_1l1tau)
  systematics.full.extend(systematics.triggerSF_0l2tau + systematics.triggerSF_1l1tau)

# Use the arguments
central_or_shifts = []
for systematic_label in systematics_label:
  for central_or_shift in getattr(systematics, systematic_label):
    if central_or_shift not in central_or_shifts:
      central_or_shifts.append(central_or_shift)
do_sync = mode.startswith('sync')
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
  'dR03mva' : 'Loose',
  ##'deepVSj' : 'VLoose', # CV: use for datacard production
  'deepVSj' : 'Loose',
}
hadTau_selection = tau_id + hadTauWP_map[tau_id]

if mode == "default":
  samples = load_samples(era, suffix = "preselected" if use_preselected else "")
  samples = load_samples_stitched(samples, era, [ 'dy_nlo' ])
elif mode == "forBDTtraining":
  if use_preselected:
    raise ValueError("Producing Ntuples for BDT training from preselected Ntuples makes no sense!")

  samples = load_samples(era, suffix = "BDT")
  samples = load_samples_stitched(samples, era, [ 'dy_lo' ])

  hadTauWP_map_relaxed = {
    'dR03mva' : 'VLoose',
    #'deepVSj' : 'VLoose', # CV: use for datacard production
    'deepVSj' : 'VVVLoose', # CV: use for BDT training
  }
  if args.tau_id_wp:
    tau_id = args.tau_id[:7]
  hadTau_selection_relaxed = tau_id + hadTauWP_map_relaxed[tau_id]
else:
  raise ValueError("Invalid mode: %s" % mode)

for sample_name, sample_info in samples.items():
  if sample_name == 'sum_events': continue
  if sample_name.startswith(("/DoubleEG/", "/DoubleMuon/", "/MuonEG/")):
    sample_info["use_it"] = False
  elif sample_name.startswith("/Tau/"):
    sample_info["use_it"] = True

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

  analysis = analyzeConfig_hh_1l_3tau(
    configDir = os.path.join("/home",       getpass.getuser(), "hhAnalysis", era, version),
    outputDir = os.path.join("/hdfs/local", getpass.getuser(), "hhAnalysis", era, version),
    executable_analyze                    = "analyze_hh_1l_3tau",
    cfgFile_analyze                       = "analyze_hh_1l_3tau_cfg.py",
    samples                               = samples,
    hadTau_selection                      = hadTau_selection,
    applyFakeRateWeights                  = "4L",
    chargeSumSelections                   = chargeSumSelections,
    central_or_shifts                     = central_or_shifts,
    lep_mva_wp                            = lep_mva_wp,
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
    histograms_to_fit                     = {
      "EventCounter"                      : {},
      "dihiggsMass"                       : {},
      "BDTOutput_300_hypo_spin0"          : {},
      "BDTOutput_SM"                      : {},
      "BDTOutput_BM1"                     : {},
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
