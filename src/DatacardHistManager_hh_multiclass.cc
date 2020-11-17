#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh_multiclass.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h"   // format_vdouble(), format_vstring()

DatacardHistManager_hh_multiclass::DatacardHistManager_hh_multiclass(const edm::ParameterSet & cfg,
                                                                     const AnalysisConfig_hh & analysisConfig, 
                                                                     const EventInfo & eventInfo, 
                                                                     const HHWeightInterface2 * HHWeight_calc,
                                                                     const std::vector<std::string> & classes,
                                                                     bool isDEBUG)
  : DatacardHistManagerBase_hh(cfg, analysisConfig, eventInfo, HHWeight_calc, isDEBUG)
{
  // CV: define one event category for each class;
  //     then fill histograms for all event categories so defined
  int category = 0;
  for ( auto classIter: classes )
  {
    categories_.push_back(category);
    classToCategoryMap_[classIter] = category;
    ++category;
  }

  initialize();
}

DatacardHistManager_hh_multiclass::DatacardHistManager_hh_multiclass(const edm::ParameterSet & cfg,
                                                                     const AnalysisConfig_hh & analysisConfig, 
                                                                     const EventInfo & eventInfo, 
                                                                     const HHWeightInterface2 * HHWeight_calc,
                                                                     const EventCategory_multiclass * eventCategory,
                                                                     bool isDEBUG)
  : DatacardHistManagerBase_hh(cfg, analysisConfig, eventInfo, HHWeight_calc, eventCategory, isDEBUG)
  , eventCategory_(eventCategory)
{
  // CV: fill histograms for all event categories defined in EventCategoryBase object
  categories_ = eventCategory_->categories();

  initialize();
}

namespace
{
  std::map<std::string, std::pair<std::string, double>> // key = gen_mHH/bmName; value = class, mvaOutput
  unpackMVAOutputMap(const std::map<std::string, std::map<std::string, double>>& mvaOutputs)
  {
    std::map<std::string, std::pair<std::string, double>> mvaOutputs_unpacked;
    for ( std::map<std::string, std::map<std::string, double>>::const_iterator classIter = mvaOutputs.begin();
          classIter != mvaOutputs.end(); ++classIter ) {
      for ( std::map<std::string, double>::const_iterator gen_mHH_or_bmName = classIter->second.begin(); 
            gen_mHH_or_bmName != classIter->second.end(); ++gen_mHH_or_bmName ) {
        const std::string & key = gen_mHH_or_bmName->first;
        if ( mvaOutputs_unpacked.find(key) == mvaOutputs_unpacked.end() || gen_mHH_or_bmName->second > mvaOutputs_unpacked[key].second )
        {
          mvaOutputs_unpacked[key] = std::pair<std::string, double>(classIter->first, gen_mHH_or_bmName->second);
        }
      }
    }
    return mvaOutputs_unpacked;
  }

  std::vector<std::string>
  get_keys(const std::map<std::string, std::pair<std::string, double>> & mvaOutputs)
  {
    std::vector<std::string> keys;
    for ( const auto & mvaOutput : mvaOutputs )
    {
      keys.push_back(mvaOutput.first);
    }
    return keys;
  } 
}

void
DatacardHistManager_hh_multiclass::fillHistograms(const std::map<std::string, std::map<std::string, double>> & mvaOutputs_resonant_spin2,
                                                  const std::map<std::string, std::map<std::string, double>> & mvaOutputs_resonant_spin0,
                                                  const std::map<std::string, std::map<std::string, double>> & mvaOutputs_nonresonant,
                                                  double evtWeight)
{
  const double evtWeightErr = 0.;

  std::map<std::string, std::pair<std::string, double>> mvaOutputs_resonant_spin2_unpacked = unpackMVAOutputMap(mvaOutputs_resonant_spin2);
  std::map<std::string, std::pair<std::string, double>> mvaOutputs_resonant_spin0_unpacked = unpackMVAOutputMap(mvaOutputs_resonant_spin0);
  std::map<std::string, std::pair<std::string, double>> mvaOutputs_nonresonant_unpacked = unpackMVAOutputMap(mvaOutputs_nonresonant);

  compHHReweightMap();
 
  for ( const auto & decayMode : decayModes_ )
  {
    if (! ( decayMode == "*" ||
          (analysisConfig_.isMC_HH() && decayMode == eventInfo_.getDiHiggsDecayModeString()) ||
          (analysisConfig_.isMC_H()  && decayMode == eventInfo_.getDecayModeString())        ))
    {
      continue;
    }
    for ( const auto & productionMode : productionModes_ )
    {
      if ( ! ( productionMode == "*" ||
               (analysisConfig_.isMC_VH() && productionMode == eventInfo_.getProductionModeString()) ))
      {
        continue;
      }
      for ( std::vector<categoryEntryType>::iterator categoryEntry = histograms_in_categories_.begin();
            categoryEntry != histograms_in_categories_.end(); ++categoryEntry ) {
        for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin2_.begin();
              histogramName != histogramNames_mvaOutput_resonant_spin2_.end(); ++histogramName ) {
          const std::string & key_resonant_spin2 = histogramName->first;
          TH1* histogram = categoryEntry->histograms_mvaOutput_resonant_spin2_[productionMode][decayMode][key_resonant_spin2];
          std::map<std::string, std::pair<std::string, double>>::const_iterator mvaOutput = mvaOutputs_resonant_spin2_unpacked.find(key_resonant_spin2);
          if ( mvaOutput == mvaOutputs_resonant_spin2_unpacked.end() )
            throw cmsException(this, __func__, __LINE__)
              << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
              << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_resonant_spin2_unpacked)) << ")\n";
          const std::string & for_class = mvaOutput->second.first;
          if ( isSelected(categoryEntry->category_, for_class) )
          {
            fillWithOverFlow(histogram, mvaOutput->second.second, evtWeight, evtWeightErr);
          }
        }
        for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin0_.begin();
              histogramName != histogramNames_mvaOutput_resonant_spin0_.end(); ++histogramName ) {
          const std::string & key_resonant_spin0 = histogramName->first;
          TH1* histogram = categoryEntry->histograms_mvaOutput_resonant_spin0_[productionMode][decayMode][key_resonant_spin0];
          std::map<std::string, std::pair<std::string, double>>::const_iterator mvaOutput = mvaOutputs_resonant_spin0_unpacked.find(key_resonant_spin0);
          if ( mvaOutput == mvaOutputs_resonant_spin0_unpacked.end() )
            throw cmsException(this, __func__, __LINE__)
              << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
              << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_resonant_spin0_unpacked)) << ")\n";
          const std::string & for_class = mvaOutput->second.first;
          if ( isSelected(categoryEntry->category_, for_class) )
          {
            fillWithOverFlow(histogram, mvaOutput->second.second, evtWeight, evtWeightErr);
          }
        }

        for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_nonresonant_.begin();
              histogramName != histogramNames_mvaOutput_nonresonant_.end(); ++histogramName ) {
          const std::string & key_nonresonant = histogramName->first;
          TH1* histogram = categoryEntry->histograms_mvaOutput_nonresonant_[productionMode][decayMode][key_nonresonant];
          std::map<std::string, std::pair<std::string, double>>::const_iterator mvaOutput = mvaOutputs_nonresonant_unpacked.find(key_nonresonant);
          if ( mvaOutput == mvaOutputs_nonresonant_unpacked.end() )
            throw cmsException(this, __func__, __LINE__)
              << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
              << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_nonresonant_unpacked)) << ")\n";
          const std::string & for_class = mvaOutput->second.first;
          if ( isSelected(categoryEntry->category_, for_class) )
          {
            double evtWeight_reweighted = evtWeight;
            double evtWeightErr_reweighted = evtWeightErr;
            if ( analysisConfig_.isMC_HH_nonresonant() && apply_HH_rwgt_ )
            {
              const std::string& bmName = histogramName->first;
              std::map<std::string, double>::const_iterator HHReweight = HHReweightMap_.find(bmName);
              assert(HHReweight != HHReweightMap_.end());
              evtWeight_reweighted *= HHReweight->second;
              evtWeightErr_reweighted *= HHReweight->second;
            }
            fillWithOverFlow(histogram, mvaOutput->second.second, evtWeight_reweighted, evtWeightErr_reweighted);
          }
        }
      }
    }
  }
}

bool
DatacardHistManager_hh_multiclass::isSelected(int for_category, const std::string & for_class) const
{
  if ( eventCategory_ )
  {
    return eventCategory_->isSelected(for_category, for_class);
  }
  else
  {
    std::map<std::string, int>::const_iterator classToCategoryIter = classToCategoryMap_.find(for_class);
    assert(classToCategoryIter != classToCategoryMap_.end());
    if ( classToCategoryIter->second == for_category ) return true;
    else return false;
  }
}
