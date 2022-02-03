#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h"   // format_vdouble(), format_vstring()
#include<boost/variant.hpp>

DatacardHistManager_hh::DatacardHistManager_hh(const edm::ParameterSet & cfg,
                                               const AnalysisConfig_hh & analysisConfig, 
                                               const EventInfo & eventInfo, 
                                               const HHWeightInterfaceLO * HHWeightLO_calc,
                                               const HHWeightInterfaceNLO * HHWeightNLO_calc,
                                               bool isDEBUG,
                                               bool fillHistograms_nonresonant, bool fillHistograms_resonant_spin0, bool fillHistograms_resonant_spin2, bool overlap)
  : DatacardHistManagerBase_hh(
      cfg, analysisConfig, eventInfo, HHWeightLO_calc, HHWeightNLO_calc, isDEBUG, 
      fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2, overlap
    )
  , eventCategory_(nullptr)
{
  // CV: fill histograms for inclusive event category
  categories_ = { -1 };

  initialize();
}

DatacardHistManager_hh::DatacardHistManager_hh(const edm::ParameterSet & cfg,
                                               const AnalysisConfig_hh & analysisConfig, 
                                               const EventInfo & eventInfo, 
                                               const HHWeightInterfaceLO * HHWeightLO_calc,
                                               const HHWeightInterfaceNLO * HHWeightNLO_calc,
                                               const EventCategory * eventCategory,
                                               bool isDEBUG,
                                               bool fillHistograms_nonresonant, bool fillHistograms_resonant_spin0, bool fillHistograms_resonant_spin2, bool overlap)
  : DatacardHistManagerBase_hh(
      cfg, analysisConfig, eventInfo, HHWeightLO_calc, HHWeightNLO_calc, eventCategory, isDEBUG, 
      fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2, overlap
    )
  , eventCategory_(eventCategory)
{
  // CV: fill histograms for all event categories defined in EventCategory object
  categories_ = eventCategory->categories();

  initialize();
}

namespace
{
  std::vector<std::string>
  get_keys(const std::map<std::string, double> & mvaOutputs)
  {
    std::vector<std::string> keys;
    for ( const auto & mvaOutput: mvaOutputs )
    {
      keys.push_back(mvaOutput.first);
    }
    return keys;
  } 
}

void
DatacardHistManager_hh::fillHistograms(const std::map<std::string, double> & mvaOutputs_resonant_spin2,
                                       const std::map<std::string, double> & mvaOutputs_resonant_spin0,
                                       const std::map<std::string, double> & mvaOutputs_nonresonant,
                                       double mvaOutput_nonresonant_allBMs,
                                       double evtWeight)
{
  const double evtWeightErr = 0.;

  compHHReweightMap();

  for ( std::vector<categoryEntryType>::iterator categoryEntry = histograms_in_categories_.begin(); 
        categoryEntry != histograms_in_categories_.end(); ++categoryEntry ) {
    if ( categoryEntry->category_ != -1 )
    {
      assert(eventCategory_);
      if ( !eventCategory_->isSelected(categoryEntry->category_) ) continue;
    }
    for ( const auto & decayMode: decayModes_ )
    {
      if (! ( decayMode == "*" ||
            (analysisConfig_.isMC_HH() && decayMode == eventInfo_.getDiHiggsDecayModeString()) ||
            (analysisConfig_.isMC_H()  && decayMode == eventInfo_.getDecayModeString())        ))
      {
        continue;
      }
      for ( const auto & productionMode: productionModes_ )
      {
        if ( ! ( productionMode == "*" ||
                 (analysisConfig_.isMC_VH() && productionMode == eventInfo_.getProductionModeString()) ))
        {
          continue;
        }
        if ( fillHistograms_resonant_spin2_ )
        {
          for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin2_.begin();
                histogramName != histogramNames_mvaOutput_resonant_spin2_.end(); ++histogramName ) {
            const std::string & key_resonant_spin2 = histogramName->first;
            boost::variant<TH1*, TH2*> histogram = categoryEntry->histograms_mvaOutput_resonant_spin2_[productionMode][decayMode][key_resonant_spin2];
            std::map<std::string, double>::const_iterator mvaOutput = mvaOutputs_resonant_spin2.find(key_resonant_spin2);
            if ( mvaOutput == mvaOutputs_resonant_spin2.end() )
              throw cmsException(this, __func__, __LINE__)
                << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
                << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_resonant_spin2)) << ")\n";
            TH1* histogram_boost = boost::get<TH1*>(histogram);
            fillWithOverFlow(histogram_boost, mvaOutput->second, evtWeight, evtWeightErr);
          }
        }
        if ( fillHistograms_resonant_spin0_ )
        {
          for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin0_.begin();
                histogramName != histogramNames_mvaOutput_resonant_spin0_.end(); ++histogramName ) {
            const std::string & key_resonant_spin0 = histogramName->first;
            boost::variant<TH1*, TH2*> histogram = categoryEntry->histograms_mvaOutput_resonant_spin0_[productionMode][decayMode][key_resonant_spin0];
            std::map<std::string, double>::const_iterator mvaOutput = mvaOutputs_resonant_spin0.find(key_resonant_spin0);
            if ( mvaOutput == mvaOutputs_resonant_spin0.end() )
              throw cmsException(this, __func__, __LINE__)
                << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
                << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_resonant_spin0)) << ")\n";
            TH1* histogram_boost = boost::get<TH1*>(histogram);
            fillWithOverFlow(histogram_boost, mvaOutput->second, evtWeight, evtWeightErr);
          }
        }

        if ( fillHistograms_nonresonant_ )
        {
          for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_nonresonant_.begin();
                histogramName != histogramNames_mvaOutput_nonresonant_.end(); ++histogramName ) {
            const std::string & key_nonresonant = histogramName->first;
            boost::variant<TH1*, TH2*> histogram = categoryEntry->histograms_mvaOutput_nonresonant_[productionMode][decayMode][key_nonresonant];
            TH1* histogram_boost = boost::get<TH1*>(histogram);
            std::map<std::string, double>::const_iterator mvaOutput = mvaOutputs_nonresonant.find(key_nonresonant);
            if ( mvaOutput == mvaOutputs_nonresonant.end() )
              throw cmsException(this, __func__, __LINE__)
                << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
                << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_nonresonant)) << ")\n";
            double evtWeight_reweighted = evtWeight;
            double evtWeightErr_reweighted = evtWeightErr;
            if ( analysisConfig_.isMC_HH_nonresonant() && (apply_HH_rwgt_lo_ || apply_HH_rwgt_nlo_) )
            {
              const std::string& bmName = histogramName->first;
              std::map<std::string, double>::const_iterator HHReweight = HHReweightMap_.find(bmName);
              assert(HHReweight != HHReweightMap_.end());
              evtWeight_reweighted *= HHReweight->second;
              evtWeightErr_reweighted *= HHReweight->second;
            }
            fillWithOverFlow(histogram_boost, mvaOutput->second, evtWeight_reweighted, evtWeightErr_reweighted);
          }
          TH1* histogram = categoryEntry->histograms_mvaOutput_nonresonant_allBMs_[productionMode][decayMode];
          fillWithOverFlow(histogram, mvaOutput_nonresonant_allBMs, evtWeight, evtWeightErr);
        }
      }
    }
  }
}
