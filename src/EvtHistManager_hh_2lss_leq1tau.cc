#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2lss_leq1tau.h"

#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow(), fillWithOverFlow2d()
#include <TMath.h>

const int histogramMakingLevel = 2; // 0 / 1 / 2: fill minimum / a few more / all histograms
const bool makeBDTIpVarsPlotsWithFullSyst = true; // true: BDT ip variable plots are made for all systematics

EvtHistManager_hh_2lss_leq1tau::EvtHistManager_hh_2lss_leq1tau(const edm::ParameterSet & cfg)
  : HistManagerBase(cfg)
{
  const std::vector<std::string> bdtIpVars = {
     "leptonPairMass", "dihiggsVisMass", "met_LD", "dR_ll", "dR_l_Wjets_min", "dR_l_leadWjet_min", "dR_l_Wjets_max", "dR_l_leadWjet_max", "dR_2j_fromW1", "mT_lep1_met",
     "lep1_conePt", "lep2_conePt", "mindr_lep1_jet", "mindr_lep2_jet", "HT", "mht", "mass_2j_fromW1"
  };
  
  central_or_shiftOptions_["numElectrons"] = { "central" };
  central_or_shiftOptions_["numMuons"] = { "central" };
  central_or_shiftOptions_["numJets"] = { "central" };
  central_or_shiftOptions_["numJetsPtGt40"] = { "central" };
  central_or_shiftOptions_["dihiggsVisMass"] = { "*" };
  central_or_shiftOptions_["dihiggsMass_wMet"] = { "central" };
  central_or_shiftOptions_["jetMass"] = { "central" };
  central_or_shiftOptions_["leptonPairMass"] = { "central" };
  central_or_shiftOptions_["electronPairMass"] = { "central" };
  central_or_shiftOptions_["muonPairMass"] = { "central" };
  central_or_shiftOptions_["leptonPairCharge"] = { "central" };
  central_or_shiftOptions_["HT"] = { "central" };
  central_or_shiftOptions_["STMET"] = { "central" };
  central_or_shiftOptions_["EventCounter"] = { "*" };

  central_or_shiftOptions_["nElectrons_in_2lss"] = { "central" };
  central_or_shiftOptions_["dR_ll"] = { "central" };
  central_or_shiftOptions_["dPhi_ll"] = { "central" };
  
  central_or_shiftOptions_["nAK8_w2subjets"] = { "central" };
  central_or_shiftOptions_["nWJets_selected"] = { "central" }; 

  central_or_shiftOptions_["mass_2j_fromW1"] = { "central" };
  central_or_shiftOptions_["mass_2j_fromW2"] = { "central" };
  central_or_shiftOptions_["dR_2j_fromW1"] = { "central" };
  central_or_shiftOptions_["dR_2j_fromW2"] = { "central" };
  
  central_or_shiftOptions_["dR_Wjets_min"] = { "central" }; 
  central_or_shiftOptions_["dR_Wjets_max"] = { "central" };
  central_or_shiftOptions_["dR_l_Wjets_min"] = { "central" };
  central_or_shiftOptions_["dR_l_Wjets_max"] = { "central" };
  central_or_shiftOptions_["dR_l_AK4jets_min"] = { "central" };
  central_or_shiftOptions_["dR_l_AK4jets_max"] = { "central" }; 

  central_or_shiftOptions_["dR_l_leadWjet_min"] = { "central" };
  central_or_shiftOptions_["dR_l_leadWjet_max"] = { "central" };
  central_or_shiftOptions_["dR_l_leadAK4jet_min"] = { "central" };
  central_or_shiftOptions_["dR_l_leadAK4jet_max"] = { "central" };
  
  central_or_shiftOptions_["met"] = { "central" };
  central_or_shiftOptions_["mht"] = { "central" };
  central_or_shiftOptions_["met_LD"] = { "central" };

  central_or_shiftOptions_["mT_lep1_met"] = { "central" };
  central_or_shiftOptions_["mT_lep2_met"] = { "central" };

  central_or_shiftOptions_["eventCategory"] = { "central" };

  central_or_shiftOptions_["nTaus"] = { "central" }; 

  central_or_shiftOptions_["mindr_lep1_jet"] = { "central" };
  central_or_shiftOptions_["mindr_lep2_jet"] = { "central" };
  central_or_shiftOptions_["lep1_conePt"] = { "central" };
  central_or_shiftOptions_["lep2_conePt"] = { "central" };
  
  if (histogramMakingLevel >= 2)
  {
  central_or_shiftOptions_["pT_ll"] = { "central" };
  central_or_shiftOptions_["max_lep_eta"] = { "central" };
  central_or_shiftOptions_["pT_llMEt"] = { "central" };
  central_or_shiftOptions_["Smin_llMEt"] = { "central" };
  //central_or_shiftOptions_["lep1_conePt"] = { "central" };
  central_or_shiftOptions_["lep1_eta"] = { "central" };
  //central_or_shiftOptions_["lep2_conePt"] = { "central" };
  central_or_shiftOptions_["lep2_eta"] = { "central" };
  }

  if (histogramMakingLevel >= 2)
  {
    central_or_shiftOptions_["BDTOutput_500_spin2_vs_700_spin2"] = { "central" };
    central_or_shiftOptions_["BDTOutput_500_spin2_vs_900_spin2"] = { "central" };
    central_or_shiftOptions_["BDTOutput_700_spin2_vs_900_spin2"] = { "central" };
  }

  if ( makeBDTIpVarsPlotsWithFullSyst )
  {
    for(const std::string & bdtIpVar: bdtIpVars)
    {
      central_or_shiftOptions_[bdtIpVar] = { "*" };
    }
  }
  
}

const TH1 *
EvtHistManager_hh_2lss_leq1tau::getHistogram_EventCounter() const
{
  return histogram_EventCounter_;
}

void
EvtHistManager_hh_2lss_leq1tau::bookHistograms(TFileDirectory & dir)
{
  histogram_numElectrons_     = book1D(dir, "numElectrons",     "numElectrons",       5, -0.5,  +4.5);
  histogram_numMuons_         = book1D(dir, "numMuons",         "numMuons",           5, -0.5,  +4.5);
  histogram_numJets_          = book1D(dir, "numJets",          "numJets",           20, -0.5, +19.5);
  histogram_numJetsPtGt40_    = book1D(dir, "numJetsPtGt40",    "numJetsPtGt40",     20, -0.5, +19.5);
  histogram_dihiggsVisMass_   = book1D(dir, "dihiggsVisMass",   "dihiggsVisMass",   150,  0., 1500.);
  histogram_dihiggsMass_wMet_ = book1D(dir, "dihiggsMass_wMet", "dihiggsMass_wMet", 150,  0., 1500.);
  histogram_jetMass_          = book1D(dir, "jetMass",          "jetMass",          150,  0., 1500.);
  histogram_leptonPairMass_   = book1D(dir, "leptonPairMass",   "leptonPairMass",   100,  0.,  200.);
  histogram_electronPairMass_ = book1D(dir, "electronPairMass", "electronPairMass", 100,  0.,  200.);
  histogram_muonPairMass_     = book1D(dir, "muonPairMass",     "muonPairMass",     100,  0.,  200.);
  histogram_leptonPairCharge_ = book1D(dir, "leptonPairCharge", "leptonPairCharge",   5, -2.5,  +2.5);
  histogram_HT_               = book1D(dir, "HT",               "HT",               150,  0., 1500.);
  histogram_STMET_            = book1D(dir, "STMET",            "STMET",            150,  0., 1500.);
  histogram_EventCounter_     = book1D(dir, "EventCounter",     "EventCounter",       1, -0.5,  +0.5);


  histogram_nElectrons_in_2lss_  = book1D(dir, "nElectrons_in_2lss",     "nElectrons_in_2lss",   3, -0.5,2.5);
  histogram_dR_ll_               = book1D(dir, "dR_ll",     "dR_ll",                           100, 0,   7);
  histogram_dPhi_ll_             = book1D(dir, "dPhi_ll",     "dPhi_ll",                       100, 0, TMath::Pi());
  //
  histogram_nAK8_w2subjets_      = book1D(dir, "nAK8_w2subjets",     "nAK8_w2subjets",           8, -0.5,7.5);
  histogram_nWJets_selected_     = book1D(dir, "nWJets_selected",     "nWJets_selected",         8, -0.5,7.5);
  //
  histogram_mass_2j_fromW1_      = book1D(dir, "mass_2j_fromW1",     "mass_2j_fromW1",         200, 0,  600);
  histogram_mass_2j_fromW2_      = book1D(dir, "mass_2j_fromW2",     "mass_2j_fromW2",         200, 0,  600);
  histogram_dR_2j_fromW1_        = book1D(dir, "dR_2j_fromW1",     "dR_2j_fromW1",             100, 0,   7);
  histogram_dR_2j_fromW2_        = book1D(dir, "dR_2j_fromW2",     "dR_2j_fromW2",             100, 0,   7);
  //
  histogram_dR_Wjets_min_        = book1D(dir, "dR_Wjets_min",         "dR_Wjets_min",         100, 0,   7);
  histogram_dR_Wjets_max_        = book1D(dir, "dR_Wjets_max",         "dR_Wjets_max",         100, 0,   7);
  histogram_dR_l_Wjets_min_      = book1D(dir, "dR_l_Wjets_min",       "dR_l_Wjets_min",       100, 0,   7);
  histogram_dR_l_Wjets_max_      = book1D(dir, "dR_l_Wjets_max",       "dR_l_Wjets_max",       100, 0,   7);
  histogram_dR_l_AK4jets_min_    = book1D(dir, "dR_l_AK4jets_min",     "dR_l_AK4jets_min",     100, 0,   7);
  histogram_dR_l_AK4jets_max_    = book1D(dir, "dR_l_AK4jets_max",     "dR_l_AK4jets_max",     100, 0,   7);
  histogram_dR_l_leadWjet_min_   = book1D(dir, "dR_l_leadWjet_min",    "dR_l_leadWjet_min",    100, 0,   7);
  histogram_dR_l_leadWjet_max_   = book1D(dir, "dR_l_leadWjet_max",    "dR_l_leadWjet_max",    100, 0,   7);
  histogram_dR_l_leadAK4jet_min_ = book1D(dir, "dR_l_leadAK4jet_min",  "dR_l_leadAK4jet_min",  100, 0,   7);
  histogram_dR_l_leadAK4jet_max_ = book1D(dir, "dR_l_leadAK4jet_max",  "dR_l_leadAK4jet_max",  100, 0,   7);
  //
  histogram_met_                 = book1D(dir, "met",                  "met",                  150, 0,500);
  histogram_mht_                 = book1D(dir, "mht",                  "mht",                  150, 0,500);
  histogram_met_LD_              = book1D(dir, "met_LD",               "met_LD",               150, 0,500);

  histogram_mT_lep1_met_         = book1D(dir, "mT_lep1_met",          "mT_lep1_met",          150, 0,500);
  histogram_mT_lep2_met_         = book1D(dir, "mT_lep2_met",          "mT_lep2_met",          150, 0,500);
  
  histogram_eventCategory_       = book1D(dir, "eventCategory",        "eventCategory",          3, 0.5,3.5);

  histogram_nTaus_               = book1D(dir, "nTaus",                "nTaus",                  3, -0.5,2.5);

  histogram_mindr_lep1_jet_      = book1D(dir, "mindr_lep1_jet",       "mindr_lep1_jet",       100, 0,   7);
  histogram_mindr_lep2_jet_      = book1D(dir, "mindr_lep2_jet",       "mindr_lep2_jet",       100, 0,   7);
  histogram_lep1_conePt_         = book1D(dir, "lep1_conePt",          "lep1_conePt",          150, 0,300);
  histogram_lep2_conePt_         = book1D(dir, "lep2_conePt",          "lep2_conePt",          150, 0,300);
  
  if (histogramMakingLevel >= 2)
  {
  histogram_pT_ll_               = book1D(dir, "pT_ll",                "pT_ll",                150, 0,300);
  histogram_max_lep_eta_         = book1D(dir, "max_lep_eta",          "max_lep_eta",          100, 0,2.5);
  histogram_pT_llMEt_            = book1D(dir, "pT_llMEt",             "pT_llMEt",             200, 0,600);

  histogram_Smin_llMEt_          = book1D(dir, "Smin_llMEt",           "Smin_llMEt",           200, 0,600);
  //histogram_lep1_conePt_         = book1D(dir, "lep1_conePt",          "lep1_conePt",          150, 0,300);
  histogram_lep1_eta_            = book1D(dir, "lep1_eta",             "lep1_eta",             100,-2.5,2.5);
  //histogram_lep2_conePt_         = book1D(dir, "lep2_conePt",          "lep2_conePt",          150, 0,300);
  histogram_lep2_eta_            = book1D(dir, "lep2_eta",             "lep2_eta",             100,-2.5,2.5);  
  }

  
  if (histogramMakingLevel >= 1)
  {
    /*
    // /home/tolange/share/dataCardsHH_unblinding_v1/rawRootFiles/2lss/Run2/newProcName/rebinned_quantile/addSystFakeRates_hh_2lss_leq1tau_hh_2lss_leq1tau_SS_MVAOutput_SM.root 
    // nonResBDM[SM] binning: 30 [ 0, 0.19, 0.25, 0.3, 0.35, 0.39, 0.42, 0.46, 0.49, 0.52, 0.54, 0.57, 0.59, 0.61, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.93, 0.95, 1] 
    int nBins_nonResBDT_SM = 30;
    double binning_nonResBDT_SM[] = { 0, 0.19, 0.25, 0.3, 0.35, 0.39, 0.42, 0.46, 0.49, 0.52, 0.54, 0.57, 0.59, 0.61, 0.64, 0.66, 0.68, 0.7, 0.72, 0.74, 0.76, 0.78, 0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.93, 0.95, 1};

    hBDTOutput_500_spin2_vs_700_spin2_                      = book2D(dir, "BDTOutput_500_spin2_vs_700_spin2",                      "BDTOutput_500_spin2_vs_700_spin2",         nBins_nonResBDT_SM,binning_nonResBDT_SM,  nBins_nonResBDT_SM,binning_nonResBDT_SM);
    hBDTOutput_500_spin2_vs_900_spin2_                      = book2D(dir, "BDTOutput_500_spin2_vs_900_spin2",                      "BDTOutput_500_spin2_vs_900_spin2",         nBins_nonResBDT_SM,binning_nonResBDT_SM,  nBins_nonResBDT_SM,binning_nonResBDT_SM);
    hBDTOutput_700_spin2_vs_900_spin2_                      = book2D(dir, "BDTOutput_700_spin2_vs_900_spin2",                      "BDTOutput_700_spin2_vs_900_spin2",         nBins_nonResBDT_SM,binning_nonResBDT_SM,  nBins_nonResBDT_SM,binning_nonResBDT_SM);
    */
    
    hBDTOutput_500_spin2_vs_700_spin2_                      = book2D(dir, "BDTOutput_500_spin2_vs_700_spin2",                      "BDTOutput_500_spin2_vs_700_spin2",         100,0,1, 100,0,1);
    hBDTOutput_500_spin2_vs_900_spin2_                      = book2D(dir, "BDTOutput_500_spin2_vs_900_spin2",                      "BDTOutput_500_spin2_vs_900_spin2",         100,0,1, 100,0,1);
    hBDTOutput_700_spin2_vs_900_spin2_                      = book2D(dir, "BDTOutput_700_spin2_vs_900_spin2",                      "BDTOutput_700_spin2_vs_900_spin2",         100,0,1, 100,0,1);
  }
  
}

void
EvtHistManager_hh_2lss_leq1tau::fillHistograms(int numElectrons,
					       int numMuons,
					       int numJets,
					       int numJetsPtGt40,
					       double dihiggsVisMass,
					       double dihiggsMass_wMet,
					       double jetMass,
					       double leptonPairMass,
					       double electronPairMass,
					       double muonPairMass,
					       double leptonPairCharge,
					       double HT,
					       double STMET,
					       //
					       //
					       //
					       int nElectrons_in_2lss,
					       //leptonPairMass_sel,
					       //leptonPairCharge_sel,
					       double dR_ll,
					       double dPhi_ll,
					       //
					       //nAK4,
					       int nAK8_w2subjets,
					       int nWJets_selected,
					       //
					       double mass_2j_fromW1,
					       double mass_2j_fromW2,
					       double dR_2j_fromW1,
					       double dR_2j_fromW2,
					       //
					       double dR_Wjets_min,
					       double dR_Wjets_max,
					       double dR_l_Wjets_min,
					       double dR_l_Wjets_max,
					       double dR_l_AK4jets_min,
					       double dR_l_AK4jets_max,
					       double dR_l_leadWjet_min,
					       double dR_l_leadWjet_max,
					       double dR_l_leadAK4jet_min,
					       double dR_l_leadAK4jet_max,
					       //
					       double met,
					       double mht,
					       double met_LD,
					       //HT,
					       //STMET,
					       //
					       double mT_lep1_met,
					       double mT_lep2_met,
					       //
					       int eventCategory,
					       //
					       int nTaus,
					       //
					       //
					       double mindr_lep1_jet,
					       double mindr_lep2_jet,
					       double pT_ll,
					       double max_lep_eta,
					       double pT_llMEt,
					       double Smin_llMEt,
					       double lep1_conePt,
					       double lep1_eta,
					       double lep2_conePt,
					       double lep2_eta,
					       //
					       //
					       //
					       std::map<std::string, double> BDTOutput_Map_spin0,
					       std::map<std::string, double> BDTOutput_Map_spin2,
					       std::map<std::string, double> BDTOutput_Map_nonRes,
					       //
					       //		 					       
					       double evtWeight)
{
  const double evtWeightErr = 0.;
  fillWithOverFlow(histogram_numElectrons_,     numElectrons,     evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numMuons_,         numMuons,         evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJets_,          numJets,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_numJetsPtGt40_,    numJetsPtGt40,    evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dihiggsVisMass_,   dihiggsVisMass,   evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dihiggsMass_wMet_, dihiggsMass_wMet, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_jetMass_,          jetMass,          evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_leptonPairMass_,   leptonPairMass,   evtWeight, evtWeightErr);
  if ( electronPairMass > 0. ) {
    fillWithOverFlow(histogram_electronPairMass_, electronPairMass, evtWeight, evtWeightErr);
  }
  if ( muonPairMass > 0. ) {
    fillWithOverFlow(histogram_muonPairMass_,     muonPairMass,     evtWeight, evtWeightErr);
  }
  fillWithOverFlow(histogram_leptonPairCharge_, leptonPairCharge, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_HT_,               HT,               evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_STMET_,            STMET,            evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_EventCounter_,     0.,               evtWeight, evtWeightErr);




  fillWithOverFlow(histogram_nElectrons_in_2lss_, nElectrons_in_2lss, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dR_ll_, dR_ll, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_dPhi_ll_, dPhi_ll, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_nAK8_w2subjets_, nAK8_w2subjets, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_nWJets_selected_, nWJets_selected, evtWeight, evtWeightErr);
  //
  if (mass_2j_fromW1 > 0)
  fillWithOverFlow(histogram_mass_2j_fromW1_, mass_2j_fromW1, evtWeight, evtWeightErr);
  if (mass_2j_fromW2 > 0)
  fillWithOverFlow(histogram_mass_2j_fromW2_, mass_2j_fromW2, evtWeight, evtWeightErr);
  if (dR_2j_fromW1 > 0)
  fillWithOverFlow(histogram_dR_2j_fromW1_, dR_2j_fromW1, evtWeight, evtWeightErr);
  if (dR_2j_fromW2 > 0)
  fillWithOverFlow(histogram_dR_2j_fromW2_, dR_2j_fromW2, evtWeight, evtWeightErr);
  //
  if (dR_Wjets_min > 0)
  fillWithOverFlow(histogram_dR_Wjets_min_, dR_Wjets_min, evtWeight, evtWeightErr);
  if (dR_Wjets_max > 0)
  fillWithOverFlow(histogram_dR_Wjets_max_, dR_Wjets_max, evtWeight, evtWeightErr);
  if (dR_l_Wjets_min > 0)
  fillWithOverFlow(histogram_dR_l_Wjets_min_, dR_l_Wjets_min, evtWeight, evtWeightErr);
  if (dR_l_Wjets_max > 0)
  fillWithOverFlow(histogram_dR_l_Wjets_max_, dR_l_Wjets_max, evtWeight, evtWeightErr);
  if (dR_l_AK4jets_min > 0)
  fillWithOverFlow(histogram_dR_l_AK4jets_min_, dR_l_AK4jets_min, evtWeight, evtWeightErr);
  if (dR_l_AK4jets_max > 0)
  fillWithOverFlow(histogram_dR_l_AK4jets_max_, dR_l_AK4jets_max, evtWeight, evtWeightErr);
  if (dR_l_leadWjet_min > 0)
  fillWithOverFlow(histogram_dR_l_leadWjet_min_, dR_l_leadWjet_min, evtWeight, evtWeightErr);
  if (dR_l_leadWjet_max > 0)
  fillWithOverFlow(histogram_dR_l_leadWjet_max_, dR_l_leadWjet_max, evtWeight, evtWeightErr);
  if (dR_l_leadAK4jet_min > 0)
  fillWithOverFlow(histogram_dR_l_leadAK4jet_min_, dR_l_leadAK4jet_min, evtWeight, evtWeightErr);
  if (dR_l_leadAK4jet_max > 0)
  fillWithOverFlow(histogram_dR_l_leadAK4jet_max_, dR_l_leadAK4jet_max, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_met_, met, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mht_, mht, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_met_LD_, met_LD, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_mT_lep1_met_, mT_lep1_met, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mT_lep2_met_, mT_lep2_met, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_eventCategory_, eventCategory, evtWeight, evtWeightErr);
  //
  fillWithOverFlow(histogram_nTaus_, nTaus, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_mindr_lep1_jet_, mindr_lep1_jet, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_mindr_lep2_jet_, mindr_lep2_jet, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_conePt_, lep1_conePt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_conePt_, lep2_conePt, evtWeight, evtWeightErr);
  
  if (histogramMakingLevel >= 2)
  {
  fillWithOverFlow(histogram_pT_ll_, pT_ll, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_max_lep_eta_, max_lep_eta, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_pT_llMEt_, pT_llMEt, evtWeight, evtWeightErr);

  fillWithOverFlow(histogram_Smin_llMEt_, Smin_llMEt, evtWeight, evtWeightErr);
  //fillWithOverFlow(histogram_lep1_conePt_, lep1_conePt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep1_eta_, lep1_eta, evtWeight, evtWeightErr);
  //fillWithOverFlow(histogram_lep2_conePt_, lep2_conePt, evtWeight, evtWeightErr);
  fillWithOverFlow(histogram_lep2_eta_, lep2_eta, evtWeight, evtWeightErr);  
  }

  if (histogramMakingLevel >= 2)
  {
    fillWithOverFlow2d(hBDTOutput_500_spin2_vs_700_spin2_,  BDTOutput_Map_spin2["500_spin2"], BDTOutput_Map_spin2["700_spin2"],  evtWeight, evtWeightErr);
    fillWithOverFlow2d(hBDTOutput_500_spin2_vs_900_spin2_,  BDTOutput_Map_spin2["500_spin2"], BDTOutput_Map_spin2["900_spin2"],  evtWeight, evtWeightErr);
    fillWithOverFlow2d(hBDTOutput_700_spin2_vs_900_spin2_,  BDTOutput_Map_spin2["700_spin2"], BDTOutput_Map_spin2["900_spin2"],  evtWeight, evtWeightErr);
  
  }  
}
