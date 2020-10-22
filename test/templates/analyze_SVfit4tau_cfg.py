import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring(''),
    maxEvents = cms.int32(-1),
    outputEvery = cms.uint32(1000)
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('analyze_SVfit4tau.root')
)

process.analyze_SVfit4tau = cms.PSet(
    treeName = cms.string('Events'),

    process = cms.string('HH'),

    histogramDir = cms.string('SVfit4tau'),

    era = cms.string('2017'),

    mode = cms.string("rec"), # CV: 'rec', 'gen', or 'gen_smeared'

    leptonSelection = cms.string(),
    hadTauSelection = cms.string(),

    SVfit4tau = cms.PSet(
        logM_wMassConstraint_MarkovChain = cms.vdouble(0.),
        logM_woMassConstraint_MarkovChain = cms.vdouble(0.),
        logM_wMassConstraint_VAMP = cms.vdouble(0.)
    ),

    use_HIP_mitigation_mediumMuonId = cms.bool(False),

    isMC = cms.bool(True),
    central_or_shift = cms.string('central'),
    lumiScale = cms.VPSet(),
    ref_genWeight = cms.double(0.),
    apply_genWeight = cms.bool(True),

    fillGenEvtHistograms = cms.bool(False),

    branchName_electrons = cms.string('Electron'),
    branchName_muons = cms.string('Muon'),
    branchName_hadTaus = cms.string('Tau'),
    branchName_jets = cms.string('Jet'),
    branchName_met = cms.string('MET'),
    branchName_memOutput = cms.string(''),

    branchName_muonGenMatch = cms.string('MuonGenMatch'),
    branchName_electronGenMatch = cms.string('ElectronGenMatch'),
    branchName_hadTauGenMatch = cms.string('TauGenMatch'),
    branchName_jetGenMatch = cms.string('JetGenMatch'),

    branchName_genLeptons = cms.string('GenLep'),
    branchName_genHadTaus = cms.string('GenVisTau'),
    branchName_genPhotons = cms.string('GenPhoton'),
    branchName_genJets = cms.string('GenJet'),

    redoGenMatching = cms.bool(False),
    genMatchingByIndex = cms.bool(True),
    jetCleaningByIndex = cms.bool(True),

    branchName_genTaus = cms.string('GenTau'),
    branchName_genHiggsBosons = cms.string('GenHiggs'),

    genHadTauSmearing = cms.PSet(
        inputFileName = cms.string("hhAnalysis/multilepton/data/hadTauSmearingCDF_toyMC.root"),
        graphName = cms.string("rCDF")
    ),
    genMEtSmearing = cms.PSet(
        sigmaX = cms.double(10.),
        sigmaY = cms.double(10.)
    ),

    selEventsFileName_input = cms.string(''),

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
)
