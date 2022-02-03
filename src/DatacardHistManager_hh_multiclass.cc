#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh_multiclass.h"

#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"          // cmsException
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow()
#include "tthAnalysis/HiggsToTauTau/interface/generalAuxFunctions.h"   // format_vdouble(), format_vstring()
#include<boost/variant.hpp>

DatacardHistManager_hh_multiclass::DatacardHistManager_hh_multiclass(const edm::ParameterSet & cfg,
                                                                     const AnalysisConfig_hh & analysisConfig, 
                                                                     const EventInfo & eventInfo, 
                                                                     const HHWeightInterfaceLO * HHWeightLO_calc,
                                                                     const HHWeightInterfaceNLO * HHWeightNLO_calc,
                                                                     const std::vector<std::string> & classes,
                                                                     bool isDEBUG,
                                                                     bool fillHistograms_nonresonant, bool fillHistograms_resonant_spin0, bool fillHistograms_resonant_spin2, bool overlap, bool use2d)
  : DatacardHistManagerBase_hh(
      cfg, analysisConfig, eventInfo, HHWeightLO_calc, HHWeightNLO_calc, isDEBUG, 
      fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2, overlap,
      use2d
    )
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
                                                                     const HHWeightInterfaceLO * HHWeightLO_calc,
                                                                     const HHWeightInterfaceNLO * HHWeightNLO_calc,
                                                                     const EventCategory_multiclass * eventCategory,
                                                                     bool isDEBUG,
                                                                     bool fillHistograms_nonresonant, bool fillHistograms_resonant_spin0, bool fillHistograms_resonant_spin2, bool overlap, bool use2d)
  : DatacardHistManagerBase_hh(
      cfg, analysisConfig, eventInfo, HHWeightLO_calc, HHWeightNLO_calc, eventCategory, isDEBUG,
      fillHistograms_nonresonant, fillHistograms_resonant_spin0, fillHistograms_resonant_spin2, overlap,
      use2d
    )
  , eventCategory_(eventCategory)
{
  // CV: fill histograms for all event categories defined in EventCategoryBase object
  categories_ = eventCategory_->categories();
  initialize();
}

namespace
{
  std::pair<std::string, double> // value = class, mvaOutput
  unpackMVAOutputMap(const std::map<std::string, double>& mvaOutputs)
  {
    std::pair<std::string, double> mvaOutputs_unpacked;
    bool isFirst = true;
    for ( std::map<std::string, double>::const_iterator classIter = mvaOutputs.begin(); 
          classIter != mvaOutputs.end(); ++classIter ) {
      if ( isFirst || classIter->second > mvaOutputs_unpacked.second )
      {
        mvaOutputs_unpacked = std::pair<std::string, double>(classIter->first, classIter->second);
        isFirst = false;
      }
    }
    return mvaOutputs_unpacked;
  }

  std::map<std::string, std::pair<std::string, double>> // key = gen_mHH/bmName; value = class, mvaOutput
  unpackMVAOutputMap(const std::map<std::string, std::map<std::string, double>>& mvaOutputs)
  {
    std::map<std::string, std::pair<std::string, double>> mvaOutputs_unpacked;
    for ( std::map<std::string, std::map<std::string, double>>::const_iterator gen_mHH_or_bmName = mvaOutputs.begin();
          gen_mHH_or_bmName != mvaOutputs.end(); ++gen_mHH_or_bmName ) {
      for ( std::map<std::string, double>::const_iterator classIter = gen_mHH_or_bmName->second.begin(); 
            classIter != gen_mHH_or_bmName->second.end(); ++classIter ) {
        //if ( gen_mHH_or_bmName->first == "SM" )
        //{
        //  std::cout << classIter->first << " = " << classIter->second << std::endl;
        //}
        const std::string & key = gen_mHH_or_bmName->first;
        if ( mvaOutputs_unpacked.find(key) == mvaOutputs_unpacked.end() || classIter->second > mvaOutputs_unpacked[key].second )
        {
          mvaOutputs_unpacked[key] = std::pair<std::string, double>(classIter->first, classIter->second);
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
                                                  const std::map<std::string, double> & mvaOutputs_nonresonant_allBMs,
                                                  double mhh_analytic,
                                                  double evtWeight)
{
  const double evtWeightErr = 0.;

  std::map<std::string, std::pair<std::string, double>> mvaOutputs_resonant_spin2_unpacked = unpackMVAOutputMap(mvaOutputs_resonant_spin2);
  std::map<std::string, std::pair<std::string, double>> mvaOutputs_resonant_spin0_unpacked = unpackMVAOutputMap(mvaOutputs_resonant_spin0);
  std::map<std::string, std::pair<std::string, double>> mvaOutputs_nonresonant_unpacked = unpackMVAOutputMap(mvaOutputs_nonresonant);
  std::pair<std::string, double> mvaOutput_nonresonant_allBMs_unpacked = unpackMVAOutputMap(mvaOutputs_nonresonant_allBMs);

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
        if ( fillHistograms_resonant_spin2_ )
        {
          for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin2_.begin();
                histogramName != histogramNames_mvaOutput_resonant_spin2_.end(); ++histogramName ) {
            const std::string & key_resonant_spin2 = histogramName->first;
            boost::variant<TH1*, TH2*> histogram = categoryEntry->histograms_mvaOutput_resonant_spin2_[productionMode][decayMode][key_resonant_spin2];
            std::map<std::string, std::pair<std::string, double>>::const_iterator mvaOutput = mvaOutputs_resonant_spin2_unpacked.find(key_resonant_spin2);
            if ( mvaOutput == mvaOutputs_resonant_spin2_unpacked.end() )
              throw cmsException(this, __func__, __LINE__)
                << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
                << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_resonant_spin2_unpacked)) << ")\n";
            const std::string & for_class = mvaOutput->second.first;
            if ( isSelected(categoryEntry->category_, for_class, false) )
            {
              if(for_class.find("HH") !=std::string::npos && use2d_) {
                TH2* histogram_2d = boost::get<TH2*>(histogram);
                fillWithOverFlow2d(histogram_2d, mvaOutput->second.second, mhh_analytic, evtWeight, evtWeightErr);
              }
              else {
                TH1* histogram_1d = boost::get<TH1*>(histogram);
                fillWithOverFlow(histogram_1d, mvaOutput->second.second, evtWeight, evtWeightErr);
              }
            }
          }
        }
        if ( fillHistograms_resonant_spin0_ )
        {
          for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_resonant_spin0_.begin();
                histogramName != histogramNames_mvaOutput_resonant_spin0_.end(); ++histogramName ) {
            const std::string & key_resonant_spin0 = histogramName->first;
            boost::variant<TH1*, TH2*> histogram = categoryEntry->histograms_mvaOutput_resonant_spin0_[productionMode][decayMode][key_resonant_spin0];
            std::map<std::string, std::pair<std::string, double>>::const_iterator mvaOutput = mvaOutputs_resonant_spin0_unpacked.find(key_resonant_spin0);
            if ( mvaOutput == mvaOutputs_resonant_spin0_unpacked.end() )
              throw cmsException(this, __func__, __LINE__)
                << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
                << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_resonant_spin0_unpacked)) << ")\n";
            const std::string & for_class = mvaOutput->second.first;
            if ( isSelected(categoryEntry->category_, for_class, false) )
            {
              if(for_class.find("HH") !=std::string::npos && use2d_) {
                TH2* histogram_2d = boost::get<TH2*>(histogram);
                fillWithOverFlow2d(histogram_2d, mvaOutput->second.second, mhh_analytic, evtWeight, evtWeightErr);
              }
              else {
                TH1* histogram_1d = boost::get<TH1*>(histogram);
                fillWithOverFlow(histogram_1d, mvaOutput->second.second, evtWeight, evtWeightErr);
              }
            }
          }
        }
        if ( fillHistograms_nonresonant_ )
        {
          for ( std::map<std::string, std::string>::const_iterator histogramName = histogramNames_mvaOutput_nonresonant_.begin();
                histogramName != histogramNames_mvaOutput_nonresonant_.end(); ++histogramName ) {
            const std::string & key_nonresonant = histogramName->first;
            boost::variant<TH1*, TH2*> histogram = categoryEntry->histograms_mvaOutput_nonresonant_[productionMode][decayMode][key_nonresonant];
            TH1* histogram_boost = boost::get<TH1*>(histogram);
            std::map<std::string, std::pair<std::string, double>>::const_iterator mvaOutput = mvaOutputs_nonresonant_unpacked.find(key_nonresonant);
            if ( mvaOutput == mvaOutputs_nonresonant_unpacked.end() )
              throw cmsException(this, __func__, __LINE__)
                << "No MVA output provided to fill histogram = '" << histogramName->second << "' !!\n"
                << "(available MVA outputs = " << format_vstring(get_keys(mvaOutputs_nonresonant_unpacked)) << ")\n";
            const std::string & for_class = mvaOutput->second.first;
            if ( isSelected(categoryEntry->category_, for_class, true) )
            {
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
              fillWithOverFlow(histogram_boost, mvaOutput->second.second, evtWeight_reweighted, evtWeightErr_reweighted);
            }
          }
          const std::string & for_class = mvaOutput_nonresonant_allBMs_unpacked.first;
          if ( isSelected(categoryEntry->category_, for_class, true) )
          {
            TH1* histogram = categoryEntry->histograms_mvaOutput_nonresonant_allBMs_[productionMode][decayMode];
            fillWithOverFlow(histogram, mvaOutput_nonresonant_allBMs_unpacked.second, evtWeight, evtWeightErr);
          }
        }
      }
    }
  }
}

bool
DatacardHistManager_hh_multiclass::isSelected(int for_category, const std::string & for_class, bool isNonRes) const
{
  if ( eventCategory_ )
  {
    return eventCategory_->isSelected(for_category, for_class, isNonRes);
  }
  else
  {
    std::map<std::string, int>::const_iterator classToCategoryIter = classToCategoryMap_.find(for_class);
    assert(classToCategoryIter != classToCategoryMap_.end());
    if ( classToCategoryIter->second == for_category ) return true;
    else return false;
  }
}
