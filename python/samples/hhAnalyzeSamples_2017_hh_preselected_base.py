from collections import OrderedDict as OD

# file generated at 2020-11-01 11:53:24 with the following command:
# create_dictionary.py -m python/samples/metaDict_2017.py -p python/samples/sampleLocations_2017_preselected.txt -N samples_2017 -E 2017 -o python/samples -g hhAnalyzeSamples_2017_hh_preselected_base.py -M

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
  ("nof_tree_events",                 197962),
  ("nof_db_events",                   400000),
  ("fsize_local",                     760932661), # 760.93MB, avg file size 760.93MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 205113),
  ("nof_db_events",                   400000),
  ("fsize_local",                     788059198), # 788.06MB, avg file size 788.06MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 203284),
  ("nof_db_events",                   385000),
  ("fsize_local",                     789297787), # 789.30MB, avg file size 789.30MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 216810),
  ("nof_db_events",                   400000),
  ("fsize_local",                     853265519), # 853.27MB, avg file size 853.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 171586),
  ("nof_db_events",                   300000),
  ("fsize_local",                     682455961), # 682.46MB, avg file size 682.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 384000, ],
    'CountWeighted'                                                                  : [ 3.83996156e+05, 3.83945188e+05, 3.83959250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.96573156e+05, 3.83992469e+05, 3.70279062e+05, 3.96573156e+05, 3.83992469e+05, 3.70279062e+05, 3.96573156e+05, 3.83992469e+05, 3.70279062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96573156e+05, 3.70279062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 2.52580700e+06, 2.49165400e+06, 3.20676225e+06, 2.52374000e+06, 2.28423150e+06, 1.67158225e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.84011344e+05, 3.84001844e+05, 5.29283750e+05, 3.83979625e+05, 3.83623281e+05, 2.54140922e+05, ],
    'CountWeightedFull'                                                              : [ 3.83970719e+05, 3.83920281e+05, 3.83934125e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 3.96547219e+05, 3.83967031e+05, 3.70254906e+05, 3.96547219e+05, 3.83967031e+05, 3.70254906e+05, 3.96547219e+05, 3.83967031e+05, 3.70254906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96547219e+05, 3.70254906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 2.52565500e+06, 2.49149325e+06, 3.20655000e+06, 2.52356175e+06, 2.28408275e+06, 1.67147638e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.83988156e+05, 3.83976938e+05, 5.29248750e+05, 3.83952719e+05, 3.83598344e+05, 2.54124828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74033656e+05, 3.73981500e+05, 3.74024875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74033656e+05, 3.71583625e+05, 3.76418812e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.86220812e+05, 3.74030469e+05, 3.60738438e+05, 3.86220812e+05, 3.74030469e+05, 3.60738438e+05, 3.86220812e+05, 3.74030469e+05, 3.60738438e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.86220812e+05, 3.60738438e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 2.46267050e+06, 2.42688225e+06, 3.12315225e+06, 2.45536475e+06, 2.22597775e+06, 1.62900475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74409875e+05, 3.73988656e+05, 5.15433250e+05, 3.73571094e+05, 3.73801344e+05, 2.47666734e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74009750e+05, 3.73957906e+05, 3.74001125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74009750e+05, 3.71559969e+05, 3.76394562e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 3.86196281e+05, 3.74006531e+05, 3.60715562e+05, 3.86196281e+05, 3.74006531e+05, 3.60715562e+05, 3.86196281e+05, 3.74006531e+05, 3.60715562e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.86196281e+05, 3.60715562e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 2.46252675e+06, 2.42672975e+06, 3.12295200e+06, 2.45519750e+06, 2.22583725e+06, 1.62890450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74388000e+05, 3.73965188e+05, 5.15400031e+05, 3.73545562e+05, 3.73777750e+05, 2.47651516e+05, ],
  }),
  ("nof_tree_events",                 229379),
  ("nof_db_events",                   384000),
  ("fsize_local",                     928397562), # 928.40MB, avg file size 928.40MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 178988),
  ("nof_db_events",                   284000),
  ("fsize_local",                     738732808), # 738.73MB, avg file size 738.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 202790),
  ("nof_db_events",                   300000),
  ("fsize_local",                     866193587), # 866.19MB, avg file size 866.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 213263),
  ("nof_db_events",                   300000),
  ("fsize_local",                     939786210), # 939.79MB, avg file size 939.79MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 147719),
  ("nof_db_events",                   200000),
  ("fsize_local",                     668885261), # 668.89MB, avg file size 668.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 152212),
  ("nof_db_events",                   200000),
  ("fsize_local",                     707215399), # 707.22MB, avg file size 707.22MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 156160),
  ("nof_db_events",                   200000),
  ("fsize_local",                     740257358), # 740.26MB, avg file size 740.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 159665),
  ("nof_db_events",                   200000),
  ("fsize_local",                     772094321), # 772.09MB, avg file size 772.09MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 162673),
  ("nof_db_events",                   200000),
  ("fsize_local",                     801939734), # 801.94MB, avg file size 801.94MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 165018),
  ("nof_db_events",                   200000),
  ("fsize_local",                     833303683), # 833.30MB, avg file size 833.30MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 166686),
  ("nof_db_events",                   200000),
  ("fsize_local",                     853639711), # 853.64MB, avg file size 853.64MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 161429),
  ("nof_db_events",                   192000),
  ("fsize_local",                     837117078), # 837.12MB, avg file size 837.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 84786),
  ("nof_db_events",                   100000),
  ("fsize_local",                     442020188), # 442.02MB, avg file size 442.02MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 85893),
  ("nof_db_events",                   100000),
  ("fsize_local",                     456340221), # 456.34MB, avg file size 456.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 86031),
  ("nof_db_events",                   100000),
  ("fsize_local",                     458865529), # 458.87MB, avg file size 458.87MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 86283),
  ("nof_db_events",                   100000),
  ("fsize_local",                     477036491), # 477.04MB, avg file size 477.04MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1250_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    6),
  ("nof_events",                      {
    'Count'                                                                          : [ 99000, ],
    'CountWeighted'                                                                  : [ 9.89602344e+04, 9.89549219e+04, 9.89615625e+04, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.12757195e+05, 9.89597500e+04, 8.76297578e+04, 1.12757195e+05, 9.89597500e+04, 8.76297578e+04, 1.12757195e+05, 9.89597500e+04, 8.76297578e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12757242e+05, 8.76296797e+04, ],
    'CountWeightedPSWeight'                                                          : [ 5.97606125e+05, 5.90384188e+05, 7.81398500e+05, 5.96843625e+05, 5.38633438e+05, 3.75516188e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.90542500e+04, 9.90528281e+04, 1.40263750e+05, 9.89502969e+04, 9.88191016e+04, 6.22461094e+04, ],
    'CountWeightedFull'                                                              : [ 9.89472656e+04, 9.89419219e+04, 9.89485000e+04, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.12742430e+05, 9.89467734e+04, 8.76182578e+04, 1.12742430e+05, 9.89467734e+04, 8.76182578e+04, 1.12742430e+05, 9.89467734e+04, 8.76182578e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.12742461e+05, 8.76181797e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 5.97533250e+05, 5.90308188e+05, 7.81295312e+05, 5.96759312e+05, 5.38562062e+05, 3.75467188e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.90421016e+04, 9.90401016e+04, 1.40245219e+05, 9.89363438e+04, 9.88059453e+04, 6.22379688e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.47062109e+04, 9.46886953e+04, 9.47229219e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.47062109e+04, 9.37572188e+04, 9.56504766e+04, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.07893219e+05, 9.47056406e+04, 8.38767500e+04, 1.07893219e+05, 9.47056406e+04, 8.38767500e+04, 1.07893219e+05, 9.47056406e+04, 8.38767500e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.07893250e+05, 8.38766719e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 5.72883812e+05, 5.64851875e+05, 7.47732188e+05, 5.69996875e+05, 5.15868125e+05, 3.59528688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.49495000e+04, 9.47546797e+04, 1.34187953e+05, 9.44925078e+04, 9.46117031e+04, 5.95911445e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.46943359e+04, 9.46767812e+04, 9.47110469e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.46943359e+04, 9.37456094e+04, 9.56383906e+04, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.07879711e+05, 9.46937578e+04, 8.38662031e+04, 1.07879711e+05, 9.46937578e+04, 8.38662031e+04, 1.07879711e+05, 9.46937578e+04, 8.38662031e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.07879742e+05, 8.38661328e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 5.72817125e+05, 5.64782562e+05, 7.47638125e+05, 5.69919875e+05, 5.15802656e+05, 3.59484031e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.49383984e+04, 9.47430781e+04, 1.34171062e+05, 9.44797656e+04, 9.45996719e+04, 5.95836953e+04, ],
  }),
  ("nof_tree_events",                 80466),
  ("nof_db_events",                   99000),
  ("fsize_local",                     440473705), # 440.47MB, avg file size 440.47MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1500_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 75818),
  ("nof_db_events",                   100000),
  ("fsize_local",                     416630957), # 416.63MB, avg file size 416.63MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1750_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 69311),
  ("nof_db_events",                   100000),
  ("fsize_local",                     379416398), # 379.42MB, avg file size 379.42MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_2000_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 60835),
  ("nof_db_events",                   100000),
  ("fsize_local",                     334326535), # 334.33MB, avg file size 334.33MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_2500_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 55683),
  ("nof_db_events",                   100000),
  ("fsize_local",                     305376865), # 305.38MB, avg file size 305.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_3000_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 195042),
  ("nof_db_events",                   391000),
  ("fsize_local",                     758067810), # 758.07MB, avg file size 758.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 200152),
  ("nof_db_events",                   386000),
  ("fsize_local",                     785273989), # 785.27MB, avg file size 785.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 204665),
  ("nof_db_events",                   380000),
  ("fsize_local",                     808645901), # 808.65MB, avg file size 808.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 222822),
  ("nof_db_events",                   400000),
  ("fsize_local",                     887584759), # 887.58MB, avg file size 887.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 236639),
  ("nof_db_events",                   400000),
  ("fsize_local",                     958814260), # 958.81MB, avg file size 958.81MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 185465),
  ("nof_db_events",                   298000),
  ("fsize_local",                     764423684), # 764.42MB, avg file size 764.42MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 254274),
  ("nof_db_events",                   384000),
  ("fsize_local",                     1070565941), # 1.07GB, avg file size 1.07GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 215090),
  ("nof_db_events",                   300000),
  ("fsize_local",                     939578963), # 939.58MB, avg file size 939.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 212521),
  ("nof_db_events",                   280000),
  ("fsize_local",                     959441297), # 959.44MB, avg file size 959.44MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 224827),
  ("nof_db_events",                   284000),
  ("fsize_local",                     1042918830), # 1.04GB, avg file size 1.04GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 163465),
  ("nof_db_events",                   200000),
  ("fsize_local",                     777616365), # 777.62MB, avg file size 777.62MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 166150),
  ("nof_db_events",                   198000),
  ("fsize_local",                     807614865), # 807.61MB, avg file size 807.61MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 171032),
  ("nof_db_events",                   200000),
  ("fsize_local",                     849219928), # 849.22MB, avg file size 849.22MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 163990),
  ("nof_db_events",                   189000),
  ("fsize_local",                     830770657), # 830.77MB, avg file size 830.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 172447),
  ("nof_db_events",                   196000),
  ("fsize_local",                     888185478), # 888.19MB, avg file size 888.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 177461),
  ("nof_db_events",                   200000),
  ("fsize_local",                     925529811), # 925.53MB, avg file size 925.53MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 173944),
  ("nof_db_events",                   194000),
  ("fsize_local",                     924530566), # 924.53MB, avg file size 924.53MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 90224),
  ("nof_db_events",                   100000),
  ("fsize_local",                     482849369), # 482.85MB, avg file size 482.85MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 90829),
  ("nof_db_events",                   100000),
  ("fsize_local",                     494135038), # 494.14MB, avg file size 494.14MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 90893),
  ("nof_db_events",                   100000),
  ("fsize_local",                     477246322), # 477.25MB, avg file size 477.25MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    8),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99908750e+04, 9.99962422e+04, 9.99942734e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99908750e+04, 9.99908750e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99947750e+05, 9.99947750e+05, 9.99947750e+05, 9.99947750e+05, 9.99947750e+05, 9.99947750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00023391e+05, 1.00062547e+05, 1.41112094e+05, 9.99654453e+04, 9.96111562e+04, 6.31628320e+04, ],
    'CountWeightedFull'                                                              : [ 9.99788203e+04, 9.99841953e+04, 9.99821953e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99788203e+04, 9.99788203e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99827375e+05, 9.99827375e+05, 9.99827375e+05, 9.99827375e+05, 9.99827375e+05, 9.99827375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00012203e+05, 1.00050562e+05, 1.41094688e+05, 9.99522500e+04, 9.95990703e+04, 6.31554258e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70882578e+04, 9.70795312e+04, 9.71045469e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70882578e+04, 9.64281250e+04, 9.77400000e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70882578e+04, 9.70882578e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70912625e+05, 9.70912625e+05, 9.70912625e+05, 9.70912625e+05, 9.70912625e+05, 9.70912625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72833438e+04, 9.71327969e+04, 1.36943516e+05, 9.68566484e+04, 9.67408906e+04, 6.13671250e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70769688e+04, 9.70682422e+04, 9.70932109e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70769688e+04, 9.64169609e+04, 9.77285078e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70769688e+04, 9.70769688e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70799625e+05, 9.70799625e+05, 9.70799625e+05, 9.70799625e+05, 9.70799625e+05, 9.70799625e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72728438e+04, 9.71215703e+04, 1.36927219e+05, 9.68443281e+04, 9.67295234e+04, 6.13601641e+04, ],
  }),
  ("nof_tree_events",                 89797),
  ("nof_db_events",                   100000),
  ("fsize_local",                     480435553), # 480.44MB, avg file size 480.44MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1250_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 81330),
  ("nof_db_events",                   100000),
  ("fsize_local",                     429569903), # 429.57MB, avg file size 429.57MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1500_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 73135),
  ("nof_db_events",                   100000),
  ("fsize_local",                     382046859), # 382.05MB, avg file size 382.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1750_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 65337),
  ("nof_db_events",                   100000),
  ("fsize_local",                     339813822), # 339.81MB, avg file size 339.81MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_2000_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 54716),
  ("nof_db_events",                   98000),
  ("fsize_local",                     283003840), # 283.00MB, avg file size 283.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_2500_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 51282),
  ("nof_db_events",                   100000),
  ("fsize_local",                     265170956), # 265.17MB, avg file size 265.17MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_3000_hh_4t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 128848),
  ("nof_db_events",                   399997),
  ("fsize_local",                     502564794), # 502.56MB, avg file size 502.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 132745),
  ("nof_db_events",                   399993),
  ("fsize_local",                     519697831), # 519.70MB, avg file size 519.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 136341),
  ("nof_db_events",                   399995),
  ("fsize_local",                     538682224), # 538.68MB, avg file size 538.68MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 132728),
  ("nof_db_events",                   379996),
  ("fsize_local",                     534244540), # 534.24MB, avg file size 534.24MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 109714),
  ("nof_db_events",                   299994),
  ("fsize_local",                     449155727), # 449.16MB, avg file size 449.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 114274),
  ("nof_db_events",                   299998),
  ("fsize_local",                     477800362), # 477.80MB, avg file size 477.80MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 120822),
  ("nof_db_events",                   299990),
  ("fsize_local",                     520990242), # 520.99MB, avg file size 520.99MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 122906),
  ("nof_db_events",                   286992),
  ("fsize_local",                     553064275), # 553.06MB, avg file size 553.06MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 131707),
  ("nof_db_events",                   291993),
  ("fsize_local",                     616515645), # 616.52MB, avg file size 616.52MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 127323),
  ("nof_db_events",                   269995),
  ("fsize_local",                     615506715), # 615.51MB, avg file size 615.51MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 145681),
  ("nof_db_events",                   299996),
  ("fsize_local",                     721990322), # 721.99MB, avg file size 721.99MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 98014),
  ("nof_db_events",                   195995),
  ("fsize_local",                     496594353), # 496.59MB, avg file size 496.59MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 102744),
  ("nof_db_events",                   199995),
  ("fsize_local",                     530336127), # 530.34MB, avg file size 530.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 100656),
  ("nof_db_events",                   191997),
  ("fsize_local",                     527356240), # 527.36MB, avg file size 527.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 106620),
  ("nof_db_events",                   199998),
  ("fsize_local",                     568001489), # 568.00MB, avg file size 568.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 108443),
  ("nof_db_events",                   199999),
  ("fsize_local",                     583022323), # 583.02MB, avg file size 583.02MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 105493),
  ("nof_db_events",                   191996),
  ("fsize_local",                     572503577), # 572.50MB, avg file size 572.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 110900),
  ("nof_db_events",                   199997),
  ("fsize_local",                     601307269), # 601.31MB, avg file size 601.31MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 55921),
  ("nof_db_events",                   99998),
  ("fsize_local",                     307360822), # 307.36MB, avg file size 307.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 56101),
  ("nof_db_events",                   100000),
  ("fsize_local",                     309332529), # 309.33MB, avg file size 309.33MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 54976),
  ("nof_db_events",                   100000),
  ("fsize_local",                     308614875), # 308.61MB, avg file size 308.61MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1250_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 48869),
  ("nof_db_events",                   99999),
  ("fsize_local",                     272483249), # 272.48MB, avg file size 272.48MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1500_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 43310),
  ("nof_db_events",                   100000),
  ("fsize_local",                     242407125), # 242.41MB, avg file size 242.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1750_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 37923),
  ("nof_db_events",                   99999),
  ("fsize_local",                     212366187), # 212.37MB, avg file size 212.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_2000_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 30854),
  ("nof_db_events",                   99999),
  ("fsize_local",                     173650104), # 173.65MB, avg file size 173.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_2500_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 26922),
  ("nof_db_events",                   99997),
  ("fsize_local",                     151507378), # 151.51MB, avg file size 151.51MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_3000_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 394995, ],
    'CountWeighted'                                                                  : [ 3.94970531e+05, 3.94982688e+05, 3.94986062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.99821875e+05, 3.94970531e+05, 3.87347688e+05, 3.99821875e+05, 3.94970531e+05, 3.87347688e+05, 3.99821875e+05, 3.94970531e+05, 3.87347688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99821875e+05, 3.87347688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87384938e+05, 3.87371969e+05, 3.87405156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87384938e+05, 3.85410938e+05, 3.89256844e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.92098969e+05, 3.87384938e+05, 3.79939281e+05, 3.92098969e+05, 3.87384938e+05, 3.79939281e+05, 3.92098969e+05, 3.87384938e+05, 3.79939281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.92098969e+05, 3.79939281e+05, ],
  }),
  ("nof_tree_events",                 128179),
  ("nof_db_events",                   394995),
  ("fsize_local",                     504361265), # 504.36MB, avg file size 504.36MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 132333),
  ("nof_db_events",                   395995),
  ("fsize_local",                     527288012), # 527.29MB, avg file size 527.29MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 138310),
  ("nof_db_events",                   399996),
  ("fsize_local",                     558321982), # 558.32MB, avg file size 558.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 140801),
  ("nof_db_events",                   394995),
  ("fsize_local",                     574664709), # 574.66MB, avg file size 574.66MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 112932),
  ("nof_db_events",                   299995),
  ("fsize_local",                     473311574), # 473.31MB, avg file size 473.31MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 112296),
  ("nof_db_events",                   284992),
  ("fsize_local",                     481566947), # 481.57MB, avg file size 481.57MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 125959),
  ("nof_db_events",                   299995),
  ("fsize_local",                     556636846), # 556.64MB, avg file size 556.64MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 131418),
  ("nof_db_events",                   289998),
  ("fsize_local",                     609303855), # 609.30MB, avg file size 609.30MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 134525),
  ("nof_db_events",                   279993),
  ("fsize_local",                     647751979), # 647.75MB, avg file size 647.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 101032),
  ("nof_db_events",                   199997),
  ("fsize_local",                     501456897), # 501.46MB, avg file size 501.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 105025),
  ("nof_db_events",                   199995),
  ("fsize_local",                     535493909), # 535.49MB, avg file size 535.49MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 108042),
  ("nof_db_events",                   199996),
  ("fsize_local",                     562485252), # 562.49MB, avg file size 562.49MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 108607),
  ("nof_db_events",                   195999),
  ("fsize_local",                     574745606), # 574.75MB, avg file size 574.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 110882),
  ("nof_db_events",                   195997),
  ("fsize_local",                     594074196), # 594.07MB, avg file size 594.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 115562),
  ("nof_db_events",                   199999),
  ("fsize_local",                     625154010), # 625.15MB, avg file size 625.15MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 116880),
  ("nof_db_events",                   199998),
  ("fsize_local",                     636870271), # 636.87MB, avg file size 636.87MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 113398),
  ("nof_db_events",                   191995),
  ("fsize_local",                     625864898), # 625.86MB, avg file size 625.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 59699),
  ("nof_db_events",                   99999),
  ("fsize_local",                     330014502), # 330.01MB, avg file size 330.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 60090),
  ("nof_db_events",                   99999),
  ("fsize_local",                     334181201), # 334.18MB, avg file size 334.18MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 59717),
  ("nof_db_events",                   99998),
  ("fsize_local",                     320495913), # 320.50MB, avg file size 320.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 56577),
  ("nof_db_events",                   99999),
  ("fsize_local",                     305954913), # 305.95MB, avg file size 305.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1250_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 47427),
  ("nof_db_events",                   99998),
  ("fsize_local",                     253797817), # 253.80MB, avg file size 253.80MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1500_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40148),
  ("nof_db_events",                   100000),
  ("fsize_local",                     213373400), # 213.37MB, avg file size 213.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1750_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99977344e+04, 1.00002461e+05, 9.99968750e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99977344e+04, 9.99977344e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, 9.99989000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00078250e+05, 1.00074266e+05, 1.45555406e+05, 9.99100625e+04, 9.97784531e+04, 5.95676016e+04, ],
    'CountWeightedFull'                                                              : [ 9.99714375e+04, 9.99761719e+04, 9.99705078e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99714375e+04, 9.99714375e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99726312e+05, 9.99726312e+05, 9.99726312e+05, 9.99726312e+05, 9.99726312e+05, 9.99726312e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 1.00053141e+05, 1.00048609e+05, 1.45516719e+05, 9.98830547e+04, 9.97512578e+04, 5.95521367e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71340469e+04, 9.71317031e+04, 9.71394609e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71340469e+04, 9.64812031e+04, 9.77766562e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71340469e+04, 9.71340469e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, 9.71349812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.73843672e+04, 9.71724062e+04, 1.41345438e+05, 9.68343516e+04, 9.69666250e+04, 5.78952344e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.71089297e+04, 9.71065625e+04, 9.71142734e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.71089297e+04, 9.64562969e+04, 9.77512578e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.71089297e+04, 9.71089297e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.71098375e+05, 9.71098375e+05, 9.71098375e+05, 9.71098375e+05, 9.71098375e+05, 9.71098375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.73603594e+04, 9.71478672e+04, 1.41308438e+05, 9.68085156e+04, 9.69405781e+04, 5.78804297e+04, ],
  }),
  ("nof_tree_events",                 33588),
  ("nof_db_events",                   99998),
  ("fsize_local",                     178163168), # 178.16MB, avg file size 178.16MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_2000_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 26085),
  ("nof_db_events",                   97997),
  ("fsize_local",                     138192396), # 138.19MB, avg file size 138.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_2500_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 23573),
  ("nof_db_events",                   99999),
  ("fsize_local",                     125406441), # 125.41MB, avg file size 125.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_3000_hh_2v2t_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 68922),
  ("nof_db_events",                   399999),
  ("fsize_local",                     267638995), # 267.64MB, avg file size 267.64MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_250_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 70733),
  ("nof_db_events",                   399998),
  ("fsize_local",                     276608287), # 276.61MB, avg file size 276.61MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_260_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 70546),
  ("nof_db_events",                   386000),
  ("fsize_local",                     279682984), # 279.68MB, avg file size 279.68MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_270_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 73096),
  ("nof_db_events",                   388998),
  ("fsize_local",                     296096293), # 296.10MB, avg file size 296.10MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_280_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 58796),
  ("nof_db_events",                   299999),
  ("fsize_local",                     243378115), # 243.38MB, avg file size 243.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_300_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 60012),
  ("nof_db_events",                   299998),
  ("fsize_local",                     254124649), # 254.12MB, avg file size 254.12MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_320_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 60829),
  ("nof_db_events",                   291998),
  ("fsize_local",                     266311513), # 266.31MB, avg file size 266.31MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_350_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 64876),
  ("nof_db_events",                   299999),
  ("fsize_local",                     297255800), # 297.26MB, avg file size 297.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_400_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 63540),
  ("nof_db_events",                   292000),
  ("fsize_local",                     304019512), # 304.02MB, avg file size 304.02MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_450_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 65677),
  ("nof_db_events",                   299997),
  ("fsize_local",                     323973823), # 323.97MB, avg file size 323.97MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_500_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 65822),
  ("nof_db_events",                   299998),
  ("fsize_local",                     333615388), # 333.62MB, avg file size 333.62MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_550_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 42536),
  ("nof_db_events",                   195999),
  ("fsize_local",                     220497161), # 220.50MB, avg file size 220.50MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_600_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 43082),
  ("nof_db_events",                   199999),
  ("fsize_local",                     226254158), # 226.25MB, avg file size 226.25MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_650_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 42271),
  ("nof_db_events",                   200000),
  ("fsize_local",                     224006883), # 224.01MB, avg file size 224.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_700_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40294),
  ("nof_db_events",                   192000),
  ("fsize_local",                     216889601), # 216.89MB, avg file size 216.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_750_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40984),
  ("nof_db_events",                   199997),
  ("fsize_local",                     222558463), # 222.56MB, avg file size 222.56MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_800_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40047),
  ("nof_db_events",                   199999),
  ("fsize_local",                     218094309), # 218.09MB, avg file size 218.09MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_850_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 39460),
  ("nof_db_events",                   200000),
  ("fsize_local",                     214477386), # 214.48MB, avg file size 214.48MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_900_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18746),
  ("nof_db_events",                   99999),
  ("fsize_local",                     103103725), # 103.10MB, avg file size 103.10MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18836),
  ("nof_db_events",                   99999),
  ("fsize_local",                     104018334), # 104.02MB, avg file size 104.02MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1000_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 13479),
  ("nof_db_events",                   78999),
  ("fsize_local",                     75914338), # 75.91MB, avg file size 75.91MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1250_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 15368),
  ("nof_db_events",                   100000),
  ("fsize_local",                     85705960), # 85.71MB, avg file size 85.71MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1500_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 13937),
  ("nof_db_events",                   100000),
  ("fsize_local",                     78086789), # 78.09MB, avg file size 78.09MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_1750_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 13204),
  ("nof_db_events",                   100000),
  ("fsize_local",                     73825666), # 73.83MB, avg file size 73.83MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_2000_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 11972),
  ("nof_db_events",                   99999),
  ("fsize_local",                     67046593), # 67.05MB, avg file size 67.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_2500_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 11092),
  ("nof_db_events",                   99999),
  ("fsize_local",                     62436148), # 62.44MB, avg file size 62.44MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin0_3000_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 69156),
  ("nof_db_events",                   399996),
  ("fsize_local",                     272091988), # 272.09MB, avg file size 272.09MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_250_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 71517),
  ("nof_db_events",                   399997),
  ("fsize_local",                     284837680), # 284.84MB, avg file size 284.84MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_260_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 74241),
  ("nof_db_events",                   400000),
  ("fsize_local",                     300436915), # 300.44MB, avg file size 300.44MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_270_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 74444),
  ("nof_db_events",                   391999),
  ("fsize_local",                     305642906), # 305.64MB, avg file size 305.64MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_280_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 76485),
  ("nof_db_events",                   383998),
  ("fsize_local",                     323038547), # 323.04MB, avg file size 323.04MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_300_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 61987),
  ("nof_db_events",                   300000),
  ("fsize_local",                     269275477), # 269.28MB, avg file size 269.28MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_320_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 64493),
  ("nof_db_events",                   299999),
  ("fsize_local",                     290227570), # 290.23MB, avg file size 290.23MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_350_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 66931),
  ("nof_db_events",                   300000),
  ("fsize_local",                     316923980), # 316.92MB, avg file size 316.92MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_400_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 64893),
  ("nof_db_events",                   287998),
  ("fsize_local",                     320311860), # 320.31MB, avg file size 320.31MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_450_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 68205),
  ("nof_db_events",                   299997),
  ("fsize_local",                     347405333), # 347.41MB, avg file size 347.41MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_500_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 67447),
  ("nof_db_events",                   299998),
  ("fsize_local",                     352046119), # 352.05MB, avg file size 352.05MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_550_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 42865),
  ("nof_db_events",                   191998),
  ("fsize_local",                     228178750), # 228.18MB, avg file size 228.18MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_600_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 43945),
  ("nof_db_events",                   200000),
  ("fsize_local",                     237165890), # 237.17MB, avg file size 237.17MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_650_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 41352),
  ("nof_db_events",                   191999),
  ("fsize_local",                     224737109), # 224.74MB, avg file size 224.74MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_700_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 42531),
  ("nof_db_events",                   199997),
  ("fsize_local",                     232233911), # 232.23MB, avg file size 232.23MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_750_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 41320),
  ("nof_db_events",                   199998),
  ("fsize_local",                     226648975), # 226.65MB, avg file size 226.65MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_800_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 40318),
  ("nof_db_events",                   199999),
  ("fsize_local",                     222769504), # 222.77MB, avg file size 222.77MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_850_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 19901),
  ("nof_db_events",                   99998),
  ("fsize_local",                     110550867), # 110.55MB, avg file size 110.55MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_900_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 18474),
  ("nof_db_events",                   99999),
  ("fsize_local",                     102483078), # 102.48MB, avg file size 102.48MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 99998, ],
    'CountWeighted'                                                                  : [ 9.99875781e+04, 9.99936797e+04, 9.99924141e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99875781e+04, 9.99875781e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99933500e+05, 9.99933500e+05, 9.99933500e+05, 9.99933500e+05, 9.99933500e+05, 9.99933500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99295625e+04, 9.98906250e+04, 1.47770359e+05, 1.00081523e+05, 1.00224289e+05, 5.78633203e+04, ],
    'CountWeightedFull'                                                              : [ 9.99550469e+04, 9.99607891e+04, 9.99595781e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99550469e+04, 9.99550469e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99605375e+05, 9.99605375e+05, 9.99605375e+05, 9.99605375e+05, 9.99605375e+05, 9.99605375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98982031e+04, 9.98584688e+04, 1.47721625e+05, 1.00048203e+05, 1.00190766e+05, 5.78444961e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69893359e+04, 9.69945469e+04, 9.69879453e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69893359e+04, 9.63078906e+04, 9.76619844e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.69893359e+04, 9.69893359e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.69937500e+05, 9.69937500e+05, 9.69937500e+05, 9.69937500e+05, 9.69937500e+05, 9.69937500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.70863594e+04, 9.68625469e+04, 1.43318125e+05, 9.68858750e+04, 9.72871094e+04, 5.61655195e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69580469e+04, 9.69629297e+04, 9.69564297e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69580469e+04, 9.62768984e+04, 9.76303906e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.69580469e+04, 9.69580469e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, 9.69622375e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.70561406e+04, 9.68317188e+04, 1.43271500e+05, 9.68539766e+04, 9.72549219e+04, 5.61474570e+04, ],
  }),
  ("nof_tree_events",                 18818),
  ("nof_db_events",                   99998),
  ("fsize_local",                     101005062), # 101.01MB, avg file size 101.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1000_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    14),
  ("nof_events",                      {
    'Count'                                                                          : [ 100000, ],
    'CountWeighted'                                                                  : [ 9.99962969e+04, 9.99967812e+04, 9.99967812e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99962969e+04, 9.99962969e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99960875e+05, 9.99960875e+05, 9.99960875e+05, 9.99960875e+05, 9.99960875e+05, 9.99960875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 9.99013906e+04, 1.00060398e+05, 1.47207562e+05, 1.00118000e+05, 9.91383125e+04, 5.76371484e+04, ],
    'CountWeightedFull'                                                              : [ 9.99619531e+04, 9.99623906e+04, 9.99624922e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99619531e+04, 9.99619531e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99616750e+05, 9.99616750e+05, 9.99616750e+05, 9.99616750e+05, 9.99616750e+05, 9.99616750e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.98679219e+04, 1.00026125e+05, 1.47156422e+05, 1.00082555e+05, 9.91040000e+04, 5.76174258e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.71053047e+04, 9.70968984e+04, 9.71166250e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.71053047e+04, 9.64482891e+04, 9.77528516e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.71053047e+04, 9.71053047e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.71053000e+05, 9.71053000e+05, 9.71053000e+05, 9.71053000e+05, 9.71053000e+05, 9.71053000e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.71778125e+04, 9.71489844e+04, 1.42902219e+05, 9.70161172e+04, 9.62988281e+04, 5.60073828e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70722891e+04, 9.70638281e+04, 9.70836484e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70722891e+04, 9.64155391e+04, 9.77195234e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70722891e+04, 9.70722891e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70722062e+05, 9.70722062e+05, 9.70722062e+05, 9.70722062e+05, 9.70722062e+05, 9.70722062e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.71455391e+04, 9.71160312e+04, 1.42853062e+05, 9.69821094e+04, 9.62657500e+04, 5.59883945e+04, ],
  }),
  ("nof_tree_events",                 16441),
  ("nof_db_events",                   100000),
  ("fsize_local",                     88017738), # 88.02MB, avg file size 88.02MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1250_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 14690),
  ("nof_db_events",                   100000),
  ("fsize_local",                     78378312), # 78.38MB, avg file size 78.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1500_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 13006),
  ("nof_db_events",                   97000),
  ("fsize_local",                     69072330), # 69.07MB, avg file size 69.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_1750_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    16),
  ("nof_events",                      {
    'Count'                                                                          : [ 99999, ],
    'CountWeighted'                                                                  : [ 9.99958594e+04, 9.99975625e+04, 9.99959219e+04, ],
    'CountWeightedLHEEnvelope'                                                       : [ 9.99958594e+04, 9.99958594e+04, ],
    'CountWeightedPSWeight'                                                          : [ 9.99978750e+05, 9.99978750e+05, 9.99978750e+05, 9.99978750e+05, 9.99978750e+05, 9.99978750e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.00013609e+05, 9.99071797e+04, 1.48690469e+05, 9.99890469e+04, 9.99237812e+04, 5.68759062e+04, ],
    'CountWeightedFull'                                                              : [ 9.99567969e+04, 9.99585938e+04, 9.99567266e+04, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 9.99567969e+04, 9.99567969e+04, ],
    'CountWeightedFullPSWeight'                                                      : [ 9.99586938e+05, 9.99586938e+05, 9.99586938e+05, 9.99586938e+05, 9.99586938e+05, 9.99586938e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 9.99774297e+04, 9.98681094e+04, 1.48631344e+05, 9.99508125e+04, 9.98840312e+04, 5.68549570e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70763594e+04, 9.70686562e+04, 9.70895703e+04, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70763594e+04, 9.64103047e+04, 9.77306328e+04, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 9.70763594e+04, 9.70763594e+04, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.70775875e+05, 9.70775875e+05, 9.70775875e+05, 9.70775875e+05, 9.70775875e+05, 9.70775875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 9.72671484e+04, 9.69477656e+04, 1.44339891e+05, 9.68535391e+04, 9.70895156e+04, 5.52481211e+04, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70393359e+04, 9.70318281e+04, 9.70523594e+04, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70393359e+04, 9.63737500e+04, 9.76931719e+04, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 9.70393359e+04, 9.70393359e+04, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 9.70405000e+05, 9.70405000e+05, 9.70405000e+05, 9.70405000e+05, 9.70405000e+05, 9.70405000e+05, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 9.72323984e+04, 9.69105703e+04, 1.44283922e+05, 9.68169375e+04, 9.70521250e+04, 5.52279844e+04, ],
  }),
  ("nof_tree_events",                 12387),
  ("nof_db_events",                   99999),
  ("fsize_local",                     65534441), # 65.53MB, avg file size 65.53MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_2000_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 11337),
  ("nof_db_events",                   99999),
  ("fsize_local",                     60191359), # 60.19MB, avg file size 60.19MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_2500_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 10729),
  ("nof_db_events",                   100000),
  ("fsize_local",                     57372966), # 57.37MB, avg file size 57.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_spin2_3000_hh_4v_PSWeights"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    11),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00033219e+05, 3.99996000e+05, 4.00030438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00033219e+05, 4.00033219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99983725e+06, 3.99988725e+06, 3.99988725e+06, 3.99983725e+06, 3.99988725e+06, 3.99983350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99872688e+05, 4.00079250e+05, 5.37982750e+05, 4.00023438e+05, 4.00065375e+05, 2.73806938e+05, ],
    'CountWeightedFull'                                                              : [ 3.99837500e+05, 3.99803000e+05, 3.99835000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99837500e+05, 3.99837500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, 3.99795075e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99737625e+05, 3.99884875e+05, 5.37719750e+05, 3.99888688e+05, 3.99867688e+05, 2.73715375e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.72293062e+05, 3.72251938e+05, 3.72315125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.72293062e+05, 3.65904312e+05, 3.78650156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72293062e+05, 3.72293062e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.72273850e+06, 3.72278500e+06, 3.72278500e+06, 3.72273825e+06, 3.72278500e+06, 3.72273475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.72196688e+05, 3.72179938e+05, 5.00416812e+05, 3.72261469e+05, 3.72620250e+05, 2.55182625e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.72116750e+05, 3.72077219e+05, 3.72138438e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.72116750e+05, 3.65732125e+05, 3.78469625e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.72116750e+05, 3.72116750e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, 3.72102850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.72074125e+05, 3.72004375e+05, 5.00178312e+05, 3.72139562e+05, 3.72440719e+05, 2.55099688e+05, ],
  }),
  ("nof_tree_events",                 226538),
  ("nof_db_events",                   400000),
  ("fsize_local",                     988338343), # 988.34MB, avg file size 988.34MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_4t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 396000, ],
    'CountWeighted'                                                                  : [ 3.96006250e+05, 3.96005438e+05, 3.96023312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96006250e+05, 3.96006250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95986925e+06, 3.95989275e+06, 3.95989275e+06, 3.95987075e+06, 3.95989275e+06, 3.95986925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95894906e+05, 3.95631812e+05, 5.36959312e+05, 3.96009719e+05, 3.96823188e+05, 2.67684906e+05, ],
    'CountWeightedFull'                                                              : [ 3.95811219e+05, 3.95811312e+05, 3.95826594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95811219e+05, 3.95811219e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95795525e+06, 3.95795525e+06, 3.95795525e+06, 3.95795525e+06, 3.95795525e+06, 3.95795525e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95748312e+05, 3.95440562e+05, 5.36698250e+05, 3.95861781e+05, 3.96624562e+05, 2.67586469e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.62100688e+05, 3.62043938e+05, 3.62147531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.62100688e+05, 3.54537969e+05, 3.69676844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.62100688e+05, 3.62100688e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.62093575e+06, 3.62095675e+06, 3.62095675e+06, 3.62093675e+06, 3.62095675e+06, 3.62093575e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.62050188e+05, 3.61571062e+05, 4.90678250e+05, 3.62048750e+05, 3.63145094e+05, 2.45149609e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.61926438e+05, 3.61870062e+05, 3.61971719e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.61926438e+05, 3.54368094e+05, 3.69497906e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.61926438e+05, 3.61926438e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, 3.61921650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.61919125e+05, 3.61399562e+05, 4.90444562e+05, 3.61916625e+05, 3.62967031e+05, 2.45061391e+05, ],
  }),
  ("nof_tree_events",                 228047),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1061898334), # 1.06GB, avg file size 1.06GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_2_hh_4t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    10),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00010469e+05, 4.00016562e+05, 3.99977781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00010469e+05, 4.00010469e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99996800e+06, 3.99999200e+06, 3.99999200e+06, 3.99996450e+06, 3.99999200e+06, 3.99996450e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99902938e+05, 3.99853500e+05, 5.37576250e+05, 3.99988562e+05, 4.00538781e+05, 2.74464625e+05, ],
    'CountWeightedFull'                                                              : [ 3.99835500e+05, 3.99840688e+05, 3.99804000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99835500e+05, 3.99835500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, 3.99822900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99772750e+05, 3.99677719e+05, 5.37342500e+05, 3.99858062e+05, 4.00364125e+05, 2.74376219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.76072312e+05, 3.76032750e+05, 3.76095406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.76072312e+05, 3.70487344e+05, 3.81608250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.76072312e+05, 3.76072312e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.76064825e+06, 3.76067125e+06, 3.76067125e+06, 3.76064475e+06, 3.76067125e+06, 3.76064475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.76006469e+05, 3.75756188e+05, 5.05197938e+05, 3.76025188e+05, 3.76872375e+05, 2.58352469e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75911312e+05, 3.75871125e+05, 3.75935125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75911312e+05, 3.70329688e+05, 3.81443938e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.75911312e+05, 3.75911312e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, 3.75905700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75886812e+05, 3.75595125e+05, 5.04983031e+05, 3.75905125e+05, 3.76710875e+05, 2.58270984e+05, ],
  }),
  ("nof_tree_events",                 240062),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1038338316), # 1.04GB, avg file size 1.04GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_0_hh_4t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99993938e+05, 4.00012656e+05, 4.00005188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99993938e+05, 3.99993938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99987125e+06, 3.99996025e+06, 3.99996025e+06, 3.99987275e+06, 3.99996025e+06, 3.99987000e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99953406e+05, 4.00090812e+05, 5.39059625e+05, 3.99874094e+05, 3.99731188e+05, 2.72497062e+05, ],
    'CountWeightedFull'                                                              : [ 3.99759750e+05, 3.99778344e+05, 3.99771156e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99759750e+05, 3.99759750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99762800e+06, 3.99762800e+06, 3.99762800e+06, 3.99762800e+06, 3.99762800e+06, 3.99762800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99801688e+05, 3.99860188e+05, 5.38747000e+05, 3.99723375e+05, 3.99491500e+05, 2.72394125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.71783719e+05, 3.71746750e+05, 3.71839219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.71783719e+05, 3.65511062e+05, 3.78058125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.71783719e+05, 3.71783719e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.71776000e+06, 3.71783150e+06, 3.71783150e+06, 3.71776125e+06, 3.71783150e+06, 3.71775925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.71777500e+05, 3.71639812e+05, 5.00752219e+05, 3.71623156e+05, 3.71925375e+05, 2.53671188e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.71572125e+05, 3.71535531e+05, 3.71627312e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.71572125e+05, 3.65304156e+05, 3.77841750e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.71572125e+05, 3.71572125e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.71571775e+06, 3.71571775e+06, 3.71571775e+06, 3.71571775e+06, 3.71571775e+06, 3.71571775e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.71640062e+05, 3.71430188e+05, 5.00472281e+05, 3.71486719e+05, 3.71711812e+05, 2.53577812e+05, ],
  }),
  ("nof_tree_events",                 306504),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1521092227), # 1.52GB, avg file size 1.52GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_4t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 378000, ],
    'CountWeighted'                                                                  : [ 3.78030500e+05, 3.78001188e+05, 3.77996562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.78030500e+05, 3.78030500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.77991700e+06, 3.78004300e+06, 3.78004300e+06, 3.77991200e+06, 3.78004300e+06, 3.77990375e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.77980438e+05, 3.78013000e+05, 5.08233594e+05, 3.77853875e+05, 3.77742656e+05, 2.58501953e+05, ],
    'CountWeightedFull'                                                              : [ 3.77827500e+05, 3.77796688e+05, 3.77793594e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.77827500e+05, 3.77827500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.77802025e+06, 3.77802025e+06, 3.77802025e+06, 3.77802025e+06, 3.77802025e+06, 3.77802025e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.77849469e+05, 3.77810656e+05, 5.07957094e+05, 3.77722875e+05, 3.77534250e+05, 2.58413203e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.52311625e+05, 3.52238625e+05, 3.52358438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.52311625e+05, 3.46486281e+05, 3.58117594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.52311625e+05, 3.52311625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.52286850e+06, 3.52298825e+06, 3.52298825e+06, 3.52286475e+06, 3.52298825e+06, 3.52285650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.52315062e+05, 3.52112281e+05, 4.73371562e+05, 3.52119125e+05, 3.52329250e+05, 2.41271000e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.52126969e+05, 3.52053062e+05, 3.52173812e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.52126969e+05, 3.46305844e+05, 3.57928875e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.52126969e+05, 3.52126969e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.52114625e+06, 3.52114625e+06, 3.52114625e+06, 3.52114625e+06, 3.52114625e+06, 3.52114625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.52196031e+05, 3.51928281e+05, 4.73120625e+05, 3.52000031e+05, 3.52140094e+05, 2.41190250e+05, ],
  }),
  ("nof_tree_events",                 260611),
  ("nof_db_events",                   378000),
  ("fsize_local",                     1225569859), # 1.23GB, avg file size 1.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_4t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 376000, ],
    'CountWeighted'                                                                  : [ 3.75976500e+05, 3.75987125e+05, 3.76009688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.75976500e+05, 3.75976500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.75994350e+06, 3.75998950e+06, 3.75998950e+06, 3.75994200e+06, 3.75998950e+06, 3.75994200e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.75950625e+05, 3.75901062e+05, 5.05651625e+05, 3.75878594e+05, 3.75697938e+05, 2.56937781e+05, ],
    'CountWeightedFull'                                                              : [ 3.75768969e+05, 3.75777906e+05, 3.75802219e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.75768969e+05, 3.75768969e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.75790550e+06, 3.75790550e+06, 3.75790550e+06, 3.75790550e+06, 3.75790550e+06, 3.75790550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.75815875e+05, 3.75696594e+05, 5.05371875e+05, 3.75743438e+05, 3.75484094e+05, 2.56846125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.49738906e+05, 3.49707000e+05, 3.49776344e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.49738906e+05, 3.43838219e+05, 3.55631656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.49738906e+05, 3.49738906e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.49741950e+06, 3.49746350e+06, 3.49746350e+06, 3.49741800e+06, 3.49746350e+06, 3.49741800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.49744688e+05, 3.49500562e+05, 4.70039531e+05, 3.49584562e+05, 3.49693469e+05, 2.39338484e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.49551844e+05, 3.49518750e+05, 3.49590250e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.49551844e+05, 3.43655750e+05, 3.55439781e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.49551844e+05, 3.49551844e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.49558950e+06, 3.49558950e+06, 3.49558950e+06, 3.49558950e+06, 3.49558950e+06, 3.49558950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.49622250e+05, 3.49316062e+05, 4.69788625e+05, 3.49461750e+05, 3.49502438e+05, 2.39254938e+05, ],
  }),
  ("nof_tree_events",                 271789),
  ("nof_db_events",                   376000),
  ("fsize_local",                     1310576665), # 1.31GB, avg file size 1.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_0_1_hh_4t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 396999, ],
    'CountWeighted'                                                                  : [ 3.96976281e+05, 3.96982188e+05, 3.97018000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.96976281e+05, 3.96976281e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.97000850e+06, 3.97002900e+06, 3.97002900e+06, 3.97000650e+06, 3.97002900e+06, 3.97000400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96949500e+05, 3.96894531e+05, 5.49344312e+05, 3.96915250e+05, 3.96595188e+05, 2.57494047e+05, ],
    'CountWeightedFull'                                                              : [ 3.96736719e+05, 3.96743375e+05, 3.96775688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.96736719e+05, 3.96736719e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.96762225e+06, 3.96762225e+06, 3.96762225e+06, 3.96762225e+06, 3.96762225e+06, 3.96762225e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.96772906e+05, 3.96655125e+05, 5.49011688e+05, 3.96739062e+05, 3.96350406e+05, 2.57379812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.70997625e+05, 3.70968875e+05, 3.71042406e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.70997625e+05, 3.64950812e+05, 3.76987156e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.70997625e+05, 3.70997625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.71005125e+06, 3.71007075e+06, 3.71007075e+06, 3.71004900e+06, 3.71007075e+06, 3.71004675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.70988938e+05, 3.70690969e+05, 5.13159500e+05, 3.70887188e+05, 3.70992125e+05, 2.40956109e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.70775625e+05, 3.70747875e+05, 3.70819750e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.70775625e+05, 3.64732906e+05, 3.76761031e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.70775625e+05, 3.70775625e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.70784825e+06, 3.70784825e+06, 3.70784825e+06, 3.70784825e+06, 3.70784825e+06, 3.70784825e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.70826875e+05, 3.70469688e+05, 5.12853594e+05, 3.70725281e+05, 3.70766812e+05, 2.40850875e+05, ],
  }),
  ("nof_tree_events",                 145986),
  ("nof_db_events",                   396999),
  ("fsize_local",                     662753221), # 662.75MB, avg file size 662.75MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_2v2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 395993, ],
    'CountWeighted'                                                                  : [ 3.95988250e+05, 3.95984469e+05, 3.95992906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95988250e+05, 3.95988250e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95976050e+06, 3.95977950e+06, 3.95977950e+06, 3.95976100e+06, 3.95977950e+06, 3.95976050e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.96027375e+05, 3.95495281e+05, 5.51705938e+05, 3.95794344e+05, 3.96325688e+05, 2.53985344e+05, ],
    'CountWeightedFull'                                                              : [ 3.95744906e+05, 3.95740750e+05, 3.95749188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95744906e+05, 3.95744906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95735375e+06, 3.95735375e+06, 3.95735375e+06, 3.95735375e+06, 3.95735375e+06, 3.95735375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95841438e+05, 3.95247875e+05, 5.51366938e+05, 3.95607938e+05, 3.96086062e+05, 2.53867188e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.63341250e+05, 3.63292312e+05, 3.63392031e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.63341250e+05, 3.56016344e+05, 3.70650875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.63341250e+05, 3.63341250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.63337175e+06, 3.63338925e+06, 3.63338925e+06, 3.63337225e+06, 3.63338925e+06, 3.63337175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.63424031e+05, 3.62640375e+05, 5.05975625e+05, 3.63099062e+05, 3.64048094e+05, 2.33403500e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.63124062e+05, 3.63075125e+05, 3.63173938e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.63124062e+05, 3.55804938e+05, 3.70427938e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.63124062e+05, 3.63124062e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.63121900e+06, 3.63121900e+06, 3.63121900e+06, 3.63121900e+06, 3.63121900e+06, 3.63121900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.63257438e+05, 3.62421031e+05, 5.05673844e+05, 3.62932250e+05, 3.63832812e+05, 2.33297734e+05, ],
  }),
  ("nof_tree_events",                 146131),
  ("nof_db_events",                   395993),
  ("fsize_local",                     704860206), # 704.86MB, avg file size 704.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_2_hh_2v2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 395993, ],
    'CountWeighted'                                                                  : [ 3.95977625e+05, 3.95989531e+05, 3.96012906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.95977625e+05, 3.95977625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.95997850e+06, 3.96003250e+06, 3.96003250e+06, 3.95997875e+06, 3.96003250e+06, 3.95997850e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.95948000e+05, 3.96280562e+05, 5.48968188e+05, 3.95815000e+05, 3.94685969e+05, 2.55407906e+05, ],
    'CountWeightedFull'                                                              : [ 3.95688281e+05, 3.95702281e+05, 3.95720750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.95688281e+05, 3.95688281e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.95711500e+06, 3.95711500e+06, 3.95711500e+06, 3.95711500e+06, 3.95711500e+06, 3.95711500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.95753812e+05, 3.95994250e+05, 5.48572062e+05, 3.95621625e+05, 3.94393781e+05, 2.55282797e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.67470594e+05, 3.67435562e+05, 3.67529156e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.67470594e+05, 3.61183281e+05, 3.73767406e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.67470594e+05, 3.67470594e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.67475925e+06, 3.67481025e+06, 3.67481025e+06, 3.67475975e+06, 3.67481025e+06, 3.67475925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.67468938e+05, 3.67514469e+05, 5.09199906e+05, 3.67284219e+05, 3.66660312e+05, 2.37373656e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.67212344e+05, 3.67179219e+05, 3.67269531e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.67212344e+05, 3.60931812e+05, 3.73502500e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.67212344e+05, 3.67212344e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.67222175e+06, 3.67222175e+06, 3.67222175e+06, 3.67222175e+06, 3.67222175e+06, 3.67222175e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.67292562e+05, 3.67259094e+05, 5.08845750e+05, 3.67108469e+05, 3.66399844e+05, 2.37259828e+05, ],
  }),
  ("nof_tree_events",                 199568),
  ("nof_db_events",                   395993),
  ("fsize_local",                     1055487410), # 1.06GB, avg file size 1.06GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_2_1_hh_2v2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 399993, ],
    'CountWeighted'                                                                  : [ 4.00011812e+05, 4.00003344e+05, 3.99989250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00011812e+05, 4.00011812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99982925e+06, 3.99984075e+06, 3.99984075e+06, 3.99982925e+06, 3.99984075e+06, 3.99982925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00019125e+05, 3.99944750e+05, 5.52636062e+05, 3.99862375e+05, 3.99345250e+05, 2.60069156e+05, ],
    'CountWeightedFull'                                                              : [ 3.99797188e+05, 3.99787000e+05, 3.99774969e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99797188e+05, 3.99797188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99770375e+06, 3.99770375e+06, 3.99770375e+06, 3.99770375e+06, 3.99770375e+06, 3.99770375e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99847719e+05, 3.99732000e+05, 5.52343438e+05, 3.99689938e+05, 3.99130406e+05, 2.59957703e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.77128625e+05, 3.77085781e+05, 3.77171562e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.77128625e+05, 3.71751062e+05, 3.82435656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.77128625e+05, 3.77128625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.77116500e+06, 3.77117650e+06, 3.77117650e+06, 3.77116500e+06, 3.77117650e+06, 3.77116500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.77193250e+05, 3.76869406e+05, 5.20712375e+05, 3.76933875e+05, 3.76748750e+05, 2.45519641e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.76929562e+05, 3.76885906e+05, 3.76972531e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.76929562e+05, 3.71555500e+05, 3.82233156e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.76929562e+05, 3.76929562e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.76918925e+06, 3.76918925e+06, 3.76918925e+06, 3.76918925e+06, 3.76918925e+06, 3.76918925e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.77034438e+05, 3.76671531e+05, 5.20441094e+05, 3.76774219e+05, 3.76550031e+05, 2.45416344e+05, ],
  }),
  ("nof_tree_events",                 155718),
  ("nof_db_events",                   399993),
  ("fsize_local",                     701447307), # 701.45MB, avg file size 701.45MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_0_hh_2v2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 375994, ],
    'CountWeighted'                                                                  : [ 3.75998812e+05, 3.75980000e+05, 3.75997781e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.75998812e+05, 3.75998812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.75954925e+06, 3.75966300e+06, 3.75966300e+06, 3.75954575e+06, 3.75966300e+06, 3.75954525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.75827562e+05, 3.76257125e+05, 5.20930375e+05, 3.75973938e+05, 3.74810062e+05, 2.42797516e+05, ],
    'CountWeightedFull'                                                              : [ 3.75715750e+05, 3.75697281e+05, 3.75716031e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.75715750e+05, 3.75715750e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.75684150e+06, 3.75684150e+06, 3.75684150e+06, 3.75684150e+06, 3.75684150e+06, 3.75684150e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.75643344e+05, 3.75974188e+05, 5.20541656e+05, 3.75790344e+05, 3.74527875e+05, 2.42678156e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.49842969e+05, 3.49815031e+05, 3.49861438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.49842969e+05, 3.44013531e+05, 3.55666125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.49842969e+05, 3.49842969e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.49819175e+06, 3.49829625e+06, 3.49829625e+06, 3.49818925e+06, 3.49829625e+06, 3.49818850e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.49721188e+05, 3.49894375e+05, 4.84467656e+05, 3.49794719e+05, 3.49063656e+05, 2.26234141e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.49591156e+05, 3.49562781e+05, 3.49610250e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.49591156e+05, 3.43768156e+05, 3.55407750e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.49591156e+05, 3.49591156e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.49578050e+06, 3.49578050e+06, 3.49578050e+06, 3.49578050e+06, 3.49578050e+06, 3.49578050e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.49552938e+05, 3.49642188e+05, 4.84122406e+05, 3.49627031e+05, 3.48813312e+05, 2.26125094e+05, ],
  }),
  ("nof_tree_events",                 184563),
  ("nof_db_events",                   375994),
  ("fsize_local",                     957070156), # 957.07MB, avg file size 957.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_2v2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 377996, ],
    'CountWeighted'                                                                  : [ 3.77985406e+05, 3.77993375e+05, 3.78012250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.77985406e+05, 3.77985406e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.77994000e+06, 3.78003100e+06, 3.78003100e+06, 3.77993700e+06, 3.78003100e+06, 3.77993250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.77934844e+05, 3.77745656e+05, 5.23568094e+05, 3.77871969e+05, 3.78135156e+05, 2.44925906e+05, ],
    'CountWeightedFull'                                                              : [ 3.77739062e+05, 3.77749000e+05, 3.77765000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.77739062e+05, 3.77739062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.77756625e+06, 3.77756625e+06, 3.77756625e+06, 3.77756625e+06, 3.77756625e+06, 3.77756625e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.77762812e+05, 3.77496875e+05, 5.23233500e+05, 3.77700062e+05, 3.77895594e+05, 2.44814812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.53060406e+05, 3.53018531e+05, 3.53116781e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.53060406e+05, 3.47383938e+05, 3.58706531e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.53060406e+05, 3.53060406e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.53059000e+06, 3.53067750e+06, 3.53067750e+06, 3.53058625e+06, 3.53067750e+06, 3.53058350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.53047438e+05, 3.52597562e+05, 4.88814719e+05, 3.52900875e+05, 3.53576656e+05, 2.29107625e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.52835688e+05, 3.52795406e+05, 3.52890688e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.52835688e+05, 3.47163938e+05, 3.58476969e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.52835688e+05, 3.52835688e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.52842950e+06, 3.52842950e+06, 3.52842950e+06, 3.52842950e+06, 3.52842950e+06, 3.52842950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.52889188e+05, 3.52370594e+05, 4.88509688e+05, 3.52742938e+05, 3.53357938e+05, 2.29005297e+05, ],
  }),
  ("nof_tree_events",                 168010),
  ("nof_db_events",                   377996),
  ("fsize_local",                     826483885), # 826.48MB, avg file size 826.48MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_2v2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399994, ],
    'CountWeighted'                                                                  : [ 3.99999375e+05, 3.99990812e+05, 4.00004375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.99999375e+05, 3.99999375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99987950e+06, 3.99997450e+06, 3.99997450e+06, 3.99987800e+06, 3.99997450e+06, 3.99987800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99869344e+05, 3.99748812e+05, 5.54167375e+05, 3.99930625e+05, 3.99949500e+05, 2.58978391e+05, ],
    'CountWeightedFull'                                                              : [ 3.99717375e+05, 3.99706875e+05, 3.99722906e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99717375e+05, 3.99717375e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, 3.99715475e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99680688e+05, 3.99472750e+05, 5.53781125e+05, 3.99742438e+05, 3.99661031e+05, 2.58856391e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.72676000e+05, 3.72613750e+05, 3.72742281e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.72676000e+05, 3.66516219e+05, 3.78815281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.72676000e+05, 3.72676000e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.72666000e+06, 3.72674800e+06, 3.72674800e+06, 3.72665825e+06, 3.72674800e+06, 3.72665800e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.72588531e+05, 3.72166812e+05, 5.16160688e+05, 3.72585469e+05, 3.73138156e+05, 2.41646344e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.72421500e+05, 3.72358125e+05, 3.72488531e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.72421500e+05, 3.66267688e+05, 3.78554875e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.72421500e+05, 3.72421500e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.72420400e+06, 3.72420400e+06, 3.72420400e+06, 3.72420400e+06, 3.72420400e+06, 3.72420400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.72415906e+05, 3.71917875e+05, 5.15811250e+05, 3.72413312e+05, 3.72877250e+05, 2.41534594e+05, ],
  }),
  ("nof_tree_events",                 185529),
  ("nof_db_events",                   399994),
  ("fsize_local",                     935605897), # 935.61MB, avg file size 935.61MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_0_1_hh_2v2t_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    18),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 4.00012062e+05, 3.99997750e+05, 4.00007969e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00012062e+05, 4.00012062e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99982800e+06, 3.99983700e+06, 3.99983700e+06, 3.99982750e+06, 3.99983700e+06, 3.99982750e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99924625e+05, 3.99961875e+05, 5.67576750e+05, 3.99935594e+05, 3.99222156e+05, 2.46694781e+05, ],
    'CountWeightedFull'                                                              : [ 3.99733438e+05, 3.99718156e+05, 3.99729188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99733438e+05, 3.99733438e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99706650e+06, 3.99706650e+06, 3.99706650e+06, 3.99706650e+06, 3.99706650e+06, 3.99706650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99705531e+05, 3.99686844e+05, 5.67177625e+05, 3.99715969e+05, 3.98935500e+05, 2.46559250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75268531e+05, 3.75237656e+05, 3.75284094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75268531e+05, 3.69459000e+05, 3.80990312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.75268531e+05, 3.75268531e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.75256550e+06, 3.75257300e+06, 3.75257300e+06, 3.75256500e+06, 3.75257300e+06, 3.75256500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.75236469e+05, 3.74958812e+05, 5.32286438e+05, 3.75156969e+05, 3.74957875e+05, 2.31744719e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75012656e+05, 3.74981188e+05, 3.75027469e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75012656e+05, 3.69208375e+05, 3.80729125e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.75012656e+05, 3.75012656e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75001875e+06, 3.75001875e+06, 3.75001875e+06, 3.75001875e+06, 3.75001875e+06, 3.75001875e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75033938e+05, 3.74706531e+05, 5.31919750e+05, 3.74953969e+05, 3.74694125e+05, 2.31619266e+05, ],
  }),
  ("nof_tree_events",                 76219),
  ("nof_db_events",                   399998),
  ("fsize_local",                     348953198), # 348.95MB, avg file size 348.95MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_1_hh_4v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 4.00015125e+05, 3.99981031e+05, 4.00012812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00015125e+05, 4.00015125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99984925e+06, 3.99987100e+06, 3.99987100e+06, 3.99984975e+06, 3.99987100e+06, 3.99984925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99943844e+05, 4.00131469e+05, 5.71289500e+05, 3.99952438e+05, 3.99288406e+05, 2.43828297e+05, ],
    'CountWeightedFull'                                                              : [ 3.99727062e+05, 3.99696125e+05, 3.99721094e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99727062e+05, 3.99727062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99699700e+06, 3.99699700e+06, 3.99699700e+06, 3.99699700e+06, 3.99699700e+06, 3.99699700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99711188e+05, 3.99842875e+05, 5.70889750e+05, 3.99719562e+05, 3.99009531e+05, 2.43686422e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.68347062e+05, 3.68278438e+05, 3.68402188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.68347062e+05, 3.61203094e+05, 3.75453719e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.68347062e+05, 3.68347062e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.68335250e+06, 3.68337100e+06, 3.68337100e+06, 3.68335250e+06, 3.68337100e+06, 3.68335250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.68341562e+05, 3.68160688e+05, 5.26029188e+05, 3.68236156e+05, 3.68295062e+05, 2.24837797e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.68086188e+05, 3.68018812e+05, 3.68139344e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.68086188e+05, 3.60948000e+05, 3.75187062e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.68086188e+05, 3.68086188e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.68076500e+06, 3.68076500e+06, 3.68076500e+06, 3.68076500e+06, 3.68076500e+06, 3.68076500e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.68130719e+05, 3.67899375e+05, 5.25666062e+05, 3.68024875e+05, 3.68040344e+05, 2.24709078e+05, ],
  }),
  ("nof_tree_events",                 76496),
  ("nof_db_events",                   399998),
  ("fsize_local",                     371632777), # 371.63MB, avg file size 371.63MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_2_hh_4v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    23),
  ("nof_events",                      {
    'Count'                                                                          : [ 387998, ],
    'CountWeighted'                                                                  : [ 3.87986688e+05, 3.87997219e+05, 3.88002750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.87986688e+05, 3.87986688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.87989775e+06, 3.87994425e+06, 3.87994425e+06, 3.87989900e+06, 3.87994425e+06, 3.87989675e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.87861688e+05, 3.87934219e+05, 5.49727062e+05, 3.88064406e+05, 3.86968375e+05, 2.39941062e+05, ],
    'CountWeightedFull'                                                              : [ 3.87735188e+05, 3.87747125e+05, 3.87751156e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.87735188e+05, 3.87735188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, 3.87741900e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.87657000e+05, 3.87686000e+05, 5.49374250e+05, 3.87859125e+05, 3.86715625e+05, 2.39814891e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.66972375e+05, 3.66937781e+05, 3.67011375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.66972375e+05, 3.61982562e+05, 3.71873188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.66972375e+05, 3.66972375e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.66970700e+06, 3.66975050e+06, 3.66975050e+06, 3.66970800e+06, 3.66975050e+06, 3.66970600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.66889781e+05, 3.66661250e+05, 5.19810719e+05, 3.66986594e+05, 3.66445719e+05, 2.27223078e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.66737844e+05, 3.66703969e+05, 3.66776250e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.66737844e+05, 3.61751781e+05, 3.71634875e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.66737844e+05, 3.66737844e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.66740225e+06, 3.66740225e+06, 3.66740225e+06, 3.66740225e+06, 3.66740225e+06, 3.66740225e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.66698500e+05, 3.66429875e+05, 5.19481312e+05, 3.66794812e+05, 3.66208906e+05, 2.27105047e+05, ],
  }),
  ("nof_tree_events",                 78428),
  ("nof_db_events",                   387998),
  ("fsize_local",                     356882150), # 356.88MB, avg file size 356.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_1_0_hh_4v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    25),
  ("nof_events",                      {
    'Count'                                                                          : [ 389999, ],
    'CountWeighted'                                                                  : [ 3.89980812e+05, 3.90007812e+05, 3.90002062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.89980812e+05, 3.89980812e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89975625e+06, 3.89983675e+06, 3.89983675e+06, 3.89975525e+06, 3.89983675e+06, 3.89975525e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.89829750e+05, 3.89789906e+05, 5.55362750e+05, 3.89978125e+05, 3.89840219e+05, 2.39050156e+05, ],
    'CountWeightedFull'                                                              : [ 3.89657562e+05, 3.89683031e+05, 3.89676281e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.89657562e+05, 3.89657562e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.89659825e+06, 3.89659825e+06, 3.89659825e+06, 3.89659825e+06, 3.89659825e+06, 3.89659825e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.89600344e+05, 3.89464469e+05, 5.54914562e+05, 3.89749125e+05, 3.89523938e+05, 2.38909203e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.62119188e+05, 3.62096156e+05, 3.62151969e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.62119188e+05, 3.55966844e+05, 3.68272594e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.62119188e+05, 3.62119188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.62113550e+06, 3.62120350e+06, 3.62120350e+06, 3.62113450e+06, 3.62120350e+06, 3.62113425e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.62010219e+05, 3.61681469e+05, 5.15411062e+05, 3.62074156e+05, 3.62347031e+05, 2.22305500e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.61830344e+05, 3.61806375e+05, 3.61862062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.61830344e+05, 3.55685094e+05, 3.67976375e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.61830344e+05, 3.61830344e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.61831125e+06, 3.61831125e+06, 3.61831125e+06, 3.61831125e+06, 3.61831125e+06, 3.61831125e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.61800625e+05, 3.61392094e+05, 5.15012031e+05, 3.61864531e+05, 3.62064781e+05, 2.22176297e+05, ],
  }),
  ("nof_tree_events",                 78076),
  ("nof_db_events",                   389999),
  ("fsize_local",                     412591466), # 412.59MB, avg file size 412.59MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_2_1_hh_4v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 387996, ],
    'CountWeighted'                                                                  : [ 3.88006719e+05, 3.87948438e+05, 3.87994219e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 3.88006719e+05, 3.88006719e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.87955500e+06, 3.87959500e+06, 3.87959500e+06, 3.87955550e+06, 3.87959500e+06, 3.87955500e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.87824594e+05, 3.88098188e+05, 5.51860938e+05, 3.87989812e+05, 3.87057125e+05, 2.38098016e+05, ],
    'CountWeightedFull'                                                              : [ 3.87680188e+05, 3.87622531e+05, 3.87669562e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.87680188e+05, 3.87680188e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.87634800e+06, 3.87634800e+06, 3.87634800e+06, 3.87634800e+06, 3.87634800e+06, 3.87634800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.87596781e+05, 3.87771250e+05, 5.51403062e+05, 3.87762406e+05, 3.86734750e+05, 2.37958031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.61206781e+05, 3.61116812e+05, 3.61263000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.61206781e+05, 3.55228375e+05, 3.67171750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.61206781e+05, 3.61206781e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.61186325e+06, 3.61189150e+06, 3.61189150e+06, 3.61186350e+06, 3.61189150e+06, 3.61186325e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.61080094e+05, 3.61076656e+05, 5.13573438e+05, 3.61155156e+05, 3.60698781e+05, 2.21934359e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.60909750e+05, 3.60819750e+05, 3.60967156e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.60909750e+05, 3.54937906e+05, 3.66868375e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.60909750e+05, 3.60909750e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.60892875e+06, 3.60892875e+06, 3.60892875e+06, 3.60892875e+06, 3.60892875e+06, 3.60892875e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.60871688e+05, 3.60779281e+05, 5.13156344e+05, 3.60947500e+05, 3.60404000e+05, 2.21806281e+05, ],
  }),
  ("nof_tree_events",                 78603),
  ("nof_db_events",                   387996),
  ("fsize_local",                     407257861), # 407.26MB, avg file size 407.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_0p5_1_1_hh_4v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    17),
  ("nof_events",                      {
    'Count'                                                                          : [ 399999, ],
    'CountWeighted'                                                                  : [ 4.00001219e+05, 3.99967812e+05, 3.99987250e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00001219e+05, 4.00001219e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99981925e+06, 3.99992550e+06, 3.99992550e+06, 3.99981250e+06, 3.99992550e+06, 3.99980925e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99919812e+05, 4.00107562e+05, 5.68116875e+05, 3.99943125e+05, 3.99300438e+05, 2.46394969e+05, ],
    'CountWeightedFull'                                                              : [ 3.99702906e+05, 3.99674125e+05, 3.99688750e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99702906e+05, 3.99702906e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, 3.99695700e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99693188e+05, 3.99803375e+05, 5.67702875e+05, 3.99716125e+05, 3.99015594e+05, 2.46255312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74326250e+05, 3.74264031e+05, 3.74364531e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74326250e+05, 3.68450156e+05, 3.80148938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.74326250e+05, 3.74326250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.74311900e+06, 3.74320750e+06, 3.74320750e+06, 3.74311200e+06, 3.74320750e+06, 3.74310900e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74291562e+05, 3.74177500e+05, 5.31398500e+05, 3.74224312e+05, 3.74004375e+05, 2.30880922e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74055250e+05, 3.73995250e+05, 3.74092375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74055250e+05, 3.68184812e+05, 3.79872375e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.74055250e+05, 3.74055250e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, 3.74050200e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74082406e+05, 3.73900938e+05, 5.31021500e+05, 3.74015406e+05, 3.73744812e+05, 2.30751938e+05, ],
  }),
  ("nof_tree_events",                 80886),
  ("nof_db_events",                   399999),
  ("fsize_local",                     396483682), # 396.48MB, avg file size 396.48MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1p5_1_1_hh_4v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 399998, ],
    'CountWeighted'                                                                  : [ 4.00009594e+05, 4.00016562e+05, 3.99996875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.00009594e+05, 4.00009594e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99993500e+06, 3.99998100e+06, 3.99998100e+06, 3.99993400e+06, 3.99998100e+06, 3.99993300e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99911625e+05, 4.00011031e+05, 5.68026250e+05, 3.99924188e+05, 3.99178719e+05, 2.46241750e+05, ],
    'CountWeightedFull'                                                              : [ 3.99716812e+05, 3.99722000e+05, 3.99704188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 3.99716812e+05, 3.99716812e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99705400e+06, 3.99705400e+06, 3.99705400e+06, 3.99705400e+06, 3.99705400e+06, 3.99705400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99684000e+05, 3.99717375e+05, 5.67612188e+05, 3.99696844e+05, 3.98885781e+05, 2.46101750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73385750e+05, 3.73347812e+05, 3.73417094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73385750e+05, 3.67361188e+05, 3.79377938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.73385750e+05, 3.73385750e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.73377075e+06, 3.73380425e+06, 3.73380425e+06, 3.73376925e+06, 3.73380425e+06, 3.73376875e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.73345031e+05, 3.73129688e+05, 5.29994625e+05, 3.73265188e+05, 3.73009438e+05, 2.30188688e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.73119188e+05, 3.73080156e+05, 3.73151656e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.73119188e+05, 3.67100438e+05, 3.79105625e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 3.73119188e+05, 3.73119188e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.73113950e+06, 3.73113950e+06, 3.73113950e+06, 3.73113950e+06, 3.73113950e+06, 3.73113950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.73135844e+05, 3.72863250e+05, 5.29618438e+05, 3.73056031e+05, 3.72742469e+05, 2.30059859e+05, ],
  }),
  ("nof_tree_events",                 80638),
  ("nof_db_events",                   399998),
  ("fsize_local",                     405577504), # 405.58MB, avg file size 405.58MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_vbf_nonresonant_1_0_1_hh_4v_dipoleRecoilOff"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 278930),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1270630215), # 1.27GB, avg file size 1.27GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    9),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 4.00005375e+05, 3.99969812e+05, 3.99952312e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10150812e+05, 4.84345188e+05, 4.59564406e+05, 4.21334062e+05, 4.00004031e+05, 3.79471688e+05, 3.54133625e+05, 3.36149688e+05, 3.18887906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10150812e+05, 3.18887875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99954000e+06, 3.99954800e+06, 3.99955250e+06, 3.99953975e+06, 3.99906175e+06, 3.99904475e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00075031e+05, 4.00100125e+05, 5.55284562e+05, 3.99905812e+05, 3.99843594e+05, 2.61596453e+05, ],
    'CountWeightedFull'                                                              : [ 3.99973875e+05, 3.99938875e+05, 3.99921062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10111125e+05, 4.84307531e+05, 4.59528719e+05, 4.21301125e+05, 3.99972562e+05, 3.79442188e+05, 3.54106062e+05, 3.36123562e+05, 3.18863062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10111125e+05, 3.18863062e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99924450e+06, 3.99924000e+06, 3.99924450e+06, 3.99924450e+06, 3.99875350e+06, 3.99874925e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00047219e+05, 4.00068969e+05, 5.55240062e+05, 3.99873250e+05, 3.99812188e+05, 2.61577625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87703750e+05, 3.87661469e+05, 3.87693219e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87703750e+05, 3.84776375e+05, 3.90578875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94351969e+05, 4.69475438e+05, 4.45559938e+05, 4.08276188e+05, 3.87701188e+05, 3.67898188e+05, 3.43151125e+05, 3.25812000e+05, 3.09155250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94351969e+05, 3.09155188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87671900e+06, 3.87672650e+06, 3.87673100e+06, 3.87671900e+06, 3.87626150e+06, 3.87624550e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88224094e+05, 3.87651062e+05, 5.38067125e+05, 3.87052625e+05, 3.87792094e+05, 2.53711344e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87674312e+05, 3.87632438e+05, 3.87664000e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87674312e+05, 3.84747375e+05, 3.90549062e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94314688e+05, 4.69440000e+05, 4.45526281e+05, 4.08245281e+05, 3.87671688e+05, 3.67870438e+05, 3.43125250e+05, 3.25787438e+05, 3.09131906e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94314688e+05, 3.09131875e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87644000e+06, 3.87643575e+06, 3.87644000e+06, 3.87644000e+06, 3.87597100e+06, 3.87596675e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88198000e+05, 3.87621875e+05, 5.38025250e+05, 3.87022125e+05, 3.87762531e+05, 2.53693625e+05, ],
  }),
  ("nof_tree_events",                 272612),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1215571885), # 1.22GB, avg file size 1.22GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 290410),
  ("nof_db_events",                   388000),
  ("fsize_local",                     1441063247), # 1.44GB, avg file size 1.44GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 281263),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1282534439), # 1.28GB, avg file size 1.28GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99998781e+05, 3.99975250e+05, 3.99986594e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10043062e+05, 4.84407156e+05, 4.59750188e+05, 4.21206156e+05, 3.99998781e+05, 3.79571375e+05, 3.53999188e+05, 3.36114125e+05, 3.18937688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10043062e+05, 3.18937688e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99969275e+06, 3.99969275e+06, 3.99969275e+06, 3.99969275e+06, 3.99969275e+06, 3.99969275e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99976250e+05, 4.00042906e+05, 5.54902062e+05, 4.00077938e+05, 3.99561125e+05, 2.61750500e+05, ],
    'CountWeightedFull'                                                              : [ 3.99968125e+05, 3.99944406e+05, 3.99955719e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10003781e+05, 4.84369938e+05, 4.59715094e+05, 4.21173688e+05, 3.99968125e+05, 3.79542250e+05, 3.53971938e+05, 3.36088312e+05, 3.18913125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10003781e+05, 3.18913125e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99938400e+06, 3.99938400e+06, 3.99938400e+06, 3.99938400e+06, 3.99938400e+06, 3.99938400e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99948125e+05, 4.00012438e+05, 5.54858188e+05, 4.00044906e+05, 3.99530031e+05, 2.61731219e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87758750e+05, 3.87720406e+05, 3.87772812e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87758750e+05, 3.84843062e+05, 3.90624688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94322750e+05, 4.69611594e+05, 4.45819875e+05, 4.08209750e+05, 3.87758750e+05, 3.68058156e+05, 3.43066844e+05, 3.25829344e+05, 3.09254906e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94322750e+05, 3.09254906e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, 3.87743350e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88175125e+05, 3.87739719e+05, 5.37750312e+05, 3.87294844e+05, 3.87468688e+05, 2.53896891e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87729844e+05, 3.87691344e+05, 3.87743750e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87729844e+05, 3.84814562e+05, 3.90595438e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94285750e+05, 4.69576406e+05, 4.45786688e+05, 4.08179188e+05, 3.87729844e+05, 3.68030719e+05, 3.43041219e+05, 3.25805000e+05, 3.09231812e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94285750e+05, 3.09231812e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87714275e+06, 3.87714275e+06, 3.87714275e+06, 3.87714275e+06, 3.87714275e+06, 3.87714275e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88148656e+05, 3.87711125e+05, 5.37709125e+05, 3.87263812e+05, 3.87439344e+05, 2.53878672e+05, ],
  }),
  ("nof_tree_events",                 272383),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1217180779), # 1.22GB, avg file size 1.22GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    21),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99981438e+05, 3.99985219e+05, 3.99982125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.13017562e+05, 4.82679688e+05, 4.54507219e+05, 4.25213875e+05, 3.99981438e+05, 3.76556312e+05, 3.58456688e+05, 3.37115281e+05, 3.17327500e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.13017562e+05, 3.17327500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99949175e+06, 3.99950350e+06, 3.99950350e+06, 3.99949200e+06, 3.99950350e+06, 3.99949175e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99954812e+05, 4.00328062e+05, 5.55735750e+05, 4.00043688e+05, 3.98689312e+05, 2.60454578e+05, ],
    'CountWeightedFull'                                                              : [ 3.99946375e+05, 3.99950625e+05, 3.99947375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.12972625e+05, 4.82637812e+05, 4.54467938e+05, 4.25176781e+05, 3.99946375e+05, 3.76523625e+05, 3.58425188e+05, 3.37085875e+05, 3.17300000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.12972625e+05, 3.17300000e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99915800e+06, 3.99915800e+06, 3.99915800e+06, 3.99915800e+06, 3.99915800e+06, 3.99915800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99924562e+05, 4.00292594e+05, 5.55685938e+05, 4.00008031e+05, 3.98655375e+05, 2.60433922e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.86937375e+05, 3.86925438e+05, 3.86959250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.86937375e+05, 3.83863688e+05, 3.89962750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.96154500e+05, 4.66961875e+05, 4.39827500e+05, 4.11219031e+05, 3.86937375e+05, 3.64379438e+05, 3.46646625e+05, 3.26112844e+05, 3.07054625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.96154500e+05, 3.07054625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.86918650e+06, 3.86919500e+06, 3.86919500e+06, 3.86918650e+06, 3.86919500e+06, 3.86918650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87365562e+05, 3.87182688e+05, 5.37425875e+05, 3.86425281e+05, 3.85817531e+05, 2.52104469e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.86905250e+05, 3.86893562e+05, 3.86927312e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.86905250e+05, 3.83832188e+05, 3.89930000e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.96113344e+05, 4.66923312e+05, 4.39791438e+05, 4.11184938e+05, 3.86905250e+05, 3.64349344e+05, 3.46617719e+05, 3.26085812e+05, 3.07029344e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.96113344e+05, 3.07029344e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.86887600e+06, 3.86887600e+06, 3.86887600e+06, 3.86887600e+06, 3.86887600e+06, 3.86887600e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87337188e+05, 3.87150312e+05, 5.37380125e+05, 3.86391875e+05, 3.85785906e+05, 2.52085156e+05, ],
  }),
  ("nof_tree_events",                 283346),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1305904381), # 1.31GB, avg file size 1.31GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99989938e+05, 3.99966625e+05, 3.99978562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10293125e+05, 4.84250750e+05, 4.59284812e+05, 4.21534188e+05, 3.99985312e+05, 3.79314250e+05, 3.54354938e+05, 3.36199750e+05, 3.18807188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10293125e+05, 3.18807188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99963600e+06, 3.99964850e+06, 3.99964850e+06, 3.99963600e+06, 3.99964850e+06, 3.99963600e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.99893562e+05, 3.99999312e+05, 5.55705250e+05, 4.00123250e+05, 4.00213250e+05, 2.61487156e+05, ],
    'CountWeightedFull'                                                              : [ 3.99957344e+05, 3.99934625e+05, 3.99945812e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10251625e+05, 4.84211438e+05, 4.59247781e+05, 4.21499906e+05, 3.99952719e+05, 3.79283469e+05, 3.54325938e+05, 3.36172406e+05, 3.18781250e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10251625e+05, 3.18781250e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, 3.99932150e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.99865188e+05, 3.99967062e+05, 5.55656688e+05, 4.00089688e+05, 4.00178594e+05, 2.61467828e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87580938e+05, 3.87534500e+05, 3.87602656e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87580938e+05, 3.84632562e+05, 3.90477625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94345438e+05, 4.69245719e+05, 4.45158094e+05, 4.08350500e+05, 3.87576719e+05, 3.67639500e+05, 3.43265250e+05, 3.25766719e+05, 3.08987812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94345438e+05, 3.08987812e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87564025e+06, 3.87565200e+06, 3.87565200e+06, 3.87564050e+06, 3.87565200e+06, 3.87564025e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.87924938e+05, 3.87477188e+05, 5.38263875e+05, 3.87157250e+05, 3.87946656e+05, 2.53535906e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87550312e+05, 3.87504312e+05, 3.87571938e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87550312e+05, 3.84602438e+05, 3.90446625e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94306375e+05, 4.69208750e+05, 4.45123188e+05, 4.08318188e+05, 3.87546062e+05, 3.67610500e+05, 3.43238031e+05, 3.25741000e+05, 3.08963469e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94306375e+05, 3.08963469e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87534550e+06, 3.87534550e+06, 3.87534550e+06, 3.87534550e+06, 3.87534550e+06, 3.87534550e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.87898188e+05, 3.87446750e+05, 5.38218250e+05, 3.87125812e+05, 3.87914156e+05, 2.53517734e+05, ],
  }),
  ("nof_tree_events",                 273714),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1222875002), # 1.22GB, avg file size 1.22GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 255549),
  ("nof_db_events",                   374000),
  ("fsize_local",                     1136817902), # 1.14GB, avg file size 1.14GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    20),
  ("nof_events",                      {
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85966219e+05, 3.85978906e+05, 3.85974188e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92136500e+05, 4.67480250e+05, 4.43748281e+05, 4.06380156e+05, 3.85961406e+05, 3.66342000e+05, 3.41512031e+05, 3.24328969e+05, 3.07805750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92136500e+05, 3.07805750e+05, ],
    'CountWeightedPSWeight'                                                          : [ 1.95978488e+06, 1.95426475e+06, 2.60344900e+06, 1.96116925e+06, 1.84867975e+06, 1.28277662e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.85872875e+05, 3.85849500e+05, 5.35713938e+05, 3.86162844e+05, 3.86028219e+05, 2.52571844e+05, ],
    'CountWeightedFull'                                                              : [ 3.85936375e+05, 3.85949062e+05, 3.85944250e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92098188e+05, 4.67443938e+05, 4.43713875e+05, 4.06348688e+05, 3.85931531e+05, 3.66313594e+05, 3.41485375e+05, 3.24303688e+05, 3.07781844e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92098188e+05, 3.07781844e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 1.95965012e+06, 1.95411475e+06, 2.60324400e+06, 1.96100962e+06, 1.84853738e+06, 1.28268412e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85846250e+05, 3.85819750e+05, 5.35671688e+05, 3.86131406e+05, 3.85998281e+05, 2.52553594e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74067812e+05, 3.74060938e+05, 3.74085250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74067812e+05, 3.71234531e+05, 3.76850750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.76844312e+05, 4.53078875e+05, 4.30179531e+05, 3.93742719e+05, 3.74062812e+05, 3.55130844e+05, 3.30883188e+05, 3.14321094e+05, 2.98378656e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.76844312e+05, 2.98378656e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 1.90146150e+06, 1.89333575e+06, 2.52262600e+06, 1.89801500e+06, 1.79302188e+06, 1.24401538e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74387344e+05, 3.73807406e+05, 5.19063438e+05, 3.73724906e+05, 3.74376656e+05, 2.44938328e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74039719e+05, 3.74032781e+05, 3.74057062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74039719e+05, 3.71206875e+05, 3.76822219e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.76808281e+05, 4.53044719e+05, 4.30147125e+05, 3.93713031e+05, 3.74034750e+05, 3.55104156e+05, 3.30858156e+05, 3.14297344e+05, 2.98356188e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.76808281e+05, 2.98356188e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 1.90133438e+06, 1.89319388e+06, 2.52243275e+06, 1.89786488e+06, 1.79288812e+06, 1.24392850e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74362312e+05, 3.73779406e+05, 5.19023656e+05, 3.73695344e+05, 3.74348438e+05, 2.44921141e+05, ],
  }),
  ("nof_tree_events",                 263352),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1174215617), # 1.17GB, avg file size 1.17GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 309353),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1525077517), # 1.53GB, avg file size 1.53GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    19),
  ("nof_events",                      {
    'Count'                                                                          : [ 386000, ],
    'CountWeighted'                                                                  : [ 3.85969562e+05, 3.85944500e+05, 3.85987125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92241656e+05, 4.67366406e+05, 4.43461688e+05, 4.06540562e+05, 3.85965562e+05, 3.66173125e+05, 3.41694750e+05, 3.24352938e+05, 3.07708188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92241656e+05, 3.07708188e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.85307800e+06, 3.84637700e+06, 3.85445200e+06, 3.85310550e+06, 3.79028500e+06, 3.78236950e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.85939750e+05, 3.85935719e+05, 5.35786625e+05, 3.86055781e+05, 3.85927094e+05, 2.52441938e+05, ],
    'CountWeightedFull'                                                              : [ 3.85938500e+05, 3.85913844e+05, 3.85955875e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92202750e+05, 4.67329031e+05, 4.43426125e+05, 4.06508281e+05, 3.85934469e+05, 3.66143750e+05, 3.41667688e+05, 3.24327000e+05, 3.07683500e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92202750e+05, 3.07683500e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.85276400e+06, 3.84607300e+06, 3.85414700e+06, 3.85279450e+06, 3.78998500e+06, 3.78206450e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85910875e+05, 3.85903688e+05, 5.35741188e+05, 3.86022219e+05, 3.85894219e+05, 2.52422031e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.73966500e+05, 3.73941312e+05, 3.73989188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.73966500e+05, 3.71112062e+05, 3.76768312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.76826562e+05, 4.52852406e+05, 4.29792562e+05, 3.93797812e+05, 3.73962250e+05, 3.54877188e+05, 3.30977281e+05, 3.14264250e+05, 2.98208688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.76826562e+05, 2.98208688e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.73333975e+06, 3.72689950e+06, 3.73467900e+06, 3.73335600e+06, 3.67281750e+06, 3.66518250e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.74361125e+05, 3.73896312e+05, 5.18902125e+05, 3.73514312e+05, 3.73956000e+05, 2.44725219e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.73936938e+05, 3.73912000e+05, 3.73959531e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.73936938e+05, 3.71082906e+05, 3.76738438e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.76789125e+05, 4.52816688e+05, 4.29758688e+05, 3.93766812e+05, 3.73932688e+05, 3.54849250e+05, 3.30951188e+05, 3.14239500e+05, 2.98185250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.76789125e+05, 2.98185250e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.73304450e+06, 3.72660750e+06, 3.73438600e+06, 3.73306350e+06, 3.67253000e+06, 3.66489650e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.74334000e+05, 3.73867000e+05, 5.18860375e+05, 3.73482906e+05, 3.73925844e+05, 2.44706547e+05, ],
  }),
  ("nof_tree_events",                 263496),
  ("nof_db_events",                   386000),
  ("fsize_local",                     1175992477), # 1.18GB, avg file size 1.18GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    15),
  ("nof_events",                      {
    'Count'                                                                          : [ 400000, ],
    'CountWeighted'                                                                  : [ 3.99953875e+05, 3.99978312e+05, 3.99942000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 5.10468719e+05, 4.84131156e+05, 4.58934562e+05, 4.21776469e+05, 3.99952562e+05, 3.79116188e+05, 3.54627406e+05, 3.36252438e+05, 3.18700656e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 5.10468719e+05, 3.18700656e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.99959650e+06, 3.99959650e+06, 3.99959650e+06, 3.99959650e+06, 3.99959650e+06, 3.99959650e+06, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 4.00062750e+05, 4.00302406e+05, 5.54879000e+05, 3.99932250e+05, 3.99224625e+05, 2.61640250e+05, ],
    'CountWeightedFull'                                                              : [ 3.99921312e+05, 3.99945156e+05, 3.99910062e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 5.10427000e+05, 4.84091688e+05, 4.58897250e+05, 4.21742000e+05, 3.99920031e+05, 3.79085375e+05, 3.54598344e+05, 3.36225062e+05, 3.18674688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 5.10427000e+05, 3.18674688e+05, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, 3.99926950e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 4.00033094e+05, 4.00270438e+05, 5.54831688e+05, 3.99897750e+05, 3.99190562e+05, 2.61619891e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.87562938e+05, 3.87553969e+05, 3.87583094e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.87562938e+05, 3.84614812e+05, 3.90458750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.94528281e+05, 4.69137500e+05, 4.44825250e+05, 4.08596188e+05, 3.87561188e+05, 3.67451875e+05, 3.43537625e+05, 3.25825625e+05, 3.08888281e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.94528281e+05, 3.08888281e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.87566400e+06, 3.87566400e+06, 3.87566400e+06, 3.87566400e+06, 3.87566400e+06, 3.87566400e+06, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.88086531e+05, 3.87790812e+05, 5.37531625e+05, 3.86993562e+05, 3.87027438e+05, 2.53674094e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.87532438e+05, 3.87522875e+05, 3.87553062e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.87532438e+05, 3.84584781e+05, 3.90427781e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.94489250e+05, 4.69100562e+05, 4.44790250e+05, 4.08563906e+05, 3.87530656e+05, 3.67423031e+05, 3.43510375e+05, 3.25800094e+05, 3.08864000e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.94489250e+05, 3.08864000e+05, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.87535800e+06, 3.87535800e+06, 3.87535800e+06, 3.87535800e+06, 3.87535800e+06, 3.87535800e+06, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.88058812e+05, 3.87760969e+05, 5.37487438e+05, 3.86961188e+05, 3.86995625e+05, 2.53655031e+05, ],
  }),
  ("nof_tree_events",                 275385),
  ("nof_db_events",                   400000),
  ("fsize_local",                     1231878228), # 1.23GB, avg file size 1.23GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 269467),
  ("nof_db_events",                   396000),
  ("fsize_local",                     1196764495), # 1.20GB, avg file size 1.20GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 993800, ],
    'CountWeighted'                                                                  : [ 9.35851250e+05, 9.35668750e+05, 9.35816500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08269050e+06, 1.06366338e+06, 1.05026100e+06, 9.57200438e+05, 9.35851188e+05, 9.18644688e+05, 8.48701375e+05, 8.26740875e+05, 8.08004125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12098862e+06, 7.89224500e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.35767562e+05, 9.35778125e+05, 1.29037900e+06, 9.35887875e+05, 9.35258125e+05, 6.16218125e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.36766484e+04, 6.36860898e+04, 8.78388047e+04, 6.36956953e+04, 6.36783555e+04, 4.19431953e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.11437250e+05, 9.11260562e+05, 9.11449750e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.11437250e+05, 9.05448312e+05, 9.17280312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.05409312e+06, 1.03579812e+06, 1.02295031e+06, 9.32018875e+05, 9.11437188e+05, 8.94870125e+05, 8.26436625e+05, 8.05249000e+05, 7.87166875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.09140838e+06, 7.68878938e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.11472625e+05, 9.11224812e+05, 1.25646712e+06, 9.11342375e+05, 9.11089625e+05, 6.00413938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 6.20071562e+04, 6.19986641e+04, 8.55085312e+04, 6.20089961e+04, 6.20159844e+04, 4.08559102e+04, ],
  }),
  ("nof_tree_events",                 659374),
  ("nof_db_events",                   993800),
  ("fsize_local",                     2796953514), # 2.80GB, avg file size 2.80GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    55),
  ("nof_events",                      {
    'Count'                                                                          : [ 973200, ],
    'CountWeighted'                                                                  : [ 8.72135750e+05, 8.72118000e+05, 8.72067125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.92976812e+05, 9.77088750e+05, 9.66615562e+05, 8.92237375e+05, 8.72084500e+05, 8.56363188e+05, 8.00844625e+05, 7.78974438e+05, 7.60652750e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03559288e+06, 7.37506375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.72235562e+05, 8.72399375e+05, 1.20490488e+06, 8.72057875e+05, 8.71816500e+05, 5.72707500e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.91179453e+04, 2.91169238e+04, 4.02133438e+04, 2.91169180e+04, 2.91232793e+04, 1.91421523e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.48528625e+05, 8.48505750e+05, 8.48480250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.48528625e+05, 8.42776375e+05, 8.54143625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.65739125e+05, 9.50499062e+05, 9.40503000e+05, 8.67879188e+05, 8.48485375e+05, 8.33351688e+05, 7.79048875e+05, 7.57959875e+05, 7.40292875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00722794e+06, 7.17762500e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.48728375e+05, 8.48622562e+05, 1.17204862e+06, 8.48309188e+05, 8.48461875e+05, 5.57449688e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.83298457e+04, 2.83202461e+04, 3.91115625e+04, 2.83199629e+04, 2.83388477e+04, 1.86300742e+04, ],
  }),
  ("nof_tree_events",                 674305),
  ("nof_db_events",                   973200),
  ("fsize_local",                     2917644218), # 2.92GB, avg file size 2.92GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    62),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 8.62699375e+05, 8.62784438e+05, 8.62588500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.84110750e+05, 9.70390688e+05, 9.61615875e+05, 8.80358938e+05, 8.62660312e+05, 8.48880938e+05, 7.87947750e+05, 7.68524625e+05, 7.52163375e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03623512e+06, 7.20361625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.62675000e+05, 8.62634375e+05, 1.19285550e+06, 8.62719062e+05, 8.62023188e+05, 5.65253812e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31737900e+04, 1.31703281e+04, 1.82129141e+04, 1.31760439e+04, 1.31758398e+04, 8.64208984e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.39325875e+05, 8.39327750e+05, 8.39302625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.39325875e+05, 8.33632375e+05, 8.44890500e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.57019875e+05, 9.43929438e+05, 9.35617750e+05, 8.56272188e+05, 8.39291562e+05, 8.26080625e+05, 7.66477750e+05, 7.47796062e+05, 7.32056375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00776438e+06, 7.01107000e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.39433938e+05, 8.39076688e+05, 1.16020125e+06, 8.39179000e+05, 8.38910562e+05, 5.50263875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.28172754e+04, 1.28091855e+04, 1.77126504e+04, 1.28148809e+04, 1.28212061e+04, 8.41160352e+03, ],
  }),
  ("nof_tree_events",                 675770),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     2973262350), # 2.97GB, avg file size 2.97GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    58),
  ("nof_events",                      {
    'Count'                                                                          : [ 991200, ],
    'CountWeighted'                                                                  : [ 9.75626250e+05, 9.75693250e+05, 9.75702062e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.16860788e+06, 1.14658975e+06, 1.12963400e+06, 9.95071750e+05, 9.75590125e+05, 9.59165250e+05, 8.56874125e+05, 8.39680312e+05, 8.24117312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.20429662e+06, 8.07343375e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.75826875e+05, 9.76011125e+05, 1.34362962e+06, 9.75431250e+05, 9.74448375e+05, 6.43645438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 7.95415391e+04, 7.95522422e+04, 1.09577094e+05, 7.95029844e+04, 7.94826797e+04, 5.24578047e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.52048250e+05, 9.52063875e+05, 9.52126438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.52048250e+05, 9.46138188e+05, 9.57784312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.13982188e+06, 1.11864512e+06, 1.10235875e+06, 9.70753062e+05, 9.52013125e+05, 9.36188500e+05, 8.36058125e+05, 8.19501125e+05, 8.04495375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.17471100e+06, 7.88093625e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.52386750e+05, 9.52222312e+05, 1.31075512e+06, 9.51652812e+05, 9.51155750e+05, 6.28464375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.76214062e+04, 7.76035078e+04, 1.06883945e+05, 7.75551094e+04, 7.75744219e+04, 5.12141641e+04, ],
  }),
  ("nof_tree_events",                 575763),
  ("nof_db_events",                   991200),
  ("fsize_local",                     2354967008), # 2.35GB, avg file size 2.35GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 177445),
  ("nof_db_events",                   399996),
  ("fsize_local",                     849076787), # 849.08MB, avg file size 849.08MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    86),
  ("nof_events",                      {
    'Count'                                                                          : [ 3859942, ],
    'CountWeighted'                                                                  : [ 3.85950975e+06, 3.85948512e+06, 3.85959238e+06, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92243188e+06, 4.67387362e+06, 4.43502588e+06, 4.06536738e+06, 3.85948825e+06, 3.66201338e+06, 3.41689688e+06, 3.24363375e+06, 3.07730150e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92243262e+06, 3.07730050e+06, ],
    'CountWeightedPSWeight'                                                          : [ 3.85962090e+07, 3.85899760e+07, 3.85962450e+07, 3.85962050e+07, 3.84519940e+07, 3.84456870e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.85965612e+06, 3.85874600e+06, 5.49814325e+06, 3.86034400e+06, 3.85768262e+06, 2.40289200e+06, ],
    'CountWeightedFull'                                                              : [ 3.85880550e+06, 3.85877650e+06, 3.85887500e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92152238e+06, 4.67301125e+06, 4.43420950e+06, 4.06461650e+06, 3.85878350e+06, 3.66133838e+06, 3.41626650e+06, 3.24303562e+06, 3.07673450e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92152338e+06, 3.07673350e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.85891020e+07, 3.85828380e+07, 3.85891040e+07, 3.85891020e+07, 3.84448840e+07, 3.84386150e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85897150e+06, 3.85804050e+06, 5.49711700e+06, 3.85961075e+06, 3.85696162e+06, 2.40245681e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.74713025e+06, 3.74691050e+06, 3.74737888e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 3.74713025e+06, 3.72007050e+06, 3.77355738e+06, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.77792812e+06, 4.53786000e+06, 4.30694988e+06, 3.94591200e+06, 3.74710738e+06, 3.55615662e+06, 3.31641025e+06, 3.14907075e+06, 2.98827038e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.77792912e+06, 2.98826962e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.74720540e+07, 3.74660140e+07, 3.74720860e+07, 3.74720520e+07, 3.73331990e+07, 3.73270890e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.75144300e+06, 3.74530900e+06, 5.33630125e+06, 3.74249050e+06, 3.74677200e+06, 2.33427588e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.74645412e+06, 3.74623250e+06, 3.74669575e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.74645412e+06, 3.71940188e+06, 3.77287425e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.77706100e+06, 4.53703725e+06, 4.30616900e+06, 3.94519512e+06, 3.74643125e+06, 3.55551188e+06, 3.31580800e+06, 3.14849938e+06, 2.98772850e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.77706150e+06, 2.98772775e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.74652680e+07, 3.74591970e+07, 3.74652700e+07, 3.74652680e+07, 3.73264140e+07, 3.73203400e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75078662e+06, 3.74463588e+06, 5.33532188e+06, 3.74179100e+06, 3.74608250e+06, 2.33385912e+06, ],
  }),
  ("nof_tree_events",                 1678893),
  ("nof_db_events",                   3859942),
  ("fsize_local",                     7879689807), # 7.88GB, avg file size 3.94GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 175779),
  ("nof_db_events",                   369992),
  ("fsize_local",                     904014367), # 904.01MB, avg file size 904.01MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 176512),
  ("nof_db_events",                   392996),
  ("fsize_local",                     847981265), # 847.98MB, avg file size 847.98MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 163332),
  ("nof_db_events",                   375989),
  ("fsize_local",                     766827190), # 766.83MB, avg file size 766.83MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 180528),
  ("nof_db_events",                   399994),
  ("fsize_local",                     872210599), # 872.21MB, avg file size 872.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 174700),
  ("nof_db_events",                   399992),
  ("fsize_local",                     819881539), # 819.88MB, avg file size 819.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 167484),
  ("nof_db_events",                   384992),
  ("fsize_local",                     784862216), # 784.86MB, avg file size 784.86MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 173406),
  ("nof_db_events",                   399997),
  ("fsize_local",                     811796110), # 811.80MB, avg file size 811.80MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 197452),
  ("nof_db_events",                   399991),
  ("fsize_local",                     1020687438), # 1.02GB, avg file size 1.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 174201),
  ("nof_db_events",                   399986),
  ("fsize_local",                     816789229), # 816.79MB, avg file size 816.79MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 173182),
  ("nof_db_events",                   395994),
  ("fsize_local",                     815438466), # 815.44MB, avg file size 815.44MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 172924),
  ("nof_db_events",                   399993),
  ("fsize_local",                     809727748), # 809.73MB, avg file size 809.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    38),
  ("nof_events",                      {
    'Count'                                                                          : [ 399995, ],
    'CountWeighted'                                                                  : [ 3.76452031e+05, 3.76409000e+05, 3.76504000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.35350688e+05, 4.27786875e+05, 4.22483750e+05, 3.84984438e+05, 3.76452031e+05, 3.69622875e+05, 3.41435375e+05, 3.32648562e+05, 3.25150906e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.50942844e+05, 3.17427094e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.76489656e+05, 3.76553812e+05, 5.32995188e+05, 3.76405156e+05, 3.75921500e+05, 2.35506062e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.56186133e+04, 2.56147207e+04, 3.63070391e+04, 2.56117461e+04, 2.56266953e+04, 1.60245605e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.67376344e+05, 3.67314594e+05, 3.67446312e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.67376344e+05, 3.65109000e+05, 3.69571000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.24694344e+05, 4.17409250e+05, 4.12317125e+05, 3.75608844e+05, 3.67376344e+05, 3.60780750e+05, 3.33151750e+05, 3.24656312e+05, 3.17405750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.39929219e+05, 3.09859188e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.67444188e+05, 3.67375625e+05, 5.20025156e+05, 3.67278812e+05, 3.66961375e+05, 2.29930250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.49970254e+04, 2.49845938e+04, 3.54143516e+04, 2.49843398e+04, 2.50084688e+04, 1.56409512e+04, ],
  }),
  ("nof_tree_events",                 169688),
  ("nof_db_events",                   399995),
  ("fsize_local",                     762109625), # 762.11MB, avg file size 762.11MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    22),
  ("nof_events",                      {
    'Count'                                                                          : [ 399997, ],
    'CountWeighted'                                                                  : [ 3.58664562e+05, 3.58694969e+05, 3.58736625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.08532531e+05, 4.01965062e+05, 3.97629875e+05, 3.66975438e+05, 3.58660812e+05, 3.52198469e+05, 3.29315375e+05, 3.20315781e+05, 3.12769844e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.26078375e+05, 3.03235562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.58745594e+05, 3.58714531e+05, 5.08267312e+05, 3.58657438e+05, 3.58134469e+05, 2.23910938e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.19841426e+04, 1.19900488e+04, 1.69669688e+04, 1.19844717e+04, 1.19608652e+04, 7.49689648e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.49603875e+05, 3.49602938e+05, 3.49669844e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.49603875e+05, 3.47365500e+05, 3.51781688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.98048875e+05, 3.91743438e+05, 3.87601312e+05, 3.57606562e+05, 3.49597906e+05, 3.43364781e+05, 3.20937062e+05, 3.12245156e+05, 3.04957062e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.15173750e+05, 2.95649812e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.49712562e+05, 3.49545188e+05, 4.95339125e+05, 3.49534562e+05, 3.49208812e+05, 2.18341438e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.16773926e+04, 1.16789355e+04, 1.65288516e+04, 1.16743750e+04, 1.16569570e+04, 7.30632324e+03, ],
  }),
  ("nof_tree_events",                 176649),
  ("nof_db_events",                   399997),
  ("fsize_local",                     812464065), # 812.46MB, avg file size 812.46MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    38),
  ("nof_events",                      {
    'Count'                                                                          : [ 390697, ],
    'CountWeighted'                                                                  : [ 3.37054062e+05, 3.37106875e+05, 3.36998000e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 3.84407469e+05, 3.79149406e+05, 3.75816000e+05, 3.43880500e+05, 3.37047188e+05, 3.31703438e+05, 3.07742500e+05, 3.00217375e+05, 2.93880406e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.04933250e+05, 2.81345625e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.37108375e+05, 3.36894875e+05, 4.79287875e+05, 3.36975844e+05, 3.37462500e+05, 2.09568719e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 5.13176123e+03, 5.12825879e+03, 7.30025195e+03, 5.12955176e+03, 5.14287402e+03, 3.19185767e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.28434812e+05, 3.28474625e+05, 3.28399000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.28434812e+05, 3.26310000e+05, 3.30497875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 3.74403875e+05, 3.69380000e+05, 3.66219250e+05, 3.34996500e+05, 3.28427125e+05, 3.23300750e+05, 2.99830938e+05, 2.92581875e+05, 2.86477250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 3.94433875e+05, 2.74242500e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.28543000e+05, 3.28238906e+05, 4.66890938e+05, 3.28290344e+05, 3.28875438e+05, 2.04317562e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 5.00058740e+03, 4.99575977e+03, 7.11058545e+03, 4.99666846e+03, 5.01133691e+03, 3.11135181e+03, ],
  }),
  ("nof_tree_events",                 169018),
  ("nof_db_events",                   390697),
  ("fsize_local",                     786228433), # 786.23MB, avg file size 786.23MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    24),
  ("nof_events",                      {
    'Count'                                                                          : [ 395591, ],
    'CountWeighted'                                                                  : [ 3.89418438e+05, 3.89419125e+05, 3.89478219e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.66548969e+05, 4.57673688e+05, 4.50840375e+05, 3.97226250e+05, 3.89406594e+05, 3.82784281e+05, 3.42052438e+05, 3.35138969e+05, 3.28888531e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.80703844e+05, 3.22267438e+05, ],
    'CountWeightedPSWeight'                                                          : [ 3.89342625e+05, 3.89360219e+05, 5.50977000e+05, 3.89531906e+05, 3.89032750e+05, 2.43976734e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.17307168e+04, 3.17359844e+04, 4.49310312e+04, 3.17464883e+04, 3.17277637e+04, 1.98820684e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.80892125e+05, 3.80871125e+05, 3.80964688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 3.80892125e+05, 3.78712125e+05, 3.82985781e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.56127219e+05, 4.47568500e+05, 4.40985438e+05, 3.88431625e+05, 3.80881188e+05, 3.74489375e+05, 3.34529906e+05, 3.27852156e+05, 3.21807844e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.70001375e+05, 3.15316500e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.80879625e+05, 3.80751062e+05, 5.38840500e+05, 3.80931188e+05, 3.80687219e+05, 2.38754312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.10366426e+04, 3.10300273e+04, 4.39339688e+04, 3.10415938e+04, 3.10417051e+04, 1.94541191e+04, ],
  }),
  ("nof_tree_events",                 147618),
  ("nof_db_events",                   395591),
  ("fsize_local",                     627375496), # 627.38MB, avg file size 627.38MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_2v2t"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 79531),
  ("nof_db_events",                   379997),
  ("fsize_local",                     381778850), # 381.78MB, avg file size 381.78MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       2),
  ("nof_db_files",                    91),
  ("nof_events",                      {
    'Count'                                                                          : [ 3860978, ],
    'CountWeighted'                                                                  : [ 3.86059050e+06, 3.86074212e+06, 3.86075112e+06, ],
    'CountWeightedLHEWeightScale'                                                    : [ 4.92384962e+06, 4.67519675e+06, 4.43632288e+06, 4.06653138e+06, 3.86054688e+06, 3.66306988e+06, 3.41786925e+06, 3.24455988e+06, 3.07818350e+06, ],
    'CountWeightedLHEEnvelope'                                                       : [ 4.92385075e+06, 3.07818262e+06, ],
    'CountWeightedPSWeight'                                                          : [ 3.86075060e+07, 3.85973460e+07, 3.86075240e+07, 3.86075020e+07, 3.83782670e+07, 3.83680650e+07, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 3.86094425e+06, 3.86148062e+06, 5.62454575e+06, 3.86101338e+06, 3.85239862e+06, 2.29320406e+06, ],
    'CountWeightedFull'                                                              : [ 3.85947425e+06, 3.85962212e+06, 3.85962812e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 4.92242262e+06, 4.67384388e+06, 4.43503850e+06, 4.06535362e+06, 3.85943062e+06, 3.66200950e+06, 3.41687888e+06, 3.24362100e+06, 3.07729238e+06, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 4.92242375e+06, 3.07729138e+06, ],
    'CountWeightedFullPSWeight'                                                      : [ 3.85963470e+07, 3.85861720e+07, 3.85963470e+07, 3.85963470e+07, 3.83671570e+07, 3.83569800e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUP'                                        : [ 3.85985362e+06, 3.86036750e+06, 5.62290875e+06, 3.85987425e+06, 3.85127662e+06, 2.29254600e+06, ],
    'CountWeightedL1PrefireNom'                                                      : [ 3.75448012e+06, 3.75442775e+06, 3.75471550e+06, ],
    'CountWeightedL1Prefire'                                                         : [ 3.75448012e+06, 3.72862250e+06, 3.77957038e+06, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 4.78735750e+06, 4.54677300e+06, 4.31540825e+06, 3.95367975e+06, 3.75444412e+06, 3.56311738e+06, 3.32292638e+06, 3.15524312e+06, 2.99410962e+06, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 4.78735850e+06, 2.99410850e+06, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 3.75457300e+07, 3.75358710e+07, 3.75457440e+07, 3.75457280e+07, 3.73245680e+07, 3.73146860e+07, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 3.75909312e+06, 3.75395212e+06, 5.46843750e+06, 3.74927700e+06, 3.74849212e+06, 2.23152575e+06, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 3.75340488e+06, 3.75335112e+06, 3.75363725e+06, ],
    'CountWeightedFullL1Prefire'                                                     : [ 3.75340488e+06, 3.72755775e+06, 3.77848600e+06, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 4.78598500e+06, 4.54547050e+06, 4.31417175e+06, 3.95254662e+06, 3.75336888e+06, 3.56209738e+06, 3.32197325e+06, 3.15433912e+06, 2.99325188e+06, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 4.78598612e+06, 2.99325075e+06, ],
    'CountWeightedFullPSWeightL1PrefireNom'                                          : [ 3.75349870e+07, 3.75251210e+07, 3.75349870e+07, 3.75349870e+07, 3.73138780e+07, 3.73040080e+07, ],
    'CountWeightedFullPSWeightOriginalXWGTUPL1PrefireNom'                            : [ 3.75804162e+06, 3.75288225e+06, 5.46686350e+06, 3.74818162e+06, 3.74741250e+06, 2.23089088e+06, ],
  }),
  ("nof_tree_events",                 813648),
  ("nof_db_events",                   3860978),
  ("fsize_local",                     3843802202), # 3.84GB, avg file size 1.92GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_1_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 77530),
  ("nof_db_events",                   399999),
  ("fsize_local",                     393876869), # 393.88MB, avg file size 393.88MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_2_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 80990),
  ("nof_db_events",                   382999),
  ("fsize_local",                     391962268), # 391.96MB, avg file size 391.96MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_3_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 82272),
  ("nof_db_events",                   391999),
  ("fsize_local",                     387695137), # 387.70MB, avg file size 387.70MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 84009),
  ("nof_db_events",                   399999),
  ("fsize_local",                     408210888), # 408.21MB, avg file size 408.21MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_5_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 83993),
  ("nof_db_events",                   396000),
  ("fsize_local",                     398265181), # 398.27MB, avg file size 398.27MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_6_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 83968),
  ("nof_db_events",                   400000),
  ("fsize_local",                     397352249), # 397.35MB, avg file size 397.35MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 83749),
  ("nof_db_events",                   395995),
  ("fsize_local",                     395366304), # 395.37MB, avg file size 395.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_8_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 81931),
  ("nof_db_events",                   399997),
  ("fsize_local",                     423435369), # 423.44MB, avg file size 423.44MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_9_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 82848),
  ("nof_db_events",                   391996),
  ("fsize_local",                     392109803), # 392.11MB, avg file size 392.11MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_10_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 84984),
  ("nof_db_events",                   399997),
  ("fsize_local",                     403372628), # 403.37MB, avg file size 403.37MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_11_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_tree_events",                 82824),
  ("nof_db_events",                   394000),
  ("fsize_local",                     390890220), # 390.89MB, avg file size 390.89MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    74),
  ("nof_events",                      {
    'Count'                                                                          : [ 999992, ],
    'CountWeighted'                                                                  : [ 9.41119438e+05, 9.41134438e+05, 9.41174625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.08848938e+06, 1.06943400e+06, 1.05603788e+06, 9.62564438e+05, 9.41119438e+05, 9.23902188e+05, 8.53666375e+05, 8.31616312e+05, 8.12804438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.12731475e+06, 7.93624125e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.41173562e+05, 9.40441188e+05, 1.36379288e+06, 9.41065375e+05, 9.40416688e+05, 5.61377875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 6.40770859e+04, 6.40472578e+04, 9.29430547e+04, 6.40752812e+04, 6.40893945e+04, 3.82120312e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.20508500e+05, 9.20495812e+05, 9.20556875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.20508500e+05, 9.15248625e+05, 9.25547625e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.06430075e+06, 1.04588625e+06, 1.03297350e+06, 9.41276875e+05, 9.20508500e+05, 9.03837562e+05, 8.34847750e+05, 8.13468188e+05, 7.95223375e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.10231338e+06, 7.76451312e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.20656562e+05, 9.19604250e+05, 1.33380150e+06, 9.20329875e+05, 9.20236375e+05, 5.49321375e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 6.26621445e+04, 6.26096523e+04, 9.08732656e+04, 6.26446602e+04, 6.26964883e+04, 3.73802383e+04, ],
  }),
  ("nof_tree_events",                 209514),
  ("nof_db_events",                   999992),
  ("fsize_local",                     952285936), # 952.29MB, avg file size 952.29MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH0_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    53),
  ("nof_events",                      {
    'Count'                                                                          : [ 963693, ],
    'CountWeighted'                                                                  : [ 8.63450000e+05, 8.63367250e+05, 8.63424688e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82849688e+05, 9.67203875e+05, 9.56899750e+05, 8.83250250e+05, 8.63397750e+05, 8.47807312e+05, 7.92834938e+05, 7.71213625e+05, 7.53099562e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.02526600e+06, 7.29957938e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.63095875e+05, 8.63102750e+05, 1.25243762e+06, 8.63811188e+05, 8.62238188e+05, 5.13989219e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 2.87884590e+04, 2.87794473e+04, 4.18346484e+04, 2.88078594e+04, 2.88346855e+04, 1.71462520e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.43204562e+05, 8.43106938e+05, 8.43250000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.43204562e+05, 8.38113375e+05, 8.48108000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.59494375e+05, 9.44426438e+05, 9.34551562e+05, 8.62364688e+05, 8.43161125e+05, 8.28120062e+05, 7.74151188e+05, 7.53219625e+05, 7.35683938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.00095150e+06, 7.13069250e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.42988812e+05, 8.42615812e+05, 1.22296388e+06, 8.43443625e+05, 8.42471312e+05, 5.02190250e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 2.81098555e+04, 2.80885762e+04, 4.08381992e+04, 2.81204941e+04, 2.81652051e+04, 1.67481895e+04, ],
  }),
  ("nof_tree_events",                 204933),
  ("nof_db_events",                   963693),
  ("fsize_local",                     954726226), # 954.73MB, avg file size 954.73MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH1_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    63),
  ("nof_events",                      {
    'Count'                                                                          : [ 999996, ],
    'CountWeighted'                                                                  : [ 8.61863875e+05, 8.61982250e+05, 8.61825750e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 9.82960625e+05, 9.69436750e+05, 9.60813750e+05, 8.79381000e+05, 8.61859562e+05, 8.48131438e+05, 7.87038500e+05, 7.67738500e+05, 7.51484438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.03520162e+06, 7.19598875e+05, ],
    'CountWeightedPSWeight'                                                          : [ 8.61759375e+05, 8.61961875e+05, 1.25138638e+06, 8.62003375e+05, 8.59598250e+05, 5.11507625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 1.31346562e+04, 1.31395605e+04, 1.90839609e+04, 1.31356465e+04, 1.31120996e+04, 7.79717871e+03, ],
    'CountWeightedL1PrefireNom'                                                      : [ 8.41422500e+05, 8.41514812e+05, 8.41412688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 8.41422500e+05, 8.36309688e+05, 8.46344562e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 9.59272125e+05, 9.46309812e+05, 9.38103688e+05, 8.58303938e+05, 8.41411438e+05, 8.28213500e+05, 7.68245375e+05, 7.49613062e+05, 7.33916812e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.01033712e+06, 7.02750000e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 8.41472875e+05, 8.41378250e+05, 1.22141400e+06, 8.41381938e+05, 8.39388125e+05, 4.99638625e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 1.28201777e+04, 1.28202646e+04, 1.86203164e+04, 1.28161885e+04, 1.27997500e+04, 7.61287695e+03, ],
  }),
  ("nof_tree_events",                 205076),
  ("nof_db_events",                   999996),
  ("fsize_local",                     957069095), # 957.07MB, avg file size 957.07MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH2p45_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    42),
  ("nof_events",                      {
    'Count'                                                                          : [ 999995, ],
    'CountWeighted'                                                                  : [ 9.84275625e+05, 9.84303500e+05, 9.84293125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.17920950e+06, 1.15681600e+06, 1.13958125e+06, 1.00401244e+06, 9.84227000e+05, 9.67553438e+05, 8.64512625e+05, 8.47067938e+05, 8.31297000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.21512150e+06, 8.14476562e+05, ],
    'CountWeightedPSWeight'                                                          : [ 9.84252188e+05, 9.84553125e+05, 1.42333675e+06, 9.84319625e+05, 9.80600438e+05, 5.87952312e+05, ],
    'CountWeightedPSWeightOriginalXWGTUP'                                            : [ 8.02275312e+04, 8.02429219e+04, 1.16176320e+05, 8.02310312e+04, 8.00910312e+04, 4.79213555e+04, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.64972875e+05, 9.64956125e+05, 9.65030250e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.64972875e+05, 9.59940938e+05, 9.69747750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.15552275e+06, 1.13387075e+06, 1.11722825e+06, 9.84076375e+05, 9.64932625e+05, 9.48785625e+05, 8.47497375e+05, 8.30600688e+05, 8.15308875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.19081250e+06, 7.98778875e+05, ],
    'CountWeightedPSWeightL1PrefireNom'                                              : [ 9.65100312e+05, 9.65005438e+05, 1.39513625e+06, 9.64824375e+05, 9.61752500e+05, 5.76758875e+05, ],
    'CountWeightedPSWeightOriginalXWGTUPL1PrefireNom'                                : [ 7.86593750e+04, 7.86422344e+04, 1.13863523e+05, 7.86346484e+04, 7.85438438e+04, 4.70043633e+04, ],
  }),
  ("nof_tree_events",                 194371),
  ("nof_db_events",                   999995),
  ("fsize_local",                     830255492), # 830.26MB, avg file size 830.26MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_cHHH5_hh_4v"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99858500e+05, 9.99790750e+05, 9.99819375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27992925e+06, 1.20810925e+06, 1.14071462e+06, 1.05955038e+06, 9.99858500e+05, 9.43905625e+05, 8.92298312e+05, 8.41875750e+05, 7.94625125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27992962e+06, 7.94624562e+05, ],
    'CountWeightedFull'                                                              : [ 9.99858500e+05, 9.99790750e+05, 9.99819375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27992925e+06, 1.20810925e+06, 1.14071462e+06, 1.05955038e+06, 9.99858500e+05, 9.43905625e+05, 8.92298312e+05, 8.41875750e+05, 7.94625125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27992962e+06, 7.94624562e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.67702750e+05, 9.67630875e+05, 9.67693375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.67702750e+05, 9.60102875e+05, 9.75182438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23842562e+06, 1.16930088e+06, 1.10437200e+06, 1.02514894e+06, 9.67702750e+05, 9.13794750e+05, 8.63294625e+05, 8.14768125e+05, 7.69248688e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23842588e+06, 7.69248375e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.67702750e+05, 9.67630875e+05, 9.67693375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.67702750e+05, 9.60102875e+05, 9.75182438e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23842562e+06, 1.16930088e+06, 1.10437200e+06, 1.02514894e+06, 9.67702750e+05, 9.13794750e+05, 8.63294625e+05, 8.14768125e+05, 7.69248688e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23842588e+06, 7.69248375e+05, ],
  }),
  ("nof_tree_events",                 695627),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3167848260), # 3.17GB, avg file size 3.17GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99929125e+05, 9.99898500e+05, 9.99967625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27521762e+06, 1.21088262e+06, 1.14908462e+06, 1.05314688e+06, 9.99929125e+05, 9.48763500e+05, 8.85127812e+05, 8.40294438e+05, 7.97246188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27521762e+06, 7.97246250e+05, ],
    'CountWeightedFull'                                                              : [ 9.99929125e+05, 9.99898500e+05, 9.99967625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27521762e+06, 1.21088262e+06, 1.14908462e+06, 1.05314688e+06, 9.99929125e+05, 9.48763500e+05, 8.85127812e+05, 8.40294438e+05, 7.97246188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27521762e+06, 7.97246250e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69038188e+05, 9.68973000e+05, 9.69102125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69038188e+05, 9.61677438e+05, 9.76255125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23552700e+06, 1.17351850e+06, 1.11388600e+06, 1.02034012e+06, 9.69038188e+05, 9.19676250e+05, 8.57537125e+05, 8.14323375e+05, 7.72786500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23552700e+06, 7.72786500e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69038188e+05, 9.68973000e+05, 9.69102125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69038188e+05, 9.61677438e+05, 9.76255125e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23552700e+06, 1.17351850e+06, 1.11388600e+06, 1.02034012e+06, 9.69038188e+05, 9.19676250e+05, 8.57537125e+05, 8.14323375e+05, 7.72786500e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23552700e+06, 7.72786500e+05, ],
  }),
  ("nof_tree_events",                 679974),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3024362153), # 3.02GB, avg file size 3.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_1_hh_4t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99904188e+05, 9.99904875e+05, 9.99878562e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27509575e+06, 1.21106025e+06, 1.14948300e+06, 1.05296638e+06, 9.99904188e+05, 9.48985125e+05, 8.84936062e+05, 8.40276688e+05, 7.97369062e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27509575e+06, 7.97369125e+05, ],
    'CountWeightedFull'                                                              : [ 9.99904188e+05, 9.99904875e+05, 9.99878562e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27509575e+06, 1.21106025e+06, 1.14948300e+06, 1.05296638e+06, 9.99904188e+05, 9.48985125e+05, 8.84936062e+05, 8.40276688e+05, 7.97369062e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27509575e+06, 7.97369125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68915750e+05, 9.68858625e+05, 9.68962625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68915750e+05, 9.61534938e+05, 9.76162000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23525012e+06, 1.17354975e+06, 1.11414950e+06, 1.02003206e+06, 9.68915750e+05, 9.19787125e+05, 8.57234062e+05, 8.14201375e+05, 7.72814750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23525012e+06, 7.72814750e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.68915750e+05, 9.68858625e+05, 9.68962625e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.68915750e+05, 9.61534938e+05, 9.76162000e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23525012e+06, 1.17354975e+06, 1.11414950e+06, 1.02003206e+06, 9.68915750e+05, 9.19787125e+05, 8.57234062e+05, 8.14201375e+05, 7.72814750e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23525012e+06, 7.72814750e+05, ],
  }),
  ("nof_tree_events",                 678505),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3021824332), # 3.02GB, avg file size 3.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99894000e+05, 9.99973125e+05, 9.99896500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27525825e+06, 1.21086588e+06, 1.14897162e+06, 1.05320850e+06, 9.99894000e+05, 9.48695938e+05, 8.85194875e+05, 8.40311875e+05, 7.97213000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27525825e+06, 7.97213000e+05, ],
    'CountWeightedFull'                                                              : [ 9.99894000e+05, 9.99973125e+05, 9.99896500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27525825e+06, 1.21086588e+06, 1.14897162e+06, 1.05320850e+06, 9.99894000e+05, 9.48695938e+05, 8.85194875e+05, 8.40311875e+05, 7.97213000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27525825e+06, 7.97213000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68778750e+05, 9.68800875e+05, 9.68812688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68778750e+05, 9.61380500e+05, 9.76048438e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23527212e+06, 1.17321525e+06, 1.11351012e+06, 1.02015862e+06, 9.68778750e+05, 9.19393500e+05, 8.57398375e+05, 8.14143125e+05, 7.72569750e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23527212e+06, 7.72569750e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.68778750e+05, 9.68800875e+05, 9.68812688e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.68778750e+05, 9.61380500e+05, 9.76048438e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23527212e+06, 1.17321525e+06, 1.11351012e+06, 1.02015862e+06, 9.68778750e+05, 9.19393500e+05, 8.57398375e+05, 8.14143125e+05, 7.72569750e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23527212e+06, 7.72569750e+05, ],
  }),
  ("nof_tree_events",                 680045),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3024619469), # 3.02GB, avg file size 3.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99911000e+05, 9.99870750e+05, 9.99921250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27489450e+06, 1.21113812e+06, 1.14975288e+06, 1.05269762e+06, 9.99911000e+05, 9.49152938e+05, 8.84625875e+05, 8.40204938e+05, 7.97462125e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27489450e+06, 7.97462125e+05, ],
    'CountWeightedFull'                                                              : [ 9.99911000e+05, 9.99870750e+05, 9.99921250e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27489450e+06, 1.21113812e+06, 1.14975288e+06, 1.05269762e+06, 9.99911000e+05, 9.49152938e+05, 8.84625875e+05, 8.40204938e+05, 7.97462125e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27489450e+06, 7.97462125e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.68832375e+05, 9.68773875e+05, 9.68872688e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.68832375e+05, 9.61432625e+05, 9.76093688e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23494838e+06, 1.17350850e+06, 1.11429412e+06, 1.01968625e+06, 9.68832375e+05, 9.19856750e+05, 8.56866438e+05, 8.14059062e+05, 7.72829875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23494838e+06, 7.72829875e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.68832375e+05, 9.68773875e+05, 9.68872688e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.68832375e+05, 9.61432625e+05, 9.76093688e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23494838e+06, 1.17350850e+06, 1.11429412e+06, 1.01968625e+06, 9.68832375e+05, 9.19856750e+05, 8.56866438e+05, 8.14059062e+05, 7.72829875e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23494838e+06, 7.72829875e+05, ],
  }),
  ("nof_tree_events",                 678121),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     3010879564), # 3.01GB, avg file size 3.01GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999997, ],
    'CountWeighted'                                                                  : [ 9.99903375e+05, 9.99921750e+05, 9.99833125e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27995988e+06, 1.20820175e+06, 1.14085312e+06, 1.05955112e+06, 9.99903375e+05, 9.43999250e+05, 8.92282688e+05, 8.41897500e+05, 7.94685875e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27996000e+06, 7.94685875e+05, ],
    'CountWeightedFull'                                                              : [ 9.99903375e+05, 9.99921750e+05, 9.99833125e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27995988e+06, 1.20820175e+06, 1.14085312e+06, 1.05955112e+06, 9.99903375e+05, 9.43999250e+05, 8.92282688e+05, 8.41897500e+05, 7.94685875e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27996000e+06, 7.94685875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.69409500e+05, 9.69355812e+05, 9.69427188e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.69409500e+05, 9.62122750e+05, 9.76536000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24057650e+06, 1.17140788e+06, 1.10641912e+06, 1.02689738e+06, 9.69409500e+05, 9.15462375e+05, 8.64744875e+05, 8.16183000e+05, 7.70629875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24057650e+06, 7.70629750e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.69409500e+05, 9.69355812e+05, 9.69427188e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.69409500e+05, 9.62122750e+05, 9.76536000e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.24057650e+06, 1.17140788e+06, 1.10641912e+06, 1.02689738e+06, 9.69409500e+05, 9.15462375e+05, 8.64744875e+05, 8.16183000e+05, 7.70629875e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24057650e+06, 7.70629750e+05, ],
  }),
  ("nof_tree_events",                 443163),
  ("nof_db_events",                   999997),
  ("fsize_local",                     2118730404), # 2.12GB, avg file size 2.12GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_2v2t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999998, ],
    'CountWeighted'                                                                  : [ 9.99833125e+05, 9.99856375e+05, 9.99926625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27524250e+06, 1.21084712e+06, 1.14896338e+06, 1.05319638e+06, 9.99833125e+05, 9.48682562e+05, 8.85187125e+05, 8.40304562e+05, 7.97196625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27524275e+06, 7.97196500e+05, ],
    'CountWeightedFull'                                                              : [ 9.99833125e+05, 9.99856375e+05, 9.99926625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27524250e+06, 1.21084712e+06, 1.14896338e+06, 1.05319638e+06, 9.99833125e+05, 9.48682562e+05, 8.85187125e+05, 8.40304562e+05, 7.97196625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27524275e+06, 7.97196500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70534188e+05, 9.70509062e+05, 9.70646375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70534188e+05, 9.63484250e+05, 9.77429875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23755888e+06, 1.17538175e+06, 1.11557338e+06, 1.02204269e+06, 9.70534188e+05, 9.21083500e+05, 8.58980375e+05, 8.15643312e+05, 7.73984625e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23755912e+06, 7.73984500e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70534188e+05, 9.70509062e+05, 9.70646375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70534188e+05, 9.63484250e+05, 9.77429875e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23755888e+06, 1.17538175e+06, 1.11557338e+06, 1.02204269e+06, 9.70534188e+05, 9.21083500e+05, 8.58980375e+05, 8.15643312e+05, 7.73984625e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23755912e+06, 7.73984500e+05, ],
  }),
  ("nof_tree_events",                 434227),
  ("nof_db_events",                   999998),
  ("fsize_local",                     2034881079), # 2.03GB, avg file size 2.03GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_1_hh_2v2t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999998, ],
    'CountWeighted'                                                                  : [ 9.99908750e+05, 9.99909375e+05, 9.99877625e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27508050e+06, 1.21102388e+06, 1.14941625e+06, 1.05296025e+06, 9.99908750e+05, 9.48933750e+05, 8.84931000e+05, 8.40252312e+05, 7.97328188e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27508250e+06, 7.97326500e+05, ],
    'CountWeightedFull'                                                              : [ 9.99908750e+05, 9.99909375e+05, 9.99877625e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27508050e+06, 1.21102388e+06, 1.14941625e+06, 1.05296025e+06, 9.99908750e+05, 9.48933750e+05, 8.84931000e+05, 8.40252312e+05, 7.97328188e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27508250e+06, 7.97326500e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70611500e+05, 9.70561438e+05, 9.70646375e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70611500e+05, 9.63562938e+05, 9.77497750e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23741450e+06, 1.17557875e+06, 1.11604525e+06, 1.02181794e+06, 9.70611500e+05, 9.21351000e+05, 8.58732250e+05, 8.15604000e+05, 7.74128500e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23741600e+06, 7.74127188e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70611500e+05, 9.70561438e+05, 9.70646375e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70611500e+05, 9.63562938e+05, 9.77497750e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23741450e+06, 1.17557875e+06, 1.11604525e+06, 1.02181794e+06, 9.70611500e+05, 9.21351000e+05, 8.58732250e+05, 8.15604000e+05, 7.74128500e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23741600e+06, 7.74127188e+05, ],
  }),
  ("nof_tree_events",                 432953),
  ("nof_db_events",                   999998),
  ("fsize_local",                     2028847917), # 2.03GB, avg file size 2.03GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_2v2t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999998, ],
    'CountWeighted'                                                                  : [ 9.99917750e+05, 9.99905750e+05, 9.99876250e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27527000e+06, 1.21089500e+06, 1.14902000e+06, 1.05320250e+06, 9.99917750e+05, 9.48730188e+05, 8.85189062e+05, 8.40309750e+05, 7.97235000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27527038e+06, 7.97234625e+05, ],
    'CountWeightedFull'                                                              : [ 9.99917750e+05, 9.99905750e+05, 9.99876250e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27527000e+06, 1.21089500e+06, 1.14902000e+06, 1.05320250e+06, 9.99917750e+05, 9.48730188e+05, 8.85189062e+05, 8.40309750e+05, 7.97235000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27527038e+06, 7.97234625e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70575938e+05, 9.70544625e+05, 9.70567000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70575938e+05, 9.63513750e+05, 9.77472000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23755625e+06, 1.17539500e+06, 1.11559300e+06, 1.02202512e+06, 9.70575938e+05, 9.21103062e+05, 8.58962875e+05, 8.15634312e+05, 7.73999250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23755638e+06, 7.73999000e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70575938e+05, 9.70544625e+05, 9.70567000e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70575938e+05, 9.63513750e+05, 9.77472000e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23755625e+06, 1.17539500e+06, 1.11559300e+06, 1.02202512e+06, 9.70575938e+05, 9.21103062e+05, 8.58962875e+05, 8.15634312e+05, 7.73999250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23755638e+06, 7.73999000e+05, ],
  }),
  ("nof_tree_events",                 433414),
  ("nof_db_events",                   999998),
  ("fsize_local",                     2030500283), # 2.03GB, avg file size 2.03GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_2v2t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999996, ],
    'CountWeighted'                                                                  : [ 9.99900625e+05, 9.99897062e+05, 9.99880500e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27485775e+06, 1.21112388e+06, 1.14973662e+06, 1.05265988e+06, 9.99900625e+05, 9.49132500e+05, 8.84588875e+05, 8.40172250e+05, 7.97439438e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27485925e+06, 7.97439312e+05, ],
    'CountWeightedFull'                                                              : [ 9.99900625e+05, 9.99897062e+05, 9.99880500e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27485775e+06, 1.21112388e+06, 1.14973662e+06, 1.05265988e+06, 9.99900625e+05, 9.49132500e+05, 8.84588875e+05, 8.40172250e+05, 7.97439438e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27485925e+06, 7.97439312e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70736375e+05, 9.70711312e+05, 9.70749438e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70736375e+05, 9.63716188e+05, 9.77590875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23737662e+06, 1.17582788e+06, 1.11648712e+06, 1.02168206e+06, 9.70736375e+05, 9.21656938e+05, 8.58534750e+05, 8.15643250e+05, 7.74335250e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23737800e+06, 7.74335250e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70736375e+05, 9.70711312e+05, 9.70749438e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70736375e+05, 9.63716188e+05, 9.77590875e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23737662e+06, 1.17582788e+06, 1.11648712e+06, 1.02168206e+06, 9.70736375e+05, 9.21656938e+05, 8.58534750e+05, 8.15643250e+05, 7.74335250e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23737800e+06, 7.74335250e+05, ],
  }),
  ("nof_tree_events",                 432752),
  ("nof_db_events",                   999996),
  ("fsize_local",                     2022885505), # 2.02GB, avg file size 2.02GB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_2v2t_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99842000e+05, 9.99956750e+05, 9.99991375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27994575e+06, 1.20818600e+06, 1.14083288e+06, 1.05954450e+06, 9.99842000e+05, 9.43985562e+05, 8.92278062e+05, 8.41896625e+05, 7.94677312e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27994750e+06, 7.94675812e+05, ],
    'CountWeightedFull'                                                              : [ 9.99842000e+05, 9.99956750e+05, 9.99991375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27994575e+06, 1.20818600e+06, 1.14083288e+06, 1.05954450e+06, 9.99842000e+05, 9.43985562e+05, 8.92278062e+05, 8.41896625e+05, 7.94677312e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27994750e+06, 7.94675812e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.70992188e+05, 9.71017188e+05, 9.71135625e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.70992188e+05, 9.64030375e+05, 9.77775000e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.24265138e+06, 1.17336450e+06, 1.10826150e+06, 1.02861300e+06, 9.70992188e+05, 9.16984500e+05, 8.66187375e+05, 8.17545250e+05, 7.71911312e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.24265312e+06, 7.71909812e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.70992188e+05, 9.71017188e+05, 9.71135625e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.70992188e+05, 9.64030375e+05, 9.77775000e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.24265138e+06, 1.17336450e+06, 1.10826150e+06, 1.02861300e+06, 9.70992188e+05, 9.16984500e+05, 8.66187375e+05, 8.17545250e+05, 7.71911312e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.24265312e+06, 7.71909812e+05, ],
  }),
  ("nof_tree_events",                 207323),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     993995213), # 994.00MB, avg file size 994.00MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_sm_hh_4v_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 1000000, ],
    'CountWeighted'                                                                  : [ 9.99951500e+05, 9.99827625e+05, 9.99867375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27525625e+06, 1.21090688e+06, 1.14904962e+06, 1.05319062e+06, 9.99951500e+05, 9.48743188e+05, 8.85172750e+05, 8.40310875e+05, 7.97241000e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27525550e+06, 7.97241000e+05, ],
    'CountWeightedFull'                                                              : [ 9.99951500e+05, 9.99827625e+05, 9.99867375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27525625e+06, 1.21090688e+06, 1.14904962e+06, 1.05319062e+06, 9.99951500e+05, 9.48743188e+05, 8.85172750e+05, 8.40310875e+05, 7.97241000e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27525550e+06, 7.97241000e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72474688e+05, 9.72355625e+05, 9.72474125e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72474688e+05, 9.65780000e+05, 9.78971875e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23995650e+06, 1.17768800e+06, 1.11777612e+06, 1.02400506e+06, 9.72474688e+05, 9.22892438e+05, 8.60619125e+05, 8.17211062e+05, 7.75495188e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23995562e+06, 7.75495188e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72474688e+05, 9.72355625e+05, 9.72474125e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72474688e+05, 9.65780000e+05, 9.78971875e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23995650e+06, 1.17768800e+06, 1.11777612e+06, 1.02400506e+06, 9.72474688e+05, 9.22892438e+05, 8.60619125e+05, 8.17211062e+05, 7.75495188e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23995562e+06, 7.75495188e+05, ],
  }),
  ("nof_tree_events",                 210936),
  ("nof_db_events",                   1000000),
  ("fsize_local",                     995316072), # 995.32MB, avg file size 995.32MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_1_hh_4v_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999997, ],
    'CountWeighted'                                                                  : [ 9.99934500e+05, 9.99934938e+05, 1.00000156e+06, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27508100e+06, 1.21105738e+06, 1.14945938e+06, 1.05296050e+06, 9.99934500e+05, 9.48961562e+05, 8.84929500e+05, 8.40264500e+05, 7.97350625e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27508300e+06, 7.97348875e+05, ],
    'CountWeightedFull'                                                              : [ 9.99934500e+05, 9.99934938e+05, 1.00000156e+06, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27508100e+06, 1.21105738e+06, 1.14945938e+06, 1.05296050e+06, 9.99934500e+05, 9.48961562e+05, 8.84929500e+05, 8.40264500e+05, 7.97350625e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27508300e+06, 7.97348875e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72424125e+05, 9.72393875e+05, 9.72512000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72424125e+05, 9.65715062e+05, 9.78926125e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23970650e+06, 1.17778012e+06, 1.11814162e+06, 1.02370438e+06, 9.72424125e+05, 9.23070375e+05, 8.60312938e+05, 8.17115312e+05, 7.75568938e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23970850e+06, 7.75567188e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72424125e+05, 9.72393875e+05, 9.72512000e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72424125e+05, 9.65715062e+05, 9.78926125e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23970650e+06, 1.17778012e+06, 1.11814162e+06, 1.02370438e+06, 9.72424125e+05, 9.23070375e+05, 8.60312938e+05, 8.17115312e+05, 7.75568938e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23970850e+06, 7.75567188e+05, ],
  }),
  ("nof_tree_events",                 208515),
  ("nof_db_events",                   999997),
  ("fsize_local",                     982428439), # 982.43MB, avg file size 982.43MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_4_hh_4v_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999999, ],
    'CountWeighted'                                                                  : [ 9.99992500e+05, 1.00000862e+06, 9.99998375e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27531950e+06, 1.21090075e+06, 1.14898850e+06, 1.05325725e+06, 9.99992500e+05, 9.48708875e+05, 8.85238750e+05, 8.40335125e+05, 7.97223688e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27531950e+06, 7.97223688e+05, ],
    'CountWeightedFull'                                                              : [ 9.99992500e+05, 1.00000862e+06, 9.99998375e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27531950e+06, 1.21090075e+06, 1.14898850e+06, 1.05325725e+06, 9.99992500e+05, 9.48708875e+05, 8.85238750e+05, 8.40335125e+05, 7.97223688e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27531950e+06, 7.97223688e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72095438e+05, 9.72083062e+05, 9.72128000e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72095438e+05, 9.65311375e+05, 9.78684312e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23948725e+06, 1.17718212e+06, 1.11724725e+06, 1.02363012e+06, 9.72095438e+05, 9.22471562e+05, 8.60314625e+05, 8.16888000e+05, 7.75153875e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23948725e+06, 7.75153875e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72095438e+05, 9.72083062e+05, 9.72128000e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72095438e+05, 9.65311375e+05, 9.78684312e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23948725e+06, 1.17718212e+06, 1.11724725e+06, 1.02363012e+06, 9.72095438e+05, 9.22471562e+05, 8.60314625e+05, 8.16888000e+05, 7.75153875e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23948725e+06, 7.75153875e+05, ],
  }),
  ("nof_tree_events",                 209930),
  ("nof_db_events",                   999999),
  ("fsize_local",                     990528633), # 990.53MB, avg file size 990.53MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_7_hh_4v_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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
  ("nof_files",                       1),
  ("nof_db_files",                    4000),
  ("nof_events",                      {
    'Count'                                                                          : [ 999999, ],
    'CountWeighted'                                                                  : [ 1.00006275e+06, 9.99901812e+05, 9.99933875e+05, ],
    'CountWeightedLHEWeightScale'                                                    : [ 1.27483650e+06, 1.21114775e+06, 1.14978238e+06, 1.05263250e+06, 1.00006275e+06, 9.49160875e+05, 8.84557688e+05, 8.40168625e+05, 7.97457812e+05, ],
    'CountWeightedLHEEnvelope'                                                       : [ 1.27483800e+06, 7.97457750e+05, ],
    'CountWeightedFull'                                                              : [ 1.00006275e+06, 9.99901812e+05, 9.99933875e+05, ],
    'CountWeightedFullLHEWeightScale'                                                : [ 1.27483650e+06, 1.21114775e+06, 1.14978238e+06, 1.05263250e+06, 1.00006275e+06, 9.49160875e+05, 8.84557688e+05, 8.40168625e+05, 7.97457812e+05, ],
    'CountWeightedFullLHEEnvelope'                                                   : [ 1.27483800e+06, 7.97457750e+05, ],
    'CountWeightedL1PrefireNom'                                                      : [ 9.72521875e+05, 9.72395500e+05, 9.72476875e+05, ],
    'CountWeightedL1Prefire'                                                         : [ 9.72521875e+05, 9.65817562e+05, 9.79026938e+05, ],
    'CountWeightedLHEWeightScaleL1PrefireNom'                                        : [ 1.23951938e+06, 1.17789238e+06, 1.11846100e+06, 1.02343744e+06, 9.72521875e+05, 9.23275875e+05, 8.60000500e+05, 8.17053812e+05, 7.75688125e+05, ],
    'CountWeightedLHEEnvelopeL1PrefireNom'                                           : [ 1.23952075e+06, 7.75688125e+05, ],
    'CountWeightedFullL1PrefireNom'                                                  : [ 9.72521875e+05, 9.72395500e+05, 9.72476875e+05, ],
    'CountWeightedFullL1Prefire'                                                     : [ 9.72521875e+05, 9.65817562e+05, 9.79026938e+05, ],
    'CountWeightedFullLHEWeightScaleL1PrefireNom'                                    : [ 1.23951938e+06, 1.17789238e+06, 1.11846100e+06, 1.02343744e+06, 9.72521875e+05, 9.23275875e+05, 8.60000500e+05, 8.17053812e+05, 7.75688125e+05, ],
    'CountWeightedFullLHEEnvelopeL1PrefireNom'                                       : [ 1.23952075e+06, 7.75688125e+05, ],
  }),
  ("nof_tree_events",                 209805),
  ("nof_db_events",                   999999),
  ("fsize_local",                     987811045), # 987.81MB, avg file size 987.81MB
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
        ("path",      "/hdfs/local/karl/ttHNtupleProduction/2017/2020Oct31_wPresel_nom_hh/ntuples/signal_ggf_nonresonant_node_12_hh_4v_private"),
        ("selection", "*"),
        ("blacklist", []),
      ]),
    ]
  ),
  ("missing_completely",           [
    # not computed
  ]),
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

