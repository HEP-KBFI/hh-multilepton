#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2l_2tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

#include <string>
#include <sstream>
#include <map>


EvtHistManager_hh_2l_2tau::EvtHistManager_hh_2l_2tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numHadTaus"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["mTauTauVis"] = { "central" };
  central_or_shiftOptions_["leptonPairCharge"] = { "central" };
  central_or_shiftOptions_["hadTauPairCharge"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "central" };
  central_or_shiftOptions_["dihiggsMass"] = { "*" };
  central_or_shiftOptions_["dihiggsMass_diLepChgZero"] = { "*" };
  central_or_shiftOptions_["dihiggsMass_diLepChgNonZero"] = { "*" };
  central_or_shiftOptions_["BDTOutput_nonres_SM"] = { "*" }; 
  central_or_shiftOptions_["BDTOutput_nonres_SM_diLepChgZero"] = { "*" }; 
  central_or_shiftOptions_["BDTOutput_nonres_SM_diLepChgNonZero"] = { "*" }; 
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  central_or_shiftOptions_["EventNumber"] = { "*" };
}

const TH1 *
EvtHistManager_hh_2l_2tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_2l_2tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",      5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",          5, -0.5,  +4.5);
  histogram_numHadTaus_       = book1D(dir, "numHadTaus",       "numHadTaus",        5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",          20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",    20, -0.5, +19.5);
  histogram_numBJets_loose_   = book1D(dir, "numBJets_loose",   "numBJets_loose",   10, -0.5,  +9.5);
  histogram_numBJets_medium_  = book1D(dir, "numBJets_medium",  "numBJets_medium",  10, -0.5,  +9.5);
  histogram_mTauTauVis_       = book1D(dir, "mTauTauVis",       "mTauTauVis",       40,  0.,  200.);
  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",  5, -2.5,  +2.5);
  histogram_hadTauPairCharge_ = book1D(dir, "hadTauPairCharge", "hadTauPairCharge",  5, -2.5,  +2.5);
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",  150,  0., 1500.);
  histogram_dihiggsMass_      = book1D(dir, "dihiggsMass",      "dihiggsMass",     150,  0., 1500.);
  histogram_dihiggsMass_diLepChgZero_ = book1D(dir, "dihiggsMass_diLepChgZero",      "dihiggsMass_diLepChgZero",     150,  0., 1500.);
  histogram_dihiggsMass_diLepChgNonZero_ = book1D(dir, "dihiggsMass_diLepChgNonZero",      "dihiggsMass_diLepChgNonZero",     150,  0., 1500.);
  histogram_BDTOutput_nonres_SM_ = book1D(dir, "BDTOutput_nonres_SM", "BDTOutput_nonres_SM",  100,  0., 1.);
  histogram_BDTOutput_nonres_SM_diLepChgZero_ = book1D(dir, "BDTOutput_nonres_SM_diLepChgZero", "BDTOutput_nonres_SM_diLepChgZero",  100,  0., 1.);
  histogram_BDTOutput_nonres_SM_diLepChgNonZero_ = book1D(dir, "BDTOutput_nonres_SM_diLepChgNonZero", "BDTOutput_nonres_SM_diLepChgNonZero",  100,  0., 1.);
  histogram_HT_               = book1D(dir, "HT",               "HT",              150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",           150,  0., 1500.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",      1, -0.5,  +0.5);
  histogram_EventNumber_      = book1D(dir, "EventNumber",      "EventNumber",       2,  0.,    2.);
  histogram_EventNumber_->GetXaxis()->SetBinLabel(1,"Odd");
  histogram_EventNumber_->GetXaxis()->SetBinLabel(2,"Even");
}

void
EvtHistManager_hh_2l_2tau::fillHistograms(double BDTOutput_nonres_SM,
					  int selLepton_lead_charge,
					  int selLepton_sublead_charge,
					  int numElectrons,
					  int numMuons,
					  int numHadTaus,
					  int numJets,
					  int numJetsPtGt40,
					  int numBJets_loose,
					  int numBJets_medium,
					  double mTauTauVis,
					  double leptonPairCharge,
					  double hadTauPairCharge,
					  double dihiggsVisMass,
					  double dihiggsMass,
					  double HT,
					  double STMET,
					  unsigned int evt_number,
					  double evtWeight)
{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_,     numElectrons,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,       numHadTaus,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,    numJetsPtGt40,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,   numBJets_loose,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_,  numBJets_medium,  evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mTauTauVis_,       mTauTauVis,       evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_leptonPairCharge_, leptonPairCharge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_hadTauPairCharge_, hadTauPairCharge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dihiggsVisMass_,   dihiggsVisMass,   evtWeight, evtWeightErr);
  if ( dihiggsMass > 0. ) {
    fillWithOverFlow(histogram_dihiggsMass_,    dihiggsMass,      evtWeight, evtWeightErr);
    if(std::abs(selLepton_lead_charge + selLepton_sublead_charge) == 0){ // Di-Lep Mass = 0 cond.
      fillWithOverFlow(histogram_dihiggsMass_diLepChgZero_,    dihiggsMass,      evtWeight, evtWeightErr);
    }else{
      fillWithOverFlow(histogram_dihiggsMass_diLepChgNonZero_,    dihiggsMass,      evtWeight, evtWeightErr);
    }
  }

  fillWithOverFlow(histogram_BDTOutput_nonres_SM_, BDTOutput_nonres_SM, evtWeight, evtWeightErr);
  if(std::abs(selLepton_lead_charge + selLepton_sublead_charge) == 0){ // Di-Lep Mass = 0 cond. 
    fillWithOverFlow(histogram_BDTOutput_nonres_SM_diLepChgZero_, BDTOutput_nonres_SM, evtWeight, evtWeightErr);
  }else{
    fillWithOverFlow(histogram_BDTOutput_nonres_SM_diLepChgNonZero_, BDTOutput_nonres_SM, evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);

  if(evt_number % 2){// Odd Event Number case
    fillWithOverFlow(histogram_EventNumber_,    0.,               evtWeight, evtWeightErr);                                  
  }else{ // Even Event Number case
    fillWithOverFlow(histogram_EventNumber_,    1.,               evtWeight, evtWeightErr);     
  }      

  
}
