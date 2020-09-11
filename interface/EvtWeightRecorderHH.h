#ifndef hhAnalysis_multilepton_EvtWeightRecorder_h
#define hhAnalysis_multilepton_EvtWeightRecorder_h

#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightRecorder.h" // EvtWeightRecorder

// forward declarations
class Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger;
class Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger;

class EvtWeightRecorderHH
  : public virtual EvtWeightRecorder
{
public:
  EvtWeightRecorderHH();
  EvtWeightRecorderHH(const std::vector<std::string> & central_or_shifts,
                      const std::string & central_or_shift,
                      bool isMC, 
                      bool isDEBUG = false);

  double
  get_tauSF(const std::string & central_or_shift) const override;

  void
  record_tauTriggerEff(const Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger * const dataToMCcorrectionInterface_hh_0l_4tau_trigger);

  void
  record_tauTriggerEff(const Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger * const dataToMCcorrectionInterface_hh_1l_3tau_trigger);

  void
  record_tauTriggerEff(const Data_to_MC_CorrectionInterface_1l_1tau_trigger * const dataToMCcorrectionInterface_1l_1tau_trigger);

  void
  record_jetToTau_FR_third(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                           const RecoHadTau * const hadTau_third);

  void
  record_jetToTau_FR_fourth(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                            const RecoHadTau * const hadTau_fourth);

  void
  record_jetToTau_SF_third(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                           const RecoHadTau * const hadTau_third);

  void
  record_jetToTau_SF_fourth(const JetToTauFakeRateInterface * const jetToTauFakeRateInterface,
                            const RecoHadTau * const hadTau_fourth);

  void
  compute_FR_4tau(bool passesTight_hadTau_lead,
                  bool passesTight_hadTau_sublead,
                  bool passesTight_hadTau_third,
                  bool passesTight_hadTau_fourth);

  void
  compute_FR_1l3tau(bool passesTight_lepton,
                    bool passesTight_hadTau_lead,
                    bool passesTight_hadTau_sublead,
                    bool passesTight_hadTau_third);

  void
  compute_FR_3tau(bool passesTight_hadTau_lead,
                  bool passesTight_hadTau_sublead,
                  bool passesTight_hadTau_third);

  double
  get_jetToTau_FR_third(const std::string & central_or_shift);

  double
  get_jetToTau_FR_fourth(const std::string & central_or_shift);

protected:
  std::map<int, double> weights_FR_hadTau_third_;
  std::map<int, double> weights_FR_hadTau_fourth_;
  std::map<int, double> weights_SF_hadTau_third_;
  std::map<int, double> weights_SF_hadTau_fourth_;
};

#endif
