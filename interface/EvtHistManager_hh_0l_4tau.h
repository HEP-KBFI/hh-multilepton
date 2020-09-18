#ifndef hhAnalysis_multilepton_EvtHistManager_hh_0l_4tau_h
#define hhAnalysis_multilepton_EvtHistManager_hh_0l_4tau_h

/** \class EvtHistManager_hh_0l_4tau
 *
 * Book and fill histograms for event-level quantities in the 0l+4tau_h category 
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

class EvtHistManager_hh_0l_4tau
  : public HistManagerBase
{
public:
  EvtHistManager_hh_0l_4tau(const edm::ParameterSet & cfg);
  ~EvtHistManager_hh_0l_4tau() {}

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
          unsigned int evt_number,
          double evtWeight);

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
  TH1 * histogram_EventNumber_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_SUM_spin2_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_SUM_spin0_;
  std::map<std::string, TH1*> histogram_Map_BDTOutput_SUM_nonres_;

  std::vector<string> labels_spin2_;
  std::vector<string> labels_spin0_;
  std::vector<string> labels_nonres_;
};

#endif
