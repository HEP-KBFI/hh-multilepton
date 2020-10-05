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
  central_or_shiftOptions_["dihiggsMass"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  central_or_shiftOptions_["EventNumber"] = { "*" };
  std::vector<double> gen_mHH = cfg.getParameter<std::vector<double>>("gen_mHH");
  std::vector<double> nonRes_BMs = cfg.getParameter<std::vector<double>>("nonRes_BMs");

  for(unsigned int i=0;i<gen_mHH.size();i++){ // Loop over signal masses (Resonant case)
    unsigned int mass_int = (int)gen_mHH[i]; // Conversion from double to unsigned int                                                                                                    
    std::string key = "";
    std::ostringstream temp;
    temp << mass_int;
    key = temp.str(); // Conversion from unsigned int to string                                                                                                                          
                                                                                   
    std::string key_final = "BDTOutput_" + key; // For the TMVAInterface
    std::string key_final_spin2 = key_final + "_hypo_spin2";
    std::string key_final_spin0 = key_final + "_hypo_spin0";
    labels_spin2_.push_back(key_final_spin2);
    labels_spin0_.push_back(key_final_spin0);
  }

  for(unsigned int i=0;i<nonRes_BMs.size();i++){ // Loop over BM indices (Non Resonant case)
    std::string key_final = "";
    if(nonRes_BMs[i] == 0){ // For SM
      key_final = "BDTOutput_SM"; // For the TMVAInterface
    }else{
      unsigned int bm_index_int = (int)nonRes_BMs[i]; // Conversion from double to unsigned int
      std::string key = "";
      std::ostringstream temp;
      temp << bm_index_int;
      key = temp.str(); // Conversion from unsigned int to string
      key_final = "BDTOutput_BM" + key; // For the TMVAInterface
    }
    std::string key_final_nonres = key_final;
    labels_nonres_.push_back(key_final_nonres);
  }

  for(unsigned int i=0;i < labels_spin2_.size();i++){
    central_or_shiftOptions_[labels_spin2_[i]] = { "*" };
  }

  for(unsigned int i=0;i < labels_spin0_.size();i++){
    central_or_shiftOptions_[labels_spin0_[i]] = { "*" };
  }

  for(unsigned int i=0;i < labels_nonres_.size();i++){
    central_or_shiftOptions_[labels_nonres_[i]] = { "*" };
  }

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
  histogram_HT_               = book1D(dir, "HT",               "HT",              150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",           150,  0., 1500.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",      1, -0.5,  +0.5);
  histogram_EventNumber_      = book1D(dir, "EventNumber",     "EventNumber",      2, 0., 2.0);
  histogram_EventNumber_->GetXaxis()->SetBinLabel(1,"Odd");
  histogram_EventNumber_->GetXaxis()->SetBinLabel(2,"Even");

  for(unsigned int i=0;i < labels_spin2_.size();i++){ 
    TH1* histogram_BDT_output_spin2 = book1D(dir, labels_spin2_[i], labels_spin2_[i], 200, -1., 1.); 
    histogram_Map_BDTOutput_SUM_spin2_.insert(std::make_pair(labels_spin2_[i], histogram_BDT_output_spin2)); 
  }

  for(unsigned int i=0;i < labels_spin0_.size();i++){ 
    TH1* histogram_BDT_output_spin0 = book1D(dir, labels_spin0_[i], labels_spin0_[i], 200, -1., 1.); 
    histogram_Map_BDTOutput_SUM_spin0_.insert(std::make_pair(labels_spin0_[i], histogram_BDT_output_spin0)); 
  }

  for(unsigned int i=0;i < labels_nonres_.size();i++){ 
    TH1* histogram_BDT_output_nonres = book1D(dir, labels_nonres_[i], labels_nonres_[i], 200, -1., 1.); 
    histogram_Map_BDTOutput_SUM_nonres_.insert(std::make_pair(labels_nonres_[i], histogram_BDT_output_nonres)); 
  }

}

void
EvtHistManager_hh_2l_2tau::fillHistograms(int numElectrons,
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
					  std::map<std::string, double> & BDTOutput_SUM_Map_spin2,
					  std::map<std::string, double> & BDTOutput_SUM_Map_spin0,
					  std::map<std::string, double> & BDTOutput_SUM_Map_nonres,
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
  }
  fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,  0., evtWeight, evtWeightErr);

  if(evt_number % 2){// Odd Event Number case
    fillWithOverFlow(histogram_EventNumber_,  0., evtWeight, evtWeightErr);                                                                                                                         
  }else{ // Even Event Number case                                                                                                                                                        
    fillWithOverFlow(histogram_EventNumber_,  1., evtWeight, evtWeightErr);     
  }      

  for(unsigned int i=0;i < labels_spin2_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_SUM_spin2_[labels_spin2_[i]], BDTOutput_SUM_Map_spin2[labels_spin2_[i]], evtWeight, evtWeightErr);
  }

  for(unsigned int i=0;i < labels_spin0_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_SUM_spin0_[labels_spin0_[i]], BDTOutput_SUM_Map_spin0[labels_spin0_[i]], evtWeight, evtWeightErr);
  }

 for(unsigned int i=0;i < labels_nonres_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_SUM_nonres_[labels_nonres_[i]], BDTOutput_SUM_Map_nonres[labels_nonres_[i]], evtWeight, evtWeightErr);
  }

}
