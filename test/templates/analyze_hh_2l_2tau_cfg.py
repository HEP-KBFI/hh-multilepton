import FWCore.ParameterSet.Config as cms
import os

from tthAnalysis.HiggsToTauTau.configs.recommendedMEtFilters_cfi import *
from tthAnalysis.HiggsToTauTau.configs.EvtYieldHistManager_cfi import *
from tthAnalysis.HiggsToTauTau.analysisSettings import *

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(100000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('')
)

process.analyze_hh_2l_2tau = cms.PSet(
    treeName = cms.string('Events'),

    Process = cms.string(''),
    histogramDir = cms.string(''),
    era = cms.string(''),

    triggers_1e = cms.vstring(),
    use_triggers_1e = cms.bool(True),
    triggers_2e = cms.vstring(),
    use_triggers_2e = cms.bool(True),
    triggers_1mu = cms.vstring(),
    use_triggers_1mu = cms.bool(True),
    triggers_2mu = cms.vstring(),
    use_triggers_2mu = cms.bool(True),
    triggers_1e1mu = cms.vstring(),
    use_triggers_1e1mu = cms.bool(True),

    apply_offline_e_trigger_cuts_1e = cms.bool(True),
    apply_offline_e_trigger_cuts_2e = cms.bool(True),
    apply_offline_e_trigger_cuts_1mu = cms.bool(True),
    apply_offline_e_trigger_cuts_2mu = cms.bool(True),
    apply_offline_e_trigger_cuts_1e1mu = cms.bool(True),

    electronSelection = cms.string(''),
    muonSelection = cms.string(''),
    apply_leptonGenMatching = cms.bool(True),
    leptonChargeSelection = cms.string(''),

    hadTauChargeSelection = cms.string(''),
    hadTauGenMatch = cms.string('all'),
    hadTauSelection = cms.string(''),
    apply_hadTauGenMatching = cms.bool(False),

    chargeSumSelection = cms.string(''),

    applyFakeRateWeights = cms.string(""),
    leptonFakeRateWeight = cms.PSet(
        inputFileName = cms.string(""),
        histogramName_e = cms.string(""),
        histogramName_mu = cms.string(""),
        era = cms.string(""),
        applyNonClosureCorrection = cms.bool(False),
    ),
    hadTauFakeRateWeight = cms.PSet(
        inputFileName = cms.string(""),
        lead = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True)
        ),
        sublead = cms.PSet(
            absEtaBins = cms.vdouble(-1., 1.479, 9.9),
            graphName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/jetToTauFakeRate_mc_hadTaus_pt"),
            applyGraph = cms.bool(True),
            fitFunctionName = cms.string("jetToTauFakeRate/$hadTauSelection/$etaBin/fitFunction_data_div_mc_hadTaus_pt"),
            applyFitFunction = cms.bool(True)
        )
    ),

    isMC = cms.bool(True),
    central_or_shift = cms.string(''),
    lumiScale = cms.VPSet(),
    apply_genWeight = cms.bool(True),
    apply_DYMCReweighting = cms.bool(False),
    apply_DYMCNormScaleFactors = cms.bool(False),
    apply_topPtReweighting = cms.string(''),
    apply_l1PreFireWeight = cms.bool(True),
    apply_hlt_filter = cms.bool(False),
    apply_met_filters = cms.bool(True),
    invert_ZbosonMassVeto = cms.bool(True),
    cfgMEtFilter = cms.PSet(),
    triggerWhiteList = cms.PSet(),
    apply_hadTauFakeRateSF = cms.bool(False),

    fillGenEvtHistograms = cms.bool(False),
    cfgEvtYieldHistManager = cms.PSet(),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),
    branchName_memOutput = cms.string(''),

    branchName_muonGenMatch     = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch   = cms.string('TauGenMatch'),
    branchName_jetGenMatch      = cms.string('JetGenMatch'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genJets = cms.string('GenJet'),

    redoGenMatching = cms.bool(False),
    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(True),

    selEventsFileName_input = cms.string(''),
    selEventsFileName_output = cms.string(''),

    useNonNominal = cms.bool(False),
    isDEBUG = cms.bool(False),
    isDEBUG_NN = cms.bool(True),
    hasLHE = cms.bool(True),
    hasPS = cms.bool(False),
    apply_LHE_nom = cms.bool(False),
    useObjectMultiplicity = cms.bool(False),

    selectBDT = cms.bool(False), ## Set it to true for making BDT training Ntuples

    gen_mHH = cms.vdouble(250,260,270,280,300,350,400,450,500,550,600,650,700,750,800,850,900,1000), ## Set the signal mass range used in the BDT .pkl/.xml/.pb files
    mvaInfo_res = cms.PSet( ## [Default hyper-para.s used]
        BDT_xml_FileName_even_spin2 = cms.string('hhAnalysis/multilepton/data/odd_half_model_def_hyper_para_spin2.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no.
        BDT_xml_FileName_odd_spin2 = cms.string('hhAnalysis/multilepton/data/even_half_model_def_hyper_para_spin2.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
        fitFunctionFileName_spin2 = cms.string('hhAnalysis/multilepton/data/TProfile_signal_fit_func_spin2.root'),  ## File contaning the fitted TF1s
        inputVars_spin2 = cms.vstring('tau1_eta', 'dr_leps', 'met', 'dr_lep_tau_min_OS', 'diHiggsMass', 'mTauTauVis', 'Smin_lltautau', 'dr_taus', 'Smin_llMEt', 'gen_mHH'),
        BDT_xml_FileName_even_spin0 = cms.string('hhAnalysis/multilepton/data/odd_half_model_def_hyper_para_spin0.xml'),
        BDT_xml_FileName_odd_spin0 = cms.string('hhAnalysis/multilepton/data/even_half_model_def_hyper_para_spin0.xml'),
        fitFunctionFileName_spin0 = cms.string('hhAnalysis/multilepton/data/TProfile_signal_fit_func_spin0.root'),
        inputVars_spin0 = cms.vstring('tau1_eta', 'dr_leps', 'ptTauTauVis', 'met', 'dr_lep_tau_min_OS', 'diHiggsMass', 'mTauTauVis', 'Smin_lltautau', 'dr_lep1_tau1_tau2_min', 'Smin_llMEt', 'gen_mHH'),
    ),
    nonRes_BMs = cms.vdouble(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12),
    mvaInfo_nonres = cms.PSet( ## [Laurits_Reso_Twaek hyp_para.s used]
        BDT_xml_FileName_even_nonres = cms.string('hhAnalysis/multilepton/data/odd_half_model_def_hyper_para_nonres.xml'), ## "BDT .xml -> Odd train:Even test" to be used for even evt no. 
        BDT_xml_FileName_odd_nonres = cms.string('hhAnalysis/multilepton/data/even_half_model_def_hyper_para_nonres.xml'), ## "BDT .xml -> Even train:Odd test" to be used for odd evt no.
        inputVars_nonres = cms.vstring('lep1_pt', 'tau1_pt', 'dr_lep1_tau2', 'dr_leps', 'dr_taus', 'met', 'HT', 'Smin_llMEt', 'mTauTau', 'diHiggsMass'), ## No Need to add BM indices they will be added for the  non-reso case on the fly
    ),

    evtWeight = cms.PSet(
        apply = cms.bool(False),
        histogramFile = cms.string(''),
        histogramName = cms.string(''),
        branchNameXaxis = cms.string(''),
        branchNameYaxis = cms.string(''),
        branchTypeXaxis = cms.string(''),
        branchTypeYaxis = cms.string(''),
    ),
    tHweights = cms.VPSet(),
    hhWeight_cfg = cms.PSet(
        denominator_file = cms.string(''),
        klScan_file = cms.string(''),
        ktScan_file = cms.string(''),
        c2Scan_file = cms.string(''),
        cgScan_file = cms.string(''),
        c2gScan_file = cms.string(''),
        coefFile = cms.string('HHStatAnalysis/AnalyticalModels/data/coefficientsByBin_extended_3M_costHHSim_19-4.txt'),
        histtitle = cms.string(''),
        isDEBUG = cms.bool(False),
        do_scan = cms.bool(True),
        do_ktscan = cms.bool(False),
        apply_rwgt = cms.bool(False),
    ),
)
