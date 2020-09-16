#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h" // RecoElectronSelectorFakeable_hh_multilepton

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // Era::k*
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"         // cmsException(), assert()

RecoElectronSelectorFakeable_hh_multilepton::RecoElectronSelectorFakeable_hh_multilepton(Era era,
                                                           int index,
                                                           bool debug,
                                                           bool set_selection_flags)
  : era_(era)
  , debug_(debug)
  , set_selection_flags_(set_selection_flags)
  , apply_offline_e_trigger_cuts_(true)
  , min_lepton_pt_(7.) // L
  , min_cone_pt_(10.) // F
  , max_absEta_(2.5) // L
  , max_dxy_(0.05) // L
  , max_dz_(0.1) // L
  , max_relIso_(0.4) // L
  , max_sip3d_(8.) // L
  , binning_absEta_(1.479) // F
  , min_sigmaEtaEta_trig_(0.011) // F
  , max_sigmaEtaEta_trig_(0.019) // F
  , max_HoE_trig_(0.10) // F
  , min_OoEminusOoP_trig_(-0.04) // F
  , min_jetPtRatio_(1. / 1.7) // F
  , max_jetBtagCSV_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium)) // F
  , apply_conversionVeto_(true) // F
  , max_nLostHits_(0) // F
  , useAssocJetBtag_(false)
{
  // L -- inherited from the preselection (loose cut)
  // F -- additional fakeable cut not applied in the preselection
}

void
RecoElectronSelectorFakeable_hh_multilepton::enable_offline_e_trigger_cuts()
{
  apply_offline_e_trigger_cuts_ = true;
}

void
RecoElectronSelectorFakeable_hh_multilepton::disable_offline_e_trigger_cuts()
{
  apply_offline_e_trigger_cuts_ = false;
}

void
RecoElectronSelectorFakeable_hh_multilepton::set_min_lepton_pt(double min_lepton_pt)
{
  min_lepton_pt_ = min_lepton_pt;
}

void
RecoElectronSelectorFakeable_hh_multilepton::set_min_cone_pt(double min_cone_pt)
{
  min_cone_pt_ = min_cone_pt;
}

void
RecoElectronSelectorFakeable_hh_multilepton::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoElectronSelectorFakeable_hh_multilepton::set_selection_flags(bool selection_flags)
{
  set_selection_flags_ = selection_flags;
}

void
RecoElectronSelectorFakeable_hh_multilepton::set_assocJetBtag(bool flag)
{
  useAssocJetBtag_ = flag;
}

double
RecoElectronSelectorFakeable_hh_multilepton::get_min_lepton_pt() const
{
  return min_lepton_pt_;
}

double
RecoElectronSelectorFakeable_hh_multilepton::get_min_cone_pt() const
{
  return min_cone_pt_;
}

double
RecoElectronSelectorFakeable_hh_multilepton::get_max_absEta() const
{
  return max_absEta_;
}

bool
RecoElectronSelectorFakeable_hh_multilepton::operator()(const RecoElectron & electron) const
{
  if(debug_)
  {
    std::cout << get_human_line(this, __func__) << ":\n" << electron;
  }

  if(electron.cone_pt() < min_cone_pt_)
  {
    if(debug_)
    {
      std::cout << "FAILS cone pT = " << electron.cone_pt() << " >= " << min_cone_pt_ << " fakeable cut\n";
    }
    return false;
  }

  if(electron.lepton_pt() < min_lepton_pt_)
  {
    if(debug_)
    {
      std::cout << "FAILS pT = " << electron.pt() << " >= " << min_lepton_pt_ << " fakeable cut\n";
    }
  }

  if(electron.absEta() > max_absEta_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(eta) = " << electron.absEta() << " <= " << max_absEta_ << " fakeable cut\n";
    }
    return false;
  }

  if(std::fabs(electron.dxy()) > max_dxy_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(dxy) = " << std::fabs(electron.dxy()) << " <= " << max_dxy_ << " fakeable cut\n";
    }
    return false;
  }

  if(std::fabs(electron.dz()) > max_dz_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(dz) = " << std::fabs(electron.dz()) << " <= " << max_dz_ << " fakeable cut\n";
    }
    return false;
  }

  if(electron.relIso() > max_relIso_)
  {
    if(debug_)
    {
      std::cout << "FAILS relIso = " << electron.relIso() << " <= " << max_relIso_ << " fakeable cut\n";
    }
    return false;
  }

  if(electron.sip3d() > max_sip3d_)
  {
    if(debug_)
    {
      std::cout << "FAILS sip3d = " << electron.sip3d() << " <= " << max_sip3d_ << " fakeable cut\n";
    }
    return false;
  }

  if(electron.nLostHits() > max_nLostHits_)
  {
    if(debug_)
    {
      std::cout << "FAILS nLostHits = " << electron.nLostHits() << " <= " << max_nLostHits_ << " fakeable cut\n";
    }
    return false;
  }

  if(! electron.passesConversionVeto() && apply_conversionVeto_)
  {
    if(debug_)
    {
      std::cout << "FAILS conversion veto fakeable cut\n";
    }
    return false;
  }

  if(! electron.mvaID_POG(EGammaWP::WPL))
  {
    if(debug_)
    {
      std::cout << "FAILS loose EGamma POG MVA fakeable cut\n";
    }
    return false;
  }


  if (electron.mvaRawTTH() > electron.mvaRawTTH_cut()) {
    if(electron.jetBtagCSV(useAssocJetBtag_) > max_jetBtagCSV_)
      {
	if(debug_)
	  {
	    std::cout << "FAILS jetBtagCSV = " << electron.jetBtagCSV(useAssocJetBtag_) << " <= " << max_jetBtagCSV_ << " fakeable cut\n";
	  }
	return false;
      }
  }

  
  if(apply_offline_e_trigger_cuts_)
  {
    const double max_sigmaEtaEta_trig = min_sigmaEtaEta_trig_ +
                                        max_sigmaEtaEta_trig_ * (electron.absEtaSC() > binning_absEta_);
    if(electron.sigmaEtaEta() > max_sigmaEtaEta_trig)
    {
      if(debug_)
      {
        std::cout << "FAILS sigmaEtaEta = " << electron.sigmaEtaEta() << " <= " << max_sigmaEtaEta_trig << " fakeable cut\n";
      }
      return false;
    }

    if(electron.HoE() > max_HoE_trig_)
    {
      if(debug_)
      {
        std::cout << "FAILS HoE = " << electron.HoE() << " <= " << max_HoE_trig_ << " fakeable cut\n";
      }
      return false;
    }
    if(electron.OoEminusOoP() < min_OoEminusOoP_trig_)
    {
      if(debug_)
      {
        std::cout << "FAILS OoEminusOoP = " << electron.OoEminusOoP() << " >= " << min_OoEminusOoP_trig_ << " fakeable cut\n";
      }
      return false;
    }
  }

  if(set_selection_flags_)
  {
    electron.set_isFakeable();
  }

  return true;
}

RecoElectronCollectionSelectorFakeable_hh_multilepton::RecoElectronCollectionSelectorFakeable_hh_multilepton(Era era,
                                                                               int index,
                                                                               bool debug,
                                                                               bool set_selection_flags)
  : ParticleCollectionSelector<RecoElectron, RecoElectronSelectorFakeable_hh_multilepton>(era, index, debug)
{
  selector_.set_selection_flags(set_selection_flags);
}

void
RecoElectronCollectionSelectorFakeable_hh_multilepton::enable_offline_e_trigger_cuts()
{
  selector_.enable_offline_e_trigger_cuts();
}

void
RecoElectronCollectionSelectorFakeable_hh_multilepton::disable_offline_e_trigger_cuts()
{
  selector_.disable_offline_e_trigger_cuts();
}
