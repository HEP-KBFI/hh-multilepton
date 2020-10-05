import FWCore.ParameterSet.Config as cms

from hhAnalysis.multilepton.configs.makePlots_cfi import process

process.makePlots.distributions.extend([
    cms.PSet(
        histogramName = cms.string('sel/electrons/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/electrons/$PROCESS/eta'),
        xAxisTitle = cms.string('e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('leading e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading e_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadElectron/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading e_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muons/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('#mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/muons/$PROCESS/eta'),
        xAxisTitle = cms.string('#mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading #mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('leading #mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading #mu_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadMuon/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading #mu_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/jets/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/jets/$PROCESS/eta'),
        xAxisTitle = cms.string('jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadJet/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('leading jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/leadJet/$PROCESS/eta'),
        xAxisTitle = cms.string('leading jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadJet/$PROCESS/pt'),
        xMin = cms.double(20.),
        xMax = cms.double(200.),
        xAxisTitle = cms.string('subleading jet_{h} p_{T} [GeV]'),
        yAxisTitle = cms.string('dN/dp_{T} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/subleadJet/$PROCESS/eta'),
        xAxisTitle = cms.string('subleading jet_{h} #eta'),
        yAxisTitle = cms.string('dN/d#eta')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairMass'),
        xAxisTitle = cms.string('m_{ll} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{ll} [1/GeV]')
    ),
   cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/electronPairMass'),
        xAxisTitle = cms.string('m_{ee} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{ee} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/muonPairMass'),
        xAxisTitle = cms.string('m_{#mu#mu} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{#mu#mu} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/leptonPairCharge'),
        xAxisTitle = cms.string('lepton charge sum'),
        yAxisTitle = cms.string('N')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsVisMass'),
        xAxisTitle = cms.string('m_{HH} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dihiggsMass_wMet'),
        xAxisTitle = cms.string('m_{HH} with Met [GeV]'),
        yAxisTitle = cms.string('dN/dm_{HH} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/jetMass'),
        xAxisTitle = cms.string('m_{jjjj} [GeV]'),
        yAxisTitle = cms.string('dN/dm_{jjjj} [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/dR_ll'),
        xAxisTitle = cms.string('#DeltaR(2l)'),
        yAxisTitle = cms.string('dN]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT_met_lepLead'),
        xAxisTitle = cms.string('m_{T}(leading lepton + MET) [GeV]'),
        yAxisTitle = cms.string('dN/dm [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT_met_lepSublead'),
        xAxisTitle = cms.string('m_{T}(subleading lepton + MET) [GeV]'),
        yAxisTitle = cms.string('dN/dm [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT_met_lep_max'),
        xAxisTitle = cms.string('(m_{T}(l + MET))_{max} [GeV]'),
        yAxisTitle = cms.string('dN/dm [1/GeV]')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/mT_met_lep_min'),
        xAxisTitle = cms.string('(m_{T}(l + MET))_{min} [GeV]'),
        yAxisTitle = cms.string('dN/dm [1/GeV]')
    ),    
#    cms.PSet(
#        histogramName = cms.string('sel/evt/$PROCESS/BDTOutput_SUM'),
#        xAxisTitle = cms.string('BDT Output'),
#        yAxisTitle = cms.string('N')
#    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/BDTOutput_SUM_gen_mHH_400'),
        xAxisTitle = cms.string('BDT Output'),
        yAxisTitle = cms.string('N')
    ),
    cms.PSet(
        histogramName = cms.string('sel/evt/$PROCESS/BDTOutput_SUM_gen_mHH_700'),
        xAxisTitle = cms.string('BDT Output'),
        yAxisTitle = cms.string('N')
    ),
])
