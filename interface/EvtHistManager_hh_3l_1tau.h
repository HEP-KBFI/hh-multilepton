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
);

  const TH1 *
  getHistogram_EventCounter() const;

 private:
  TH1 * histogram_numElectrons_;
  TH1 * histogram_numMuons_;
  TH1 * histogram_numHadTaus_;
  TH1 * histogram_numJets_;
  TH1 * histogram_MET_;
  TH1 * histogram_nSFOS_;
  TH1 * histogram_HT_;
  TH1 * histogram_MET_LD_;
  TH1 * histogram_lep1_pt_;
  TH1 * histogram_dihiggsVisMass_;
  TH1 * histogram_dihiggsMass_;
  TH1 * histogram_dR_smartpair_ltau_;
  TH1 * histogram_m_smartpair_ltau_;
  TH1 * histogram_dR_smartpair_ll_;
  TH1 * histogram_m_smartpair_ll_;
  TH1 * histogram_mllOS_closestToZ_;
  TH1 * histogram_mT_SSlepdR_;
  TH1 * histogram_maxdZ_lep_;
  TH1 * histogram_mindPhiLepMET_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_spin2_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_spin0_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_nonRes_;
  TH1 * histogram_EventCounter_;
  TH1 * histogram_EventNumber_;
  std::vector<string> labels_spin2_;
  std::vector<string> labels_spin0_;
  std::vector<string> labels_nonres_;
};

#endif
