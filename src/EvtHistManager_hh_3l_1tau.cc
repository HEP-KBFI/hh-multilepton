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
  central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
  central_or_shiftOptions_["numBJets_loose"] = { "central" };
  central_or_shiftOptions_["numBJets_medium"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "central" };
  central_or_shiftOptions_["dihiggsMass"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };
  central_or_shiftOptions_["HTMiss"] = { "central" };
  central_or_shiftOptions_["MET"] = { "central" };
  central_or_shiftOptions_["MET_LD"] = { "central" };
  central_or_shiftOptions_["mT_nonZlepMET"] = { "central" };
  central_or_shiftOptions_["mT_SSlephigh"] = { "central" };
  central_or_shiftOptions_["mT_SSleplow"] = { "central" };
  central_or_shiftOptions_["mT_SSlepdR"] = { "central" };
  central_or_shiftOptions_["mllOS_closestToZ"] = { "central" };
  central_or_shiftOptions_["SVFit_h1_visMass"] = { "central" }; 
  central_or_shiftOptions_["SVFit_h2_visMass"] = { "central" };
  central_or_shiftOptions_["SVFit_h1_pT"] = { "central" }; 
  central_or_shiftOptions_["SVFit_h2_pT"] = { "central" }; 
  central_or_shiftOptions_["SVFit_hh_deltaPhi"] = { "central" }; 
  central_or_shiftOptions_["SVFit_hh_deltaEta"] = { "central" };
  central_or_shiftOptions_["SVFit_hh_deltaR"] = { "central" };
  central_or_shiftOptions_["SVFit_hh_pT"] = { "central" };
  central_or_shiftOptions_["SVFit_hh_cosTheta"] = { "central" };
  central_or_shiftOptions_["m_ltau_minltaupair"] = { "central" };
  central_or_shiftOptions_["pT_ltau_minltaupair"] = { "central" };
  central_or_shiftOptions_["dR_ltau_minltaupair"] = { "central" };
  central_or_shiftOptions_["dEta_ltau_minltaupair"] = { "central" };
  central_or_shiftOptions_["dPhi_ltau_minltaupair"] = { "central" };
  central_or_shiftOptions_["m_ll_minltaupair"] = { "central" };
  central_or_shiftOptions_["pT_ll_minltaupair"] = { "central" };
  central_or_shiftOptions_["dR_ll_minltaupair"] = { "central" };
  central_or_shiftOptions_["dEta_ll_minltaupair"] = { "central" };
  central_or_shiftOptions_["dPhi_ll_minltaupair"] = { "central" };
  central_or_shiftOptions_["m_ltau_minllpair"] = { "central" };
  central_or_shiftOptions_["pT_ltau_minllpair"] = { "central" };
  central_or_shiftOptions_["dR_ltau_minllpair"] = { "central" };
  central_or_shiftOptions_["dEta_ltau_minllpair"] = { "central" };
  central_or_shiftOptions_["dPhi_ltau_minllpair"] = { "central" };
  central_or_shiftOptions_["m_ll_minllpair"] = { "central" };
  central_or_shiftOptions_["pT_ll_minllpair"] = { "central" };
  central_or_shiftOptions_["dR_ll_minllpair"] = { "central" };
  central_or_shiftOptions_["dEta_ll_minllpair"] = { "central" };
  central_or_shiftOptions_["dPhi_ll_minllpair"] = { "central" };
  central_or_shiftOptions_["mlll"] = { "central" };
  central_or_shiftOptions_["mAll"] = { "central" };
  central_or_shiftOptions_["dr_los1"] = { "central" };
  central_or_shiftOptions_["dr_los2"] = { "central" };
  central_or_shiftOptions_["m_OS_etau_closestToZ"] = { "central" };
  central_or_shiftOptions_["m_OS_etau_closestToZ"] = { "central" };
  central_or_shiftOptions_["trigger_eTauZVezto"] = { "central" };
  central_or_shiftOptions_["triggerECalCrackVeto"] = { "central" };
  central_or_shiftOptions_["triggerBadTauVeto"] = { "central" };
  central_or_shiftOptions_["m_ltau_closestToZ"] = { "central" };
  central_or_shiftOptions_["m_OS_ltau_closestTo"] = { "central" };
  central_or_shiftOptions_["tau_antiElectron_matched"] = { "central" };
  central_or_shiftOptions_["tau_antiElectron_unmatched"] = { "central" };
  central_or_shiftOptions_["dR_smartpair1"] = { "central" };
  central_or_shiftOptions_["dEta_smartpair1"] = { "central" };
  central_or_shiftOptions_["dPhi_smartpair1"] = { "central" };
  central_or_shiftOptions_["m_smartpair1"] = { "central" };
  central_or_shiftOptions_["pT_smartpair1"] = { "central" };
  central_or_shiftOptions_["pTSum_smartpair1"] = { "central" };
  central_or_shiftOptions_["pTDiff_smartpair1"] = { "central" };
  central_or_shiftOptions_["dR_smartpair2"] = { "central" };
  central_or_shiftOptions_["dEta_smartpair2"] = { "central" };
  central_or_shiftOptions_["dPhi_smartpair2"] = { "central" };
  central_or_shiftOptions_["m_smartpair2"] = { "central" };
  central_or_shiftOptions_["pT_smartpair2"] = { "central" };
  central_or_shiftOptions_["pTSum_smartpair2"] = { "central" };
  central_or_shiftOptions_["pTDiff_smartpair2"] = { "central" };
  central_or_shiftOptions_["dR_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["dEta_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["m_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["pT_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["pTSum_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["pTDiff_smartpair_ll"] = { "central" };
  central_or_shiftOptions_["dR_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["dEta_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["dPhi_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["m_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["pT_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["pTSum_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["pTDiff_smartpair_ltau"] = { "central" };
  central_or_shiftOptions_["nSFOS"] = { "central" };
  central_or_shiftOptions_["mZ_tau"] = { "central" };
  central_or_shiftOptions_["dPhi_nonZlMET"] = { "central" };
  central_or_shiftOptions_["mindPhiLepMET"] = { "central" };
  central_or_shiftOptions_["pT4l"] = { "central" };
  std::vector<double> gen_mHH = cfg.getParameter<std::vector<double>>("gen_mHH");


  for(unsigned int i=0;i<gen_mHH.size();i++){
    unsigned int mass_int = (int)gen_mHH[i]; // Conversion from double to unsigned int                                                                                                                                                                                
    std::string key = "";
    ostringstream temp;
    temp << mass_int;
    key = temp.str(); // Conversion from unsigned int to string                                                                                                                                                                                                             
    std::string key_final = "BDTOutput_" + key; // For the TMVAInterface
    labels_.push_back(key_final);

    //std::string XGB_key_final = "BDTOutput_" + key + "_pkl"; // For the XGBInterface
    //std::string XGB_key_final = "NNOutput_" + key;             // For the TensorFlowInterface
    //XGB_labels_.push_back(XGB_key_final);
  }
  for(unsigned int i=0;i < labels_.size();i++){
    central_or_shiftOptions_[labels_[i]] = { "*" }; 
    //central_or_shiftOptions_[XGB_labels_[i]] = { "*" }; 
  }
  std::vector<std::string> BMS = { "SM", "BM1", "BM2", "BM3", "BM4", "BM5", "BM6", "BM7", "BM8", "BM9", "BM10", "BM11", "BM12" };
  for(unsigned int i=0; i<BMS.size(); i++){ // Loop over different nodes
    std::string key_final = "BDTOutput_nonRes_" + BMS[i];
    labels_nonRes_.push_back(key_final);
  }
  for(unsigned int i=0;i < labels_nonRes_.size();i++){
    central_or_shiftOptions_[labels_nonRes_[i]] = { "*" }; 
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

  histogram_EventCounter_    = book1D(dir, "EventCounter",    "EventCounter",      1, -0.5,  +0.5);

  histogram_EventNumber_      = book1D(dir, "EventNumber",     "EventNumber",      2, 0., 2.0);
  histogram_EventNumber_->GetXaxis()->SetBinLabel(1,"Odd");
  histogram_EventNumber_->GetXaxis()->SetBinLabel(2,"Even");
  for(unsigned int i=0;i < labels_.size();i++){
    TH1* histogram_BDT_output = book1D(dir, labels_[i], labels_[i], 100, 0., 1.); 
    histogram_Map_BDTOutput_SUM_.insert(std::make_pair(labels_[i], histogram_BDT_output));
  }
  for(unsigned int i=0;i < labels_nonRes_.size();i++){
    TH1* histogram_BDT_output = book1D(dir, labels_nonRes_[i], labels_nonRes_[i], 100, 0., 1.); 
    histogram_Map_BDTOutput_nonRes_SUM_.insert(std::make_pair(labels_nonRes_[i], histogram_BDT_output));
  }
  //  for(unsigned int j=0;j < XGB_labels_.size();j++){
  //  TH1* histogram_XGB_output = book1D(dir, XGB_labels_[j], XGB_labels_[j], 100, 0., 1.); 
  //  histogram_Map_XGBOutput_SUM_.insert(std::make_pair(XGB_labels_[j], histogram_XGB_output));
  // }

  histogram_HTMiss_          = book1D(dir, "HTMiss",           "HTMiss",          125, 0., 250.);
  histogram_MET_             = book1D(dir, "MET",              "MET",             125, 0., 250.);
  histogram_MET_LD_          = book1D(dir, "MET_LD",           "MET_LD",          125, 0., 250.);
  histogram_mT_nonZlepMET_   = book1D(dir, "mT_nonZlepMET",    "mT_nonZlepMET",   125, 0., 150.);
  histogram_mT_SSlephigh_    = book1D(dir, "mT_SSlephigh",     "mT_SSlephigh",    125, 0., 150.);
  histogram_mT_SSleplow_     = book1D(dir, "mT_SSleplow",      "mT_SSleplow",     125, 0., 150.);
  histogram_mT_SSlepdR_      = book1D(dir, "mT_SSlepdR",       "mT_SSlepdR",      125, 0., 150.);
  histogram_mllOS_closestToZ_= book1D(dir, "mllOS_closestToZ", "mllOS_closestToZ",125, 0., 250.);
  histogram_SVFit_h1_visMass_= book1D(dir, "SVFit_h1_visMass", "SVFit_h1_visMass",151, -1.,150.); 
  histogram_SVFit_h2_visMass_= book1D(dir, "SVFit_h2_visMass", "SVFit_h2_visMass",151, -1.,150.); 
  histogram_SVFit_h1_pT_     = book1D(dir, "SVFit_h1_pT",      "SVFit_h1_pT"     ,161, -5.,800.); 
  histogram_SVFit_h2_pT_     = book1D(dir, "SVFit_h2_pT",      "SVFit_h2_pT"     ,161, -5.,800.); 
  histogram_SVFit_hh_deltaPhi_= book1D(dir,"SVFit_hh_deltaPhi","SVFit_hh_deltaPhi",45, -1., 3.5); 
  histogram_SVFit_hh_deltaEta_= book1D(dir,"SVFit_hh_deltaEta","SVFit_hh_deltaEta",45, -1., 3.5); 
  histogram_SVFit_hh_deltaR_ = book1D(dir, "SVFit_hh_deltaR",  "SVFit_hh_deltaR" ,45, -1.,  3.5); 
  histogram_SVFit_hh_pT_     = book1D(dir, "SVFit_hh_pT",      "SVFit_hh_pT"     ,151,-2., 300.); 
  histogram_SVFit_hh_cosTheta_= book1D(dir,"SVFit_hh_cosTheta","SVFit_hh_cosTheta",100,-1., 1.); 
  histogram_m_ltau_minltaupair_= book1D(dir, "m_ltau_minltaupair", "m_ltau_minltaupair",100,  0., 200.);
  histogram_pT_ltau_minltaupair_= book1D(dir, "pT_ltau_minltaupair", "pT_ltau_minltaupair",100, 0., 200.);
  histogram_dR_ltau_minltaupair_= book1D(dir, "dR_ltau_minltaupair", "dR_ltau_minltaupair",35, 0., 3.5);
  histogram_dEta_ltau_minltaupair_= book1D(dir, "dEta_ltau_minltaupair", "dEta_ltau_minltaupair",35, 0., 3.5);
  histogram_dPhi_ltau_minltaupair_= book1D(dir, "dPhi_ltau_minltaupair", "dPhi_ltau_minltaupair",35, 0., 3.5);
  histogram_m_ll_minltaupair_= book1D(dir, "m_ll_minltaupair", "m_ll_minltaupair",100,  0., 200.);
  histogram_pT_ll_minltaupair_= book1D(dir, "pT_ll_minltaupair", "pT_ll_minltaupair",100, 0., 200.);
  histogram_dR_ll_minltaupair_= book1D(dir, "dR_ll_minltaupair", "dR_ll_minltaupair",35, 0., 3.5);
  histogram_dEta_ll_minltaupair_= book1D(dir, "dEta_ll_minltaupair", "dEta_ll_minltaupair",35, 0., 3.5);
  histogram_dPhi_ll_minltaupair_= book1D(dir, "dPhi_ll_minltaupair", "dPhi_ll_minltaupair",35, 0., 3.5);
  histogram_m_ltau_minllpair_= book1D(dir, "m_ltau_minllpair", "m_ltau_minllpair",100,  0., 200.);
  histogram_pT_ltau_minllpair_= book1D(dir, "pT_ltau_minllpair", "pT_ltau_minllpair",100, 0., 200.);
  histogram_dR_ltau_minllpair_= book1D(dir, "dR_ltau_minllpair", "dR_ltau_minllpair",35, 0., 3.5);
  histogram_dEta_ltau_minllpair_= book1D(dir, "dEta_ltau_minllpair", "dEta_ltau_minllpair",35, 0., 3.5);
  histogram_dPhi_ltau_minllpair_= book1D(dir, "dPhi_ltau_minllpair", "dPhi_ltau_minllpair",35, 0., 3.5);
  histogram_m_ll_minllpair_= book1D(dir, "m_ll_minllpair", "m_ll_minllpair",100,  0., 200.);
  histogram_pT_ll_minllpair_= book1D(dir, "pT_ll_minllpair", "pT_ll_minllpair",100, 0., 200.);
  histogram_dR_ll_minllpair_= book1D(dir, "dR_ll_minllpair", "dR_ll_minllpair",35, 0., 3.5);
  histogram_dEta_ll_minllpair_= book1D(dir, "dEta_ll_minllpair", "dEta_ll_minllpair",35, 0., 3.5);
  histogram_dPhi_ll_minllpair_= book1D(dir, "dPhi_ll_minllpair", "dPhi_ll_minllpair",35, 0., 3.5);
  histogram_mlll_             = book1D(dir, "mlll",              "mlll",             100,0., 500.);
  histogram_mAll_             = book1D(dir, "mAll",              "mAll",             100,0., 500.);
  histogram_dr_los1_= book1D(dir, "dr_los1",                     "dr_los1",          35,  0.,3.5);
  histogram_dr_los2_= book1D(dir, "dr_los2",                     "dr_los2",          35,  0.,3.5);
  histogram_m_OS_etau_closestToZ_= book1D(dir, "m_OS_etau_closestToZ",  "m_OS_etau_closestToZ",          100,  0.,200);
  histogram_m_etau_closestToZ_= book1D(dir, "m_etau_closestToZ", "m_etau_closestToZ",  100,  0.,200);
  histogram_trigger_eTauZVezto_= book1D(dir, "trigger_eTauZVezto", "trigger_eTauZVezto",  2,  -0.5,1.5);
  histogram_triggerECalCrackVeto_= book1D(dir, "triggerECalCrackVeto",  "triggerECalCrackVeto",  2,  -0.5,1.5);
  histogram_triggerBadTauVeto_= book1D(dir, "triggerBadTauVeto",  "triggerBadTauVeto", 2,  -0.5,1.5);
  histogram_m_OS_ltau_closestToZ_= book1D(dir, "m_OS_ltau_closestToZ",  "m_OS_ltau_closestToZ",          100,  0.,200);
  histogram_m_ltau_closestToZ_= book1D(dir, "m_ltau_closestToZ",  "m_ltau_closestToZ",          100,  0.,200);
  histogram_tau_antiElectron_matched_= book1D(dir, "tau_antiElectron_matched",  "tau_antiElectron_matched",          10,  -1.5,8.5);
  histogram_tau_antiElectron_unmatched_= book1D(dir, "tau_antiElectron_unmatched",  "tau_antiElectron_unmatched",          10,  -1.5,8.5);
  histogram_dR_smartpair1_= book1D(dir, "dR_smartpair1",                     "dR_smartpair1",          35,  0.,3.5);
  histogram_dR_smartpair2_= book1D(dir, "dR_smartpair2",                     "dR_smartpair2",          35,  0.,3.5);
  histogram_dR_smartpair_ll_= book1D(dir, "dR_smartpair_ll",                     "dR_smartpair_ll",          35,  0.,3.5);
  histogram_dR_smartpair_ltau_= book1D(dir, "dR_smartpair_ltau",                     "dR_smartpair_ltau",          35,  0.,3.5);
  histogram_dPhi_smartpair1_= book1D(dir, "dPhi_smartpair1",                     "dPhi_smartpair1",          35,  -3.5,3.5);
  histogram_dPhi_smartpair2_= book1D(dir, "dPhi_smartpair2",                     "dPhi_smartpair2",          35,  -3.5,3.5);
  histogram_dPhi_smartpair_ll_= book1D(dir, "dPhi_smartpair_ll",                     "dPhi_smartpair_ll",          35,  -3.5,3.5);
  histogram_dPhi_smartpair_ltau_= book1D(dir, "dPhi_smartpair_ltau",                     "dPhi_smartpair_ltau",          35,  -3.5,3.5);
  histogram_dEta_smartpair1_= book1D(dir, "dEta_smartpair1",                     "dEta_smartpair1",          50,  -5,5);
  histogram_dEta_smartpair2_= book1D(dir, "dEta_smartpair2",                     "dEta_smartpair2",          50,  -5,5);
  histogram_dEta_smartpair_ll_= book1D(dir, "dEta_smartpair_ll",                     "dEta_smartpair_ll",          50,  -5,5);
  histogram_dEta_smartpair_ltau_= book1D(dir, "dEta_smartpair_ltau",                     "dEta_smartpair_ltau",          50,  -5,5);
  histogram_pT_smartpair1_= book1D(dir, "pT_smartpair1",                     "pT_smartpair1",          40,  0.,200);
  histogram_pT_smartpair2_= book1D(dir, "pT_smartpair2",                     "pT_smartpair2",          40,  0.,200);
  histogram_pT_smartpair_ll_= book1D(dir, "pT_smartpair_ll",                     "pT_smartpair_ll",          40,  0.,200);
  histogram_pT_smartpair_ltau_= book1D(dir, "pT_smartpair_ltau",                     "pT_smartpair_ltau",          40,  0.,200);
  histogram_pTSum_smartpair1_= book1D(dir, "pTSum_smartpair1",                     "pTSum_smartpair1",          30,  0.,300);
  histogram_pTSum_smartpair2_= book1D(dir, "pTSum_smartpair2",                     "pTSum_smartpair2",          30,  0.,300);
  histogram_pTSum_smartpair_ll_= book1D(dir, "pTSum_smartpair_ll",                     "pTSum_smartpair_ll",          30,  0.,300);
  histogram_pTSum_smartpair_ltau_= book1D(dir, "pTSum_smartpair_ltau",                     "pTSum_smartpair_ltau",          30,  0.,300);
  histogram_pTDiff_smartpair1_= book1D(dir, "pTDiff_smartpair1",                     "pTDiff_smartpair1",          40,  0.,200);
  histogram_pTDiff_smartpair2_= book1D(dir, "pTDiff_smartpair2",                     "pTDiff_smartpair2",          40,  0.,200);
  histogram_pTDiff_smartpair_ll_= book1D(dir, "pTDiff_smartpair_ll",                     "pTDiff_smartpair_ll",          40,  0.,200);
  histogram_pTDiff_smartpair_ltau_= book1D(dir, "pTDiff_smartpair_ltau",                     "pTDiff_smartpair_ltau",          40,  0.,200);
  histogram_nSFOS_= book1D(dir, "nSFOS",                     "nSFOS",          5,  0,5);
  histogram_mZ_tau_= book1D(dir, "mZ_tau",                     "mZ_tau",          25,  0.,250);
  histogram_dPhi_nonZlMET_= book1D(dir, "dPhi_nonZlMET",                     "dPhi_nonZlMET",          35,  -3.5,3.5);  
  histogram_mindPhiLepMET_= book1D(dir, "mindPhiLepMET",                     "mindPhiLepMET",          35,  -3.5,3.5);
  histogram_pT4l_= book1D(dir, "pT4l",                     "pT4l",          25,  0.,250);
}

void
EvtHistManager_hh_3l_1tau::fillHistograms(int numElectrons,
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
					  double evtWeight,
					  double HTMiss,
					  double MET,
					  double MET_LD,
					  double mT_nonZlepMET,
					  double mT_SSlephigh,
					  double mT_SSleplow,
					  double mT_SSlepdR,
					  double mllOS_closestToZ,
					  double SVFit_h1_visMass, 
					  double SVFit_h2_visMass,
					  double SVFit_h1_pT, 
					  double SVFit_h2_pT, 
					  double SVFit_hh_deltaPhi, 
					  double SVFit_hh_deltaEta,
					  double SVFit_hh_deltaR,
					  double SVFit_hh_pT,
					  double SVFit_hh_cosTheta,
					  double m_ltau_minltaupair,
					  double pT_ltau_minltaupair,
					  double dR_ltau_minltaupair,
					  double dEta_ltau_minltaupair,
					  double dPhi_ltau_minltaupair,
					  double m_ll_minltaupair,
					  double pT_ll_minltaupair,
					  double dR_ll_minltaupair,
					  double dEta_ll_minltaupair,
					  double dPhi_ll_minltaupair,
					  double m_ltau_minllpair,
					  double pT_ltau_minllpair,
					  double dR_ltau_minllpair,
					  double dEta_ltau_minllpair,
					  double dPhi_ltau_minllpair,
					  double m_ll_minllpair,
					  double pT_ll_minllpair,
					  double dR_ll_minllpair,
					  double dEta_ll_minllpair,
					  double dPhi_ll_minllpair,
					  double mlll,
					  double mAll,
					  double dr_los1,
					  double dr_los2,
					  double m_OS_etau_closestToZ,
					  double m_etau_closestToZ,
					  int trigger_eTauZVezto,
					  int triggerECalCrackVeto,
					  int triggerBadTauVeto,
					  double m_ltau_closestToZ,
					  double m_OS_ltau_closestToZ,
					  double tau_antiElectron_matched,
					  double tau_antiElectron_unmatched,
					  double dR_smartpair1,
					  double dR_smartpair2,
					  double dR_smartpair_ll,
					  double dR_smartpair_ltau,
					  double dPhi_smartpair1,
					  double dPhi_smartpair2,
					  double dPhi_smartpair_ll,
					  double dPhi_smartpair_ltau,
					  double dEta_smartpair1,
					  double dEta_smartpair2,
					  double dEta_smartpair_ll,
					  double dEta_smartpair_ltau,
					  double pT_smartpair1,
					  double pT_smartpair2,
					  double pT_smartpair_ll,
					  double pT_smartpair_ltau,
					  double pTSum_smartpair1,
					  double pTSum_smartpair2,
					  double pTSum_smartpair_ll,
					  double pTSum_smartpair_ltau,
					  double pTDiff_smartpair1,
					  double pTDiff_smartpair2,
					  double pTDiff_smartpair_ll,
					  double pTDiff_smartpair_ltau,
					  int nSFOS,
					  double mZ_tau,
					  double dPhi_nonZlMET,
					  double mindPhiLepMET,
					  double pT4l,
					  std::map<std::string, double> & BDTOutput_SUM_Map,
					  std::map<std::string, double> & BDTOutput_nonRes_SUM_Map,
					  unsigned int evt_number					 
)
{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_,    numElectrons,        evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,        numMuons,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numHadTaus_,      numHadTaus,          evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numJets_,         numJets,             evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,   numJetsPtGt40,       evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numBJets_loose_,  numBJets_loose,      evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_numBJets_medium_, numBJets_medium,     evtWeight,     evtWeightErr);

  fillWithOverFlow(histogram_dihiggsVisMass_,  dihiggsVisMass,  evtWeight, evtWeightErr);
  if ( dihiggsMass > 0. ) {
    fillWithOverFlow(histogram_dihiggsMass_,   dihiggsMass,     evtWeight, evtWeightErr);
  }

  fillWithOverFlow(histogram_HT_,              HT,              evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,           STMET,           evtWeight, evtWeightErr);
  
  fillWithOverFlow(histogram_EventCounter_,    0.,              evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_HTMiss_,           HTMiss,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MET_,              MET,             evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_MET_LD_,           MET_LD,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_nonZlepMET_,    mT_nonZlepMET,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_SSlephigh_,     mT_SSlephigh,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_SSleplow_,      mT_SSleplow,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_SSlepdR_,       mT_SSlepdR,      evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mllOS_closestToZ_, mllOS_closestToZ,evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_h1_visMass_, SVFit_h1_visMass,evtWeight, evtWeightErr); 
  fillWithOverFlow(histogram_SVFit_h2_visMass_, SVFit_h2_visMass,evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_h2_pT_,      SVFit_h2_pT,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_h1_pT_,      SVFit_h1_pT,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_hh_deltaPhi_,SVFit_hh_deltaPhi,evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_hh_deltaEta_,SVFit_hh_deltaEta,evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_hh_deltaR_,  SVFit_hh_deltaR, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_hh_pT_,      SVFit_hh_pT,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_SVFit_hh_cosTheta_,SVFit_hh_cosTheta,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_m_ltau_minltaupair_,m_ltau_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_pT_ltau_minltaupair_,pT_ltau_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dR_ltau_minltaupair_,dR_ltau_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dEta_ltau_minltaupair_,dEta_ltau_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ltau_minltaupair_,dPhi_ltau_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_m_ll_minltaupair_,m_ll_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_pT_ll_minltaupair_,pT_ll_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_minltaupair_,dR_ll_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dEta_ll_minltaupair_,dEta_ll_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_minltaupair_,dPhi_ll_minltaupair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_m_ltau_minllpair_,m_ltau_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_pT_ltau_minllpair_,pT_ltau_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dR_ltau_minllpair_,dR_ltau_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dEta_ltau_minllpair_,dEta_ltau_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ltau_minllpair_,dPhi_ltau_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_m_ll_minllpair_,m_ll_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_pT_ll_minllpair_,pT_ll_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_minllpair_,dR_ll_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dEta_ll_minllpair_,dEta_ll_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_minllpair_,dPhi_ll_minllpair,evtWeight,evtWeightErr);
  fillWithOverFlow(histogram_mlll_,          mlll,               evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_mAll_,          mAll,               evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dr_los1_,       dr_los1,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dr_los2_,       dr_los2,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_OS_etau_closestToZ_,      m_OS_etau_closestToZ,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_etau_closestToZ_,       m_etau_closestToZ,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_trigger_eTauZVezto_,       trigger_eTauZVezto,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_triggerECalCrackVeto_,       triggerECalCrackVeto,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_triggerBadTauVeto_,triggerBadTauVeto       ,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_ltau_closestToZ_,m_ltau_closestToZ       ,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_m_OS_ltau_closestToZ_,m_OS_ltau_closestToZ       ,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_tau_antiElectron_matched_,tau_antiElectron_matched       ,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_tau_antiElectron_unmatched_,tau_antiElectron_unmatched       ,            evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dR_smartpair1_, dR_smartpair1, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dR_smartpair2_, dR_smartpair2, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dR_smartpair_ll_, dR_smartpair_ll, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dPhi_smartpair_ltau_, dR_smartpair_ltau, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dPhi_smartpair1_, dPhi_smartpair1, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dPhi_smartpair2_, dPhi_smartpair2, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dPhi_smartpair_ll_, dPhi_smartpair_ll, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dPhi_smartpair_ltau_, dPhi_smartpair_ltau, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dEta_smartpair1_, dEta_smartpair1, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dEta_smartpair2_, dEta_smartpair2, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dEta_smartpair_ll_, dEta_smartpair_ll, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dEta_smartpair_ltau_, dEta_smartpair_ltau, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pT_smartpair1_, pT_smartpair1, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pT_smartpair2_, pT_smartpair2, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pT_smartpair_ll_, pT_smartpair_ll, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pT_smartpair_ltau_, pT_smartpair_ltau, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTSum_smartpair1_, pTSum_smartpair1, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTSum_smartpair2_, pTSum_smartpair2, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTSum_smartpair_ll_, pTSum_smartpair_ll, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTSum_smartpair_ltau_, pTSum_smartpair_ltau, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTDiff_smartpair1_, pTDiff_smartpair1, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTDiff_smartpair2_, pTDiff_smartpair2, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTDiff_smartpair_ll_, pTDiff_smartpair_ll, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pTDiff_smartpair_ltau_, pTDiff_smartpair_ltau, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_nSFOS_, nSFOS, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_mZ_tau_, mZ_tau, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_dPhi_nonZlMET_, dPhi_nonZlMET, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_mindPhiLepMET_, mindPhiLepMET, evtWeight,     evtWeightErr);
  fillWithOverFlow(histogram_pT4l_, pT4l, evtWeight,     evtWeightErr);

  if(evt_number % 2){// ODD EVENT NUMBER CASE                                                                                                                                                    
    fillWithOverFlow(histogram_EventNumber_,  0., evtWeight, evtWeightErr);                                                                                                                         
  }else{ // EVEN EVENT NUMBER CASE                                                                                                                                                                   
    fillWithOverFlow(histogram_EventNumber_,  1., evtWeight, evtWeightErr);     
  }      
  for(unsigned int i=0;i < labels_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_SUM_[labels_[i]], BDTOutput_SUM_Map[labels_[i]], evtWeight, evtWeightErr);
  }
  for(unsigned int i=0;i < labels_nonRes_.size();i++){
    fillWithOverFlow(histogram_Map_BDTOutput_nonRes_SUM_[labels_nonRes_[i]], BDTOutput_nonRes_SUM_Map[labels_nonRes_[i]], evtWeight, evtWeightErr);
  }

  //for(unsigned int i=0;i < XGB_labels_.size();i++){
  // fillWithOverFlow(histogram_Map_XGBOutput_SUM_[XGB_labels_[i]], XGBOutput_SUM_Map[XGB_labels_[i]], evtWeight, evtWeightErr);
  //}
}
