#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h"

#include "hhAnalysis/multilepton/interface/Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger.h"
#include "hhAnalysis/multilepton/interface/Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger.h"

#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_1l_1tau_trigger.h"
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h"
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h"
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h"
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"

EvtWeightRecorderHH::EvtWeightRecorderHH()
  : EvtWeightRecorder()
{}

EvtWeightRecorderHH::EvtWeightRecorderHH(const std::vector<std::string> & central_or_shifts,
                                         const std::string & central_or_shift,
                                         bool isMC, 
                                         bool isDEBUG)
  : EvtWeightRecorder(central_or_shifts, central_or_shift, isMC, isDEBUG)
{}

double
EvtWeightRecorderHH::get_tauSF(const std::string & central_or_shift) const
{
  double tauSF_weight = EvtWeightRecorder::get_tauSF(central_or_shift);
  if(isMC_)
  {
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    if(weights_SF_hadTau_third_.count(jetToTauFakeRate_option))
    {
      tauSF_weight *= weights_SF_hadTau_third_.at(jetToTauFakeRate_option);
    }
    if(weights_SF_hadTau_fourth_.count(jetToTauFakeRate_option))
    {
      tauSF_weight *= weights_SF_hadTau_fourth_.at(jetToTauFakeRate_option);
    }
  }
  return tauSF_weight;
}

void
EvtWeightRecorderHH::record_tauTriggerEff(const Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger * const dataToMCcorrectionInterface_hh_0l_4tau_trigger)
{
  assert(isMC_);
  weights_tauTriggerEff_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const TriggerSFsys triggerSF_option = getTriggerSF_option(central_or_shift, TriggerSFsysChoice::hadTauOnly);
    if(weights_tauTriggerEff_.count(triggerSF_option))
    {
      continue;
    }
    weights_tauTriggerEff_[triggerSF_option] = dataToMCcorrectionInterface_hh_0l_4tau_trigger->getSF_triggerEff(triggerSF_option);
  }
}

void
EvtWeightRecorderHH::record_tauTriggerEff(const Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger * const dataToMCcorrectionInterface_hh_1l_3tau_trigger)
{
  assert(isMC_);
  weights_tauTriggerEff_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const TriggerSFsys triggerSF_option = getTriggerSF_option(central_or_shift, TriggerSFsysChoice::hadTauOnly);
    if(weights_tauTriggerEff_.count(triggerSF_option))
    {
      continue;
    }
    weights_tauTriggerEff_[triggerSF_option] = dataToMCcorrectionInterface_hh_1l_3tau_trigger->getSF_triggerEff(triggerSF_option);
  }
}

void
EvtWeightRecorderHH::record_tauTriggerEff(const Data_to_MC_CorrectionInterface_1l_1tau_trigger * const dataToMCcorrectionInterface_1l_1tau_trigger)
{
  return EvtWeightRecorder::record_tauTriggerEff(dataToMCcorrectionInterface_1l_1tau_trigger);
}

void
EvtWeightRecorderHH::record_jetToTau_FR_third(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                                              const RecoHadTau * const hadTau_third)
{
  const double hadTauPt_third = hadTau_third->pt();
  const double hadTauAbsEta_third = hadTau_third->absEta();
  weights_FR_hadTau_third_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    if(weights_FR_hadTau_third_.count(jetToTauFakeRate_option))
    {
      continue;
    }
    weights_FR_hadTau_third_[jetToTauFakeRate_option] = jetToTauFakeRateInterface->getWeight_third(
      hadTauPt_third, hadTauAbsEta_third, jetToTauFakeRate_option
    );
  }
}

void
EvtWeightRecorderHH::record_jetToTau_FR_fourth(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                                               const RecoHadTau * const hadTau_fourth)
{
  const double hadTauPt_fourth = hadTau_fourth->pt();
  const double hadTauAbsEta_fourth = hadTau_fourth->absEta();
  weights_FR_hadTau_fourth_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    if(weights_FR_hadTau_fourth_.count(jetToTauFakeRate_option))
    {
      continue;
    }
    weights_FR_hadTau_fourth_[jetToTauFakeRate_option] = jetToTauFakeRateInterface->getWeight_fourth(
      hadTauPt_fourth, hadTauAbsEta_fourth, jetToTauFakeRate_option
    );
  }
}

void
EvtWeightRecorderHH::record_jetToTau_SF_third(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                                             const RecoHadTau * const hadTau_third)
{
  assert(isMC_);
  const double hadTauPt_third = hadTau_third->pt();
  const double hadTauAbsEta_third = hadTau_third->absEta();
  weights_SF_hadTau_third_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    if(weights_SF_hadTau_third_.count(jetToTauFakeRate_option))
    {
      continue;
    }
    weights_SF_hadTau_third_[jetToTauFakeRate_option] = jetToTauFakeRateInterface->getSF_third(
      hadTauPt_third, hadTauAbsEta_third, jetToTauFakeRate_option
    );
  }
}

void
EvtWeightRecorderHH::record_jetToTau_SF_fourth(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                                               const RecoHadTau * const hadTau_fourth)
{
  assert(isMC_);
  const double hadTauPt_fourth = hadTau_fourth->pt();
  const double hadTauAbsEta_fourth = hadTau_fourth->absEta();
  weights_SF_hadTau_fourth_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    if(weights_SF_hadTau_fourth_.count(jetToTauFakeRate_option))
    {
      continue;
    }
    weights_SF_hadTau_fourth_[jetToTauFakeRate_option] = jetToTauFakeRateInterface->getSF_fourth(
      hadTauPt_fourth, hadTauAbsEta_fourth, jetToTauFakeRate_option
    );
  }
}


void
EvtWeightRecorderHH::compute_FR_4tau(bool passesTight_hadTau_lead,
                                     bool passesTight_hadTau_sublead,
                                     bool passesTight_hadTau_third,
                                     bool passesTight_hadTau_fourth)
{
  assert(! weights_FR_hadTau_lead_.empty());
  assert(! weights_FR_hadTau_sublead_.empty());
  assert(! weights_FR_hadTau_third_.empty());
  assert(! weights_FR_hadTau_fourth_.empty());
  weights_FR_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToLeptonFakeRate_option = getJetToLeptonFR_option(central_or_shift);
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    assert(weights_FR_hadTau_lead_.count(jetToTauFakeRate_option));
    assert(weights_FR_hadTau_sublead_.count(jetToTauFakeRate_option));
    assert(weights_FR_hadTau_third_.count(jetToTauFakeRate_option));
    assert(weights_FR_hadTau_fourth_.count(jetToTauFakeRate_option));
    const std::string weightKey = jetToLeptonFakeRate_option == kFRl_central && jetToTauFakeRate_option == kFRjt_central ? "central" : central_or_shift;
    if(weights_FR_.count(weightKey))
    {
      continue;
    }
    weights_FR_[weightKey] = getWeight_4L(
      weights_FR_hadTau_lead_.at(jetToTauFakeRate_option),    passesTight_hadTau_lead,
      weights_FR_hadTau_sublead_.at(jetToTauFakeRate_option), passesTight_hadTau_sublead,
      weights_FR_hadTau_third_.at(jetToTauFakeRate_option),   passesTight_hadTau_third,
      weights_FR_hadTau_fourth_.at(jetToTauFakeRate_option),  passesTight_hadTau_fourth
    );
  }
}

void
EvtWeightRecorderHH::compute_FR_1l3tau(bool passesTight_lepton,
                                       bool passesTight_hadTau_lead,
                                       bool passesTight_hadTau_sublead,
                                       bool passesTight_hadTau_third)
{
  assert(! weights_FR_lepton_lead_.empty());
  assert(! weights_FR_hadTau_lead_.empty());
  assert(! weights_FR_hadTau_sublead_.empty());
  assert(! weights_FR_hadTau_third_.empty());
  weights_FR_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToLeptonFakeRate_option = getJetToLeptonFR_option(central_or_shift);
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    assert(weights_FR_lepton_lead_.count(jetToLeptonFakeRate_option));
    assert(weights_FR_hadTau_lead_.count(jetToTauFakeRate_option));
    assert(weights_FR_hadTau_sublead_.count(jetToTauFakeRate_option));
    assert(weights_FR_hadTau_third_.count(jetToTauFakeRate_option));
    const std::string weightKey = jetToLeptonFakeRate_option == kFRl_central && jetToTauFakeRate_option == kFRjt_central ? "central" : central_or_shift;
    if(weights_FR_.count(weightKey))
    {
      continue;
    }
    weights_FR_[weightKey] = getWeight_4L(
      weights_FR_lepton_lead_.at(jetToLeptonFakeRate_option), passesTight_lepton,
      weights_FR_hadTau_lead_.at(jetToTauFakeRate_option),    passesTight_hadTau_lead,
      weights_FR_hadTau_sublead_.at(jetToTauFakeRate_option), passesTight_hadTau_sublead,
      weights_FR_hadTau_third_.at(jetToTauFakeRate_option),   passesTight_hadTau_third
    );
  }
}

void
EvtWeightRecorderHH::compute_FR_3tau(bool passesTight_hadTau_lead,
                                     bool passesTight_hadTau_sublead,
                                     bool passesTight_hadTau_third)
{
  assert(! weights_FR_hadTau_lead_.empty());
  assert(! weights_FR_hadTau_sublead_.empty());
  assert(! weights_FR_hadTau_third_.empty());
  weights_FR_.clear();
  for(const std::string & central_or_shift: central_or_shifts_)
  {
    const int jetToLeptonFakeRate_option = getJetToLeptonFR_option(central_or_shift);
    const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
    assert(weights_FR_hadTau_lead_.count(jetToTauFakeRate_option));
    assert(weights_FR_hadTau_sublead_.count(jetToTauFakeRate_option));
    assert(weights_FR_hadTau_third_.count(jetToTauFakeRate_option));
    const std::string weightKey = jetToLeptonFakeRate_option == kFRl_central && jetToTauFakeRate_option == kFRjt_central ? "central" : central_or_shift;
    if(weights_FR_.count(weightKey))
    {
      continue;
    }
    weights_FR_[weightKey] = getWeight_3L(
      weights_FR_hadTau_lead_.at(jetToTauFakeRate_option),    passesTight_hadTau_lead,
      weights_FR_hadTau_sublead_.at(jetToTauFakeRate_option), passesTight_hadTau_sublead,
      weights_FR_hadTau_third_.at(jetToTauFakeRate_option),   passesTight_hadTau_third
    );
  }
}

double
EvtWeightRecorderHH::get_jetToTau_FR_third(const std::string & central_or_shift)
{
  assert(! weights_FR_hadTau_third_.empty());
  const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
  assert(weights_FR_hadTau_third_.count(jetToTauFakeRate_option));
  return weights_FR_hadTau_third_.at(jetToTauFakeRate_option);
}

double
EvtWeightRecorderHH::get_jetToTau_FR_fourth(const std::string & central_or_shift)
{
  assert(! weights_FR_hadTau_fourth_.empty());
  const int jetToTauFakeRate_option = getJetToTauFR_option(central_or_shift);
  assert(weights_FR_hadTau_fourth_.count(jetToTauFakeRate_option));
  return weights_FR_hadTau_fourth_.at(jetToTauFakeRate_option);
}
