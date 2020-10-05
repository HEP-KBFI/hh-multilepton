#ifndef hhAnalysis_multilepton_EvtHistManager_hh_3l_1tau_h
#define hhAnalysis_multilepton_EvtHistManager_hh_3l_1tau_h

/** \class EvtHistManager_hh_3l_1tau
 *
 * Book and fill histograms for event-level quantities in the 1l+3tau_h category 
 * of the HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult


#include <vector>
#include <map>

using namespace std; 

class EvtHistManager_hh_3l_1tau
  : public HistManagerBase
{
public:
  EvtHistManager_hh_3l_1tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_3l_1tau() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(int numElectrons,
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
		 double m_ltau_closestTo,
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
		 std::map<std::string, double>& BDTOutput_SUM_Map,
		 std::map<std::string, double>& BDTOutput_nonRes_SUM_Map,
		 //std::map<std::string, double>& XGBOutput_SUM_Map,
		 unsigned int evt_number
);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_numJetsPtGt40_;
  TH1 * histogram_numBJets_loose_;
  TH1 * histogram_numBJets_medium_;

  TH1 * histogram_dihiggsVisMass_;
  TH1 * histogram_dihiggsMass_;

  TH1 * histogram_HT_;
  TH1 * histogram_STMET_;
  
  TH1 * histogram_EventCounter_;

  TH1 * histogram_HTMiss_;
  TH1 * histogram_MET_;
  TH1 * histogram_MET_LD_;
  TH1 * histogram_mT_nonZlepMET_;
  TH1 * histogram_mT_SSlephigh_;
  TH1 * histogram_mT_SSleplow_;
  TH1 * histogram_mT_SSlepdR_;
  TH1 * histogram_mllOS_closestToZ_;
  TH1 * histogram_SVFit_h1_visMass_; 
  TH1 * histogram_SVFit_h2_visMass_;
  TH1 * histogram_SVFit_h1_pT_; 
  TH1 * histogram_SVFit_h2_pT_; 
  TH1 * histogram_SVFit_hh_deltaPhi_; 
  TH1 * histogram_SVFit_hh_deltaEta_;
  TH1 * histogram_SVFit_hh_deltaR_;
  TH1 * histogram_SVFit_hh_pT_;
  TH1 * histogram_SVFit_hh_cosTheta_;
  TH1 * histogram_m_ltau_minltaupair_;
  TH1 * histogram_pT_ltau_minltaupair_;
  TH1 * histogram_dR_ltau_minltaupair_;
  TH1 * histogram_dEta_ltau_minltaupair_;
  TH1 * histogram_dPhi_ltau_minltaupair_;
  TH1 * histogram_m_ll_minltaupair_;
  TH1 * histogram_pT_ll_minltaupair_;
  TH1 * histogram_dR_ll_minltaupair_;
  TH1 * histogram_dEta_ll_minltaupair_;
  TH1 * histogram_dPhi_ll_minltaupair_;
  TH1 * histogram_m_ltau_minllpair_;
  TH1 * histogram_pT_ltau_minllpair_;
  TH1 * histogram_dR_ltau_minllpair_;
  TH1 * histogram_dEta_ltau_minllpair_;
  TH1 * histogram_dPhi_ltau_minllpair_;
  TH1 * histogram_m_ll_minllpair_;
  TH1 * histogram_pT_ll_minllpair_;
  TH1 * histogram_dR_ll_minllpair_;
  TH1 * histogram_dEta_ll_minllpair_;
  TH1 * histogram_dPhi_ll_minllpair_;
  TH1 * histogram_mlll_;
  TH1 * histogram_mAll_;
  TH1 * histogram_dr_los1_;
  TH1 * histogram_dr_los2_;
  TH1 * histogram_m_OS_etau_closestToZ_;
  TH1 * histogram_m_etau_closestToZ_;
  TH1 * histogram_trigger_eTauZVezto_;
  TH1 * histogram_triggerECalCrackVeto_;
  TH1 * histogram_triggerBadTauVeto_;
  TH1 * histogram_m_ltau_closestToZ_;
  TH1 * histogram_m_OS_ltau_closestToZ_;
  TH1 * histogram_tau_antiElectron_matched_;
  TH1 * histogram_tau_antiElectron_unmatched_;
  TH1 * histogram_dR_smartpair1_;
  TH1 * histogram_dR_smartpair2_;
  TH1 * histogram_dR_smartpair_ll_;
  TH1 * histogram_dR_smartpair_ltau_;
  TH1 * histogram_dPhi_smartpair1_;
  TH1 * histogram_dPhi_smartpair2_;
  TH1 * histogram_dPhi_smartpair_ll_;
  TH1 * histogram_dPhi_smartpair_ltau_;
  TH1 * histogram_dEta_smartpair1_;
  TH1 * histogram_dEta_smartpair2_;
  TH1 * histogram_dEta_smartpair_ll_;
  TH1 * histogram_dEta_smartpair_ltau_;
  TH1 * histogram_pT_smartpair1_;
  TH1 * histogram_pT_smartpair2_;
  TH1 * histogram_pT_smartpair_ll_;
  TH1 * histogram_pT_smartpair_ltau_;
  TH1 * histogram_pTSum_smartpair1_;
  TH1 * histogram_pTSum_smartpair2_;
  TH1 * histogram_pTSum_smartpair_ll_;
  TH1 * histogram_pTSum_smartpair_ltau_;
  TH1 * histogram_pTDiff_smartpair1_;
  TH1 * histogram_pTDiff_smartpair2_;
  TH1 * histogram_pTDiff_smartpair_ll_;
  TH1 * histogram_pTDiff_smartpair_ltau_;
  TH1 * histogram_nSFOS_;
  TH1 * histogram_mZ_tau_;
  TH1 * histogram_dPhi_nonZlMET_;
  TH1 * histogram_mindPhiLepMET_;
  TH1 * histogram_pT4l_;
  TH1 * histogram_EventNumber_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_SUM_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_nonRes_SUM_;
  //std::map<std::string, TH1*> histogram_Map_XGBOutput_SUM_;
   
  std::vector<string> labels_;
  std::vector<string> labels_nonRes_;
  //std::vector<string> XGB_labels_;
  
};

#endif
