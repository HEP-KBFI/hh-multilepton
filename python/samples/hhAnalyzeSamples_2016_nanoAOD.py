from collections import OrderedDict as OD

# file generated at 2020-10-17 20:12:32 with the following command:
# create_dictionary.py -m python/samples/metaDict_2016_hh.py -p python/samples/sampleLocations_2016_nanoAOD_hh_multilepton.txt -N samples_2016 -E 2016 -o python/samples -g hhAnalyzeSamples_2016_nanoAOD.py -M

samples_2016 = OD()
samples_2016["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     174788909), # 174.79MB, avg file size 87.39MB
  ("fsize_db",                        3874786969), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_114712"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t_PSWeights"),
  ("nof_files",                       9),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398700),
  ("nof_db_events",                   398700),
  ("fsize_local",                     665565348), # 665.57MB, avg file size 73.95MB
  ("fsize_db",                        16519862413), # 16.52GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_124607"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99204),
  ("nof_db_events",                   99204),
  ("fsize_local",                     173265171), # 173.27MB, avg file size 173.27MB
  ("fsize_db",                        3865138450), # 3.87GB, avg file size 3.87GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_114851"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     179431629), # 179.43MB, avg file size 89.72MB
  ("fsize_db",                        3829876445), # 3.83GB, avg file size 1.91GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_115028"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98567),
  ("nof_db_events",                   98567),
  ("fsize_local",                     175576884), # 175.58MB, avg file size 175.58MB
  ("fsize_db",                        3900002340), # 3.90GB, avg file size 1.95GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_115237"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4t_PSWeights"),
  ("nof_files",                       25),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 397400),
  ("nof_db_events",                   397400),
  ("fsize_local",                     731820057), # 731.82MB, avg file size 29.27MB
  ("fsize_db",                        16615518051), # 16.62GB, avg file size 755.25MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_124715"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 94730),
  ("nof_db_events",                   94730),
  ("fsize_local",                     172294444), # 172.29MB, avg file size 172.29MB
  ("fsize_db",                        3783167238), # 3.78GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_115441"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     184877280), # 184.88MB, avg file size 184.88MB
  ("fsize_db",                        3916703835), # 3.92GB, avg file size 1.96GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-320_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-320_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_115654"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4t_PSWeights"),
  ("nof_files",                       18),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     570424078), # 570.42MB, avg file size 31.69MB
  ("fsize_db",                        12792833416), # 12.79GB, avg file size 799.55MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_124850"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_340_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_340_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     188280202), # 188.28MB, avg file size 188.28MB
  ("fsize_db",                        3984955042), # 3.98GB, avg file size 1.99GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-340_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-340_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_115900"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98356),
  ("nof_db_events",                   98356),
  ("fsize_local",                     186582381), # 186.58MB, avg file size 186.58MB
  ("fsize_db",                        4031403477), # 4.03GB, avg file size 2.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_120050"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97614),
  ("nof_db_events",                   97614),
  ("fsize_local",                     192773660), # 192.77MB, avg file size 192.77MB
  ("fsize_db",                        4056144350), # 4.06GB, avg file size 2.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_120326"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t_PSWeights"),
  ("nof_files",                       9),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 281200),
  ("nof_db_events",                   281200),
  ("fsize_local",                     544477378), # 544.48MB, avg file size 60.50MB
  ("fsize_db",                        11960344453), # 11.96GB, avg file size 1.71GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_124957"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     205862531), # 205.86MB, avg file size 102.93MB
  ("fsize_db",                        4254873375), # 4.25GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_120534"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4t_PSWeights"),
  ("nof_files",                       7),
  ("nof_db_files",                    4),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     594859118), # 594.86MB, avg file size 84.98MB
  ("fsize_db",                        13134547939), # 13.13GB, avg file size 3.28GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_125102"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     106568720), # 106.57MB, avg file size 106.57MB
  ("fsize_db",                        2208888272), # 2.21GB, avg file size 2.21GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_120709"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4t_PSWeights"),
  ("nof_files",                       18),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 285800),
  ("nof_db_events",                   285800),
  ("fsize_local",                     615853333), # 615.85MB, avg file size 34.21MB
  ("fsize_db",                        12621986477), # 12.62GB, avg file size 788.87MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_125246"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     109190855), # 109.19MB, avg file size 109.19MB
  ("fsize_db",                        2111067830), # 2.11GB, avg file size 2.11GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_120846"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     111800074), # 111.80MB, avg file size 111.80MB
  ("fsize_db",                        2253668540), # 2.25GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_121053"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4t_PSWeights"),
  ("nof_files",                       6),
  ("nof_db_files",                    4),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     432875275), # 432.88MB, avg file size 72.15MB
  ("fsize_db",                        8920890867), # 8.92GB, avg file size 2.23GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_125425"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 48463),
  ("nof_db_events",                   48463),
  ("fsize_local",                     110859231), # 110.86MB, avg file size 110.86MB
  ("fsize_db",                        2355229431), # 2.36GB, avg file size 2.36GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_121311"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4t_PSWeights"),
  ("nof_files",                       11),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 187000),
  ("nof_db_events",                   187000),
  ("fsize_local",                     429061460), # 429.06MB, avg file size 39.01MB
  ("fsize_db",                        8518094701), # 8.52GB, avg file size 851.81MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_125529"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     116961028), # 116.96MB, avg file size 116.96MB
  ("fsize_db",                        2263100514), # 2.26GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_121448"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     118986983), # 118.99MB, avg file size 118.99MB
  ("fsize_db",                        2299577348), # 2.30GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_121658"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4t_PSWeights"),
  ("nof_files",                       15),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 197000),
  ("nof_db_events",                   197000),
  ("fsize_local",                     478710516), # 478.71MB, avg file size 31.91MB
  ("fsize_db",                        9219847015), # 9.22GB, avg file size 658.56MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_125704"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     120835301), # 120.84MB, avg file size 120.84MB
  ("fsize_db",                        2263981849), # 2.26GB, avg file size 2.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_121912"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4t_PSWeights"),
  ("nof_files",                       4),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 153100),
  ("nof_db_events",                   153100),
  ("fsize_local",                     355626393), # 355.63MB, avg file size 88.91MB
  ("fsize_db",                        7040872910), # 7.04GB, avg file size 3.52GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_125810"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_4t_PSWeights"),
  ("nof_files",                       5),
  ("nof_db_files",                    4),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     470758009), # 470.76MB, avg file size 94.15MB
  ("fsize_db",                        9285551161), # 9.29GB, avg file size 2.32GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_125914"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     124100519), # 124.10MB, avg file size 124.10MB
  ("fsize_db",                        2478591891), # 2.48GB, avg file size 2.48GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_122151"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4t_PSWeights"),
  ("nof_files",                       19),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199100),
  ("nof_db_events",                   199100),
  ("fsize_local",                     515134469), # 515.13MB, avg file size 27.11MB
  ("fsize_db",                        9582412539), # 9.58GB, avg file size 532.36MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_130052"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_4t_PSWeights"),
  ("nof_files",                       7),
  ("nof_db_files",                    6),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     264556762), # 264.56MB, avg file size 37.79MB
  ("fsize_db",                        5027571214), # 5.03GB, avg file size 837.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_130302"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_4t_PSWeights"),
  ("nof_files",                       15),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 96800),
  ("nof_db_events",                   96800),
  ("fsize_local",                     283482659), # 283.48MB, avg file size 18.90MB
  ("fsize_db",                        5193927613), # 5.19GB, avg file size 324.62MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_130547"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_4t_PSWeights"),
  ("nof_files",                       2),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     253568642), # 253.57MB, avg file size 126.78MB
  ("fsize_db",                        5047825418), # 5.05GB, avg file size 5.05GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_130652"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_4t_PSWeights"),
  ("nof_files",                       14),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99300),
  ("nof_db_events",                   99300),
  ("fsize_local",                     285129934), # 285.13MB, avg file size 20.37MB
  ("fsize_db",                        5286751029), # 5.29GB, avg file size 406.67MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_130757"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4T_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_4t_PSWeights"),
  ("nof_files",                       3),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 96500),
  ("nof_db_events",                   96500),
  ("fsize_local",                     247919300), # 247.92MB, avg file size 82.64MB
  ("fsize_db",                        5222043153), # 5.22GB, avg file size 373.00MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4T_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4T_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_130933"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99430),
  ("nof_db_events",                   99430),
  ("fsize_local",                     174717877), # 174.72MB, avg file size 174.72MB
  ("fsize_db",                        3877049177), # 3.88GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_122402"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97772),
  ("nof_db_events",                   97772),
  ("fsize_local",                     174208040), # 174.21MB, avg file size 174.21MB
  ("fsize_db",                        3871755682), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_122614"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     182781522), # 182.78MB, avg file size 91.39MB
  ("fsize_db",                        3873301459), # 3.87GB, avg file size 1.94GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_122954"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4t_PSWeights"),
  ("nof_files",                       14),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 396400),
  ("nof_db_events",                   396400),
  ("fsize_local",                     708291579), # 708.29MB, avg file size 50.59MB
  ("fsize_db",                        16657530575), # 16.66GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131038"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98688),
  ("nof_db_events",                   98688),
  ("fsize_local",                     179775004), # 179.78MB, avg file size 179.78MB
  ("fsize_db",                        4085852491), # 4.09GB, avg file size 2.04GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_123159"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4t_PSWeights"),
  ("nof_files",                       9),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398500),
  ("nof_db_events",                   398500),
  ("fsize_local",                     705546103), # 705.55MB, avg file size 78.39MB
  ("fsize_db",                        16847191505), # 16.85GB, avg file size 1.68GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131144"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99502),
  ("nof_db_events",                   99502),
  ("fsize_local",                     185441016), # 185.44MB, avg file size 185.44MB
  ("fsize_db",                        3937638636), # 3.94GB, avg file size 1.97GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_123546"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97676),
  ("nof_db_events",                   97676),
  ("fsize_local",                     185581629), # 185.58MB, avg file size 185.58MB
  ("fsize_db",                        3947093624), # 3.95GB, avg file size 3.95GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_123959"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4t_PSWeights"),
  ("nof_files",                       22),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 277600),
  ("nof_db_events",                   277600),
  ("fsize_local",                     556574311), # 556.57MB, avg file size 25.30MB
  ("fsize_db",                        12164950744), # 12.16GB, avg file size 608.25MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131320"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-340_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_340_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_340_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99226),
  ("nof_db_events",                   99226),
  ("fsize_local",                     192051072), # 192.05MB, avg file size 192.05MB
  ("fsize_db",                        4027035901), # 4.03GB, avg file size 2.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-340_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-340_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_124142"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98212),
  ("nof_db_events",                   98212),
  ("fsize_local",                     191732141), # 191.73MB, avg file size 191.73MB
  ("fsize_db",                        4125701387), # 4.13GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_124317"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98789),
  ("nof_db_events",                   98789),
  ("fsize_local",                     200847977), # 200.85MB, avg file size 200.85MB
  ("fsize_db",                        4251757973), # 4.25GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_124526"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     213042733), # 213.04MB, avg file size 106.52MB
  ("fsize_db",                        4221394903), # 4.22GB, avg file size 2.11GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_124742"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 49535),
  ("nof_db_events",                   49535),
  ("fsize_local",                     109048720), # 109.05MB, avg file size 109.05MB
  ("fsize_db",                        2291615192), # 2.29GB, avg file size 763.87MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_124958"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4t_PSWeights"),
  ("nof_files",                       21),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 297800),
  ("nof_db_events",                   297800),
  ("fsize_local",                     670556229), # 670.56MB, avg file size 31.93MB
  ("fsize_db",                        13876837520), # 13.88GB, avg file size 730.36MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131424"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     113126204), # 113.13MB, avg file size 113.13MB
  ("fsize_db",                        2274028392), # 2.27GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_125414"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4t_PSWeights"),
  ("nof_files",                       17),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 281600),
  ("nof_db_events",                   281600),
  ("fsize_local",                     642804822), # 642.80MB, avg file size 37.81MB
  ("fsize_db",                        13197657604), # 13.20GB, avg file size 879.84MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131529"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 49175),
  ("nof_db_events",                   49175),
  ("fsize_local",                     114236277), # 114.24MB, avg file size 114.24MB
  ("fsize_db",                        2305398213), # 2.31GB, avg file size 2.31GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/191004_125604"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4t_PSWeights"),
  ("nof_files",                       22),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 197300),
  ("nof_db_events",                   197300),
  ("fsize_local",                     490118211), # 490.12MB, avg file size 22.28MB
  ("fsize_db",                        9539609752), # 9.54GB, avg file size 454.27MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131704"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     118790803), # 118.79MB, avg file size 118.79MB
  ("fsize_db",                        2270214311), # 2.27GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_125746"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4t_PSWeights"),
  ("nof_files",                       14),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199000),
  ("nof_db_events",                   199000),
  ("fsize_local",                     479405793), # 479.41MB, avg file size 34.24MB
  ("fsize_db",                        9560072029), # 9.56GB, avg file size 735.39MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131810"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 49080),
  ("nof_db_events",                   49080),
  ("fsize_local",                     118920947), # 118.92MB, avg file size 118.92MB
  ("fsize_db",                        2393147016), # 2.39GB, avg file size 2.39GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_125924"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4t_PSWeights"),
  ("nof_files",                       19),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 195000),
  ("nof_db_events",                   195000),
  ("fsize_local",                     494904884), # 494.90MB, avg file size 26.05MB
  ("fsize_db",                        9636044360), # 9.64GB, avg file size 535.34MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_131916"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 50000),
  ("nof_db_events",                   50000),
  ("fsize_local",                     123308462), # 123.31MB, avg file size 123.31MB
  ("fsize_db",                        2439402593), # 2.44GB, avg file size 2.44GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_130134"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 49178),
  ("nof_db_events",                   49178),
  ("fsize_local",                     123255948), # 123.26MB, avg file size 123.26MB
  ("fsize_db",                        2401512581), # 2.40GB, avg file size 2.40GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_130343"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4t_PSWeights"),
  ("nof_files",                       20),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 193000),
  ("nof_db_events",                   193000),
  ("fsize_local",                     509145595), # 509.15MB, avg file size 25.46MB
  ("fsize_db",                        9649596690), # 9.65GB, avg file size 536.09MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_132026"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_4t_PSWeights"),
  ("nof_files",                       4),
  ("nof_db_files",                    3),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     486068714), # 486.07MB, avg file size 121.52MB
  ("fsize_db",                        9763809130), # 9.76GB, avg file size 3.25GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_132202"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    1),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 49283),
  ("nof_db_events",                   49283),
  ("fsize_local",                     126625954), # 126.63MB, avg file size 126.63MB
  ("fsize_db",                        2506744879), # 2.51GB, avg file size 2.51GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph/2016v3_2019Oct04_GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_130559"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4t_PSWeights"),
  ("nof_files",                       19),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 179000),
  ("nof_db_events",                   179000),
  ("fsize_local",                     484361384), # 484.36MB, avg file size 25.49MB
  ("fsize_db",                        9088367034), # 9.09GB, avg file size 478.34MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_132306"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99100),
  ("nof_db_events",                   99100),
  ("fsize_local",                     253359329), # 253.36MB, avg file size 63.34MB
  ("fsize_db",                        5028842478), # 5.03GB, avg file size 558.76MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_132411"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_4t_PSWeights"),
  ("nof_files",                       5),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98200),
  ("nof_db_events",                   98200),
  ("fsize_local",                     261019597), # 261.02MB, avg file size 52.20MB
  ("fsize_db",                        5156299296), # 5.16GB, avg file size 429.69MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_132547"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_4t_PSWeights"),
  ("nof_files",                       11),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98400),
  ("nof_db_events",                   98400),
  ("fsize_local",                     275169889), # 275.17MB, avg file size 25.02MB
  ("fsize_db",                        5173520925), # 5.17GB, avg file size 517.35MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_132758"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_4t_PSWeights"),
  ("nof_files",                       5),
  ("nof_db_files",                    7),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     262241528), # 262.24MB, avg file size 52.45MB
  ("fsize_db",                        5250753743), # 5.25GB, avg file size 750.11MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_132934"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4T_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_4t_PSWeights"),
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     254790187), # 254.79MB, avg file size 84.93MB
  ("fsize_db",                        5169230329), # 5.17GB, avg file size 2.58GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4T_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4T_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_133041"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2v2t"),
  ("nof_files",                       17),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 377997),
  ("nof_db_events",                   377997),
  ("fsize_local",                     670458574), # 670.46MB, avg file size 39.44MB
  ("fsize_db",                        15877394876), # 15.88GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_133147"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2v2t"),
  ("nof_files",                       10),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398797),
  ("nof_db_events",                   398797),
  ("fsize_local",                     693144827), # 693.14MB, avg file size 69.31MB
  ("fsize_db",                        16845240982), # 16.85GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_133323"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2v2t"),
  ("nof_files",                       11),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 397195),
  ("nof_db_events",                   397195),
  ("fsize_local",                     703968089), # 703.97MB, avg file size 64.00MB
  ("fsize_db",                        16871942644), # 16.87GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_133429"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2v2t"),
  ("nof_files",                       7),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     555531330), # 555.53MB, avg file size 79.36MB
  ("fsize_db",                        12871103355), # 12.87GB, avg file size 858.07MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_133534"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2v2t"),
  ("nof_files",                       21),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 289199),
  ("nof_db_events",                   289199),
  ("fsize_local",                     594028669), # 594.03MB, avg file size 28.29MB
  ("fsize_db",                        12724200727), # 12.72GB, avg file size 636.21MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_133710"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2v2t"),
  ("nof_files",                       20),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 289896),
  ("nof_db_events",                   289896),
  ("fsize_local",                     647086003), # 647.09MB, avg file size 32.35MB
  ("fsize_db",                        13212226657), # 13.21GB, avg file size 695.38MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_133815"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2v2t"),
  ("nof_files",                       18),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 295996),
  ("nof_db_events",                   295996),
  ("fsize_local",                     676122035), # 676.12MB, avg file size 37.56MB
  ("fsize_db",                        13652021853), # 13.65GB, avg file size 803.06MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_133921"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2v2t"),
  ("nof_files",                       10),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 292996),
  ("nof_db_events",                   292996),
  ("fsize_local",                     666750576), # 666.75MB, avg file size 66.68MB
  ("fsize_db",                        13728394128), # 13.73GB, avg file size 807.55MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_134026"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 193600),
  ("nof_db_events",                   193600),
  ("fsize_local",                     456140543), # 456.14MB, avg file size 91.23MB
  ("fsize_db",                        9338768733), # 9.34GB, avg file size 718.37MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_134203"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199096),
  ("nof_db_events",                   199096),
  ("fsize_local",                     480236728), # 480.24MB, avg file size 80.04MB
  ("fsize_db",                        9737820064), # 9.74GB, avg file size 649.19MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_134309"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2v2t"),
  ("nof_files",                       11),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     503123510), # 503.12MB, avg file size 45.74MB
  ("fsize_db",                        9748383226), # 9.75GB, avg file size 974.84MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_134415"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     492543152), # 492.54MB, avg file size 98.51MB
  ("fsize_db",                        9778316747), # 9.78GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_134554"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 193696),
  ("nof_db_events",                   193696),
  ("fsize_local",                     485637827), # 485.64MB, avg file size 80.94MB
  ("fsize_db",                        9710157542), # 9.71GB, avg file size 647.34MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_134700"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 197594),
  ("nof_db_events",                   197594),
  ("fsize_local",                     498973442), # 498.97MB, avg file size 83.16MB
  ("fsize_db",                        9935965414), # 9.94GB, avg file size 764.31MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_as/201011_134808"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 96798),
  ("nof_db_events",                   96798),
  ("fsize_local",                     248922917), # 248.92MB, avg file size 82.97MB
  ("fsize_db",                        4969383021), # 4.97GB, avg file size 552.15MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a/201011_134947"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     264896526), # 264.90MB, avg file size 66.22MB
  ("fsize_db",                        5280186913), # 5.28GB, avg file size 528.02MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a/201011_135053"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     263936779), # 263.94MB, avg file size 87.98MB
  ("fsize_db",                        5199568414), # 5.20GB, avg file size 2.60GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a/201011_135159"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99399),
  ("nof_db_events",                   99399),
  ("fsize_local",                     265963320), # 265.96MB, avg file size 66.49MB
  ("fsize_db",                        5325473888), # 5.33GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a/201011_135305"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2v2t"),
  ("nof_files",                       16),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     301830061), # 301.83MB, avg file size 18.86MB
  ("fsize_db",                        5592310162), # 5.59GB, avg file size 372.82MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a/201011_135441"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98996),
  ("nof_db_events",                   98996),
  ("fsize_local",                     263284781), # 263.28MB, avg file size 87.76MB
  ("fsize_db",                        5475887837), # 5.48GB, avg file size 684.49MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a/201011_135547"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo2V2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2v2t"),
  ("nof_files",                       5),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     271441862), # 271.44MB, avg file size 54.29MB
  ("fsize_db",                        5740201558), # 5.74GB, avg file size 358.76MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo2V2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo2V2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_a/201011_135652"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2v2t"),
  ("nof_files",                       21),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 386789),
  ("nof_db_events",                   386789),
  ("fsize_local",                     699339796), # 699.34MB, avg file size 33.30MB
  ("fsize_db",                        16493369519), # 16.49GB, avg file size 868.07MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_135829"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2v2t"),
  ("nof_files",                       11),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 392193),
  ("nof_db_events",                   392193),
  ("fsize_local",                     690939662), # 690.94MB, avg file size 62.81MB
  ("fsize_db",                        16811286864), # 16.81GB, avg file size 988.90MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_135934"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2v2t"),
  ("nof_files",                       14),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398694),
  ("nof_db_events",                   398694),
  ("fsize_local",                     723366703), # 723.37MB, avg file size 51.67MB
  ("fsize_db",                        17065138035), # 17.07GB, avg file size 1.71GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140043"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2v2t"),
  ("nof_files",                       8),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398792),
  ("nof_db_events",                   398792),
  ("fsize_local",                     718038998), # 718.04MB, avg file size 89.75MB
  ("fsize_db",                        17234947936), # 17.23GB, avg file size 1.91GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140150"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 297797),
  ("nof_db_events",                   297797),
  ("fsize_local",                     551334604), # 551.33MB, avg file size 91.89MB
  ("fsize_db",                        12994378711), # 12.99GB, avg file size 1.44GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140327"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 297798),
  ("nof_db_events",                   297798),
  ("fsize_local",                     574789584), # 574.79MB, avg file size 63.87MB
  ("fsize_db",                        13282872519), # 13.28GB, avg file size 948.78MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140435"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2v2t"),
  ("nof_files",                       23),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 296399),
  ("nof_db_events",                   296399),
  ("fsize_local",                     666132003), # 666.13MB, avg file size 28.96MB
  ("fsize_db",                        13909898866), # 13.91GB, avg file size 662.38MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140541"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2v2t"),
  ("nof_files",                       16),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 294595),
  ("nof_db_events",                   294595),
  ("fsize_local",                     670310925), # 670.31MB, avg file size 41.89MB
  ("fsize_db",                        14047985955), # 14.05GB, avg file size 878.00MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140717"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2v2t"),
  ("nof_files",                       13),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     698607962), # 698.61MB, avg file size 53.74MB
  ("fsize_db",                        14481726165), # 14.48GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140823"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    6),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     700241977), # 700.24MB, avg file size 116.71MB
  ("fsize_db",                        14588899672), # 14.59GB, avg file size 2.43GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_140930"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     495169593), # 495.17MB, avg file size 123.79MB
  ("fsize_db",                        10029561846), # 10.03GB, avg file size 5.01GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_141211"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2v2t"),
  ("nof_files",                       20),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     537387969), # 537.39MB, avg file size 26.87MB
  ("fsize_db",                        10160566544), # 10.16GB, avg file size 564.48MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_141454"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2v2t"),
  ("nof_files",                       18),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97599),
  ("nof_db_events",                   97599),
  ("fsize_local",                     300220917), # 300.22MB, avg file size 16.68MB
  ("fsize_db",                        5411079155), # 5.41GB, avg file size 300.62MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc/201011_141704"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2v2t"),
  ("nof_files",                       11),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 94497),
  ("nof_db_events",                   94497),
  ("fsize_local",                     275462689), # 275.46MB, avg file size 25.04MB
  ("fsize_db",                        5173446366), # 5.17GB, avg file size 470.31MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc/201011_141840"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2v2t"),
  ("nof_files",                       4),
  ("nof_db_files",                    6),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97198),
  ("nof_db_events",                   97198),
  ("fsize_local",                     261565301), # 261.57MB, avg file size 65.39MB
  ("fsize_db",                        5277533846), # 5.28GB, avg file size 879.59MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc/201011_141945"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2v2t"),
  ("nof_files",                       13),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 94398),
  ("nof_db_events",                   94398),
  ("fsize_local",                     278838385), # 278.84MB, avg file size 21.45MB
  ("fsize_db",                        5291338150), # 5.29GB, avg file size 407.03MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc/201011_142052"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2v2t"),
  ("nof_files",                       14),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 92999),
  ("nof_db_events",                   92999),
  ("fsize_local",                     278011732), # 278.01MB, avg file size 19.86MB
  ("fsize_db",                        5259287389), # 5.26GB, avg file size 375.66MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc/201011_142230"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2v2t"),
  ("nof_files",                       3),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99400),
  ("nof_db_events",                   99400),
  ("fsize_local",                     263259759), # 263.26MB, avg file size 87.75MB
  ("fsize_db",                        5519689136), # 5.52GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo2V2Tau_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mc/201011_142335"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4v"),
  ("nof_files",                       24),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 374798),
  ("nof_db_events",                   374798),
  ("fsize_local",                     673567117), # 673.57MB, avg file size 28.07MB
  ("fsize_db",                        16077537091), # 16.08GB, avg file size 669.90MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_142443"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 381597),
  ("nof_db_events",                   381597),
  ("fsize_local",                     649757070), # 649.76MB, avg file size 81.22MB
  ("fsize_db",                        16275381425), # 16.28GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-260_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_142619"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4v"),
  ("nof_files",                       27),
  ("nof_db_files",                    25),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 388398),
  ("nof_db_events",                   388398),
  ("fsize_local",                     724889483), # 724.89MB, avg file size 26.85MB
  ("fsize_db",                        16805980899), # 16.81GB, avg file size 672.24MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_142725"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4v"),
  ("nof_files",                       18),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 348699),
  ("nof_db_events",                   348699),
  ("fsize_local",                     644761302), # 644.76MB, avg file size 35.82MB
  ("fsize_db",                        15131627743), # 15.13GB, avg file size 890.10MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_142833"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4v"),
  ("nof_files",                       7),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 269696),
  ("nof_db_events",                   269696),
  ("fsize_local",                     494298403), # 494.30MB, avg file size 70.61MB
  ("fsize_db",                        11953451448), # 11.95GB, avg file size 703.14MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143011"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     569357986), # 569.36MB, avg file size 63.26MB
  ("fsize_db",                        13075944384), # 13.08GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-320_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143115"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 293199),
  ("nof_db_events",                   293199),
  ("fsize_local",                     572548045), # 572.55MB, avg file size 95.42MB
  ("fsize_db",                        13063518005), # 13.06GB, avg file size 870.90MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143221"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4v"),
  ("nof_files",                       18),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 298999),
  ("nof_db_events",                   298999),
  ("fsize_local",                     652704392), # 652.70MB, avg file size 36.26MB
  ("fsize_db",                        13726613111), # 13.73GB, avg file size 807.45MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-400_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143327"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4v"),
  ("nof_files",                       16),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 290998),
  ("nof_db_events",                   290998),
  ("fsize_local",                     661886615), # 661.89MB, avg file size 41.37MB
  ("fsize_db",                        13666705434), # 13.67GB, avg file size 854.17MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143503"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 296399),
  ("nof_db_events",                   296399),
  ("fsize_local",                     678441372), # 678.44MB, avg file size 84.81MB
  ("fsize_db",                        14189137407), # 14.19GB, avg file size 945.94MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143609"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4v"),
  ("nof_files",                       16),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 289200),
  ("nof_db_events",                   289200),
  ("fsize_local",                     705785229), # 705.79MB, avg file size 44.11MB
  ("fsize_db",                        14090925766), # 14.09GB, avg file size 939.40MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143714"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4v"),
  ("nof_files",                       13),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     506409181), # 506.41MB, avg file size 38.95MB
  ("fsize_db",                        9928055655), # 9.93GB, avg file size 827.34MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143851"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 194599),
  ("nof_db_events",                   194599),
  ("fsize_local",                     483380818), # 483.38MB, avg file size 80.56MB
  ("fsize_db",                        9705394586), # 9.71GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_143957"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199099),
  ("nof_db_events",                   199099),
  ("fsize_local",                     500794698), # 500.79MB, avg file size 125.20MB
  ("fsize_db",                        10412573762), # 10.41GB, avg file size 495.84MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_144104"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_4v"),
  ("nof_files",                       6),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 193499),
  ("nof_db_events",                   193499),
  ("fsize_local",                     502677214), # 502.68MB, avg file size 83.78MB
  ("fsize_db",                        10096327837), # 10.10GB, avg file size 776.64MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-850_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_144240"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4v"),
  ("nof_files",                       7),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     504812130), # 504.81MB, avg file size 72.12MB
  ("fsize_db",                        10196278081), # 10.20GB, avg file size 566.46MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asympt/201011_144347"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4v"),
  ("nof_files",                       3),
  ("nof_db_files",                    4),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     263186226), # 263.19MB, avg file size 87.73MB
  ("fsize_db",                        5239982075), # 5.24GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_144456"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_4v"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 96000),
  ("nof_db_events",                   96000),
  ("fsize_local",                     253047694), # 253.05MB, avg file size 126.52MB
  ("fsize_db",                        5178725213), # 5.18GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_144634"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98199),
  ("nof_db_events",                   98199),
  ("fsize_local",                     265844654), # 265.84MB, avg file size 66.46MB
  ("fsize_db",                        5450650734), # 5.45GB, avg file size 495.51MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_144741"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_4v"),
  ("nof_files",                       10),
  ("nof_db_files",                    9),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98800),
  ("nof_db_events",                   98800),
  ("fsize_local",                     284829073), # 284.83MB, avg file size 28.48MB
  ("fsize_db",                        5575865633), # 5.58GB, avg file size 619.54MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_144848"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_4v"),
  ("nof_files",                       11),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 96999),
  ("nof_db_events",                   96999),
  ("fsize_local",                     283539520), # 283.54MB, avg file size 25.78MB
  ("fsize_db",                        5559977740), # 5.56GB, avg file size 556.00MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_144953"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_4v"),
  ("nof_files",                       17),
  ("nof_db_files",                    17),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 96700),
  ("nof_db_events",                   96700),
  ("fsize_local",                     302401318), # 302.40MB, avg file size 17.79MB
  ("fsize_db",                        5823719429), # 5.82GB, avg file size 342.57MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_145129"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToRadionToHHTo4V_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_4v"),
  ("nof_files",                       14),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99500),
  ("nof_db_events",                   99500),
  ("fsize_local",                     300639335), # 300.64MB, avg file size 21.47MB
  ("fsize_db",                        5928270827), # 5.93GB, avg file size 423.45MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToRadionToHHTo4V_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToRadionToHHTo4V_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymp/201011_145238"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4v"),
  ("nof_files",                       18),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 395999),
  ("nof_db_events",                   395999),
  ("fsize_local",                     704323073), # 704.32MB, avg file size 39.13MB
  ("fsize_db",                        17070181354), # 17.07GB, avg file size 1.14GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_145344"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4v"),
  ("nof_files",                       25),
  ("nof_db_files",                    25),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 379098),
  ("nof_db_events",                   379098),
  ("fsize_local",                     722625298), # 722.63MB, avg file size 28.91MB
  ("fsize_db",                        16750745578), # 16.75GB, avg file size 670.03MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-270_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_145521"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4v"),
  ("nof_files",                       14),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 396998),
  ("nof_db_events",                   396998),
  ("fsize_local",                     736600033), # 736.60MB, avg file size 52.61MB
  ("fsize_db",                        17491372764), # 17.49GB, avg file size 1.75GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-280_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_145626"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4v"),
  ("nof_files",                       23),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 289200),
  ("nof_db_events",                   289200),
  ("fsize_local",                     592804875), # 592.80MB, avg file size 25.77MB
  ("fsize_db",                        13268242227), # 13.27GB, avg file size 576.88MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-300_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_145732"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 297798),
  ("nof_db_events",                   297798),
  ("fsize_local",                     611649388), # 611.65MB, avg file size 76.46MB
  ("fsize_db",                        13948525797), # 13.95GB, avg file size 871.78MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-350_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_145908"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4v"),
  ("nof_files",                       20),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 291198),
  ("nof_db_events",                   291198),
  ("fsize_local",                     704329687), # 704.33MB, avg file size 35.22MB
  ("fsize_db",                        14494356228), # 14.49GB, avg file size 805.24MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-450_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_150120"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4v"),
  ("nof_files",                       8),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299098),
  ("nof_db_events",                   299098),
  ("fsize_local",                     718379813), # 718.38MB, avg file size 89.80MB
  ("fsize_db",                        15009928805), # 15.01GB, avg file size 1.50GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_150227"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4v"),
  ("nof_files",                       13),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 296400),
  ("nof_db_events",                   296400),
  ("fsize_local",                     747102910), # 747.10MB, avg file size 57.47MB
  ("fsize_db",                        15138881712), # 15.14GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-550_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_150402"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     506051466), # 506.05MB, avg file size 56.23MB
  ("fsize_db",                        10310545217), # 10.31GB, avg file size 687.37MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-600_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_150509"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4v"),
  ("nof_files",                       14),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 197099),
  ("nof_db_events",                   197099),
  ("fsize_local",                     531286561), # 531.29MB, avg file size 37.95MB
  ("fsize_db",                        10433831917), # 10.43GB, avg file size 802.60MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-650_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_150614"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4v"),
  ("nof_files",                       13),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 198400),
  ("nof_db_events",                   198400),
  ("fsize_local",                     542839869), # 542.84MB, avg file size 41.76MB
  ("fsize_db",                        10717323236), # 10.72GB, avg file size 893.11MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_150750"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4v"),
  ("nof_files",                       12),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     545802604), # 545.80MB, avg file size 45.48MB
  ("fsize_db",                        10818639215), # 10.82GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-800_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_150856"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4v"),
  ("nof_files",                       5),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 198397),
  ("nof_db_events",                   198397),
  ("fsize_local",                     526645219), # 526.65MB, avg file size 105.33MB
  ("fsize_db",                        10862842617), # 10.86GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-900_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_151139"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4v"),
  ("nof_files",                       2),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     264905930), # 264.91MB, avg file size 132.45MB
  ("fsize_db",                        5482745038), # 5.48GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-1000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_151247"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_4v"),
  ("nof_files",                       7),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     279810025), # 279.81MB, avg file size 39.97MB
  ("fsize_db",                        5691322878), # 5.69GB, avg file size 474.28MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-1250_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_151355"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_4v"),
  ("nof_files",                       3),
  ("nof_db_files",                    3),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     267591667), # 267.59MB, avg file size 89.20MB
  ("fsize_db",                        5569843012), # 5.57GB, avg file size 1.86GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-1500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_151532"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_4v"),
  ("nof_files",                       12),
  ("nof_db_files",                    11),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97600),
  ("nof_db_events",                   97600),
  ("fsize_local",                     287001249), # 287.00MB, avg file size 23.92MB
  ("fsize_db",                        5624509090), # 5.62GB, avg file size 511.32MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-1750_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_151644"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_4v"),
  ("nof_files",                       3),
  ("nof_db_files",                    5),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98800),
  ("nof_db_events",                   98800),
  ("fsize_local",                     265008533), # 265.01MB, avg file size 88.34MB
  ("fsize_db",                        5614621956), # 5.61GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-2000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_151753"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_4v"),
  ("nof_files",                       5),
  ("nof_db_files",                    10),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98200),
  ("nof_db_events",                   98200),
  ("fsize_local",                     270171195), # 270.17MB, avg file size 54.03MB
  ("fsize_db",                        5783411381), # 5.78GB, avg file size 578.34MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-2500_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_151859"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToBulkGravitonToHHTo4V_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_4v"),
  ("nof_files",                       9),
  ("nof_db_files",                    8),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 95100),
  ("nof_db_events",                   95100),
  ("fsize_local",                     273550065), # 273.55MB, avg file size 30.39MB
  ("fsize_db",                        5631778372), # 5.63GB, avg file size 703.97MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToBulkGravitonToHHTo4V_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToBulkGravitonToHHTo4V_M-3000_narrow_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2/201011_152005"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4T_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       10),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     836857489), # 836.86MB, avg file size 83.69MB
  ("fsize_db",                        18337645661), # 18.34GB, avg file size 764.07MB
  ("use_it",                          True),
  ("xsection",                        5.5932e-06),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4T_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4T_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_152143"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4T_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       25),
  ("nof_db_files",                    25),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399200),
  ("nof_db_events",                   399200),
  ("fsize_local",                     974217641), # 974.22MB, avg file size 38.97MB
  ("fsize_db",                        19035822380), # 19.04GB, avg file size 761.43MB
  ("use_it",                          True),
  ("xsection",                        5.5891e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4T_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4T_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_152251"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4T_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       20),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 396400),
  ("nof_db_events",                   396400),
  ("fsize_local",                     927690838), # 927.69MB, avg file size 46.38MB
  ("fsize_db",                        18592779701), # 18.59GB, avg file size 885.37MB
  ("use_it",                          True),
  ("xsection",                        4.25487e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4T_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4T_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun/201011_152359"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4T_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       25),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398200),
  ("nof_db_events",                   398200),
  ("fsize_local",                     884279476), # 884.28MB, avg file size 35.37MB
  ("fsize_db",                        18174217627), # 18.17GB, avg file size 865.44MB
  ("use_it",                          True),
  ("xsection",                        0.0002595228),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4T_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4T_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun/201011_152536"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4T_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       23),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     909936110), # 909.94MB, avg file size 39.56MB
  ("fsize_db",                        18416108721), # 18.42GB, avg file size 920.81MB
  ("use_it",                          True),
  ("xsection",                        0.0001064477),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4T_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4T_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_152643"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       24),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     902970357), # 902.97MB, avg file size 37.62MB
  ("fsize_db",                        18791082669), # 18.79GB, avg file size 854.14MB
  ("use_it",                          True),
  ("xsection",                        4.27833e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo2V2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo2V2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_152750"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2V2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       25),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 383191),
  ("nof_db_events",                   383191),
  ("fsize_local",                     987409145), # 987.41MB, avg file size 39.50MB
  ("fsize_db",                        19166074534), # 19.17GB, avg file size 798.59MB
  ("use_it",                          True),
  ("xsection",                        0.0004275219),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo2V2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo2V2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_152927"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       9),
  ("nof_db_files",                    14),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398197),
  ("nof_db_events",                   398197),
  ("fsize_local",                     802840690), # 802.84MB, avg file size 89.20MB
  ("fsize_db",                        17935707869), # 17.94GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.0001385868),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo2V2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo2V2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_153032"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2V2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       25),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 397295),
  ("nof_db_events",                   397295),
  ("fsize_local",                     995068452), # 995.07MB, avg file size 39.80MB
  ("fsize_db",                        19530490653), # 19.53GB, avg file size 849.15MB
  ("use_it",                          True),
  ("xsection",                        0.0003254642),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo2V2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo2V2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_m/201011_153138"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2V2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       22),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 396993),
  ("nof_db_events",                   396993),
  ("fsize_local",                     917034842), # 917.03MB, avg file size 41.68MB
  ("fsize_db",                        18832486606), # 18.83GB, avg file size 896.79MB
  ("use_it",                          True),
  ("xsection",                        0.001985145),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo2V2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo2V2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_m/201011_153248"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo2V2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       22),
  ("nof_db_files",                    19),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 398994),
  ("nof_db_events",                   398994),
  ("fsize_local",                     950279343), # 950.28MB, avg file size 43.19MB
  ("fsize_db",                        19150368996), # 19.15GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.0008142775),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo2V2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo2V2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcR/201011_153425"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4V_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       27),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 386496),
  ("nof_db_events",                   386496),
  ("fsize_local",                     901286443), # 901.29MB, avg file size 33.38MB
  ("fsize_db",                        18636089106), # 18.64GB, avg file size 776.50MB
  ("use_it",                          True),
  ("xsection",                        8.18177e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4V_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4V_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_153531"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4V_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       26),
  ("nof_db_files",                    25),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 397997),
  ("nof_db_events",                   397997),
  ("fsize_local",                     868084536), # 868.08MB, avg file size 33.39MB
  ("fsize_db",                        18558351469), # 18.56GB, avg file size 742.33MB
  ("use_it",                          True),
  ("xsection",                        0.00026503),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4V_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4V_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_153641"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4V_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       30),
  ("nof_db_files",                    28),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 397297),
  ("nof_db_events",                   397297),
  ("fsize_local",                     967817367), # 967.82MB, avg file size 32.26MB
  ("fsize_db",                        19570320877), # 19.57GB, avg file size 698.94MB
  ("use_it",                          True),
  ("xsection",                        0.003796343),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4V_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4V_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun/201011_153748"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/VBFHHTo4V_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       24),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399098),
  ("nof_db_events",                   399098),
  ("fsize_local",                     987055064), # 987.06MB, avg file size 41.13MB
  ("fsize_db",                        19933948507), # 19.93GB, avg file size 906.09MB
  ("use_it",                          True),
  ("xsection",                        0.003796343),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/VBFHHTo4V_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8/2016v3_2020Oct11_VBFHHTo4V_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCUETP8M1_PSweights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_/201011_153925"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_SM_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     221482748), # 221.48MB, avg file size 110.74MB
  ("fsize_db",                        4335254200), # 4.34GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_SM_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_SM_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_130811"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_box_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_box_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     214361350), # 214.36MB, avg file size 214.36MB
  ("fsize_db",                        4343698408), # 4.34GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_box_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_box_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_131050"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_2_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 95878),
  ("nof_db_events",                   95878),
  ("fsize_local",                     239546984), # 239.55MB, avg file size 239.55MB
  ("fsize_db",                        4587536778), # 4.59GB, avg file size 2.29GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_2_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_2_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_131230"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_3_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99000),
  ("nof_db_events",                   99000),
  ("fsize_local",                     221305771), # 221.31MB, avg file size 221.31MB
  ("fsize_db",                        4402287226), # 4.40GB, avg file size 1.47GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_3_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_3_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_131436"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_4_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97777),
  ("nof_db_events",                   97777),
  ("fsize_local",                     211897802), # 211.90MB, avg file size 211.90MB
  ("fsize_db",                        4296631601), # 4.30GB, avg file size 2.15GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_4_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_4_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_131643"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_5_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98210),
  ("nof_db_events",                   98210),
  ("fsize_local",                     233072264), # 233.07MB, avg file size 233.07MB
  ("fsize_db",                        4483694248), # 4.48GB, avg file size 2.24GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_5_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_5_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_131922"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_6_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99178),
  ("nof_db_events",                   99178),
  ("fsize_local",                     214218286), # 214.22MB, avg file size 214.22MB
  ("fsize_db",                        4255863331), # 4.26GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_6_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_6_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_132229"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_7_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 97801),
  ("nof_db_events",                   97801),
  ("fsize_local",                     197237094), # 197.24MB, avg file size 197.24MB
  ("fsize_db",                        3951072091), # 3.95GB, avg file size 1.98GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_7_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_7_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_132402"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_8_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99301),
  ("nof_db_events",                   99301),
  ("fsize_local",                     224147592), # 224.15MB, avg file size 224.15MB
  ("fsize_db",                        4354193987), # 4.35GB, avg file size 1.45GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_8_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_8_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_132613"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_9_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98588),
  ("nof_db_events",                   98588),
  ("fsize_local",                     229741491), # 229.74MB, avg file size 229.74MB
  ("fsize_db",                        4491891214), # 4.49GB, avg file size 2.25GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_9_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_9_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_132749"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_10_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 98724),
  ("nof_db_events",                   98724),
  ("fsize_local",                     202270712), # 202.27MB, avg file size 202.27MB
  ("fsize_db",                        4130096263), # 4.13GB, avg file size 2.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_10_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_10_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_132954"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_11_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     218274050), # 218.27MB, avg file size 109.14MB
  ("fsize_db",                        4262962926), # 4.26GB, avg file size 2.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_11_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_11_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_133201"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4Tau_node_12_13TeV-madgraph/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    2),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 99190),
  ("nof_db_events",                   99190),
  ("fsize_local",                     205420634), # 205.42MB, avg file size 205.42MB
  ("fsize_db",                        4123293762), # 4.12GB, avg file size 2.06GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 262000 - 262100 -> NNPDF30_lo_as_0130 PDF set, expecting 101 weights (counted 101 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/snandan/2016v3_2019Oct04/GluGluToHHTo4Tau_node_12_13TeV-madgraph/2016v3_2019Oct04_GluGluToHHTo4Tau_node_12_13TeV-madgraph__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v2/191004_133412"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2v2t"),
  ("nof_files",                       18),
  ("nof_db_files",                    15),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299096),
  ("nof_db_events",                   299096),
  ("fsize_local",                     684600408), # 684.60MB, avg file size 38.03MB
  ("fsize_db",                        12968987676), # 12.97GB, avg file size 864.60MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v/201011_154036"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2v2t"),
  ("nof_files",                       21),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     677603050), # 677.60MB, avg file size 32.27MB
  ("fsize_db",                        12924643901), # 12.92GB, avg file size 646.23MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_154237"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2v2t"),
  ("nof_files",                       24),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299096),
  ("nof_db_events",                   299096),
  ("fsize_local",                     790446903), # 790.45MB, avg file size 32.94MB
  ("fsize_db",                        14188726732), # 14.19GB, avg file size 644.94MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_154413"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2v2t"),
  ("nof_files",                       18),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     688792443), # 688.79MB, avg file size 38.27MB
  ("fsize_db",                        13070695442), # 13.07GB, avg file size 816.92MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_3_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_154518"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2v2t"),
  ("nof_files",                       15),
  ("nof_db_files",                    13),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299699),
  ("nof_db_events",                   299699),
  ("fsize_local",                     660287406), # 660.29MB, avg file size 44.02MB
  ("fsize_db",                        12793836191), # 12.79GB, avg file size 984.14MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_154656"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2v2t"),
  ("nof_files",                       22),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 290096),
  ("nof_db_events",                   290096),
  ("fsize_local",                     731523119), # 731.52MB, avg file size 33.25MB
  ("fsize_db",                        13319772071), # 13.32GB, avg file size 665.99MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_154801"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2v2t"),
  ("nof_files",                       23),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     686411094), # 686.41MB, avg file size 29.84MB
  ("fsize_db",                        12992110434), # 12.99GB, avg file size 590.55MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_154907"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2v2t"),
  ("nof_files",                       6),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 298795),
  ("nof_db_events",                   298795),
  ("fsize_local",                     631639785), # 631.64MB, avg file size 105.27MB
  ("fsize_db",                        12626549461), # 12.63GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_8_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_155013"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2v2t"),
  ("nof_files",                       19),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     732962611), # 732.96MB, avg file size 38.58MB
  ("fsize_db",                        13556885360), # 13.56GB, avg file size 753.16MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_155149"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2v2t"),
  ("nof_files",                       25),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 295998),
  ("nof_db_events",                   295998),
  ("fsize_local",                     682004161), # 682.00MB, avg file size 27.28MB
  ("fsize_db",                        12820088187), # 12.82GB, avg file size 534.17MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v/201011_155256"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_11_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2v2t"),
  ("nof_files",                       18),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     685354413), # 685.35MB, avg file size 38.08MB
  ("fsize_db",                        13031165765), # 13.03GB, avg file size 814.45MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_11_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_11_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v/201011_155401"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("nof_files",                       17),
  ("nof_db_files",                    16),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 292799),
  ("nof_db_events",                   292799),
  ("fsize_local",                     651284168), # 651.28MB, avg file size 38.31MB
  ("fsize_db",                        12450906706), # 12.45GB, avg file size 778.18MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v/201011_155535"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2v2t"),
  ("nof_files",                       12),
  ("nof_db_files",                    23),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 383199),
  ("nof_db_events",                   383199),
  ("fsize_local",                     829881936), # 829.88MB, avg file size 69.16MB
  ("fsize_db",                        15456054734), # 15.46GB, avg file size 672.00MB
  ("use_it",                          True),
  ("xsection",                        0.0020155),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-/201011_155644"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2v2t"),
  ("nof_files",                       9),
  ("nof_db_files",                    25),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     879727003), # 879.73MB, avg file size 97.75MB
  ("fsize_db",                        16374952584), # 16.37GB, avg file size 655.00MB
  ("use_it",                          True),
  ("xsection",                        0.00089753),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-/201011_155750"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
  ("nof_files",                       31),
  ("nof_db_files",                    31),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 393591),
  ("nof_db_events",                   393591),
  ("fsize_local",                     933062917), # 933.06MB, avg file size 30.10MB
  ("fsize_db",                        16238506681), # 16.24GB, avg file size 523.82MB
  ("use_it",                          True),
  ("xsection",                        0.00038015),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_/201011_155856"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo2V2Tau_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2v2t"),
  ("nof_files",                       26),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 395997),
  ("nof_db_events",                   395997),
  ("fsize_local",                     846304044), # 846.30MB, avg file size 32.55MB
  ("fsize_db",                        15486983330), # 15.49GB, avg file size 645.29MB
  ("use_it",                          True),
  ("xsection",                        0.00265166),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo2V2Tau_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo2V2Tau_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-/201011_160039"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4v"),
  ("nof_files",                       12),
  ("nof_db_files",                    24),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 390098),
  ("nof_db_events",                   390098),
  ("fsize_local",                     890391194), # 890.39MB, avg file size 74.20MB
  ("fsize_db",                        17662183893), # 17.66GB, avg file size 735.92MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_SM_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_160145"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_4v"),
  ("nof_files",                       22),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     918486785), # 918.49MB, avg file size 41.75MB
  ("fsize_db",                        17725404767), # 17.73GB, avg file size 984.74MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_1_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_160251"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4v"),
  ("nof_files",                       22),
  ("nof_db_files",                    20),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 379297),
  ("nof_db_events",                   379297),
  ("fsize_local",                     1007054907), # 1.01GB, avg file size 45.78MB
  ("fsize_db",                        18656297998), # 18.66GB, avg file size 932.81MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_2_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_160356"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4v"),
  ("nof_files",                       22),
  ("nof_db_files",                    22),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 380198),
  ("nof_db_events",                   380198),
  ("fsize_local",                     874738759), # 874.74MB, avg file size 39.76MB
  ("fsize_db",                        16911847129), # 16.91GB, avg file size 768.72MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_4_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_160534"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_4v"),
  ("nof_files",                       16),
  ("nof_db_files",                    12),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 399095),
  ("nof_db_events",                   399095),
  ("fsize_local",                     997354253), # 997.35MB, avg file size 62.33MB
  ("fsize_db",                        18837769814), # 18.84GB, avg file size 1.57GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_5_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_160640"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4v"),
  ("nof_files",                       21),
  ("nof_db_files",                    18),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 390594),
  ("nof_db_events",                   390594),
  ("fsize_local",                     893965351), # 893.97MB, avg file size 42.57MB
  ("fsize_db",                        17330267709), # 17.33GB, avg file size 962.79MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_7_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_160748"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4v"),
  ("nof_files",                       23),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 362398),
  ("nof_db_events",                   362398),
  ("fsize_local",                     915566078), # 915.57MB, avg file size 39.81MB
  ("fsize_db",                        17067209959), # 17.07GB, avg file size 812.72MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_9_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_160924"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_4v"),
  ("nof_files",                       23),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 372500),
  ("nof_db_events",                   372500),
  ("fsize_local",                     860563173), # 860.56MB, avg file size 37.42MB
  ("fsize_db",                        16520337515), # 16.52GB, avg file size 786.68MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_10_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_161035"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4v"),
  ("nof_files",                       23),
  ("nof_db_files",                    21),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 393997),
  ("nof_db_events",                   393997),
  ("fsize_local",                     904706953), # 904.71MB, avg file size 39.34MB
  ("fsize_db",                        17362352725), # 17.36GB, avg file size 826.78MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         ""),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_12_TuneCUETP8M1_PSWeights_13TeV-madgraph-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_161141"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_4v"),
  ("nof_files",                       37),
  ("nof_db_files",                    40),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 971897),
  ("nof_db_events",                   971897),
  ("fsize_local",                     2193274108), # 2.19GB, avg file size 59.28MB
  ("fsize_db",                        40336608667), # 40.34GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.00385439),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_cHHH0_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_161247"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_4v"),
  ("nof_files",                       22),
  ("nof_db_files",                    45),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 962393),
  ("nof_db_events",                   962393),
  ("fsize_local",                     2194411054), # 2.19GB, avg file size 99.75MB
  ("fsize_db",                        40722538714), # 40.72GB, avg file size 904.95MB
  ("use_it",                          True),
  ("xsection",                        0.00171641),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_cHHH1_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_161423"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_4v"),
  ("nof_files",                       21),
  ("nof_db_files",                    31),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 991594),
  ("nof_db_events",                   991594),
  ("fsize_local",                     2253599867), # 2.25GB, avg file size 107.31MB
  ("fsize_db",                        41734175155), # 41.73GB, avg file size 1.35GB
  ("use_it",                          True),
  ("xsection",                        0.00072699),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_cHHH2p45_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v/201011_161529"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["/GluGluToHHTo4V_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_4v"),
  ("nof_files",                       37),
  ("nof_db_files",                    48),
  ("nof_events",                      {
  }),
  ("nof_tree_events",                 974394),
  ("nof_db_events",                   974394),
  ("fsize_local",                     2035100003), # 2.04GB, avg file size 55.00MB
  ("fsize_db",                        38929152863), # 38.93GB, avg file size 811.02MB
  ("use_it",                          True),
  ("xsection",                        0.00507095),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/cms/store/user/kaehatah/2016v3_2020Oct11/GluGluToHHTo4V_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8/2016v3_2020Oct11_GluGluToHHTo4V_node_cHHH5_TuneCUETP8M1_PSWeights_13TeV-powheg-pythia8__RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3-v1/201011_161642"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
  ("missing_from_superset",        [
    # not computed
  ]),
  ("missing_hlt_paths",            [

  ]),
  ("hlt_paths",                    [
    # not computed
  ]),
])

samples_2016["sum_events"] = [
  [ 'signal_ggf_spin0_650_hh_4t',                      'signal_ggf_spin0_650_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_450_hh_4t',                      'signal_ggf_spin0_450_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_260_hh_4t',                      'signal_ggf_spin0_260_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_750_hh_4t',                      'signal_ggf_spin0_750_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_700_hh_4t',                      'signal_ggf_spin2_700_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_650_hh_4t',                      'signal_ggf_spin2_650_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_250_hh_4t',                      'signal_ggf_spin2_250_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_550_hh_4t',                      'signal_ggf_spin2_550_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_350_hh_4t',                      'signal_ggf_spin2_350_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_400_hh_4t',                      'signal_ggf_spin2_400_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_600_hh_4t',                      'signal_ggf_spin2_600_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_350_hh_4t',                      'signal_ggf_spin0_350_hh_4t_PSWeights',             ],
  [ 'signal_ggf_nonresonant_node_sm_hh_4v',            'signal_ggf_nonresonant_node_1_hh_4v',             'signal_ggf_nonresonant_node_2_hh_4v',             'signal_ggf_nonresonant_node_3_hh_4v',             'signal_ggf_nonresonant_node_4_hh_4v',             'signal_ggf_nonresonant_node_5_hh_4v',             'signal_ggf_nonresonant_node_6_hh_4v',             'signal_ggf_nonresonant_node_7_hh_4v',             'signal_ggf_nonresonant_node_8_hh_4v',             'signal_ggf_nonresonant_node_9_hh_4v',             'signal_ggf_nonresonant_node_10_hh_4v',            'signal_ggf_nonresonant_node_11_hh_4v',            'signal_ggf_nonresonant_node_12_hh_4v',             ],
  [ 'signal_ggf_spin2_900_hh_4t',                      'signal_ggf_spin2_900_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_300_hh_4t',                      'signal_ggf_spin2_300_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_550_hh_4t',                      'signal_ggf_spin0_550_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_280_hh_4t',                      'signal_ggf_spin0_280_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_600_hh_4t',                      'signal_ggf_spin0_600_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_450_hh_4t',                      'signal_ggf_spin2_450_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_700_hh_4t',                      'signal_ggf_spin0_700_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_280_hh_4t',                      'signal_ggf_spin2_280_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_320_hh_4t',                      'signal_ggf_spin0_320_hh_4t_PSWeights',             ],
  [ 'signal_ggf_nonresonant_node_sm_hh_2v2t',          'signal_ggf_nonresonant_node_1_hh_2v2t',           'signal_ggf_nonresonant_node_2_hh_2v2t',           'signal_ggf_nonresonant_node_3_hh_2v2t',           'signal_ggf_nonresonant_node_4_hh_2v2t',           'signal_ggf_nonresonant_node_5_hh_2v2t',           'signal_ggf_nonresonant_node_6_hh_2v2t',           'signal_ggf_nonresonant_node_7_hh_2v2t',           'signal_ggf_nonresonant_node_8_hh_2v2t',           'signal_ggf_nonresonant_node_9_hh_2v2t',           'signal_ggf_nonresonant_node_10_hh_2v2t',          'signal_ggf_nonresonant_node_11_hh_2v2t',          'signal_ggf_nonresonant_node_12_hh_2v2t',           ],
  [ 'signal_ggf_spin2_800_hh_4t',                      'signal_ggf_spin2_800_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_900_hh_4t',                      'signal_ggf_spin0_900_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_320_hh_4t',                      'signal_ggf_spin2_320_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_260_hh_4t',                      'signal_ggf_spin2_260_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_270_hh_4t',                      'signal_ggf_spin2_270_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_300_hh_4t',                      'signal_ggf_spin0_300_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_250_hh_4t',                      'signal_ggf_spin0_250_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_800_hh_4t',                      'signal_ggf_spin0_800_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_500_hh_4t',                      'signal_ggf_spin0_500_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_500_hh_4t',                      'signal_ggf_spin2_500_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin0_400_hh_4t',                      'signal_ggf_spin0_400_hh_4t_PSWeights',             ],
  [ 'signal_ggf_nonresonant_node_sm_hh_4t',            'signal_ggf_nonresonant_node_box_hh_4t',           'signal_ggf_nonresonant_node_2_hh_4t',             'signal_ggf_nonresonant_node_3_hh_4t',             'signal_ggf_nonresonant_node_4_hh_4t',             'signal_ggf_nonresonant_node_5_hh_4t',             'signal_ggf_nonresonant_node_6_hh_4t',             'signal_ggf_nonresonant_node_7_hh_4t',             'signal_ggf_nonresonant_node_8_hh_4t',             'signal_ggf_nonresonant_node_9_hh_4t',             'signal_ggf_nonresonant_node_10_hh_4t',            'signal_ggf_nonresonant_node_11_hh_4t',            'signal_ggf_nonresonant_node_12_hh_4t',             ],
  [ 'signal_ggf_spin0_270_hh_4t',                      'signal_ggf_spin0_270_hh_4t_PSWeights',             ],
  [ 'signal_ggf_spin2_750_hh_4t',                      'signal_ggf_spin2_750_hh_4t_PSWeights',             ],
]

