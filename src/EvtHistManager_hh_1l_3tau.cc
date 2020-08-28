#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_1l_3tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h"  // z_mass

EvtHistManager_hh_1l_3tau::EvtHistManager_hh_1l_3tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numHadTaus"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "central" };
  central_or_shiftOptions_["dihiggsMass"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  central_or_shiftOptions_["antiE_tau1_OS_matched"] = { "central" };
  central_or_shiftOptions_["antiE_tau1_OS_unmatched"] = { "central" };
  central_or_shiftOptions_["antiE_tau2_OS_matched"] = { "central" };
  central_or_shiftOptions_["antiE_tau2_OS_unmatched"] = { "central" };
  central_or_shiftOptions_["antiE_tau3_OS_matched"] = { "central" };
  central_or_shiftOptions_["antiE_tau3_OS_unmatched"] = { "central" };
  central_or_shiftOptions_["m_OS_etau_closestToZ"] = { "central" };
  central_or_shiftOptions_["eta_OS_etau1"] = { "central" };
  central_or_shiftOptions_["eta_OS_etau2"] = { "central" };
  central_or_shiftOptions_["eta_OS_etau3"] = { "central" };
}

const TH1 *
EvtHistManager_hh_1l_3tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_1l_3tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_    = book1D(dir, "numElectrons",    "numElectrons",      5, -0.5,  +4.5);
  histogram_numMuons_        = book1D(dir, "numMuons",        "numMuons",          5, -0.5,  +4.5);
  histogram_numHadTaus_      = book1D(dir, "numHadTaus",      "numHadTaus",        5, -0.5,  +4.5);
  histogram_numJets_         = book1D(dir, "numJets",         "numJets",          20, -0.5, +19.5);
  histogram_numJetsPtGt40_   = book1D(dir, "numJetsPtGt40",   "numJetsPtGt40",    20, -0.5, +19.5);
  histogram_numBJets_loose_  = book1D(dir, "numBJets_loose",  "numBJets_loose",   10, -0.5,  +9.5);
  histogram_numBJets_medium_ = book1D(dir, "numBJets_medium", "numBJets_medium",  10, -0.5,  +9.5);

  histogram_dihiggsVisMass_  = book1D(dir, "dihiggsVisMass",  "dihiggsVisMass",  150,  0., 1500.);
  histogram_dihiggsMass_     = book1D(dir, "dihiggsMass",     "dihiggsMass",     150,  0., 1500.);

  histogram_HT_              = book1D(dir, "HT",              "HT",              150,  0., 1500.);
  histogram_STMET_           = book1D(dir, "STMET",           "STMET",           150,  0., 1500.);

  // CV: plots specific to 1e+3tau category
  histogram_1e3tau_tau1_OS_eta_                      = book1D(dir, "1e3tau_tau1_OS_eta",                      "1e3tau_tau1_OS_eta",                     46, -2.3,  +2.3);
  histogram_1e3tau_tau1_OS_antiE_OS_matched_         = book1D(dir, "1e3tau_tau1_OS_antiE_matched",            "1e3tau_tau1_OS_antiE_matched",           11, -2.5,   8.5);
  histogram_1e3tau_tau1_OS_antiE_OS_unmatched_       = book1D(dir, "1e3tau_tau1_OS_antiE_unmatched",          "1e3tau_tau1_OS_antiE_unmatched",         11, -2.5,   8.5);
  histogram_1e3tau_tau1_OS_eta_                      = book1D(dir, "1e3tau_tau2_OS_eta",                      "1e3tau_tau2_OS_eta",                     46, -2.3,  +2.3);
  histogram_1e3tau_tau2_OS_antiE_OS_matched_         = book1D(dir, "1e3tau_tau2_OS_antiE_matched",            "1e3tau_tau2_OS_antiE_matched",           11, -2.5,   8.5);
  histogram_1e3tau_tau2_OS_antiE_OS_unmatched_       = book1D(dir, "1e3tau_tau2_OS_antiE_unmatched",          "1e3tau_tau2_OS_antiE_unmatched",         11, -2.5,   8.5); 
  histogram_1e3tau_tau3_OS_eta_                      = book1D(dir, "1e3tau_tau3_OS_eta",                      "1e3tau_tau3_OS_eta",                     46, -2.3,  +2.3);
  histogram_1e3tau_tau3_OS_antiE_OS_matched_         = book1D(dir, "1e3tau_tau3_OS_antiE_matched",            "1e3tau_tau3_OS_antiE_matched",           11, -2.5,   8.5);
  histogram_1e3tau_tau3_OS_antiE_OS_unmatched_       = book1D(dir, "1e3tau_tau3_OS_antiE_unmatched",          "1e3tau_tau3_OS_antiE_unmatched",         11, -2.5,   8.5);
  histogram_1e3tau_mass_etau_OS_closestToZ_          = book1D(dir, "1e3tau_mass_etau_OS_closestToZ",          "1e3tau_mass_etau_OS_closestToZ",        200,  0.,  200.);
  histogram_1e3tau_numTightLeptons_                  = book1D(dir, "1e3tau_numTightLeptons",                  "1e3tau_numTightLeptons",                  5, -0.5,   4.5);
  histogram_1e3tau_numFakeableTaus_passingElecVeto_  = book1D(dir, "1e3tau_numFakeableTaus_passingElecVeto",  "1e3tau_numFakeableTaus_passingElecVeto",  5, -0.5,   4.5);
  histogram_1e3tau_numTightTaus_                     = book1D(dir, "1e3tau_numTightTaus",                     "1e3tau_numTightTaus",                     5, -0.5,   4.5);
  histogram_1e3tau_numTightTaus_passingElecVeto_     = book1D(dir, "1e3tau_numTightTaus_passingElecVeto",     "1e3tau_numTightTaus_passingElecVeto",     5, -0.5,   4.5);
  histogram_1e3tau_numTightLeptons_and_Taus_         = book1D(dir, "1e3tau_numTightLeptons_and_Taus",         "1e3tau_numTightLeptons_and_Taus",         5, -0.5,   4.5);
  histogram_1e3tau_evtWeight_                        = book1D(dir, "1e3tau_evtWeight",                        "1e3tau_evtWeight",                      200, -1.,   +1.);

  // CV: plots specific to 1mu+3tau category
  histogram_1mu3tau_numTightLeptons_                 = book1D(dir, "1mu3tau_numTightLeptons",                 "1mu3tau_numTightLeptons",                 5, -0.5,   4.5);
  histogram_1mu3tau_numFakeableTaus_passingElecVeto_ = book1D(dir, "1mu3tau_numFakeableTaus_passingElecVeto", "1mu3tau_numFakeableTaus_passingElecVeto", 5, -0.5,   4.5);
  histogram_1mu3tau_numTightTaus_                    = book1D(dir, "1mu3tau_numTightTaus",                    "1mu3tau_numTightTaus",                    5, -0.5,   4.5);
  histogram_1mu3tau_numTightTaus_passingElecVeto_    = book1D(dir, "1mu3tau_numTightTaus_passingElecVeto",    "1mu3tau_numTightTaus_passingElecVeto",    5, -0.5,   4.5);
  histogram_1mu3tau_numTightLeptons_and_Taus_        = book1D(dir, "1mu3tau_numTightLeptons_and_Taus",        "1mu3tau_numTightLeptons_and_Taus",        5, -0.5,   4.5);
  histogram_1mu3tau_evtWeight_                       = book1D(dir, "1mu3tau_evtWeight",                       "1mu3tau_evtWeight",                     200, -1.,   +1.);

  histogram_EventCounter_ = book1D(dir, "EventCounter", "EventCounter", 1, -0.5, +0.5);
}

namespace
{
  void fillHistograms_1e3tau_tau(TH1* histogram_tau_OS_eta, TH1* histogram_tau_OS_antiE_OS_matched, TH1* histogram_tau_OS_antiE_OS_unmatched,
                                 const RecoLepton* selLepton, const RecoHadTau* selHadTau, double evtWeight, double evtWeightErr)
  {
    if ( selHadTau->charge()*selLepton->charge() < 0. )
    {
      fillWithOverFlow(histogram_tau_OS_eta, selHadTau->eta(), evtWeight, evtWeightErr);
      TH1* histogram_tau_OS_antiE_OS = nullptr;
      if ( TMath::Abs(getHadTau_genPdgId(selHadTau)) == 11 )
      {
        histogram_tau_OS_antiE_OS = histogram_tau_OS_antiE_OS_matched;
      }
      else
      {
        histogram_tau_OS_antiE_OS = histogram_tau_OS_antiE_OS_unmatched;
      }
      fillWithOverFlow(histogram_tau_OS_antiE_OS, selHadTau->id_mva(TauID::DeepTau2017v2VSe), evtWeight, evtWeightErr);
    }
  }
}

void
EvtHistManager_hh_1l_3tau::fillHistograms(int numElectrons,
					  int numMuons,
					  int numHadTaus,
					  int numJets,
					  int numJetsPtGt40,
					  int numBJets_loose,
					  int numBJets_medium,
					  double dihiggsVisMass,
					  double dihiggsMass,
					  double HT,
					  double STMET,
                                          const RecoLepton* selLepton,
                                          const RecoHadTau* selHadTau_lead,
                                          const RecoHadTau* selHadTau_sublead,
                                          const RecoHadTau* selHadTau_third,
                                          int numTightLeptons,    
                                          int numFakeableHadTaus_passingElecVeto,
                                          int numTightHadTaus,
                                          int numTightHadTaus_passingElecVeto,
                                          bool isMC,
					  double evtWeight)
{
  const double evtWeightErr = 0.;

  fillWithOverFlow(histogram_numElectrons_,    numElectrons,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,        numMuons,        evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,      numHadTaus,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,         numJets,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,   numJetsPtGt40,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,  numBJets_loose,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_dihiggsVisMass_,  dihiggsVisMass,  evtWeight, evtWeightErr);
  if ( dihiggsMass > 0. ) {
    fillWithOverFlow(histogram_dihiggsMass_,   dihiggsMass,     evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_HT_,              HT,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,           STMET,           evtWeight, evtWeightErr);

  if ( selLepton->is_electron() )
  {
    fillHistograms_1e3tau_tau(
      histogram_1e3tau_tau1_OS_eta_, histogram_1e3tau_tau1_OS_antiE_OS_matched_, histogram_1e3tau_tau1_OS_antiE_OS_unmatched_,
      selLepton, selHadTau_lead, evtWeight, evtWeightErr);
    fillHistograms_1e3tau_tau(
      histogram_1e3tau_tau2_OS_eta_, histogram_1e3tau_tau2_OS_antiE_OS_matched_, histogram_1e3tau_tau2_OS_antiE_OS_unmatched_,
      selLepton, selHadTau_sublead, evtWeight, evtWeightErr);
    fillHistograms_1e3tau_tau(
      histogram_1e3tau_tau3_OS_eta_, histogram_1e3tau_tau3_OS_antiE_OS_matched_, histogram_1e3tau_tau3_OS_antiE_OS_unmatched_,
      selLepton, selHadTau_third, evtWeight, evtWeightErr);
    std::vector<const RecoHadTau*> selHadTaus = { selHadTau_lead, selHadTau_sublead, selHadTau_third };
    double mass_etau_OS_closestToZ = -1.;
    for ( const RecoHadTau* selHadTau : selHadTaus )
    {
      if ( selHadTau->charge()*selLepton->charge() < 0. )
      {
        double mass_etau = (selLepton->p4() + selHadTau->p4()).mass();
	if ( mass_etau_OS_closestToZ == -1. || TMath::Abs(mass_etau - z_mass) < TMath::Abs(mass_etau_OS_closestToZ - z_mass) )
        {
          mass_etau_OS_closestToZ = mass_etau;
        }
      }
    }
    fillWithOverFlow(histogram_1e3tau_mass_etau_OS_closestToZ_,          mass_etau_OS_closestToZ,              evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1e3tau_numTightLeptons_,                  numTightLeptons,                      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1e3tau_numFakeableTaus_passingElecVeto_,  numFakeableHadTaus_passingElecVeto,   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1e3tau_numTightTaus_,                     numTightHadTaus,                      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1e3tau_numTightTaus_passingElecVeto_,     numTightHadTaus_passingElecVeto,      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1e3tau_numTightLeptons_and_Taus_,         numTightLeptons + numTightHadTaus,    evtWeight, evtWeightErr);
    if ( !isMC ) 
    {
      fillWithOverFlow(histogram_1e3tau_evtWeight_,                      evtWeight,                            evtWeight, evtWeightErr);
    }
  }
  
  if ( selLepton->is_muon() ) 
  {
    fillWithOverFlow(histogram_1mu3tau_numTightLeptons_,                 numTightLeptons,                      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1mu3tau_numFakeableTaus_passingElecVeto_, numFakeableHadTaus_passingElecVeto,   evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1mu3tau_numTightTaus_,                    numTightHadTaus,                      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1mu3tau_numTightTaus_passingElecVeto_,    numTightHadTaus_passingElecVeto,      evtWeight, evtWeightErr);
    fillWithOverFlow(histogram_1mu3tau_numTightLeptons_and_Taus_,        numTightLeptons + numTightHadTaus,    evtWeight, evtWeightErr);
    if ( !isMC ) 
    {
      fillWithOverFlow(histogram_1mu3tau_evtWeight_,                     evtWeight,                            evtWeight, evtWeightErr);
    }
  }
  
  fillWithOverFlow(histogram_EventCounter_, 0., evtWeight, evtWeightErr);
}
