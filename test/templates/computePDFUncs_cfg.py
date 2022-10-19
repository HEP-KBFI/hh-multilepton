import FWCore.ParameterSet.Config as cms

import os

process = cms.PSet()

process.fwliteInput = cms.PSet(
    fileNames = cms.vstring("/local/ram/hhAnalysis/2017/2018Oct4/histograms/hh_2l_2tau/histograms_harvested_stage1_hh_2l_2tau_signal_ggf_spin0_400_hh_2v2t_disabled_disabled_Tight_OS.root")
)

process.fwliteOutput = cms.PSet(
    fileName = cms.string('signal_ggf_spin0_400_hh_2v2t_disabled_disabled_Tight_OS_PDFUncs.root')
)

process.computePDFUncs = cms.PSet(

    categories = cms.vstring(['hh_2l_2tau_sumOS_Tight', 
                              # 'hh_2lSS_2tau_sumOS_Tight', 'hh_2lOS_2tau_sumOS_Tight', 'hh_2e_2tau_sumOS_Tight', 
                              # 'hh_1e1mu_2tau_sumOS_Tight', 'hh_2mu_2tau_sumOS_Tight', 'hh_2eSS_2tau_sumOS_Tight', 'hh_2eOS_2tau_sumOS_Tight', 
                              # 'hh_1e1muSS_2tau_sumOS_Tight', 'hh_1e1muOS_2tau_sumOS_Tight', 'hh_2muSS_2tau_sumOS_Tight', 'hh_2muOS_2tau_sumOS_Tight'
                              ]),
    
    num_dir = cms.string("sel/lheInfo"),
    den_dir = cms.string("unbiased/lheInfo"),
    process_name = cms.string("signal_ggf_spin0_400_hh_wwtt"),    
    sysShifts = cms.vstring()
)


