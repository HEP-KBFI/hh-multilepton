#ifndef hhAnalysis_multilepton_DatacardHistManagerBase_hh_h
#define hhAnalysis_multilepton_DatacardHistManagerBase_hh_h

/** \class DatacardHistManagerBase_hh
 *
 * Base class for DatacardHistManager and DatacardHistManager_multiclass
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h"      // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h"            // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLO.h"  // HHWeightInterfaceLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceNLO.h" // HHWeightInterfaceNLO
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h"       // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/EventCategoryBase.h"       // EventCategoryBase

#include <string>
#include <vector>
#include <map>
//#include<boost/any.hpp>
#include<boost/variant.hpp>

using namespace std;

class DatacardHistManagerBase_hh
  : public HistManagerBase
{
 public:
  DatacardHistManagerBase_hh(const edm::ParameterSet & cfg,
                             const AnalysisConfig_hh & analysisConfig, 
                             const EventInfo & eventInfo, 
                             const HHWeightInterfaceLO * HHWeightLO_calc,
                             const HHWeightInterfaceNLO * HHWeightNLO_calc,
                             bool isDEBUG = false,
                             bool fillHistograms_nonresonant = true, bool fillHistograms_resonant_spin0 = true, bool fillHistograms_resonant_spin2 = true, bool overlap=false, bool use2d=false);
  DatacardHistManagerBase_hh(const edm::ParameterSet & cfg,
                             const AnalysisConfig_hh & analysisConfig, 
                             const EventInfo & eventInfo, 
                             const HHWeightInterfaceLO * HHWeightLO_calc,
                             const HHWeightInterfaceNLO * HHWeightNLO_calc,
                             const EventCategoryBase * eventCategoryBase,
                             bool isDEBUG = false,
                             bool fillHistograms_nonresonant = true, bool fillHistograms_resonant_spin0 = true, bool fillHistograms_resonant_spin2 = true, bool overlap = false, bool use2d=false);
  ~DatacardHistManagerBase_hh() {}

  /// book histograms
  void
  bookHistograms(TFileDirectory & dir) override;

 protected:
  void
  initialize();

  void
  compHHReweightMap();

  const AnalysisConfig_hh & analysisConfig_;
  const EventInfo & eventInfo_;
  const HHWeightInterfaceLO * HHWeightLO_calc_;
  bool apply_HH_rwgt_lo_;
  const HHWeightInterfaceNLO * HHWeightNLO_calc_;
  bool apply_HH_rwgt_nlo_;
  std::map<std::string, double> HHReweightMap_;
  const EventCategoryBase * eventCategoryBase_;
  std::vector<int> categories_;

  bool fillHistograms_nonresonant_;
  bool fillHistograms_resonant_spin0_;
  bool fillHistograms_resonant_spin2_;

  std::vector<double> resonant_gen_mHH_;
  std::vector<std::string> nonresonant_BMs_;
  std::vector<std::string> decayModes_;
  std::map<std::string, std::vector<std::string>> decayModeMap_;      // key = "_tttt"/"_wwww"/"_wwtt"/"_bbtt"/"_bbvv"
  std::vector<std::string> productionModes_;
  std::map<std::string, std::vector<std::string>> productionModeMap_; // key = "WH"/"ZH"

  std::map<std::string, std::string> histogramNames_mvaOutput_resonant_spin2_; // key = gen_mHH + "_spin2", value = histogramName
  std::map<std::string, std::string> histogramNames_mvaOutput_resonant_spin0_; // key = gen_mHH + "_spin0", value = histogramName
  std::map<std::string, std::string> histogramNames_mvaOutput_nonresonant_;    // key = bmName, value = histogramName
  std::string histogramName_mvaOutput_nonresonant_allBMs_;

  int numBinsX_;
  double xMin_;
  double xMax_;

  struct categoryEntryType
  {
    // key = prduction and decay mode ("*" for data and background), histogramName
    std::map<std::string, std::map<std::string, std::map<std::string, boost::variant<TH1*, TH2*>>>> histograms_mvaOutput_resonant_spin2_; // keys = productionMode, decayMode, gen_mHH + "_spin2"
    std::map<std::string, std::map<std::string, std::map<std::string, boost::variant<TH1*, TH2*>>>> histograms_mvaOutput_resonant_spin0_; // keys = productionMode, decayMode, gen_mHH + "_spin0"
    std::map<std::string, std::map<std::string, std::map<std::string, boost::variant<TH1*, TH2*>>>> histograms_mvaOutput_nonresonant_;    // keys = productionMode, decayMode, bmName
    std::map<std::string, std::map<std::string, TH1*>> histograms_mvaOutput_nonresonant_allBMs_;                    // keys = productionMode, decayMode
    int category_;
  };
  std::vector<categoryEntryType> histograms_in_categories_;

  bool overlap_;
  bool use2d_;
  bool isDEBUG_;
};

#endif
