#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic.h" // RecoElectronSelectorFakeable_hh_multilepton_Dynamic

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // Era::k*
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"         // cmsException(), assert()

RecoElectronSelectorFakeable_hh_multilepton_Dynamic::RecoElectronSelectorFakeable_hh_multilepton_Dynamic(Era era,
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
  , min_jetPtRatio_(1. / 2.9) // F   // default 1. / 1.7
  , max_jetBtagCSV_forFakeable_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kTight)) // F
  , max_jetBtagCSV_forTight_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium)) // F        
  , apply_conversionVeto_(true) // F
  , max_nLostHits_(0) // F
  , useAssocJetBtag_(false)
{
  // L -- inherited from the preselection (loose cut)
  // F -- additional fakeable cut not applied in the preselection
}

void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::enable_offline_e_trigger_cuts()
{
  apply_offline_e_trigger_cuts_ = true;
}

void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::disable_offline_e_trigger_cuts()
{
  apply_offline_e_trigger_cuts_ = false;
}

void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_min_lepton_pt(double min_lepton_pt)
{
  min_lepton_pt_ = min_lepton_pt;
}

void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_min_cone_pt(double min_cone_pt)
{
  min_cone_pt_ = min_cone_pt;
}

void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_selection_flags(bool selection_flags)
{
  set_selection_flags_ = selection_flags;
}

void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_assocJetBtag(bool flag)
{
  useAssocJetBtag_ = flag;
}

double
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::get_min_lepton_pt() const
{
  return min_lepton_pt_;
}

double
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::get_min_cone_pt() const
{
  return min_cone_pt_;
}

double
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::get_max_absEta() const
{
  return max_absEta_;
}

bool
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::operator()(const RecoElectron & electron) const
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

  if(electron.mvaRawTTH() > electron.mvaRawTTH_cut()) {
    if(electron.jetBtagCSV(useAssocJetBtag_) > max_jetBtagCSV_forTight_)
    {
      if(debug_)
      {
	std::cout << "FAILS jetBtagCSV = " << electron.jetBtagCSV(useAssocJetBtag_) << " <= " << max_jetBtagCSV_forTight_ << " fakeable cut\n";
      }
      return false;
    }
  }

  if(electron.mvaRawTTH() <= electron.mvaRawTTH_cut())
  {
    if(electron.jetBtagCSV(useAssocJetBtag_) > max_jetBtagCSV_forFakeable_)
    {
      if(debug_)
      {
	std::cout << "FAILS jetBtagCSV = " << electron.jetBtagCSV(useAssocJetBtag_) << " <= " << max_jetBtagCSV_forFakeable_ << " fakeable cut\n";
      }
      return false;
    }    
    if(electron.jetPtRatio() < min_jetPtRatio_)
    {
      if(debug_)
      {
        std::cout << "FAILS jetPtRatio = " << electron.jetPtRatio() << " >= " << min_jetPtRatio_ << " fakeable cut\n";
      }
      return false;
    }
    
    bool passPOG_WP_forFakeable = false;
    if      (pod_wp_forFakeable_.compare("WP-L")  == 0) {
      passPOG_WP_forFakeable = electron.mvaID_POG(EGammaWP::WPL);
    } else if (pod_wp_forFakeable_.compare("WP-90") == 0) {
      passPOG_WP_forFakeable = electron.mvaID_POG(EGammaWP::WP90);
    } else if (pod_wp_forFakeable_.compare("WP-80") == 0) {
      passPOG_WP_forFakeable = electron.mvaID_POG(EGammaWP::WP80);
    }    
    if(! passPOG_WP_forFakeable)
    {
      if(debug_)
      {
        std::cout << "FAILS 80% EGamma POG MVA fakeable cut\n";
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




void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_POGID_forFakeable(std::string pog_wp) {
  pod_wp_forFakeable_ = pog_wp; // "WP-L", "WP-90", "WP-80"
  std::cout << "RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_POGID_forFakeable() pod_wp_forFakeable_: " << pod_wp_forFakeable_ << std::endl;
}


void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_jetBtagCSV_ID_forFakeable(std::string sjetBtagCSV_ID_forFakeable) {
  std::string jetBtagCSV_ID_forFakeable_ = sjetBtagCSV_ID_forFakeable;
  
  if (jetBtagCSV_ID_forFakeable_.compare("WP-L") == 0) {
    max_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kLoose));
  }
  if (jetBtagCSV_ID_forFakeable_.compare("WP-M") == 0) {
    max_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium));
  }
  if (jetBtagCSV_ID_forFakeable_.compare("WP-T") == 0) {
    max_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kTight));
  }
  if (jetBtagCSV_ID_forFakeable_.compare("WP-NoCut") == 0) {
    max_jetBtagCSV_forFakeable_ = 1.0;
  }
  std::cout << "RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_jetBtagCSV_ID_forFakeable():: jetBtagCSV_ID_forFakeable_: " << jetBtagCSV_ID_forFakeable_
	    << ", max_jetBtagCSV_forFakeable_: " << max_jetBtagCSV_forFakeable_
	    << std::endl;
}


void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_jetRelIso_cut(double jetRelIso_cut) {
  min_jetPtRatio_ = 1.0 / (1.0 + jetRelIso_cut);
  std::cout << "RecoElectronSelectorFakeable_hh_multilepton_Dynamic::set_jetRelIso_cut():: jetRelIso_cut: " << jetRelIso_cut << ",  min_jetPtRatio_: " << min_jetPtRatio_ << std::endl;
}


void
RecoElectronSelectorFakeable_hh_multilepton_Dynamic::print_fakeable_consitions() {
  std::cout << "RecoElectronSelectorFakeable_hh_multilepton_Dynamic::print_fakeable_consitions()::  pod_wp_forFakeable_: " << pod_wp_forFakeable_     
	    << ", max_jetBtagCSV_forFakeable_: " << max_jetBtagCSV_forFakeable_
	    << ", min_jetPtRatio_: " << min_jetPtRatio_
	    << std::endl;    
}


RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic::RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic(Era era,
                                                                               int index,
                                                                               bool debug,
                                                                               bool set_selection_flags)
  : ParticleCollectionSelector<RecoElectron, RecoElectronSelectorFakeable_hh_multilepton_Dynamic>(era, index, debug)
{
  selector_.set_selection_flags(set_selection_flags);
}

void
RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic::enable_offline_e_trigger_cuts()
{
  selector_.enable_offline_e_trigger_cuts();
}

void
RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic::disable_offline_e_trigger_cuts()
{
  selector_.disable_offline_e_trigger_cuts();
}


void
RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic::set_POGID_forFakeable(std::string pog_wp) {
  selector_.set_POGID_forFakeable(pog_wp);
}

void
RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic::set_jetBtagCSV_ID_forFakeable(std::string sjetBtagCSV_ID_forFakeable) {
  selector_.set_jetBtagCSV_ID_forFakeable(sjetBtagCSV_ID_forFakeable);
}

void
RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic::set_jetRelIso_cut(double jetRelIso_cut) {
  selector_.set_jetRelIso_cut(jetRelIso_cut);
}

void
RecoElectronCollectionSelectorFakeable_hh_multilepton_Dynamic::print_fakeable_consitions() {
  selector_.print_fakeable_consitions();
}
