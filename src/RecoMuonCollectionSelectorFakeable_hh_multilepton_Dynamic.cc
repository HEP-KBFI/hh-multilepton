#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton_Dynamic.h"

#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // Era::k*
#include "tthAnalysis/HiggsToTauTau/interface/cmsException.h"         // cmsException()

RecoMuonSelectorFakeable_hh_multilepton_Dynamic::RecoMuonSelectorFakeable_hh_multilepton_Dynamic(Era era,
                                                   int index,
                                                   bool debug,
                                                   bool set_selection_flags)
  : era_(era)
  , debug_(debug)
  , set_selection_flags_(set_selection_flags)
  , min_lepton_pt_(5.) // L
  , min_cone_pt_(10.) // F
  , max_absEta_(2.4) // L
  , max_dxy_(0.05) // L
  , max_dz_(0.1) // L
  , max_relIso_(0.4) // L
  , max_sip3d_(8.) // L
  , apply_looseIdPOG_(true) // L
  , apply_mediumIdPOG_(false) // L
  , min_jetPtRatio_(2. / 3) // F
  , min_jetBtagCSV_forFakeable_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium)) // F
  , max_jetBtagCSV_forFakeable_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kTight)) // F
  , max_jetBtagCSV_forTight_(get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium)) // F
  , smoothBtagCut_minPt_(20.)
  , smoothBtagCut_maxPt_(45.)
  , smoothBtagCut_ptDiff_(smoothBtagCut_maxPt_ - smoothBtagCut_minPt_)
  , useAssocJetBtag_(false)
{
  // L -- inherited from the preselection (loose cut)
  // F -- additional fakeable cut not applied in the preselection
}

void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_min_lepton_pt(double min_lepton_pt)
{
  min_lepton_pt_ = min_lepton_pt;
}

void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_min_cone_pt(double min_cone_pt)
{
  min_cone_pt_ = min_cone_pt;
}

void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_max_absEta(double max_absEta)
{
  max_absEta_ = max_absEta;
}

void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_selection_flags(bool selection_flags)
{
  set_selection_flags_ = selection_flags;
}

void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_assocJetBtag(bool flag)
{
  useAssocJetBtag_ = flag;
}

double
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::get_min_lepton_pt() const
{
  return min_lepton_pt_;
}

double
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::get_min_cone_pt() const
{
  return min_cone_pt_;
}

double
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::get_max_absEta() const
{
  return max_absEta_;
}

bool
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::operator()(const RecoMuon & muon) const
{
  if(debug_)
  {
    std::cout << get_human_line(this, __func__) << ":\n" << muon;
  }

  if(muon.cone_pt() < min_cone_pt_)
  {
    if(debug_)
    {
      std::cout << "FAILS cone pT = " << muon.cone_pt() << " >= " << min_cone_pt_ << " fakeable cut\n";
    }
    return false;
  }

  if(muon.lepton_pt() < min_lepton_pt_)
  {
    if(debug_)
    {
      std::cout << "FAILS pT = " << muon.pt() << " >= " << min_lepton_pt_ << " fakeable cut\n";
    }
  }

  if(muon.absEta() > max_absEta_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(eta) = " << muon.absEta() << " <= " << max_absEta_ << " fakeable cut\n";
    }
    return false;
  }

  if(std::fabs(muon.dxy()) > max_dxy_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(dxy) = " << std::fabs(muon.dxy()) << " <= " << max_dxy_ << " fakeable cut\n";
    }
    return false;
  }

  if(std::fabs(muon.dz()) > max_dz_)
  {
    if(debug_)
    {
      std::cout << "FAILS abs(dz) = " << std::fabs(muon.dz()) << " <= " << max_dz_ << " fakeable cut\n";
    }
    return false;
  }

  if(muon.relIso() > max_relIso_)
  {
    if(debug_)
    {
      std::cout << "FAILS relIso = " << muon.relIso() << " <= " << max_relIso_ << " fakeable cut\n";
    }
    return false;
  }

  if(muon.sip3d() > max_sip3d_)
  {
    if(debug_)
    {
      std::cout << "FAILS sip3d = " << muon.sip3d() << " <= " << max_sip3d_ << " fakeable cut\n";
    }
    return false;
  }

  if(! muon.passesLooseIdPOG() && apply_looseIdPOG_)
  {
    if(debug_)
    {
      std::cout << "FAILS loose POG fakeable cut\n";
    }
    return false;
  }

  if(! muon.passesMediumIdPOG() && apply_mediumIdPOG_)
  {
    if(debug_)
    {
      std::cout << "FAILS medium POG fakeable cut\n";
    }
    return false;
  }
  if (muon.mvaRawTTH() > muon.mvaRawTTH_cut()) {
    if(muon.jetBtagCSV(useAssocJetBtag_) > max_jetBtagCSV_forTight_)
    {
      if(debug_)
      {
	std::cout << "FAILS jetBtagCSV = " << muon.jetBtagCSV(useAssocJetBtag_) << " <= " << max_jetBtagCSV_forTight_ << " fakeable cut\n";
      }
      return false;
    }
  }

  if(muon.mvaRawTTH() <= muon.mvaRawTTH_cut())
  {
    if(muon.jetPtRatio() < min_jetPtRatio_)
    {
      if(debug_)
      {
        std::cout << "FAILS jetPtRatio = " << muon.jetPtRatio() << " >= " << min_jetPtRatio_ << " fakeable cut\n";
      }
      return false;
    }

    double max_jetBtagCSV; 
    if ( (jetBtagCSV_ID_forFakeable_.compare("WP-I") == 0) || (jetBtagCSV_ID_forFakeable_.compare("WP-IMT") == 0)) { // 
      max_jetBtagCSV = smoothBtagCut(muon.assocJet_pt());
    }
    if ( (jetBtagCSV_ID_forFakeable_.compare("WP-M") == 0) || (jetBtagCSV_ID_forFakeable_.compare("WP-T") == 0) || (jetBtagCSV_ID_forFakeable_.compare("WP-NoCut") == 0)) { // 
       max_jetBtagCSV = max_jetBtagCSV_forFakeable_;
    }   
    
    if(debug_)
    {
      std::cout << get_human_line(this, __func__) << ": smooth jetBtagCSV cut = " << max_jetBtagCSV << '\n';
    }
    if(muon.jetBtagCSV(useAssocJetBtag_) > max_jetBtagCSV)
    {
      if(debug_)
      {
        std::cout << "FAILS smooth jetBtagCSV = " << muon.jetBtagCSV(useAssocJetBtag_) << " <= " << max_jetBtagCSV << " fakeable cut\n";
      }
      return false;
    }
  }

  if(set_selection_flags_)
  {
    muon.set_isFakeable();
  }

  return true;
}




double
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::smoothBtagCut(double assocJet_pt) const
{
  const double ptInterp = std::min(1., std::max(0., assocJet_pt - smoothBtagCut_minPt_) / smoothBtagCut_ptDiff_);
  return ptInterp * min_jetBtagCSV_forFakeable_ + (1. - ptInterp) * max_jetBtagCSV_forFakeable_;
}


void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_POGID(std::string pog_wp) {
  if (pog_wp.compare("WP-M") == 0) {
    apply_mediumIdPOG_ = true;
    std::cout << "RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_POGID POG WP-Medium set" << std::endl;
  }
}


void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_jetBtagCSV_ID_forFakeable(std::string sjetBtagCSV_ID_forFakeable) {
  jetBtagCSV_ID_forFakeable_ = sjetBtagCSV_ID_forFakeable;
  
  if (jetBtagCSV_ID_forFakeable_.compare("WP-I") == 0) {
    min_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kLoose));
    max_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium));
  }
  if (jetBtagCSV_ID_forFakeable_.compare("WP-M") == 0) {
    min_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium));
    max_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium));
  }
  if (jetBtagCSV_ID_forFakeable_.compare("WP-IMT") == 0) {
    min_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kMedium));
    max_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kTight));
  }
  if (jetBtagCSV_ID_forFakeable_.compare("WP-T") == 0) {
    min_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kTight));
    max_jetBtagCSV_forFakeable_ = (get_BtagWP(era_, Btag::kDeepJet, BtagWP::kTight));
  }
  if (jetBtagCSV_ID_forFakeable_.compare("WP-NoCut") == 0) {
    min_jetBtagCSV_forFakeable_ = 1.0;
    max_jetBtagCSV_forFakeable_ = 1.0;
  }
  std::cout << "RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_jetBtagCSV_ID_forFakeable():: jetBtagCSV_ID_forFakeable_: " << jetBtagCSV_ID_forFakeable_
	    << ", min_jetBtagCSV_forFakeable_: " << min_jetBtagCSV_forFakeable_
	    << ", max_jetBtagCSV_forFakeable_: " << max_jetBtagCSV_forFakeable_
	    << std::endl;
}


void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_jetRelIso_cut(double jetRelIso_cut) {
  min_jetPtRatio_ = 1.0 / (1.0 + jetRelIso_cut);
  std::cout << "RecoMuonSelectorFakeable_hh_multilepton_Dynamic::set_jetRelIso_cut():: jetRelIso_cut: " << jetRelIso_cut << ",  min_jetPtRatio_: " << min_jetPtRatio_ << std::endl;
}


void
RecoMuonSelectorFakeable_hh_multilepton_Dynamic::print_fakeable_consitions() {
  std::cout << "RecoMuonSelectorFakeable_hh_multilepton_Dynamic::print_fakeable_consitions():: apply_looseIdPOG_: " << apply_looseIdPOG_
	    << ", apply_mediumIdPOG_:" << apply_mediumIdPOG_
	    << ", jetBtagCSV_ID_forFakeable_: " << jetBtagCSV_ID_forFakeable_
	    << ", min_jetBtagCSV_forFakeable_: " << min_jetBtagCSV_forFakeable_
	    << ", max_jetBtagCSV_forFakeable_: " << max_jetBtagCSV_forFakeable_
	    << ", min_jetPtRatio_: " << min_jetPtRatio_
	    << std::endl;    
}


RecoMuonCollectionSelectorFakeable_hh_multilepton_Dynamic::RecoMuonCollectionSelectorFakeable_hh_multilepton_Dynamic(Era era,
                                                                       int index,
                                                                       bool debug,
                                                                       bool set_selection_flags)
  : ParticleCollectionSelector<RecoMuon, RecoMuonSelectorFakeable_hh_multilepton_Dynamic>(era, index, debug)
{
  selector_.set_selection_flags(set_selection_flags);
}



void
RecoMuonCollectionSelectorFakeable_hh_multilepton_Dynamic::set_POGID(std::string pog_wp) {
  selector_.set_POGID(pog_wp);
}

void
RecoMuonCollectionSelectorFakeable_hh_multilepton_Dynamic::set_jetBtagCSV_ID_forFakeable(std::string sjetBtagCSV_ID_forFakeable) {
  selector_.set_jetBtagCSV_ID_forFakeable(sjetBtagCSV_ID_forFakeable);
}

void
RecoMuonCollectionSelectorFakeable_hh_multilepton_Dynamic::set_jetRelIso_cut(double jetRelIso_cut) {
  selector_.set_jetRelIso_cut(jetRelIso_cut);
}

void
RecoMuonCollectionSelectorFakeable_hh_multilepton_Dynamic::print_fakeable_consitions() {
  selector_.print_fakeable_consitions();
}
