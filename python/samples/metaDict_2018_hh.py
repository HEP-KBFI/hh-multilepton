from collections import OrderedDict as OD

# file generated at 2020-10-19 13:54:29 with the following command:
# find_samples.py -V -i ../../tthAnalysis/NanoAOD/test/datasets/txt/datasets_hh_multilepton_mc_2018_RunIIAutumn18MiniAOD.txt -m python/samples/metaDict_2018_hh.py -s ../../tthAnalysis/NanoAOD/test/datasets/txt/sum_datasets_hh_multilepton_2018_RunIIAutumn18MiniAOD.txt -c python/samples/sampleLocations_2018_nanoAOD_hh_multilepton.txt

meta_dictionary = OD()


### event sums

sum_events = { 
  ("signal_ggf_nonresonant_node_sm_hh_4v", "signal_ggf_nonresonant_node_1_hh_4v", "signal_ggf_nonresonant_node_2_hh_4v", "signal_ggf_nonresonant_node_3_hh_4v", "signal_ggf_nonresonant_node_4_hh_4v", "signal_ggf_nonresonant_node_5_hh_4v", "signal_ggf_nonresonant_node_6_hh_4v", "signal_ggf_nonresonant_node_7_hh_4v", "signal_ggf_nonresonant_node_8_hh_4v", "signal_ggf_nonresonant_node_9_hh_4v", "signal_ggf_nonresonant_node_10_hh_4v", "signal_ggf_nonresonant_node_11_hh_4v", "signal_ggf_nonresonant_node_12_hh_4v"),
  ("signal_ggf_nonresonant_node_sm_hh_2v2t", "signal_ggf_nonresonant_node_1_hh_2v2t", "signal_ggf_nonresonant_node_2_hh_2v2t", "signal_ggf_nonresonant_node_3_hh_2v2t", "signal_ggf_nonresonant_node_4_hh_2v2t", "signal_ggf_nonresonant_node_5_hh_2v2t", "signal_ggf_nonresonant_node_6_hh_2v2t", "signal_ggf_nonresonant_node_7_hh_2v2t", "signal_ggf_nonresonant_node_8_hh_2v2t", "signal_ggf_nonresonant_node_9_hh_2v2t", "signal_ggf_nonresonant_node_10_hh_2v2t", "signal_ggf_nonresonant_node_11_hh_2v2t", "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("signal_ggf_nonresonant_node_sm_hh_4t", "signal_ggf_nonresonant_node_1_hh_4t", "signal_ggf_nonresonant_node_2_hh_4t", "signal_ggf_nonresonant_node_3_hh_4t", "signal_ggf_nonresonant_node_4_hh_4t", "signal_ggf_nonresonant_node_5_hh_4t", "signal_ggf_nonresonant_node_6_hh_4t", "signal_ggf_nonresonant_node_7_hh_4t", "signal_ggf_nonresonant_node_8_hh_4t", "signal_ggf_nonresonant_node_9_hh_4t", "signal_ggf_nonresonant_node_10_hh_4t", "signal_ggf_nonresonant_node_11_hh_4t", "signal_ggf_nonresonant_node_12_hh_4t"),
}


meta_dictionary["/GluGluToRadionToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          13),
  ("fsize_db",              21421829719),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.42GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-16 17:32:21"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          10),
  ("fsize_db",              20670227545),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.67GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-12 01:42:19"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          14),
  ("fsize_db",              20783178743),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.78GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-14 14:59:59"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_4t"),
  ("nof_db_events",         385000),
  ("nof_db_files",          21),
  ("fsize_db",              20779525724),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.78GB; nevents: 385.00k; release: 10_2_5; last modified: 2019-11-10 07:00:30"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_4t"),
  ("nof_db_events",         294000),
  ("nof_db_files",          17),
  ("fsize_db",              15512052325),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.51GB; nevents: 294.00k; release: 10_2_5; last modified: 2019-11-10 12:06:30"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_320_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_4t"),
  ("nof_db_events",         297000),
  ("nof_db_files",          15),
  ("fsize_db",              15790119701),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.79GB; nevents: 297.00k; release: 10_2_5; last modified: 2019-11-10 23:46:34"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_4t"),
  ("nof_db_events",         297000),
  ("nof_db_files",          9),
  ("fsize_db",              15967583373),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.97GB; nevents: 297.00k; release: 10_2_5; last modified: 2019-10-13 00:50:20"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          18),
  ("fsize_db",              15976195307),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.98GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-30 04:19:10"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          6),
  ("fsize_db",              17563676363),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.56GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-11 15:48:38"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          5),
  ("fsize_db",              16876391387),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.88GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-11 22:32:16"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          16),
  ("fsize_db",              17078741577),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.08GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-06 14:08:10"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_4t"),
  ("nof_db_events",         196000),
  ("nof_db_files",          4),
  ("fsize_db",              10929556578),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 10.93GB; nevents: 196.00k; release: 10_2_5; last modified: 2019-10-11 15:49:32"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          12),
  ("fsize_db",              11285007994),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.29GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-07 03:40:28"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              11712322920),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.71GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-13 00:49:15"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          6),
  ("fsize_db",              12140113240),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.14GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-13 05:11:24"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_4t"),
  ("nof_db_events",         196000),
  ("nof_db_files",          5),
  ("fsize_db",              11652048519),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.65GB; nevents: 196.00k; release: 10_2_5; last modified: 2019-10-16 20:29:11"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_850_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              12308761975),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.31GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-11 06:44:14"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_4t"),
  ("nof_db_events",         190000),
  ("nof_db_files",          17),
  ("fsize_db",              12135155388),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.14GB; nevents: 190.00k; release: 10_2_5; last modified: 2019-11-01 15:31:01"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6443692606),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.44GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 17:58:29"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          5),
  ("fsize_db",              6712151176),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.71GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-15 07:24:02"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6302147130),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.30GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-09 14:24:43"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6821889709),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.82GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-10 20:25:07"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_4t"),
  ("nof_db_events",         96000),
  ("nof_db_files",          12),
  ("fsize_db",              6494733234),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.49GB; nevents: 96.00k; release: 10_2_5; last modified: 2019-11-03 10:36:33"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6926930812),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.93GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-13 08:50:22"),
])

meta_dictionary["/GluGluToRadionToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6993185515),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.99GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-13 23:07:02"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_250_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_250_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          25),
  ("fsize_db",              25688213729),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.69GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-11-07 03:41:27"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_260_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_260_hh_4t"),
  ("nof_db_events",         392000),
  ("nof_db_files",          27),
  ("fsize_db",              26459235708),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.46GB; nevents: 392.00k; release: 10_2_5; last modified: 2019-11-07 10:40:57"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_270_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_270_hh_4t"),
  ("nof_db_events",         360000),
  ("nof_db_files",          21),
  ("fsize_db",              22838217629),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.84GB; nevents: 360.00k; release: 10_2_5; last modified: 2019-11-08 12:55:09"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_280_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_280_hh_4t"),
  ("nof_db_events",         392000),
  ("nof_db_files",          13),
  ("fsize_db",              24989693699),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.99GB; nevents: 392.00k; release: 10_2_5; last modified: 2019-11-25 15:29:51"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_300_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_300_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          6),
  ("fsize_db",              19311475451),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.31GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-11 10:30:17"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_320_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_320_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          25),
  ("fsize_db",              19594757568),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.59GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-03 10:36:08"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_350_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_350_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          31),
  ("fsize_db",              21184916301),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.18GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-09 14:24:48"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_400_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_400_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          9),
  ("fsize_db",              21535525625),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.54GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-16 06:51:14"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_450_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_450_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          9),
  ("fsize_db",              21898598924),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.90GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-15 06:23:18"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_500_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_500_hh_4t"),
  ("nof_db_events",         296000),
  ("nof_db_files",          20),
  ("fsize_db",              20445801040),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.45GB; nevents: 296.00k; release: 10_2_5; last modified: 2019-11-06 23:18:11"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_550_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_550_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          27),
  ("fsize_db",              21548412071),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.55GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-06 23:18:36"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_600_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_600_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          6),
  ("fsize_db",              15178299980),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.18GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-13 15:45:51"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_650_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_650_hh_4t"),
  ("nof_db_events",         196000),
  ("nof_db_files",          7),
  ("fsize_db",              15016770852),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.02GB; nevents: 196.00k; release: 10_2_5; last modified: 2019-10-11 17:57:24"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_700_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_700_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              15459043528),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.46GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-11 17:59:59"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_750_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_750_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          17),
  ("fsize_db",              15621663509),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.62GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-27 12:00:31"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_800_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_800_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          15),
  ("fsize_db",              15721000671),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.72GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-28 18:25:49"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_850_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_850_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          8),
  ("fsize_db",              15824798381),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.82GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-11 22:33:42"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_900_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_900_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          14),
  ("fsize_db",              15947921131),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.95GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-23 22:42:59"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_1000_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_1000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              8058532298),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 8.06GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-23 22:42:23"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_1250_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_1250_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          18),
  ("fsize_db",              9385953952),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.39GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-27 21:36:03"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_1500_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_1500_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              9486059274),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.49GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-13 06:59:49"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_1750_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_1750_hh_4t"),
  ("nof_db_events",         98000),
  ("nof_db_files",          15),
  ("fsize_db",              8276227918),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 8.28GB; nevents: 98.00k; release: 10_2_5; last modified: 2019-11-10 12:06:50"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_2000_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_2000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          17),
  ("fsize_db",              9683084437),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.68GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-27 21:42:28"),
])

meta_dictionary["/VBFToRadionToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_3000_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin0_3000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          18),
  ("fsize_db",              9822846522),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 9.82GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-11 19:06:29"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_250_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          8),
  ("fsize_db",              20777026746),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.78GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-11 18:01:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_260_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          8),
  ("fsize_db",              20936620034),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.94GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-11 17:57:39"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          7),
  ("fsize_db",              20729048194),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.73GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-11 15:48:18"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          9),
  ("fsize_db",              21136018972),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.14GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-12 00:20:46"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_300_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_4t"),
  ("nof_db_events",         297000),
  ("nof_db_files",          9),
  ("fsize_db",              15976487156),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.98GB; nevents: 297.00k; release: 10_2_5; last modified: 2019-10-12 05:37:40"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          12),
  ("fsize_db",              16324747735),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.32GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-19 04:56:00"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_350_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          6),
  ("fsize_db",              17221121634),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.22GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-12 21:40:51"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_400_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          6),
  ("fsize_db",              16917922951),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.92GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-12 09:03:06"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_450_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_4t"),
  ("nof_db_events",         295000),
  ("nof_db_files",          9),
  ("fsize_db",              16095046767),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.10GB; nevents: 295.00k; release: 10_2_5; last modified: 2019-10-16 10:05:24"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          8),
  ("fsize_db",              17370100767),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.37GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-13 06:55:14"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          8),
  ("fsize_db",              18535631090),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.54GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-12 03:43:50"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              12464159691),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.46GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-12 21:39:27"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          10),
  ("fsize_db",              12571955086),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.57GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-06 18:17:07"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          22),
  ("fsize_db",              12721700410),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.72GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-28 01:09:12"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_750_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_4t"),
  ("nof_db_events",         196000),
  ("nof_db_files",          6),
  ("fsize_db",              11417510981),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.42GB; nevents: 196.00k; release: 10_2_5; last modified: 2019-10-12 00:20:36"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          6),
  ("fsize_db",              12832750406),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.83GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-15 06:48:15"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_850_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              12511610477),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.51GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-30 09:31:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          17),
  ("fsize_db",              13263531937),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.26GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-28 07:22:53"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6575758202),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.58GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-27 06:09:52"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6795292081),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.80GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 19:50:57"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6511569391),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.51GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 09:26:16"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          11),
  ("fsize_db",              6883287799),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.88GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-11 17:41:48"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          13),
  ("fsize_db",              6432782988),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.43GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-11 17:37:03"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6860162901),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.86GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-10 22:35:30"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_tttt"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6476075631),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.48GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 15:48:08"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_250_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_250_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          14),
  ("fsize_db",              25847161991),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.85GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-12 21:37:47"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_260_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_260_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          7),
  ("fsize_db",              25361450382),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.36GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-11 19:47:01"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_270_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_270_hh_4t"),
  ("nof_db_events",         382000),
  ("nof_db_files",          12),
  ("fsize_db",              23019807000),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.02GB; nevents: 382.00k; release: 10_2_5; last modified: 2019-10-13 20:17:30"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_280_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_280_hh_4t"),
  ("nof_db_events",         397000),
  ("nof_db_files",          22),
  ("fsize_db",              24078569317),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.08GB; nevents: 397.00k; release: 10_2_5; last modified: 2019-11-30 07:31:14"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_300_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_300_hh_4t"),
  ("nof_db_events",         292000),
  ("nof_db_files",          15),
  ("fsize_db",              17208593955),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.21GB; nevents: 292.00k; release: 10_2_5; last modified: 2019-11-02 02:18:12"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_320_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_320_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          22),
  ("fsize_db",              18909348383),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.91GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-28 15:10:38"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_350_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_350_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          21),
  ("fsize_db",              18896343646),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.90GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-13 00:56:47"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_400_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_400_hh_4t"),
  ("nof_db_events",         297000),
  ("nof_db_files",          20),
  ("fsize_db",              17699306957),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.70GB; nevents: 297.00k; release: 10_2_5; last modified: 2019-11-02 08:35:06"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_450_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_450_hh_4t"),
  ("nof_db_events",         298000),
  ("nof_db_files",          17),
  ("fsize_db",              18708714887),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.71GB; nevents: 298.00k; release: 10_2_5; last modified: 2019-11-06 18:17:31"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_500_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_500_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          6),
  ("fsize_db",              18801588414),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.80GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-11 06:43:33"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_550_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_550_hh_4t"),
  ("nof_db_events",         300000),
  ("nof_db_files",          7),
  ("fsize_db",              18305564047),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.31GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-11 06:43:45"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_600_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_600_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              12515645230),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.52GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-10 20:25:42"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_650_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_650_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              12072020917),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.07GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-11 02:28:10"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_700_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_700_hh_4t"),
  ("nof_db_events",         194000),
  ("nof_db_files",          14),
  ("fsize_db",              12224804271),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.22GB; nevents: 194.00k; release: 10_2_5; last modified: 2019-11-03 00:01:26"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_750_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_750_hh_4t"),
  ("nof_db_events",         198000),
  ("nof_db_files",          22),
  ("fsize_db",              12643257670),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.64GB; nevents: 198.00k; release: 10_2_5; last modified: 2019-11-06 14:05:21"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_800_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_800_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              12034640363),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.03GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-07 03:45:18"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_850_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_850_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          4),
  ("fsize_db",              11719677487),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.72GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-13 15:44:21"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_900_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_900_hh_4t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          5),
  ("fsize_db",              11740308279),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.74GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-12 11:44:03"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_1000_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_1000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6057895707),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.06GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-13 15:46:06"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_1200_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_1200_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              6411531409),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.41GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-09 10:44:19"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_1250_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_1250_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6251695894),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.25GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-14 06:49:22"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_1500_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_1500_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6261842364),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.26GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 08:05:01"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_1750_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_1750_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          3),
  ("fsize_db",              6467004835),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.47GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 10:31:17"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_2000_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_2000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6463629715),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.46GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-13 23:05:32"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_2500_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_2500_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6303222189),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.30GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 22:37:22"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo4T_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin2_3000_hh_tttt"),
  ("process_name_specific", "signal_vbf_spin2_3000_hh_4t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          14),
  ("fsize_db",              6621087952),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.62GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-06 14:11:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_250_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          22),
  ("fsize_db",              21134388781),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.13GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-11-28 15:10:45"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_260_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          10),
  ("fsize_db",              20298425114),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.30GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-13 05:10:04"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_270_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_2v2t"),
  ("nof_db_events",         393998),
  ("nof_db_files",          16),
  ("fsize_db",              21723772822),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.72GB; nevents: 394.00k; release: 10_2_5; last modified: 2019-10-11 17:56:24"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_280_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          11),
  ("fsize_db",              21797314763),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.80GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-23 18:51:50"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_300_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_2v2t"),
  ("nof_db_events",         299996),
  ("nof_db_files",          16),
  ("fsize_db",              16029048036),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.03GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-11 17:37:53"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_320_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_2v2t"),
  ("nof_db_events",         293996),
  ("nof_db_files",          19),
  ("fsize_db",              15888556444),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.89GB; nevents: 294.00k; release: 10_2_5; last modified: 2019-11-11 17:37:58"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_350_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_2v2t"),
  ("nof_db_events",         299993),
  ("nof_db_files",          5),
  ("fsize_db",              15974763144),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.97GB; nevents: 299.99k; release: 10_2_5; last modified: 2019-10-29 11:18:12"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_400_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_2v2t"),
  ("nof_db_events",         278994),
  ("nof_db_files",          17),
  ("fsize_db",              15658111382),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.66GB; nevents: 278.99k; release: 10_2_5; last modified: 2019-11-08 12:42:55"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_450_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_2v2t"),
  ("nof_db_events",         293997),
  ("nof_db_files",          23),
  ("fsize_db",              17725740224),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.73GB; nevents: 294.00k; release: 10_2_5; last modified: 2019-11-07 20:03:26"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_2v2t"),
  ("nof_db_events",         299996),
  ("nof_db_files",          6),
  ("fsize_db",              18359036586),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.36GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-11 02:28:29"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_550_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_2v2t"),
  ("nof_db_events",         295998),
  ("nof_db_files",          16),
  ("fsize_db",              16949359291),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.95GB; nevents: 296.00k; release: 10_2_5; last modified: 2019-11-07 03:41:14"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_600_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          14),
  ("fsize_db",              11943067602),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.94GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-06 08:48:57"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_650_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_2v2t"),
  ("nof_db_events",         199995),
  ("nof_db_files",          5),
  ("fsize_db",              11686132211),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.69GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-12 10:45:36"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_700_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_2v2t"),
  ("nof_db_events",         199995),
  ("nof_db_files",          4),
  ("fsize_db",              12840929781),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.84GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-10 22:35:20"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_750_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_2v2t"),
  ("nof_db_events",         196000),
  ("nof_db_files",          15),
  ("fsize_db",              12970290914),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.97GB; nevents: 196.00k; release: 10_2_5; last modified: 2019-11-03 02:40:47"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_800_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          18),
  ("fsize_db",              13346223144),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.35GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-07 03:40:23"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_850_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_2v2t"),
  ("nof_db_events",         193998),
  ("nof_db_files",          8),
  ("fsize_db",              13004188270),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.00GB; nevents: 194.00k; release: 10_2_5; last modified: 2019-11-06 18:12:31"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_900_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          6),
  ("fsize_db",              13219528779),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.22GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-11 06:46:49"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          4),
  ("fsize_db",              6685081658),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.69GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 06:46:25"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_2v2t"),
  ("nof_db_events",         96999),
  ("nof_db_files",          9),
  ("fsize_db",              6424419348),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.42GB; nevents: 97.00k; release: 10_2_5; last modified: 2019-11-06 23:25:06"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          5),
  ("fsize_db",              6512314789),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.51GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-14 08:47:43"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          14),
  ("fsize_db",              7078717091),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.08GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-06 08:49:52"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_2v2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6969030499),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.97GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 02:28:25"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_2v2t"),
  ("nof_db_events",         99997),
  ("nof_db_files",          5),
  ("fsize_db",              8227083083),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 8.23GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-15 06:27:30"),
])

meta_dictionary["/GluGluToRadionToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToRadionToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          8),
  ("fsize_db",              8326148543),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 8.33GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-15 07:19:37"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_250_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_250_hh_2v2t"),
  ("nof_db_events",         383996),
  ("nof_db_files",          17),
  ("fsize_db",              24278727790),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.28GB; nevents: 384.00k; release: 10_2_5; last modified: 2019-10-31 12:38:16"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_260_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_260_hh_2v2t"),
  ("nof_db_events",         389991),
  ("nof_db_files",          23),
  ("fsize_db",              26571434322),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.57GB; nevents: 389.99k; release: 10_2_5; last modified: 2019-11-03 07:55:43"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_270_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_270_hh_2v2t"),
  ("nof_db_events",         399996),
  ("nof_db_files",          10),
  ("fsize_db",              27386438209),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 27.39GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-11 10:32:32"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_280_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_280_hh_2v2t"),
  ("nof_db_events",         399997),
  ("nof_db_files",          11),
  ("fsize_db",              27556511297),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 27.56GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-11 18:01:15"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_300_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_300_hh_2v2t"),
  ("nof_db_events",         293996),
  ("nof_db_files",          30),
  ("fsize_db",              20555029971),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.56GB; nevents: 294.00k; release: 10_2_5; last modified: 2019-11-06 23:13:06"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_320_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_320_hh_2v2t"),
  ("nof_db_events",         299996),
  ("nof_db_files",          8),
  ("fsize_db",              20860701519),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.86GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-11 17:57:18"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_350_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_350_hh_2v2t"),
  ("nof_db_events",         299996),
  ("nof_db_files",          6),
  ("fsize_db",              21462869404),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.46GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-13 06:59:48"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_400_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_400_hh_2v2t"),
  ("nof_db_events",         299992),
  ("nof_db_files",          9),
  ("fsize_db",              21940279980),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.94GB; nevents: 299.99k; release: 10_2_5; last modified: 2019-10-13 20:21:19"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_450_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_450_hh_2v2t"),
  ("nof_db_events",         299993),
  ("nof_db_files",          7),
  ("fsize_db",              22350188940),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.35GB; nevents: 299.99k; release: 10_2_5; last modified: 2019-10-13 05:10:39"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_500_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_500_hh_2v2t"),
  ("nof_db_events",         299992),
  ("nof_db_files",          7),
  ("fsize_db",              21732849779),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.73GB; nevents: 299.99k; release: 10_2_5; last modified: 2019-10-12 11:44:18"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_550_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_550_hh_2v2t"),
  ("nof_db_events",         299994),
  ("nof_db_files",          8),
  ("fsize_db",              22027024008),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.03GB; nevents: 299.99k; release: 10_2_5; last modified: 2019-10-13 20:21:32"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_vbf_spin0_600_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_600_hh_2v2t"),
  ("nof_db_events",         199993),
  ("nof_db_files",          6),
  ("fsize_db",              15551759262),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.55GB; nevents: 199.99k; release: 10_2_5; last modified: 2019-10-15 07:16:14"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_650_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_650_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          9),
  ("fsize_db",              13853892609),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.85GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-13 08:58:21"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_700_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_700_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          13),
  ("fsize_db",              14045165712),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.05GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-04 05:46:24"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_750_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_750_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          14),
  ("fsize_db",              14174590935),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.17GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-11 06:43:37"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_800_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_800_hh_2v2t"),
  ("nof_db_events",         191996),
  ("nof_db_files",          11),
  ("fsize_db",              13643630164),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.64GB; nevents: 192.00k; release: 10_2_5; last modified: 2019-12-03 11:53:34"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_850_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_850_hh_2v2t"),
  ("nof_db_events",         199993),
  ("nof_db_files",          11),
  ("fsize_db",              14301131301),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.30GB; nevents: 199.99k; release: 10_2_5; last modified: 2020-01-14 20:59:46"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_900_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_900_hh_2v2t"),
  ("nof_db_events",         199999),
  ("nof_db_files",          13),
  ("fsize_db",              14436186956),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 14.44GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-03 11:54:28"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1000_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_1000_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          9),
  ("fsize_db",              7357026530),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.36GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-01-04 03:34:28"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1250_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_1250_hh_2v2t"),
  ("nof_db_events",         99997),
  ("nof_db_files",          8),
  ("fsize_db",              7500010088),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.50GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-03 11:48:43"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1500_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_1500_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          13),
  ("fsize_db",              7713759404),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.71GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-04 08:27:46"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_1750_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_1750_hh_2v2t"),
  ("nof_db_events",         98998),
  ("nof_db_files",          11),
  ("fsize_db",              7662155139),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.66GB; nevents: 99.00k; release: 10_2_5; last modified: 2020-02-04 05:35:12"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_2000_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_2000_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          8),
  ("fsize_db",              7724622965),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.72GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-03 11:51:34"),
])

meta_dictionary["/VBFToRadionToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToRadionToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_vbf_spin0_3000_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin0_3000_hh_2v2t"),
  ("nof_db_events",         99996),
  ("nof_db_files",          10),
  ("fsize_db",              7943067646),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.94GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-15 13:22:32"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_250_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_2v2t"),
  ("nof_db_events",         391996),
  ("nof_db_files",          18),
  ("fsize_db",              20055994832),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.06GB; nevents: 392.00k; release: 10_2_5; last modified: 2019-11-07 03:36:08"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_260_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_2v2t"),
  ("nof_db_events",         399991),
  ("nof_db_files",          17),
  ("fsize_db",              20560214076),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.56GB; nevents: 399.99k; release: 10_2_5; last modified: 2019-11-06 08:51:22"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_270_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_2v2t"),
  ("nof_db_events",         397996),
  ("nof_db_files",          10),
  ("fsize_db",              22172374707),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.17GB; nevents: 398.00k; release: 10_2_5; last modified: 2019-10-15 07:09:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_280_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_2v2t"),
  ("nof_db_events",         399992),
  ("nof_db_files",          17),
  ("fsize_db",              20820001722),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.82GB; nevents: 399.99k; release: 10_2_5; last modified: 2019-11-08 05:12:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_300_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_2v2t"),
  ("nof_db_events",         297998),
  ("nof_db_files",          20),
  ("fsize_db",              17126493878),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.13GB; nevents: 298.00k; release: 10_2_5; last modified: 2019-11-12 10:44:00"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_320_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_2v2t"),
  ("nof_db_events",         299995),
  ("nof_db_files",          6),
  ("fsize_db",              16154095425),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.15GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-10-12 05:37:38"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_350_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_2v2t"),
  ("nof_db_events",         295998),
  ("nof_db_files",          9),
  ("fsize_db",              16258445329),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.26GB; nevents: 296.00k; release: 10_2_5; last modified: 2019-10-30 17:12:32"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_400_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_2v2t"),
  ("nof_db_events",         297995),
  ("nof_db_files",          19),
  ("fsize_db",              17915945878),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.92GB; nevents: 298.00k; release: 10_2_5; last modified: 2019-11-11 20:51:05"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_450_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_2v2t"),
  ("nof_db_events",         284994),
  ("nof_db_files",          16),
  ("fsize_db",              16848799352),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.85GB; nevents: 284.99k; release: 10_2_5; last modified: 2019-10-29 01:06:22"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_2v2t"),
  ("nof_db_events",         299996),
  ("nof_db_files",          15),
  ("fsize_db",              17493740155),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.49GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-11 20:53:10"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_550_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_2v2t"),
  ("nof_db_events",         299996),
  ("nof_db_files",          20),
  ("fsize_db",              17710981794),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.71GB; nevents: 300.00k; release: 10_2_5; last modified: 2019-11-03 07:55:58"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_600_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          16),
  ("fsize_db",              11919833002),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.92GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-11 20:50:25"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_650_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          9),
  ("fsize_db",              11994685720),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.99GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-23 22:41:53"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_700_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_2v2t"),
  ("nof_db_events",         199999),
  ("nof_db_files",          6),
  ("fsize_db",              12072988172),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.07GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-10-13 21:33:50"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_750_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_2v2t"),
  ("nof_db_events",         197997),
  ("nof_db_files",          20),
  ("fsize_db",              13158550685),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.16GB; nevents: 198.00k; release: 10_2_5; last modified: 2019-11-28 18:28:19"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_800_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_2v2t"),
  ("nof_db_events",         199995),
  ("nof_db_files",          13),
  ("fsize_db",              12213814696),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.21GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-11 17:37:47"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_850_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          17),
  ("fsize_db",              12732436951),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 12.73GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-11-30 04:19:52"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_ggf_spin2_900_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_2v2t"),
  ("nof_db_events",         195995),
  ("nof_db_files",          18),
  ("fsize_db",              13482710118),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 13.48GB; nevents: 196.00k; release: 10_2_5; last modified: 2019-11-11 19:05:09"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          8),
  ("fsize_db",              6814333152),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.81GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-24 00:02:28"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_2v2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              6700622854),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.70GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-14 02:55:07"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          4),
  ("fsize_db",              6724912073),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.72GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 19:46:17"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_2v2t"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6757238050),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.76GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-12 16:54:31"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          4),
  ("fsize_db",              7030476859),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.03GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-12 21:37:57"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_2v2t"),
  ("nof_db_events",         99996),
  ("nof_db_files",          4),
  ("fsize_db",              7124837516),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.12GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-10-11 15:50:13"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_wwtt"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_2v2t"),
  ("nof_db_events",         99997),
  ("nof_db_files",          15),
  ("fsize_db",              6801982100),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.80GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-11-10 00:38:22"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_250_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_250_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          22),
  ("fsize_db",              24054774128),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.05GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-12-18 05:11:48"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_260_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_260_hh_2v2t"),
  ("nof_db_events",         399988),
  ("nof_db_files",          17),
  ("fsize_db",              22637330314),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.64GB; nevents: 399.99k; release: 10_2_5; last modified: 2019-12-18 01:38:08"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_270_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_270_hh_2v2t"),
  ("nof_db_events",         399997),
  ("nof_db_files",          20),
  ("fsize_db",              22515385410),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.52GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-12-18 01:17:06"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_280_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_280_hh_2v2t"),
  ("nof_db_events",         387993),
  ("nof_db_files",          21),
  ("fsize_db",              21745034723),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.75GB; nevents: 387.99k; release: 10_2_5; last modified: 2020-01-04 12:32:15"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_300_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_300_hh_2v2t"),
  ("nof_db_events",         299998),
  ("nof_db_files",          14),
  ("fsize_db",              16963251239),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.96GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-02-14 10:40:34"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_320_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_320_hh_2v2t"),
  ("nof_db_events",         299992),
  ("nof_db_files",          16),
  ("fsize_db",              16652379052),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.65GB; nevents: 299.99k; release: 10_2_5; last modified: 2020-01-13 10:22:00"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_350_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_350_hh_2v2t"),
  ("nof_db_events",         284992),
  ("nof_db_files",          15),
  ("fsize_db",              15762362705),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 15.76GB; nevents: 284.99k; release: 10_2_5; last modified: 2020-01-14 00:55:32"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_400_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_400_hh_2v2t"),
  ("nof_db_events",         296996),
  ("nof_db_files",          15),
  ("fsize_db",              16521281646),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.52GB; nevents: 297.00k; release: 10_2_5; last modified: 2019-12-07 18:27:38"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_450_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_450_hh_2v2t"),
  ("nof_db_events",         299998),
  ("nof_db_files",          17),
  ("fsize_db",              16625335022),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.63GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-02-25 01:47:25"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_500_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_500_hh_2v2t"),
  ("nof_db_events",         299997),
  ("nof_db_files",          20),
  ("fsize_db",              16847345601),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 16.85GB; nevents: 300.00k; release: 10_2_5; last modified: 2020-02-15 00:50:38"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_550_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_550_hh_2v2t"),
  ("nof_db_events",         299993),
  ("nof_db_files",          16),
  ("fsize_db",              17390260115),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 17.39GB; nevents: 299.99k; release: 10_2_5; last modified: 2020-02-10 21:46:37"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_600_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_600_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          14),
  ("fsize_db",              11461789019),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.46GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-04 05:52:04"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_650_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_650_hh_2v2t"),
  ("nof_db_events",         200000),
  ("nof_db_files",          11),
  ("fsize_db",              11185859826),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.19GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-08 02:42:35"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_700_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_700_hh_2v2t"),
  ("nof_db_events",         199996),
  ("nof_db_files",          14),
  ("fsize_db",              11512583657),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.51GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-17 19:23:38"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_750_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_750_hh_2v2t"),
  ("nof_db_events",         199994),
  ("nof_db_files",          14),
  ("fsize_db",              11559274596),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.56GB; nevents: 199.99k; release: 10_2_5; last modified: 2019-12-08 02:44:46"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_800_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_800_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          10),
  ("fsize_db",              11741664635),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.74GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-03 11:47:28"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_850_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_850_hh_2v2t"),
  ("nof_db_events",         199998),
  ("nof_db_files",          14),
  ("fsize_db",              11434850687),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.43GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-03 11:41:34"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_vbf_spin2_900_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_900_hh_2v2t"),
  ("nof_db_events",         199997),
  ("nof_db_files",          12),
  ("fsize_db",              11404514844),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 11.40GB; nevents: 200.00k; release: 10_2_5; last modified: 2019-12-07 09:26:08"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_1000_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_1000_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          8),
  ("fsize_db",              5759188056),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.76GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-03 11:43:38"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-1200_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_1200_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_1200_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          7),
  ("fsize_db",              5800432824),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.80GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-07 09:24:06"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_1250_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_1250_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          11),
  ("fsize_db",              6064296650),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.06GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-08 22:11:43"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_1500_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_1500_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          7),
  ("fsize_db",              6002045697),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.00GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-03-02 13:34:05"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_1750_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_1750_hh_2v2t"),
  ("nof_db_events",         95997),
  ("nof_db_files",          8),
  ("fsize_db",              5595401383),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.60GB; nevents: 96.00k; release: 10_2_5; last modified: 2020-02-12 18:29:14"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_2000_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_2000_hh_2v2t"),
  ("nof_db_events",         99999),
  ("nof_db_files",          12),
  ("fsize_db",              5933132461),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 5.93GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-04 05:33:36"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_2500_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_2500_hh_2v2t"),
  ("nof_db_events",         99997),
  ("nof_db_files",          7),
  ("fsize_db",              6048578056),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.05GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-18 10:07:00"),
])

meta_dictionary["/VBFToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_VBFToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_spin2_3000_hh_wwtt"),
  ("process_name_specific", "signal_vbf_spin2_3000_hh_2v2t"),
  ("nof_db_events",         99998),
  ("nof_db_files",          6),
  ("fsize_db",              6043078205),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.04GB; nevents: 100.00k; release: 10_2_5; last modified: 2019-12-04 05:34:25"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_250_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_250_hh_4v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          18),
  ("fsize_db",              21207113276),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.21GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 10:58:06"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_260_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_260_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          22),
  ("fsize_db",              20436296039),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.44GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 11:09:52"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_270_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_270_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          18),
  ("fsize_db",              20604091050),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.60GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-06 23:54:59"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_280_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_280_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          19),
  ("fsize_db",              21513442041),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.51GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 22:06:03"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_300_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_300_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          21),
  ("fsize_db",              21040222568),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.04GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 10:59:00"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_320_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_320_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          19),
  ("fsize_db",              20981319223),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.98GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-09 01:49:59"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_350_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_350_hh_4v"),
  ("nof_db_events",         394997),
  ("nof_db_files",          19),
  ("fsize_db",              21093280463),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.09GB; nevents: 395.00k; release: 10_2_5; last modified: 2020-09-09 07:52:38"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_400_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_400_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          17),
  ("fsize_db",              21900594279),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.90GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 05:21:58"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_450_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_450_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          10),
  ("fsize_db",              22749661838),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.75GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-09 01:51:45"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_500_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          21),
  ("fsize_db",              23888325634),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.89GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 10:59:40"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_550_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_550_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          16),
  ("fsize_db",              21920359480),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.92GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-13 17:40:56"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_600_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_600_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          22),
  ("fsize_db",              24624773678),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.62GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 11:00:15"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_650_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_650_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          12),
  ("fsize_db",              24163209445),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.16GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 00:50:55"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_700_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_700_hh_4v"),
  ("nof_db_events",         399993),
  ("nof_db_files",          19),
  ("fsize_db",              25131830524),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.13GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-10 20:54:23"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_750_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_750_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          17),
  ("fsize_db",              25342935304),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.34GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 18:52:50"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_800_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_800_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          12),
  ("fsize_db",              25519024835),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.52GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 00:49:05"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct17_GluGluToRadionToHHTo4V_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_850_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_850_hh_4v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          17),
  ("fsize_db",              24098840264),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.10GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 22:56:25"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_900_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_900_hh_4v"),
  ("nof_db_events",         399995),
  ("nof_db_files",          19),
  ("fsize_db",              25838972055),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.84GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-06 17:53:47"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_1000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_1000_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          18),
  ("fsize_db",              26086811862),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.09GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-09 03:48:50"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_1250_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_1250_hh_4v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          7),
  ("fsize_db",              6253325588),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.25GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-17 03:09:47"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_1500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_1500_hh_4v"),
  ("nof_db_events",         99998),
  ("nof_db_files",          4),
  ("fsize_db",              6022977751),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.02GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-16 03:15:42"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_1750_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_1750_hh_4v_PSWeights"),
  ("nof_db_events",         100000),
  ("nof_db_files",          9),
  ("fsize_db",              6492547817),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.49GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-10-08 20:50:44"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_spin0_2000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_2000_hh_4v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          6),
  ("fsize_db",              6218068891),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.22GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-18 09:09:17"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_2500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_2500_hh_4v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          11),
  ("fsize_db",              7092441419),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.09GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-15 14:43:42"),
])

meta_dictionary["/GluGluToRadionToHHTo4V_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToRadionToHHTo4V_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_spin0_3000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin0_3000_hh_4v"),
  ("nof_db_events",         99999),
  ("nof_db_files",          7),
  ("fsize_db",              7517374490),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.52GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-12 22:50:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_250_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_250_hh_4v"),
  ("nof_db_events",         395997),
  ("nof_db_files",          21),
  ("fsize_db",              20362821567),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.36GB; nevents: 396.00k; release: 10_2_5; last modified: 2020-09-11 20:57:43"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-260_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_260_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_260_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          12),
  ("fsize_db",              20681386539),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 20.68GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-09 07:52:33"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-270_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_270_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_270_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          18),
  ("fsize_db",              21144866001),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.14GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 05:20:08"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-280_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_280_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_280_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          13),
  ("fsize_db",              21015414734),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.02GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-07 03:49:38"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-300_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_300_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_300_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          13),
  ("fsize_db",              21130830157),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.13GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-07 11:52:14"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_320_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_320_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          12),
  ("fsize_db",              21905276558),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.91GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-06 23:54:09"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-350_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_350_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_350_hh_4v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          20),
  ("fsize_db",              22401037955),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.40GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 11:04:21"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-400_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_400_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_400_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          20),
  ("fsize_db",              22659470426),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.66GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 14:52:06"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-450_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_450_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_450_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          17),
  ("fsize_db",              23584490800),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.58GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-12 02:53:04"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_500_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          15),
  ("fsize_db",              23572679192),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.57GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-06 23:55:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-550_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_550_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_550_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          17),
  ("fsize_db",              22595039752),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.60GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-13 10:44:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-600_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_600_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_600_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          19),
  ("fsize_db",              22894068907),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.89GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-12 15:08:14"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-650_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_650_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_650_hh_4v"),
  ("nof_db_events",         399995),
  ("nof_db_files",          19),
  ("fsize_db",              23092978786),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.09GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-12 05:00:35"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-700_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_700_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_700_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          18),
  ("fsize_db",              25015217730),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.02GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 08:53:41"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct17_GluGluToBulkGravitonToHHTo4V_M-750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_750_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_750_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          18),
  ("fsize_db",              23376157301),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.38GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-13 20:40:41"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-800_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_800_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_800_hh_4v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          20),
  ("fsize_db",              23808627871),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.81GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 16:04:14"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-850_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_850_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_850_hh_4v"),
  ("nof_db_events",         399998),
  ("nof_db_files",          17),
  ("fsize_db",              24730371281),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.73GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-21 19:02:20"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-900_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_ggf_spin2_900_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_900_hh_4v"),
  ("nof_db_events",         399995),
  ("nof_db_files",          17),
  ("fsize_db",              24758813025),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.76GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-12 00:52:59"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_1000_hh_4v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          22),
  ("fsize_db",              24280089329),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.28GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-14 02:46:28"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1250_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_1250_hh_4v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          4),
  ("fsize_db",              6902357499),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.90GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-13 00:47:12"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_1500_hh_4v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              6474473667),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 6.47GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-14 15:59:49"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_1750_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_1750_hh_4v"),
  ("nof_db_events",         99998),
  ("nof_db_files",          6),
  ("fsize_db",              6998650656),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.00GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-13 04:50:02"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_2000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_2000_hh_4v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              7030232088),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.03GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-14 06:43:43"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_2500_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_2500_hh_4v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              7141126152),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.14GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-15 21:56:01"),
])

meta_dictionary["/GluGluToBulkGravitonToHHTo4V_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToBulkGravitonToHHTo4V_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-"),
  ("sample_category",       "signal_ggf_spin2_3000_hh_wwww"),
  ("process_name_specific", "signal_ggf_spin2_3000_hh_4v"),
  ("nof_db_events",         100000),
  ("nof_db_files",          10),
  ("fsize_db",              7577431106),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 7.58GB; nevents: 100.00k; release: 10_2_5; last modified: 2020-09-13 23:41:06"),
])

meta_dictionary["/VBFHHTo4T_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4T_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          18),
  ("fsize_db",              22634108447),
  ("xsection",              6.785e-06),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.63GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-26 13:23:33"),
])

meta_dictionary["/VBFHHTo4T_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4T_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_4t_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          18),
  ("fsize_db",              23291656236),
  ("xsection",              5.5932e-06),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.29GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 10:13:15"),
])

meta_dictionary["/VBFHHTo4T_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4T_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_4t_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          20),
  ("fsize_db",              24351698585),
  ("xsection",              5.5891e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.35GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-26 12:23:54"),
])

meta_dictionary["/VBFHHTo4T_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4T_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_4t_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          19),
  ("fsize_db",              22543007356),
  ("xsection",              1.81178e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.54GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 05:14:45"),
])

meta_dictionary["/VBFHHTo4T_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4T_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          17),
  ("fsize_db",              23661885213),
  ("xsection",              4.25487e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.66GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-10-03 06:09:53"),
])

meta_dictionary["/VBFHHTo4T_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4T_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_db_events",         375000),
  ("nof_db_files",          15),
  ("fsize_db",              21561349932),
  ("xsection",              0.0002595228),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.56GB; nevents: 375.00k; release: 10_2_5; last modified: 2020-10-11 06:58:34"),
])

meta_dictionary["/VBFHHTo4T_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4T_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_tttt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_4t_dipoleRecoilOff"),
  ("nof_db_events",         400000),
  ("nof_db_files",          22),
  ("fsize_db",              23646552081),
  ("xsection",              0.0001064477),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.65GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-29 07:01:13"),
])

meta_dictionary["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2V2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_wwtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_db_events",         399991),
  ("nof_db_files",          20),
  ("fsize_db",              23485176323),
  ("xsection",              5.19e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.49GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-26 04:20:48"),
])

meta_dictionary["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2V2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_wwtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_2v2t_dipoleRecoilOff"),
  ("nof_db_events",         399994),
  ("nof_db_files",          17),
  ("fsize_db",              23678895847),
  ("xsection",              4.27833e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.68GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-29 07:00:17"),
])

meta_dictionary["/VBFHHTo2V2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2V2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_wwtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          22),
  ("fsize_db",              25781900117),
  ("xsection",              0.0004275219),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.78GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-28 03:13:25"),
])

meta_dictionary["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2V2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_wwtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_2v2t_dipoleRecoilOff"),
  ("nof_db_events",         399993),
  ("nof_db_files",          16),
  ("fsize_db",              22676342101),
  ("xsection",              0.0001385868),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.68GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-28 07:13:40"),
])

meta_dictionary["/VBFHHTo2V2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2V2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_wwtt"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_db_events",         399993),
  ("nof_db_files",          22),
  ("fsize_db",              24807340471),
  ("xsection",              0.0003254642),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.81GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-30 02:13:44"),
])

meta_dictionary["/VBFHHTo2V2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2V2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_wwtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_db_events",         399996),
  ("nof_db_files",          23),
  ("fsize_db",              24518198124),
  ("xsection",              0.0019851452),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.52GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-28 06:15:31"),
])

meta_dictionary["/VBFHHTo2V2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo2V2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_wwtt"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_db_events",         399993),
  ("nof_db_files",          23),
  ("fsize_db",              24896105301),
  ("xsection",              0.0008142775),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.90GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-29 01:04:40"),
])

meta_dictionary["/VBFHHTo4V_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4V_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_1_1_hh_wwww"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_1_hh_4v_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          26),
  ("fsize_db",              23364632294),
  ("xsection",              9.92524e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.36GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-29 17:08:46"),
])

meta_dictionary["/VBFHHTo4V_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal_vbf_nonresonant_1_1_2_hh_wwww"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_2_hh_4v_dipoleRecoilOff"),
  ("nof_db_events",         387999),
  ("nof_db_files",          18),
  ("fsize_db",              23310667051),
  ("xsection",              8.18177e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.31GB; nevents: 388.00k; release: 10_2_5; last modified: 2020-09-29 08:02:50"),
])

meta_dictionary["/VBFHHTo4V_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           ""),
  ("sample_category",       "signal_vbf_nonresonant_1_1_0_hh_wwww"),
  ("process_name_specific", "signal_vbf_nonresonant_1_1_0_hh_4v_dipoleRecoilOff"),
  ("nof_db_events",         399997),
  ("nof_db_files",          25),
  ("fsize_db",              23821650265),
  ("xsection",              0.00026503),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "status: VALID; size: 23.82GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 08:13:55"),
])

meta_dictionary["/VBFHHTo4V_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4V_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_2_1_hh_wwww"),
  ("process_name_specific", "signal_vbf_nonresonant_1_2_1_hh_4v_dipoleRecoilOff"),
  ("nof_db_events",         399998),
  ("nof_db_files",          23),
  ("fsize_db",              26493017055),
  ("xsection",              0.0008175824),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.49GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-28 10:14:07"),
])

meta_dictionary["/VBFHHTo4V_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4V_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_nonresonant_0p5_1_1_hh_wwww"),
  ("process_name_specific", "signal_vbf_nonresonant_0p5_1_1_hh_4v_dipoleRecoilOff"),
  ("nof_db_events",         399997),
  ("nof_db_files",          21),
  ("fsize_db",              26069132478),
  ("xsection",              0.0006224099),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 26.07GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-29 08:02:45"),
])

meta_dictionary["/VBFHHTo4V_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4V_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15"),
  ("sample_category",       "signal_vbf_nonresonant_1p5_1_1_hh_wwww"),
  ("process_name_specific", "signal_vbf_nonresonant_1p5_1_1_hh_4v_dipoleRecoilOff"),
  ("nof_db_events",         399995),
  ("nof_db_files",          23),
  ("fsize_db",              25037107007),
  ("xsection",              0.0037963435),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.04GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-28 18:15:18"),
])

meta_dictionary["/VBFHHTo4V_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_VBFHHTo4V_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v"),
  ("sample_category",       "signal_vbf_nonresonant_1_0_1_hh_wwww"),
  ("process_name_specific", "signal_vbf_nonresonant_1_0_1_hh_4v_dipoleRecoilOff"),
  ("nof_db_events",         399999),
  ("nof_db_files",          22),
  ("fsize_db",              25496879832),
  ("xsection",              0.0037963435),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.50GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-28 17:17:24"),
])

meta_dictionary["/GluGluToHHTo4T_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          22),
  ("fsize_db",              22565271440),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.57GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-11-30 04:19:15"),
])

meta_dictionary["/GluGluToHHTo4T_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4T_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          11),
  ("fsize_db",              21720556796),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.72GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-28 10:13:07"),
])

meta_dictionary["/GluGluToHHTo4T_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_4t"),
  ("nof_db_events",         396000),
  ("nof_db_files",          24),
  ("fsize_db",              22812356401),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.81GB; nevents: 396.00k; release: 10_2_5; last modified: 2019-11-30 07:31:18"),
])

meta_dictionary["/GluGluToHHTo4T_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          8),
  ("fsize_db",              22577919040),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.58GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-12 01:41:29"),
])

meta_dictionary["/GluGluToHHTo4T_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_4t"),
  ("nof_db_events",         394000),
  ("nof_db_files",          28),
  ("fsize_db",              23345042125),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.35GB; nevents: 394.00k; release: 10_2_5; last modified: 2019-11-10 11:53:39"),
])

meta_dictionary["/GluGluToHHTo4T_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          10),
  ("fsize_db",              22616576770),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.62GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-13 05:10:24"),
])

meta_dictionary["/GluGluToHHTo4T_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          21),
  ("fsize_db",              22434110190),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.43GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-11-27 21:30:12"),
])

meta_dictionary["/GluGluToHHTo4T_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_4t"),
  ("nof_db_events",         397000),
  ("nof_db_files",          9),
  ("fsize_db",              22349849698),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.35GB; nevents: 397.00k; release: 10_2_5; last modified: 2019-10-14 04:44:02"),
])

meta_dictionary["/GluGluToHHTo4T_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_4t"),
  ("nof_db_events",         388000),
  ("nof_db_files",          24),
  ("fsize_db",              21577784792),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 21.58GB; nevents: 388.00k; release: 10_2_5; last modified: 2019-10-31 12:38:35"),
])

meta_dictionary["/GluGluToHHTo4T_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          20),
  ("fsize_db",              23501535916),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.50GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-28 22:16:55"),
])

meta_dictionary["/GluGluToHHTo4T_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_4t"),
  ("nof_db_events",         397000),
  ("nof_db_files",          21),
  ("fsize_db",              22257366649),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.26GB; nevents: 397.00k; release: 10_2_5; last modified: 2019-11-11 17:38:13"),
])

meta_dictionary["/GluGluToHHTo4T_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_4t"),
  ("nof_db_events",         398000),
  ("nof_db_files",          26),
  ("fsize_db",              23587120978),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.59GB; nevents: 398.00k; release: 10_2_5; last modified: 2019-11-28 18:29:24"),
])

meta_dictionary["/GluGluToHHTo4T_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4T_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_4t"),
  ("nof_db_events",         400000),
  ("nof_db_files",          8),
  ("fsize_db",              22176978836),
  ("xsection",              0.003934),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.18GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-12 16:55:00"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_4t"),
  ("nof_db_events",         979100),
  ("nof_db_files",          29),
  ("fsize_db",              46583707050),
  ("xsection",              0.00026349),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 46.58GB; nevents: 979.10k; release: 10_2_5; last modified: 2020-03-13 08:58:50"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_4t"),
  ("nof_db_events",         963000),
  ("nof_db_files",          56),
  ("fsize_db",              46586377730),
  ("xsection",              0.00011734),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 46.59GB; nevents: 963.00k; release: 10_2_5; last modified: 2020-03-31 16:03:15"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_4t"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          33),
  ("fsize_db",              48200072580),
  ("xsection",              4.97e-05),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 48.20GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-03-21 23:48:07"),
])

meta_dictionary["/GluGluToHHTo4Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_tttt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_4t"),
  ("nof_db_events",         1000000),
  ("nof_db_files",          37),
  ("fsize_db",              46823526474),
  ("xsection",              0.00034666),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 46.82GB; nevents: 1.00M; release: 10_2_5; last modified: 2020-03-13 09:00:18"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_2v2t"),
  ("nof_db_events",         393993),
  ("nof_db_files",          18),
  ("fsize_db",              24027472831),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.03GB; nevents: 393.99k; release: 10_2_5; last modified: 2019-11-06 14:12:49"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo2V2Tau_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          11),
  ("fsize_db",              22878549981),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.88GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-27 00:16:12"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_2v2t"),
  ("nof_db_events",         399994),
  ("nof_db_files",          15),
  ("fsize_db",              25778291187),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.78GB; nevents: 399.99k; release: 10_2_5; last modified: 2019-10-24 00:03:13"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_2v2t"),
  ("nof_db_events",         395996),
  ("nof_db_files",          25),
  ("fsize_db",              24237765625),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.24GB; nevents: 396.00k; release: 10_2_5; last modified: 2019-11-11 17:36:42"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          19),
  ("fsize_db",              24245036817),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.25GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-30 14:41:58"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_2v2t"),
  ("nof_db_events",         397992),
  ("nof_db_files",          24),
  ("fsize_db",              24407491284),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.41GB; nevents: 397.99k; release: 10_2_5; last modified: 2019-11-11 17:37:18"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_2v2t"),
  ("nof_db_events",         393990),
  ("nof_db_files",          25),
  ("fsize_db",              23907169624),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.91GB; nevents: 393.99k; release: 10_2_5; last modified: 2019-11-11 19:04:19"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_2v2t"),
  ("nof_db_events",         395994),
  ("nof_db_files",          21),
  ("fsize_db",              24013488664),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.01GB; nevents: 395.99k; release: 10_2_5; last modified: 2019-11-06 18:13:47"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_2v2t"),
  ("nof_db_events",         399995),
  ("nof_db_files",          16),
  ("fsize_db",              22774541667),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.77GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-24 12:00:06"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_2v2t"),
  ("nof_db_events",         399993),
  ("nof_db_files",          9),
  ("fsize_db",              25563876624),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.56GB; nevents: 399.99k; release: 10_2_5; last modified: 2019-10-15 06:57:52"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_2v2t"),
  ("nof_db_events",         399996),
  ("nof_db_files",          11),
  ("fsize_db",              23894007583),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.89GB; nevents: 400.00k; release: 10_2_5; last modified: 2019-10-11 17:56:09"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_2v2t"),
  ("nof_db_events",         399991),
  ("nof_db_files",          8),
  ("fsize_db",              22984187913),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.98GB; nevents: 399.99k; release: 10_2_5; last modified: 2019-10-13 00:47:24"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("nof_db_events",         399994),
  ("nof_db_files",          27),
  ("fsize_db",              23989311263),
  ("xsection",              0.030092),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.99GB; nevents: 399.99k; release: 10_2_5; last modified: 2019-10-30 17:10:57"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_2v2t"),
  ("nof_db_events",         399991),
  ("nof_db_files",          23),
  ("fsize_db",              19678248548),
  ("xsection",              0.0020155),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.68GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-03-26 12:55:07"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_2v2t"),
  ("nof_db_events",         396992),
  ("nof_db_files",          18),
  ("fsize_db",              19734784964),
  ("xsection",              0.00089753),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.73GB; nevents: 396.99k; release: 10_2_5; last modified: 2020-03-20 09:45:41"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
  ("nof_db_events",         383094),
  ("nof_db_files",          24),
  ("fsize_db",              19131899752),
  ("xsection",              0.00038015),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 19.13GB; nevents: 383.09k; release: 10_2_5; last modified: 2020-03-04 08:31:02"),
])

meta_dictionary["/GluGluToHHTo2V2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo2V2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_wwtt"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_2v2t"),
  ("nof_db_events",         386288),
  ("nof_db_files",          21),
  ("fsize_db",              18478360608),
  ("xsection",              0.00265166),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 18.48GB; nevents: 386.29k; release: 10_2_5; last modified: 2020-03-20 03:45:31"),
])

meta_dictionary["/GluGluToHHTo4V_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_SM_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_sm_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          17),
  ("fsize_db",              22993961841),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.99GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 23:48:39"),
])

meta_dictionary["/GluGluToHHTo4V_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_1_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          17),
  ("fsize_db",              22758752072),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.76GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-04 20:55:56"),
])

meta_dictionary["/GluGluToHHTo4V_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_2_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_2_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          29),
  ("fsize_db",              25130419268),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 25.13GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-06 15:55:09"),
])

meta_dictionary["/GluGluToHHTo4V_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_3_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_3_hh_4v"),
  ("nof_db_events",         399994),
  ("nof_db_files",          25),
  ("fsize_db",              23079089709),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.08GB; nevents: 399.99k; release: 10_2_5; last modified: 2020-09-10 05:17:38"),
])

meta_dictionary["/GluGluToHHTo4V_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_4_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          19),
  ("fsize_db",              22874788644),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.87GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-06 11:54:00"),
])

meta_dictionary["/GluGluToHHTo4V_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_5_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          17),
  ("fsize_db",              23210648345),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.21GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-05 01:05:55"),
])

meta_dictionary["/GluGluToHHTo4V_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_6_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          15),
  ("fsize_db",              22829868112),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.83GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 16:53:13"),
])

meta_dictionary["/GluGluToHHTo4V_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_7_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_7_hh_4v"),
  ("nof_db_events",         399996),
  ("nof_db_files",          25),
  ("fsize_db",              23592765986),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.59GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-09 13:50:46"),
])

meta_dictionary["/GluGluToHHTo4V_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_8_hh_4v"),
  ("nof_db_events",         399997),
  ("nof_db_files",          27),
  ("fsize_db",              23280917922),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.28GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-09 01:51:20"),
])

meta_dictionary["/GluGluToHHTo4V_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_9_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_9_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          22),
  ("fsize_db",              24945614295),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 24.95GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-11 10:59:55"),
])

meta_dictionary["/GluGluToHHTo4V_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_10_hh_4v"),
  ("nof_db_events",         399999),
  ("nof_db_files",          25),
  ("fsize_db",              23479433610),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 23.48GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-10 05:20:13"),
])

meta_dictionary["/GluGluToHHTo4V_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_11_hh_4v"),
  ("nof_db_events",         394995),
  ("nof_db_files",          17),
  ("fsize_db",              22158832767),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.16GB; nevents: 395.00k; release: 10_2_5; last modified: 2020-09-10 05:18:53"),
])

meta_dictionary["/GluGluToHHTo4V_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020Oct12_GluGluToHHTo4V_node_12_TuneCP5_PSWeights_13TeV-madgraph-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v2"),
  ("sample_category",       "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_node_12_hh_4v"),
  ("nof_db_events",         400000),
  ("nof_db_files",          18),
  ("fsize_db",              22627810833),
  ("xsection",              0.057547),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 22.63GB; nevents: 400.00k; release: 10_2_5; last modified: 2020-09-08 16:52:44"),
])

meta_dictionary["/GluGluToHHTo4V_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4V_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH0_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH0_hh_4v"),
  ("nof_db_events",         985392),
  ("nof_db_files",          30),
  ("fsize_db",              49340466342),
  ("xsection",              0.00385439),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 49.34GB; nevents: 985.39k; release: 10_2_5; last modified: 2020-03-13 00:56:39"),
])

meta_dictionary["/GluGluToHHTo4V_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4V_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH1_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH1_hh_4v"),
  ("nof_db_events",         932996),
  ("nof_db_files",          59),
  ("fsize_db",              47734342494),
  ("xsection",              0.00171641),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 47.73GB; nevents: 933.00k; release: 10_2_5; last modified: 2020-04-13 14:50:51"),
])

meta_dictionary["/GluGluToHHTo4V_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4V_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH2p45_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH2p45_hh_4v"),
  ("nof_db_events",         999995),
  ("nof_db_files",          39),
  ("fsize_db",              50832748643),
  ("xsection",              0.00072699),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 50.83GB; nevents: 1000.00k; release: 10_2_5; last modified: 2020-03-23 02:49:28"),
])

meta_dictionary["/GluGluToHHTo4V_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1/MINIAODSIM"] =  OD([
  ("crab_string",           "2018_2020May05_GluGluToHHTo4V_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8__RunIIAutumn18MiniAOD-102X_upgrade2018_realistic_v15-v1"),
  ("sample_category",       "signal_ggf_nonresonant_cHHH5_hh_wwww"),
  ("process_name_specific", "signal_ggf_nonresonant_cHHH5_hh_4v"),
  ("nof_db_events",         999792),
  ("nof_db_files",          66),
  ("fsize_db",              48774118094),
  ("xsection",              0.00507095),
  ("use_it",                True),
  ("genWeight",             True),
  ("comment",               "100.0%; status: VALID; size: 48.77GB; nevents: 999.79k; release: 10_2_5; last modified: 2020-03-27 05:05:52"),
])


# event statistics by sample category:
# signal_ggf_spin0_250_hh_tttt:            400.00k
# signal_ggf_spin0_260_hh_tttt:            400.00k
# signal_ggf_spin0_270_hh_tttt:            400.00k
# signal_ggf_spin0_280_hh_tttt:            385.00k
# signal_ggf_spin0_300_hh_tttt:            294.00k
# signal_ggf_spin0_320_hh_tttt:            297.00k
# signal_ggf_spin0_350_hh_tttt:            297.00k
# signal_ggf_spin0_400_hh_tttt:            300.00k
# signal_ggf_spin0_450_hh_tttt:            300.00k
# signal_ggf_spin0_500_hh_tttt:            300.00k
# signal_ggf_spin0_550_hh_tttt:            300.00k
# signal_ggf_spin0_600_hh_tttt:            196.00k
# signal_ggf_spin0_650_hh_tttt:            200.00k
# signal_ggf_spin0_700_hh_tttt:            200.00k
# signal_ggf_spin0_750_hh_tttt:            200.00k
# signal_ggf_spin0_800_hh_tttt:            196.00k
# signal_ggf_spin0_850_hh_tttt:            200.00k
# signal_ggf_spin0_900_hh_tttt:            190.00k
# signal_ggf_spin0_1000_hh_tttt:           100.00k
# signal_ggf_spin0_1250_hh_tttt:           100.00k
# signal_ggf_spin0_1500_hh_tttt:           100.00k
# signal_ggf_spin0_1750_hh_tttt:           100.00k
# signal_ggf_spin0_2000_hh_tttt:           96.00k
# signal_ggf_spin0_2500_hh_tttt:           100.00k
# signal_ggf_spin0_3000_hh_tttt:           100.00k
# signal_vbf_spin0_250_hh_tttt:            400.00k
# signal_vbf_spin0_260_hh_tttt:            392.00k
# signal_vbf_spin0_270_hh_tttt:            360.00k
# signal_vbf_spin0_280_hh_tttt:            392.00k
# signal_vbf_spin0_300_hh_tttt:            300.00k
# signal_vbf_spin0_320_hh_tttt:            300.00k
# signal_vbf_spin0_350_hh_tttt:            300.00k
# signal_vbf_spin0_400_hh_tttt:            300.00k
# signal_vbf_spin0_450_hh_tttt:            300.00k
# signal_vbf_spin0_500_hh_tttt:            296.00k
# signal_vbf_spin0_550_hh_tttt:            300.00k
# signal_vbf_spin0_600_hh_tttt:            200.00k
# signal_vbf_spin0_650_hh_tttt:            196.00k
# signal_vbf_spin0_700_hh_tttt:            200.00k
# signal_vbf_spin0_750_hh_tttt:            200.00k
# signal_vbf_spin0_800_hh_tttt:            200.00k
# signal_vbf_spin0_850_hh_tttt:            200.00k
# signal_vbf_spin0_900_hh_tttt:            200.00k
# signal_vbf_spin0_1000_hh_tttt:           100.00k
# signal_vbf_spin0_1250_hh_tttt:           100.00k
# signal_vbf_spin0_1500_hh_tttt:           100.00k
# signal_vbf_spin0_1750_hh_tttt:           98.00k
# signal_vbf_spin0_2000_hh_tttt:           100.00k
# signal_vbf_spin0_3000_hh_tttt:           100.00k
# signal_ggf_spin2_250_hh_tttt:            400.00k
# signal_ggf_spin2_260_hh_tttt:            400.00k
# signal_ggf_spin2_270_hh_tttt:            400.00k
# signal_ggf_spin2_280_hh_tttt:            400.00k
# signal_ggf_spin2_300_hh_tttt:            297.00k
# signal_ggf_spin2_320_hh_tttt:            300.00k
# signal_ggf_spin2_350_hh_tttt:            300.00k
# signal_ggf_spin2_400_hh_tttt:            300.00k
# signal_ggf_spin2_450_hh_tttt:            295.00k
# signal_ggf_spin2_500_hh_tttt:            300.00k
# signal_ggf_spin2_550_hh_tttt:            300.00k
# signal_ggf_spin2_600_hh_tttt:            200.00k
# signal_ggf_spin2_650_hh_tttt:            200.00k
# signal_ggf_spin2_700_hh_tttt:            200.00k
# signal_ggf_spin2_750_hh_tttt:            196.00k
# signal_ggf_spin2_800_hh_tttt:            200.00k
# signal_ggf_spin2_850_hh_tttt:            200.00k
# signal_ggf_spin2_900_hh_tttt:            200.00k
# signal_ggf_spin2_1000_hh_tttt:           100.00k
# signal_ggf_spin2_1250_hh_tttt:           100.00k
# signal_ggf_spin2_1500_hh_tttt:           100.00k
# signal_ggf_spin2_1750_hh_tttt:           100.00k
# signal_ggf_spin2_2000_hh_tttt:           100.00k
# signal_ggf_spin2_2500_hh_tttt:           100.00k
# signal_ggf_spin2_3000_hh_tttt:           100.00k
# signal_vbf_spin2_250_hh_tttt:            400.00k
# signal_vbf_spin2_260_hh_tttt:            400.00k
# signal_vbf_spin2_270_hh_tttt:            382.00k
# signal_vbf_spin2_280_hh_tttt:            397.00k
# signal_vbf_spin2_300_hh_tttt:            292.00k
# signal_vbf_spin2_320_hh_tttt:            300.00k
# signal_vbf_spin2_350_hh_tttt:            300.00k
# signal_vbf_spin2_400_hh_tttt:            297.00k
# signal_vbf_spin2_450_hh_tttt:            298.00k
# signal_vbf_spin2_500_hh_tttt:            300.00k
# signal_vbf_spin2_550_hh_tttt:            300.00k
# signal_vbf_spin2_600_hh_tttt:            200.00k
# signal_vbf_spin2_650_hh_tttt:            200.00k
# signal_vbf_spin2_700_hh_tttt:            194.00k
# signal_vbf_spin2_750_hh_tttt:            198.00k
# signal_vbf_spin2_800_hh_tttt:            200.00k
# signal_vbf_spin2_850_hh_tttt:            200.00k
# signal_vbf_spin2_900_hh_tttt:            200.00k
# signal_vbf_spin2_1000_hh_tttt:           100.00k
# signal_vbf_spin2_1200_hh_tttt:           100.00k
# signal_vbf_spin2_1250_hh_tttt:           100.00k
# signal_vbf_spin2_1500_hh_tttt:           100.00k
# signal_vbf_spin2_1750_hh_tttt:           100.00k
# signal_vbf_spin2_2000_hh_tttt:           100.00k
# signal_vbf_spin2_2500_hh_tttt:           100.00k
# signal_vbf_spin2_3000_hh_tttt:           100.00k
# signal_ggf_spin0_250_hh_wwtt:            400.00k
# signal_ggf_spin0_260_hh_wwtt:            400.00k
# signal_ggf_spin0_270_hh_wwtt:            394.00k
# signal_ggf_spin0_280_hh_wwtt:            400.00k
# signal_ggf_spin0_300_hh_wwtt:            300.00k
# signal_ggf_spin0_320_hh_wwtt:            294.00k
# signal_ggf_spin0_350_hh_wwtt:            299.99k
# signal_ggf_spin0_400_hh_wwtt:            278.99k
# signal_ggf_spin0_450_hh_wwtt:            294.00k
# signal_ggf_spin0_500_hh_wwtt:            300.00k
# signal_ggf_spin0_550_hh_wwtt:            296.00k
# signal_ggf_spin0_600_hh_wwtt:            200.00k
# signal_ggf_spin0_650_hh_wwtt:            200.00k
# signal_ggf_spin0_700_hh_wwtt:            200.00k
# signal_ggf_spin0_750_hh_wwtt:            196.00k
# signal_ggf_spin0_800_hh_wwtt:            200.00k
# signal_ggf_spin0_850_hh_wwtt:            194.00k
# signal_ggf_spin0_900_hh_wwtt:            200.00k
# signal_ggf_spin0_1000_hh_wwtt:           100.00k
# signal_ggf_spin0_1250_hh_wwtt:           97.00k
# signal_ggf_spin0_1500_hh_wwtt:           100.00k
# signal_ggf_spin0_1750_hh_wwtt:           100.00k
# signal_ggf_spin0_2000_hh_wwtt:           100.00k
# signal_ggf_spin0_2500_hh_wwtt:           100.00k
# signal_ggf_spin0_3000_hh_wwtt:           100.00k
# signal_vbf_spin0_250_hh_wwtt:            384.00k
# signal_vbf_spin0_260_hh_wwtt:            389.99k
# signal_vbf_spin0_270_hh_wwtt:            400.00k
# signal_vbf_spin0_280_hh_wwtt:            400.00k
# signal_vbf_spin0_300_hh_wwtt:            294.00k
# signal_vbf_spin0_320_hh_wwtt:            300.00k
# signal_vbf_spin0_350_hh_wwtt:            300.00k
# signal_vbf_spin0_400_hh_wwtt:            299.99k
# signal_vbf_spin0_450_hh_wwtt:            299.99k
# signal_vbf_spin0_500_hh_wwtt:            299.99k
# signal_vbf_spin0_550_hh_wwtt:            299.99k
# signal_vbf_spin0_600_hh_wwtt:            199.99k
# signal_vbf_spin0_650_hh_wwtt:            200.00k
# signal_vbf_spin0_700_hh_wwtt:            200.00k
# signal_vbf_spin0_750_hh_wwtt:            200.00k
# signal_vbf_spin0_800_hh_wwtt:            192.00k
# signal_vbf_spin0_850_hh_wwtt:            199.99k
# signal_vbf_spin0_900_hh_wwtt:            200.00k
# signal_vbf_spin0_1000_hh_wwtt:           100.00k
# signal_vbf_spin0_1250_hh_wwtt:           100.00k
# signal_vbf_spin0_1500_hh_wwtt:           100.00k
# signal_vbf_spin0_1750_hh_wwtt:           99.00k
# signal_vbf_spin0_2000_hh_wwtt:           100.00k
# signal_vbf_spin0_3000_hh_wwtt:           100.00k
# signal_ggf_spin2_250_hh_wwtt:            392.00k
# signal_ggf_spin2_260_hh_wwtt:            399.99k
# signal_ggf_spin2_270_hh_wwtt:            398.00k
# signal_ggf_spin2_280_hh_wwtt:            399.99k
# signal_ggf_spin2_300_hh_wwtt:            298.00k
# signal_ggf_spin2_320_hh_wwtt:            300.00k
# signal_ggf_spin2_350_hh_wwtt:            296.00k
# signal_ggf_spin2_400_hh_wwtt:            298.00k
# signal_ggf_spin2_450_hh_wwtt:            284.99k
# signal_ggf_spin2_500_hh_wwtt:            300.00k
# signal_ggf_spin2_550_hh_wwtt:            300.00k
# signal_ggf_spin2_600_hh_wwtt:            200.00k
# signal_ggf_spin2_650_hh_wwtt:            200.00k
# signal_ggf_spin2_700_hh_wwtt:            200.00k
# signal_ggf_spin2_750_hh_wwtt:            198.00k
# signal_ggf_spin2_800_hh_wwtt:            200.00k
# signal_ggf_spin2_850_hh_wwtt:            200.00k
# signal_ggf_spin2_900_hh_wwtt:            196.00k
# signal_ggf_spin2_1000_hh_wwtt:           100.00k
# signal_ggf_spin2_1250_hh_wwtt:           100.00k
# signal_ggf_spin2_1500_hh_wwtt:           100.00k
# signal_ggf_spin2_1750_hh_wwtt:           100.00k
# signal_ggf_spin2_2000_hh_wwtt:           100.00k
# signal_ggf_spin2_2500_hh_wwtt:           100.00k
# signal_ggf_spin2_3000_hh_wwtt:           100.00k
# signal_vbf_spin2_250_hh_wwtt:            400.00k
# signal_vbf_spin2_260_hh_wwtt:            399.99k
# signal_vbf_spin2_270_hh_wwtt:            400.00k
# signal_vbf_spin2_280_hh_wwtt:            387.99k
# signal_vbf_spin2_300_hh_wwtt:            300.00k
# signal_vbf_spin2_320_hh_wwtt:            299.99k
# signal_vbf_spin2_350_hh_wwtt:            284.99k
# signal_vbf_spin2_400_hh_wwtt:            297.00k
# signal_vbf_spin2_450_hh_wwtt:            300.00k
# signal_vbf_spin2_500_hh_wwtt:            300.00k
# signal_vbf_spin2_550_hh_wwtt:            299.99k
# signal_vbf_spin2_600_hh_wwtt:            200.00k
# signal_vbf_spin2_650_hh_wwtt:            200.00k
# signal_vbf_spin2_700_hh_wwtt:            200.00k
# signal_vbf_spin2_750_hh_wwtt:            199.99k
# signal_vbf_spin2_800_hh_wwtt:            200.00k
# signal_vbf_spin2_850_hh_wwtt:            200.00k
# signal_vbf_spin2_900_hh_wwtt:            200.00k
# signal_vbf_spin2_1000_hh_wwtt:           100.00k
# signal_vbf_spin2_1200_hh_wwtt:           100.00k
# signal_vbf_spin2_1250_hh_wwtt:           100.00k
# signal_vbf_spin2_1500_hh_wwtt:           100.00k
# signal_vbf_spin2_1750_hh_wwtt:           96.00k
# signal_vbf_spin2_2000_hh_wwtt:           100.00k
# signal_vbf_spin2_2500_hh_wwtt:           100.00k
# signal_vbf_spin2_3000_hh_wwtt:           100.00k
# signal_ggf_spin0_250_hh_wwww:            400.00k
# signal_ggf_spin0_260_hh_wwww:            400.00k
# signal_ggf_spin0_270_hh_wwww:            400.00k
# signal_ggf_spin0_280_hh_wwww:            400.00k
# signal_ggf_spin0_300_hh_wwww:            400.00k
# signal_ggf_spin0_320_hh_wwww:            400.00k
# signal_ggf_spin0_350_hh_wwww:            395.00k
# signal_ggf_spin0_400_hh_wwww:            400.00k
# signal_ggf_spin0_450_hh_wwww:            400.00k
# signal_ggf_spin0_500_hh_wwww:            400.00k
# signal_ggf_spin0_550_hh_wwww:            400.00k
# signal_ggf_spin0_600_hh_wwww:            400.00k
# signal_ggf_spin0_650_hh_wwww:            400.00k
# signal_ggf_spin0_700_hh_wwww:            399.99k
# signal_ggf_spin0_750_hh_wwww:            400.00k
# signal_ggf_spin0_800_hh_wwww:            400.00k
# signal_ggf_spin0_850_hh_wwww:            400.00k
# signal_ggf_spin0_900_hh_wwww:            400.00k
# signal_ggf_spin0_1000_hh_wwww:           400.00k
# signal_ggf_spin0_1250_hh_wwww:           100.00k
# signal_ggf_spin0_1500_hh_wwww:           100.00k
# signal_ggf_spin0_1750_hh_wwww:           100.00k
# signal_ggf_spin0_2000_hh_wwww:           100.00k
# signal_ggf_spin0_2500_hh_wwww:           100.00k
# signal_ggf_spin0_3000_hh_wwww:           100.00k
# signal_ggf_spin2_250_hh_wwww:            396.00k
# signal_ggf_spin2_260_hh_wwww:            400.00k
# signal_ggf_spin2_270_hh_wwww:            400.00k
# signal_ggf_spin2_280_hh_wwww:            400.00k
# signal_ggf_spin2_300_hh_wwww:            400.00k
# signal_ggf_spin2_320_hh_wwww:            400.00k
# signal_ggf_spin2_350_hh_wwww:            400.00k
# signal_ggf_spin2_400_hh_wwww:            400.00k
# signal_ggf_spin2_450_hh_wwww:            400.00k
# signal_ggf_spin2_500_hh_wwww:            400.00k
# signal_ggf_spin2_550_hh_wwww:            400.00k
# signal_ggf_spin2_600_hh_wwww:            400.00k
# signal_ggf_spin2_650_hh_wwww:            400.00k
# signal_ggf_spin2_700_hh_wwww:            400.00k
# signal_ggf_spin2_750_hh_wwww:            400.00k
# signal_ggf_spin2_800_hh_wwww:            400.00k
# signal_ggf_spin2_850_hh_wwww:            400.00k
# signal_ggf_spin2_900_hh_wwww:            400.00k
# signal_ggf_spin2_1000_hh_wwww:           400.00k
# signal_ggf_spin2_1250_hh_wwww:           100.00k
# signal_ggf_spin2_1500_hh_wwww:           100.00k
# signal_ggf_spin2_1750_hh_wwww:           100.00k
# signal_ggf_spin2_2000_hh_wwww:           100.00k
# signal_ggf_spin2_2500_hh_wwww:           100.00k
# signal_ggf_spin2_3000_hh_wwww:           100.00k
# signal_vbf_nonresonant_1_1_1_hh_tttt:    400.00k
# signal_vbf_nonresonant_1_1_2_hh_tttt:    400.00k
# signal_vbf_nonresonant_1_2_1_hh_tttt:    400.00k
# signal_vbf_nonresonant_1_1_0_hh_tttt:    400.00k
# signal_vbf_nonresonant_0p5_1_1_hh_tttt:  400.00k
# signal_vbf_nonresonant_1p5_1_1_hh_tttt:  375.00k
# signal_vbf_nonresonant_1_0_1_hh_tttt:    400.00k
# signal_vbf_nonresonant_1_1_1_hh_wwtt:    399.99k
# signal_vbf_nonresonant_1_1_2_hh_wwtt:    399.99k
# signal_vbf_nonresonant_1_2_1_hh_wwtt:    400.00k
# signal_vbf_nonresonant_1_1_0_hh_wwtt:    399.99k
# signal_vbf_nonresonant_0p5_1_1_hh_wwtt:  399.99k
# signal_vbf_nonresonant_1p5_1_1_hh_wwtt:  400.00k
# signal_vbf_nonresonant_1_0_1_hh_wwtt:    399.99k
# signal_vbf_nonresonant_1_1_1_hh_wwww:    400.00k
# signal_vbf_nonresonant_1_1_2_hh_wwww:    388.00k
# signal_vbf_nonresonant_1_1_0_hh_wwww:    400.00k
# signal_vbf_nonresonant_1_2_1_hh_wwww:    400.00k
# signal_vbf_nonresonant_0p5_1_1_hh_wwww:  400.00k
# signal_vbf_nonresonant_1p5_1_1_hh_wwww:  400.00k
# signal_vbf_nonresonant_1_0_1_hh_wwww:    400.00k
# signal_ggf_nonresonant_hh_tttt:          5.17M
# signal_ggf_nonresonant_cHHH0_hh_tttt:    979.10k
# signal_ggf_nonresonant_cHHH1_hh_tttt:    963.00k
# signal_ggf_nonresonant_cHHH2p45_hh_tttt: 1.00M
# signal_ggf_nonresonant_cHHH5_hh_tttt:    1.00M
# signal_ggf_nonresonant_hh_wwtt:          5.18M
# signal_ggf_nonresonant_cHHH0_hh_wwtt:    399.99k
# signal_ggf_nonresonant_cHHH1_hh_wwtt:    396.99k
# signal_ggf_nonresonant_cHHH2p45_hh_wwtt: 383.09k
# signal_ggf_nonresonant_cHHH5_hh_wwtt:    386.29k
# signal_ggf_nonresonant_hh_wwww:          5.19M
# signal_ggf_nonresonant_cHHH0_hh_wwww:    985.39k
# signal_ggf_nonresonant_cHHH1_hh_wwww:    933.00k
# signal_ggf_nonresonant_cHHH2p45_hh_wwww: 1000.00k
# signal_ggf_nonresonant_cHHH5_hh_wwww:    999.79k

