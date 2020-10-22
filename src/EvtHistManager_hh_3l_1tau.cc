#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_3l_1tau.h"
//#include "tthAnalysis/HiggsToTauTau/interface/BM_list.h" // BMS
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()

EvtHistManager_hh_3l_1tau::EvtHistManager_hh_3l_1tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numHadTaus"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["MET"] = { "central" };
  central_or_shiftOptions_["nSFOS"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["MET_LD"] = { "central" };
  central_or_shiftOptions_["lep1_pt"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "central" };
  central_or_shiftOptions_["dihiggsMass"] = { "central" };
  central_or_shiftOptions_["dR_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["m_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["dR_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["m_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["mllOS_closestToZ"] = { "central" };
  central_or_shiftOptions_["mT_SSlepdR"] = { "central" };
  central_or_shiftOptions_["maxdZ_lep"] = { "central" };
  central_or_shiftOptions_["mindPhiLepMET"] = { "central" };
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
EvtHistManager_hh_3l_1tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_3l_1tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",      5,   -0.5,  +4.5  );
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",          5,   -0.5,  +4.5  );
  histogram_numHadTaus_       = book1D(dir, "numHadTaus",       "numHadTaus",        5,   -0.5,  +4.5  );
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20,  -0.5,  +19.5 );
  histogram_MET_              = book1D(dir, "MET",              "MET",               125, -0.,   +250  );
  histogram_nSFOS_            = book1D(dir, "nSFOS",            "nSFOS",             5,   -0.5,  +4.5  );
  histogram_HT_               = book1D(dir, "HT",               "HT",                150, -0.,   +1500.);
  histogram_MET_LD_           = book1D(dir, "MET_LD",           "MET_LD",            125, -0.,   +250. );
  histogram_lep1_pt_          = book1D(dir, "lep1_pt",          "lep1_pt",           125, -0.,   +250. );
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",    150, -0.,   +1500.);
  histogram_dihiggsMass_      = book1D(dir, "dihiggsMass",      "dihiggsMass",       150, -0.,   +1500.);
  histogram_dR_smartpair_ltau_= book1D(dir, "dR_smartpair_ltau","dR_smartpair_ltau", 35,  -0.,   +3.5  );
  histogram_m_smartpair_ltau_ = book1D(dir, "m_smartpair_ltau", "m_smartpair_ltau",  100, -0.,   +200. );
  histogram_dR_smartpair_ll_  = book1D(dir, "dR_smartpair_ll",  "dR_smartpair_ll",   35,  -0.,   +3.5  );
  histogram_m_smartpair_ll_   = book1D(dir, "m_smartpair_ll",   "m_smartpair_ll",    100, -0.,   +200. );
  histogram_mllOS_closestToZ_ = book1D(dir, "mllOS_closestToZ", "mllOS_closestToZ",  126, -2.,   +250. );
  histogram_mT_SSlepdR_       = book1D(dir, "mT_SSlepdR",       "mT_SSlepdR",        151, -1.,   +150. );
  histogram_maxdZ_lep_        = book1D(dir, "maxdZ_lep",        "maxdZ_lep",         100, -0.,   +0.05 );
  histogram_mindPhiLepMET_    = book1D(dir, "mindPhiLepMET",    "mindPhiLepMET",     35,  -3.5,  +3.5  );
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",      1,   -0.5,  +0.5  );
  histogram_EventNumber_      = book1D(dir, "EventNumber",      "EventNumber",       2,   -0.5,  +1.5  );
  histogram_EventNumber_->GetXaxis()->SetBinLabel(1,"Odd");
  histogram_EventNumber_->GetXaxis()->SetBinLabel(2,"Even");

  for(unsigned int i=0;i < labels_spin2_.size();i++){ 
    TH1* histogram_BDT_output_spin2 = book1D(dir, labels_spin2_[i], labels_spin2_[i], 100, 0., 1.); 
    histogram_Map_BDTOutput_spin2_.insert(std::make_pair(labels_spin2_[i], histogram_BDT_output_spin2)); 
  }

  for(unsigned int i=0;i < labels_spin0_.size();i++){ 
    TH1* histogram_BDT_output_spin0 = book1D(dir, labels_spin0_[i], labels_spin0_[i], 100, 0., 1.); 
    histogram_Map_BDTOutput_spin0_.insert(std::make_pair(labels_spin0_[i], histogram_BDT_output_spin0)); 
  }

  for(unsigned int i=0;i < labels_nonres_.size();i++){ 
    TH1* histogram_BDT_output_nonres = book1D(dir, labels_nonres_[i], labels_nonres_[i], 100, 0., 1.); 
    histogram_Map_BDTOutput_nonRes_.insert(std::make_pair(labels_nonres_[i], histogram_BDT_output_nonres)); 
  }
}

void
EvtHistManager_hh_3l_1tau::fillHistograms(int numElectrons,
					  int numMuons,
					  int numHadTaus,
					  int numJets,
					  double MET,
					  int nSFOS,
					  double HT,
					  double MET_LD,
					  double lep1_pt,
					  double dihiggsVisMass,
					  double dihiggsMass,
					  double dR_smartpair_ltau,
					  double m_smartpair_ltau,
					  double dR_smartpair_ll,
					  double m_smartpair_ll,
					  double mllOS_closestToZ,
					  double mT_SSlepdR,
					  double maxdZ_lep,
					  double mindPhiLepMET,
					  std::map<std::string, double> & BDTOutput_Map_spin0,
					  std::map<std::string, double> & BDTOutput_Map_spin2,
					  std::map<std::string, double> & BDTOutput_Map_nonRes,
					  double evtWeight,					 
					  unsigned int evt_number					 
)
{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_,      numElectrons,        evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,          numMuons,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,        numHadTaus,          evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numJets_,           numJets,             evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_MET_,               MET,                 evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_nSFOS_,               nSFOS,                 evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_HT_,                HT,                  evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_MET_LD_,            MET_LD,              evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_lep1_pt_,           lep1_pt,             evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dihiggsVisMass_,    dihiggsVisMass,      evtWeight,     evtWeightErr);
  if ( dihiggsMass > 0. ) {
    fillWithOverFlow(histogram_dihiggsMass_,     dihiggsMass,         evtWeight,     evtWeightErr);
  }
  fillWithOverFlow(histogram_dR_smartpair_ll_,   dR_smartpair_ltau,   evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_smartpair_ll_,    m_smartpair_ltau,    evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dR_smartpair_ltau_, dR_smartpair_ll,     evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_smartpair_ltau_,  m_smartpair_ll,      evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_mllOS_closestToZ_,  mllOS_closestToZ,    evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_mT_SSlepdR_,        mT_SSlepdR,          evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_maxdZ_lep_,         maxdZ_lep,           evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_mindPhiLepMET_,     mindPhiLepMET,       evtWeight,     evtWeightErr);  
  fillWithOverFlow(histogram_EventCounter_,      0.,                  evtWeight,     evtWeightErr);
  if(evt_number % 2){// ODD EVENT NUMBER CASE                                                                                                                                                    
    fillWithOverFlow(histogram_EventNumber_,     0.,                  evtWeight,     evtWeightErr);                                                                                                                         
  }else{ // EVEN EVENT NUMBER CASE                                                                                                                                                                   
    fillWithOverFlow(histogram_EventNumber_,     1.,                  evtWeight,     evtWeightErr);     
  }      
  for(unsigned int i=0;i < labels_spin2_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_spin2_[labels_spin2_[i]], BDTOutput_Map_spin2[labels_spin2_[i]], evtWeight, evtWeightErr);
  }
  for(unsigned int i=0;i < labels_spin0_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_spin0_[labels_spin0_[i]], BDTOutput_Map_spin0[labels_spin0_[i]], evtWeight, evtWeightErr);
  }
  for(unsigned int i=0;i < labels_nonres_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_nonRes_[labels_nonres_[i]], BDTOutput_Map_nonRes[labels_nonres_[i]], evtWeight, evtWeightErr);
  }
}
