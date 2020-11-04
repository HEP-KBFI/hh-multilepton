from collections import OrderedDict as OD

# file generated at 2020-11-04 10:42:21 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017.py -p python/samples/sampleLocations_2017_hh_multilepton.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh.py -M

samples_2017 = OD()
samples_2017["/GluGluToRadionToHHTo4Tau_M-250_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99957031e+05, 3.99953688e+05, 3.99928375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99957031e+05, 3.99957031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91753375e+05, 3.91738375e+05, 3.91746656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91753375e+05, 3.89637000e+05, 3.93799188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.91753375e+05, 3.91753375e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1429499835), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        20114964479), # 20.11GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-260_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99961438e+05, 3.99946344e+05, 3.99950031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06226969e+05, 3.99961438e+05, 3.91154312e+05, 4.06226969e+05, 3.99961438e+05, 3.91154312e+05, 4.06226969e+05, 3.99961438e+05, 3.91154312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06227031e+05, 3.91154188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91466938e+05, 3.91443594e+05, 3.91480688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91466938e+05, 3.89297375e+05, 3.93563812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.97544938e+05, 3.91466938e+05, 3.82896062e+05, 3.97544938e+05, 3.91466938e+05, 3.82896062e+05, 3.97544938e+05, 3.91466938e+05, 3.82896062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.97545000e+05, 3.82895938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1437293231), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        19104985604), # 19.10GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-270_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 385000, ],
    'CountWeighted'                                                                  : [ 3.84993750e+05, 3.85057594e+05, 3.84965562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.92263188e+05, 3.84993750e+05, 3.75530156e+05, 3.92263188e+05, 3.84993750e+05, 3.75530156e+05, 3.92263188e+05, 3.84993750e+05, 3.75530156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92263188e+05, 3.75530156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76402062e+05, 3.76428656e+05, 3.76390625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76402062e+05, 3.74220438e+05, 3.78504656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.83448656e+05, 3.76402062e+05, 3.67198688e+05, 3.83448656e+05, 3.76402062e+05, 3.67198688e+05, 3.83448656e+05, 3.76402062e+05, 3.67198688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.83448656e+05, 3.67198688e+05, ],
  }),
  ("nof_tree_events",                 385000),
  ("nof_db_events",                   385000),
  ("fsize_local",                     1402099938), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        18511645006), # 18.51GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-280_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00002250e+05, 3.99926938e+05, 3.99922531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00002250e+05, 4.00002250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90729938e+05, 3.90657969e+05, 3.90687344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90729938e+05, 3.88399594e+05, 3.92989812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.90729938e+05, 3.90729938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1485019968), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        20219319064), # 20.22GB, avg file size 962.82MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-300_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00057781e+05, 2.99966938e+05, 3.00015094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08244250e+05, 3.00057781e+05, 2.90542875e+05, 3.08244250e+05, 3.00057781e+05, 2.90542875e+05, 3.08244250e+05, 3.00057781e+05, 2.90542875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08244250e+05, 2.90542875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92679156e+05, 2.92604406e+05, 2.92668125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92679156e+05, 2.90846750e+05, 2.94457625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00635875e+05, 2.92679156e+05, 2.83460219e+05, 3.00635875e+05, 2.92679156e+05, 2.83460219e+05, 3.00635875e+05, 2.92679156e+05, 2.83460219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00635875e+05, 2.83460219e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1131312058), # 1.13GB, avg file size 1.13GB
  ("fsize_db",                        14610494649), # 14.61GB, avg file size 859.44MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4T_M-320_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83996157e+05, 3.83945211e+05, 3.83959251e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.96573156e+05, 3.83992470e+05, 3.70279047e+05, 3.96573156e+05, 3.83992470e+05, 3.70279047e+05, 3.96573156e+05, 3.83992470e+05, 3.70279047e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96573156e+05, 3.70279047e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.52580716e+06, 2.49165395e+06, 3.20676205e+06, 2.52373976e+06, 2.28423127e+06, 1.67158230e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.84011349e+05, 3.84001825e+05, 5.29283764e+05, 3.83979655e+05, 3.83623256e+05, 2.54140927e+05, ],
    'CountWeightedFull'                                                              : [ 3.83970726e+05, 3.83920283e+05, 3.83934108e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.96547217e+05, 3.83967040e+05, 3.70254897e+05, 3.96547217e+05, 3.83967040e+05, 3.70254897e+05, 3.96547217e+05, 3.83967040e+05, 3.70254897e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96547217e+05, 3.70254897e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.52565501e+06, 2.49149313e+06, 3.20655011e+06, 2.52356170e+06, 2.28408262e+06, 1.67147640e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.83988171e+05, 3.83976941e+05, 5.29248721e+05, 3.83952706e+05, 3.83598347e+05, 2.54124827e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74033666e+05, 3.73981500e+05, 3.74024877e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74033666e+05, 3.71583656e+05, 3.76418798e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.86220813e+05, 3.74030453e+05, 3.60738461e+05, 3.86220813e+05, 3.74030453e+05, 3.60738461e+05, 3.86220813e+05, 3.74030453e+05, 3.60738461e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86220813e+05, 3.60738461e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.46267030e+06, 2.42688204e+06, 3.12315223e+06, 2.45536484e+06, 2.22597778e+06, 1.62900470e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74409890e+05, 3.73988680e+05, 5.15433244e+05, 3.73571093e+05, 3.73801344e+05, 2.47666729e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74009752e+05, 3.73957910e+05, 3.74001098e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74009752e+05, 3.71559999e+05, 3.76394548e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.86196280e+05, 3.74006516e+05, 3.60715574e+05, 3.86196280e+05, 3.74006516e+05, 3.60715574e+05, 3.86196280e+05, 3.74006516e+05, 3.60715574e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.86196280e+05, 3.60715574e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.46252671e+06, 2.42672980e+06, 3.12295219e+06, 2.45519738e+06, 2.22583715e+06, 1.62890452e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74388012e+05, 3.73965193e+05, 5.15400023e+05, 3.73545568e+05, 3.73777775e+05, 2.47651513e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1485378273), # 1.49GB, avg file size 495.13MB
  ("fsize_db",                        18874636094), # 18.87GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_320_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-350_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 284000, ],
    'CountWeighted'                                                                  : [ 2.83970438e+05, 2.83959250e+05, 2.83963875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.95331719e+05, 2.83970438e+05, 2.72299188e+05, 2.95331719e+05, 2.83970438e+05, 2.72299188e+05, 2.95331719e+05, 2.83970438e+05, 2.72299188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.95331719e+05, 2.72299188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.76080312e+05, 2.76070188e+05, 2.76078031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.76080312e+05, 2.74166875e+05, 2.77949250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.87068875e+05, 2.76080312e+05, 2.64774062e+05, 2.87068875e+05, 2.76080312e+05, 2.64774062e+05, 2.87068875e+05, 2.76080312e+05, 2.64774062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87068875e+05, 2.64774062e+05, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1123577013), # 1.12GB, avg file size 1.12GB
  ("fsize_db",                        14267271177), # 14.27GB, avg file size 713.36MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-400_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99956062e+05, 3.00033688e+05, 2.99897688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15120312e+05, 2.99931344e+05, 2.85260031e+05, 3.15120312e+05, 2.99931344e+05, 2.85260031e+05, 3.15120312e+05, 2.99931344e+05, 2.85260031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15120312e+05, 2.85260031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91050375e+05, 2.91096750e+05, 2.91005719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91050375e+05, 2.88914062e+05, 2.93143812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.05691750e+05, 2.91032938e+05, 2.76833500e+05, 3.05691750e+05, 2.91032938e+05, 2.76833500e+05, 3.05691750e+05, 2.91032938e+05, 2.76833500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.05691750e+05, 2.76833500e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1237729003), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        15112224162), # 15.11GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-450_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99869188e+05, 2.99990656e+05, 2.99933562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.17756500e+05, 2.99869188e+05, 2.83230938e+05, 3.17756500e+05, 2.99869188e+05, 2.83230938e+05, 3.17756500e+05, 2.99869188e+05, 2.83230938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.17756500e+05, 2.83230938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90399625e+05, 2.90460875e+05, 2.90451469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90399625e+05, 2.88156688e+05, 2.92608094e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.07626625e+05, 2.90399625e+05, 2.74311250e+05, 3.07626625e+05, 2.90399625e+05, 2.74311250e+05, 3.07626625e+05, 2.90399625e+05, 2.74311250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.07626625e+05, 2.74311250e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1282107768), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        15314286391), # 15.31GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-500_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99976188e+05, 1.99985062e+05, 1.99951828e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13411406e+05, 1.99975797e+05, 1.87663062e+05, 2.13411406e+05, 1.99975797e+05, 1.87663062e+05, 2.13411406e+05, 1.99975797e+05, 1.87663062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13411406e+05, 1.87662984e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93292469e+05, 1.93282797e+05, 1.93288906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93292469e+05, 1.91721219e+05, 1.94837500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06223859e+05, 1.93291688e+05, 1.81419188e+05, 2.06223859e+05, 1.93291688e+05, 1.81419188e+05, 2.06223859e+05, 1.93291688e+05, 1.81419188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06223875e+05, 1.81419125e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     881123312), # 881.12MB, avg file size 881.12MB
  ("fsize_db",                        10307241524), # 10.31GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-550_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 2.00003844e+05, 1.99925719e+05, 1.99958438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14706484e+05, 2.00003375e+05, 1.86563125e+05, 2.14706484e+05, 2.00003375e+05, 1.86563125e+05, 2.14706484e+05, 2.00003375e+05, 1.86563125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14706484e+05, 1.86563125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93005594e+05, 1.92956750e+05, 1.92971266e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93005594e+05, 1.91376734e+05, 1.94608969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07165891e+05, 1.93004234e+05, 1.80086281e+05, 2.07165891e+05, 1.93004234e+05, 1.80086281e+05, 2.07165891e+05, 1.93004234e+05, 1.80086281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07165891e+05, 1.80086281e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     906855322), # 906.86MB, avg file size 906.86MB
  ("fsize_db",                        10435371711), # 10.44GB, avg file size 948.67MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-600_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99988156e+05, 1.99935125e+05, 2.00006656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15949203e+05, 1.99988156e+05, 1.85660000e+05, 2.15949203e+05, 1.99988156e+05, 1.85660000e+05, 2.15949203e+05, 1.99988156e+05, 1.85660000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15949203e+05, 1.85660000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92779031e+05, 1.92745266e+05, 1.92800969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92779031e+05, 1.91110969e+05, 1.94433688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08126688e+05, 1.92779031e+05, 1.79011344e+05, 2.08126688e+05, 1.92779031e+05, 1.79011344e+05, 2.08126688e+05, 1.92779031e+05, 1.79011344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08126688e+05, 1.79011344e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     928090478), # 928.09MB, avg file size 928.09MB
  ("fsize_db",                        10556003606), # 10.56GB, avg file size 812.00MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-650_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99969578e+05, 1.99942344e+05, 1.99977375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17051531e+05, 1.99969578e+05, 1.84812906e+05, 2.17051531e+05, 1.99969578e+05, 1.84812906e+05, 2.17051531e+05, 1.99969578e+05, 1.84812906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17051531e+05, 1.84812906e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92693047e+05, 1.92676250e+05, 1.92697156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92693047e+05, 1.91008438e+05, 1.94356531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09105688e+05, 1.92693047e+05, 1.78123000e+05, 2.09105688e+05, 1.92693047e+05, 1.78123000e+05, 2.09105688e+05, 1.92693047e+05, 1.78123000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09105688e+05, 1.78123000e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     947767551), # 947.77MB, avg file size 947.77MB
  ("fsize_db",                        10638007613), # 10.64GB, avg file size 709.20MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-700_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99992250e+05, 1.99943938e+05, 1.99941984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18037719e+05, 1.99992250e+05, 1.84049938e+05, 2.18037719e+05, 1.99992250e+05, 1.84049938e+05, 2.18037719e+05, 1.99992250e+05, 1.84049938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18037734e+05, 1.84049922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92485031e+05, 1.92428969e+05, 1.92478656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92485031e+05, 1.90761438e+05, 1.94192500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09814281e+05, 1.92485031e+05, 1.77188094e+05, 2.09814281e+05, 1.92485031e+05, 1.77188094e+05, 2.09814281e+05, 1.92485031e+05, 1.77188094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09814312e+05, 1.77188094e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     967715015), # 967.72MB, avg file size 967.72MB
  ("fsize_db",                        10705047349), # 10.71GB, avg file size 823.47MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-750_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99970875e+05, 1.99962328e+05, 1.99938578e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99970875e+05, 1.99970875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92279688e+05, 1.92263469e+05, 1.92259812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92279688e+05, 1.90512500e+05, 1.94022906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92279688e+05, 1.92279688e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     992480121), # 992.48MB, avg file size 992.48MB
  ("fsize_db",                        11200569052), # 11.20GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-800_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99963828e+05, 1.99952047e+05, 1.99986594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99963828e+05, 1.99963828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92240906e+05, 1.92226234e+05, 1.92261062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92240906e+05, 1.90470438e+05, 1.93990406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92240906e+05, 1.92240906e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1008140850), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11266991203), # 11.27GB, avg file size 1.13GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-850_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91955125e+05, 1.91988688e+05, 1.91948766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91955125e+05, 1.91955125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84439766e+05, 1.84463156e+05, 1.84428703e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84439766e+05, 1.82721688e+05, 1.86140719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84439766e+05, 1.84439766e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     981459235), # 981.46MB, avg file size 981.46MB
  ("fsize_db",                        10933218336), # 10.93GB, avg file size 993.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-900_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99836094e+04, 9.99947656e+04, 1.00000039e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10686578e+05, 9.99836094e+04, 9.08187266e+04, 1.10686578e+05, 9.99836094e+04, 9.08187266e+04, 1.10686578e+05, 9.99836094e+04, 9.08187266e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10686578e+05, 9.08187266e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.60522109e+04, 9.60615703e+04, 9.60546406e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.60522109e+04, 9.51564141e+04, 9.69388203e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06304250e+05, 9.60522109e+04, 8.72628516e+04, 1.06304250e+05, 9.60522109e+04, 8.72628516e+04, 1.06304250e+05, 9.60522109e+04, 8.72628516e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06304250e+05, 8.72628516e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514409988), # 514.41MB, avg file size 514.41MB
  ("fsize_db",                        5507575850), # 5.51GB, avg file size 917.93MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4Tau_M-1000_narrow_13TeV-madgraph/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99722188e+04, 9.99884297e+04, 9.99862969e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11340117e+05, 9.99722188e+04, 9.03435859e+04, 1.11340117e+05, 9.99722188e+04, 9.03435859e+04, 1.11340117e+05, 9.99722188e+04, 9.03435859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11340117e+05, 9.03435859e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59610938e+04, 9.59567109e+04, 9.59825078e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59610938e+04, 9.50512031e+04, 9.68641797e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06847047e+05, 9.59610938e+04, 8.67302969e+04, 1.06847047e+05, 9.59610938e+04, 8.67302969e+04, 1.06847047e+05, 9.59610938e+04, 8.67302969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06847047e+05, 8.67302969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     525161359), # 525.16MB, avg file size 525.16MB
  ("fsize_db",                        5537065038), # 5.54GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4t"),
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

samples_2017["/GluGluToRadionToHHTo4tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99794453e+04, 9.99808281e+04, 9.99743906e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11334656e+05, 9.99794453e+04, 9.03382812e+04, 1.11334656e+05, 9.99794453e+04, 9.03382812e+04, 1.11334656e+05, 9.99794453e+04, 9.03382812e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11334891e+05, 9.03380469e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.73073438e+05, 3.73246844e+05, 5.13219062e+05, 3.73284562e+05, 3.60771281e+05, 2.37590094e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99612266e+04, 1.00042055e+05, 1.40676625e+05, 1.00016812e+05, 9.97975156e+04, 6.36620938e+04, ],
    'CountWeightedFull'                                                              : [ 9.99692891e+04, 9.99705234e+04, 9.99642812e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11323367e+05, 9.99692891e+04, 9.03290859e+04, 1.11323367e+05, 9.99692891e+04, 9.03290859e+04, 1.11323367e+05, 9.99692891e+04, 9.03290859e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11323602e+05, 9.03288516e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.73038344e+05, 3.73209500e+05, 5.13166062e+05, 3.73243375e+05, 3.60734250e+05, 2.37566719e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99518281e+04, 1.00032086e+05, 1.40661906e+05, 1.00005820e+05, 9.97870078e+04, 6.36558008e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59692734e+04, 9.59604062e+04, 9.59746172e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59692734e+04, 9.50624688e+04, 9.68695156e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06847922e+05, 9.59692734e+04, 8.67306719e+04, 1.06847922e+05, 9.59692734e+04, 8.67306719e+04, 1.06847922e+05, 9.59692734e+04, 8.67306719e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06848141e+05, 8.67304531e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.58655969e+05, 3.58207062e+05, 4.92515812e+05, 3.57636188e+05, 3.46413219e+05, 2.28139688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.60937734e+04, 9.60076797e+04, 1.34981438e+05, 9.58197969e+04, 9.58038047e+04, 6.11262031e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.59598906e+04, 9.59509453e+04, 9.59652734e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.59598906e+04, 9.50533047e+04, 9.68600000e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.06837547e+05, 9.59598906e+04, 8.67222109e+04, 1.06837547e+05, 9.59598906e+04, 8.67222109e+04, 1.06837547e+05, 9.59598906e+04, 8.67222109e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.06837766e+05, 8.67219922e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.58623719e+05, 3.58172844e+05, 4.92467125e+05, 3.57598156e+05, 3.46379000e+05, 2.28118172e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.60851250e+04, 9.59984766e+04, 1.34967812e+05, 9.58096875e+04, 9.57941250e+04, 6.11204492e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     527610466), # 527.61MB, avg file size 527.61MB
  ("fsize_db",                        5625360264), # 5.63GB, avg file size 625.04MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_4t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99675938e+04, 9.99719766e+04, 9.99661562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99675938e+04, 9.99675938e+04, ],
    'CountWeightedPSWeight'                                                          : [ 4.68513562e+05, 4.67935750e+05, 6.34197125e+05, 4.67822375e+05, 4.40799750e+05, 2.95913188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00062578e+05, 1.00162328e+05, 1.41138031e+05, 9.99150469e+04, 9.96132812e+04, 6.32021562e+04, ],
    'CountWeightedFull'                                                              : [ 9.99554688e+04, 9.99598906e+04, 9.99540391e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99554688e+04, 9.99554688e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.68461312e+05, 4.67880031e+05, 6.34119750e+05, 4.67762250e+05, 4.40745125e+05, 2.95878531e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00051438e+05, 1.00150375e+05, 1.41120781e+05, 9.99022031e+04, 9.96009531e+04, 6.31947891e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.57906875e+04, 9.57854297e+04, 9.57983594e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.57906875e+04, 9.48498281e+04, 9.67250312e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.57906875e+04, 9.57906875e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 4.49641719e+05, 4.48253000e+05, 6.07699562e+05, 4.47379500e+05, 4.22662250e+05, 2.83622156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.60223438e+04, 9.59413359e+04, 1.35243781e+05, 9.55401094e+04, 9.55152344e+04, 6.05698555e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.57795000e+04, 9.57742656e+04, 9.57872266e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.57795000e+04, 9.48388750e+04, 9.67136719e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.57795000e+04, 9.57795000e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.49593406e+05, 4.48201719e+05, 6.07628375e+05, 4.47323812e+05, 4.22611969e+05, 2.83590250e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.60120391e+04, 9.59303672e+04, 1.35227938e+05, 9.55282344e+04, 9.55038984e+04, 6.05630156e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     548668105), # 548.67MB, avg file size 548.67MB
  ("fsize_db",                        5900418024), # 5.90GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_4t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_4t_PSWeights"),
  ("nof_files",                       2),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 99000, ],
    'CountWeighted'                                                                  : [ 9.89602351e+04, 9.89549255e+04, 9.89615635e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.12757194e+05, 9.89597507e+04, 8.76297546e+04, 1.12757194e+05, 9.89597507e+04, 8.76297546e+04, 1.12757194e+05, 9.89597507e+04, 8.76297546e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12757241e+05, 8.76296765e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.97606131e+05, 5.90384195e+05, 7.81398488e+05, 5.96843623e+05, 5.38633447e+05, 3.75516201e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.90542517e+04, 9.90528308e+04, 1.40263747e+05, 9.89503008e+04, 9.88191042e+04, 6.22461084e+04, ],
    'CountWeightedFull'                                                              : [ 9.89472632e+04, 9.89419224e+04, 9.89485020e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.12742433e+05, 9.89467710e+04, 8.76182571e+04, 1.12742433e+05, 9.89467710e+04, 8.76182571e+04, 1.12742433e+05, 9.89467710e+04, 8.76182571e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.12742464e+05, 8.76181790e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.97533252e+05, 5.90308162e+05, 7.81295289e+05, 5.96759322e+05, 5.38562086e+05, 3.75467183e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.90421052e+04, 9.90401001e+04, 1.40245218e+05, 9.89363423e+04, 9.88059426e+04, 6.22379700e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.47062080e+04, 9.46886936e+04, 9.47229248e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.47062080e+04, 9.37572200e+04, 9.56504734e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07893220e+05, 9.47056377e+04, 8.38767488e+04, 1.07893220e+05, 9.47056377e+04, 8.38767488e+04, 1.07893220e+05, 9.47056377e+04, 8.38767488e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07893251e+05, 8.38766707e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 5.72883814e+05, 5.64851906e+05, 7.47732162e+05, 5.69996873e+05, 5.15868117e+05, 3.59528699e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.49494983e+04, 9.47546824e+04, 1.34187960e+05, 9.44925098e+04, 9.46117063e+04, 5.95911445e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.46943374e+04, 9.46767786e+04, 9.47110435e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.46943374e+04, 9.37456096e+04, 9.56383899e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.07879708e+05, 9.46937593e+04, 8.38662058e+04, 1.07879708e+05, 9.46937593e+04, 8.38662058e+04, 1.07879708e+05, 9.46937593e+04, 8.38662058e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.07879740e+05, 8.38661355e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 5.72817154e+05, 5.64782541e+05, 7.47638107e+05, 5.69919857e+05, 5.15802662e+05, 3.59484019e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.49383987e+04, 9.47430820e+04, 1.34171065e+05, 9.44797629e+04, 9.45996719e+04, 5.95836965e+04, ],
  }),
  ("nof_tree_events",                 99000),
  ("nof_db_events",                   99000),
  ("fsize_local",                     537968065), # 537.97MB, avg file size 268.98MB
  ("fsize_db",                        5826586959), # 5.83GB, avg file size 971.10MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_4t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99623594e+04, 9.99540469e+04, 9.99611562e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99623594e+04, 9.99623594e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.95835812e+05, 3.95023531e+05, 5.46412375e+05, 3.95633938e+05, 3.80721312e+05, 2.47833547e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00027406e+05, 9.98881719e+04, 1.42180641e+05, 9.99758125e+04, 1.00249375e+05, 6.26312539e+04, ],
    'CountWeightedFull'                                                              : [ 9.99480703e+04, 9.99398984e+04, 9.99467891e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99480703e+04, 9.99480703e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95783125e+05, 3.94966781e+05, 5.46332625e+05, 3.95574094e+05, 3.80666094e+05, 2.47798828e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00014125e+05, 9.98738828e+04, 1.42159891e+05, 9.99607578e+04, 1.00234805e+05, 6.26224141e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56577422e+04, 9.56380625e+04, 9.56715703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56577422e+04, 9.46986797e+04, 9.66115781e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.56577422e+04, 9.56577422e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.79439094e+05, 3.77873812e+05, 5.22777531e+05, 3.77794219e+05, 3.64564219e+05, 2.37264062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.58737500e+04, 9.55417031e+04, 1.36010609e+05, 9.54576094e+04, 9.59739062e+04, 5.99529727e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.56444062e+04, 9.56248750e+04, 9.56582109e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.56444062e+04, 9.46856094e+04, 9.65980547e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.56444062e+04, 9.56444062e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.79390000e+05, 3.77821219e+05, 5.22703281e+05, 3.77738656e+05, 3.64512750e+05, 2.37231562e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.58613906e+04, 9.55285000e+04, 1.35991391e+05, 9.54436328e+04, 9.59603438e+04, 5.99447422e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     543255545), # 543.26MB, avg file size 543.26MB
  ("fsize_db",                        6809063426), # 6.81GB, avg file size 851.13MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_4t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99237656e+04, 9.99264766e+04, 9.99277344e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15692781e+05, 9.99237656e+04, 8.72091016e+04, 1.15692781e+05, 9.99237656e+04, 8.72091016e+04, 1.15692781e+05, 9.99237656e+04, 8.72091016e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15693656e+05, 8.72082109e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98065188e+05, 9.44710875e+05, 9.99321500e+05, 9.95002312e+05, 8.55772250e+05, 7.98677750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00025781e+05, 1.00070984e+05, 1.42326641e+05, 9.99511719e+04, 9.99243438e+04, 6.24096719e+04, ],
    'CountWeightedFull'                                                              : [ 9.99089219e+04, 9.99117812e+04, 9.99126719e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15675625e+05, 9.99089219e+04, 8.71961328e+04, 1.15675625e+05, 9.99089219e+04, 8.71961328e+04, 1.15675625e+05, 9.99089219e+04, 8.71961328e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15676508e+05, 8.71952422e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.97919375e+05, 9.44571375e+05, 9.99171250e+05, 9.94855875e+05, 8.55643938e+05, 7.98564125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00012242e+05, 1.00056406e+05, 1.42304859e+05, 9.99355625e+04, 9.99086328e+04, 6.24008047e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.55343750e+04, 9.55351562e+04, 9.55325312e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.55343750e+04, 9.45593047e+04, 9.65053281e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.10595734e+05, 9.55343750e+04, 8.33852578e+04, 1.10595734e+05, 9.55343750e+04, 8.33852578e+04, 1.10595734e+05, 9.55343750e+04, 8.33852578e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10596383e+05, 8.33846094e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.54215250e+05, 9.03302125e+05, 9.55397000e+05, 9.51154688e+05, 8.18407250e+05, 7.63884875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.57810000e+04, 9.56626172e+04, 1.36014125e+05, 9.53439844e+04, 9.55112344e+04, 5.96779023e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.55205859e+04, 9.55214688e+04, 9.55186406e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.55205859e+04, 9.45458516e+04, 9.64913750e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.10579844e+05, 9.55205859e+04, 8.33732578e+04, 1.10579844e+05, 9.55205859e+04, 8.33732578e+04, 1.10579844e+05, 9.55205859e+04, 8.33732578e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.10580500e+05, 8.33726016e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.54080250e+05, 9.03173500e+05, 9.55258562e+05, 9.51019125e+05, 8.18289250e+05, 7.63779875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.57684844e+04, 9.56491016e+04, 1.35993797e+05, 9.53294844e+04, 9.54965859e+04, 5.96696680e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     539456944), # 539.46MB, avg file size 539.46MB
  ("fsize_db",                        5854674389), # 5.85GB, avg file size 731.83MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_4t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.98730938e+04, 9.98913984e+04, 9.98865156e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98730938e+04, 9.98730938e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.24378812e+05, 8.44201625e+05, 9.97537375e+05, 9.12874812e+05, 7.42855750e+05, 5.99568625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99298281e+04, 9.97760625e+04, 1.42390375e+05, 1.00074055e+05, 1.00117766e+05, 6.22810469e+04, ],
    'CountWeightedFull'                                                              : [ 9.98543750e+04, 9.98724062e+04, 9.98678594e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98543750e+04, 9.98543750e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.24228812e+05, 8.44052125e+05, 9.97351188e+05, 9.12711750e+05, 7.42710625e+05, 5.99467062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99140156e+04, 9.97585781e+04, 1.42361203e+05, 1.00055656e+05, 1.00095516e+05, 6.22705391e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53778984e+04, 9.53927109e+04, 9.53803594e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53778984e+04, 9.43892188e+04, 9.63657031e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.53778984e+04, 9.53778984e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.83697500e+05, 8.06071875e+05, 9.52605875e+05, 8.70468250e+05, 7.10002125e+05, 5.72939250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.55920859e+04, 9.52071875e+04, 1.35940156e+05, 9.53303594e+04, 9.56952969e+04, 5.95054141e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.53604531e+04, 9.53751250e+04, 9.53630703e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.53604531e+04, 9.43720625e+04, 9.63480156e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.53604531e+04, 9.53604531e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 8.83557875e+05, 8.05932625e+05, 9.52432375e+05, 8.70316625e+05, 7.09867625e+05, 5.72844750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.55774062e+04, 9.51910781e+04, 1.35913203e+05, 9.53134062e+04, 9.56746406e+04, 5.94956406e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     541067818), # 541.07MB, avg file size 541.07MB
  ("fsize_db",                        6884912483), # 6.88GB, avg file size 764.99MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_4t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.97830781e+04, 9.97864297e+04, 9.97802969e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97830781e+04, 9.97830781e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.97851000e+05, 9.83602625e+05, 9.97883000e+05, 9.97856375e+05, 9.31972062e+05, 9.17663500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00006602e+05, 1.00058750e+05, 1.42505797e+05, 9.99656172e+04, 9.97962188e+04, 6.21123359e+04, ],
    'CountWeightedFull'                                                              : [ 9.97620156e+04, 9.97648281e+04, 9.97597344e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97620156e+04, 9.97620156e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.97664438e+05, 9.83393875e+05, 9.97670875e+05, 9.97667125e+05, 9.31774375e+05, 9.17493312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99887656e+04, 1.00037141e+05, 1.42475391e+05, 9.99451406e+04, 9.97742266e+04, 6.21003984e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52112031e+04, 9.51994375e+04, 9.52228125e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52112031e+04, 9.42106875e+04, 9.62102344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.52112031e+04, 9.52112031e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.52112000e+05, 9.38522875e+05, 9.52143125e+05, 9.52116938e+05, 8.89447188e+05, 8.75799250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.55699062e+04, 9.54105938e+04, 1.35934484e+05, 9.51471406e+04, 9.52672188e+04, 5.92699453e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.51914844e+04, 9.51792188e+04, 9.52035625e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.51914844e+04, 9.41913125e+04, 9.61902344e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.51914844e+04, 9.51914844e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.51939250e+05, 9.38328062e+05, 9.51945125e+05, 9.51941500e+05, 8.89262750e+05, 8.75641938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.55533594e+04, 9.53903906e+04, 1.35906094e+05, 9.51281641e+04, 9.52467031e+04, 5.92588789e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     540690754), # 540.69MB, avg file size 540.69MB
  ("fsize_db",                        6944166133), # 6.94GB, avg file size 771.57MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_4t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 391000, ],
    'CountWeighted'                                                                  : [ 3.90962844e+05, 3.90985875e+05, 3.90868188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.95791062e+05, 3.90955656e+05, 3.83420562e+05, 3.95791062e+05, 3.90955656e+05, 3.83420562e+05, 3.95791062e+05, 3.90955656e+05, 3.83420562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95791062e+05, 3.83420562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.82617938e+05, 3.82603312e+05, 3.82577281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.82617938e+05, 3.80477281e+05, 3.84679375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.87281688e+05, 3.82611812e+05, 3.75274312e+05, 3.87281688e+05, 3.82611812e+05, 3.75274312e+05, 3.87281688e+05, 3.82611812e+05, 3.75274312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.87281688e+05, 3.75274312e+05, ],
  }),
  ("nof_tree_events",                 391000),
  ("nof_db_events",                   391000),
  ("fsize_local",                     1413132508), # 1.41GB, avg file size 1.41GB
  ("fsize_db",                        18879671024), # 18.88GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85979688e+05, 3.85964312e+05, 3.86005156e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.92027375e+05, 3.85979688e+05, 3.77493000e+05, 3.92027375e+05, 3.85979688e+05, 3.77493000e+05, 3.92027375e+05, 3.85979688e+05, 3.77493000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.92027844e+05, 3.77492562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.77354938e+05, 3.77331312e+05, 3.77384375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.77354938e+05, 3.75171625e+05, 3.79469188e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.83207094e+05, 3.77354938e+05, 3.69099625e+05, 3.83207094e+05, 3.77354938e+05, 3.69099625e+05, 3.83207094e+05, 3.77354938e+05, 3.69099625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.83207562e+05, 3.69099156e+05, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1416664492), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        18925798715), # 18.93GB, avg file size 727.92MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 380000, ],
    'CountWeighted'                                                                  : [ 3.80032312e+05, 3.79991875e+05, 3.79941312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.87117250e+05, 3.80029219e+05, 3.70624625e+05, 3.87117250e+05, 3.80029219e+05, 3.70624625e+05, 3.87117250e+05, 3.80029219e+05, 3.70624625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87117250e+05, 3.70624625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.71255500e+05, 3.71228688e+05, 3.71192062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.71255500e+05, 3.69052250e+05, 3.73386250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.78137344e+05, 3.71252312e+05, 3.62136312e+05, 3.78137344e+05, 3.71252312e+05, 3.62136312e+05, 3.78137344e+05, 3.71252312e+05, 3.62136312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.78137344e+05, 3.62136312e+05, ],
  }),
  ("nof_tree_events",                 380000),
  ("nof_db_events",                   380000),
  ("fsize_local",                     1415233363), # 1.42GB, avg file size 1.42GB
  ("fsize_db",                        18931125504), # 18.93GB, avg file size 728.12MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    30),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99976000e+05, 4.00033406e+05, 3.99957875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08711906e+05, 3.99973000e+05, 3.89181219e+05, 4.08711906e+05, 3.99973000e+05, 3.89181219e+05, 4.08711906e+05, 3.99973000e+05, 3.89181219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.08711969e+05, 3.89181125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.90461938e+05, 3.90496875e+05, 3.90445125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.90461938e+05, 3.88090969e+05, 3.92764562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98921719e+05, 3.90458500e+05, 3.79977844e+05, 3.98921719e+05, 3.90458500e+05, 3.79977844e+05, 3.98921719e+05, 3.90458500e+05, 3.79977844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98921812e+05, 3.79977719e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1509110216), # 1.51GB, avg file size 1.51GB
  ("fsize_db",                        19706361148), # 19.71GB, avg file size 656.88MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00043125e+05, 4.00001656e+05, 3.99972938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.11015062e+05, 4.00043125e+05, 3.87374500e+05, 4.11015062e+05, 4.00043125e+05, 3.87374500e+05, 4.11015062e+05, 4.00043125e+05, 3.87374500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.11016094e+05, 3.87373469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.89929875e+05, 3.89874906e+05, 3.89912438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.89929875e+05, 3.87440875e+05, 3.92349188e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.00569844e+05, 3.89929875e+05, 3.77663438e+05, 4.00569844e+05, 3.89929875e+05, 3.77663438e+05, 4.00569844e+05, 3.89929875e+05, 3.77663438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.00570875e+05, 3.77662406e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1546833892), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        20098276225), # 20.10GB, avg file size 773.01MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 298000, ],
    'CountWeighted'                                                                  : [ 2.97932844e+05, 2.97997906e+05, 2.97964906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.07751938e+05, 2.97932844e+05, 2.87342375e+05, 3.07751938e+05, 2.97932844e+05, 2.87342375e+05, 3.07751938e+05, 2.97932844e+05, 2.87342375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.07751938e+05, 2.87342375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90134812e+05, 2.90169125e+05, 2.90157781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90134812e+05, 2.88238688e+05, 2.91996562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.99628375e+05, 2.90134812e+05, 2.79863344e+05, 2.99628375e+05, 2.90134812e+05, 2.79863344e+05, 2.99628375e+05, 2.90134812e+05, 2.79863344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.99628375e+05, 2.79863344e+05, ],
  }),
  ("nof_tree_events",                 298000),
  ("nof_db_events",                   298000),
  ("fsize_local",                     1179252726), # 1.18GB, avg file size 1.18GB
  ("fsize_db",                        15176832017), # 15.18GB, avg file size 758.84MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83888188e+05, 3.83949375e+05, 3.84001312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99338875e+05, 3.83888188e+05, 3.68141875e+05, 3.99338875e+05, 3.83888188e+05, 3.68141875e+05, 3.99338875e+05, 3.83888188e+05, 3.68141875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99338875e+05, 3.68141844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73339656e+05, 3.73356938e+05, 3.73423969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73339656e+05, 3.70801906e+05, 3.75828125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.88250031e+05, 3.73339656e+05, 3.58073906e+05, 3.88250031e+05, 3.73339656e+05, 3.58073906e+05, 3.88250031e+05, 3.73339656e+05, 3.58073906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.88250031e+05, 3.58073844e+05, ],
  }),
  ("nof_tree_events",                 384000),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1564940896), # 1.56GB, avg file size 1.56GB
  ("fsize_db",                        19349982170), # 19.35GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 3.00007938e+05, 2.99973219e+05, 2.99999406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15125375e+05, 3.00007938e+05, 2.85252188e+05, 3.15125375e+05, 3.00007938e+05, 2.85252188e+05, 3.15125375e+05, 3.00007938e+05, 2.85252188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15125375e+05, 2.85252188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91273688e+05, 2.91249000e+05, 2.91265625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91273688e+05, 2.89207594e+05, 2.93306312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.05892906e+05, 2.91273688e+05, 2.77018156e+05, 3.05892906e+05, 2.91273688e+05, 2.77018156e+05, 3.05892906e+05, 2.91273688e+05, 2.77018156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.05892906e+05, 2.77018156e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1278939126), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        15427844934), # 15.43GB, avg file size 857.10MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 280000, ],
    'CountWeighted'                                                                  : [ 2.79984938e+05, 2.80001312e+05, 2.79960344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.96615812e+05, 2.79984938e+05, 2.64337938e+05, 2.96615812e+05, 2.79984938e+05, 2.64337938e+05, 2.96615812e+05, 2.79984938e+05, 2.64337938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.96617344e+05, 2.64336375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71534688e+05, 2.71532688e+05, 2.71524812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71534688e+05, 2.69562219e+05, 2.73478000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.87593438e+05, 2.71534688e+05, 2.56420531e+05, 2.87593438e+05, 2.71534688e+05, 2.56420531e+05, 2.87593438e+05, 2.71534688e+05, 2.56420531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87594938e+05, 2.56419062e+05, ],
  }),
  ("nof_tree_events",                 280000),
  ("nof_db_events",                   280000),
  ("fsize_local",                     1240222140), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        14667839164), # 14.67GB, avg file size 637.73MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 284000, ],
    'CountWeighted'                                                                  : [ 2.83953625e+05, 2.84019562e+05, 2.83902875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.03009719e+05, 2.83953625e+05, 2.66463125e+05, 3.03009719e+05, 2.83953625e+05, 2.66463125e+05, 3.03009719e+05, 2.83953625e+05, 2.66463125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.03009719e+05, 2.66463125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.75433000e+05, 2.75464875e+05, 2.75403969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.75433000e+05, 2.73447375e+05, 2.77393562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.93835656e+05, 2.75433000e+05, 2.58513000e+05, 2.93835656e+05, 2.75433000e+05, 2.58513000e+05, 2.93835656e+05, 2.75433000e+05, 2.58513000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.93835656e+05, 2.58513000e+05, ],
  }),
  ("nof_tree_events",                 284000),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1298058672), # 1.30GB, avg file size 1.30GB
  ("fsize_db",                        15248320207), # 15.25GB, avg file size 693.11MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99979047e+05, 1.99978828e+05, 1.99969109e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14731594e+05, 1.99978719e+05, 1.86604188e+05, 2.14731594e+05, 1.99978719e+05, 1.86604188e+05, 2.14731594e+05, 1.99978719e+05, 1.86604188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14731594e+05, 1.86604188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93924625e+05, 1.93923156e+05, 1.93925719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93924625e+05, 1.92525125e+05, 1.95308031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08183812e+05, 1.93923656e+05, 1.80992781e+05, 2.08183812e+05, 1.93923656e+05, 1.80992781e+05, 2.08183812e+05, 1.93923656e+05, 1.80992781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08183812e+05, 1.80992781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     940503856), # 940.50MB, avg file size 940.50MB
  ("fsize_db",                        10729026481), # 10.73GB, avg file size 536.45MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 198000, ],
    'CountWeighted'                                                                  : [ 1.97981609e+05, 1.97967172e+05, 1.97985359e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13791688e+05, 1.97981609e+05, 1.83808391e+05, 2.13791688e+05, 1.97981609e+05, 1.83808391e+05, 2.13791688e+05, 1.97981609e+05, 1.83808391e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13792000e+05, 1.83808094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.91926359e+05, 1.91909062e+05, 1.91940438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.91926359e+05, 1.90530609e+05, 1.93304031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07208406e+05, 1.91926359e+05, 1.78222672e+05, 2.07208406e+05, 1.91926359e+05, 1.78222672e+05, 2.07208406e+05, 1.91926359e+05, 1.78222672e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07208516e+05, 1.78222547e+05, ],
  }),
  ("nof_tree_events",                 198000),
  ("nof_db_events",                   198000),
  ("fsize_local",                     953765545), # 953.77MB, avg file size 953.77MB
  ("fsize_db",                        10881260447), # 10.88GB, avg file size 604.51MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99964719e+05, 1.99944688e+05, 1.99943500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17056844e+05, 1.99961594e+05, 1.84835844e+05, 2.17056844e+05, 1.99961594e+05, 1.84835844e+05, 2.17056844e+05, 1.99961594e+05, 1.84835844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17056844e+05, 1.84835844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93894078e+05, 1.93868078e+05, 1.93892562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93894078e+05, 1.92494125e+05, 1.95275938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10416156e+05, 1.93891484e+05, 1.79252781e+05, 2.10416156e+05, 1.93891484e+05, 1.79252781e+05, 2.10416156e+05, 1.93891484e+05, 1.79252781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10416156e+05, 1.79252781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     985593348), # 985.59MB, avg file size 985.59MB
  ("fsize_db",                        10995288880), # 11.00GB, avg file size 610.85MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 189000, ],
    'CountWeighted'                                                                  : [ 1.88975141e+05, 1.88986000e+05, 1.88967688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.06028094e+05, 1.88975141e+05, 1.73935875e+05, 2.06028094e+05, 1.88975141e+05, 1.73935875e+05, 2.06028094e+05, 1.88975141e+05, 1.73935875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.06028094e+05, 1.73935875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.83333484e+05, 1.83320125e+05, 1.83348750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.83333484e+05, 1.82034422e+05, 1.84612875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.99843250e+05, 1.83333484e+05, 1.68773859e+05, 1.99843250e+05, 1.83333484e+05, 1.68773859e+05, 1.99843250e+05, 1.83333484e+05, 1.68773859e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.99843250e+05, 1.68773859e+05, ],
  }),
  ("nof_tree_events",                 189000),
  ("nof_db_events",                   189000),
  ("fsize_local",                     951669407), # 951.67MB, avg file size 951.67MB
  ("fsize_db",                        10562893577), # 10.56GB, avg file size 528.14MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    26),
  ("nof_events",                      {
    'Count'                                                                          : [ 196000, ],
    'CountWeighted'                                                                  : [ 1.95958031e+05, 1.95984500e+05, 1.96001188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14575156e+05, 1.95958031e+05, 1.79692328e+05, 2.14575156e+05, 1.95958031e+05, 1.79692328e+05, 2.14575156e+05, 1.95958031e+05, 1.79692328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14575172e+05, 1.79692328e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90102266e+05, 1.90107516e+05, 1.90150438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90102266e+05, 1.88758375e+05, 1.91429156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08116938e+05, 1.90102266e+05, 1.74353406e+05, 2.08116938e+05, 1.90102266e+05, 1.74353406e+05, 2.08116938e+05, 1.90102266e+05, 1.74353406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08116938e+05, 1.74353406e+05, ],
  }),
  ("nof_tree_events",                 196000),
  ("nof_db_events",                   196000),
  ("fsize_local",                     1004924679), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11128480225), # 11.13GB, avg file size 428.02MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99965719e+05, 1.99928156e+05, 1.99990375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19780531e+05, 1.99965719e+05, 1.82751938e+05, 2.19780531e+05, 1.99965719e+05, 1.82751938e+05, 2.19780531e+05, 1.99965719e+05, 1.82751938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19780531e+05, 1.82751938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94027812e+05, 1.93987719e+05, 1.94056266e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94027812e+05, 1.92666906e+05, 1.95372234e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.13219281e+05, 1.94027812e+05, 1.77350969e+05, 2.13219281e+05, 1.94027812e+05, 1.77350969e+05, 2.13219281e+05, 1.94027812e+05, 1.77350969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.13219281e+05, 1.77350969e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1039059094), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11297900227), # 11.30GB, avg file size 470.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 194000, ],
    'CountWeighted'                                                                  : [ 1.93918844e+05, 1.93958672e+05, 1.93975812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.93918844e+05, 1.93918844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.88167094e+05, 1.88178250e+05, 1.88226422e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.88167094e+05, 1.86847312e+05, 1.89469266e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.88167094e+05, 1.88167094e+05, ],
  }),
  ("nof_tree_events",                 194000),
  ("nof_db_events",                   194000),
  ("fsize_local",                     1027807435), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11268378526), # 11.27GB, avg file size 704.27MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99836953e+04, 9.99772734e+04, 1.00000344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10544883e+05, 9.99836953e+04, 9.09752734e+04, 1.10544883e+05, 9.99836953e+04, 9.09752734e+04, 1.10544883e+05, 9.99836953e+04, 9.09752734e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10544883e+05, 9.09752734e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71493984e+04, 9.71368906e+04, 9.71694922e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71493984e+04, 9.64993984e+04, 9.77905547e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07391797e+05, 9.71493984e+04, 8.84047344e+04, 1.07391797e+05, 9.71493984e+04, 8.84047344e+04, 1.07391797e+05, 9.71493984e+04, 8.84047344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07391797e+05, 8.84047344e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     534192407), # 534.19MB, avg file size 534.19MB
  ("fsize_db",                        5743750248), # 5.74GB, avg file size 441.83MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99550312e+04, 9.99787344e+04, 9.99576953e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11321031e+05, 9.99550312e+04, 9.03187578e+04, 1.11321031e+05, 9.99550312e+04, 9.03187578e+04, 1.11321031e+05, 9.99550312e+04, 9.03187578e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11321031e+05, 9.03187578e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70344531e+04, 9.70459062e+04, 9.70435703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70344531e+04, 9.63676641e+04, 9.76921953e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08055273e+05, 9.70344531e+04, 8.76862812e+04, 1.08055273e+05, 9.70344531e+04, 8.76862812e+04, 1.08055273e+05, 9.70344531e+04, 8.76862812e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08055273e+05, 8.76862812e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     543620853), # 543.62MB, avg file size 543.62MB
  ("fsize_db",                        5923175401), # 5.92GB, avg file size 311.75MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00012594e+05, 1.00004867e+05, 1.00001938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.00012594e+05, 1.00012594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99949438e+05, 9.99949438e+05, 9.99949438e+05, 9.99949438e+05, 9.99949438e+05, 9.99949438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00025094e+05, 1.00075438e+05, 1.40684594e+05, 9.99562344e+04, 9.97229062e+04, 6.35965352e+04, ],
    'CountWeightedFull'                                                              : [ 1.00000891e+05, 9.99932031e+04, 9.99902500e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.00000891e+05, 1.00000891e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99834625e+05, 9.99834625e+05, 9.99834625e+05, 9.99834625e+05, 9.99834625e+05, 9.99834625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00014227e+05, 1.00063992e+05, 1.40668281e+05, 9.99437500e+04, 9.97115000e+04, 6.35893125e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70906875e+04, 9.70802969e+04, 9.70838906e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70906875e+04, 9.64257656e+04, 9.77463672e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70906875e+04, 9.70906875e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70781812e+05, 9.70781812e+05, 9.70781812e+05, 9.70781812e+05, 9.70781812e+05, 9.70781812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72588203e+04, 9.71218750e+04, 1.36547031e+05, 9.68463594e+04, 9.68786250e+04, 6.17803672e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70798906e+04, 9.70695156e+04, 9.70730312e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70798906e+04, 9.64150781e+04, 9.77353281e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70798906e+04, 9.70798906e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70674812e+05, 9.70674812e+05, 9.70674812e+05, 9.70674812e+05, 9.70674812e+05, 9.70674812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72487266e+04, 9.71112578e+04, 1.36531844e+05, 9.68347500e+04, 9.68679219e+04, 6.17736172e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     524886697), # 524.89MB, avg file size 524.89MB
  ("fsize_db",                        5934590716), # 5.93GB, avg file size 741.82MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_4t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_4t_PSWeights"),
  ("nof_files",                       2),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99908711e+04, 9.99962451e+04, 9.99942744e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99908711e+04, 9.99908711e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99947766e+05, 9.99947766e+05, 9.99947766e+05, 9.99947766e+05, 9.99947766e+05, 9.99947766e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00023388e+05, 1.00062550e+05, 1.41112087e+05, 9.99654438e+04, 9.96111582e+04, 6.31628320e+04, ],
    'CountWeightedFull'                                                              : [ 9.99788184e+04, 9.99841973e+04, 9.99821938e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99788184e+04, 9.99788184e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99827344e+05, 9.99827344e+05, 9.99827344e+05, 9.99827344e+05, 9.99827344e+05, 9.99827344e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00012199e+05, 1.00050561e+05, 1.41094682e+05, 9.99522471e+04, 9.95990703e+04, 6.31554248e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70882559e+04, 9.70795308e+04, 9.71045449e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70882559e+04, 9.64281221e+04, 9.77400005e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70882559e+04, 9.70882559e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70912609e+05, 9.70912609e+05, 9.70912609e+05, 9.70912609e+05, 9.70912609e+05, 9.70912609e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72833428e+04, 9.71327954e+04, 1.36943510e+05, 9.68566519e+04, 9.67408931e+04, 6.13671260e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70769717e+04, 9.70682397e+04, 9.70932109e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70769717e+04, 9.64169639e+04, 9.77285103e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70769717e+04, 9.70769717e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70799609e+05, 9.70799609e+05, 9.70799609e+05, 9.70799609e+05, 9.70799609e+05, 9.70799609e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72728398e+04, 9.71215674e+04, 1.36927215e+05, 9.68443242e+04, 9.67295249e+04, 6.13601646e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     537862980), # 537.86MB, avg file size 268.93MB
  ("fsize_db",                        6175038620), # 6.18GB, avg file size 771.88MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_4t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99973828e+04, 1.00005062e+05, 9.99935000e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99973828e+04, 9.99973828e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99988250e+05, 9.99988250e+05, 9.99988250e+05, 9.99988250e+05, 9.99988250e+05, 9.99988250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00052281e+05, 9.99014062e+04, 1.41678781e+05, 9.99381406e+04, 1.00016453e+05, 6.28873242e+04, ],
    'CountWeightedFull'                                                              : [ 9.99821641e+04, 9.99898750e+04, 9.99783672e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99821641e+04, 9.99821641e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99835750e+05, 9.99835750e+05, 9.99835750e+05, 9.99835750e+05, 9.99835750e+05, 9.99835750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00039477e+05, 9.98867734e+04, 1.41654234e+05, 9.99234531e+04, 9.99981875e+04, 6.28787500e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70820547e+04, 9.70875547e+04, 9.70826562e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70820547e+04, 9.64202266e+04, 9.77345781e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70820547e+04, 9.70820547e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70832062e+05, 9.70832062e+05, 9.70832062e+05, 9.70832062e+05, 9.70832062e+05, 9.70832062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73063750e+04, 9.69390469e+04, 1.37506906e+05, 9.68095469e+04, 9.71714531e+04, 6.10953242e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70678672e+04, 9.70733828e+04, 9.70685469e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70678672e+04, 9.64062812e+04, 9.77202031e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70678672e+04, 9.70678672e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70689938e+05, 9.70689938e+05, 9.70689938e+05, 9.70689938e+05, 9.70689938e+05, 9.70689938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72943984e+04, 9.69254062e+04, 1.37484141e+05, 9.67957656e+04, 9.71545469e+04, 6.10872969e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     525913462), # 525.91MB, avg file size 525.91MB
  ("fsize_db",                        6057381888), # 6.06GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_4t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99977031e+04, 9.99840469e+04, 9.99870312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99977031e+04, 9.99977031e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99828188e+05, 9.99828188e+05, 9.99828188e+05, 9.99828188e+05, 9.99828188e+05, 9.99828188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00000109e+05, 9.99958984e+04, 1.41765000e+05, 9.99726562e+04, 9.96902969e+04, 6.26032695e+04, ],
    'CountWeightedFull'                                                              : [ 9.99809688e+04, 9.99678281e+04, 9.99702969e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99809688e+04, 9.99809688e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99663500e+05, 9.99663500e+05, 9.99663500e+05, 9.99663500e+05, 9.99663500e+05, 9.99663500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99860312e+04, 9.99798906e+04, 1.41741625e+05, 9.99565625e+04, 9.96732344e+04, 6.25939375e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70729844e+04, 9.70597656e+04, 9.70692500e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70729844e+04, 9.64105000e+04, 9.77260469e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70729844e+04, 9.70729844e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70640812e+05, 9.70640812e+05, 9.70640812e+05, 9.70640812e+05, 9.70640812e+05, 9.70640812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72537031e+04, 9.70108125e+04, 1.37578234e+05, 9.68335000e+04, 9.68562656e+04, 6.08163359e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70582109e+04, 9.70452656e+04, 9.70545156e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70582109e+04, 9.63961562e+04, 9.77108906e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70582109e+04, 9.70582109e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70494375e+05, 9.70494375e+05, 9.70494375e+05, 9.70494375e+05, 9.70494375e+05, 9.70494375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72405469e+04, 9.69964844e+04, 1.37557328e+05, 9.68185000e+04, 9.68413438e+04, 6.08076016e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     518142350), # 518.14MB, avg file size 518.14MB
  ("fsize_db",                        6084635698), # 6.08GB, avg file size 760.58MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_4t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 1.00001086e+05, 9.99942969e+04, 9.99979062e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.00001086e+05, 1.00001086e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99949500e+05, 9.99949500e+05, 9.99949500e+05, 9.99949500e+05, 9.99949500e+05, 9.99949500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00039305e+05, 1.00117328e+05, 1.41978141e+05, 9.99472891e+04, 9.95050781e+04, 6.23942773e+04, ],
    'CountWeightedFull'                                                              : [ 9.99860312e+04, 9.99793516e+04, 9.99829375e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99860312e+04, 9.99860312e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99799500e+05, 9.99799500e+05, 9.99799500e+05, 9.99799500e+05, 9.99799500e+05, 9.99799500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00025188e+05, 1.00102758e+05, 1.41956438e+05, 9.99311953e+04, 9.94894375e+04, 6.23849180e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70369375e+04, 9.70327734e+04, 9.70353594e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70369375e+04, 9.63653047e+04, 9.76988906e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70369375e+04, 9.70369375e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70330000e+05, 9.70330000e+05, 9.70330000e+05, 9.70330000e+05, 9.70330000e+05, 9.70330000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72508594e+04, 9.71215781e+04, 1.37753453e+05, 9.67670156e+04, 9.66200938e+04, 6.05770039e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70227812e+04, 9.70186484e+04, 9.70212422e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70227812e+04, 9.63513125e+04, 9.76845078e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70227812e+04, 9.70227812e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70188875e+05, 9.70188875e+05, 9.70188875e+05, 9.70188875e+05, 9.70188875e+05, 9.70188875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72375156e+04, 9.71079531e+04, 1.37733062e+05, 9.67519141e+04, 9.66053984e+04, 6.05682109e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     514009801), # 514.01MB, avg file size 514.01MB
  ("fsize_db",                        6186084238), # 6.19GB, avg file size 515.51MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_4t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 98000, ],
    'CountWeighted'                                                                  : [ 9.79951094e+04, 9.79994531e+04, 9.79929531e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.79951094e+04, 9.79951094e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.80012875e+05, 9.80012875e+05, 9.80012875e+05, 9.80012875e+05, 9.80012875e+05, 9.80012875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.80416406e+04, 9.78910859e+04, 1.39559531e+05, 9.79289922e+04, 9.79835391e+04, 6.09516719e+04, ],
    'CountWeightedFull'                                                              : [ 9.79773984e+04, 9.79816406e+04, 9.79753750e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.79773984e+04, 9.79773984e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.79834250e+05, 9.79834250e+05, 9.79834250e+05, 9.79834250e+05, 9.79834250e+05, 9.79834250e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.80258828e+04, 9.78734688e+04, 1.39533797e+05, 9.79107109e+04, 9.79656484e+04, 6.09412539e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.50884922e+04, 9.50850547e+04, 9.50913594e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.50884922e+04, 9.44254688e+04, 9.57400625e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.50884922e+04, 9.50884922e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.50921438e+05, 9.50921438e+05, 9.50921438e+05, 9.50921438e+05, 9.50921438e+05, 9.50921438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.53068281e+04, 9.49561875e+04, 1.35382781e+05, 9.48053438e+04, 9.51191719e+04, 5.91677344e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.50717891e+04, 9.50683438e+04, 9.50747812e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.50717891e+04, 9.44090156e+04, 9.57231797e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.50717891e+04, 9.50717891e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.50753688e+05, 9.50753688e+05, 9.50753688e+05, 9.50753688e+05, 9.50753688e+05, 9.50753688e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.52920391e+04, 9.49396641e+04, 1.35358688e+05, 9.47882500e+04, 9.51022891e+04, 5.91579141e+04, ],
  }),
  ("nof_tree_events",                 98000),
  ("nof_db_events",                   98000),
  ("fsize_local",                     501257945), # 501.26MB, avg file size 501.26MB
  ("fsize_db",                        6828488277), # 6.83GB, avg file size 758.72MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_4t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_tttt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_4t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99860156e+04, 9.99977891e+04, 9.99959531e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99860156e+04, 9.99860156e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99982500e+05, 9.99982500e+05, 9.99982500e+05, 9.99982500e+05, 9.99982500e+05, 9.99982500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99930469e+04, 9.97321094e+04, 1.42863047e+05, 9.99699609e+04, 1.00520023e+05, 6.21187109e+04, ],
    'CountWeightedFull'                                                              : [ 9.99660781e+04, 9.99777578e+04, 9.99759375e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99660781e+04, 9.99660781e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99781500e+05, 9.99781500e+05, 9.99781500e+05, 9.99781500e+05, 9.99781500e+05, 9.99781500e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99760234e+04, 9.97121406e+04, 1.42834734e+05, 9.99505938e+04, 1.00499883e+05, 6.21076406e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69770234e+04, 9.69823438e+04, 9.69872422e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69770234e+04, 9.62902656e+04, 9.76528359e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.69770234e+04, 9.69770234e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.69859438e+05, 9.69859438e+05, 9.69859438e+05, 9.69859438e+05, 9.69859438e+05, 9.69859438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.71591562e+04, 9.66974844e+04, 1.38529203e+05, 9.67392188e+04, 9.75369219e+04, 6.02770547e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69581328e+04, 9.69634297e+04, 9.69682812e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69581328e+04, 9.62716016e+04, 9.76336875e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.69581328e+04, 9.69581328e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.69669312e+05, 9.69669312e+05, 9.69669312e+05, 9.69669312e+05, 9.69669312e+05, 9.69669312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.71429062e+04, 9.66786406e+04, 1.38502328e+05, 9.67207578e+04, 9.75178828e+04, 6.02664609e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     512098846), # 512.10MB, avg file size 512.10MB
  ("fsize_db",                        6994832463), # 6.99GB, avg file size 582.90MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_4t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99912000e+05, 3.99995125e+05, 4.00008938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99912000e+05, 3.99912000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92663000e+05, 3.92701000e+05, 3.92743938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92663000e+05, 3.90757625e+05, 3.94479562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92663000e+05, 3.92663000e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1451360323), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        20344351713), # 20.34GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 3.99926344e+05, 3.99979688e+05, 4.00061688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06243688e+05, 3.99925500e+05, 3.91187094e+05, 4.06243688e+05, 3.99925500e+05, 3.91187094e+05, 4.06243688e+05, 3.99925500e+05, 3.91187094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06243688e+05, 3.91187094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92304844e+05, 3.92323250e+05, 3.92408219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92304844e+05, 3.90314562e+05, 3.94197062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98436688e+05, 3.92302938e+05, 3.83746125e+05, 3.98436688e+05, 3.92302938e+05, 3.83746125e+05, 3.98436688e+05, 3.92302938e+05, 3.83746125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98436688e+05, 3.83746125e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1463903886), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        19527920598), # 19.53GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 4.00039531e+05, 3.99917531e+05, 3.99979219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07500875e+05, 4.00039531e+05, 3.90165938e+05, 4.07500875e+05, 4.00039531e+05, 3.90165938e+05, 4.07500875e+05, 4.00039531e+05, 3.90165938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07500875e+05, 3.90165938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92092938e+05, 3.91998062e+05, 3.92056219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92092938e+05, 3.90041312e+05, 3.94043969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99373406e+05, 3.92092938e+05, 3.82468688e+05, 3.99373406e+05, 3.92092938e+05, 3.82468688e+05, 3.99373406e+05, 3.92092938e+05, 3.82468688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99373406e+05, 3.82468688e+05, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1483238971), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        19473148919), # 19.47GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    27),
  ("nof_events",                      {
    'Count'                                                                          : [ 379996, ],
    'CountWeighted'                                                                  : [ 3.80026812e+05, 3.79978250e+05, 3.80015938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.80026812e+05, 3.80026812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.72179250e+05, 3.72139312e+05, 3.72174375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.72179250e+05, 3.70166906e+05, 3.74100531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72179250e+05, 3.72179250e+05, ],
  }),
  ("nof_tree_events",                 379996),
  ("nof_db_events",                   379996),
  ("fsize_local",                     1443317478), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        19590423166), # 19.59GB, avg file size 725.57MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 299994, ],
    'CountWeighted'                                                                  : [ 2.99947469e+05, 2.99958469e+05, 2.99956000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08253906e+05, 2.99947062e+05, 2.90539812e+05, 3.08253906e+05, 2.99947062e+05, 2.90539812e+05, 3.08253906e+05, 2.99947062e+05, 2.90539812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08253906e+05, 2.90539812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93250594e+05, 2.93245312e+05, 2.93265250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93250594e+05, 2.91556188e+05, 2.94881250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01313750e+05, 2.93249312e+05, 2.84074375e+05, 3.01313750e+05, 2.93249312e+05, 2.84074375e+05, 3.01313750e+05, 2.93249312e+05, 2.84074375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01313750e+05, 2.84074375e+05, ],
  }),
  ("nof_tree_events",                 299994),
  ("nof_db_events",                   299994),
  ("fsize_local",                     1164639721), # 1.16GB, avg file size 1.16GB
  ("fsize_db",                        14916149163), # 14.92GB, avg file size 828.67MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99972750e+05, 2.99989969e+05, 3.00038531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09807000e+05, 2.99972625e+05, 2.89291938e+05, 3.09807000e+05, 2.99972625e+05, 2.89291938e+05, 3.09807000e+05, 2.99972625e+05, 2.89291938e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09807000e+05, 2.89291938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92946594e+05, 2.92944781e+05, 2.93008688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92946594e+05, 2.91185625e+05, 2.94643500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02505469e+05, 2.92945250e+05, 2.82553375e+05, 3.02505469e+05, 2.92945250e+05, 2.82553375e+05, 3.02505469e+05, 2.92945250e+05, 2.82553375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02505469e+05, 2.82553375e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1192106413), # 1.19GB, avg file size 1.19GB
  ("fsize_db",                        14997791200), # 15.00GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 299990, ],
    'CountWeighted'                                                                  : [ 3.00014938e+05, 2.99997125e+05, 3.00031344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11942438e+05, 3.00013188e+05, 2.87615531e+05, 3.11942438e+05, 3.00013188e+05, 2.87615531e+05, 3.11942438e+05, 3.00013188e+05, 2.87615531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11942438e+05, 2.87615531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92395750e+05, 2.92362625e+05, 2.92428344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92395750e+05, 2.90515312e+05, 2.94218844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03991562e+05, 2.92392938e+05, 2.80368094e+05, 3.03991562e+05, 2.92392938e+05, 2.80368094e+05, 3.03991562e+05, 2.92392938e+05, 2.80368094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03991562e+05, 2.80368094e+05, ],
  }),
  ("nof_tree_events",                 299990),
  ("nof_db_events",                   299990),
  ("fsize_local",                     1236136314), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        15235183188), # 15.24GB, avg file size 952.20MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 286992, ],
    'CountWeighted'                                                                  : [ 2.86998156e+05, 2.87037562e+05, 2.86973531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.01485281e+05, 2.86998156e+05, 2.72878688e+05, 3.01485281e+05, 2.86998156e+05, 2.72878688e+05, 3.01485281e+05, 2.86998156e+05, 2.72878688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.01485281e+05, 2.72878688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.78904375e+05, 2.78920094e+05, 2.78890250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.78904375e+05, 2.76940250e+05, 2.80814938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.92930938e+05, 2.78904375e+05, 2.65235906e+05, 2.92930938e+05, 2.78904375e+05, 2.65235906e+05, 2.92930938e+05, 2.78904375e+05, 2.65235906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.92930938e+05, 2.65235906e+05, ],
  }),
  ("nof_tree_events",                 286992),
  ("nof_db_events",                   286992),
  ("fsize_local",                     1242967949), # 1.24GB, avg file size 1.24GB
  ("fsize_db",                        14884438376), # 14.88GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 291993, ],
    'CountWeighted'                                                                  : [ 2.91964250e+05, 2.91937750e+05, 2.91926844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09261969e+05, 2.91964250e+05, 2.75698125e+05, 3.09261969e+05, 2.91964250e+05, 2.75698125e+05, 3.09261969e+05, 2.91964250e+05, 2.75698125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09261969e+05, 2.75698125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.83177281e+05, 2.83150188e+05, 2.83158156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.83177281e+05, 2.81068875e+05, 2.85234469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.99898094e+05, 2.83177281e+05, 2.67443781e+05, 2.99898094e+05, 2.83177281e+05, 2.67443781e+05, 2.99898094e+05, 2.83177281e+05, 2.67443781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.99898094e+05, 2.67443781e+05, ],
  }),
  ("nof_tree_events",                 291993),
  ("nof_db_events",                   291993),
  ("fsize_local",                     1317996151), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        15416817462), # 15.42GB, avg file size 906.87MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 269995, ],
    'CountWeighted'                                                                  : [ 2.69945250e+05, 2.69994406e+05, 2.69968594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.88081438e+05, 2.69945250e+05, 2.53320172e+05, 2.88081438e+05, 2.69945250e+05, 2.53320172e+05, 2.88081438e+05, 2.69945250e+05, 2.53320172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.88081438e+05, 2.53320172e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.61382625e+05, 2.61398500e+05, 2.61410719e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.61382625e+05, 2.59349578e+05, 2.63379375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.78870125e+05, 2.61382625e+05, 2.45321594e+05, 2.78870125e+05, 2.61382625e+05, 2.45321594e+05, 2.78870125e+05, 2.61382625e+05, 2.45321594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.78870125e+05, 2.45321594e+05, ],
  }),
  ("nof_tree_events",                 269995),
  ("nof_db_events",                   269995),
  ("fsize_local",                     1261881216), # 1.26GB, avg file size 1.26GB
  ("fsize_db",                        14437624405), # 14.44GB, avg file size 802.09MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 299996, ],
    'CountWeighted'                                                                  : [ 2.99951094e+05, 2.99985406e+05, 2.99982531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22112562e+05, 2.99951094e+05, 2.79890469e+05, 3.22112562e+05, 2.99951094e+05, 2.79890469e+05, 3.22112562e+05, 2.99951094e+05, 2.79890469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22112562e+05, 2.79890469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.89898500e+05, 2.89907812e+05, 2.89935312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.89898500e+05, 2.87535312e+05, 2.92224406e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.11241312e+05, 2.89898500e+05, 2.70556188e+05, 3.11241312e+05, 2.89898500e+05, 2.70556188e+05, 3.11241312e+05, 2.89898500e+05, 2.70556188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.11241312e+05, 2.70556188e+05, ],
  }),
  ("nof_tree_events",                 299996),
  ("nof_db_events",                   299996),
  ("fsize_local",                     1441159698), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        16219407866), # 16.22GB, avg file size 954.08MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 195995, ],
    'CountWeighted'                                                                  : [ 1.95994000e+05, 1.95979547e+05, 1.95931578e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.11660203e+05, 1.95994000e+05, 1.81972750e+05, 2.11660203e+05, 1.95994000e+05, 1.81972750e+05, 2.11660203e+05, 1.95994000e+05, 1.81972750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.11660219e+05, 1.81972750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89210656e+05, 1.89191031e+05, 1.89175781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89210656e+05, 1.87627969e+05, 1.90768297e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.04286344e+05, 1.89210656e+05, 1.75706109e+05, 2.04286344e+05, 1.89210656e+05, 1.75706109e+05, 2.04286344e+05, 1.89210656e+05, 1.75706109e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04286344e+05, 1.75706109e+05, ],
  }),
  ("nof_tree_events",                 195995),
  ("nof_db_events",                   195995),
  ("fsize_local",                     963879095), # 963.88MB, avg file size 963.88MB
  ("fsize_db",                        10725957373), # 10.73GB, avg file size 893.83MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99976344e+05, 2.00016688e+05, 1.99985531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17031484e+05, 1.99976344e+05, 1.84826344e+05, 2.17031484e+05, 1.99976344e+05, 1.84826344e+05, 2.17031484e+05, 1.99976344e+05, 1.84826344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17031719e+05, 1.84826125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92824484e+05, 1.92849969e+05, 1.92825672e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92824484e+05, 1.91161750e+05, 1.94464984e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09228344e+05, 1.92824484e+05, 1.78251812e+05, 2.09228344e+05, 1.92824484e+05, 1.78251812e+05, 2.09228344e+05, 1.92824484e+05, 1.78251812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09228562e+05, 1.78251594e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1002437920), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11039880992), # 11.04GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 191997, ],
    'CountWeighted'                                                                  : [ 1.91969297e+05, 1.91984438e+05, 1.92001656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.09335125e+05, 1.91969297e+05, 1.76706250e+05, 2.09335125e+05, 1.91969297e+05, 1.76706250e+05, 2.09335125e+05, 1.91969297e+05, 1.76706250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.09335125e+05, 1.76706250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84877406e+05, 1.84869562e+05, 1.84914859e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84877406e+05, 1.83239000e+05, 1.86497469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.01547703e+05, 1.84877406e+05, 1.70209656e+05, 2.01547703e+05, 1.84877406e+05, 1.70209656e+05, 2.01547703e+05, 1.84877406e+05, 1.70209656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.01547703e+05, 1.70209656e+05, ],
  }),
  ("nof_tree_events",                 191997),
  ("nof_db_events",                   191997),
  ("fsize_local",                     977587834), # 977.59MB, avg file size 977.59MB
  ("fsize_db",                        10772500407), # 10.77GB, avg file size 769.46MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99936969e+05, 1.99943109e+05, 1.99980734e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99936969e+05, 1.99936969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92514000e+05, 1.92494266e+05, 1.92559656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92514000e+05, 1.90802734e+05, 1.94206000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92514000e+05, 1.92514000e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1036377761), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11660934047), # 11.66GB, avg file size 832.92MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 2.00007594e+05, 1.99962828e+05, 1.99958219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.00007594e+05, 2.00007594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92410812e+05, 1.92369406e+05, 1.92385047e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92410812e+05, 1.90669219e+05, 1.94133172e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92410812e+05, 1.92410812e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1047112930), # 1.05GB, avg file size 1.05GB
  ("fsize_db",                        11774979133), # 11.77GB, avg file size 692.65MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 191996, ],
    'CountWeighted'                                                                  : [ 1.91963000e+05, 1.91965609e+05, 1.91969500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91963000e+05, 1.91963000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84557125e+05, 1.84544500e+05, 1.84574828e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84557125e+05, 1.82858828e+05, 1.86236328e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84557125e+05, 1.84557125e+05, ],
  }),
  ("nof_tree_events",                 191996),
  ("nof_db_events",                   191996),
  ("fsize_local",                     1014986486), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11335819766), # 11.34GB, avg file size 944.65MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99948734e+05, 1.99993344e+05, 1.99967297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21318812e+05, 1.99948734e+05, 1.81636281e+05, 2.21318812e+05, 1.99948734e+05, 1.81636281e+05, 2.21318812e+05, 1.99948734e+05, 1.81636281e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21318906e+05, 1.81636219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92072969e+05, 1.92093453e+05, 1.92098969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92072969e+05, 1.90277375e+05, 1.93851703e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12549969e+05, 1.92072969e+05, 1.74511219e+05, 2.12549969e+05, 1.92072969e+05, 1.74511219e+05, 2.12549969e+05, 1.92072969e+05, 1.74511219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12550031e+05, 1.74511125e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1057921703), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11421628490), # 11.42GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99807578e+04, 9.99730234e+04, 9.99710078e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11335477e+05, 9.99807578e+04, 9.03286953e+04, 1.11335477e+05, 9.99807578e+04, 9.03286953e+04, 1.11335477e+05, 9.99807578e+04, 9.03286953e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11335477e+05, 9.03286953e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59499062e+04, 9.59401328e+04, 9.59501406e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59499062e+04, 9.50349609e+04, 9.68552734e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06826461e+05, 9.59499062e+04, 8.67055312e+04, 1.06826461e+05, 9.59499062e+04, 8.67055312e+04, 1.06826461e+05, 9.59499062e+04, 8.67055312e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06826461e+05, 8.67055312e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     536584086), # 536.58MB, avg file size 536.58MB
  ("fsize_db",                        5783738671), # 5.78GB, avg file size 826.25MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_2v2t"),
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

samples_2017["/GluGluToRadionToHHTo2V2tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99788047e+04, 9.99779062e+04, 9.99837969e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11349117e+05, 9.99788047e+04, 9.03320625e+04, 1.11349117e+05, 9.99788047e+04, 9.03320625e+04, 1.11349117e+05, 9.99788047e+04, 9.03320625e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11349203e+05, 9.03319688e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.73110312e+05, 3.72497500e+05, 5.22638375e+05, 3.73238000e+05, 3.57823156e+05, 2.26388969e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99818594e+04, 9.98829141e+04, 1.44189375e+05, 1.00016547e+05, 9.99605547e+04, 6.06670117e+04, ],
    'CountWeightedFull'                                                              : [ 9.99580469e+04, 9.99573203e+04, 9.99626094e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11325875e+05, 9.99580469e+04, 9.03134375e+04, 1.11325875e+05, 9.99580469e+04, 9.03134375e+04, 1.11325875e+05, 9.99580469e+04, 9.03134375e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11325961e+05, 9.03133438e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.73035062e+05, 3.72419875e+05, 5.22528438e+05, 3.73157281e+05, 3.57749562e+05, 2.26343062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99616953e+04, 9.98620469e+04, 1.44159344e+05, 9.99948906e+04, 9.99401406e+04, 6.06547344e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59342031e+04, 9.59312656e+04, 9.59456094e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59342031e+04, 9.50158047e+04, 9.68439219e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06820438e+05, 9.59342031e+04, 8.66936250e+04, 1.06820438e+05, 9.59342031e+04, 8.66936250e+04, 1.06820438e+05, 9.59342031e+04, 8.66936250e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06820469e+05, 8.66935938e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.58563000e+05, 3.57365500e+05, 5.01442000e+05, 3.57442469e+05, 3.43504594e+05, 2.17295344e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.60798438e+04, 9.58207422e+04, 1.38330656e+05, 9.57795156e+04, 9.59492422e+04, 5.82272109e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.59144375e+04, 9.59116094e+04, 9.59256562e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.59144375e+04, 9.49962656e+04, 9.68239609e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.06798406e+05, 9.59144375e+04, 8.66758281e+04, 1.06798406e+05, 9.59144375e+04, 8.66758281e+04, 1.06798406e+05, 9.59144375e+04, 8.66758281e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.06798438e+05, 8.66757969e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.58491250e+05, 3.57291562e+05, 5.01337312e+05, 3.57365875e+05, 3.43434781e+05, 2.17251625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.60605781e+04, 9.58009062e+04, 1.38301969e+05, 9.57589688e+04, 9.59298594e+04, 5.82155547e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     538616608), # 538.62MB, avg file size 538.62MB
  ("fsize_db",                        5836670617), # 5.84GB, avg file size 648.52MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo2V2tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    4),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99753516e+04, 9.99850938e+04, 9.99677188e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99753516e+04, 9.99753516e+04, ],
    'CountWeightedPSWeight'                                                          : [ 4.68448125e+05, 4.67833125e+05, 6.43086625e+05, 4.68096062e+05, 4.33593656e+05, 2.82102188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00026211e+05, 1.00251125e+05, 1.44488125e+05, 9.99498828e+04, 9.94012578e+04, 6.02374180e+04, ],
    'CountWeightedFull'                                                              : [ 9.99533281e+04, 9.99627734e+04, 9.99455469e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99533281e+04, 9.99533281e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 4.68348938e+05, 4.67730938e+05, 6.42944750e+05, 4.67988875e+05, 4.33498000e+05, 2.82040375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00004953e+05, 1.00229344e+05, 1.44456031e+05, 9.99268359e+04, 9.93790312e+04, 6.02241836e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.58185156e+04, 9.58186328e+04, 9.58215859e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.58185156e+04, 9.48824453e+04, 9.67476875e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.58185156e+04, 9.58185156e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 4.49681094e+05, 4.48286844e+05, 6.16248250e+05, 4.47745750e+05, 4.15767500e+05, 2.70489188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.60100000e+04, 9.60518516e+04, 1.38432266e+05, 9.55960391e+04, 9.52893906e+04, 5.77519297e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.57978750e+04, 9.57977344e+04, 9.58007656e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.57978750e+04, 9.48620781e+04, 9.67266875e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.57978750e+04, 9.57978750e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 4.49587688e+05, 4.48191062e+05, 6.16115250e+05, 4.47645125e+05, 4.15677719e+05, 2.70430938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.59900625e+04, 9.60313281e+04, 1.38402328e+05, 9.55745000e+04, 9.52686094e+04, 5.77395078e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     550148844), # 550.15MB, avg file size 550.15MB
  ("fsize_db",                        6080434302), # 6.08GB, avg file size 1.52GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo2V2tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99636719e+04, 9.99577656e+04, 9.99520391e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13896555e+05, 9.99636719e+04, 8.85151875e+04, 1.13896555e+05, 9.99636719e+04, 8.85151875e+04, 1.13896555e+05, 9.99636719e+04, 8.85151875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13897062e+05, 8.85146875e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.01607562e+05, 3.01676312e+05, 4.29189625e+05, 3.01590125e+05, 2.92850562e+05, 1.80941766e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99945312e+04, 1.00030812e+05, 1.44952531e+05, 9.99876406e+04, 9.97409297e+04, 5.99906562e+04, ],
    'CountWeightedFull'                                                              : [ 9.99395391e+04, 9.99337188e+04, 9.99283438e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.13869383e+05, 9.99395391e+04, 8.84940703e+04, 1.13869383e+05, 9.99395391e+04, 8.84940703e+04, 1.13869383e+05, 9.99395391e+04, 8.84940703e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.13869891e+05, 8.84935625e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.01537969e+05, 3.01604500e+05, 4.29086250e+05, 3.01514812e+05, 2.92780375e+05, 1.80899219e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99713750e+04, 1.00007008e+05, 1.44917344e+05, 9.99627891e+04, 9.97167734e+04, 5.99765703e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56729297e+04, 9.56629062e+04, 9.56715781e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56729297e+04, 9.47142969e+04, 9.66261094e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08991602e+05, 9.56729297e+04, 8.47314922e+04, 1.08991602e+05, 9.56729297e+04, 8.47314922e+04, 1.08991602e+05, 9.56729297e+04, 8.47314922e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08992047e+05, 8.47310469e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.89167625e+05, 2.88533406e+05, 4.10695375e+05, 2.88022344e+05, 2.80572469e+05, 1.73279281e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.58600156e+04, 9.56642344e+04, 1.38690938e+05, 9.54795781e+04, 9.55430469e+04, 5.74439062e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.56502656e+04, 9.56404453e+04, 9.56491562e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.56502656e+04, 9.46919297e+04, 9.66031562e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.08966000e+05, 9.56502656e+04, 8.47116094e+04, 1.08966000e+05, 9.56502656e+04, 8.47116094e+04, 1.08966000e+05, 9.56502656e+04, 8.47116094e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.08966445e+05, 8.47111562e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.89101656e+05, 2.88466000e+05, 4.10597875e+05, 2.87951938e+05, 2.80506188e+05, 1.73239094e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.58381562e+04, 9.56418750e+04, 1.38657688e+05, 9.54562344e+04, 9.55201641e+04, 5.74306094e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     542816333), # 542.82MB, avg file size 542.82MB
  ("fsize_db",                        6864309470), # 6.86GB, avg file size 762.70MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo2V2tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    7),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99565234e+04, 9.99493828e+04, 9.99615391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99565234e+04, 9.99565234e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.39802250e+05, 8.45192250e+05, 9.99307625e+05, 9.26632812e+05, 7.35831438e+05, 5.91500375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99937969e+04, 9.98068750e+04, 1.45408344e+05, 1.00010656e+05, 1.00202266e+05, 5.97862734e+04, ],
    'CountWeightedFull'                                                              : [ 9.99318281e+04, 9.99247969e+04, 9.99368750e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99318281e+04, 9.99318281e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.39574625e+05, 8.44984375e+05, 9.99061500e+05, 9.26399250e+05, 7.35650062e+05, 5.91353938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99700547e+04, 9.97823906e+04, 1.45372469e+05, 9.99849219e+04, 1.00177578e+05, 5.97714609e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.55768594e+04, 9.55689219e+04, 9.55802031e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.55768594e+04, 9.46032266e+04, 9.65460781e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.55768594e+04, 9.55768594e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.99418562e+05, 8.08165125e+05, 9.55518312e+05, 8.84977938e+05, 7.03991062e+05, 5.65911438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.57705625e+04, 9.53898125e+04, 1.38971391e+05, 9.54204375e+04, 9.58327266e+04, 5.71972500e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.55538281e+04, 9.55460000e+04, 9.55572500e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.55538281e+04, 9.45805469e+04, 9.65227031e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.55538281e+04, 9.55538281e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 8.99206500e+05, 8.07971500e+05, 9.55288250e+05, 8.84760625e+05, 7.03821438e+05, 5.65774812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.57483359e+04, 9.53669531e+04, 1.38937969e+05, 9.53964844e+04, 9.58097969e+04, 5.71834141e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     543630150), # 543.63MB, avg file size 543.63MB
  ("fsize_db",                        6154953101), # 6.15GB, avg file size 879.28MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo2V2tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99250781e+04, 9.99294375e+04, 9.99303672e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15698133e+05, 9.99250781e+04, 8.72048125e+04, 1.15698133e+05, 9.99250781e+04, 8.72048125e+04, 1.15698133e+05, 9.99250781e+04, 8.72048125e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15699258e+05, 8.72036875e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.26169375e+05, 5.22665625e+05, 7.12715750e+05, 5.26699625e+05, 4.76181625e+05, 3.13668844e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99518906e+04, 1.00077453e+05, 1.45254594e+05, 1.00055969e+05, 9.95288750e+04, 5.95824609e+04, ],
    'CountWeightedFull'                                                              : [ 9.98984609e+04, 9.99027344e+04, 9.99037422e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15667289e+05, 9.98984609e+04, 8.71815625e+04, 1.15667289e+05, 9.98984609e+04, 8.71815625e+04, 1.15667289e+05, 9.98984609e+04, 8.71815625e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15668422e+05, 8.71804375e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.26036250e+05, 5.22526375e+05, 7.12524250e+05, 5.26554188e+05, 4.76055625e+05, 3.13587594e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99267578e+04, 1.00050656e+05, 1.45215094e+05, 1.00028289e+05, 9.95019922e+04, 5.95670352e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.54890859e+04, 9.54875938e+04, 9.55013516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.54890859e+04, 9.45071797e+04, 9.64669062e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.10546922e+05, 9.54890859e+04, 8.33420156e+04, 1.10546922e+05, 9.54890859e+04, 8.33420156e+04, 1.10546922e+05, 9.54890859e+04, 8.33420156e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10548031e+05, 8.33408828e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 5.03647625e+05, 4.99316688e+05, 6.80992500e+05, 5.02257312e+05, 4.55308969e+05, 2.99851031e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.56613047e+04, 9.55894297e+04, 1.38770422e+05, 9.53996641e+04, 9.51521875e+04, 5.69502695e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.54640156e+04, 9.54625000e+04, 9.54763516e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.54640156e+04, 9.44824922e+04, 9.64415000e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.10517891e+05, 9.54640156e+04, 8.33200547e+04, 1.10517891e+05, 9.54640156e+04, 8.33200547e+04, 1.10517891e+05, 9.54640156e+04, 8.33200547e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.10519023e+05, 8.33189375e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 5.03522000e+05, 4.99185344e+05, 6.80812250e+05, 5.02120469e+05, 4.55190625e+05, 2.99774750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.56375547e+04, 9.55642500e+04, 1.38733312e+05, 9.53737188e+04, 9.51268906e+04, 5.69357891e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     540667258), # 540.67MB, avg file size 540.67MB
  ("fsize_db",                        6943822895), # 6.94GB, avg file size 694.38MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo2V2tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    3),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.98543516e+04, 9.98574219e+04, 9.98625000e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98543516e+04, 9.98543516e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98665000e+05, 9.92946125e+05, 9.98652125e+05, 9.98665000e+05, 9.57691938e+05, 9.51999375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99880078e+04, 9.99162656e+04, 1.45920469e+05, 1.00023586e+05, 1.00028875e+05, 5.93653945e+04, ],
    'CountWeightedFull'                                                              : [ 9.98289219e+04, 9.98316875e+04, 9.98366719e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98289219e+04, 9.98289219e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98395688e+05, 9.92691688e+05, 9.98395688e+05, 9.98395688e+05, 9.57446750e+05, 9.51743375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99621562e+04, 9.98881641e+04, 1.45879000e+05, 9.99954531e+04, 1.00000156e+05, 5.93494609e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53071875e+04, 9.53108125e+04, 9.53070703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53071875e+04, 9.43083906e+04, 9.63041250e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.53071875e+04, 9.53071875e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.53135875e+05, 9.47709500e+05, 9.53132625e+05, 9.53135875e+05, 9.14276688e+05, 9.08856938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.55968125e+04, 9.52810469e+04, 1.39210438e+05, 9.52231719e+04, 9.55379609e+04, 5.66847734e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.52822656e+04, 9.52857969e+04, 9.52820156e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.52822656e+04, 9.42836250e+04, 9.62790234e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.52822656e+04, 9.52822656e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.52882750e+05, 9.47461625e+05, 9.52882750e+05, 9.52882750e+05, 9.14037625e+05, 9.08616625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.55725000e+04, 9.52555000e+04, 1.39172312e+05, 9.51969531e+04, 9.55114375e+04, 5.66698047e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     542442768), # 542.44MB, avg file size 542.44MB
  ("fsize_db",                        6282400312), # 6.28GB, avg file size 2.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo2V2tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99997, ],
    'CountWeighted'                                                                  : [ 9.97616797e+04, 9.97720000e+04, 9.97773672e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.97616797e+04, 9.97616797e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.97639375e+05, 9.78737625e+05, 9.97654875e+05, 9.97630812e+05, 9.15926000e+05, 8.96990750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00015555e+05, 9.98490391e+04, 1.45669000e+05, 9.99538594e+04, 9.99071875e+04, 5.94155156e+04, ],
    'CountWeightedFull'                                                              : [ 9.97310156e+04, 9.97412344e+04, 9.97458906e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97310156e+04, 9.97310156e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.97344625e+05, 9.78436562e+05, 9.97348062e+05, 9.97335750e+05, 9.15643812e+05, 8.96725125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99875234e+04, 9.98186016e+04, 1.45623984e+05, 9.99231562e+04, 9.98758672e+04, 5.93979453e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52079766e+04, 9.52008281e+04, 9.52259766e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52079766e+04, 9.42145391e+04, 9.62015469e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.52079766e+04, 9.52079766e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.52086438e+05, 9.34116062e+05, 9.52099375e+05, 9.52078812e+05, 8.74290125e+05, 8.56292500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.56131719e+04, 9.52471641e+04, 1.38939688e+05, 9.51492500e+04, 9.53421719e+04, 5.67127148e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.51796250e+04, 9.51724844e+04, 9.51971641e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.51796250e+04, 9.41866641e+04, 9.61727109e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.51796250e+04, 9.51796250e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.51813875e+05, 9.33838250e+05, 9.51816188e+05, 9.51805500e+05, 8.74030250e+05, 8.56046812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.55869609e+04, 9.52190859e+04, 1.38897953e+05, 9.51208281e+04, 9.53132656e+04, 5.66964062e+04, ],
  }),
  ("nof_tree_events",                 99997),
  ("nof_db_events",                   99997),
  ("fsize_local",                     541823358), # 541.82MB, avg file size 541.82MB
  ("fsize_db",                        7212112356), # 7.21GB, avg file size 721.21MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 394995, ],
    'CountWeighted'                                                                  : [ 3.94970543e+05, 3.94982699e+05, 3.94986055e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99821884e+05, 3.94970543e+05, 3.87347695e+05, 3.99821884e+05, 3.94970543e+05, 3.87347695e+05, 3.99821884e+05, 3.94970543e+05, 3.87347695e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99821884e+05, 3.87347695e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87384950e+05, 3.87371970e+05, 3.87405163e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87384950e+05, 3.85410941e+05, 3.89256848e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.92098971e+05, 3.87384950e+05, 3.79939293e+05, 3.92098971e+05, 3.87384950e+05, 3.79939293e+05, 3.92098971e+05, 3.87384950e+05, 3.79939293e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92098971e+05, 3.79939293e+05, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     1449930522), # 1.45GB, avg file size 724.97MB
  ("fsize_db",                        19490651554), # 19.49GB, avg file size 2.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 395995, ],
    'CountWeighted'                                                                  : [ 3.96046062e+05, 3.95973562e+05, 3.95918531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.02169000e+05, 3.96042031e+05, 3.87238812e+05, 4.02169000e+05, 3.96042031e+05, 3.87238812e+05, 4.02169000e+05, 3.96042031e+05, 3.87238812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.02169000e+05, 3.87238812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88066938e+05, 3.87999938e+05, 3.87991094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88066938e+05, 3.86014719e+05, 3.90016812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.94042500e+05, 3.88062688e+05, 3.79496562e+05, 3.94042500e+05, 3.88062688e+05, 3.79496562e+05, 3.94042500e+05, 3.88062688e+05, 3.79496562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.94042500e+05, 3.79496562e+05, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     1478302719), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        19808318644), # 19.81GB, avg file size 943.25MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99985469e+05, 4.00019625e+05, 3.99915250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07519344e+05, 3.99978031e+05, 3.90123625e+05, 4.07519344e+05, 3.99978031e+05, 3.90123625e+05, 4.07519344e+05, 3.99978031e+05, 3.90123625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07519344e+05, 3.90123625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.91644625e+05, 3.91668969e+05, 3.91579312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.91644625e+05, 3.89514500e+05, 3.93681938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98969906e+05, 3.91637938e+05, 3.82033969e+05, 3.98969906e+05, 3.91637938e+05, 3.82033969e+05, 3.98969906e+05, 3.91637938e+05, 3.82033969e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98969906e+05, 3.82033969e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1522310632), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        19945565524), # 19.95GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 394995, ],
    'CountWeighted'                                                                  : [ 3.94911812e+05, 3.94998844e+05, 3.94962500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.03595000e+05, 3.94911812e+05, 3.84344531e+05, 4.03595000e+05, 3.94911812e+05, 3.84344531e+05, 4.03595000e+05, 3.94911812e+05, 3.84344531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.03595000e+05, 3.84344531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86437094e+05, 3.86489719e+05, 3.86490938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86437094e+05, 3.84286750e+05, 3.88510500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.94863812e+05, 3.86437094e+05, 3.76119000e+05, 3.94863812e+05, 3.86437094e+05, 3.76119000e+05, 3.94863812e+05, 3.86437094e+05, 3.76119000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.94863812e+05, 3.76119000e+05, ],
  }),
  ("nof_tree_events",                 394995),
  ("nof_db_events",                   394995),
  ("fsize_local",                     1527631171), # 1.53GB, avg file size 1.53GB
  ("fsize_db",                        19924344376), # 19.92GB, avg file size 830.18MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99902094e+05, 2.99974719e+05, 2.99951500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08265688e+05, 2.99902094e+05, 2.90533625e+05, 3.08265688e+05, 2.99902094e+05, 2.90533625e+05, 3.08265688e+05, 2.99902094e+05, 2.90533625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08265688e+05, 2.90533625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92983938e+05, 2.93012500e+05, 2.93032219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92983938e+05, 2.91248000e+05, 2.94661438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.01080750e+05, 2.92983938e+05, 2.83845406e+05, 3.01080750e+05, 2.92983938e+05, 2.83845406e+05, 3.01080750e+05, 2.92983938e+05, 2.83845406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.01080750e+05, 2.83845406e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1196794744), # 1.20GB, avg file size 1.20GB
  ("fsize_db",                        15226334046), # 15.23GB, avg file size 761.32MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 284992, ],
    'CountWeighted'                                                                  : [ 2.85007656e+05, 2.85000000e+05, 2.84948562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.94338250e+05, 2.85006250e+05, 2.74835156e+05, 2.94338250e+05, 2.85006250e+05, 2.74835156e+05, 2.94338250e+05, 2.85006250e+05, 2.74835156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.94338250e+05, 2.74835125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.78087031e+05, 2.78071469e+05, 2.78056656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.78087031e+05, 2.76376188e+05, 2.79742781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.87148500e+05, 2.78084938e+05, 2.68209688e+05, 2.87148500e+05, 2.78084938e+05, 2.68209688e+05, 2.87148500e+05, 2.78084938e+05, 2.68209688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.87148500e+05, 2.68209656e+05, ],
  }),
  ("nof_tree_events",                 284992),
  ("nof_db_events",                   284992),
  ("fsize_local",                     1169663491), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        14565597893), # 14.57GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 299995, ],
    'CountWeighted'                                                                  : [ 2.99937562e+05, 2.99881344e+05, 3.00032750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11973625e+05, 2.99937562e+05, 2.87601406e+05, 3.11973625e+05, 2.99937562e+05, 2.87601406e+05, 3.11973625e+05, 2.99937562e+05, 2.87601406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11973625e+05, 2.87601406e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92221125e+05, 2.92175062e+05, 2.92293812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92221125e+05, 2.90340656e+05, 2.94059312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03879875e+05, 2.92221125e+05, 2.80244750e+05, 3.03879875e+05, 2.92221125e+05, 2.80244750e+05, 3.03879875e+05, 2.92221125e+05, 2.80244750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03879875e+05, 2.80244750e+05, ],
  }),
  ("nof_tree_events",                 299995),
  ("nof_db_events",                   299995),
  ("fsize_local",                     1281596561), # 1.28GB, avg file size 1.28GB
  ("fsize_db",                        15709690748), # 15.71GB, avg file size 924.10MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 289998, ],
    'CountWeighted'                                                                  : [ 2.89995812e+05, 2.89956625e+05, 2.89965594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.04610969e+05, 2.89995812e+05, 2.75747344e+05, 3.04610969e+05, 2.89995812e+05, 2.75747344e+05, 3.04610969e+05, 2.89995812e+05, 2.75747344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.04610969e+05, 2.75747344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.81938625e+05, 2.81907938e+05, 2.81924312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.81938625e+05, 2.80012000e+05, 2.83823875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96093188e+05, 2.81938625e+05, 2.68143875e+05, 2.96093188e+05, 2.81938625e+05, 2.68143875e+05, 2.96093188e+05, 2.81938625e+05, 2.68143875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96093188e+05, 2.68143875e+05, ],
  }),
  ("nof_tree_events",                 289998),
  ("nof_db_events",                   289998),
  ("fsize_local",                     1306300429), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        15476703995), # 15.48GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 279993, ],
    'CountWeighted'                                                                  : [ 2.79968375e+05, 2.79990500e+05, 2.79973250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.96578844e+05, 2.79968375e+05, 2.64335062e+05, 2.96578844e+05, 2.79968375e+05, 2.64335062e+05, 2.96578844e+05, 2.79968375e+05, 2.64335062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.96578844e+05, 2.64335062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.71965062e+05, 2.71968562e+05, 2.71975375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.71965062e+05, 2.70068438e+05, 2.73824281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.88036625e+05, 2.71965062e+05, 2.56832578e+05, 2.88036625e+05, 2.71965062e+05, 2.56832578e+05, 2.88036625e+05, 2.71965062e+05, 2.56832578e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.88036625e+05, 2.56832578e+05, ],
  }),
  ("nof_tree_events",                 279993),
  ("nof_db_events",                   279993),
  ("fsize_local",                     1316582992), # 1.32GB, avg file size 1.32GB
  ("fsize_db",                        15200236312), # 15.20GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99961703e+05, 1.99953672e+05, 2.00027188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13367812e+05, 1.99961703e+05, 1.87663609e+05, 2.13367812e+05, 1.99961703e+05, 1.87663609e+05, 2.13367812e+05, 1.99961703e+05, 1.87663609e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13367922e+05, 1.87663484e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94020547e+05, 1.94013953e+05, 1.94066562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94020547e+05, 1.92631078e+05, 1.95388906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06975312e+05, 1.94020547e+05, 1.82118406e+05, 2.06975312e+05, 1.94020547e+05, 1.82118406e+05, 2.06975312e+05, 1.94020547e+05, 1.82118406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06975406e+05, 1.82118312e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     972975743), # 972.98MB, avg file size 972.98MB
  ("fsize_db",                        11038820268), # 11.04GB, avg file size 849.14MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199995, ],
    'CountWeighted'                                                                  : [ 1.99967062e+05, 1.99962750e+05, 1.99991656e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.14710312e+05, 1.99967062e+05, 1.86601250e+05, 2.14710312e+05, 1.99967062e+05, 1.86601250e+05, 2.14710312e+05, 1.99967062e+05, 1.86601250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.14710312e+05, 1.86601250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94015984e+05, 1.94001906e+05, 1.94045938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94015984e+05, 1.92630688e+05, 1.95380250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.08272656e+05, 1.94015984e+05, 1.81080562e+05, 2.08272656e+05, 1.94015984e+05, 1.81080562e+05, 2.08272656e+05, 1.94015984e+05, 1.81080562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.08272656e+05, 1.81080562e+05, ],
  }),
  ("nof_tree_events",                 199995),
  ("nof_db_events",                   199995),
  ("fsize_local",                     1001949655), # 1.00GB, avg file size 1.00GB
  ("fsize_db",                        11235761543), # 11.24GB, avg file size 802.55MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199996, ],
    'CountWeighted'                                                                  : [ 1.99984594e+05, 1.99986406e+05, 1.99962500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.15957328e+05, 1.99984594e+05, 1.85674125e+05, 2.15957328e+05, 1.99984594e+05, 1.85674125e+05, 2.15957328e+05, 1.99984594e+05, 1.85674125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.15957328e+05, 1.85674125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93922438e+05, 1.93909594e+05, 1.93918688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93922438e+05, 1.92518328e+05, 1.95304984e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09364312e+05, 1.93922438e+05, 1.80080094e+05, 2.09364312e+05, 1.93922438e+05, 1.80080094e+05, 2.09364312e+05, 1.93922438e+05, 1.80080094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09364312e+05, 1.80080094e+05, ],
  }),
  ("nof_tree_events",                 199996),
  ("nof_db_events",                   199996),
  ("fsize_local",                     1023250041), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11265507117), # 11.27GB, avg file size 804.68MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 195999, ],
    'CountWeighted'                                                                  : [ 1.95966469e+05, 1.96011125e+05, 1.96008750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.12742938e+05, 1.95965562e+05, 1.81136844e+05, 2.12742938e+05, 1.95965562e+05, 1.81136844e+05, 2.12742938e+05, 1.95965562e+05, 1.81136844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.12743125e+05, 1.81136656e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90109469e+05, 1.90128344e+05, 1.90147375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90109469e+05, 1.88756938e+05, 1.91444844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.06325391e+05, 1.90108375e+05, 1.75750000e+05, 2.06325391e+05, 1.90108375e+05, 1.75750000e+05, 2.06325391e+05, 1.90108375e+05, 1.75750000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.06325531e+05, 1.75749875e+05, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     1017963396), # 1.02GB, avg file size 1.02GB
  ("fsize_db",                        11148852408), # 11.15GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 195997, ],
    'CountWeighted'                                                                  : [ 1.95964781e+05, 1.95970406e+05, 1.95941297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.13670062e+05, 1.95963109e+05, 1.80385625e+05, 2.13670062e+05, 1.95963109e+05, 1.80385625e+05, 2.13670062e+05, 1.95963109e+05, 1.80385625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.13671188e+05, 1.80384469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.90094875e+05, 1.90087094e+05, 1.90083016e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.90094875e+05, 1.88743125e+05, 1.91426062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.07223688e+05, 1.90093438e+05, 1.75009812e+05, 2.07223688e+05, 1.90093438e+05, 1.75009812e+05, 2.07223688e+05, 1.90093438e+05, 1.75009812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.07224234e+05, 1.75009281e+05, ],
  }),
  ("nof_tree_events",                 195997),
  ("nof_db_events",                   195997),
  ("fsize_local",                     1031456296), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11274075929), # 11.27GB, avg file size 626.34MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99946891e+05, 1.99974656e+05, 1.99953719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18950312e+05, 1.99946891e+05, 1.83382469e+05, 2.18950312e+05, 1.99946891e+05, 1.83382469e+05, 2.18950312e+05, 1.99946891e+05, 1.83382469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18950984e+05, 1.83381781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94016281e+05, 1.94014031e+05, 1.94044609e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94016281e+05, 1.92652641e+05, 1.95362500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12409188e+05, 1.94016281e+05, 1.77967219e+05, 2.12409188e+05, 1.94016281e+05, 1.77967219e+05, 2.12409188e+05, 1.94016281e+05, 1.77967219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12409453e+05, 1.77966938e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1064198907), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11369615851), # 11.37GB, avg file size 1.89GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99960438e+05, 1.99995516e+05, 1.99960500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19821969e+05, 1.99960438e+05, 1.82751422e+05, 2.19821969e+05, 1.99960438e+05, 1.82751422e+05, 2.19821969e+05, 1.99960438e+05, 1.82751422e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19821969e+05, 1.82751422e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94074781e+05, 1.94082031e+05, 1.94085125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94074781e+05, 1.92725031e+05, 1.95407844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.13300062e+05, 1.94074219e+05, 1.77397844e+05, 2.13300062e+05, 1.94074219e+05, 1.77397844e+05, 2.13300062e+05, 1.94074219e+05, 1.77397844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.13300062e+05, 1.77397844e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1071714772), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        11488159001), # 11.49GB, avg file size 1.15GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 191995, ],
    'CountWeighted'                                                                  : [ 1.91991703e+05, 1.91940906e+05, 1.91948703e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91991703e+05, 1.91991703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86298844e+05, 1.86261094e+05, 1.86273938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86298844e+05, 1.84995875e+05, 1.87579594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.86298844e+05, 1.86298844e+05, ],
  }),
  ("nof_tree_events",                 191995),
  ("nof_db_events",                   191995),
  ("fsize_local",                     1042160135), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11613877178), # 11.61GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 1.00007969e+05, 1.00003773e+05, 9.99957656e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10551680e+05, 1.00007969e+05, 9.09851875e+04, 1.10551680e+05, 1.00007969e+05, 9.09851875e+04, 1.10551680e+05, 1.00007969e+05, 9.09851875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10551680e+05, 9.09851875e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71716094e+04, 9.71614219e+04, 9.71713438e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71716094e+04, 9.65215000e+04, 9.78114062e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07401406e+05, 9.71716094e+04, 8.84177422e+04, 1.07401406e+05, 9.71716094e+04, 8.84177422e+04, 1.07401406e+05, 9.71716094e+04, 8.84177422e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07401406e+05, 8.84177422e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     543864763), # 543.86MB, avg file size 543.86MB
  ("fsize_db",                        5984452524), # 5.98GB, avg file size 598.45MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2Tau_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99832344e+04, 9.99760469e+04, 9.99992344e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11340320e+05, 9.99832344e+04, 9.03368828e+04, 1.11340320e+05, 9.99832344e+04, 9.03368828e+04, 1.11340320e+05, 9.99832344e+04, 9.03368828e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11340320e+05, 9.03368828e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70214922e+04, 9.70016094e+04, 9.70454688e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70214922e+04, 9.63482578e+04, 9.76866016e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08028406e+05, 9.70214922e+04, 8.76718203e+04, 1.08028406e+05, 9.70214922e+04, 8.76718203e+04, 1.08028406e+05, 9.70214922e+04, 8.76718203e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08028406e+05, 8.76718203e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     547829762), # 547.83MB, avg file size 547.83MB
  ("fsize_db",                        5974953438), # 5.97GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_2v2t"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2tau_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99935703e+04, 9.99838516e+04, 9.99839688e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99935703e+04, 9.99935703e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99911812e+05, 9.99911812e+05, 9.99911812e+05, 9.99911812e+05, 9.99911812e+05, 9.99911812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00016320e+05, 1.00103961e+05, 1.44419625e+05, 9.99605547e+04, 9.99037734e+04, 6.05719688e+04, ],
    'CountWeightedFull'                                                              : [ 9.99717422e+04, 9.99619297e+04, 9.99622266e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99717422e+04, 9.99717422e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99692875e+05, 9.99692875e+05, 9.99692875e+05, 9.99692875e+05, 9.99692875e+05, 9.99692875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99952500e+04, 1.00082086e+05, 1.44387953e+05, 9.99377266e+04, 9.98819297e+04, 6.05588242e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70980781e+04, 9.70762578e+04, 9.71058672e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70980781e+04, 9.64368594e+04, 9.77491172e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70980781e+04, 9.70980781e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70960812e+05, 9.70960812e+05, 9.70960812e+05, 9.70960812e+05, 9.70960812e+05, 9.70960812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72622812e+04, 9.71720625e+04, 1.40218859e+05, 9.68882422e+04, 9.70761016e+04, 5.88528828e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70772578e+04, 9.70554062e+04, 9.70850781e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70772578e+04, 9.64162812e+04, 9.77280781e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70772578e+04, 9.70772578e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70752750e+05, 9.70752750e+05, 9.70752750e+05, 9.70752750e+05, 9.70752750e+05, 9.70752750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72421875e+04, 9.71513750e+04, 1.40188719e+05, 9.68666328e+04, 9.70553125e+04, 5.88403359e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     528919894), # 528.92MB, avg file size 528.92MB
  ("fsize_db",                        6241216475), # 6.24GB, avg file size 567.38MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2tau_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99916719e+04, 9.99959141e+04, 9.99855859e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99916719e+04, 9.99916719e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99838125e+05, 9.99838125e+05, 9.99838125e+05, 9.99838125e+05, 9.99838125e+05, 9.99838125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99607188e+04, 1.00310016e+05, 1.44670172e+05, 1.00022477e+05, 9.93602188e+04, 6.00847891e+04, ],
    'CountWeightedFull'                                                              : [ 9.99672500e+04, 9.99716016e+04, 9.99611406e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99672500e+04, 9.99672500e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99594875e+05, 9.99594875e+05, 9.99594875e+05, 9.99594875e+05, 9.99594875e+05, 9.99594875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99378281e+04, 1.00285828e+05, 1.44635766e+05, 9.99976406e+04, 9.93364688e+04, 6.00703867e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70587578e+04, 9.70682500e+04, 9.70540469e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70587578e+04, 9.63951250e+04, 9.77138125e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70587578e+04, 9.70587578e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70530312e+05, 9.70530312e+05, 9.70530312e+05, 9.70530312e+05, 9.70530312e+05, 9.70530312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.71925781e+04, 9.73226875e+04, 1.40381719e+05, 9.68831406e+04, 9.65055469e+04, 5.83645977e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70360312e+04, 9.70455781e+04, 9.70312969e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70360312e+04, 9.63726875e+04, 9.76906250e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70360312e+04, 9.70360312e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70303375e+05, 9.70303375e+05, 9.70303375e+05, 9.70303375e+05, 9.70303375e+05, 9.70303375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.71709062e+04, 9.73000781e+04, 1.40349469e+05, 9.68597500e+04, 9.64834297e+04, 5.83510508e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     532418801), # 532.42MB, avg file size 532.42MB
  ("fsize_db",                        6208722036), # 6.21GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2tau_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99915703e+04, 1.00001188e+05, 9.99967344e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99915703e+04, 9.99915703e+04, ],
    'CountWeightedPSWeight'                                                          : [ 1.00004631e+06, 1.00004631e+06, 1.00004631e+06, 1.00004631e+06, 1.00004631e+06, 1.00004631e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00036250e+05, 1.00108219e+05, 1.45215766e+05, 9.99592031e+04, 9.98161953e+04, 5.98638711e+04, ],
    'CountWeightedFull'                                                              : [ 9.99675000e+04, 9.99765469e+04, 9.99722734e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99675000e+04, 9.99675000e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99797000e+05, 9.99797000e+05, 9.99797000e+05, 9.99797000e+05, 9.99797000e+05, 9.99797000e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00012719e+05, 1.00083625e+05, 1.45179297e+05, 9.99334766e+04, 9.97911484e+04, 5.98493711e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70993438e+04, 9.70967422e+04, 9.71133516e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70993438e+04, 9.64425469e+04, 9.77475391e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70993438e+04, 9.70993438e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.71086188e+05, 9.71086188e+05, 9.71086188e+05, 9.71086188e+05, 9.71086188e+05, 9.71086188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73102656e+04, 9.71742109e+04, 1.40953672e+05, 9.68568516e+04, 9.69669922e+04, 5.81778789e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70763203e+04, 9.70733984e+04, 9.70901094e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70763203e+04, 9.64198047e+04, 9.77242500e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70763203e+04, 9.70763203e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70851125e+05, 9.70851125e+05, 9.70851125e+05, 9.70851125e+05, 9.70851125e+05, 9.70851125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72877969e+04, 9.71509531e+04, 1.40919219e+05, 9.68325234e+04, 9.69432500e+04, 5.81641016e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     522378810), # 522.38MB, avg file size 522.38MB
  ("fsize_db",                        7095285309), # 7.10GB, avg file size 645.03MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2tau_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99948281e+04, 9.99868594e+04, 9.99870625e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99948281e+04, 9.99948281e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99935438e+05, 9.99935438e+05, 9.99935438e+05, 9.99935438e+05, 9.99935438e+05, 9.99935438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00009430e+05, 1.00048602e+05, 1.45363000e+05, 9.99757188e+04, 9.97697031e+04, 5.96727188e+04, ],
    'CountWeightedFull'                                                              : [ 9.99690547e+04, 9.99615078e+04, 9.99613984e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99690547e+04, 9.99690547e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99677125e+05, 9.99677125e+05, 9.99677125e+05, 9.99677125e+05, 9.99677125e+05, 9.99677125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99854062e+04, 1.00022641e+05, 1.45325859e+05, 9.99495859e+04, 9.97451016e+04, 5.96578789e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70780781e+04, 9.70779609e+04, 9.70717344e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70780781e+04, 9.64141250e+04, 9.77312500e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70780781e+04, 9.70780781e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70773125e+05, 9.70773125e+05, 9.70773125e+05, 9.70773125e+05, 9.70773125e+05, 9.70773125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72714453e+04, 9.70898438e+04, 1.41059922e+05, 9.68381797e+04, 9.68991875e+04, 5.79734141e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70534062e+04, 9.70536406e+04, 9.70471016e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70534062e+04, 9.63897109e+04, 9.77063281e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70534062e+04, 9.70534062e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70525938e+05, 9.70525938e+05, 9.70525938e+05, 9.70525938e+05, 9.70525938e+05, 9.70525938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72484062e+04, 9.70649375e+04, 1.41024406e+05, 9.68132031e+04, 9.68756406e+04, 5.79591836e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     516042539), # 516.04MB, avg file size 516.04MB
  ("fsize_db",                        6313392877), # 6.31GB, avg file size 631.34MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2tau_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_2v2t_PSWeights"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99977383e+04, 1.00002461e+05, 9.99968750e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99977383e+04, 9.99977383e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00078250e+05, 1.00074268e+05, 1.45555406e+05, 9.99100664e+04, 9.97784551e+04, 5.95676025e+04, ],
    'CountWeightedFull'                                                              : [ 9.99714375e+04, 9.99761719e+04, 9.99705098e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99714375e+04, 9.99714375e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99726297e+05, 9.99726297e+05, 9.99726297e+05, 9.99726297e+05, 9.99726297e+05, 9.99726297e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00053145e+05, 1.00048613e+05, 1.45516715e+05, 9.98830527e+04, 9.97512578e+04, 5.95521367e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71340508e+04, 9.71316992e+04, 9.71394609e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71340508e+04, 9.64812031e+04, 9.77766602e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71340508e+04, 9.71340508e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73843672e+04, 9.71724102e+04, 1.41345434e+05, 9.68343516e+04, 9.69666289e+04, 5.78952344e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.71089297e+04, 9.71065664e+04, 9.71142734e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.71089297e+04, 9.64563008e+04, 9.77512598e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.71089297e+04, 9.71089297e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.71098406e+05, 9.71098406e+05, 9.71098406e+05, 9.71098406e+05, 9.71098406e+05, 9.71098406e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.73603574e+04, 9.71478672e+04, 1.41308445e+05, 9.68085195e+04, 9.69405820e+04, 5.78804287e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     514082201), # 514.08MB, avg file size 257.04MB
  ("fsize_db",                        6538556294), # 6.54GB, avg file size 594.41MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2tau_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 97997, ],
    'CountWeighted'                                                                  : [ 9.80015625e+04, 9.79914297e+04, 9.79967656e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.80015625e+04, 9.80015625e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.79991375e+05, 9.79991375e+05, 9.79991375e+05, 9.79991375e+05, 9.79991375e+05, 9.79991375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.80395391e+04, 9.78430156e+04, 1.42787766e+05, 9.79304062e+04, 9.80015312e+04, 5.81852109e+04, ],
    'CountWeightedFull'                                                              : [ 9.79698828e+04, 9.79607344e+04, 9.79647734e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.79698828e+04, 9.79698828e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.79677625e+05, 9.79677625e+05, 9.79677625e+05, 9.79677625e+05, 9.79677625e+05, 9.79677625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.80134844e+04, 9.78109844e+04, 1.42742203e+05, 9.79023125e+04, 9.79706484e+04, 5.81689688e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.50800000e+04, 9.50675391e+04, 9.50865703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.50800000e+04, 9.44152891e+04, 9.57337969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.50800000e+04, 9.50800000e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.50785000e+05, 9.50785000e+05, 9.50785000e+05, 9.50785000e+05, 9.50785000e+05, 9.50785000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.52907812e+04, 9.49204688e+04, 1.38547625e+05, 9.47995859e+04, 9.51366875e+04, 5.64691055e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.50506875e+04, 9.50388984e+04, 9.50568906e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.50506875e+04, 9.43864297e+04, 9.57039375e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.50506875e+04, 9.50506875e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.50493875e+05, 9.50493875e+05, 9.50493875e+05, 9.50493875e+05, 9.50493875e+05, 9.50493875e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.52658828e+04, 9.48905703e+04, 1.38505000e+05, 9.47728594e+04, 9.51080625e+04, 5.64536406e+04, ],
  }),
  ("nof_tree_events",                 97997),
  ("nof_db_events",                   97997),
  ("fsize_local",                     501668008), # 501.67MB, avg file size 501.67MB
  ("fsize_db",                        6260618237), # 6.26GB, avg file size 782.58MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo2V2tau_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_2v2t_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 1.00002469e+05, 9.99998125e+04, 9.99886875e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.00002469e+05, 1.00002469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99970375e+05, 9.99970375e+05, 9.99970375e+05, 9.99970375e+05, 9.99970375e+05, 9.99970375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99577969e+04, 1.00040805e+05, 1.45957094e+05, 1.00026234e+05, 9.98886875e+04, 5.92621875e+04, ],
    'CountWeightedFull'                                                              : [ 9.99696094e+04, 9.99674922e+04, 9.99564375e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99696094e+04, 9.99696094e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99647625e+05, 9.99647625e+05, 9.99647625e+05, 9.99647625e+05, 9.99647625e+05, 9.99647625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99290469e+04, 1.00008016e+05, 1.45910156e+05, 9.99946875e+04, 9.98572031e+04, 5.92442188e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69599531e+04, 9.69536250e+04, 9.69555234e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69599531e+04, 9.62668125e+04, 9.76411562e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.69599531e+04, 9.69599531e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.69564625e+05, 9.69564625e+05, 9.69564625e+05, 9.69564625e+05, 9.69564625e+05, 9.69564625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.70965156e+04, 9.69549062e+04, 1.41514062e+05, 9.67635469e+04, 9.69370781e+04, 5.74884375e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69295625e+04, 9.69236875e+04, 9.69253750e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69295625e+04, 9.62370156e+04, 9.76102656e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.69295625e+04, 9.69295625e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.69264188e+05, 9.69264188e+05, 9.69264188e+05, 9.69264188e+05, 9.69264188e+05, 9.69264188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.70692812e+04, 9.69246016e+04, 1.41470328e+05, 9.67339531e+04, 9.69075469e+04, 5.74716172e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     513177011), # 513.18MB, avg file size 513.18MB
  ("fsize_db",                        6427253404), # 6.43GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_2v2t_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_250_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99938000e+05, 3.99982188e+05, 4.00000906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99938000e+05, 3.99938000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.93456625e+05, 3.93478250e+05, 3.93505812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.93456625e+05, 3.91730969e+05, 3.95078875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.93456625e+05, 3.93456625e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1442897499), # 1.44GB, avg file size 1.44GB
  ("fsize_db",                        20459339723), # 20.46GB, avg file size 1.46GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_260_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_260_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 3.99967750e+05, 3.99970219e+05, 3.99949594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06231594e+05, 3.99967750e+05, 3.91162438e+05, 4.06231594e+05, 3.99967750e+05, 3.91162438e+05, 4.06231594e+05, 3.99967750e+05, 3.91162438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06231594e+05, 3.91162438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.93223344e+05, 3.93218438e+05, 3.93217375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.93223344e+05, 3.91440438e+05, 3.94904750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99350000e+05, 3.93223344e+05, 3.84596875e+05, 3.99350000e+05, 3.93223344e+05, 3.84596875e+05, 3.99350000e+05, 3.93223344e+05, 3.84596875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99350000e+05, 3.84596875e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1457206746), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        19550516838), # 19.55GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_270_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_270_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85978656e+05, 3.86073594e+05, 3.85895281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.93216938e+05, 3.85978281e+05, 3.76476375e+05, 3.93216938e+05, 3.85978281e+05, 3.76476375e+05, 3.93216938e+05, 3.85978281e+05, 3.76476375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.93216938e+05, 3.76476375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.79159000e+05, 3.79213062e+05, 3.79109000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.79159000e+05, 3.77367250e+05, 3.80851000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.86241438e+05, 3.79158000e+05, 3.69855562e+05, 3.86241438e+05, 3.79158000e+05, 3.69855562e+05, 3.86241438e+05, 3.79158000e+05, 3.69855562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86241438e+05, 3.69855562e+05, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1430045185), # 1.43GB, avg file size 1.43GB
  ("fsize_db",                        18992366194), # 18.99GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_280_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_280_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 388998, ],
    'CountWeighted'                                                                  : [ 3.88993312e+05, 3.89050188e+05, 3.89025094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.88993312e+05, 3.88993312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81861250e+05, 3.81889219e+05, 3.81896219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81861250e+05, 3.79997344e+05, 3.83628531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.81861250e+05, 3.81861250e+05, ],
  }),
  ("nof_tree_events",                 388998),
  ("nof_db_events",                   388998),
  ("fsize_local",                     1478108345), # 1.48GB, avg file size 1.48GB
  ("fsize_db",                        20249921988), # 20.25GB, avg file size 880.43MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_300_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_300_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99994156e+05, 2.99953906e+05, 2.99988125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.08273938e+05, 2.99993250e+05, 2.90511031e+05, 3.08273938e+05, 2.99993250e+05, 2.90511031e+05, 3.08273938e+05, 2.99993250e+05, 2.90511031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.08273938e+05, 2.90511031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93966938e+05, 2.93936812e+05, 2.93963000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93966938e+05, 2.92413625e+05, 2.95445812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02047688e+05, 2.93965438e+05, 2.84706750e+05, 3.02047688e+05, 2.93965438e+05, 2.84706750e+05, 3.02047688e+05, 2.93965438e+05, 2.84706750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02047688e+05, 2.84706750e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1170732826), # 1.17GB, avg file size 1.17GB
  ("fsize_db",                        15102940723), # 15.10GB, avg file size 943.93MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_320_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_320_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99958625e+05, 2.99975531e+05, 3.00022219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09824000e+05, 2.99958625e+05, 2.89276062e+05, 3.09824000e+05, 2.99958625e+05, 2.89276062e+05, 3.09824000e+05, 2.99958625e+05, 2.89276062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09824000e+05, 2.89276062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93538344e+05, 2.93526406e+05, 2.93594469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93538344e+05, 2.91899406e+05, 2.95100844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.03146562e+05, 2.93538344e+05, 2.83112625e+05, 3.03146562e+05, 2.93538344e+05, 2.83112625e+05, 3.03146562e+05, 2.93538344e+05, 2.83112625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.03146562e+05, 2.83112625e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1208652503), # 1.21GB, avg file size 1.21GB
  ("fsize_db",                        15313788135), # 15.31GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_350_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_350_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 291998, ],
    'CountWeighted'                                                                  : [ 2.92021500e+05, 2.91952531e+05, 2.91962125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.03639531e+05, 2.92021500e+05, 2.79966875e+05, 3.03639531e+05, 2.92021500e+05, 2.79966875e+05, 3.03639531e+05, 2.92021500e+05, 2.79966875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.03639531e+05, 2.79966875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.85216219e+05, 2.85151375e+05, 2.85194188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.85216219e+05, 2.83505281e+05, 2.86853375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96541375e+05, 2.85216219e+05, 2.73488188e+05, 2.96541375e+05, 2.85216219e+05, 2.73488188e+05, 2.96541375e+05, 2.85216219e+05, 2.73488188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96541375e+05, 2.73488188e+05, ],
  }),
  ("nof_tree_events",                 291998),
  ("nof_db_events",                   291998),
  ("fsize_local",                     1224632436), # 1.22GB, avg file size 1.22GB
  ("fsize_db",                        15117730207), # 15.12GB, avg file size 1.16GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_400_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_400_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 3.00046125e+05, 2.99928000e+05, 3.00051719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15116438e+05, 3.00046125e+05, 2.85271875e+05, 3.15116438e+05, 3.00046125e+05, 2.85271875e+05, 3.15116438e+05, 3.00046125e+05, 2.85271875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15116438e+05, 2.85271812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92168969e+05, 2.92079094e+05, 2.92191406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92168969e+05, 2.90230188e+05, 2.94043594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06820875e+05, 2.92168969e+05, 2.77846438e+05, 3.06820875e+05, 2.92168969e+05, 2.77846438e+05, 3.06820875e+05, 2.92168969e+05, 2.77846438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06820906e+05, 2.77846375e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1334794810), # 1.33GB, avg file size 1.33GB
  ("fsize_db",                        15994431220), # 15.99GB, avg file size 799.72MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_450_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_450_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 292000, ],
    'CountWeighted'                                                                  : [ 2.91998500e+05, 2.91991281e+05, 2.91964469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09297375e+05, 2.91989812e+05, 2.75677750e+05, 3.09297375e+05, 2.91989812e+05, 2.75677750e+05, 3.09297375e+05, 2.91989812e+05, 2.75677750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09297375e+05, 2.75677750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.83698875e+05, 2.83672594e+05, 2.83689531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.83698875e+05, 2.81684625e+05, 2.85652719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.00458812e+05, 2.83692688e+05, 2.67895562e+05, 3.00458812e+05, 2.83692688e+05, 2.67895562e+05, 3.00458812e+05, 2.83692688e+05, 2.67895562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.00458812e+05, 2.67895562e+05, ],
  }),
  ("nof_tree_events",                 292000),
  ("nof_db_events",                   292000),
  ("fsize_local",                     1357081034), # 1.36GB, avg file size 1.36GB
  ("fsize_db",                        15872838181), # 15.87GB, avg file size 755.85MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_500_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99981688e+05, 2.99979688e+05, 2.99981281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20091656e+05, 2.99981688e+05, 2.81474156e+05, 3.20091656e+05, 2.99981688e+05, 2.81474156e+05, 3.20091656e+05, 2.99981688e+05, 2.81474156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20092000e+05, 2.81473781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90825125e+05, 2.90814625e+05, 2.90830375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90825125e+05, 2.88629844e+05, 2.92964000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.10255438e+05, 2.90825125e+05, 2.72934688e+05, 3.10255438e+05, 2.90825125e+05, 2.72934688e+05, 3.10255438e+05, 2.90825125e+05, 2.72934688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.10255781e+05, 2.72934375e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1449096531), # 1.45GB, avg file size 1.45GB
  ("fsize_db",                        16481520657), # 16.48GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_550_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_550_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 2.99980938e+05, 2.99981469e+05, 2.99912719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22090156e+05, 2.99980938e+05, 2.79884125e+05, 3.22090156e+05, 2.99980938e+05, 2.79884125e+05, 3.22090156e+05, 2.99980938e+05, 2.79884125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22091531e+05, 2.79882750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.90197406e+05, 2.90189656e+05, 2.90164938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.90197406e+05, 2.87885312e+05, 2.92465656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.11529031e+05, 2.90197406e+05, 2.70817750e+05, 3.11529031e+05, 2.90197406e+05, 2.70817750e+05, 3.11529031e+05, 2.90197406e+05, 2.70817750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.11530406e+05, 2.70816375e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1493973020), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        16709110067), # 16.71GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_600_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_600_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 195999, ],
    'CountWeighted'                                                                  : [ 1.95990094e+05, 1.95993875e+05, 1.95981484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.11611094e+05, 1.95990094e+05, 1.81952625e+05, 2.11611094e+05, 1.95990094e+05, 1.81952625e+05, 2.11611094e+05, 1.95990094e+05, 1.81952625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.11611156e+05, 1.81952562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.89369656e+05, 1.89375797e+05, 1.89364000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.89369656e+05, 1.87813781e+05, 1.90896875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.04428172e+05, 1.89369656e+05, 1.75843094e+05, 2.04428172e+05, 1.89369656e+05, 1.75843094e+05, 2.04428172e+05, 1.89369656e+05, 1.75843094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.04428188e+05, 1.75843062e+05, ],
  }),
  ("nof_tree_events",                 195999),
  ("nof_db_events",                   195999),
  ("fsize_local",                     995854465), # 995.85MB, avg file size 995.85MB
  ("fsize_db",                        11098413315), # 11.10GB, avg file size 1.11GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_650_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_650_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99958188e+05, 1.99957578e+05, 1.99938219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17067875e+05, 1.99958188e+05, 1.84802188e+05, 2.17067875e+05, 1.99958188e+05, 1.84802188e+05, 2.17067875e+05, 1.99958188e+05, 1.84802188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17067875e+05, 1.84802188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92896375e+05, 1.92884250e+05, 1.92905578e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92896375e+05, 1.91250812e+05, 1.94515234e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.09343047e+05, 1.92896375e+05, 1.78312672e+05, 2.09343047e+05, 1.92896375e+05, 1.78312672e+05, 2.09343047e+05, 1.92896375e+05, 1.78312672e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.09343047e+05, 1.78312672e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1029555319), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11471924888), # 11.47GB, avg file size 819.42MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_700_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_700_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99997719e+05, 2.00008844e+05, 1.99966625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18036312e+05, 1.99997719e+05, 1.84073594e+05, 2.18036312e+05, 1.99997719e+05, 1.84073594e+05, 2.18036312e+05, 1.99997719e+05, 1.84073594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18036312e+05, 1.84073594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92911391e+05, 1.92910062e+05, 1.92893953e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92911391e+05, 1.91265094e+05, 1.94534281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10273531e+05, 1.92911391e+05, 1.77594406e+05, 2.10273531e+05, 1.92911391e+05, 1.77594406e+05, 2.10273531e+05, 1.92911391e+05, 1.77594406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10273531e+05, 1.77594406e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1040975952), # 1.04GB, avg file size 1.04GB
  ("fsize_db",                        11589915708), # 11.59GB, avg file size 772.66MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_750_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 192000, ],
    'CountWeighted'                                                                  : [ 1.91986516e+05, 1.91985594e+05, 1.91977766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.91986516e+05, 1.91986516e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.84948156e+05, 1.84936078e+05, 1.84956094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.84948156e+05, 1.83321250e+05, 1.86553875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.84948156e+05, 1.84948156e+05, ],
  }),
  ("nof_tree_events",                 192000),
  ("nof_db_events",                   192000),
  ("fsize_local",                     1013702990), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11585622017), # 11.59GB, avg file size 965.47MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_800_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_800_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99951688e+05, 1.99955688e+05, 1.99958094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99951688e+05, 1.99951688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92537938e+05, 1.92520031e+05, 1.92556734e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92537938e+05, 1.90827125e+05, 1.94228641e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92537938e+05, 1.92537938e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1061350128), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        12059647437), # 12.06GB, avg file size 1.51GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_850_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_850_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99966375e+05, 1.99933156e+05, 1.99983953e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99966375e+05, 1.99966375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92344031e+05, 1.92313078e+05, 1.92363000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92344031e+05, 1.90594156e+05, 1.94068781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.92344031e+05, 1.92344031e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1065055830), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        12157898020), # 12.16GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_900_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_900_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99981891e+05, 1.99987156e+05, 1.99977812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.21313812e+05, 1.99981891e+05, 1.81619125e+05, 2.21313812e+05, 1.99981891e+05, 1.81619125e+05, 2.21313812e+05, 1.99981891e+05, 1.81619125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.21313812e+05, 1.81619125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.92276281e+05, 1.92265625e+05, 1.92294969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.92276281e+05, 1.90514750e+05, 1.94018812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12747781e+05, 1.92276281e+05, 1.74669781e+05, 2.12747781e+05, 1.92276281e+05, 1.74669781e+05, 2.12747781e+05, 1.92276281e+05, 1.74669781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12747781e+05, 1.74669781e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1061996640), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11885543228), # 11.89GB, avg file size 742.85MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99630078e+04, 9.99682422e+04, 9.99854766e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11351805e+05, 9.99623359e+04, 9.03295391e+04, 1.11351805e+05, 9.99623359e+04, 9.03295391e+04, 1.11351805e+05, 9.99623359e+04, 9.03295391e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11351805e+05, 9.03295391e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59384297e+04, 9.59389688e+04, 9.59525703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59384297e+04, 9.50253203e+04, 9.68423750e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06835023e+05, 9.59375859e+04, 8.67047969e+04, 1.06835023e+05, 9.59375859e+04, 8.67047969e+04, 1.06835023e+05, 9.59375859e+04, 8.67047969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06835023e+05, 8.67047969e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     533493168), # 533.49MB, avg file size 533.49MB
  ("fsize_db",                        5933581710), # 5.93GB, avg file size 988.93MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4v"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1000_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    5),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99704922e+04, 9.99687969e+04, 9.99756328e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11333992e+05, 9.99704922e+04, 9.03258438e+04, 1.11333992e+05, 9.99704922e+04, 9.03258438e+04, 1.11333992e+05, 9.99704922e+04, 9.03258438e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11333992e+05, 9.03258438e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.73095312e+05, 3.71798406e+05, 5.30645750e+05, 3.73311625e+05, 3.54745500e+05, 2.16408750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99723047e+04, 9.97209375e+04, 1.47631281e+05, 1.00028531e+05, 1.00402812e+05, 5.79888438e+04, ],
    'CountWeightedFull'                                                              : [ 9.99389531e+04, 9.99367109e+04, 9.99443125e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.11298711e+05, 9.99389531e+04, 9.02973906e+04, 1.11298711e+05, 9.99389531e+04, 9.02973906e+04, 1.11298711e+05, 9.99389531e+04, 9.02973906e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.11298711e+05, 9.02973906e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.72982344e+05, 3.71681969e+05, 5.30477125e+05, 3.73192250e+05, 3.54631750e+05, 2.16341344e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99419219e+04, 9.96897891e+04, 1.47584172e+05, 9.99966094e+04, 1.00370422e+05, 5.79707969e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.59263438e+04, 9.59131016e+04, 9.59428672e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.59263438e+04, 9.50082656e+04, 9.68351172e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06805031e+05, 9.59263438e+04, 8.66891250e+04, 1.06805031e+05, 9.59263438e+04, 8.66891250e+04, 1.06805031e+05, 9.59263438e+04, 8.66891250e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.06805031e+05, 8.66891250e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.58511031e+05, 3.56599250e+05, 5.09227781e+05, 3.57573344e+05, 3.40735500e+05, 2.07727406e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.60581172e+04, 9.56404766e+04, 1.41666797e+05, 9.58043750e+04, 9.64277109e+04, 5.56580508e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.58963594e+04, 9.58827031e+04, 9.59132188e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.58963594e+04, 9.49785625e+04, 9.68047656e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.06771594e+05, 9.58963594e+04, 8.66620703e+04, 1.06771594e+05, 9.58963594e+04, 8.66620703e+04, 1.06771594e+05, 9.58963594e+04, 8.66620703e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.06771594e+05, 8.66620703e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.58403625e+05, 3.56489000e+05, 5.09068125e+05, 3.57460375e+05, 3.40627750e+05, 2.07663516e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.60292734e+04, 9.56109297e+04, 1.41622094e+05, 9.57741328e+04, 9.63969922e+04, 5.56409570e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     536171849), # 536.17MB, avg file size 536.17MB
  ("fsize_db",                        5973143877), # 5.97GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1000_hh_4v_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1250_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 78999, ],
    'CountWeighted'                                                                  : [ 7.89682891e+04, 7.89730469e+04, 7.89661250e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 7.89682891e+04, 7.89682891e+04, ],
    'CountWeightedPSWeight'                                                          : [ 2.75108688e+05, 2.75655938e+05, 3.93520219e+05, 2.75195219e+05, 2.61010266e+05, 1.58451156e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 7.89826250e+04, 7.91924375e+04, 1.16665945e+05, 7.90109062e+04, 7.85720234e+04, 4.54941367e+04, ],
    'CountWeightedFull'                                                              : [ 7.89411719e+04, 7.89459141e+04, 7.89391406e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 7.89411719e+04, 7.89411719e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.75017094e+05, 2.75562719e+05, 3.93385031e+05, 2.75098188e+05, 2.60920609e+05, 1.58397734e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 7.89563828e+04, 7.91654531e+04, 1.16625695e+05, 7.89829219e+04, 7.85448672e+04, 4.54787656e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 7.56836016e+04, 7.56721016e+04, 7.56949922e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 7.56836016e+04, 7.49462578e+04, 7.64158281e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 7.56836016e+04, 7.56836016e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.64061094e+05, 2.64086312e+05, 3.77129875e+05, 2.63274031e+05, 2.50357422e+05, 1.51937266e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.57962578e+04, 7.58553594e+04, 1.11801273e+05, 7.55727891e+04, 7.53613516e+04, 4.36140312e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 7.56580938e+04, 7.56465469e+04, 7.56696328e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 7.56580938e+04, 7.49210312e+04, 7.63900234e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 7.56580938e+04, 7.56580938e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.63974875e+05, 2.63998344e+05, 3.77002312e+05, 2.63182531e+05, 2.50272891e+05, 1.51887000e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 7.57714375e+04, 7.58299688e+04, 1.11763391e+05, 7.55464453e+04, 7.53357656e+04, 4.35995508e+04, ],
  }),
  ("nof_tree_events",                 78999),
  ("nof_db_events",                   78999),
  ("fsize_local",                     425208338), # 425.21MB, avg file size 425.21MB
  ("fsize_db",                        5029972001), # 5.03GB, avg file size 503.00MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1250_hh_4v_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1500_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99577578e+04, 9.99589766e+04, 9.99621250e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.13900516e+05, 9.99577578e+04, 8.85188594e+04, 1.13900516e+05, 9.99577578e+04, 8.85188594e+04, 1.13900516e+05, 9.99577578e+04, 8.85188594e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.13900672e+05, 8.85187188e+04, ],
    'CountWeightedPSWeight'                                                          : [ 3.01546938e+05, 3.01015656e+05, 4.36323156e+05, 3.01820750e+05, 2.91289688e+05, 1.72933656e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99545312e+04, 9.98021172e+04, 1.48197250e+05, 1.00044133e+05, 1.00102281e+05, 5.73259883e+04, ],
    'CountWeightedFull'                                                              : [ 9.99234609e+04, 9.99246953e+04, 9.99275312e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.13861164e+05, 9.99234609e+04, 8.84884375e+04, 1.13861164e+05, 9.99234609e+04, 8.84884375e+04, 1.13861164e+05, 9.99234609e+04, 8.84884375e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.13861312e+05, 8.84882969e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.01446438e+05, 3.00914688e+05, 4.36170938e+05, 3.01714562e+05, 2.91185312e+05, 1.72874469e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99211562e+04, 9.97685469e+04, 1.48145000e+05, 1.00008875e+05, 1.00066023e+05, 5.73063828e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.56125000e+04, 9.56036719e+04, 9.56292578e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.56125000e+04, 9.46414375e+04, 9.65771562e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08930578e+05, 9.56125000e+04, 8.46832812e+04, 1.08930578e+05, 9.56125000e+04, 8.46832812e+04, 1.08930578e+05, 9.56125000e+04, 8.46832812e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08930672e+05, 8.46832031e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.88936375e+05, 2.87862438e+05, 4.17277188e+05, 2.88074375e+05, 2.78732594e+05, 1.65499344e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.57604375e+04, 9.54276250e+04, 1.41711062e+05, 9.54740000e+04, 9.57725156e+04, 5.48522344e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.55801250e+04, 9.55712656e+04, 9.55965781e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.55801250e+04, 9.46094375e+04, 9.65442812e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.08893359e+05, 9.55801250e+04, 8.46544688e+04, 1.08893359e+05, 9.55801250e+04, 8.46544688e+04, 1.08893359e+05, 9.55801250e+04, 8.46544688e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.08893453e+05, 8.46543906e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.88841625e+05, 2.87766750e+05, 4.17133562e+05, 2.87973969e+05, 2.78634281e+05, 1.65443438e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.57288125e+04, 9.53958828e+04, 1.41661812e+05, 9.54407812e+04, 9.57383359e+04, 5.48337188e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     530848003), # 530.85MB, avg file size 530.85MB
  ("fsize_db",                        7042080075), # 7.04GB, avg file size 704.21MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1500_hh_4v_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_1750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_1750_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99461250e+04, 9.99395938e+04, 9.99493047e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99461250e+04, 9.99461250e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.89440688e+05, 5.76781875e+05, 7.85395125e+05, 5.89788938e+05, 5.11991062e+05, 3.36878906e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99615234e+04, 9.98864219e+04, 1.47841500e+05, 1.00020672e+05, 9.94037188e+04, 5.71392422e+04, ],
    'CountWeightedFull'                                                              : [ 9.99101094e+04, 9.99041250e+04, 9.99128125e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99101094e+04, 9.99101094e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.89242250e+05, 5.76577438e+05, 7.85111750e+05, 5.89577375e+05, 5.11804031e+05, 3.36762188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99279219e+04, 9.98510312e+04, 1.47788312e+05, 9.99846875e+04, 9.93673906e+04, 5.71194766e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.55509453e+04, 9.55448906e+04, 9.55586094e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.55509453e+04, 9.45760078e+04, 9.65209141e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.55509453e+04, 9.55509453e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 5.64507875e+05, 5.51281000e+05, 7.50726125e+05, 5.62686000e+05, 4.89771031e+05, 3.22294688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.57171172e+04, 9.54405938e+04, 1.41275938e+05, 9.54086875e+04, 9.50622812e+04, 5.46551875e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.55172266e+04, 9.55115469e+04, 9.55244922e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.55172266e+04, 9.45427812e+04, 9.64867656e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.55172266e+04, 9.55172266e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 5.64319750e+05, 5.51088750e+05, 7.50460688e+05, 5.62486375e+05, 4.89596188e+05, 3.22184594e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.56853438e+04, 9.54073906e+04, 1.41225875e+05, 9.53748125e+04, 9.50282344e+04, 5.46365234e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     531890793), # 531.89MB, avg file size 531.89MB
  ("fsize_db",                        6399831148), # 6.40GB, avg file size 799.98MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_1750_hh_4v_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_2000_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99245000e+04, 9.99142812e+04, 9.99352891e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.15689406e+05, 9.99213906e+04, 8.71981094e+04, 1.15689406e+05, 9.99213906e+04, 8.71981094e+04, 1.15689406e+05, 9.99213906e+04, 8.71981094e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.15690055e+05, 8.71974688e+04, ],
    'CountWeightedPSWeight'                                                          : [ 7.81885438e+05, 7.24898250e+05, 9.41357000e+05, 7.79355125e+05, 6.22621875e+05, 4.46969250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99292500e+04, 9.99922266e+04, 1.48587734e+05, 1.00083328e+05, 9.98335938e+04, 5.69974805e+04, ],
    'CountWeightedFull'                                                              : [ 9.98852500e+04, 9.98754531e+04, 9.98958750e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.15644289e+05, 9.98822031e+04, 8.71642031e+04, 1.15644289e+05, 9.98822031e+04, 8.71642031e+04, 1.15644289e+05, 9.98822031e+04, 8.71642031e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.15644938e+05, 8.71635625e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 7.81596000e+05, 7.24617000e+05, 9.40990875e+05, 7.79050625e+05, 6.22377000e+05, 4.46797562e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98923516e+04, 9.99536562e+04, 1.48530812e+05, 1.00044156e+05, 9.97950156e+04, 5.69756328e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.54696484e+04, 9.54527656e+04, 9.54858125e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.54696484e+04, 9.44847812e+04, 9.64510781e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.10517938e+05, 9.54674219e+04, 8.33219844e+04, 1.10517938e+05, 9.54674219e+04, 8.33219844e+04, 1.10517938e+05, 9.54674219e+04, 8.33219844e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10518555e+05, 8.33213672e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 7.48286062e+05, 6.92533250e+05, 8.99420500e+05, 7.43190375e+05, 5.95288625e+05, 4.27301500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.56217969e+04, 9.54785156e+04, 1.41891750e+05, 9.54132656e+04, 9.54026875e+04, 5.44773984e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.54327344e+04, 9.54159766e+04, 9.54488750e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.54327344e+04, 9.44483438e+04, 9.64136875e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.10475359e+05, 9.54305078e+04, 8.32899766e+04, 1.10475359e+05, 9.54305078e+04, 8.32899766e+04, 1.10475359e+05, 9.54305078e+04, 8.32899766e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.10475977e+05, 8.32893594e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 7.48012938e+05, 6.92269000e+05, 8.99075625e+05, 7.42904062e+05, 5.95057875e+05, 4.27139938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.55870000e+04, 9.54423125e+04, 1.41838031e+05, 9.53765156e+04, 9.53662656e+04, 5.44568359e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     529366372), # 529.37MB, avg file size 529.37MB
  ("fsize_db",                        6277909587), # 6.28GB, avg file size 570.72MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2000_hh_4v_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_2500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_2500_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.98797109e+04, 9.98824531e+04, 9.98940312e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98797109e+04, 9.98797109e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.98793750e+05, 9.78911875e+05, 9.98789250e+05, 9.98789625e+05, 9.09139250e+05, 8.89265500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99717734e+04, 9.99597422e+04, 1.49005062e+05, 1.00018742e+05, 1.00039234e+05, 5.67346875e+04, ],
    'CountWeightedFull'                                                              : [ 9.98419688e+04, 9.98451250e+04, 9.98551406e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.98419688e+04, 9.98419688e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.98411250e+05, 9.78542125e+05, 9.98411375e+05, 9.98407125e+05, 9.08796375e+05, 8.88926188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99344844e+04, 9.99188750e+04, 1.48944172e+05, 9.99790156e+04, 9.99976719e+04, 5.67128906e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.53005625e+04, 9.52974531e+04, 9.53142969e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.53005625e+04, 9.42959688e+04, 9.63025469e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.53005625e+04, 9.53005625e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.53006312e+05, 9.34016812e+05, 9.52996250e+05, 9.53002125e+05, 8.67866000e+05, 8.48895000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.55444844e+04, 9.52809219e+04, 1.42124344e+05, 9.52024844e+04, 9.55327500e+04, 5.41591797e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.52656641e+04, 9.52628281e+04, 9.52785781e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.52656641e+04, 9.42616562e+04, 9.62670781e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.52656641e+04, 9.52656641e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.52645812e+05, 9.33674062e+05, 9.52645875e+05, 9.52641625e+05, 8.67548875e+05, 8.48575562e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.55093438e+04, 9.52428281e+04, 1.42067609e+05, 9.51652109e+04, 9.54939297e+04, 5.41386797e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     531723158), # 531.72MB, avg file size 531.72MB
  ("fsize_db",                        6536657422), # 6.54GB, avg file size 817.08MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_2500_hh_4v_PSWeights"),
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

samples_2017["/GluGluToRadionToHHTo4V_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin0_3000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin0_3000_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.98035703e+04, 9.98014219e+04, 9.97890078e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.98035703e+04, 9.98035703e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.97914500e+05, 9.74085875e+05, 9.97918500e+05, 9.97904750e+05, 8.97902688e+05, 8.74058438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99369141e+04, 9.99599141e+04, 1.48782812e+05, 1.00072180e+05, 9.97509609e+04, 5.66966914e+04, ],
    'CountWeightedFull'                                                              : [ 9.97639609e+04, 9.97620156e+04, 9.97495391e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.97639609e+04, 9.97639609e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.97522438e+05, 9.73702625e+05, 9.97525125e+05, 9.97511875e+05, 8.97544688e+05, 8.73711938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98987422e+04, 9.99211016e+04, 1.48723859e+05, 1.00031750e+05, 9.97106719e+04, 5.66741562e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.51716250e+04, 9.51578438e+04, 9.51770859e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.51716250e+04, 9.41646641e+04, 9.61777969e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.51716250e+04, 9.51716250e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.51646188e+05, 9.28929125e+05, 9.51650188e+05, 9.51637438e+05, 8.56538562e+05, 8.33808125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.54506719e+04, 9.52511562e+04, 1.41846859e+05, 9.51880938e+04, 9.51814219e+04, 5.40750117e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.51345391e+04, 9.51206562e+04, 9.51401250e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.51345391e+04, 9.41280156e+04, 9.61401719e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.51345391e+04, 9.51345391e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.51277750e+05, 9.28568312e+05, 9.51280438e+05, 9.51268250e+05, 8.56202125e+05, 8.33481812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.54146562e+04, 9.52146719e+04, 1.41791469e+05, 9.51503203e+04, 9.51435156e+04, 5.40538203e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     531632069), # 531.63MB, avg file size 531.63MB
  ("fsize_db",                        7450630911), # 7.45GB, avg file size 573.13MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin0_3000_hh_4v_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-250_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_250_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 4.00014625e+05, 3.99954781e+05, 3.99984094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.04907469e+05, 4.00014625e+05, 3.92226062e+05, 4.04907469e+05, 4.00014625e+05, 3.92226062e+05, 4.04907469e+05, 4.00014625e+05, 3.92226062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04907469e+05, 3.92226062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.93165219e+05, 3.93103156e+05, 3.93168531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.93165219e+05, 3.91363656e+05, 3.94859375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.97950156e+05, 3.93165219e+05, 3.85549219e+05, 3.97950156e+05, 3.93165219e+05, 3.85549219e+05, 3.97950156e+05, 3.93165219e+05, 3.85549219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.97950156e+05, 3.85549219e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1459244189), # 1.46GB, avg file size 1.46GB
  ("fsize_db",                        20066660592), # 20.07GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-260_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_260_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_260_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 4.00006438e+05, 3.99970344e+05, 3.99987906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.06233875e+05, 4.00005500e+05, 3.91158344e+05, 4.06233875e+05, 4.00005500e+05, 3.91158344e+05, 4.06233875e+05, 4.00005500e+05, 3.91158344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.06233875e+05, 3.91158344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92837625e+05, 3.92796688e+05, 3.92843031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92837625e+05, 3.90962969e+05, 3.94602562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98924375e+05, 3.92836125e+05, 3.84187125e+05, 3.98924375e+05, 3.92836125e+05, 3.84187125e+05, 3.98924375e+05, 3.92836125e+05, 3.84187125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.98924375e+05, 3.84187125e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1490854087), # 1.49GB, avg file size 1.49GB
  ("fsize_db",                        19879949428), # 19.88GB, avg file size 994.00MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-270_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_270_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_270_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99952156e+05, 3.99938344e+05, 3.99997500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.07518438e+05, 3.99952156e+05, 3.90144750e+05, 4.07518438e+05, 3.99952156e+05, 3.90144750e+05, 4.07518438e+05, 3.99952156e+05, 3.90144750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.07518438e+05, 3.90144750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.92566125e+05, 3.92534719e+05, 3.92615562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.92566125e+05, 3.90637156e+05, 3.94387000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.99940750e+05, 3.92566125e+05, 3.82962438e+05, 3.99940750e+05, 3.92566125e+05, 3.82962438e+05, 3.99940750e+05, 3.92566125e+05, 3.82962438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.99940750e+05, 3.82962438e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1519704538), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        20200851289), # 20.20GB, avg file size 961.95MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-280_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_280_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_280_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 391999, ],
    'CountWeighted'                                                                  : [ 3.91963062e+05, 3.91926906e+05, 3.91970312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.00557281e+05, 3.91963062e+05, 3.81389656e+05, 4.00557281e+05, 3.91963062e+05, 3.81389656e+05, 4.00557281e+05, 3.91963062e+05, 3.81389656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00557281e+05, 3.81389656e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.84316719e+05, 3.84280938e+05, 3.84320000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.84316719e+05, 3.82339969e+05, 3.86186375e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.92695656e+05, 3.84316719e+05, 3.73982000e+05, 3.92695656e+05, 3.84316719e+05, 3.73982000e+05, 3.92695656e+05, 3.84316719e+05, 3.73982000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92695656e+05, 3.73982000e+05, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     1519834815), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        19893233798), # 19.89GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-300_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_300_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_300_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 383998, ],
    'CountWeighted'                                                                  : [ 3.83900281e+05, 3.83940625e+05, 3.84001719e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.94554625e+05, 3.83900281e+05, 3.71885875e+05, 3.94554625e+05, 3.83900281e+05, 3.71885875e+05, 3.94554625e+05, 3.83900281e+05, 3.71885875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.94554625e+05, 3.71885875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75910031e+05, 3.75918844e+05, 3.75995656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75910031e+05, 3.73868812e+05, 3.77855938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.86271000e+05, 3.75910031e+05, 3.64161812e+05, 3.86271000e+05, 3.75910031e+05, 3.64161812e+05, 3.86271000e+05, 3.75910031e+05, 3.64161812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86271000e+05, 3.64161812e+05, ],
  }),
  ("nof_tree_events",                 383998),
  ("nof_db_events",                   383998),
  ("fsize_local",                     1549484304), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        19708482041), # 19.71GB, avg file size 985.42MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-320_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_320_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_320_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99983594e+05, 2.99945938e+05, 3.00008094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.09819125e+05, 2.99983594e+05, 2.89293062e+05, 3.09819125e+05, 2.99983594e+05, 2.89293062e+05, 3.09819125e+05, 2.99983594e+05, 2.89293062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.09819594e+05, 2.89292594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.93359250e+05, 2.93323125e+05, 2.93388125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.93359250e+05, 2.91690000e+05, 2.94957625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.02939781e+05, 2.93359250e+05, 2.82944000e+05, 3.02939781e+05, 2.93359250e+05, 2.82944000e+05, 3.02939781e+05, 2.93359250e+05, 2.82944000e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.02940125e+05, 2.82943688e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1251335063), # 1.25GB, avg file size 1.25GB
  ("fsize_db",                        15656023835), # 15.66GB, avg file size 1.20GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-350_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_350_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_350_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 299999, ],
    'CountWeighted'                                                                  : [ 2.99948625e+05, 3.00021938e+05, 2.99978375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.11994344e+05, 2.99948625e+05, 2.87634438e+05, 3.11994344e+05, 2.99948625e+05, 2.87634438e+05, 3.11994344e+05, 2.99948625e+05, 2.87634438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.11994344e+05, 2.87634438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92808438e+05, 2.92851250e+05, 2.92834375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92808438e+05, 2.91034344e+05, 2.94520000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.04505719e+05, 2.92808438e+05, 2.80817625e+05, 3.04505719e+05, 2.92808438e+05, 2.80817625e+05, 3.04505719e+05, 2.92808438e+05, 2.80817625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.04505719e+05, 2.80817625e+05, ],
  }),
  ("nof_tree_events",                 299999),
  ("nof_db_events",                   299999),
  ("fsize_local",                     1313117405), # 1.31GB, avg file size 1.31GB
  ("fsize_db",                        16009029568), # 16.01GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-400_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_400_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_400_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 300000, ],
    'CountWeighted'                                                                  : [ 2.99961219e+05, 2.99948719e+05, 2.99978406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.15114281e+05, 2.99961219e+05, 2.85299188e+05, 3.15114281e+05, 2.99961219e+05, 2.85299188e+05, 3.15114281e+05, 2.99961219e+05, 2.85299188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.15114281e+05, 2.85299188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.92122781e+05, 2.92107906e+05, 2.92141812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.92122781e+05, 2.90216375e+05, 2.93975562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.06817125e+05, 2.92122781e+05, 2.77884125e+05, 3.06817125e+05, 2.92122781e+05, 2.77884125e+05, 3.06817125e+05, 2.92122781e+05, 2.77884125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.06817125e+05, 2.77884125e+05, ],
  }),
  ("nof_tree_events",                 300000),
  ("nof_db_events",                   300000),
  ("fsize_local",                     1393235442), # 1.39GB, avg file size 1.39GB
  ("fsize_db",                        16480100060), # 16.48GB, avg file size 915.56MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-450_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_450_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_450_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 287998, ],
    'CountWeighted'                                                                  : [ 2.87999781e+05, 2.87963281e+05, 2.87965562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.05060562e+05, 2.87999781e+05, 2.71898625e+05, 3.05060562e+05, 2.87999781e+05, 2.71898625e+05, 3.05060562e+05, 2.87999781e+05, 2.71898625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.05060562e+05, 2.71898625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.79988062e+05, 2.79956062e+05, 2.79967750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.79988062e+05, 2.78074188e+05, 2.81857656e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.96519500e+05, 2.79988062e+05, 2.64399094e+05, 2.96519500e+05, 2.79988062e+05, 2.64399094e+05, 2.96519500e+05, 2.79988062e+05, 2.64399094e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.96519500e+05, 2.64399094e+05, ],
  }),
  ("nof_tree_events",                 287998),
  ("nof_db_events",                   287998),
  ("fsize_local",                     1401638942), # 1.40GB, avg file size 1.40GB
  ("fsize_db",                        16214133807), # 16.21GB, avg file size 953.77MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-500_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_500_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 299997, ],
    'CountWeighted'                                                                  : [ 2.99986281e+05, 2.99985125e+05, 2.99932500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.20048000e+05, 2.99986281e+05, 2.81478594e+05, 3.20048000e+05, 2.99986281e+05, 2.81478594e+05, 3.20048000e+05, 2.99986281e+05, 2.81478594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.20048000e+05, 2.81478594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91339906e+05, 2.91327219e+05, 2.91328062e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91339906e+05, 2.89304062e+05, 2.93339250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.10762688e+05, 2.91339906e+05, 2.73424625e+05, 3.10762688e+05, 2.91339906e+05, 2.73424625e+05, 3.10762688e+05, 2.91339906e+05, 2.73424625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.10762688e+05, 2.73424625e+05, ],
  }),
  ("nof_tree_events",                 299997),
  ("nof_db_events",                   299997),
  ("fsize_local",                     1515692238), # 1.52GB, avg file size 1.52GB
  ("fsize_db",                        17053053622), # 17.05GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-550_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_550_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_550_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 299998, ],
    'CountWeighted'                                                                  : [ 3.00039062e+05, 3.00037688e+05, 2.99930750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.22091188e+05, 3.00039062e+05, 2.79875125e+05, 3.22091188e+05, 3.00039062e+05, 2.79875125e+05, 3.22091188e+05, 3.00039062e+05, 2.79875125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.22091562e+05, 2.79874750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 2.91187562e+05, 2.91169281e+05, 2.91124875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 2.91187562e+05, 2.89119188e+05, 2.93212938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.12536031e+05, 2.91187562e+05, 2.71696500e+05, 3.12536031e+05, 2.91187562e+05, 2.71696500e+05, 3.12536031e+05, 2.91187562e+05, 2.71696500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.12536281e+05, 2.71696250e+05, ],
  }),
  ("nof_tree_events",                 299998),
  ("nof_db_events",                   299998),
  ("fsize_local",                     1554471753), # 1.55GB, avg file size 1.55GB
  ("fsize_db",                        17210955077), # 17.21GB, avg file size 1.43GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-600_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_600_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_600_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 191998, ],
    'CountWeighted'                                                                  : [ 1.92007266e+05, 1.92023906e+05, 1.91961812e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.07321891e+05, 1.92007266e+05, 1.78227969e+05, 2.07321891e+05, 1.92007266e+05, 1.78227969e+05, 2.07321891e+05, 1.92007266e+05, 1.78227969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.07321891e+05, 1.78227969e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86311219e+05, 1.86306953e+05, 1.86297500e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86311219e+05, 1.84989688e+05, 1.87612281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.01130391e+05, 1.86311219e+05, 1.72985906e+05, 2.01130391e+05, 1.86311219e+05, 1.72985906e+05, 2.01130391e+05, 1.86311219e+05, 1.72985906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.01130391e+05, 1.72985906e+05, ],
  }),
  ("nof_tree_events",                 191998),
  ("nof_db_events",                   191998),
  ("fsize_local",                     1011551932), # 1.01GB, avg file size 1.01GB
  ("fsize_db",                        11180869047), # 11.18GB, avg file size 860.07MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-650_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_650_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_650_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 200000, ],
    'CountWeighted'                                                                  : [ 1.99957688e+05, 2.00016219e+05, 1.99953344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.17069391e+05, 1.99957234e+05, 1.84853797e+05, 2.17069391e+05, 1.99957234e+05, 1.84853797e+05, 2.17069391e+05, 1.99957234e+05, 1.84853797e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.17069391e+05, 1.84853797e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93935734e+05, 1.93967609e+05, 1.93933891e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93935734e+05, 1.92544422e+05, 1.95309219e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.10468844e+05, 1.93934953e+05, 1.79311625e+05, 2.10468844e+05, 1.93934953e+05, 1.79311625e+05, 2.10468844e+05, 1.93934953e+05, 1.79311625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.10468844e+05, 1.79311625e+05, ],
  }),
  ("nof_tree_events",                 200000),
  ("nof_db_events",                   200000),
  ("fsize_local",                     1064750918), # 1.06GB, avg file size 1.06GB
  ("fsize_db",                        11726047160), # 11.73GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-700_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_700_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_700_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 191999, ],
    'CountWeighted'                                                                  : [ 1.91987531e+05, 1.91988969e+05, 1.92020781e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.09349641e+05, 1.91986688e+05, 1.76704547e+05, 2.09349641e+05, 1.91986688e+05, 1.76704547e+05, 2.09349641e+05, 1.91986688e+05, 1.76704547e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.09349641e+05, 1.76704547e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.86285281e+05, 1.86281625e+05, 1.86311812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.86285281e+05, 1.84972703e+05, 1.87581031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.03084453e+05, 1.86284281e+05, 1.71493812e+05, 2.03084453e+05, 1.86284281e+05, 1.71493812e+05, 2.03084453e+05, 1.86284281e+05, 1.71493812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.03084453e+05, 1.71493812e+05, ],
  }),
  ("nof_tree_events",                 191999),
  ("nof_db_events",                   191999),
  ("fsize_local",                     1027815199), # 1.03GB, avg file size 1.03GB
  ("fsize_db",                        11310227020), # 11.31GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-750_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_750_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 199997, ],
    'CountWeighted'                                                                  : [ 1.99977562e+05, 1.99959281e+05, 1.99965031e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.18966062e+05, 1.99977562e+05, 1.83370641e+05, 2.18966062e+05, 1.99977562e+05, 1.83370641e+05, 2.18966062e+05, 1.99977562e+05, 1.83370641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.18966062e+05, 1.83370641e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.93981750e+05, 1.93957703e+05, 1.93983000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.93981750e+05, 1.92604812e+05, 1.95336625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.12353438e+05, 1.93981750e+05, 1.77907219e+05, 2.12353438e+05, 1.93981750e+05, 1.77907219e+05, 2.12353438e+05, 1.93981750e+05, 1.77907219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.12353438e+05, 1.77907219e+05, ],
  }),
  ("nof_tree_events",                 199997),
  ("nof_db_events",                   199997),
  ("fsize_local",                     1074773837), # 1.07GB, avg file size 1.07GB
  ("fsize_db",                        11817475227), # 11.82GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-800_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_800_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_800_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 199998, ],
    'CountWeighted'                                                                  : [ 1.99978594e+05, 1.99932406e+05, 1.99967594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 2.19772969e+05, 1.99977625e+05, 1.82732344e+05, 2.19772969e+05, 1.99977625e+05, 1.82732344e+05, 2.19772969e+05, 1.99977625e+05, 1.82732344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 2.19773203e+05, 1.82732094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94000766e+05, 1.93956328e+05, 1.93999406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94000766e+05, 1.92633641e+05, 1.95347969e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 2.13169188e+05, 1.93999875e+05, 1.77306062e+05, 2.13169188e+05, 1.93999875e+05, 1.77306062e+05, 2.13169188e+05, 1.93999875e+05, 1.77306062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 2.13169250e+05, 1.77306016e+05, ],
  }),
  ("nof_tree_events",                 199998),
  ("nof_db_events",                   199998),
  ("fsize_local",                     1076482557), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        11932391412), # 11.93GB, avg file size 701.91MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-850_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_850_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_850_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 199999, ],
    'CountWeighted'                                                                  : [ 1.99950469e+05, 1.99956031e+05, 1.99983531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.99950469e+05, 1.99950469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 1.94040750e+05, 1.94034234e+05, 1.94073031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 1.94040750e+05, 1.92688094e+05, 1.95373531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.94040750e+05, 1.94040750e+05, ],
  }),
  ("nof_tree_events",                 199999),
  ("nof_db_events",                   199999),
  ("fsize_local",                     1083724599), # 1.08GB, avg file size 1.08GB
  ("fsize_db",                        12455825050), # 12.46GB, avg file size 958.14MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-900_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_900_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_900_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99866562e+04, 9.99833516e+04, 9.99901641e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.10549570e+05, 9.99866562e+04, 9.09819844e+04, 1.10549570e+05, 9.99866562e+04, 9.09819844e+04, 1.10549570e+05, 9.99866562e+04, 9.09819844e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.10549570e+05, 9.09819844e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71242656e+04, 9.71228984e+04, 9.71265547e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71242656e+04, 9.64678984e+04, 9.77721953e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07363617e+05, 9.71242656e+04, 8.83851016e+04, 1.07363617e+05, 9.71242656e+04, 8.83851016e+04, 1.07363617e+05, 9.71242656e+04, 8.83851016e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07363617e+05, 8.83851016e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     540678583), # 540.68MB, avg file size 540.68MB
  ("fsize_db",                        6157522996), # 6.16GB, avg file size 769.69MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-1000_narrow_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99917344e+04, 9.99856641e+04, 9.99733359e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.11347883e+05, 9.99917344e+04, 9.03333828e+04, 1.11347883e+05, 9.99917344e+04, 9.03333828e+04, 1.11347883e+05, 9.99917344e+04, 9.03333828e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.11347883e+05, 9.03333828e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70476406e+04, 9.70427578e+04, 9.70298906e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70476406e+04, 9.63770469e+04, 9.77081562e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.08057453e+05, 9.70476406e+04, 8.76858516e+04, 1.08057453e+05, 9.70476406e+04, 8.76858516e+04, 1.08057453e+05, 9.70476406e+04, 8.76858516e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.08057453e+05, 8.76858516e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     538964916), # 538.96MB, avg file size 538.96MB
  ("fsize_db",                        6189551070), # 6.19GB, avg file size 773.69MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4v"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-1000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1000_hh_4v_PSWeights"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99875801e+04, 9.99936777e+04, 9.99924141e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99875801e+04, 9.99875801e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99933531e+05, 9.99933531e+05, 9.99933531e+05, 9.99933531e+05, 9.99933531e+05, 9.99933531e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99295625e+04, 9.98906270e+04, 1.47770359e+05, 1.00081525e+05, 1.00224287e+05, 5.78633184e+04, ],
    'CountWeightedFull'                                                              : [ 9.99550430e+04, 9.99607871e+04, 9.99595762e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99550430e+04, 9.99550430e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99605344e+05, 9.99605344e+05, 9.99605344e+05, 9.99605344e+05, 9.99605344e+05, 9.99605344e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98982031e+04, 9.98584688e+04, 1.47721621e+05, 1.00048203e+05, 1.00190770e+05, 5.78444961e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69893359e+04, 9.69945488e+04, 9.69879473e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69893359e+04, 9.63078887e+04, 9.76619824e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.69893359e+04, 9.69893359e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.69937531e+05, 9.69937531e+05, 9.69937531e+05, 9.69937531e+05, 9.69937531e+05, 9.69937531e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.70863574e+04, 9.68625469e+04, 1.43318121e+05, 9.68858789e+04, 9.72871133e+04, 5.61655186e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69580488e+04, 9.69629277e+04, 9.69564297e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69580488e+04, 9.62769004e+04, 9.76303945e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.69580488e+04, 9.69580488e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.70561445e+04, 9.68317188e+04, 1.43271492e+05, 9.68539746e+04, 9.72549238e+04, 5.61474570e+04, ],
  }),
  ("nof_tree_events",                 99998),
  ("nof_db_events",                   99998),
  ("fsize_local",                     522022005), # 522.02MB, avg file size 261.01MB
  ("fsize_db",                        6549987247), # 6.55GB, avg file size 595.45MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1000_hh_4v_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-1250_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1250_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1250_hh_4v_PSWeights"),
  ("nof_files",                       3),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99962969e+04, 9.99967891e+04, 9.99967822e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99962969e+04, 9.99962969e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99960828e+05, 9.99960828e+05, 9.99960828e+05, 9.99960828e+05, 9.99960828e+05, 9.99960828e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99013887e+04, 1.00060405e+05, 1.47207572e+05, 1.00117998e+05, 9.91383154e+04, 5.76371475e+04, ],
    'CountWeightedFull'                                                              : [ 9.99619512e+04, 9.99623867e+04, 9.99624912e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99619512e+04, 9.99619512e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99616812e+05, 9.99616812e+05, 9.99616812e+05, 9.99616812e+05, 9.99616812e+05, 9.99616812e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98679248e+04, 1.00026123e+05, 1.47156412e+05, 1.00082557e+05, 9.91039961e+04, 5.76174248e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71053115e+04, 9.70969043e+04, 9.71166289e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71053115e+04, 9.64482910e+04, 9.77528486e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71053115e+04, 9.71053115e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.71052969e+05, 9.71052969e+05, 9.71052969e+05, 9.71052969e+05, 9.71052969e+05, 9.71052969e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.71778145e+04, 9.71489873e+04, 1.42902213e+05, 9.70161211e+04, 9.62988320e+04, 5.60073809e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70722910e+04, 9.70638213e+04, 9.70836465e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70722910e+04, 9.64155420e+04, 9.77195244e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70722910e+04, 9.70722910e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70722031e+05, 9.70722031e+05, 9.70722031e+05, 9.70722031e+05, 9.70722031e+05, 9.70722031e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.71455449e+04, 9.71160352e+04, 1.42853055e+05, 9.69821123e+04, 9.62657451e+04, 5.59883955e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     515923051), # 515.92MB, avg file size 171.97MB
  ("fsize_db",                        6613981103), # 6.61GB, avg file size 472.43MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1250_hh_4v_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-1500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1500_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99978906e+04, 9.99938672e+04, 1.00000203e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99978906e+04, 9.99978906e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99955688e+05, 9.99964625e+05, 9.99964625e+05, 9.99956500e+05, 9.99964625e+05, 9.99955688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00004047e+05, 1.00114125e+05, 1.48262000e+05, 9.99874609e+04, 9.97386875e+04, 5.72100078e+04, ],
    'CountWeightedFull'                                                              : [ 9.99618125e+04, 9.99579609e+04, 9.99642500e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99618125e+04, 9.99618125e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99602125e+05, 9.99602125e+05, 9.99602125e+05, 9.99602125e+05, 9.99602125e+05, 9.99602125e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99705234e+04, 1.00078773e+05, 1.48209625e+05, 9.99523281e+04, 9.97028750e+04, 5.71904219e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70449688e+04, 9.70393906e+04, 9.70465156e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70449688e+04, 9.63758516e+04, 9.77039062e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70449688e+04, 9.70449688e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70439375e+05, 9.70441375e+05, 9.70441375e+05, 9.70440125e+05, 9.70441375e+05, 9.70439375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72243750e+04, 9.71344688e+04, 1.43848562e+05, 9.68187344e+04, 9.68330625e+04, 5.55511953e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70111094e+04, 9.70057031e+04, 9.70126562e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70111094e+04, 9.63423750e+04, 9.76696406e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70111094e+04, 9.70111094e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70101625e+05, 9.70101625e+05, 9.70101625e+05, 9.70101625e+05, 9.70101625e+05, 9.70101625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.71922188e+04, 9.71011719e+04, 1.43799094e+05, 9.67850781e+04, 9.67994922e+04, 5.55324258e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     506842934), # 506.84MB, avg file size 506.84MB
  ("fsize_db",                        7251061993), # 7.25GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1500_hh_4v_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-1750_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_1750_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_1750_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 97000, ],
    'CountWeighted'                                                                  : [ 9.70034844e+04, 9.70045000e+04, 9.69980156e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.70034844e+04, 9.70034844e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.69971312e+05, 9.69971312e+05, 9.69971312e+05, 9.69971312e+05, 9.69971312e+05, 9.69971312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.70753750e+04, 9.70487812e+04, 1.44091031e+05, 9.69019922e+04, 9.68298203e+04, 5.52930742e+04, ],
    'CountWeightedFull'                                                              : [ 9.69690000e+04, 9.69696875e+04, 9.69639531e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.69690000e+04, 9.69690000e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.69628438e+05, 9.69628438e+05, 9.69628438e+05, 9.69628438e+05, 9.69628438e+05, 9.69628438e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.70418828e+04, 9.70145234e+04, 1.44039750e+05, 9.68666484e+04, 9.67953594e+04, 5.52735469e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.41322656e+04, 9.41335469e+04, 9.41299297e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.41322656e+04, 9.34814844e+04, 9.47732344e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.41322656e+04, 9.41322656e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.41271500e+05, 9.41271500e+05, 9.41271500e+05, 9.41271500e+05, 9.41271500e+05, 9.41271500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.43738359e+04, 9.41483359e+04, 1.39789688e+05, 9.38187891e+04, 9.40075156e+04, 5.36847383e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.40993047e+04, 9.41003438e+04, 9.40971641e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.40993047e+04, 9.34487969e+04, 9.47399453e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.40993047e+04, 9.40993047e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.40942562e+05, 9.40942562e+05, 9.40942562e+05, 9.40942562e+05, 9.40942562e+05, 9.40942562e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.43417031e+04, 9.41156172e+04, 1.39740578e+05, 9.37850391e+04, 9.39743203e+04, 5.36659961e+04, ],
  }),
  ("nof_tree_events",                 97000),
  ("nof_db_events",                   97000),
  ("fsize_local",                     487341630), # 487.34MB, avg file size 487.34MB
  ("fsize_db",                        6392184600), # 6.39GB, avg file size 456.58MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_1750_hh_4v_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-2000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_2000_hh_4v_PSWeights"),
  ("nof_files",                       3),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99958574e+04, 9.99975586e+04, 9.99959277e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99958574e+04, 9.99958574e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99978734e+05, 9.99978734e+05, 9.99978734e+05, 9.99978734e+05, 9.99978734e+05, 9.99978734e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00013613e+05, 9.99071797e+04, 1.48690477e+05, 9.99890469e+04, 9.99237852e+04, 5.68759062e+04, ],
    'CountWeightedFull'                                                              : [ 9.99568008e+04, 9.99585879e+04, 9.99567227e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99568008e+04, 9.99568008e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99586922e+05, 9.99586922e+05, 9.99586922e+05, 9.99586922e+05, 9.99586922e+05, 9.99586922e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99774336e+04, 9.98681055e+04, 1.48631348e+05, 9.99508047e+04, 9.98840332e+04, 5.68549570e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70763574e+04, 9.70686602e+04, 9.70895684e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70763574e+04, 9.64103047e+04, 9.77306328e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70763574e+04, 9.70763574e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70775859e+05, 9.70775859e+05, 9.70775859e+05, 9.70775859e+05, 9.70775859e+05, 9.70775859e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72671465e+04, 9.69477656e+04, 1.44339889e+05, 9.68535391e+04, 9.70895156e+04, 5.52481211e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70393398e+04, 9.70318203e+04, 9.70523516e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70393398e+04, 9.63737520e+04, 9.76931680e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70393398e+04, 9.70393398e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70404969e+05, 9.70404969e+05, 9.70404969e+05, 9.70404969e+05, 9.70404969e+05, 9.70404969e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72324004e+04, 9.69105703e+04, 1.44283922e+05, 9.68169336e+04, 9.70521270e+04, 5.52279863e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     503680592), # 503.68MB, avg file size 167.89MB
  ("fsize_db",                        6688028547), # 6.69GB, avg file size 418.00MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2000_hh_4v_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-2500_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_2500_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_2500_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 1.00001906e+05, 1.00003680e+05, 1.00004742e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.00001906e+05, 1.00001906e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.99972500e+05, 9.99974000e+05, 9.99974000e+05, 9.99972062e+05, 9.99974000e+05, 9.99972062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98986328e+04, 1.00215719e+05, 1.48495484e+05, 1.00112445e+05, 9.92089922e+04, 5.66949297e+04, ],
    'CountWeightedFull'                                                              : [ 9.99590781e+04, 9.99609531e+04, 9.99622031e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99590781e+04, 9.99590781e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99552375e+05, 9.99552375e+05, 9.99552375e+05, 9.99552375e+05, 9.99552375e+05, 9.99552375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98613438e+04, 1.00173523e+05, 1.48432312e+05, 1.00072609e+05, 9.91665938e+04, 5.66730156e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70115625e+04, 9.69998984e+04, 9.70232734e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70115625e+04, 9.63313438e+04, 9.76806484e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70115625e+04, 9.70115625e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70084875e+05, 9.70086250e+05, 9.70086250e+05, 9.70084500e+05, 9.70086250e+05, 9.70084500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.70913594e+04, 9.71836641e+04, 1.43991000e+05, 9.68958047e+04, 9.62605703e+04, 5.50321797e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69707188e+04, 9.69590781e+04, 9.69825469e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69707188e+04, 9.62908594e+04, 9.76393906e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.69707188e+04, 9.69707188e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.69681375e+05, 9.69681375e+05, 9.69681375e+05, 9.69681375e+05, 9.69681375e+05, 9.69681375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.70554688e+04, 9.71432578e+04, 1.43930516e+05, 9.68576797e+04, 9.62198281e+04, 5.50111172e+04, ],
  }),
  ("nof_tree_events",                 99999),
  ("nof_db_events",                   99999),
  ("fsize_local",                     500731456), # 500.73MB, avg file size 500.73MB
  ("fsize_db",                        6615307441), # 6.62GB, avg file size 826.91MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_2500_hh_4v_PSWeights"),
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

samples_2017["/GluGluToBulkGravitonToHHTo4V_M-3000_narrow_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_spin2_3000_hh_wwww"),
  ("process_name_specific",           "signal_ggf_spin2_3000_hh_4v_PSWeights"),
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99947656e+04, 1.00001875e+05, 9.99950000e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99947656e+04, 9.99947656e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99968750e+05, 9.99968750e+05, 9.99968750e+05, 9.99968750e+05, 9.99968750e+05, 9.99968750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.98809219e+04, 9.98932188e+04, 1.48367469e+05, 1.00113797e+05, 9.94723828e+04, 5.67549844e+04, ],
    'CountWeightedFull'                                                              : [ 9.99529688e+04, 9.99599141e+04, 9.99535000e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99529688e+04, 9.99529688e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99556188e+05, 9.99556188e+05, 9.99556188e+05, 9.99556188e+05, 9.99556188e+05, 9.99556188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98426797e+04, 9.98500938e+04, 1.48305453e+05, 1.00073211e+05, 9.94324844e+04, 5.67325898e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69945859e+04, 9.69952500e+04, 9.69978672e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69945859e+04, 9.63081797e+04, 9.76687734e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.69945859e+04, 9.69945859e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.69957188e+05, 9.69957188e+05, 9.69957188e+05, 9.69957188e+05, 9.69957188e+05, 9.69957188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.70573672e+04, 9.68550469e+04, 1.43886359e+05, 9.68934688e+04, 9.65389531e+04, 5.50812266e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69551016e+04, 9.69556172e+04, 9.69585859e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69551016e+04, 9.62692500e+04, 9.76287891e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.69551016e+04, 9.69551016e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.69566188e+05, 9.69566188e+05, 9.69566188e+05, 9.69566188e+05, 9.69566188e+05, 9.69566188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.70207344e+04, 9.68150156e+04, 1.43828234e+05, 9.68547500e+04, 9.65007578e+04, 5.50599297e+04, ],
  }),
  ("nof_tree_events",                 100000),
  ("nof_db_events",                   100000),
  ("fsize_local",                     502523357), # 502.52MB, avg file size 502.52MB
  ("fsize_db",                        7538473155), # 7.54GB, avg file size 685.32MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_spin2_3000_hh_4v_PSWeights"),
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

samples_2017["/VBFHHTo4T_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00033219e+05, 3.99996016e+05, 4.00030422e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00033219e+05, 4.00033219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99983725e+06, 3.99988725e+06, 3.99988725e+06, 3.99983725e+06, 3.99988725e+06, 3.99983350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99872672e+05, 4.00079250e+05, 5.37982781e+05, 4.00023453e+05, 4.00065375e+05, 2.73806938e+05, ],
    'CountWeightedFull'                                                              : [ 3.99837500e+05, 3.99803016e+05, 3.99835016e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99837500e+05, 3.99837500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99737641e+05, 3.99884859e+05, 5.37719781e+05, 3.99888688e+05, 3.99867672e+05, 2.73715375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.72293047e+05, 3.72251938e+05, 3.72315109e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.72293047e+05, 3.65904328e+05, 3.78650156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72293047e+05, 3.72293047e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.72273838e+06, 3.72278488e+06, 3.72278488e+06, 3.72273825e+06, 3.72278488e+06, 3.72273475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.72196672e+05, 3.72179938e+05, 5.00416812e+05, 3.72261469e+05, 3.72620234e+05, 2.55182625e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.72116750e+05, 3.72077219e+05, 3.72138422e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.72116750e+05, 3.65732125e+05, 3.78469625e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.72116750e+05, 3.72116750e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.72074125e+05, 3.72004359e+05, 5.00178297e+05, 3.72139547e+05, 3.72440719e+05, 2.55099688e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1649525985), # 1.65GB, avg file size 824.76MB
  ("fsize_db",                        24223283374), # 24.22GB, avg file size 2.20GB
  ("use_it",                          True),
  ("xsection",                        6.785e-06),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_4t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4T_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.96006273e+05, 3.96005461e+05, 3.96023328e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96006273e+05, 3.96006273e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95986944e+06, 3.95989281e+06, 3.95989281e+06, 3.95987069e+06, 3.95989281e+06, 3.95986944e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95894891e+05, 3.95631789e+05, 5.36959305e+05, 3.96009727e+05, 3.96823180e+05, 2.67684918e+05, ],
    'CountWeightedFull'                                                              : [ 3.95811219e+05, 3.95811312e+05, 3.95826609e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95811219e+05, 3.95811219e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95795544e+06, 3.95795544e+06, 3.95795544e+06, 3.95795544e+06, 3.95795544e+06, 3.95795544e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95748328e+05, 3.95440562e+05, 5.36698289e+05, 3.95861781e+05, 3.96624539e+05, 2.67586484e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.62100695e+05, 3.62043922e+05, 3.62147547e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.62100695e+05, 3.54537969e+05, 3.69676828e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.62100695e+05, 3.62100695e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.62093562e+06, 3.62095669e+06, 3.62095669e+06, 3.62093669e+06, 3.62095669e+06, 3.62093562e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.62050203e+05, 3.61571047e+05, 4.90678234e+05, 3.62048734e+05, 3.63145109e+05, 2.45149617e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.61926453e+05, 3.61870078e+05, 3.61971727e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.61926453e+05, 3.54368070e+05, 3.69497914e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.61926453e+05, 3.61926453e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.61919125e+05, 3.61399570e+05, 4.90444547e+05, 3.61916617e+05, 3.62967023e+05, 2.45061391e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1746715628), # 1.75GB, avg file size 436.68MB
  ("fsize_db",                        24703273195), # 24.70GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        5.5932e-06),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_4t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4T_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       5),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 397000, ],
    'CountWeighted'                                                                  : [ 3.97000617e+05, 3.96995922e+05, 3.96989117e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.97000617e+05, 3.97000617e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.96975447e+06, 3.96981344e+06, 3.96981344e+06, 3.96975100e+06, 3.96981344e+06, 3.96975034e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96865398e+05, 3.96634348e+05, 5.35286445e+05, 3.96911279e+05, 3.97049105e+05, 2.70080662e+05, ],
    'CountWeightedFull'                                                              : [ 3.96741674e+05, 3.96736984e+05, 3.96729285e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96741674e+05, 3.96741674e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96722641e+06, 3.96722641e+06, 3.96722641e+06, 3.96722641e+06, 3.96722641e+06, 3.96722641e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96710969e+05, 3.96376066e+05, 5.34941938e+05, 3.96757234e+05, 3.96789422e+05, 2.69975938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.68299707e+05, 3.68223945e+05, 3.68370836e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.68299707e+05, 3.61981246e+05, 3.74632717e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.68299707e+05, 3.68299707e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.68284888e+06, 3.68290094e+06, 3.68290094e+06, 3.68284547e+06, 3.68290094e+06, 3.68284484e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.68222375e+05, 3.67698527e+05, 4.96317051e+05, 3.68163307e+05, 3.68798502e+05, 2.50976713e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.68068711e+05, 3.67993340e+05, 3.68138754e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.68068711e+05, 3.61756121e+05, 3.74395773e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.68068711e+05, 3.68068711e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.68059206e+06, 3.68059206e+06, 3.68059206e+06, 3.68059206e+06, 3.68059206e+06, 3.68059206e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.68082775e+05, 3.67468027e+05, 4.96011340e+05, 3.68023949e+05, 3.68568281e+05, 2.50881859e+05, ],
  }),
  ("nof_tree_events",                 397000),
  ("nof_db_events",                   397000),
  ("fsize_local",                     1984147585), # 1.98GB, avg file size 396.83MB
  ("fsize_db",                        24795263904), # 24.80GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        5.5891e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Nov03_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_4t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4T_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00010469e+05, 4.00016578e+05, 3.99977781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00010469e+05, 4.00010469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99996812e+06, 3.99999200e+06, 3.99999200e+06, 3.99996450e+06, 3.99999200e+06, 3.99996438e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99902938e+05, 3.99853484e+05, 5.37576281e+05, 3.99988562e+05, 4.00538781e+05, 2.74464609e+05, ],
    'CountWeightedFull'                                                              : [ 3.99835516e+05, 3.99840688e+05, 3.99804016e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99835516e+05, 3.99835516e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99772766e+05, 3.99677719e+05, 5.37342516e+05, 3.99858047e+05, 4.00364109e+05, 2.74376219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76072328e+05, 3.76032750e+05, 3.76095406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76072328e+05, 3.70487344e+05, 3.81608234e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76072328e+05, 3.76072328e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.76064825e+06, 3.76067125e+06, 3.76067125e+06, 3.76064475e+06, 3.76067125e+06, 3.76064475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.76006469e+05, 3.75756188e+05, 5.05197922e+05, 3.76025188e+05, 3.76872359e+05, 2.58352461e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75911312e+05, 3.75871141e+05, 3.75935109e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75911312e+05, 3.70329688e+05, 3.81443953e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.75911312e+05, 3.75911312e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75886797e+05, 3.75595141e+05, 5.04983031e+05, 3.75905109e+05, 3.76710891e+05, 2.58270984e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1647832603), # 1.65GB, avg file size 823.92MB
  ("fsize_db",                        23200715448), # 23.20GB, avg file size 2.32GB
  ("use_it",                          True),
  ("xsection",                        1.81178e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_4t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4T_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99993961e+05, 4.00012668e+05, 4.00005184e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99993961e+05, 3.99993961e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99987131e+06, 3.99996038e+06, 3.99996038e+06, 3.99987269e+06, 3.99996038e+06, 3.99987012e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99953422e+05, 4.00090797e+05, 5.39059633e+05, 3.99874117e+05, 3.99731207e+05, 2.72497070e+05, ],
    'CountWeightedFull'                                                              : [ 3.99759766e+05, 3.99778352e+05, 3.99771148e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99759766e+05, 3.99759766e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99762812e+06, 3.99762812e+06, 3.99762812e+06, 3.99762812e+06, 3.99762812e+06, 3.99762812e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99801719e+05, 3.99860156e+05, 5.38746977e+05, 3.99723344e+05, 3.99491523e+05, 2.72394141e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.71783723e+05, 3.71746715e+05, 3.71839250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.71783723e+05, 3.65511078e+05, 3.78058102e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.71783723e+05, 3.71783723e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.71776000e+06, 3.71783156e+06, 3.71783156e+06, 3.71776125e+06, 3.71783156e+06, 3.71775906e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.71777504e+05, 3.71639809e+05, 5.00752203e+05, 3.71623148e+05, 3.71925371e+05, 2.53671172e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.71572133e+05, 3.71535520e+05, 3.71627297e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.71572133e+05, 3.65304176e+05, 3.77841750e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.71572133e+05, 3.71572133e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.71571791e+06, 3.71571791e+06, 3.71571791e+06, 3.71571791e+06, 3.71571791e+06, 3.71571791e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.71640062e+05, 3.71430191e+05, 5.00472281e+05, 3.71486723e+05, 3.71711793e+05, 2.53577797e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1937780311), # 1.94GB, avg file size 484.45MB
  ("fsize_db",                        24679606006), # 24.68GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        4.25487e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_4t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4T_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 378000, ],
    'CountWeighted'                                                                  : [ 3.78030495e+05, 3.78001170e+05, 3.77996582e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.78030495e+05, 3.78030495e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.77991689e+06, 3.78004308e+06, 3.78004308e+06, 3.77991202e+06, 3.78004308e+06, 3.77990358e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.77980443e+05, 3.78013005e+05, 5.08233598e+05, 3.77853897e+05, 3.77742646e+05, 2.58501961e+05, ],
    'CountWeightedFull'                                                              : [ 3.77827484e+05, 3.77796699e+05, 3.77793590e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.77827484e+05, 3.77827484e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.77802018e+06, 3.77802018e+06, 3.77802018e+06, 3.77802018e+06, 3.77802018e+06, 3.77802018e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.77849474e+05, 3.77810617e+05, 5.07957072e+05, 3.77722898e+05, 3.77534264e+05, 2.58413224e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.52311607e+05, 3.52238586e+05, 3.52358419e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.52311607e+05, 3.46486293e+05, 3.58117586e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.52311607e+05, 3.52311607e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.52286832e+06, 3.52298801e+06, 3.52298801e+06, 3.52286457e+06, 3.52298801e+06, 3.52285645e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.52315071e+05, 3.52112293e+05, 4.73371593e+05, 3.52119136e+05, 3.52329270e+05, 2.41271008e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.52126975e+05, 3.52053036e+05, 3.52173804e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.52126975e+05, 3.46305847e+05, 3.57928868e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.52126975e+05, 3.52126975e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.52114619e+06, 3.52114619e+06, 3.52114619e+06, 3.52114619e+06, 3.52114619e+06, 3.52114619e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.52196030e+05, 3.51928270e+05, 4.73120640e+05, 3.52000043e+05, 3.52140064e+05, 2.41190243e+05, ],
  }),
  ("nof_tree_events",                 378000),
  ("nof_db_events",                   378000),
  ("fsize_local",                     1707239491), # 1.71GB, avg file size 426.81MB
  ("fsize_db",                        23650183821), # 23.65GB, avg file size 1.31GB
  ("use_it",                          True),
  ("xsection",                        0.0002595228),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_4t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4T_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_tttt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_4t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 376000, ],
    'CountWeighted'                                                                  : [ 3.75976500e+05, 3.75987145e+05, 3.76009699e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.75976500e+05, 3.75976500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.75994334e+06, 3.75998947e+06, 3.75998947e+06, 3.75994197e+06, 3.75998947e+06, 3.75994197e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.75950637e+05, 3.75901078e+05, 5.05651625e+05, 3.75878598e+05, 3.75697945e+05, 2.56937789e+05, ],
    'CountWeightedFull'                                                              : [ 3.75768977e+05, 3.75777918e+05, 3.75802223e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.75768977e+05, 3.75768977e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.75790569e+06, 3.75790569e+06, 3.75790569e+06, 3.75790569e+06, 3.75790569e+06, 3.75790569e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.75815879e+05, 3.75696602e+05, 5.05371859e+05, 3.75743430e+05, 3.75484098e+05, 2.56846123e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.49738891e+05, 3.49707012e+05, 3.49776355e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.49738891e+05, 3.43838227e+05, 3.55631656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.49738891e+05, 3.49738891e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.49741944e+06, 3.49746356e+06, 3.49746356e+06, 3.49741819e+06, 3.49746356e+06, 3.49741806e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.49744660e+05, 3.49500574e+05, 4.70039512e+05, 3.49584559e+05, 3.49693477e+05, 2.39338486e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.49551852e+05, 3.49518770e+05, 3.49590242e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.49551852e+05, 3.43655750e+05, 3.55439781e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.49551852e+05, 3.49551852e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.49558953e+06, 3.49558953e+06, 3.49558953e+06, 3.49558953e+06, 3.49558953e+06, 3.49558953e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.49622234e+05, 3.49316078e+05, 4.69788641e+05, 3.49461762e+05, 3.49502438e+05, 2.39254945e+05, ],
  }),
  ("nof_tree_events",                 376000),
  ("nof_db_events",                   376000),
  ("fsize_local",                     1751354561), # 1.75GB, avg file size 437.84MB
  ("fsize_db",                        22808941807), # 22.81GB, avg file size 950.37MB
  ("use_it",                          True),
  ("xsection",                        0.0001064477),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_4t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 396999, ],
    'CountWeighted'                                                                  : [ 3.96976301e+05, 3.96982195e+05, 3.97017996e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96976301e+05, 3.96976301e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97000831e+06, 3.97002881e+06, 3.97002881e+06, 3.97000619e+06, 3.97002881e+06, 3.97000381e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96949496e+05, 3.96894539e+05, 5.49344281e+05, 3.96915246e+05, 3.96595156e+05, 2.57494051e+05, ],
    'CountWeightedFull'                                                              : [ 3.96736734e+05, 3.96743383e+05, 3.96775680e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96736734e+05, 3.96736734e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96762238e+06, 3.96762238e+06, 3.96762238e+06, 3.96762238e+06, 3.96762238e+06, 3.96762238e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96772887e+05, 3.96655117e+05, 5.49011711e+05, 3.96739055e+05, 3.96350434e+05, 2.57379805e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.70997621e+05, 3.70968875e+05, 3.71042426e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.70997621e+05, 3.64950824e+05, 3.76987176e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.70997621e+05, 3.70997621e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.71005103e+06, 3.71007053e+06, 3.71007053e+06, 3.71004903e+06, 3.71007053e+06, 3.71004666e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.70988938e+05, 3.70690941e+05, 5.13159469e+05, 3.70887176e+05, 3.70992113e+05, 2.40956109e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.70775652e+05, 3.70747859e+05, 3.70819734e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.70775652e+05, 3.64732902e+05, 3.76761066e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.70775652e+05, 3.70775652e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.70784809e+06, 3.70784809e+06, 3.70784809e+06, 3.70784809e+06, 3.70784809e+06, 3.70784809e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.70826879e+05, 3.70469691e+05, 5.12853586e+05, 3.70725270e+05, 3.70766816e+05, 2.40850879e+05, ],
  }),
  ("nof_tree_events",                 396999),
  ("nof_db_events",                   396999),
  ("fsize_local",                     1697900441), # 1.70GB, avg file size 424.48MB
  ("fsize_db",                        23489272411), # 23.49GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        5.19e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_2v2t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 395993, ],
    'CountWeighted'                                                                  : [ 3.95988258e+05, 3.95984471e+05, 3.95992902e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95988258e+05, 3.95988258e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95976047e+06, 3.95977934e+06, 3.95977934e+06, 3.95976109e+06, 3.95977934e+06, 3.95976047e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96027348e+05, 3.95495299e+05, 5.51705918e+05, 3.95794377e+05, 3.96325693e+05, 2.53985342e+05, ],
    'CountWeightedFull'                                                              : [ 3.95744896e+05, 3.95740752e+05, 3.95749195e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95744896e+05, 3.95744896e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95735388e+06, 3.95735388e+06, 3.95735388e+06, 3.95735388e+06, 3.95735388e+06, 3.95735388e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95841414e+05, 3.95247873e+05, 5.51366902e+05, 3.95607932e+05, 3.96086082e+05, 2.53867193e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.63341242e+05, 3.63292307e+05, 3.63392045e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.63341242e+05, 3.56016357e+05, 3.70650885e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.63341242e+05, 3.63341242e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.63337155e+06, 3.63338905e+06, 3.63338905e+06, 3.63337205e+06, 3.63338905e+06, 3.63337155e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.63424029e+05, 3.62640395e+05, 5.05975627e+05, 3.63099055e+05, 3.64048105e+05, 2.33403504e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.63124062e+05, 3.63075117e+05, 3.63173951e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.63124062e+05, 3.55804961e+05, 3.70427939e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.63124062e+05, 3.63124062e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.63121878e+06, 3.63121878e+06, 3.63121878e+06, 3.63121878e+06, 3.63121878e+06, 3.63121878e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.63257443e+05, 3.62421041e+05, 5.05673838e+05, 3.62932238e+05, 3.63832814e+05, 2.33297750e+05, ],
  }),
  ("nof_tree_events",                 395993),
  ("nof_db_events",                   395993),
  ("fsize_local",                     1802773509), # 1.80GB, avg file size 450.69MB
  ("fsize_db",                        25137822771), # 25.14GB, avg file size 1.32GB
  ("use_it",                          True),
  ("xsection",                        4.27833e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_2v2t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo2V2Tau_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 395993, ],
    'CountWeighted'                                                                  : [ 3.95977633e+05, 3.95989526e+05, 3.96012903e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95977633e+05, 3.95977633e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95997861e+06, 3.96003248e+06, 3.96003248e+06, 3.95997886e+06, 3.96003248e+06, 3.95997848e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95947971e+05, 3.96280569e+05, 5.48968193e+05, 3.95814968e+05, 3.94685962e+05, 2.55407912e+05, ],
    'CountWeightedFull'                                                              : [ 3.95688280e+05, 3.95702263e+05, 3.95720745e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95688280e+05, 3.95688280e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95711487e+06, 3.95711487e+06, 3.95711487e+06, 3.95711487e+06, 3.95711487e+06, 3.95711487e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95753818e+05, 3.95994253e+05, 5.48572093e+05, 3.95621623e+05, 3.94393782e+05, 2.55282807e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.67470599e+05, 3.67435591e+05, 3.67529143e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.67470599e+05, 3.61183289e+05, 3.73767404e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.67470599e+05, 3.67470599e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.67475937e+06, 3.67481025e+06, 3.67481025e+06, 3.67475962e+06, 3.67481025e+06, 3.67475912e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.67468917e+05, 3.67514438e+05, 5.09199912e+05, 3.67284242e+05, 3.66660308e+05, 2.37373655e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.67212340e+05, 3.67179225e+05, 3.67269527e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.67212340e+05, 3.60931826e+05, 3.73502518e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.67212340e+05, 3.67212340e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.67222170e+06, 3.67222170e+06, 3.67222170e+06, 3.67222170e+06, 3.67222170e+06, 3.67222170e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.67292565e+05, 3.67259098e+05, 5.08845753e+05, 3.67108470e+05, 3.66399848e+05, 2.37259836e+05, ],
  }),
  ("nof_tree_events",                 395993),
  ("nof_db_events",                   395993),
  ("fsize_local",                     2038311366), # 2.04GB, avg file size 509.58MB
  ("fsize_db",                        26724800210), # 26.72GB, avg file size 1.41GB
  ("use_it",                          True),
  ("xsection",                        0.0004275219),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_2v2t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo2V2Tau_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       5),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 4.00011824e+05, 4.00003309e+05, 3.99989254e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00011824e+05, 4.00011824e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99982894e+06, 3.99984069e+06, 3.99984069e+06, 3.99982906e+06, 3.99984069e+06, 3.99982894e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00019145e+05, 3.99944750e+05, 5.52636031e+05, 3.99862348e+05, 3.99345266e+05, 2.60069156e+05, ],
    'CountWeightedFull'                                                              : [ 3.99797180e+05, 3.99786977e+05, 3.99774965e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99797180e+05, 3.99797180e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99770388e+06, 3.99770388e+06, 3.99770388e+06, 3.99770388e+06, 3.99770388e+06, 3.99770388e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99847703e+05, 3.99732008e+05, 5.52343445e+05, 3.99689949e+05, 3.99130410e+05, 2.59957688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.77128633e+05, 3.77085797e+05, 3.77171566e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.77128633e+05, 3.71751059e+05, 3.82435684e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77128633e+05, 3.77128633e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.77116481e+06, 3.77117644e+06, 3.77117644e+06, 3.77116481e+06, 3.77117644e+06, 3.77116481e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.77193250e+05, 3.76869398e+05, 5.20712359e+05, 3.76933879e+05, 3.76748754e+05, 2.45519656e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.76929574e+05, 3.76885879e+05, 3.76972516e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.76929574e+05, 3.71555516e+05, 3.82233160e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.76929574e+05, 3.76929574e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.76918912e+06, 3.76918912e+06, 3.76918912e+06, 3.76918912e+06, 3.76918912e+06, 3.76918912e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.77034422e+05, 3.76671523e+05, 5.20441070e+05, 3.76774227e+05, 3.76550055e+05, 2.45416328e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1710622788), # 1.71GB, avg file size 342.12MB
  ("fsize_db",                        24672842840), # 24.67GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.0001385868),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_2v2t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo2V2Tau_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 375994, ],
    'CountWeighted'                                                                  : [ 3.75998840e+05, 3.75980004e+05, 3.75997777e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.75998840e+05, 3.75998840e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.75954916e+06, 3.75966294e+06, 3.75966294e+06, 3.75954594e+06, 3.75966294e+06, 3.75954528e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.75827555e+05, 3.76257137e+05, 5.20930379e+05, 3.75973953e+05, 3.74810074e+05, 2.42797523e+05, ],
    'CountWeightedFull'                                                              : [ 3.75715719e+05, 3.75697289e+05, 3.75716031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.75715719e+05, 3.75715719e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.75684141e+06, 3.75684141e+06, 3.75684141e+06, 3.75684141e+06, 3.75684141e+06, 3.75684141e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.75643348e+05, 3.75974152e+05, 5.20541656e+05, 3.75790363e+05, 3.74527891e+05, 2.42678145e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.49842980e+05, 3.49815025e+05, 3.49861439e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.49842980e+05, 3.44013547e+05, 3.55666111e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.49842980e+05, 3.49842980e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.49819172e+06, 3.49829606e+06, 3.49829606e+06, 3.49818897e+06, 3.49829606e+06, 3.49818841e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.49721156e+05, 3.49894391e+05, 4.84467637e+05, 3.49794730e+05, 3.49063648e+05, 2.26234150e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.49591146e+05, 3.49562771e+05, 3.49610242e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.49591146e+05, 3.43768135e+05, 3.55407744e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.49591146e+05, 3.49591146e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.49578056e+06, 3.49578056e+06, 3.49578056e+06, 3.49578056e+06, 3.49578056e+06, 3.49578056e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.49552930e+05, 3.49642176e+05, 4.84122418e+05, 3.49627023e+05, 3.48813309e+05, 2.26125088e+05, ],
  }),
  ("nof_tree_events",                 375994),
  ("nof_db_events",                   375994),
  ("fsize_local",                     1883915951), # 1.88GB, avg file size 470.98MB
  ("fsize_db",                        25006485348), # 25.01GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.0003254642),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2v2t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo2V2Tau_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 377996, ],
    'CountWeighted'                                                                  : [ 3.77985395e+05, 3.77993375e+05, 3.78012275e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.77985395e+05, 3.77985395e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.77994003e+06, 3.78003103e+06, 3.78003103e+06, 3.77993678e+06, 3.78003103e+06, 3.77993266e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.77934826e+05, 3.77745656e+05, 5.23568098e+05, 3.77871945e+05, 3.78135146e+05, 2.44925911e+05, ],
    'CountWeightedFull'                                                              : [ 3.77739082e+05, 3.77749010e+05, 3.77765006e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.77739082e+05, 3.77739082e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.77756633e+06, 3.77756633e+06, 3.77756633e+06, 3.77756633e+06, 3.77756633e+06, 3.77756633e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.77762812e+05, 3.77496865e+05, 5.23233508e+05, 3.77700080e+05, 3.77895572e+05, 2.44814819e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.53060414e+05, 3.53018545e+05, 3.53116779e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.53060414e+05, 3.47383938e+05, 3.58706527e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.53060414e+05, 3.53060414e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.53059000e+06, 3.53067738e+06, 3.53067738e+06, 3.53058631e+06, 3.53067738e+06, 3.53058331e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.53047441e+05, 3.52597531e+05, 4.88814709e+05, 3.52900865e+05, 3.53576635e+05, 2.29107629e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.52835688e+05, 3.52795396e+05, 3.52890686e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.52835688e+05, 3.47163961e+05, 3.58476980e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.52835688e+05, 3.52835688e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.52842942e+06, 3.52842942e+06, 3.52842942e+06, 3.52842942e+06, 3.52842942e+06, 3.52842942e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.52889201e+05, 3.52370596e+05, 4.88509684e+05, 3.52742939e+05, 3.53357945e+05, 2.29005294e+05, ],
  }),
  ("nof_tree_events",                 377996),
  ("nof_db_events",                   377996),
  ("fsize_local",                     1771515018), # 1.77GB, avg file size 442.88MB
  ("fsize_db",                        24275480052), # 24.28GB, avg file size 1.21GB
  ("use_it",                          True),
  ("xsection",                        0.001985145),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2v2t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo2V2Tau_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_wwtt"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_2v2t_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99999367e+05, 3.99990812e+05, 4.00004367e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99999367e+05, 3.99999367e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99987956e+06, 3.99997450e+06, 3.99997450e+06, 3.99987806e+06, 3.99997450e+06, 3.99987794e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99869344e+05, 3.99748820e+05, 5.54167367e+05, 3.99930633e+05, 3.99949469e+05, 2.58978395e+05, ],
    'CountWeightedFull'                                                              : [ 3.99717359e+05, 3.99706875e+05, 3.99722906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99717359e+05, 3.99717359e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99680688e+05, 3.99472734e+05, 5.53781078e+05, 3.99742453e+05, 3.99661031e+05, 2.58856391e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.72676004e+05, 3.72613738e+05, 3.72742277e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.72676004e+05, 3.66516227e+05, 3.78815277e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72676004e+05, 3.72676004e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.72665969e+06, 3.72674788e+06, 3.72674788e+06, 3.72665825e+06, 3.72674788e+06, 3.72665800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.72588531e+05, 3.72166797e+05, 5.16160703e+05, 3.72585477e+05, 3.73138172e+05, 2.41646355e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.72421516e+05, 3.72358137e+05, 3.72488531e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.72421516e+05, 3.66267676e+05, 3.78554887e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.72421516e+05, 3.72421516e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.72420375e+06, 3.72420375e+06, 3.72420375e+06, 3.72420375e+06, 3.72420375e+06, 3.72420375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.72415910e+05, 3.71917867e+05, 5.15811242e+05, 3.72413305e+05, 3.72877234e+05, 2.41534594e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1931543120), # 1.93GB, avg file size 482.89MB
  ("fsize_db",                        24971666367), # 24.97GB, avg file size 1.19GB
  ("use_it",                          True),
  ("xsection",                        0.0008142775),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_2v2t_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4V_CV_1_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_1_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_1_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 4.00012068e+05, 3.99997758e+05, 4.00007955e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00012068e+05, 4.00012068e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99982784e+06, 3.99983684e+06, 3.99983684e+06, 3.99982759e+06, 3.99983684e+06, 3.99982759e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99924609e+05, 3.99961883e+05, 5.67576750e+05, 3.99935617e+05, 3.99222127e+05, 2.46694797e+05, ],
    'CountWeightedFull'                                                              : [ 3.99733453e+05, 3.99718164e+05, 3.99729189e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99733453e+05, 3.99733453e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99706662e+06, 3.99706662e+06, 3.99706662e+06, 3.99706662e+06, 3.99706662e+06, 3.99706662e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99705531e+05, 3.99686850e+05, 5.67177641e+05, 3.99715951e+05, 3.98935496e+05, 2.46559250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75268535e+05, 3.75237676e+05, 3.75284104e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75268535e+05, 3.69459014e+05, 3.80990301e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75268535e+05, 3.75268535e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.75256531e+06, 3.75257294e+06, 3.75257294e+06, 3.75256506e+06, 3.75257294e+06, 3.75256506e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.75236494e+05, 3.74958795e+05, 5.32286453e+05, 3.75156953e+05, 3.74957861e+05, 2.31744719e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75012650e+05, 3.74981193e+05, 3.75027494e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75012650e+05, 3.69208395e+05, 3.80729154e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.75012650e+05, 3.75012650e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75001866e+06, 3.75001866e+06, 3.75001866e+06, 3.75001866e+06, 3.75001866e+06, 3.75001866e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75033928e+05, 3.74706541e+05, 5.31919703e+05, 3.74953990e+05, 3.74694113e+05, 2.31619271e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1735995652), # 1.74GB, avg file size 434.00MB
  ("fsize_db",                        24034433959), # 24.03GB, avg file size 1.34GB
  ("use_it",                          True),
  ("xsection",                        9.92524e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_1_hh_4v_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4V_CV_1_C2V_1_C3_2_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_2_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_2_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       3),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 4.00015113e+05, 3.99981028e+05, 4.00012808e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00015113e+05, 4.00015113e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99984929e+06, 3.99987104e+06, 3.99987104e+06, 3.99984966e+06, 3.99987104e+06, 3.99984929e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99943832e+05, 4.00131471e+05, 5.71289495e+05, 3.99952421e+05, 3.99288420e+05, 2.43828297e+05, ],
    'CountWeightedFull'                                                              : [ 3.99727040e+05, 3.99696132e+05, 3.99721076e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99727040e+05, 3.99727040e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99699724e+06, 3.99699724e+06, 3.99699724e+06, 3.99699724e+06, 3.99699724e+06, 3.99699724e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99711191e+05, 3.99842860e+05, 5.70889769e+05, 3.99719552e+05, 3.99009542e+05, 2.43686423e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.68347057e+05, 3.68278424e+05, 3.68402172e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.68347057e+05, 3.61203089e+05, 3.75453692e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.68347057e+05, 3.68347057e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.68335249e+06, 3.68337099e+06, 3.68337099e+06, 3.68335249e+06, 3.68337099e+06, 3.68335249e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.68341577e+05, 3.68160667e+05, 5.26029190e+05, 3.68236153e+05, 3.68295071e+05, 2.24837797e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.68086183e+05, 3.68018790e+05, 3.68139319e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.68086183e+05, 3.60947973e+05, 3.75187064e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.68086183e+05, 3.68086183e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.68076507e+06, 3.68076507e+06, 3.68076507e+06, 3.68076507e+06, 3.68076507e+06, 3.68076507e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.68130707e+05, 3.67899347e+05, 5.25666062e+05, 3.68024883e+05, 3.68040332e+05, 2.24709087e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1843157360), # 1.84GB, avg file size 614.39MB
  ("fsize_db",                        25813375781), # 25.81GB, avg file size 1.23GB
  ("use_it",                          True),
  ("xsection",                        8.18177e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_2_hh_4v_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4V_CV_1_C2V_1_C3_0_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_1_0_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_1_0_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       5),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 387998, ],
    'CountWeighted'                                                                  : [ 3.87986683e+05, 3.87997211e+05, 3.88002740e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87986683e+05, 3.87986683e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.87989805e+06, 3.87994427e+06, 3.87994427e+06, 3.87989905e+06, 3.87994427e+06, 3.87989705e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.87861710e+05, 3.87934210e+05, 5.49727012e+05, 3.88064394e+05, 3.86968373e+05, 2.39941062e+05, ],
    'CountWeightedFull'                                                              : [ 3.87735195e+05, 3.87747149e+05, 3.87751137e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.87735195e+05, 3.87735195e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.87657008e+05, 3.87685994e+05, 5.49374250e+05, 3.87859123e+05, 3.86715610e+05, 2.39814884e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.66972391e+05, 3.66937782e+05, 3.67011388e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.66972391e+05, 3.61982560e+05, 3.71873205e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.66972391e+05, 3.66972391e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.66970694e+06, 3.66975053e+06, 3.66975053e+06, 3.66970802e+06, 3.66975053e+06, 3.66970594e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.66889769e+05, 3.66661274e+05, 5.19810723e+05, 3.66986587e+05, 3.66445714e+05, 2.27223066e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.66737835e+05, 3.66703985e+05, 3.66776250e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.66737835e+05, 3.61751804e+05, 3.71634870e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.66737835e+05, 3.66737835e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.66740198e+06, 3.66740198e+06, 3.66740198e+06, 3.66740198e+06, 3.66740198e+06, 3.66740198e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.66698507e+05, 3.66429849e+05, 5.19481322e+05, 3.66794811e+05, 3.66208900e+05, 2.27105038e+05, ],
  }),
  ("nof_tree_events",                 387998),
  ("nof_db_events",                   387998),
  ("fsize_local",                     1685000463), # 1.69GB, avg file size 337.00MB
  ("fsize_db",                        24323082282), # 24.32GB, avg file size 1.06GB
  ("use_it",                          True),
  ("xsection",                        0.00026503),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_1_0_hh_4v_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4V_CV_1_C2V_2_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_2_1_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_2_1_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       5),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 389999, ],
    'CountWeighted'                                                                  : [ 3.89980811e+05, 3.90007797e+05, 3.90002056e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89980811e+05, 3.89980811e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89975602e+06, 3.89983689e+06, 3.89983689e+06, 3.89975520e+06, 3.89983689e+06, 3.89975502e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.89829754e+05, 3.89789889e+05, 5.55362707e+05, 3.89978111e+05, 3.89840209e+05, 2.39050170e+05, ],
    'CountWeightedFull'                                                              : [ 3.89657591e+05, 3.89683060e+05, 3.89676276e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.89657591e+05, 3.89657591e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.89659814e+06, 3.89659814e+06, 3.89659814e+06, 3.89659814e+06, 3.89659814e+06, 3.89659814e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.89600355e+05, 3.89464451e+05, 5.54914539e+05, 3.89749106e+05, 3.89523956e+05, 2.38909200e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.62119175e+05, 3.62096183e+05, 3.62151953e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.62119175e+05, 3.55966855e+05, 3.68272587e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.62119175e+05, 3.62119175e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.62113562e+06, 3.62120356e+06, 3.62120356e+06, 3.62113456e+06, 3.62120356e+06, 3.62113431e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.62010239e+05, 3.61681482e+05, 5.15411042e+05, 3.62074191e+05, 3.62347057e+05, 2.22305495e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.61830370e+05, 3.61806354e+05, 3.61862041e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.61830370e+05, 3.55685088e+05, 3.67976401e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.61830370e+05, 3.61830370e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.61831111e+06, 3.61831111e+06, 3.61831111e+06, 3.61831111e+06, 3.61831111e+06, 3.61831111e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.61800611e+05, 3.61392088e+05, 5.15012050e+05, 3.61864551e+05, 3.62064798e+05, 2.22176300e+05, ],
  }),
  ("nof_tree_events",                 389999),
  ("nof_db_events",                   389999),
  ("fsize_local",                     2021901296), # 2.02GB, avg file size 404.38MB
  ("fsize_db",                        27060007025), # 27.06GB, avg file size 1.08GB
  ("use_it",                          True),
  ("xsection",                        0.0008175824),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_2_1_hh_4v_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4V_CV_0_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_0p5_1_1_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_0p5_1_1_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 387996, ],
    'CountWeighted'                                                                  : [ 3.88006719e+05, 3.87948445e+05, 3.87994232e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.88006719e+05, 3.88006719e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.87955509e+06, 3.87959503e+06, 3.87959503e+06, 3.87955547e+06, 3.87959503e+06, 3.87955509e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.87824594e+05, 3.88098178e+05, 5.51860902e+05, 3.87989793e+05, 3.87057096e+05, 2.38098014e+05, ],
    'CountWeightedFull'                                                              : [ 3.87680172e+05, 3.87622520e+05, 3.87669562e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.87680172e+05, 3.87680172e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.87634778e+06, 3.87634778e+06, 3.87634778e+06, 3.87634778e+06, 3.87634778e+06, 3.87634778e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.87596807e+05, 3.87771258e+05, 5.51403055e+05, 3.87762441e+05, 3.86734760e+05, 2.37958023e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.61206762e+05, 3.61116818e+05, 3.61262998e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.61206762e+05, 3.55228393e+05, 3.67171781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.61206762e+05, 3.61206762e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.61186322e+06, 3.61189159e+06, 3.61189159e+06, 3.61186347e+06, 3.61189159e+06, 3.61186322e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.61080096e+05, 3.61076660e+05, 5.13573465e+05, 3.61155166e+05, 3.60698785e+05, 2.21934369e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.60909738e+05, 3.60819734e+05, 3.60967127e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.60909738e+05, 3.54937930e+05, 3.66868395e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.60909738e+05, 3.60909738e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.60892869e+06, 3.60892869e+06, 3.60892869e+06, 3.60892869e+06, 3.60892869e+06, 3.60892869e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.60871682e+05, 3.60779264e+05, 5.13156320e+05, 3.60947500e+05, 3.60404002e+05, 2.21806290e+05, ],
  }),
  ("nof_tree_events",                 387996),
  ("nof_db_events",                   387996),
  ("fsize_local",                     1963547345), # 1.96GB, avg file size 490.89MB
  ("fsize_db",                        25351714176), # 25.35GB, avg file size 1.27GB
  ("use_it",                          True),
  ("xsection",                        0.0006224099),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_4v_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4V_CV_1_5_C2V_1_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1p5_1_1_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1p5_1_1_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       2),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 4.00001219e+05, 3.99967812e+05, 3.99987234e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00001219e+05, 4.00001219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99981925e+06, 3.99992538e+06, 3.99992538e+06, 3.99981250e+06, 3.99992538e+06, 3.99980925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99919812e+05, 4.00107547e+05, 5.68116906e+05, 3.99943125e+05, 3.99300438e+05, 2.46394969e+05, ],
    'CountWeightedFull'                                                              : [ 3.99702906e+05, 3.99674109e+05, 3.99688750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99702906e+05, 3.99702906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99693188e+05, 3.99803375e+05, 5.67702859e+05, 3.99716125e+05, 3.99015594e+05, 2.46255312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74326234e+05, 3.74264031e+05, 3.74364531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74326234e+05, 3.68450156e+05, 3.80148953e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.74326234e+05, 3.74326234e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.74311888e+06, 3.74320762e+06, 3.74320762e+06, 3.74311212e+06, 3.74320762e+06, 3.74310912e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74291562e+05, 3.74177500e+05, 5.31398500e+05, 3.74224328e+05, 3.74004375e+05, 2.30880922e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74055234e+05, 3.73995250e+05, 3.74092375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74055234e+05, 3.68184828e+05, 3.79872391e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.74055234e+05, 3.74055234e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74082406e+05, 3.73900953e+05, 5.31021500e+05, 3.74015406e+05, 3.73744797e+05, 2.30751938e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1899884512), # 1.90GB, avg file size 949.94MB
  ("fsize_db",                        26269896355), # 26.27GB, avg file size 1.55GB
  ("use_it",                          True),
  ("xsection",                        0.003796343),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_4v_dipoleRecoilOff"),
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

samples_2017["/VBFHHTo4V_CV_1_C2V_0_C3_1_dipoleRecoilOff-TuneCP5_PSweights_13TeV-madgraph-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v2/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_vbf_nonresonant_1_0_1_hh_wwww"),
  ("process_name_specific",           "signal_vbf_nonresonant_1_0_1_hh_4v_dipoleRecoilOff"),
  ("nof_files",                       4),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 4.00009609e+05, 4.00016566e+05, 3.99996889e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00009609e+05, 4.00009609e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99993509e+06, 3.99998112e+06, 3.99998112e+06, 3.99993381e+06, 3.99998112e+06, 3.99993300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99911648e+05, 4.00011018e+05, 5.68026211e+05, 3.99924176e+05, 3.99178723e+05, 2.46241756e+05, ],
    'CountWeightedFull'                                                              : [ 3.99716816e+05, 3.99722029e+05, 3.99704164e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99716816e+05, 3.99716816e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99705397e+06, 3.99705397e+06, 3.99705397e+06, 3.99705397e+06, 3.99705397e+06, 3.99705397e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99683992e+05, 3.99717359e+05, 5.67612180e+05, 3.99696809e+05, 3.98885777e+05, 2.46101736e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73385742e+05, 3.73347799e+05, 3.73417074e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73385742e+05, 3.67361203e+05, 3.79377934e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73385742e+05, 3.73385742e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.73377081e+06, 3.73380422e+06, 3.73380422e+06, 3.73376931e+06, 3.73380422e+06, 3.73376894e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.73345021e+05, 3.73129672e+05, 5.29994594e+05, 3.73265188e+05, 3.73009406e+05, 2.30188689e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.73119148e+05, 3.73080129e+05, 3.73151672e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.73119148e+05, 3.67100424e+05, 3.79105656e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.73119148e+05, 3.73119148e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.73113972e+06, 3.73113972e+06, 3.73113972e+06, 3.73113972e+06, 3.73113972e+06, 3.73113972e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.73135854e+05, 3.72863289e+05, 5.29618465e+05, 3.73056066e+05, 3.72742494e+05, 2.30059867e+05, ],
  }),
  ("nof_tree_events",                 399998),
  ("nof_db_events",                   399998),
  ("fsize_local",                     1955194060), # 1.96GB, avg file size 488.80MB
  ("fsize_db",                        26693997325), # 26.69GB, avg file size 1.33GB
  ("use_it",                          True),
  ("xsection",                        0.003796343),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         False),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHEPdfWeight[nLHEPdfWeight]/F"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_vbf_nonresonant_1_0_1_hh_4v_dipoleRecoilOff"),
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

samples_2017["/GluGluToHHTo4Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99941812e+05, 3.99958688e+05, 3.99992844e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.11981406e+05, 4.83258344e+05, 4.56283688e+05, 4.23837688e+05, 3.99941812e+05, 3.77566188e+05, 3.56937688e+05, 3.36759188e+05, 3.17858750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.11984281e+05, 3.17857781e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87170656e+05, 3.87149500e+05, 3.87232875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87170656e+05, 3.84148438e+05, 3.90140250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95490531e+05, 4.67837125e+05, 4.41844250e+05, 4.10164625e+05, 3.87170656e+05, 3.65603062e+05, 3.45410312e+05, 3.25988594e+05, 3.07776125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95493406e+05, 3.07775125e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1749281207), # 1.75GB, avg file size 1.75GB
  ("fsize_db",                        20766449398), # 20.77GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00005359e+05, 3.99969828e+05, 3.99952312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10150812e+05, 4.84345172e+05, 4.59564406e+05, 4.21334078e+05, 4.00004031e+05, 3.79471672e+05, 3.54133609e+05, 3.36149672e+05, 3.18887906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10150812e+05, 3.18887875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99954000e+06, 3.99954800e+06, 3.99955250e+06, 3.99953975e+06, 3.99906175e+06, 3.99904475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00075031e+05, 4.00100125e+05, 5.55284578e+05, 3.99905812e+05, 3.99843594e+05, 2.61596453e+05, ],
    'CountWeightedFull'                                                              : [ 3.99973859e+05, 3.99938875e+05, 3.99921062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10111109e+05, 4.84307531e+05, 4.59528719e+05, 4.21301125e+05, 3.99972578e+05, 3.79442188e+05, 3.54106047e+05, 3.36123547e+05, 3.18863062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10111109e+05, 3.18863047e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99924438e+06, 3.99924000e+06, 3.99924438e+06, 3.99924438e+06, 3.99875350e+06, 3.99874925e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00047219e+05, 4.00068969e+05, 5.55240062e+05, 3.99873234e+05, 3.99812188e+05, 2.61577625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87703766e+05, 3.87661469e+05, 3.87693219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87703766e+05, 3.84776375e+05, 3.90578875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94351969e+05, 4.69475422e+05, 4.45559938e+05, 4.08276172e+05, 3.87701172e+05, 3.67898188e+05, 3.43151109e+05, 3.25811984e+05, 3.09155234e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94351969e+05, 3.09155203e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87671912e+06, 3.87672650e+06, 3.87673088e+06, 3.87671900e+06, 3.87626162e+06, 3.87624538e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88224094e+05, 3.87651047e+05, 5.38067156e+05, 3.87052625e+05, 3.87792094e+05, 2.53711344e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87674328e+05, 3.87632438e+05, 3.87663984e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87674328e+05, 3.84747391e+05, 3.90549062e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94314688e+05, 4.69440000e+05, 4.45526281e+05, 4.08245281e+05, 3.87671703e+05, 3.67870453e+05, 3.43125250e+05, 3.25787422e+05, 3.09131906e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94314688e+05, 3.09131875e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87644012e+06, 3.87643575e+06, 3.87644012e+06, 3.87644012e+06, 3.87597100e+06, 3.87596675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88198000e+05, 3.87621859e+05, 5.38025250e+05, 3.87022141e+05, 3.87762531e+05, 2.53693633e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1713041107), # 1.71GB, avg file size 856.52MB
  ("fsize_db",                        20438934957), # 20.44GB, avg file size 2.27GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 388000, ],
    'CountWeighted'                                                                  : [ 3.87882969e+05, 3.87857188e+05, 3.87846219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04101125e+05, 4.64442469e+05, 4.29581625e+05, 4.21280312e+05, 3.87869500e+05, 3.58650562e+05, 3.57634000e+05, 3.29170281e+05, 3.04204312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04101188e+05, 3.04204281e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74120469e+05, 3.74085500e+05, 3.74118125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74120469e+05, 3.70938531e+05, 3.77262938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.86036000e+05, 4.47982500e+05, 4.14512469e+05, 4.06147812e+05, 3.74110719e+05, 3.46038125e+05, 3.44761250e+05, 3.17452312e+05, 2.93484875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.86036062e+05, 2.93484844e+05, ],
  }),
  ("nof_tree_events",                 388000),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1859963491), # 1.86GB, avg file size 1.86GB
  ("fsize_db",                        21137556590), # 21.14GB, avg file size 1.01GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99962562e+05, 3.99949688e+05, 3.99932906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12031844e+05, 4.83198531e+05, 4.56119500e+05, 4.23902000e+05, 3.99962000e+05, 3.77489094e+05, 3.57007188e+05, 3.36786750e+05, 3.17831500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12031844e+05, 3.17831500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87087312e+05, 3.87056438e+05, 3.87079438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87087312e+05, 3.84047875e+05, 3.90076938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95416531e+05, 4.67658781e+05, 4.41567688e+05, 4.10131938e+05, 3.87085688e+05, 3.65432844e+05, 3.45398625e+05, 3.25936344e+05, 3.07671688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95416531e+05, 3.07671688e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1752141428), # 1.75GB, avg file size 1.75GB
  ("fsize_db",                        20758947388), # 20.76GB, avg file size 902.56MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_4_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99998777e+05, 3.99975254e+05, 3.99986583e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10043075e+05, 4.84407154e+05, 4.59750201e+05, 4.21206146e+05, 3.99998777e+05, 3.79571361e+05, 3.53999218e+05, 3.36114125e+05, 3.18937686e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10043075e+05, 3.18937686e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99969283e+06, 3.99969283e+06, 3.99969283e+06, 3.99969283e+06, 3.99969283e+06, 3.99969283e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99976223e+05, 4.00042899e+05, 5.54902052e+05, 4.00077965e+05, 3.99561138e+05, 2.61750500e+05, ],
    'CountWeightedFull'                                                              : [ 3.99968113e+05, 3.99944415e+05, 3.99955707e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10003793e+05, 4.84369911e+05, 4.59715094e+05, 4.21173694e+05, 3.99968113e+05, 3.79542265e+05, 3.53971920e+05, 3.36088313e+05, 3.18913137e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10003793e+05, 3.18913137e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99938412e+06, 3.99938412e+06, 3.99938412e+06, 3.99938412e+06, 3.99938412e+06, 3.99938412e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99948110e+05, 4.00012422e+05, 5.54858191e+05, 4.00044893e+05, 3.99530048e+05, 2.61731221e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87758765e+05, 3.87720396e+05, 3.87772817e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87758765e+05, 3.84843051e+05, 3.90624702e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94322762e+05, 4.69611586e+05, 4.45819878e+05, 4.08209738e+05, 3.87758765e+05, 3.68058159e+05, 3.43066869e+05, 3.25829358e+05, 3.09254903e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94322762e+05, 3.09254903e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88175117e+05, 3.87739710e+05, 5.37750288e+05, 3.87294860e+05, 3.87468690e+05, 2.53896875e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87729856e+05, 3.87691340e+05, 3.87743750e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87729856e+05, 3.84814551e+05, 3.90595460e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94285751e+05, 4.69576411e+05, 4.45786698e+05, 4.08179197e+05, 3.87729856e+05, 3.68030738e+05, 3.43041227e+05, 3.25804993e+05, 3.09231819e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94285751e+05, 3.09231819e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87714273e+06, 3.87714273e+06, 3.87714273e+06, 3.87714273e+06, 3.87714273e+06, 3.87714273e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88148662e+05, 3.87711124e+05, 5.37709076e+05, 3.87263809e+05, 3.87439351e+05, 2.53878687e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1715839544), # 1.72GB, avg file size 571.95MB
  ("fsize_db",                        20743041889), # 20.74GB, avg file size 987.76MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_5_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99981430e+05, 3.99985227e+05, 3.99982102e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.13017562e+05, 4.82679715e+05, 4.54507211e+05, 4.25213879e+05, 3.99981430e+05, 3.76556312e+05, 3.58456684e+05, 3.37115281e+05, 3.17327488e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.13017562e+05, 3.17327488e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99949175e+06, 3.99950362e+06, 3.99950362e+06, 3.99949200e+06, 3.99950362e+06, 3.99949175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99954820e+05, 4.00328059e+05, 5.55735711e+05, 4.00043684e+05, 3.98689312e+05, 2.60454578e+05, ],
    'CountWeightedFull'                                                              : [ 3.99946383e+05, 3.99950633e+05, 3.99947379e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12972633e+05, 4.82637812e+05, 4.54467957e+05, 4.25176781e+05, 3.99946383e+05, 3.76523621e+05, 3.58425191e+05, 3.37085859e+05, 3.17300008e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12972633e+05, 3.17300008e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99915781e+06, 3.99915781e+06, 3.99915781e+06, 3.99915781e+06, 3.99915781e+06, 3.99915781e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99924539e+05, 4.00292594e+05, 5.55685930e+05, 4.00008043e+05, 3.98655352e+05, 2.60433918e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86937395e+05, 3.86925434e+05, 3.86959242e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86937395e+05, 3.83863676e+05, 3.89962758e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96154516e+05, 4.66961859e+05, 4.39827508e+05, 4.11219039e+05, 3.86937395e+05, 3.64379445e+05, 3.46646633e+05, 3.26112844e+05, 3.07054617e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96154516e+05, 3.07054617e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.86918634e+06, 3.86919491e+06, 3.86919491e+06, 3.86918653e+06, 3.86919491e+06, 3.86918634e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87365539e+05, 3.87182660e+05, 5.37425883e+05, 3.86425281e+05, 3.85817539e+05, 2.52104461e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.86905254e+05, 3.86893539e+05, 3.86927301e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.86905254e+05, 3.83832168e+05, 3.89930008e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.96113355e+05, 4.66923320e+05, 4.39791434e+05, 4.11184945e+05, 3.86905254e+05, 3.64349324e+05, 3.46617715e+05, 3.26085789e+05, 3.07029344e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.96113355e+05, 3.07029344e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.86887609e+06, 3.86887609e+06, 3.86887609e+06, 3.86887609e+06, 3.86887609e+06, 3.86887609e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87337176e+05, 3.87150301e+05, 5.37380109e+05, 3.86391863e+05, 3.85785914e+05, 2.52085154e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1778083806), # 1.78GB, avg file size 592.69MB
  ("fsize_db",                        21373837304), # 21.37GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_5_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_6_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99989938e+05, 3.99966625e+05, 3.99978562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10293109e+05, 4.84250766e+05, 4.59284812e+05, 4.21534172e+05, 3.99985297e+05, 3.79314266e+05, 3.54354922e+05, 3.36199750e+05, 3.18807172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10293109e+05, 3.18807172e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99963600e+06, 3.99964862e+06, 3.99964862e+06, 3.99963600e+06, 3.99964862e+06, 3.99963600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99893578e+05, 3.99999297e+05, 5.55705281e+05, 4.00123266e+05, 4.00213250e+05, 2.61487164e+05, ],
    'CountWeightedFull'                                                              : [ 3.99957344e+05, 3.99934609e+05, 3.99945828e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10251609e+05, 4.84211453e+05, 4.59247781e+05, 4.21499906e+05, 3.99952719e+05, 3.79283469e+05, 3.54325938e+05, 3.36172406e+05, 3.18781234e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10251609e+05, 3.18781234e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99932162e+06, 3.99932162e+06, 3.99932162e+06, 3.99932162e+06, 3.99932162e+06, 3.99932162e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99865172e+05, 3.99967078e+05, 5.55656688e+05, 4.00089703e+05, 4.00178594e+05, 2.61467828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87580953e+05, 3.87534484e+05, 3.87602656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87580953e+05, 3.84632562e+05, 3.90477609e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94345453e+05, 4.69245719e+05, 4.45158094e+05, 4.08350500e+05, 3.87576719e+05, 3.67639484e+05, 3.43265250e+05, 3.25766719e+05, 3.08987828e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94345453e+05, 3.08987828e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87564025e+06, 3.87565212e+06, 3.87565212e+06, 3.87564038e+06, 3.87565212e+06, 3.87564025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87924938e+05, 3.87477172e+05, 5.38263906e+05, 3.87157266e+05, 3.87946656e+05, 2.53535898e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87550312e+05, 3.87504312e+05, 3.87571953e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87550312e+05, 3.84602422e+05, 3.90446641e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94306391e+05, 4.69208734e+05, 4.45123172e+05, 4.08318172e+05, 3.87546078e+05, 3.67610516e+05, 3.43238031e+05, 3.25740984e+05, 3.08963469e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94306391e+05, 3.08963469e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87534538e+06, 3.87534538e+06, 3.87534538e+06, 3.87534538e+06, 3.87534538e+06, 3.87534538e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87898188e+05, 3.87446766e+05, 5.38218250e+05, 3.87125797e+05, 3.87914156e+05, 2.53517734e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1717969422), # 1.72GB, avg file size 858.98MB
  ("fsize_db",                        21327709588), # 21.33GB, avg file size 1.12GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_6_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 374000, ],
    'CountWeighted'                                                                  : [ 3.73979250e+05, 3.73896469e+05, 3.73970219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.76968062e+05, 4.52875438e+05, 4.29698125e+05, 3.93920750e+05, 3.73979250e+05, 3.54812625e+05, 3.31091500e+05, 3.14286750e+05, 2.98159000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.76968062e+05, 2.98159000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.62279875e+05, 3.62196156e+05, 3.62301969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.62279875e+05, 3.59507500e+05, 3.65008625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.61933781e+05, 4.38716812e+05, 4.16365938e+05, 3.81496000e+05, 3.62279875e+05, 3.43794812e+05, 3.20639906e+05, 3.04449812e+05, 2.88896875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.61933781e+05, 2.88896875e+05, ],
  }),
  ("nof_tree_events",                 374000),
  ("nof_db_events",                   374000),
  ("fsize_local",                     1596650076), # 1.60GB, avg file size 1.60GB
  ("fsize_db",                        19521414949), # 19.52GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_8_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_4t"),
  ("nof_files",                       3),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85966207e+05, 3.85978934e+05, 3.85974191e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92136490e+05, 4.67480260e+05, 4.43748287e+05, 4.06380170e+05, 3.85961381e+05, 3.66341990e+05, 3.41512021e+05, 3.24328957e+05, 3.07805762e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92136490e+05, 3.07805762e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.95978484e+06, 1.95426484e+06, 2.60344878e+06, 1.96116929e+06, 1.84867968e+06, 1.28277661e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.85872883e+05, 3.85849471e+05, 5.35713951e+05, 3.86162832e+05, 3.86028232e+05, 2.52571844e+05, ],
    'CountWeightedFull'                                                              : [ 3.85936379e+05, 3.85949059e+05, 3.85944242e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92098191e+05, 4.67443936e+05, 4.43713855e+05, 4.06348717e+05, 3.85931521e+05, 3.66313586e+05, 3.41485389e+05, 3.24303678e+05, 3.07781824e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92098191e+05, 3.07781824e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.95965008e+06, 1.95411470e+06, 2.60324395e+06, 1.96100964e+06, 1.84853737e+06, 1.28268416e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85846256e+05, 3.85819756e+05, 5.35671711e+05, 3.86131418e+05, 3.85998299e+05, 2.52553592e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74067795e+05, 3.74060910e+05, 3.74085262e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74067795e+05, 3.71234557e+05, 3.76850730e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.76844301e+05, 4.53078861e+05, 4.30179531e+05, 3.93742697e+05, 3.74062801e+05, 3.55130840e+05, 3.30883195e+05, 3.14321096e+05, 2.98378673e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.76844301e+05, 2.98378673e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90146140e+06, 1.89333579e+06, 2.52262600e+06, 1.89801501e+06, 1.79302193e+06, 1.24401534e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74387334e+05, 3.73807396e+05, 5.19063422e+05, 3.73724914e+05, 3.74376676e+05, 2.44938321e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74039703e+05, 3.74032770e+05, 3.74057045e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74039703e+05, 3.71206869e+05, 3.76822215e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.76808270e+05, 4.53044742e+05, 4.30147127e+05, 3.93713023e+05, 3.74034748e+05, 3.55104152e+05, 3.30858166e+05, 3.14297324e+05, 2.98356200e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.76808270e+05, 2.98356200e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90133444e+06, 1.89319384e+06, 2.52243278e+06, 1.89786488e+06, 1.79288817e+06, 1.24392856e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74362338e+05, 3.73779412e+05, 5.19023652e+05, 3.73695355e+05, 3.74348424e+05, 2.44921145e+05, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1654313438), # 1.65GB, avg file size 551.44MB
  ("fsize_db",                        19769722803), # 19.77GB, avg file size 988.49MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_8_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99932875e+05, 3.99996688e+05, 3.99998250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19447031e+05, 4.78878406e+05, 4.43029219e+05, 4.33960125e+05, 3.99932875e+05, 3.69929781e+05, 3.68249062e+05, 3.39303750e+05, 3.13772812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19447062e+05, 3.13772812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85684031e+05, 3.85692125e+05, 3.85761219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85684031e+05, 3.82396188e+05, 3.88944000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.00794500e+05, 4.61833094e+05, 4.27386406e+05, 4.18356750e+05, 3.85684031e+05, 3.56848281e+05, 3.54993875e+05, 3.27199000e+05, 3.02666938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.00794500e+05, 3.02666938e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1918950365), # 1.92GB, avg file size 1.92GB
  ("fsize_db",                        21901746830), # 21.90GB, avg file size 1.10GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_10_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85969562e+05, 3.85944500e+05, 3.85987109e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92241656e+05, 4.67366406e+05, 4.43461703e+05, 4.06540562e+05, 3.85965547e+05, 3.66173141e+05, 3.41694734e+05, 3.24352938e+05, 3.07708203e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92241656e+05, 3.07708203e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.85307800e+06, 3.84637712e+06, 3.85445212e+06, 3.85310538e+06, 3.79028500e+06, 3.78236938e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.85939766e+05, 3.85935719e+05, 5.35786609e+05, 3.86055781e+05, 3.85927094e+05, 2.52441938e+05, ],
    'CountWeightedFull'                                                              : [ 3.85938500e+05, 3.85913844e+05, 3.85955875e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92202734e+05, 4.67329031e+05, 4.43426125e+05, 4.06508281e+05, 3.85934469e+05, 3.66143766e+05, 3.41667703e+05, 3.24327000e+05, 3.07683500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92202734e+05, 3.07683500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.85276388e+06, 3.84607312e+06, 3.85414688e+06, 3.85279438e+06, 3.78998500e+06, 3.78206462e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85910859e+05, 3.85903672e+05, 5.35741188e+05, 3.86022219e+05, 3.85894219e+05, 2.52422039e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73966484e+05, 3.73941328e+05, 3.73989188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73966484e+05, 3.71112078e+05, 3.76768312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.76826562e+05, 4.52852406e+05, 4.29792562e+05, 3.93797812e+05, 3.73962234e+05, 3.54877203e+05, 3.30977281e+05, 3.14264234e+05, 2.98208703e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.76826562e+05, 2.98208703e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.73333975e+06, 3.72689938e+06, 3.73467888e+06, 3.73335588e+06, 3.67281762e+06, 3.66518250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74361109e+05, 3.73896312e+05, 5.18902109e+05, 3.73514312e+05, 3.73955984e+05, 2.44725227e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.73936938e+05, 3.73911984e+05, 3.73959531e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.73936938e+05, 3.71082906e+05, 3.76738422e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.76789125e+05, 4.52816703e+05, 4.29758672e+05, 3.93766797e+05, 3.73932672e+05, 3.54849266e+05, 3.30951203e+05, 3.14239500e+05, 2.98185250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.76789125e+05, 2.98185250e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.73304462e+06, 3.72660750e+06, 3.73438600e+06, 3.73306350e+06, 3.67253000e+06, 3.66489650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74333984e+05, 3.73867016e+05, 5.18860375e+05, 3.73482906e+05, 3.73925844e+05, 2.44706547e+05, ],
  }),
  ("nof_tree_events",                 386000),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1654929460), # 1.65GB, avg file size 827.46MB
  ("fsize_db",                        19949920750), # 19.95GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_10_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_11_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_4t"),
  ("nof_files",                       2),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99953875e+05, 3.99978312e+05, 3.99941984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10468719e+05, 4.84131156e+05, 4.58934562e+05, 4.21776469e+05, 3.99952547e+05, 3.79116172e+05, 3.54627406e+05, 3.36252438e+05, 3.18700656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10468719e+05, 3.18700656e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99959638e+06, 3.99959638e+06, 3.99959638e+06, 3.99959638e+06, 3.99959638e+06, 3.99959638e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00062766e+05, 4.00302406e+05, 5.54878969e+05, 3.99932266e+05, 3.99224609e+05, 2.61640258e+05, ],
    'CountWeightedFull'                                                              : [ 3.99921328e+05, 3.99945156e+05, 3.99910047e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10426984e+05, 4.84091688e+05, 4.58897266e+05, 4.21742016e+05, 3.99920031e+05, 3.79085375e+05, 3.54598344e+05, 3.36225078e+05, 3.18674672e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10426984e+05, 3.18674672e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00033094e+05, 4.00270453e+05, 5.54831688e+05, 3.99897734e+05, 3.99190562e+05, 2.61619891e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87562938e+05, 3.87553969e+05, 3.87583094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87562938e+05, 3.84614812e+05, 3.90458766e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94528281e+05, 4.69137516e+05, 4.44825234e+05, 4.08596172e+05, 3.87561172e+05, 3.67451859e+05, 3.43537625e+05, 3.25825641e+05, 3.08888281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94528281e+05, 3.08888281e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87566388e+06, 3.87566388e+06, 3.87566388e+06, 3.87566388e+06, 3.87566388e+06, 3.87566388e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88086531e+05, 3.87790797e+05, 5.37531594e+05, 3.86993562e+05, 3.87027422e+05, 2.53674094e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87532438e+05, 3.87522891e+05, 3.87553062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87532438e+05, 3.84584781e+05, 3.90427781e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94489266e+05, 4.69100578e+05, 4.44790250e+05, 4.08563906e+05, 3.87530656e+05, 3.67423031e+05, 3.43510391e+05, 3.25800094e+05, 3.08863984e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94489266e+05, 3.08863984e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87535788e+06, 3.87535788e+06, 3.87535788e+06, 3.87535788e+06, 3.87535788e+06, 3.87535788e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88058797e+05, 3.87760969e+05, 5.37487438e+05, 3.86961203e+05, 3.86995609e+05, 2.53655023e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1721341322), # 1.72GB, avg file size 860.67MB
  ("fsize_db",                        20767271120), # 20.77GB, avg file size 1.38GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_11_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4t"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.95942031e+05, 3.96003594e+05, 3.95945906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04830000e+05, 4.79599375e+05, 4.55277188e+05, 4.16854062e+05, 3.95942031e+05, 3.75852438e+05, 3.50307812e+05, 3.32711406e+05, 3.15790000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04830000e+05, 3.15790000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83655844e+05, 3.83677438e+05, 3.83673781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83655844e+05, 3.80736188e+05, 3.86530875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.89039031e+05, 4.64719188e+05, 4.41253375e+05, 4.03803375e+05, 3.83655844e+05, 3.64266625e+05, 3.39332344e+05, 3.22372406e+05, 3.06048875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.89039031e+05, 3.06048875e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1687383825), # 1.69GB, avg file size 1.69GB
  ("fsize_db",                        20180485758), # 20.18GB, avg file size 1.26GB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 993800, ],
    'CountWeighted'                                                                  : [ 9.35851250e+05, 9.35668766e+05, 9.35816516e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08269056e+06, 1.06366330e+06, 1.05026102e+06, 9.57200469e+05, 9.35851234e+05, 9.18644641e+05, 8.48701406e+05, 8.26740828e+05, 8.08004172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12098859e+06, 7.89224516e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.35767547e+05, 9.35778156e+05, 1.29037906e+06, 9.35887875e+05, 9.35258172e+05, 6.16218094e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.36766475e+04, 6.36860898e+04, 8.78388066e+04, 6.36956982e+04, 6.36783564e+04, 4.19431953e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.11437250e+05, 9.11260547e+05, 9.11449828e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.11437250e+05, 9.05448344e+05, 9.17280266e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05409314e+06, 1.03579808e+06, 1.02295031e+06, 9.32018859e+05, 9.11437203e+05, 8.94870141e+05, 8.26436625e+05, 8.05249000e+05, 7.87166875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.09140834e+06, 7.68878969e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.11472609e+05, 9.11224797e+05, 1.25646722e+06, 9.11342438e+05, 9.11089625e+05, 6.00413938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 6.20071543e+04, 6.19986631e+04, 8.55085352e+04, 6.20089951e+04, 6.20159863e+04, 4.08559092e+04, ],
  }),
  ("nof_tree_events",                 993800),
  ("nof_db_events",                   993800),
  ("fsize_local",                     4055293270), # 4.06GB, avg file size 1.01GB
  ("fsize_db",                        48437908822), # 48.44GB, avg file size 880.69MB
  ("use_it",                          True),
  ("xsection",                        0.00026349),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 973200, ],
    'CountWeighted'                                                                  : [ 8.72135797e+05, 8.72118000e+05, 8.72067078e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.92976781e+05, 9.77088797e+05, 9.66615578e+05, 8.92237359e+05, 8.72084469e+05, 8.56363141e+05, 8.00844656e+05, 7.78974422e+05, 7.60652766e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03559289e+06, 7.37506391e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.72235516e+05, 8.72399375e+05, 1.20490481e+06, 8.72057906e+05, 8.71816469e+05, 5.72707438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.91179463e+04, 2.91169233e+04, 4.02133398e+04, 2.91169180e+04, 2.91232778e+04, 1.91421523e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.48528594e+05, 8.48505750e+05, 8.48480297e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.48528594e+05, 8.42776422e+05, 8.54143578e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.65739109e+05, 9.50499047e+05, 9.40503000e+05, 8.67879125e+05, 8.48485406e+05, 8.33351688e+05, 7.79048812e+05, 7.57959859e+05, 7.40292875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00722794e+06, 7.17762453e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.48728375e+05, 8.48622578e+05, 1.17204866e+06, 8.48309141e+05, 8.48461844e+05, 5.57449680e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.83298462e+04, 2.83202446e+04, 3.91115645e+04, 2.83199644e+04, 2.83388486e+04, 1.86300747e+04, ],
  }),
  ("nof_tree_events",                 973200),
  ("nof_db_events",                   973200),
  ("fsize_local",                     4066476593), # 4.07GB, avg file size 1.02GB
  ("fsize_db",                        47737447211), # 47.74GB, avg file size 867.95MB
  ("use_it",                          True),
  ("xsection",                        0.00011734),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    62),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 8.62699391e+05, 8.62784453e+05, 8.62588484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.84110781e+05, 9.70390672e+05, 9.61615875e+05, 8.80358906e+05, 8.62660312e+05, 8.48880953e+05, 7.87947781e+05, 7.68524625e+05, 7.52163375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03623509e+06, 7.20361641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.62675047e+05, 8.62634391e+05, 1.19285556e+06, 8.62719047e+05, 8.62023172e+05, 5.65253828e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31737903e+04, 1.31703269e+04, 1.82129136e+04, 1.31760439e+04, 1.31758391e+04, 8.64209082e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.39325891e+05, 8.39327734e+05, 8.39302594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.39325891e+05, 8.33632328e+05, 8.44890562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.57019891e+05, 9.43929438e+05, 9.35617750e+05, 8.56272234e+05, 8.39291547e+05, 8.26080609e+05, 7.66477734e+05, 7.47796078e+05, 7.32056375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00776438e+06, 7.01107016e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.39433953e+05, 8.39076719e+05, 1.16020112e+06, 8.39178984e+05, 8.38910562e+05, 5.50263891e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.28172744e+04, 1.28091853e+04, 1.77126514e+04, 1.28148801e+04, 1.28212061e+04, 8.41160327e+03, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4210889018), # 4.21GB, avg file size 1.05GB
  ("fsize_db",                        49299783371), # 49.30GB, avg file size 795.16MB
  ("use_it",                          True),
  ("xsection",                        4.97e-05),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4t"),
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

samples_2017["/GluGluToHHTo4Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_4t"),
  ("nof_files",                       4),
  ("nof_db_files",                    58),
  ("nof_events",                      {
    'Count'                                                                          : [ 991200, ],
    'CountWeighted'                                                                  : [ 9.75626250e+05, 9.75693250e+05, 9.75702094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.16860781e+06, 1.14658962e+06, 1.12963400e+06, 9.95071703e+05, 9.75590094e+05, 9.59165234e+05, 8.56874094e+05, 8.39680328e+05, 8.24117297e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.20429662e+06, 8.07343391e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.75826812e+05, 9.76011125e+05, 1.34362962e+06, 9.75431281e+05, 9.74448453e+05, 6.43645422e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 7.95415391e+04, 7.95522422e+04, 1.09577090e+05, 7.95029785e+04, 7.94826836e+04, 5.24578037e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52048281e+05, 9.52063859e+05, 9.52126453e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52048281e+05, 9.46138234e+05, 9.57784312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.13982188e+06, 1.11864509e+06, 1.10235869e+06, 9.70753047e+05, 9.52013172e+05, 9.36188531e+05, 8.36058141e+05, 8.19501156e+05, 8.04495391e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.17471109e+06, 7.88093641e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.52386750e+05, 9.52222281e+05, 1.31075509e+06, 9.51652766e+05, 9.51155781e+05, 6.28464375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.76214062e+04, 7.76035039e+04, 1.06883943e+05, 7.75551133e+04, 7.75744180e+04, 5.12141641e+04, ],
  }),
  ("nof_tree_events",                 991200),
  ("nof_db_events",                   991200),
  ("fsize_local",                     3840770806), # 3.84GB, avg file size 960.19MB
  ("fsize_db",                        47501791315), # 47.50GB, avg file size 819.00MB
  ("use_it",                          True),
  ("xsection",                        0.00034666),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 399996, ],
    'CountWeighted'                                                                  : [ 3.99957375e+05, 3.99958188e+05, 3.99988938e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12035625e+05, 4.83279000e+05, 4.56279500e+05, 4.23879594e+05, 3.99956406e+05, 3.77572719e+05, 3.56977094e+05, 3.36780875e+05, 3.17864094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12035969e+05, 3.17863594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87740219e+05, 3.87731656e+05, 3.87761219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87740219e+05, 3.84821438e+05, 3.90593469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96246438e+05, 4.68526719e+05, 4.42477406e+05, 4.10789500e+05, 3.87738188e+05, 3.66133062e+05, 3.45939469e+05, 3.26472562e+05, 3.08222344e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96246781e+05, 3.08221875e+05, ],
  }),
  ("nof_tree_events",                 399996),
  ("nof_db_events",                   399996),
  ("fsize_local",                     1828350814), # 1.83GB, avg file size 1.83GB
  ("fsize_db",                        21713327567), # 21.71GB, avg file size 1.45GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2tau_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2v2t"),
  ("nof_files",                       16),
  ("nof_db_files",                    86),
  ("nof_events",                      {
    'Count'                                                                          : [ 3859942, ],
    'CountWeighted'                                                                  : [ 3.85950995e+06, 3.85948500e+06, 3.85959227e+06, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92243172e+06, 4.67387328e+06, 4.43502569e+06, 4.06536742e+06, 3.85948811e+06, 3.66201312e+06, 3.41689698e+06, 3.24363373e+06, 3.07730156e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92243269e+06, 3.07730047e+06, ],
    'CountWeightedPSWeight'                                                          : [ 3.85962092e+07, 3.85899781e+07, 3.85962465e+07, 3.85962072e+07, 3.84519950e+07, 3.84456871e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.85965620e+06, 3.85874597e+06, 5.49814341e+06, 3.86034380e+06, 3.85768269e+06, 2.40289190e+06, ],
    'CountWeightedFull'                                                              : [ 3.85880553e+06, 3.85877656e+06, 3.85887498e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92152230e+06, 4.67301108e+06, 4.43420920e+06, 4.06461650e+06, 3.85878342e+06, 3.66133828e+06, 3.41626648e+06, 3.24303550e+06, 3.07673462e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92152327e+06, 3.07673355e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.85891022e+07, 3.85828368e+07, 3.85891035e+07, 3.85891020e+07, 3.84448839e+07, 3.84386152e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85897136e+06, 3.85804048e+06, 5.49711709e+06, 3.85961070e+06, 3.85696170e+06, 2.40245684e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74713017e+06, 3.74691012e+06, 3.74737884e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74713017e+06, 3.72007067e+06, 3.77355731e+06, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.77792828e+06, 4.53786028e+06, 4.30694977e+06, 3.94591209e+06, 3.74710747e+06, 3.55615662e+06, 3.31641028e+06, 3.14907078e+06, 2.98827028e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.77792906e+06, 2.98826947e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.74720558e+07, 3.74660119e+07, 3.74720868e+07, 3.74720532e+07, 3.73331992e+07, 3.73270916e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.75144292e+06, 3.74530906e+06, 5.33630148e+06, 3.74249047e+06, 3.74677177e+06, 2.33427580e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74645402e+06, 3.74623264e+06, 3.74669586e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74645402e+06, 3.71940197e+06, 3.77287403e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.77706066e+06, 4.53703723e+06, 4.30616916e+06, 3.94519528e+06, 3.74643119e+06, 3.55551192e+06, 3.31580814e+06, 3.14849952e+06, 2.98772856e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.77706141e+06, 2.98772775e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.74652689e+07, 3.74591975e+07, 3.74652699e+07, 3.74652686e+07, 3.73264139e+07, 3.73203401e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75078659e+06, 3.74463575e+06, 5.33532203e+06, 3.74179122e+06, 3.74608228e+06, 2.33385919e+06, ],
  }),
  ("nof_tree_events",                 3859942),
  ("nof_db_events",                   3859942),
  ("fsize_local",                     17320712169), # 17.32GB, avg file size 1.08GB
  ("fsize_db",                        203407106593), # 203.41GB, avg file size 2.37GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 369992, ],
    'CountWeighted'                                                                  : [ 3.69968406e+05, 3.69942844e+05, 3.69992906e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.80692500e+05, 4.42947688e+05, 4.09764188e+05, 4.01694375e+05, 3.69968406e+05, 3.42076125e+05, 3.40983594e+05, 3.13889406e+05, 2.90126969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.80695375e+05, 2.90124438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.57228656e+05, 3.57207156e+05, 3.57255688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.57228656e+05, 3.54270938e+05, 3.60142625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.63984094e+05, 4.27750906e+05, 3.95869156e+05, 3.87692562e+05, 3.57228656e+05, 3.30440688e+05, 3.29069125e+05, 3.03063375e+05, 2.80236156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.63986656e+05, 2.80233875e+05, ],
  }),
  ("nof_tree_events",                 369992),
  ("nof_db_events",                   369992),
  ("fsize_local",                     1824685750), # 1.82GB, avg file size 1.82GB
  ("fsize_db",                        20666744125), # 20.67GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 392996, ],
    'CountWeighted'                                                                  : [ 3.92980156e+05, 3.93009969e+05, 3.92944188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.03066812e+05, 4.74755438e+05, 4.48161250e+05, 4.16473062e+05, 3.92980156e+05, 3.70900344e+05, 3.50746812e+05, 3.30894625e+05, 3.12278125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.03066812e+05, 3.12278125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81002250e+05, 3.81017312e+05, 3.80973938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81002250e+05, 3.78142281e+05, 3.83795000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.87612438e+05, 4.60307688e+05, 4.34635688e+05, 4.03664312e+05, 3.81002250e+05, 3.59692594e+05, 3.39945750e+05, 3.20801781e+05, 3.02830250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.87612438e+05, 3.02830250e+05, ],
  }),
  ("nof_tree_events",                 392996),
  ("nof_db_events",                   392996),
  ("fsize_local",                     1803196101), # 1.80GB, avg file size 1.80GB
  ("fsize_db",                        20864139002), # 20.86GB, avg file size 1.49GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 375989, ],
    'CountWeighted'                                                                  : [ 3.75942344e+05, 3.75900812e+05, 3.75909062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.79431188e+05, 4.55317156e+05, 4.32108094e+05, 3.95940062e+05, 3.75942344e+05, 3.56764375e+05, 3.32774406e+05, 3.15938500e+05, 2.99778344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.79431188e+05, 2.99778344e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.65001562e+05, 3.64947062e+05, 3.65006031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.65001562e+05, 3.62364562e+05, 3.67574438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.65357875e+05, 4.42073094e+05, 4.19641562e+05, 3.84304156e+05, 3.65001562e+05, 3.46456844e+05, 3.22984469e+05, 3.06730469e+05, 2.91110750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.65357875e+05, 2.91110750e+05, ],
  }),
  ("nof_tree_events",                 375989),
  ("nof_db_events",                   375989),
  ("fsize_local",                     1680309348), # 1.68GB, avg file size 1.68GB
  ("fsize_db",                        19916065120), # 19.92GB, avg file size 1.53GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99928188e+05, 3.99937562e+05, 3.99889344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12958344e+05, 4.82659688e+05, 4.54506500e+05, 4.25159156e+05, 3.99928188e+05, 3.76550125e+05, 3.58412375e+05, 3.37086562e+05, 3.17317062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12958562e+05, 3.17317000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87536562e+05, 3.87521656e+05, 3.87534906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87536562e+05, 3.84586688e+05, 3.90422031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96920688e+05, 4.67718812e+05, 4.40557000e+05, 4.11848125e+05, 3.87536562e+05, 3.64973188e+05, 3.47173312e+05, 3.26622062e+05, 3.07552438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96920844e+05, 3.07552406e+05, ],
  }),
  ("nof_tree_events",                 399994),
  ("nof_db_events",                   399994),
  ("fsize_local",                     1849347478), # 1.85GB, avg file size 1.85GB
  ("fsize_db",                        21844664310), # 21.84GB, avg file size 1.09GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_6_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 399992, ],
    'CountWeighted'                                                                  : [ 4.00012500e+05, 3.99947625e+05, 3.99905281e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10237156e+05, 4.84218438e+05, 4.59263812e+05, 4.21483125e+05, 4.00012500e+05, 3.79293250e+05, 3.54315375e+05, 3.36162844e+05, 3.18785406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10239812e+05, 3.18783188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88315719e+05, 3.88247625e+05, 3.88271438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88315719e+05, 3.85505125e+05, 3.91060875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95235375e+05, 4.70102125e+05, 4.45975844e+05, 4.09079250e+05, 3.88315719e+05, 3.68309562e+05, 3.43877969e+05, 3.26349219e+05, 3.09547062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95238031e+05, 3.09544812e+05, ],
  }),
  ("nof_tree_events",                 399992),
  ("nof_db_events",                   399992),
  ("fsize_local",                     1792433729), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21124650657), # 21.12GB, avg file size 1.17GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 384992, ],
    'CountWeighted'                                                                  : [ 3.84885938e+05, 3.84939656e+05, 3.85031531e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.90972156e+05, 4.66187594e+05, 4.42348594e+05, 4.05486719e+05, 3.84885938e+05, 3.65247812e+05, 3.40809750e+05, 3.23515938e+05, 3.06930188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.90972156e+05, 3.06930188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73665938e+05, 3.73671344e+05, 3.73780938e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73665938e+05, 3.70967812e+05, 3.76305156e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.76520688e+05, 4.52576500e+05, 4.29532281e+05, 3.93539188e+05, 3.73665938e+05, 3.54655281e+05, 3.30757406e+05, 3.14059000e+05, 2.98023062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.76520688e+05, 2.98023062e+05, ],
  }),
  ("nof_tree_events",                 384992),
  ("nof_db_events",                   384992),
  ("fsize_local",                     1721373758), # 1.72GB, avg file size 1.72GB
  ("fsize_db",                        20503345442), # 20.50GB, avg file size 1.03GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_8_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99973625e+05, 3.99962781e+05, 3.99921344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09944719e+05, 4.84427062e+05, 4.59848875e+05, 4.21075500e+05, 3.99973625e+05, 3.79626938e+05, 3.53863188e+05, 3.36076312e+05, 3.18965219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09944719e+05, 3.18965219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88379125e+05, 3.88372719e+05, 3.88339750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88379125e+05, 3.85588812e+05, 3.91099625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95057500e+05, 4.70406375e+05, 4.46639125e+05, 4.08771719e+05, 3.88379125e+05, 3.68712688e+05, 3.43514000e+05, 3.26329688e+05, 3.09787188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95057500e+05, 3.09787188e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1786275996), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21039976306), # 21.04GB, avg file size 1.00GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    12),
  ("nof_events",                      {
    'Count'                                                                          : [ 399991, ],
    'CountWeighted'                                                                  : [ 3.99960906e+05, 3.99951125e+05, 3.99946969e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19447438e+05, 4.78882281e+05, 4.43042156e+05, 4.33948844e+05, 3.99960906e+05, 3.69935688e+05, 3.68235062e+05, 3.39303500e+05, 3.13770812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19447438e+05, 3.13770812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86012531e+05, 3.85984531e+05, 3.86022656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86012531e+05, 3.82775000e+05, 3.89207062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01188312e+05, 4.62207281e+05, 4.27747938e+05, 4.18674688e+05, 3.86012531e+05, 3.57146250e+05, 3.55258438e+05, 3.27458812e+05, 3.02911375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01188312e+05, 3.02911375e+05, ],
  }),
  ("nof_tree_events",                 399991),
  ("nof_db_events",                   399991),
  ("fsize_local",                     1997726780), # 2.00GB, avg file size 2.00GB
  ("fsize_db",                        22600644898), # 22.60GB, avg file size 1.88GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_10_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 399986, ],
    'CountWeighted'                                                                  : [ 3.99978375e+05, 3.99962344e+05, 3.99916188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10079625e+05, 4.84326469e+05, 4.59553156e+05, 4.21272125e+05, 3.99978375e+05, 3.79460938e+05, 3.54086125e+05, 3.36115031e+05, 3.18870844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10079625e+05, 3.18870844e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88381531e+05, 3.88353625e+05, 3.88347812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88381531e+05, 3.85588656e+05, 3.91105562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95186812e+05, 4.70303125e+05, 4.46350562e+05, 4.08962719e+05, 3.88381531e+05, 3.68549406e+05, 3.43729500e+05, 3.26369531e+05, 3.09695031e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95186812e+05, 3.09695031e+05, ],
  }),
  ("nof_tree_events",                 399986),
  ("nof_db_events",                   399986),
  ("fsize_local",                     1788637296), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21181482185), # 21.18GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_11_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 395994, ],
    'CountWeighted'                                                                  : [ 3.95966562e+05, 3.95890562e+05, 3.95945000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.05350531e+05, 4.79294000e+05, 4.54333375e+05, 4.17546469e+05, 3.95965594e+05, 3.75321156e+05, 3.51069250e+05, 3.32890031e+05, 3.15505688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.05350531e+05, 3.15505688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.84266594e+05, 3.84202625e+05, 3.84279000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.84266594e+05, 3.81460562e+05, 3.87011781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.90313000e+05, 4.65147156e+05, 4.41026375e+05, 4.05110375e+05, 3.84265219e+05, 3.64316469e+05, 3.40604812e+05, 3.23049375e+05, 3.06249688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.90313000e+05, 3.06249688e+05, ],
  }),
  ("nof_tree_events",                 395994),
  ("nof_db_events",                   395994),
  ("fsize_local",                     1779952009), # 1.78GB, avg file size 1.78GB
  ("fsize_db",                        21005832838), # 21.01GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2v2t"),
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 3.99941562e+05, 3.99938312e+05, 3.99955219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.09953219e+05, 4.84407750e+05, 4.59807344e+05, 4.21095000e+05, 3.99941562e+05, 3.79602812e+05, 3.53883125e+05, 3.36069094e+05, 3.18948000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.09953219e+05, 3.18948000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88355938e+05, 3.88323000e+05, 3.88388562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88355938e+05, 3.85563656e+05, 3.91081531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.95060594e+05, 4.70384188e+05, 4.46597312e+05, 4.08785281e+05, 3.88355938e+05, 3.68686500e+05, 3.43526469e+05, 3.26322438e+05, 3.09770062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.95060594e+05, 3.09770062e+05, ],
  }),
  ("nof_tree_events",                 399993),
  ("nof_db_events",                   399993),
  ("fsize_local",                     1786126379), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21048263593), # 21.05GB, avg file size 1.05GB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    38),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.76452031e+05, 3.76409000e+05, 3.76504016e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.35350672e+05, 4.27786891e+05, 4.22483766e+05, 3.84984438e+05, 3.76452031e+05, 3.69622891e+05, 3.41435375e+05, 3.32648555e+05, 3.25150898e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.50942844e+05, 3.17427094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.76489656e+05, 3.76553828e+05, 5.32995172e+05, 3.76405156e+05, 3.75921500e+05, 2.35506062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.56186133e+04, 2.56147207e+04, 3.63070391e+04, 2.56117451e+04, 2.56266953e+04, 1.60245610e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.67376344e+05, 3.67314594e+05, 3.67446328e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.67376344e+05, 3.65109000e+05, 3.69571016e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.24694344e+05, 4.17409234e+05, 4.12317125e+05, 3.75608844e+05, 3.67376344e+05, 3.60780750e+05, 3.33151734e+05, 3.24656297e+05, 3.17405750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.39929219e+05, 3.09859180e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.67444172e+05, 3.67375609e+05, 5.20025156e+05, 3.67278828e+05, 3.66961391e+05, 2.29930242e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.49970254e+04, 2.49845947e+04, 3.54143516e+04, 2.49843408e+04, 2.50084678e+04, 1.56409512e+04, ],
  }),
  ("nof_tree_events",                 399995),
  ("nof_db_events",                   399995),
  ("fsize_local",                     1715031176), # 1.72GB, avg file size 857.52MB
  ("fsize_db",                        20212438535), # 20.21GB, avg file size 531.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.58664578e+05, 3.58694969e+05, 3.58736641e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08532531e+05, 4.01965062e+05, 3.97629891e+05, 3.66975422e+05, 3.58660812e+05, 3.52198469e+05, 3.29315375e+05, 3.20315781e+05, 3.12769844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.26078359e+05, 3.03235570e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.58745594e+05, 3.58714531e+05, 5.08267297e+05, 3.58657422e+05, 3.58134469e+05, 2.23910938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19841426e+04, 1.19900483e+04, 1.69669697e+04, 1.19844717e+04, 1.19608647e+04, 7.49689673e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.49603875e+05, 3.49602938e+05, 3.49669852e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.49603875e+05, 3.47365516e+05, 3.51781703e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98048891e+05, 3.91743422e+05, 3.87601297e+05, 3.57606578e+05, 3.49597906e+05, 3.43364781e+05, 3.20937078e+05, 3.12245148e+05, 3.04957078e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.15173766e+05, 2.95649828e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.49712562e+05, 3.49545172e+05, 4.95339125e+05, 3.49534555e+05, 3.49208812e+05, 2.18341438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.16773921e+04, 1.16789351e+04, 1.65288525e+04, 1.16743755e+04, 1.16569575e+04, 7.30632324e+03, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1764957465), # 1.76GB, avg file size 882.48MB
  ("fsize_db",                        20236176844), # 20.24GB, avg file size 919.83MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    38),
  ("nof_events",                      {
    'Count'                                                                          : [ 390697, ],
    'CountWeighted'                                                                  : [ 3.37054062e+05, 3.37106891e+05, 3.36997984e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84407469e+05, 3.79149406e+05, 3.75816016e+05, 3.43880484e+05, 3.37047172e+05, 3.31703438e+05, 3.07742516e+05, 3.00217359e+05, 2.93880406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04933266e+05, 2.81345641e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.37108391e+05, 3.36894891e+05, 4.79287891e+05, 3.36975844e+05, 3.37462484e+05, 2.09568719e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.13176123e+03, 5.12825903e+03, 7.30025220e+03, 5.12955151e+03, 5.14287427e+03, 3.19185767e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.28434828e+05, 3.28474641e+05, 3.28398984e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.28434828e+05, 3.26310016e+05, 3.30497891e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.74403859e+05, 3.69380016e+05, 3.66219250e+05, 3.34996516e+05, 3.28427109e+05, 3.23300766e+05, 2.99830938e+05, 2.92581875e+05, 2.86477250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.94433859e+05, 2.74242484e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.28543016e+05, 3.28238906e+05, 4.66890922e+05, 3.28290344e+05, 3.28875422e+05, 2.04317570e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.00058740e+03, 4.99575952e+03, 7.11058545e+03, 4.99666846e+03, 5.01133716e+03, 3.11135181e+03, ],
  }),
  ("nof_tree_events",                 390697),
  ("nof_db_events",                   390697),
  ("fsize_local",                     1727376597), # 1.73GB, avg file size 863.69MB
  ("fsize_db",                        20005894046), # 20.01GB, avg file size 526.47MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_2v2t"),
  ("nof_files",                       2),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 395591, ],
    'CountWeighted'                                                                  : [ 3.89418438e+05, 3.89419125e+05, 3.89478219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.66548969e+05, 4.57673703e+05, 4.50840391e+05, 3.97226266e+05, 3.89406594e+05, 3.82784281e+05, 3.42052453e+05, 3.35138969e+05, 3.28888523e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.80703844e+05, 3.22267430e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89342609e+05, 3.89360219e+05, 5.50976969e+05, 3.89531906e+05, 3.89032734e+05, 2.43976734e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.17307168e+04, 3.17359844e+04, 4.49310332e+04, 3.17464883e+04, 3.17277637e+04, 1.98820684e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.80892109e+05, 3.80871141e+05, 3.80964703e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.80892109e+05, 3.78712109e+05, 3.82985781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.56127219e+05, 4.47568500e+05, 4.40985422e+05, 3.88431609e+05, 3.80881172e+05, 3.74489375e+05, 3.34529906e+05, 3.27852156e+05, 3.21807844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.70001391e+05, 3.15316508e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.80879609e+05, 3.80751062e+05, 5.38840531e+05, 3.80931203e+05, 3.80687219e+05, 2.38754305e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.10366426e+04, 3.10300273e+04, 4.39339668e+04, 3.10415928e+04, 3.10417051e+04, 1.94541187e+04, ],
  }),
  ("nof_tree_events",                 395591),
  ("nof_db_events",                   395591),
  ("fsize_local",                     1584294346), # 1.58GB, avg file size 792.15MB
  ("fsize_db",                        19318646300), # 19.32GB, avg file size 804.94MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_2v2t"),
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

samples_2017["/GluGluToHHTo4V_node_SM_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 379997, ],
    'CountWeighted'                                                                  : [ 3.79965875e+05, 3.79896062e+05, 3.79950438e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.86418750e+05, 4.59095594e+05, 4.33443688e+05, 4.02671125e+05, 3.79964438e+05, 3.58676875e+05, 3.39120812e+05, 3.19925250e+05, 3.01956125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.86418750e+05, 3.01956125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.68965188e+05, 3.68896094e+05, 3.68987688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.68965188e+05, 3.66313375e+05, 3.71547281e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.72210125e+05, 4.45827906e+05, 4.21037000e+05, 3.90886156e+05, 3.68963375e+05, 3.48391875e+05, 3.29178969e+05, 3.10650531e+05, 2.93284438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.72210125e+05, 2.93284438e+05, ],
  }),
  ("nof_tree_events",                 379997),
  ("nof_db_events",                   379997),
  ("fsize_local",                     1772266263), # 1.77GB, avg file size 1.77GB
  ("fsize_db",                        20701310914), # 20.70GB, avg file size 1.22GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_1_TuneCP5_PSWeights_13TeV-madgraph-pythia8_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_4v"),
  ("nof_files",                       17),
  ("nof_db_files",                    91),
  ("nof_events",                      {
    'Count'                                                                          : [ 3860978, ],
    'CountWeighted'                                                                  : [ 3.86059046e+06, 3.86074228e+06, 3.86075109e+06, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92384967e+06, 4.67519711e+06, 4.43632301e+06, 4.06653130e+06, 3.86054673e+06, 3.66306979e+06, 3.41786931e+06, 3.24455997e+06, 3.07818364e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92385086e+06, 3.07818263e+06, ],
    'CountWeightedPSWeight'                                                          : [ 3.86075052e+07, 3.85973461e+07, 3.86075247e+07, 3.86075015e+07, 3.83782673e+07, 3.83680642e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.86094441e+06, 3.86148071e+06, 5.62454573e+06, 3.86101314e+06, 3.85239867e+06, 2.29320403e+06, ],
    'CountWeightedFull'                                                              : [ 3.85947400e+06, 3.85962178e+06, 3.85962818e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92242262e+06, 4.67384363e+06, 4.43503863e+06, 4.06535383e+06, 3.85943054e+06, 3.66200973e+06, 3.41687893e+06, 3.24362099e+06, 3.07729243e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92242381e+06, 3.07729138e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.85963460e+07, 3.85861708e+07, 3.85963470e+07, 3.85963453e+07, 3.83671583e+07, 3.83569807e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85985370e+06, 3.86036744e+06, 5.62290872e+06, 3.85987457e+06, 3.85127680e+06, 2.29254612e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75448029e+06, 3.75442790e+06, 3.75471560e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75448029e+06, 3.72862270e+06, 3.77957061e+06, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.78735752e+06, 4.54677307e+06, 4.31540830e+06, 3.95367998e+06, 3.75444394e+06, 3.56311734e+06, 3.32292635e+06, 3.15524319e+06, 2.99410956e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.78735861e+06, 2.99410850e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.75457303e+07, 3.75358705e+07, 3.75457418e+07, 3.75457283e+07, 3.73245683e+07, 3.73146837e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.75909316e+06, 3.75395236e+06, 5.46843771e+06, 3.74927702e+06, 3.74849204e+06, 2.23152572e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75340498e+06, 3.75335118e+06, 3.75363717e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75340498e+06, 3.72755774e+06, 3.77848592e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.78598464e+06, 4.54547067e+06, 4.31417196e+06, 3.95254684e+06, 3.75336874e+06, 3.56209714e+06, 3.32197314e+06, 3.15433929e+06, 2.99325188e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.78598573e+06, 2.99325085e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75349875e+07, 3.75251204e+07, 3.75349880e+07, 3.75349872e+07, 3.73138802e+07, 3.73040111e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75804132e+06, 3.75288216e+06, 5.46686367e+06, 3.74818171e+06, 3.74741259e+06, 2.23089093e+06, ],
  }),
  ("nof_tree_events",                 3860978),
  ("nof_db_events",                   3860978),
  ("fsize_local",                     17713270175), # 17.71GB, avg file size 1.04GB
  ("fsize_db",                        209053196536), # 209.05GB, avg file size 2.30GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   4),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_2_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_2_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99956500e+05, 3.99890062e+05, 3.99849375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19677375e+05, 4.78803281e+05, 4.42871625e+05, 4.34290438e+05, 3.99956500e+05, 3.69738844e+05, 3.68675250e+05, 3.39330938e+05, 3.13603031e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19677438e+05, 3.13602938e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86454688e+05, 3.86414562e+05, 3.86391906e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86454688e+05, 3.83314875e+05, 3.89539812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01965125e+05, 4.62712062e+05, 4.28177188e+05, 4.19440812e+05, 3.86454688e+05, 3.57426219e+05, 3.56030469e+05, 3.27856438e+05, 3.03131312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01965219e+05, 3.03131250e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1986460975), # 1.99GB, avg file size 1.99GB
  ("fsize_db",                        23052019817), # 23.05GB, avg file size 1.54GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_3_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_3_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 382999, ],
    'CountWeighted'                                                                  : [ 3.82919406e+05, 3.83001250e+05, 3.82988594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.90277438e+05, 4.62670438e+05, 4.36736062e+05, 4.05892938e+05, 3.82919406e+05, 3.61453125e+05, 3.41837688e+05, 3.22477000e+05, 3.04324156e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.90277438e+05, 3.04324156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.71783188e+05, 3.71816312e+05, 3.71840812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.71783188e+05, 3.69098750e+05, 3.74398531e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.75876312e+05, 4.49214031e+05, 4.24144938e+05, 3.93951656e+05, 3.71783188e+05, 3.51014656e+05, 3.31768719e+05, 3.13072812e+05, 2.95525375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.75876312e+05, 2.95525375e+05, ],
  }),
  ("nof_tree_events",                 382999),
  ("nof_db_events",                   382999),
  ("fsize_local",                     1797409170), # 1.80GB, avg file size 1.80GB
  ("fsize_db",                        20935006290), # 20.94GB, avg file size 951.59MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_4_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 391999, ],
    'CountWeighted'                                                                  : [ 3.92007438e+05, 3.92043531e+05, 3.91910344e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.99819625e+05, 4.74721438e+05, 4.50576125e+05, 4.12762062e+05, 3.92007438e+05, 3.72001781e+05, 3.46906500e+05, 3.29397062e+05, 3.12567688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.99819625e+05, 3.12567688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81311156e+05, 3.81321906e+05, 3.81263281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81311156e+05, 3.78704281e+05, 3.83836250e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.86083094e+05, 4.61796344e+05, 4.38404719e+05, 4.01403469e+05, 3.81311156e+05, 3.61939062e+05, 3.37348188e+05, 3.20404469e+05, 3.04106562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.86083094e+05, 3.04106562e+05, ],
  }),
  ("nof_tree_events",                 391999),
  ("nof_db_events",                   391999),
  ("fsize_local",                     1788057498), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21344876204), # 21.34GB, avg file size 970.22MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_5_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_5_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 3.99899000e+05, 3.99932625e+05, 3.99929875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.12975031e+05, 4.82669938e+05, 4.54490562e+05, 4.25171094e+05, 3.99899000e+05, 3.76546469e+05, 3.58426125e+05, 3.37101812e+05, 3.17319656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.12975344e+05, 3.17319375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87974750e+05, 3.87963750e+05, 3.88025875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87974750e+05, 3.85110562e+05, 3.90771125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.97518562e+05, 4.68274375e+05, 4.41064094e+05, 4.12337938e+05, 3.87974750e+05, 3.65403219e+05, 3.47591719e+05, 3.27016812e+05, 3.07913562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.97518844e+05, 3.07913312e+05, ],
  }),
  ("nof_tree_events",                 399999),
  ("nof_db_events",                   399999),
  ("fsize_local",                     1890750332), # 1.89GB, avg file size 1.89GB
  ("fsize_db",                        22416145291), # 22.42GB, avg file size 1.07GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_6_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_6_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.96038625e+05, 3.95940750e+05, 3.95938750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.05183812e+05, 4.79426000e+05, 4.54701750e+05, 4.17308281e+05, 3.96032125e+05, 3.75533750e+05, 3.50806062e+05, 3.32836250e+05, 3.15618531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.05183812e+05, 3.15618531e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85039500e+05, 3.84974250e+05, 3.84980781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85039500e+05, 3.82364906e+05, 3.87629062e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.91073125e+05, 4.66147969e+05, 4.42203344e+05, 4.05637781e+05, 3.85033906e+05, 3.65199375e+05, 3.40985750e+05, 3.23600188e+05, 3.06928625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.91073125e+05, 3.06928625e+05, ],
  }),
  ("nof_tree_events",                 396000),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1814756331), # 1.81GB, avg file size 1.81GB
  ("fsize_db",                        21470016217), # 21.47GB, avg file size 1.34GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_7_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99895844e+05, 3.99970688e+05, 4.00048000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10129688e+05, 4.84349062e+05, 4.59582969e+05, 4.21310719e+05, 3.99895844e+05, 3.79486125e+05, 3.54112688e+05, 3.36147031e+05, 3.18893312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10129688e+05, 3.18893312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88968625e+05, 3.88986688e+05, 3.89082812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88968625e+05, 3.86297938e+05, 3.91559031e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96042688e+05, 4.71092750e+05, 4.47095562e+05, 4.09665250e+05, 3.88968625e+05, 3.69165500e+05, 3.44316094e+05, 3.26925438e+05, 3.10213844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96042688e+05, 3.10213844e+05, ],
  }),
  ("nof_tree_events",                 400000),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1828878568), # 1.83GB, avg file size 1.83GB
  ("fsize_db",                        21847137342), # 21.85GB, avg file size 1.04GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_8_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_8_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 395995, ],
    'CountWeighted'                                                                  : [ 3.96045906e+05, 3.95933656e+05, 3.95999188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.04858656e+05, 4.79596750e+05, 4.55260438e+05, 4.16883562e+05, 3.96045906e+05, 3.75841719e+05, 3.50342125e+05, 3.32726938e+05, 3.15789469e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.04858656e+05, 3.15789469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.85262688e+05, 3.85175062e+05, 3.85244531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.85262688e+05, 3.82633281e+05, 3.87808906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.91035688e+05, 4.66583500e+05, 4.43006062e+05, 4.05457938e+05, 3.85262688e+05, 3.65714469e+05, 3.40728812e+05, 3.23680188e+05, 3.07271219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.91035688e+05, 3.07271219e+05, ],
  }),
  ("nof_tree_events",                 395995),
  ("nof_db_events",                   395995),
  ("fsize_local",                     1806742986), # 1.81GB, avg file size 1.81GB
  ("fsize_db",                        21294763606), # 21.29GB, avg file size 1.25GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_9_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_9_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.99939688e+05, 3.99878250e+05, 3.99909312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.19409375e+05, 4.78830938e+05, 4.42995188e+05, 4.33928562e+05, 3.99939688e+05, 3.69907062e+05, 3.68228656e+05, 3.39285312e+05, 3.13755312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.19409375e+05, 3.13755312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86364875e+05, 3.86311938e+05, 3.86365125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86364875e+05, 3.83196188e+05, 3.89477125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 5.01643875e+05, 4.62618688e+05, 4.28127312e+05, 4.19061062e+05, 3.86364875e+05, 3.57469062e+05, 3.55594031e+05, 3.27759438e+05, 3.03191469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 5.01643875e+05, 3.03191469e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     2029419511), # 2.03GB, avg file size 2.03GB
  ("fsize_db",                        23472759858), # 23.47GB, avg file size 1.02GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_10_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_10_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 391996, ],
    'CountWeighted'                                                                  : [ 3.91944812e+05, 3.92051688e+05, 3.91874250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.99933438e+05, 4.74655875e+05, 4.50354312e+05, 4.12904938e+05, 3.91934219e+05, 3.71872719e+05, 3.47049906e+05, 3.29414625e+05, 3.12498125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.99933500e+05, 3.12498062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.81137188e+05, 3.81204000e+05, 3.81099875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.81137188e+05, 3.78513906e+05, 3.83691688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.86030469e+05, 4.61576750e+05, 4.38046438e+05, 4.01406562e+05, 3.81128875e+05, 3.61697375e+05, 3.37377125e+05, 3.20319469e+05, 3.03938625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.86030531e+05, 3.03938562e+05, ],
  }),
  ("nof_tree_events",                 391996),
  ("nof_db_events",                   391996),
  ("fsize_local",                     1792867546), # 1.79GB, avg file size 1.79GB
  ("fsize_db",                        21244437020), # 21.24GB, avg file size 1.18GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_11_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_11_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 4.00010656e+05, 4.00003875e+05, 3.99939062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10460438e+05, 4.84147688e+05, 4.58939656e+05, 4.21770750e+05, 4.00003094e+05, 3.79123031e+05, 3.54620875e+05, 3.36252500e+05, 3.18700500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10460438e+05, 3.18700438e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.88927562e+05, 3.88908844e+05, 3.88892250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.88927562e+05, 3.86229469e+05, 3.91539719e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96225781e+05, 4.70762000e+05, 4.46351000e+05, 4.09997094e+05, 3.88921562e+05, 3.68713031e+05, 3.44711531e+05, 3.26939438e+05, 3.09941438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96225781e+05, 3.09941375e+05, ],
  }),
  ("nof_tree_events",                 399997),
  ("nof_db_events",                   399997),
  ("fsize_local",                     1838375868), # 1.84GB, avg file size 1.84GB
  ("fsize_db",                        21689984880), # 21.69GB, avg file size 1.28GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_12_13TeV-madgraph_correctedcfg/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4v"),
  ("nof_files",                       1),
  ("nof_db_files",                    13),
  ("nof_events",                      {
    'Count'                                                                          : [ 394000, ],
    'CountWeighted'                                                                  : [ 3.93914000e+05, 3.93999125e+05, 3.93941625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.02311688e+05, 4.77199875e+05, 4.52976438e+05, 4.14771188e+05, 3.93913781e+05, 3.73949656e+05, 3.48555938e+05, 3.31031625e+05, 3.14192531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.02311688e+05, 3.14192500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.83178438e+05, 3.83230594e+05, 3.83198281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.83178438e+05, 3.80554438e+05, 3.85723469e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.88490469e+05, 4.64181812e+05, 4.40721219e+05, 4.03344688e+05, 3.83177500e+05, 3.63822062e+05, 3.38941844e+05, 3.21988000e+05, 3.05674562e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.88490469e+05, 3.05674562e+05, ],
  }),
  ("nof_tree_events",                 394000),
  ("nof_db_events",                   394000),
  ("fsize_local",                     1796731124), # 1.80GB, avg file size 1.80GB
  ("fsize_db",                        21086443719), # 21.09GB, avg file size 1.62GB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Apr12_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_cHHH0_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH0_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH0_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    74),
  ("nof_events",                      {
    'Count'                                                                          : [ 999992, ],
    'CountWeighted'                                                                  : [ 9.41119406e+05, 9.41134438e+05, 9.41174672e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08848938e+06, 1.06943397e+06, 1.05603791e+06, 9.62564438e+05, 9.41119406e+05, 9.23902156e+05, 8.53666297e+05, 8.31616297e+05, 8.12804453e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12731481e+06, 7.93624109e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.41173578e+05, 9.40441203e+05, 1.36379288e+06, 9.41065375e+05, 9.40416656e+05, 5.61377844e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.40770859e+04, 6.40472568e+04, 9.29430566e+04, 6.40752812e+04, 6.40893955e+04, 3.82120332e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.20508469e+05, 9.20495797e+05, 9.20556891e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.20508469e+05, 9.15248594e+05, 9.25547594e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06430072e+06, 1.04588623e+06, 1.03297352e+06, 9.41276875e+05, 9.20508469e+05, 9.03837562e+05, 8.34847781e+05, 8.13468203e+05, 7.95223312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10231338e+06, 7.76451312e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.20656547e+05, 9.19604219e+05, 1.33380159e+06, 9.20329859e+05, 9.20236375e+05, 5.49321312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 6.26621465e+04, 6.26096533e+04, 9.08732656e+04, 6.26446582e+04, 6.26964883e+04, 3.73802373e+04, ],
  }),
  ("nof_tree_events",                 999992),
  ("nof_db_events",                   999992),
  ("fsize_local",                     4401470243), # 4.40GB, avg file size 1.10GB
  ("fsize_db",                        51563406070), # 51.56GB, avg file size 696.80MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_cHHH1_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH1_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH1_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    53),
  ("nof_events",                      {
    'Count'                                                                          : [ 963693, ],
    'CountWeighted'                                                                  : [ 8.63450016e+05, 8.63367266e+05, 8.63424750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82849672e+05, 9.67203906e+05, 9.56899797e+05, 8.83250281e+05, 8.63397766e+05, 8.47807328e+05, 7.92834906e+05, 7.71213641e+05, 7.53099594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02526606e+06, 7.29957922e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.63095891e+05, 8.63102750e+05, 1.25243769e+06, 8.63811203e+05, 8.62238203e+05, 5.13989227e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.87884595e+04, 2.87794463e+04, 4.18346475e+04, 2.88078604e+04, 2.88346841e+04, 1.71462507e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.43204516e+05, 8.43106953e+05, 8.43250016e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.43204516e+05, 8.38113344e+05, 8.48108016e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.59494344e+05, 9.44426438e+05, 9.34551547e+05, 8.62364719e+05, 8.43161188e+05, 8.28120047e+05, 7.74151203e+05, 7.53219656e+05, 7.35683984e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00095155e+06, 7.13069219e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.42988812e+05, 8.42615781e+05, 1.22296388e+06, 8.43443625e+05, 8.42471328e+05, 5.02190227e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.81098574e+04, 2.80885757e+04, 4.08382002e+04, 2.81204941e+04, 2.81652051e+04, 1.67481890e+04, ],
  }),
  ("nof_tree_events",                 963693),
  ("nof_db_events",                   963693),
  ("fsize_local",                     4378289511), # 4.38GB, avg file size 1.09GB
  ("fsize_db",                        50159794192), # 50.16GB, avg file size 946.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_cHHH2p45_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH2p45_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH2p45_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    63),
  ("nof_events",                      {
    'Count'                                                                          : [ 999996, ],
    'CountWeighted'                                                                  : [ 8.61863875e+05, 8.61982250e+05, 8.61825766e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82960656e+05, 9.69436703e+05, 9.60813750e+05, 8.79381031e+05, 8.61859562e+05, 8.48131438e+05, 7.87038484e+05, 7.67738531e+05, 7.51484406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03520162e+06, 7.19598891e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.61759328e+05, 8.61961891e+05, 1.25138638e+06, 8.62003328e+05, 8.59598266e+05, 5.11507648e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31346560e+04, 1.31395608e+04, 1.90839604e+04, 1.31356467e+04, 1.31121006e+04, 7.79717847e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.41422500e+05, 8.41514828e+05, 8.41412672e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.41422500e+05, 8.36309672e+05, 8.46344562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.59272156e+05, 9.46309797e+05, 9.38103672e+05, 8.58303922e+05, 8.41411438e+05, 8.28213453e+05, 7.68245375e+05, 7.49613031e+05, 7.33916844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01033717e+06, 7.02750000e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.41472859e+05, 8.41378281e+05, 1.22141400e+06, 8.41381922e+05, 8.39388172e+05, 4.99638648e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.28201785e+04, 1.28202644e+04, 1.86203154e+04, 1.28161887e+04, 1.27997498e+04, 7.61287659e+03, ],
  }),
  ("nof_tree_events",                 999996),
  ("nof_db_events",                   999996),
  ("fsize_local",                     4512892780), # 4.51GB, avg file size 1.13GB
  ("fsize_db",                        52111900186), # 52.11GB, avg file size 827.17MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4v"),
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

samples_2017["/GluGluToHHTo4V_node_cHHH5_TuneCP5_PSWeights_13TeV-powheg-pythia8/RunIIFall17MiniAODv2-PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/MINIAODSIM"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_cHHH5_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_cHHH5_hh_4v"),
  ("nof_files",                       4),
  ("nof_db_files",                    42),
  ("nof_events",                      {
    'Count'                                                                          : [ 999995, ],
    'CountWeighted'                                                                  : [ 9.84275656e+05, 9.84303500e+05, 9.84293141e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17920944e+06, 1.15681609e+06, 1.13958131e+06, 1.00401247e+06, 9.84226984e+05, 9.67553484e+05, 8.64512688e+05, 8.47067938e+05, 8.31296969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.21512141e+06, 8.14476547e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.84252172e+05, 9.84553141e+05, 1.42333678e+06, 9.84319641e+05, 9.80600391e+05, 5.87952312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.02275254e+04, 8.02429199e+04, 1.16176324e+05, 8.02310312e+04, 8.00910312e+04, 4.79213594e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.64972891e+05, 9.64956109e+05, 9.65030250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.64972891e+05, 9.59940953e+05, 9.69747781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.15552272e+06, 1.13387078e+06, 1.11722822e+06, 9.84076406e+05, 9.64932625e+05, 9.48785594e+05, 8.47497375e+05, 8.30600688e+05, 8.15308875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.19081250e+06, 7.98778875e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.65100312e+05, 9.65005422e+05, 1.39513622e+06, 9.64824391e+05, 9.61752469e+05, 5.76758875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.86593789e+04, 7.86422383e+04, 1.13863523e+05, 7.86346445e+04, 7.85438438e+04, 4.70043604e+04, ],
  }),
  ("nof_tree_events",                 999995),
  ("nof_db_events",                   999995),
  ("fsize_local",                     4052868482), # 4.05GB, avg file size 1.01GB
  ("fsize_db",                        49489862385), # 49.49GB, avg file size 1.18GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020May11_woPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4v"),
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

samples_2017["/GluGluToHHTo4Tau_node_SM_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99858516e+05, 9.99790797e+05, 9.99819391e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27992925e+06, 1.20810925e+06, 1.14071462e+06, 1.05955044e+06, 9.99858516e+05, 9.43905672e+05, 8.92298328e+05, 8.41875734e+05, 7.94625125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27992969e+06, 7.94624562e+05, ],
    'CountWeightedFull'                                                              : [ 9.99858516e+05, 9.99790797e+05, 9.99819391e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27992925e+06, 1.20810925e+06, 1.14071462e+06, 1.05955044e+06, 9.99858516e+05, 9.43905672e+05, 8.92298328e+05, 8.41875734e+05, 7.94625125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27992969e+06, 7.94624562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.67702750e+05, 9.67630875e+05, 9.67693406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.67702750e+05, 9.60102828e+05, 9.75182438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23842566e+06, 1.16930088e+06, 1.10437191e+06, 1.02514894e+06, 9.67702750e+05, 9.13794797e+05, 8.63294625e+05, 8.14768125e+05, 7.69248703e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23842584e+06, 7.69248375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.67702750e+05, 9.67630875e+05, 9.67693406e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.67702750e+05, 9.60102828e+05, 9.75182438e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23842566e+06, 1.16930088e+06, 1.10437191e+06, 1.02514894e+06, 9.67702750e+05, 9.13794797e+05, 8.63294625e+05, 8.14768125e+05, 7.69248703e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23842584e+06, 7.69248375e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4376791713), # 4.38GB, avg file size 1.09GB
  ("fsize_db",                        79886965724), # 79.89GB, avg file size 19.97MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_4t_private"),
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

samples_2017["/GluGluToHHTo4Tau_node_1_TuneCP5_PSWeights_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_4t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99929078e+05, 9.99898500e+05, 9.99967609e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27521769e+06, 1.21088262e+06, 1.14908469e+06, 1.05314684e+06, 9.99929078e+05, 9.48763516e+05, 8.85127828e+05, 8.40294453e+05, 7.97246172e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27521769e+06, 7.97246203e+05, ],
    'CountWeightedFull'                                                              : [ 9.99929078e+05, 9.99898500e+05, 9.99967609e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27521769e+06, 1.21088262e+06, 1.14908469e+06, 1.05314684e+06, 9.99929078e+05, 9.48763516e+05, 8.85127828e+05, 8.40294453e+05, 7.97246172e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27521769e+06, 7.97246203e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69038203e+05, 9.68973016e+05, 9.69102172e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69038203e+05, 9.61677469e+05, 9.76255125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23552703e+06, 1.17351859e+06, 1.11388603e+06, 1.02034017e+06, 9.69038203e+05, 9.19676219e+05, 8.57537109e+05, 8.14323422e+05, 7.72786469e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23552703e+06, 7.72786500e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69038203e+05, 9.68973016e+05, 9.69102172e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69038203e+05, 9.61677469e+05, 9.76255125e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23552703e+06, 1.17351859e+06, 1.11388603e+06, 1.02034017e+06, 9.69038203e+05, 9.19676219e+05, 8.57537109e+05, 8.14323422e+05, 7.72786469e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23552703e+06, 7.72786500e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4271834134), # 4.27GB, avg file size 1.07GB
  ("fsize_db",                        79103654607), # 79.10GB, avg file size 19.78MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_4t_private"),
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

samples_2017["/GluGluToHHTo4Tau_node_4_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99904219e+05, 9.99904859e+05, 9.99878578e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27509575e+06, 1.21106028e+06, 1.14948300e+06, 1.05296638e+06, 9.99904219e+05, 9.48985125e+05, 8.84936078e+05, 8.40276719e+05, 7.97369016e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27509575e+06, 7.97369062e+05, ],
    'CountWeightedFull'                                                              : [ 9.99904219e+05, 9.99904859e+05, 9.99878578e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27509575e+06, 1.21106028e+06, 1.14948300e+06, 1.05296638e+06, 9.99904219e+05, 9.48985125e+05, 8.84936078e+05, 8.40276719e+05, 7.97369016e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27509575e+06, 7.97369062e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68915703e+05, 9.68858625e+05, 9.68962594e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68915703e+05, 9.61534922e+05, 9.76161953e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23525009e+06, 1.17354981e+06, 1.11414953e+06, 1.02003208e+06, 9.68915703e+05, 9.19787125e+05, 8.57234078e+05, 8.14201391e+05, 7.72814703e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23525009e+06, 7.72814734e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.68915703e+05, 9.68858625e+05, 9.68962594e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.68915703e+05, 9.61534922e+05, 9.76161953e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23525009e+06, 1.17354981e+06, 1.11414953e+06, 1.02003208e+06, 9.68915703e+05, 9.19787125e+05, 8.57234078e+05, 8.14201391e+05, 7.72814703e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23525009e+06, 7.72814734e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4272051380), # 4.27GB, avg file size 1.07GB
  ("fsize_db",                        79167526635), # 79.17GB, avg file size 19.79MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_4t_private"),
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

samples_2017["/GluGluToHHTo4Tau_node_7_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99893953e+05, 9.99973094e+05, 9.99896484e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27525822e+06, 1.21086588e+06, 1.14897156e+06, 1.05320850e+06, 9.99893953e+05, 9.48695969e+05, 8.85194828e+05, 8.40311875e+05, 7.97213000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27525822e+06, 7.97213000e+05, ],
    'CountWeightedFull'                                                              : [ 9.99893953e+05, 9.99973094e+05, 9.99896484e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27525822e+06, 1.21086588e+06, 1.14897156e+06, 1.05320850e+06, 9.99893953e+05, 9.48695969e+05, 8.85194828e+05, 8.40311875e+05, 7.97213000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27525822e+06, 7.97213000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68778797e+05, 9.68800922e+05, 9.68812703e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68778797e+05, 9.61380500e+05, 9.76048438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23527222e+06, 1.17321525e+06, 1.11351006e+06, 1.02015856e+06, 9.68778797e+05, 9.19393453e+05, 8.57398406e+05, 8.14143172e+05, 7.72569781e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23527222e+06, 7.72569750e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.68778797e+05, 9.68800922e+05, 9.68812703e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.68778797e+05, 9.61380500e+05, 9.76048438e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23527222e+06, 1.17321525e+06, 1.11351006e+06, 1.02015856e+06, 9.68778797e+05, 9.19393453e+05, 8.57398406e+05, 8.14143172e+05, 7.72569781e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23527222e+06, 7.72569750e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4272405579), # 4.27GB, avg file size 1.07GB
  ("fsize_db",                        79131507440), # 79.13GB, avg file size 19.78MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_4t_private"),
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

samples_2017["/GluGluToHHTo4Tau_node_12_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_tttt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99910969e+05, 9.99870719e+05, 9.99921297e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27489444e+06, 1.21113812e+06, 1.14975291e+06, 1.05269766e+06, 9.99910969e+05, 9.49152969e+05, 8.84625859e+05, 8.40204938e+05, 7.97462094e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27489444e+06, 7.97462094e+05, ],
    'CountWeightedFull'                                                              : [ 9.99910969e+05, 9.99870719e+05, 9.99921297e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27489444e+06, 1.21113812e+06, 1.14975291e+06, 1.05269766e+06, 9.99910969e+05, 9.49152969e+05, 8.84625859e+05, 8.40204938e+05, 7.97462094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27489444e+06, 7.97462094e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68832438e+05, 9.68773938e+05, 9.68872688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68832438e+05, 9.61432703e+05, 9.76093688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23494838e+06, 1.17350844e+06, 1.11429412e+06, 1.01968627e+06, 9.68832438e+05, 9.19856781e+05, 8.56866406e+05, 8.14059062e+05, 7.72829828e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23494838e+06, 7.72829859e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.68832438e+05, 9.68773938e+05, 9.68872688e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.68832438e+05, 9.61432703e+05, 9.76093688e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23494838e+06, 1.17350844e+06, 1.11429412e+06, 1.01968627e+06, 9.68832438e+05, 9.19856781e+05, 8.56866406e+05, 8.14059062e+05, 7.72829828e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23494838e+06, 7.72829859e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4263886802), # 4.26GB, avg file size 1.07GB
  ("fsize_db",                        78754180682), # 78.75GB, avg file size 19.69MB
  ("use_it",                          True),
  ("xsection",                        0.003934),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_4t_private"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_SM_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_2v2t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999997, ],
    'CountWeighted'                                                                  : [ 9.99903359e+05, 9.99921766e+05, 9.99833094e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27995988e+06, 1.20820184e+06, 1.14085306e+06, 1.05955109e+06, 9.99903359e+05, 9.43999219e+05, 8.92282719e+05, 8.41897469e+05, 7.94685875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27995994e+06, 7.94685812e+05, ],
    'CountWeightedFull'                                                              : [ 9.99903359e+05, 9.99921766e+05, 9.99833094e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27995988e+06, 1.20820184e+06, 1.14085306e+06, 1.05955109e+06, 9.99903359e+05, 9.43999219e+05, 8.92282719e+05, 8.41897469e+05, 7.94685875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27995994e+06, 7.94685812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69409469e+05, 9.69355859e+05, 9.69427219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69409469e+05, 9.62122750e+05, 9.76535922e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24057641e+06, 1.17140794e+06, 1.10641916e+06, 1.02689742e+06, 9.69409469e+05, 9.15462344e+05, 8.64744891e+05, 8.16183016e+05, 7.70629844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24057644e+06, 7.70629781e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69409469e+05, 9.69355859e+05, 9.69427219e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69409469e+05, 9.62122750e+05, 9.76535922e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.24057641e+06, 1.17140794e+06, 1.10641916e+06, 1.02689742e+06, 9.69409469e+05, 9.15462344e+05, 8.64744891e+05, 8.16183016e+05, 7.70629844e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24057644e+06, 7.70629781e+05, ],
  }),
  ("nof_tree_events",                 999997),
  ("nof_db_events",                   999997),
  ("fsize_local",                     4573264862), # 4.57GB, avg file size 1.14GB
  ("fsize_db",                        81657974168), # 81.66GB, avg file size 20.41MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t_private"),
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

samples_2017["/GluGluToHHTo2V2tau_node_1_TuneCP5_PSWeights_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_2v2t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999998, ],
    'CountWeighted'                                                                  : [ 9.99833078e+05, 9.99856312e+05, 9.99926625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27524259e+06, 1.21084709e+06, 1.14896334e+06, 1.05319641e+06, 9.99833078e+05, 9.48682609e+05, 8.85187125e+05, 8.40304531e+05, 7.97196594e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27524278e+06, 7.97196469e+05, ],
    'CountWeightedFull'                                                              : [ 9.99833078e+05, 9.99856312e+05, 9.99926625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27524259e+06, 1.21084709e+06, 1.14896334e+06, 1.05319641e+06, 9.99833078e+05, 9.48682609e+05, 8.85187125e+05, 8.40304531e+05, 7.97196594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27524278e+06, 7.97196469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70534219e+05, 9.70509109e+05, 9.70646375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70534219e+05, 9.63484281e+05, 9.77429906e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23755891e+06, 1.17538178e+06, 1.11557338e+06, 1.02204270e+06, 9.70534219e+05, 9.21083531e+05, 8.58980406e+05, 8.15643297e+05, 7.73984688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23755912e+06, 7.73984562e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70534219e+05, 9.70509109e+05, 9.70646375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70534219e+05, 9.63484281e+05, 9.77429906e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23755891e+06, 1.17538178e+06, 1.11557338e+06, 1.02204270e+06, 9.70534219e+05, 9.21083531e+05, 8.58980406e+05, 8.15643297e+05, 7.73984688e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23755912e+06, 7.73984562e+05, ],
  }),
  ("nof_tree_events",                 999998),
  ("nof_db_events",                   999998),
  ("fsize_local",                     4475508162), # 4.48GB, avg file size 1.12GB
  ("fsize_db",                        80767326118), # 80.77GB, avg file size 20.19MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_2v2t_private"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_4_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_2v2t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999998, ],
    'CountWeighted'                                                                  : [ 9.99908750e+05, 9.99909375e+05, 9.99877625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27508053e+06, 1.21102388e+06, 1.14941631e+06, 1.05296028e+06, 9.99908750e+05, 9.48933766e+05, 8.84930984e+05, 8.40252328e+05, 7.97328219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27508250e+06, 7.97326516e+05, ],
    'CountWeightedFull'                                                              : [ 9.99908750e+05, 9.99909375e+05, 9.99877625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27508053e+06, 1.21102388e+06, 1.14941631e+06, 1.05296028e+06, 9.99908750e+05, 9.48933766e+05, 8.84930984e+05, 8.40252328e+05, 7.97328219e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27508250e+06, 7.97326516e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70611484e+05, 9.70561469e+05, 9.70646344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70611484e+05, 9.63562891e+05, 9.77497812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23741459e+06, 1.17557878e+06, 1.11604531e+06, 1.02181794e+06, 9.70611484e+05, 9.21350984e+05, 8.58732250e+05, 8.15604031e+05, 7.74128484e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23741609e+06, 7.74127219e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70611484e+05, 9.70561469e+05, 9.70646344e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70611484e+05, 9.63562891e+05, 9.77497812e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23741459e+06, 1.17557878e+06, 1.11604531e+06, 1.02181794e+06, 9.70611484e+05, 9.21350984e+05, 8.58732250e+05, 8.15604031e+05, 7.74128484e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23741609e+06, 7.74127219e+05, ],
  }),
  ("nof_tree_events",                 999998),
  ("nof_db_events",                   999998),
  ("fsize_local",                     4469207024), # 4.47GB, avg file size 1.12GB
  ("fsize_db",                        80793399079), # 80.79GB, avg file size 20.20MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t_private"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_7_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_2v2t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999998, ],
    'CountWeighted'                                                                  : [ 9.99917719e+05, 9.99905812e+05, 9.99876250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27527003e+06, 1.21089506e+06, 1.14901997e+06, 1.05320250e+06, 9.99917719e+05, 9.48730203e+05, 8.85189094e+05, 8.40309750e+05, 7.97234984e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27527041e+06, 7.97234609e+05, ],
    'CountWeightedFull'                                                              : [ 9.99917719e+05, 9.99905812e+05, 9.99876250e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27527003e+06, 1.21089506e+06, 1.14901997e+06, 1.05320250e+06, 9.99917719e+05, 9.48730203e+05, 8.85189094e+05, 8.40309750e+05, 7.97234984e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27527041e+06, 7.97234609e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70575922e+05, 9.70544688e+05, 9.70566984e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70575922e+05, 9.63513750e+05, 9.77472047e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23755622e+06, 1.17539503e+06, 1.11559294e+06, 1.02202511e+06, 9.70575922e+05, 9.21103078e+05, 8.58962875e+05, 8.15634297e+05, 7.73999234e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23755644e+06, 7.73999016e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70575922e+05, 9.70544688e+05, 9.70566984e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70575922e+05, 9.63513750e+05, 9.77472047e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23755622e+06, 1.17539503e+06, 1.11559294e+06, 1.02202511e+06, 9.70575922e+05, 9.21103078e+05, 8.58962875e+05, 8.15634297e+05, 7.73999234e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23755644e+06, 7.73999016e+05, ],
  }),
  ("nof_tree_events",                 999998),
  ("nof_db_events",                   999998),
  ("fsize_local",                     4475434184), # 4.48GB, avg file size 1.12GB
  ("fsize_db",                        80792256740), # 80.79GB, avg file size 20.20MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t_private"),
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

samples_2017["/GluGluToHHTo2V2Tau_node_12_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwtt"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_2v2t_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999996, ],
    'CountWeighted'                                                                  : [ 9.99900656e+05, 9.99897062e+05, 9.99880469e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27485772e+06, 1.21112388e+06, 1.14973662e+06, 1.05265984e+06, 9.99900656e+05, 9.49132484e+05, 8.84588938e+05, 8.40172250e+05, 7.97439406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27485922e+06, 7.97439359e+05, ],
    'CountWeightedFull'                                                              : [ 9.99900656e+05, 9.99897062e+05, 9.99880469e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27485772e+06, 1.21112388e+06, 1.14973662e+06, 1.05265984e+06, 9.99900656e+05, 9.49132484e+05, 8.84588938e+05, 8.40172250e+05, 7.97439406e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27485922e+06, 7.97439359e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70736391e+05, 9.70711328e+05, 9.70749469e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70736391e+05, 9.63716172e+05, 9.77590891e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23737662e+06, 1.17582788e+06, 1.11648706e+06, 1.02168206e+06, 9.70736391e+05, 9.21656922e+05, 8.58534781e+05, 8.15643281e+05, 7.74335219e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23737809e+06, 7.74335188e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70736391e+05, 9.70711328e+05, 9.70749469e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70736391e+05, 9.63716172e+05, 9.77590891e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23737662e+06, 1.17582788e+06, 1.11648706e+06, 1.02168206e+06, 9.70736391e+05, 9.21656922e+05, 8.58534781e+05, 8.15643281e+05, 7.74335219e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23737809e+06, 7.74335188e+05, ],
  }),
  ("nof_tree_events",                 999996),
  ("nof_db_events",                   999996),
  ("fsize_local",                     4465641999), # 4.47GB, avg file size 1.12GB
  ("fsize_db",                        80383889041), # 80.38GB, avg file size 20.10MB
  ("use_it",                          True),
  ("xsection",                        0.030092),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t_private"),
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

samples_2017["/GluGluToHHTo4V_node_SM_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_sm_hh_4v_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99842000e+05, 9.99956781e+05, 9.99991406e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27994572e+06, 1.20818594e+06, 1.14083288e+06, 1.05954453e+06, 9.99842000e+05, 9.43985594e+05, 8.92278016e+05, 8.41896594e+05, 7.94677344e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27994753e+06, 7.94675766e+05, ],
    'CountWeightedFull'                                                              : [ 9.99842000e+05, 9.99956781e+05, 9.99991406e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27994572e+06, 1.20818594e+06, 1.14083288e+06, 1.05954453e+06, 9.99842000e+05, 9.43985594e+05, 8.92278016e+05, 8.41896594e+05, 7.94677344e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27994753e+06, 7.94675766e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70992156e+05, 9.71017156e+05, 9.71135672e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70992156e+05, 9.64030328e+05, 9.77775000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24265134e+06, 1.17336450e+06, 1.10826153e+06, 1.02861295e+06, 9.70992156e+05, 9.16984531e+05, 8.66187422e+05, 8.17545250e+05, 7.71911312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24265309e+06, 7.71909812e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70992156e+05, 9.71017156e+05, 9.71135672e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70992156e+05, 9.64030328e+05, 9.77775000e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.24265134e+06, 1.17336450e+06, 1.10826153e+06, 1.02861295e+06, 9.70992156e+05, 9.16984531e+05, 8.66187422e+05, 8.17545250e+05, 7.71911312e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24265309e+06, 7.71909812e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4669760532), # 4.67GB, avg file size 1.17GB
  ("fsize_db",                        83190363853), # 83.19GB, avg file size 20.80MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_sm_hh_4v_private"),
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

samples_2017["/GluGluToHHTo4V_node_1_TuneCP5_PSWeights_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_1_hh_4v_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99951453e+05, 9.99827625e+05, 9.99867359e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27525631e+06, 1.21090681e+06, 1.14904962e+06, 1.05319059e+06, 9.99951453e+05, 9.48743203e+05, 8.85172719e+05, 8.40310891e+05, 7.97240969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27525544e+06, 7.97240953e+05, ],
    'CountWeightedFull'                                                              : [ 9.99951453e+05, 9.99827625e+05, 9.99867359e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27525631e+06, 1.21090681e+06, 1.14904962e+06, 1.05319059e+06, 9.99951453e+05, 9.48743203e+05, 8.85172719e+05, 8.40310891e+05, 7.97240969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27525544e+06, 7.97240953e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72474656e+05, 9.72355609e+05, 9.72474156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72474656e+05, 9.65780031e+05, 9.78971875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23995653e+06, 1.17768797e+06, 1.11777609e+06, 1.02400506e+06, 9.72474656e+05, 9.22892453e+05, 8.60619156e+05, 8.17211031e+05, 7.75495234e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23995562e+06, 7.75495203e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72474656e+05, 9.72355609e+05, 9.72474156e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72474656e+05, 9.65780031e+05, 9.78971875e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23995653e+06, 1.17768797e+06, 1.11777609e+06, 1.02400506e+06, 9.72474656e+05, 9.22892453e+05, 8.60619156e+05, 8.17211031e+05, 7.75495234e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23995562e+06, 7.75495203e+05, ],
  }),
  ("nof_tree_events",                 1000000),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     4580073914), # 4.58GB, avg file size 1.15GB
  ("fsize_db",                        82235953558), # 82.24GB, avg file size 20.56MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_1_hh_4v_private"),
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

samples_2017["/GluGluToHHTo4V_node_4_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_4_hh_4v_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999997, ],
    'CountWeighted'                                                                  : [ 9.99934516e+05, 9.99934953e+05, 1.00000159e+06, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27508106e+06, 1.21105744e+06, 1.14945938e+06, 1.05296050e+06, 9.99934516e+05, 9.48961531e+05, 8.84929469e+05, 8.40264547e+05, 7.97350641e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27508309e+06, 7.97348875e+05, ],
    'CountWeightedFull'                                                              : [ 9.99934516e+05, 9.99934953e+05, 1.00000159e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27508106e+06, 1.21105744e+06, 1.14945938e+06, 1.05296050e+06, 9.99934516e+05, 9.48961531e+05, 8.84929469e+05, 8.40264547e+05, 7.97350641e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27508309e+06, 7.97348875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72424109e+05, 9.72393812e+05, 9.72512000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72424109e+05, 9.65715094e+05, 9.78926109e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23970644e+06, 1.17778009e+06, 1.11814162e+06, 1.02370439e+06, 9.72424109e+05, 9.23070344e+05, 8.60312891e+05, 8.17115328e+05, 7.75568891e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23970847e+06, 7.75567141e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72424109e+05, 9.72393812e+05, 9.72512000e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72424109e+05, 9.65715094e+05, 9.78926109e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23970644e+06, 1.17778009e+06, 1.11814162e+06, 1.02370439e+06, 9.72424109e+05, 9.23070344e+05, 8.60312891e+05, 8.17115328e+05, 7.75568891e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23970847e+06, 7.75567141e+05, ],
  }),
  ("nof_tree_events",                 999997),
  ("nof_db_events",                   999997),
  ("fsize_local",                     4568505157), # 4.57GB, avg file size 1.14GB
  ("fsize_db",                        82255572456), # 82.26GB, avg file size 20.56MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_4_hh_4v_private"),
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

samples_2017["/GluGluToHHTo4V_node_7_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_7_hh_4v_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999999, ],
    'CountWeighted'                                                                  : [ 9.99992484e+05, 1.00000862e+06, 9.99998391e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27531956e+06, 1.21090078e+06, 1.14898859e+06, 1.05325719e+06, 9.99992484e+05, 9.48708891e+05, 8.85238734e+05, 8.40335109e+05, 7.97223703e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27531956e+06, 7.97223703e+05, ],
    'CountWeightedFull'                                                              : [ 9.99992484e+05, 1.00000862e+06, 9.99998391e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27531956e+06, 1.21090078e+06, 1.14898859e+06, 1.05325719e+06, 9.99992484e+05, 9.48708891e+05, 8.85238734e+05, 8.40335109e+05, 7.97223703e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27531956e+06, 7.97223703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72095406e+05, 9.72083016e+05, 9.72127984e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72095406e+05, 9.65311359e+05, 9.78684344e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23948731e+06, 1.17718216e+06, 1.11724728e+06, 1.02363016e+06, 9.72095406e+05, 9.22471578e+05, 8.60314672e+05, 8.16887969e+05, 7.75153906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23948731e+06, 7.75153906e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72095406e+05, 9.72083016e+05, 9.72127984e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72095406e+05, 9.65311359e+05, 9.78684344e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23948731e+06, 1.17718216e+06, 1.11724728e+06, 1.02363016e+06, 9.72095406e+05, 9.22471578e+05, 8.60314672e+05, 8.16887969e+05, 7.75153906e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23948731e+06, 7.75153906e+05, ],
  }),
  ("nof_tree_events",                 999999),
  ("nof_db_events",                   999999),
  ("fsize_local",                     4578964962), # 4.58GB, avg file size 1.14GB
  ("fsize_db",                        82292366273), # 82.29GB, avg file size 20.57MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_7_hh_4v_private"),
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

samples_2017["/GluGluToHHTo4V_node_12_13TeV/RunIIFall17MiniAODv2/USER"] = OD([
  ("type",                            "mc"),
  ("sample_category",                 "signal_ggf_nonresonant_hh_wwww"),
  ("process_name_specific",           "signal_ggf_nonresonant_node_12_hh_4v_private"),
  ("nof_files",                       4),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999999, ],
    'CountWeighted'                                                                  : [ 1.00006278e+06, 9.99901812e+05, 9.99933875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27483650e+06, 1.21114778e+06, 1.14978238e+06, 1.05263244e+06, 1.00006278e+06, 9.49160828e+05, 8.84557688e+05, 8.40168578e+05, 7.97457828e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27483800e+06, 7.97457750e+05, ],
    'CountWeightedFull'                                                              : [ 1.00006278e+06, 9.99901812e+05, 9.99933875e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27483650e+06, 1.21114778e+06, 1.14978238e+06, 1.05263244e+06, 1.00006278e+06, 9.49160828e+05, 8.84557688e+05, 8.40168578e+05, 7.97457828e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27483800e+06, 7.97457750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72521844e+05, 9.72395500e+05, 9.72476828e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72521844e+05, 9.65817562e+05, 9.79026938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23951938e+06, 1.17789247e+06, 1.11846106e+06, 1.02343741e+06, 9.72521844e+05, 9.23275828e+05, 8.60000484e+05, 8.17053844e+05, 7.75688188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23952069e+06, 7.75688125e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72521844e+05, 9.72395500e+05, 9.72476828e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72521844e+05, 9.65817562e+05, 9.79026938e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23951938e+06, 1.17789247e+06, 1.11846106e+06, 1.02343741e+06, 9.72521844e+05, 9.23275828e+05, 8.60000484e+05, 8.17053844e+05, 7.75688188e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23952069e+06, 7.75688125e+05, ],
  }),
  ("nof_tree_events",                 999999),
  ("nof_db_events",                   999999),
  ("fsize_local",                     4569719369), # 4.57GB, avg file size 1.14GB
  ("fsize_db",                        81871806292), # 81.87GB, avg file size 20.47MB
  ("use_it",                          True),
  ("xsection",                        0.057547),
  ("genWeight",                       True),
  ("triggers",                        ['1e', '1mu', '2e', '2mu', '1e1mu', '3e', '3mu', '2e1mu', '1e2mu', '1e1tau', '1mu1tau', '2tau']),
  ("has_LHE",                         True),
  ("nof_PSweights",                   1),
  ("LHE_set",                         "LHA IDs 306000 - 306102 -> NNPDF31_nnlo_hessian_pdfas PDF set, expecting 103 weights (counted 103 weights)"),
  ("nof_reweighting",                 0),
  ("local_paths",
    [
      OD([
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct28_woPresel_nom_all/ntuples/signal_ggf_nonresonant_node_12_hh_4v_private"),
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

samples_2017["sum_events"] = [
  [ 'signal_ggf_nonresonant_node_sm_hh_2v2t',          'signal_ggf_nonresonant_node_sm_hh_2v2t_private',  'signal_ggf_nonresonant_node_1_hh_2v2t',           'signal_ggf_nonresonant_node_1_hh_2v2t_private',   'signal_ggf_nonresonant_node_2_hh_2v2t',           'signal_ggf_nonresonant_node_3_hh_2v2t',           'signal_ggf_nonresonant_node_4_hh_2v2t',           'signal_ggf_nonresonant_node_4_hh_2v2t_private',   'signal_ggf_nonresonant_node_5_hh_2v2t',           'signal_ggf_nonresonant_node_6_hh_2v2t',           'signal_ggf_nonresonant_node_7_hh_2v2t',           'signal_ggf_nonresonant_node_7_hh_2v2t_private',   'signal_ggf_nonresonant_node_8_hh_2v2t',           'signal_ggf_nonresonant_node_9_hh_2v2t',           'signal_ggf_nonresonant_node_10_hh_2v2t',          'signal_ggf_nonresonant_node_11_hh_2v2t',          'signal_ggf_nonresonant_node_12_hh_2v2t',          'signal_ggf_nonresonant_node_12_hh_2v2t_private',   ],
  [ 'signal_ggf_spin2_1000_hh_4v',                     'signal_ggf_spin2_1000_hh_4v_PSWeights',            ],
  [ 'signal_ggf_spin0_1000_hh_2v2t',                   'signal_ggf_spin0_1000_hh_2v2t_PSWeights',          ],
  [ 'signal_ggf_nonresonant_node_sm_hh_4v',            'signal_ggf_nonresonant_node_sm_hh_4v_private',    'signal_ggf_nonresonant_node_1_hh_4v',             'signal_ggf_nonresonant_node_1_hh_4v_private',     'signal_ggf_nonresonant_node_2_hh_4v',             'signal_ggf_nonresonant_node_3_hh_4v',             'signal_ggf_nonresonant_node_4_hh_4v',             'signal_ggf_nonresonant_node_4_hh_4v_private',     'signal_ggf_nonresonant_node_5_hh_4v',             'signal_ggf_nonresonant_node_6_hh_4v',             'signal_ggf_nonresonant_node_7_hh_4v',             'signal_ggf_nonresonant_node_7_hh_4v_private',     'signal_ggf_nonresonant_node_8_hh_4v',             'signal_ggf_nonresonant_node_9_hh_4v',             'signal_ggf_nonresonant_node_10_hh_4v',            'signal_ggf_nonresonant_node_11_hh_4v',            'signal_ggf_nonresonant_node_12_hh_4v',            'signal_ggf_nonresonant_node_12_hh_4v_private',     ],
  [ 'signal_ggf_spin0_1000_hh_4v',                     'signal_ggf_spin0_1000_hh_4v_PSWeights',            ],
  [ 'signal_ggf_spin2_1000_hh_2v2t',                   'signal_ggf_spin2_1000_hh_2v2t_PSWeights',          ],
  [ 'signal_ggf_spin0_1000_hh_4t',                     'signal_ggf_spin0_1000_hh_4t_PSWeights',            ],
  [ 'signal_ggf_spin2_1000_hh_4t',                     'signal_ggf_spin2_1000_hh_4t_PSWeights',            ],
  [ 'signal_ggf_nonresonant_node_sm_hh_4t',            'signal_ggf_nonresonant_node_sm_hh_4t_private',    'signal_ggf_nonresonant_node_1_hh_4t',             'signal_ggf_nonresonant_node_1_hh_4t_private',     'signal_ggf_nonresonant_node_2_hh_4t',             'signal_ggf_nonresonant_node_3_hh_4t',             'signal_ggf_nonresonant_node_4_hh_4t',             'signal_ggf_nonresonant_node_4_hh_4t_private',     'signal_ggf_nonresonant_node_5_hh_4t',             'signal_ggf_nonresonant_node_6_hh_4t',             'signal_ggf_nonresonant_node_7_hh_4t',             'signal_ggf_nonresonant_node_7_hh_4t_private',     'signal_ggf_nonresonant_node_8_hh_4t',             'signal_ggf_nonresonant_node_9_hh_4t',             'signal_ggf_nonresonant_node_10_hh_4t',            'signal_ggf_nonresonant_node_11_hh_4t',            'signal_ggf_nonresonant_node_12_hh_4t',            'signal_ggf_nonresonant_node_12_hh_4t_private',     ],
]

