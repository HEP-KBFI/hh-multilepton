#ifndef hhAnalysis_multilepton_EvtHistManager_hh_1l_3tau_h
#define hhAnalysis_multilepton_EvtHistManager_hh_1l_3tau_h

/** \class EvtHistManager_hh_1l_3tau
 *
 * Book and fill histograms for event-level quantities in the 1l+3tau_h category 
 * of the HH->tttt, WWtt, and WWWW analysis 
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h"      // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h"      // RecoHadTau

#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult


#include <vector>
#include <map>

using namespace std;

class EvtHistManager_hh_1l_3tau
  : public HistManagerBase
{
public:
  EvtHistManager_hh_1l_3tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_1l_3tau() {}

  /// book and fill histograms
  void
  bookHistograms(TFileDirectory & dir) override;

  void
  fillHistograms(
          int numElectrons,
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
          std::map<std::string, double>& BDTOutput_SUM_Map_spin2,
          std::map<std::string, double>& BDTOutput_SUM_Map_spin0,
          std::map<std::string, double>& BDTOutput_SUM_Map_nonres,
          const RecoLepton* selLepton,
          const RecoHadTau* selHadTau_lead,
          const RecoHadTau* selHadTau_sublead,
          const RecoHadTau* selHadTau_third,
          int numTightLeptons,
          int numFakeableHadTaus_passingElecVeto,
          int numTightHadTaus,
          int numTightHadTaus_passingElecVeto,
          bool isMC,
          double evtWeight
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
  std::map<std::string, TH1*> histogram_Map_BDTOutput_SUM_spin2_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_SUM_spin0_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_SUM_nonres_;

  std::vector<string> labels_spin2_;
  std::vector<string> labels_spin0_;
  std::vector<string> labels_nonres_;

  // CV: plots specific to 1e+3tau category
  TH1 * histogram_1e3tau_tau1_OS_antiE_OS_matched_;
  TH1 * histogram_1e3tau_tau1_OS_antiE_OS_unmatched_;
  TH1 * histogram_1e3tau_tau2_OS_antiE_OS_matched_;
  TH1 * histogram_1e3tau_tau2_OS_antiE_OS_unmatched_;
  TH1 * histogram_1e3tau_tau3_OS_antiE_OS_matched_;
  TH1 * histogram_1e3tau_tau3_OS_antiE_OS_unmatched_;
  TH1 * histogram_1e3tau_mass_etau_OS_closestToZ_;
  TH1 * histogram_1e3tau_tau1_OS_eta_;
  TH1 * histogram_1e3tau_tau2_OS_eta_;
  TH1 * histogram_1e3tau_tau3_OS_eta_;
  TH1 * histogram_1e3tau_numTightLeptons_;
  TH1 * histogram_1e3tau_numFakeableTaus_passingElecVeto_;
  TH1 * histogram_1e3tau_numTightTaus_;
  TH1 * histogram_1e3tau_numTightTaus_passingElecVeto_;
  TH1 * histogram_1e3tau_numTightLeptons_and_Taus_;
  TH1 * histogram_1e3tau_evtWeight_;

  // CV: plots specific to 1mu+3tau category
  TH1 * histogram_1mu3tau_numTightLeptons_;
  TH1 * histogram_1mu3tau_numFakeableTaus_passingElecVeto_;
  TH1 * histogram_1mu3tau_numTightTaus_;
  TH1 * histogram_1mu3tau_numTightTaus_passingElecVeto_;
  TH1 * histogram_1mu3tau_numTightLeptons_and_Taus_;
  TH1 * histogram_1mu3tau_evtWeight_;
};

#endif
