#include "FWCore/ParameterSet/interface/ParameterSet.h" // edm::ParameterSet
#include "FWCore/Utilities/interface/Exception.h" // cms::Exception
#include "PhysicsTools/FWLite/interface/TFileService.h" // fwlite::TFileService
#include "DataFormats/FWLite/interface/InputSource.h" // fwlite::InputSource
#include "DataFormats/FWLite/interface/OutputFiles.h" // fwlite::OutputFiles
#include "DataFormats/Math/interface/LorentzVector.h" // math::PtEtaPhiMLorentzVector
#include "DataFormats/Math/interface/deltaR.h" // deltaR

#if __has_include (<FWCore/ParameterSetReader/interface/ParameterSetReader.h>)
#  include <FWCore/ParameterSetReader/interface/ParameterSetReader.h> // edm::readPSetsFrom()
#else
#  include <FWCore/PythonParameterSet/interface/MakeParameterSets.h> // edm::readPSetsFrom()
#endif

#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
#include <TRandom3.h> // TRandom3
#include <TROOT.h> // TROOT

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicity.h" // ObjectMultiplicity
#include "tthAnalysis/HiggsToTauTau/interface/TrigObj.h" // TrigObj
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h" // JetToTauFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/jetToTauFakeRateAuxFunctions.h" // getTrigMatchingOption
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/TrigObjReader.h" // TrigObjReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoReader.h" // LHEInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/PSWeightReader.h" // PSWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicityReader.h" // ObjectMultiplicityReader
#include "tthAnalysis/HiggsToTauTau/interface/convert_to_ptrs.h" // convert_to_ptrs
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionCleaner.h" // RecoElectronCollectionCleaner, RecoMuonCollectionCleaner, RecoHadTauCollectionCleaner, RecoJetCollectionCleaner
#include "tthAnalysis/HiggsToTauTau/interface/ParticleCollectionGenMatcher.h" // RecoElectronCollectionGenMatcher, RecoMuonCollectionGenMatcher, RecoHadTauCollectionGenMatcher, RecoJetCollectionGenMatcher
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorLoose.h" // RecoElectronCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorFakeable.h" // RecoElectronCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronCollectionSelectorTight.h" // RecoElectronCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorLoose.h" // RecoMuonCollectionSelectorLoose
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorFakeable.h" // RecoMuonCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonCollectionSelectorTight.h" // RecoMuonCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorFakeable.h" // RecoHadTauCollectionSelectorFakeable
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorTight.h" // RecoHadTauCollectionSelectorTight
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtHistManager.h" // MEtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterHistManager.h" // MEtFilterHistManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtYieldHistManager.h" // EvtYieldHistManager
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h" // fillWithOverFlow2d
#include "tthAnalysis/HiggsToTauTau/interface/hadTauGenMatchingAuxFunctions.h" // getHadTauGenMatch_definitions_1tau, getHadTauGenMatch_string, getHadTauGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h" // getWeight_4L, getWeight_4L
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface_2.h" // HHWeightInterface
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/BM_list.h" // BMS
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility

#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_0l_4tau.h" // EvtHistManager_hh_0l_4tau
#include "hhAnalysis/multilepton/interface/SVfit4tauHistManager_MarkovChain.h" // SVfit4tauHistManager_MarkovChain
#include "hhAnalysis/multilepton/interface/Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger.h"
#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // getMeasuredTauLeptonType, getHadTauDecayMode
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "TauAnalysis/ClassicSVfit4tau/interface/ClassicSVfit4tau.h" // ClassicSVfit4tau
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit4tau/interface/svFitHistogramAdapter4tau.h" // HistogramAdapterDiHiggs, HistogramAdapterHiggs
#include "TauAnalysis/ClassicSVfit/interface/svFitAuxFunctions.h" // aux functions
#include "TauAnalysis/ClassicSVfit/interface/ClassicSVfit.h" // SVFit for 2 taus


#include <boost/math/special_functions/sign.hpp> // boost::math::sign()
#include <boost/algorithm/string/predicate.hpp> // boost::starts_with()
#include <boost/algorithm/string/replace.hpp> // boost::replace_all_copy()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <fstream> // std::ofstream
#include <assert.h> // assert
#include <bits/stdc++.h> // finding max element

#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // for comp_*()

#include <TMath.h>
#include <Python.h>


edm::ParameterSet
makeHistManager_cfg(const std::string & process,
                    const std::string & category,
                    const std::string & era,
                    const std::string & central_or_shift,
                    const std::vector<double> & gen_mHH,
                    int idx = -1)
{
  edm::ParameterSet cfg = makeHistManager_cfg(process, category, era, central_or_shift, idx);
  cfg.addParameter<std::vector<double>>("gen_mHH", gen_mHH);
  return cfg;
}

edm::ParameterSet
makeHistManager_cfg(const std::string & process,
                    const std::string & category,
                    const std::string & era,
                    const std::string & central_or_shift,
                    const std::vector<double> & gen_mHH,
                    const std::string & option,
                    int idx = -1)
{
  edm::ParameterSet cfg = makeHistManager_cfg(process, category, era, central_or_shift, gen_mHH, idx);
  cfg.addParameter<std::string>("option", option);
  return cfg;
}



typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

enum { k1e, k1mu };
enum { kFR_disabled, kFR_4tau };

const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied

struct HadTauHistManagerWrapper_eta
{
  HadTauHistManager* histManager_;
  double etaMin_;
  double etaMax_;
};

/**
 * @brief Produce datacard and control plots for 0l_4tau category of HH "multilepton" (HH->WWWW,WWtt,tttt) analysis.
 */
int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- stop ROOT from keeping track of all histograms
  TH1::AddDirectory(false);

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_hh_0l_4tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_0l_4tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_0l_4tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_0l_4tau");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isMC_ttH = process_string == "TTH";
  bool isMC_tH = process_string == "TH";
  bool isMC_EWK = process_string == "WZ" || process_string == "ZZ";
  bool isSignal = boost::starts_with(process_string, "signal_") && process_string.find("_hh_") != std::string::npos;
  bool isHH_rwgt_allowed = boost::starts_with(process_string, "signal_ggf_nonresonant_") && process_string.find("cHHH") == std::string::npos;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_t = histogramDir.find("mcClosure_t") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  vstring triggerNames_2tau = cfg_analyze.getParameter<vstring>("triggers_2tau");
  std::vector<hltPath*> triggers_2tau = create_hltPaths(triggerNames_2tau, "triggers_2tau");
  bool use_triggers_2tau = cfg_analyze.getParameter<bool>("use_triggers_2tau");

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  const std::string hadTauSelection_part1 = (dynamic_cast<TObjString*>(hadTauSelection_parts->At(0)))->GetString().Data();
  const int hadTauSelection = get_selection(hadTauSelection_part1);
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;
  const TauID tauId = TauID_PyMap.at(hadTauSelection_part2.substr(0, 7));
  int tauLevel = get_tau_id_wp_int(hadTauSelection_part2);

  const double lep_mva_cut_mu = cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e  = cfg_analyze.getParameter<double>("lep_mva_cut_e");

  bool apply_hadTauGenMatching = cfg_analyze.getParameter<bool>("apply_hadTauGenMatching");
  std::vector<hadTauGenMatchEntry> hadTauGenMatch_definitions = getHadTauGenMatch_definitions_4tau(true);
  std::cout << "hadTauGenMatch_definitions:" << std::endl;
  std::cout << hadTauGenMatch_definitions;

  GenMatchInterface genMatchInterface(4, apply_hadTauGenMatching);

  enum { kOS, kSS };
  std::string hadTauChargeSelection_string = cfg_analyze.getParameter<std::string>("hadTauChargeSelection");
  int hadTauChargeSelection = -1;
  if      ( hadTauChargeSelection_string == "OS" ) hadTauChargeSelection = kOS;
  else if ( hadTauChargeSelection_string == "SS" ) hadTauChargeSelection = kSS;
  else throw cms::Exception("analyze_hh_0l_4tau") 
    << "Invalid Configuration parameter 'hadTauChargeSelection' = " << hadTauChargeSelection_string << " !!\n";
  TRandom3 rnd; // used to randomly kill one of three possible combination of measuredTauLeptons into pairs in case chargeSumSelection is "SS" or "disabled",
                // to ensure that exactly two possible combination of measuredTauLeptons are considered, regardless of chargeSumSelection

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  bool hasLHE = cfg_analyze.getParameter<bool>("hasLHE");
  bool hasPS = cfg_analyze.getParameter<bool>("hasPS");
  bool apply_LHE_nom = cfg_analyze.getParameter<bool>("apply_LHE_nom");
  bool useObjectMultiplicity = cfg_analyze.getParameter<bool>("useObjectMultiplicity");
  std::string central_or_shift_main = cfg_analyze.getParameter<std::string>("central_or_shift");
  std::vector<std::string> central_or_shifts_local = cfg_analyze.getParameter<std::vector<std::string>>("central_or_shifts_local");
  edm::VParameterSet lumiScale = cfg_analyze.getParameter<edm::VParameterSet>("lumiScale");
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");
  std::string apply_topPtReweighting_str = cfg_analyze.getParameter<std::string>("apply_topPtReweighting");
  bool apply_topPtReweighting = ! apply_topPtReweighting_str.empty();
  bool apply_l1PreFireWeight = cfg_analyze.getParameter<bool>("apply_l1PreFireWeight");
  bool apply_btagSFRatio = cfg_analyze.getParameter<bool>("applyBtagSFRatio");
  bool apply_hlt_filter = cfg_analyze.getParameter<bool>("apply_hlt_filter");
  bool apply_met_filters = cfg_analyze.getParameter<bool>("apply_met_filters");
  edm::ParameterSet cfgMEtFilter = cfg_analyze.getParameter<edm::ParameterSet>("cfgMEtFilter");
  MEtFilterSelector metFilterSelector(cfgMEtFilter, isMC);
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;

  if(! central_or_shifts_local.empty())
  {
    assert(central_or_shift_main == "central");
    assert(std::find(central_or_shifts_local.cbegin(), central_or_shifts_local.cend(), "central") != central_or_shifts_local.cend());
  }
  else
  {
    central_or_shifts_local = { central_or_shift_main };
  }

  edm::ParameterSet triggerWhiteList;
  if(! isMC)
  {
    triggerWhiteList = cfg_analyze.getParameter<edm::ParameterSet>("triggerWhiteList");
  }

  const edm::ParameterSet additionalEvtWeight = cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight = additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager * eventWeightManager = nullptr;
  if(applyAdditionalEvtWeight)
  {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
    eventWeightManager->set_central_or_shift(central_or_shift_main);
  }

  bool isDEBUG = cfg_analyze.getParameter<bool>("isDEBUG");
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  checkOptionValidity(central_or_shift_main, isMC);
  const int met_option      = useNonNominal_jetmet ? kJetMET_central_nonNominal : getMET_option(central_or_shift_main, isMC);
  const int jetPt_option    = useNonNominal_jetmet ? kJetMET_central_nonNominal : getJet_option(central_or_shift_main, isMC);
  const int hadTauPt_option = useNonNominal_jetmet ? kHadTauPt_uncorrected      : getHadTauPt_option(central_or_shift_main);

  std::cout
    << "central_or_shift = "    << central_or_shift_main << "\n"
       " -> hadTauPt_option = " << hadTauPt_option       << "\n"
       " -> met_option      = " << met_option            << "\n"
       " -> jetPt_option    = " << jetPt_option          << '\n'
  ;

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron_lead", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon_lead", hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron_sublead", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon_sublead", hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", false);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case Era::k2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case Era::k2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case Era::k2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_0l_2tau", __LINE__) << "Invalid era = " << static_cast<int>(era);
  }
  Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger* dataToMCcorrectionInterface_hh_0l_4tau_trigger = new Data_to_MC_CorrectionInterface_hh_0l_4tau_trigger(cfg_dataToMCcorrectionInterface);

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "4tau"     ) applyFakeRateWeights = kFR_4tau;
  else throw cms::Exception("analyze_hh_0l_4tau")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  JetToTauFakeRateInterface* jetToTauFakeRateInterface_passesTrigger = nullptr;
  JetToTauFakeRateInterface* jetToTauFakeRateInterface_failsTrigger  = nullptr;
  // CV: ditau trigger uses medium isolation (tight charged isolation) 
  //     for both tau legs in 2016 data-taking period (2017 and 2018 data-taking periods)
  std::string trigMatching_passesTrigger, trigMatching_failsTrigger;
  int filterBit_passesTrigger = 0;
  if ( era == Era::k2016 )
  {
    trigMatching_passesTrigger = "passesTriggerMatchingMediumIso";
    trigMatching_failsTrigger  = "failsTriggerMatchingMediumIso";
    filterBit_passesTrigger = getTrigMatchingOption_2016(trigMatching_passesTrigger);
  }
  else if ( era == Era::k2017 || era == Era::k2018 )
  {
    trigMatching_passesTrigger = "passesTriggerMatchingTightChargedIso";
    trigMatching_failsTrigger  = "failsTriggerMatchingTightChargedIso";
    filterBit_passesTrigger = getTrigMatchingOption_2017and2018(trigMatching_passesTrigger);
  }
  else throw cmsException("analyze_hh_0l_4tau", __LINE__) << "Invalid era = " << static_cast<int>(era);
  if ( applyFakeRateWeights == kFR_4tau ) {
    edm::ParameterSet cfg_hadTauFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("hadTauFakeRateWeight");
    cfg_hadTauFakeRateWeight.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
    jetToTauFakeRateInterface_passesTrigger = new JetToTauFakeRateInterface(cfg_hadTauFakeRateWeight, trigMatching_passesTrigger);
    jetToTauFakeRateInterface_failsTrigger  = new JetToTauFakeRateInterface(cfg_hadTauFakeRateWeight, trigMatching_failsTrigger);
  }

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");
  std::string branchName_trigObjs = cfg_analyze.getParameter<std::string>("branchName_trigObjs");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");

  std::string branchName_muonGenMatch     = cfg_analyze.getParameter<std::string>("branchName_muonGenMatch");
  std::string branchName_electronGenMatch = cfg_analyze.getParameter<std::string>("branchName_electronGenMatch");
  std::string branchName_hadTauGenMatch   = cfg_analyze.getParameter<std::string>("branchName_hadTauGenMatch");
  std::string branchName_jetGenMatch      = cfg_analyze.getParameter<std::string>("branchName_jetGenMatch");

  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");
  bool genMatchingByIndex = cfg_analyze.getParameter<bool>("genMatchingByIndex");

  const bool selectBDT = cfg_analyze.exists("selectBDT") ? cfg_analyze.getParameter<bool>("selectBDT") : false;

  const edm::ParameterSet mvaInfo_res = cfg_analyze.getParameter<edm::ParameterSet>("mvaInfo_res");
  std::vector<double> gen_mHH = cfg_analyze.getParameter<std::vector<double>>("gen_mHH");
  std::string BDTFileName_even_spin2  = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_even_spin2");
  std::string BDTFileName_odd_spin2   = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_odd_spin2");
  std::string fitFunctionFileName_spin2 = mvaInfo_res.getParameter<std::string>("fitFunctionFileName_spin2");
  std::vector<std::string> BDTInputVariables_SUM_spin2 = mvaInfo_res.getParameter<std::vector<std::string>>("inputVars_spin2");
  std::string BDTFileName_even_spin0  = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_even_spin0");
  std::string BDTFileName_odd_spin0   = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_odd_spin0");
  std::string fitFunctionFileName_spin0 = mvaInfo_res.getParameter<std::string>("fitFunctionFileName_spin0");
  std::vector<std::string> BDTInputVariables_SUM_spin0 = mvaInfo_res.getParameter<std::vector<std::string>>("inputVars_spin0");


  assert(fitFunctionFileName_spin2 != "");
  assert(fitFunctionFileName_spin0 != "");
  TMVAInterface* BDT_SUM_spin2 = new TMVAInterface(BDTFileName_odd_spin2, BDTFileName_even_spin2, BDTInputVariables_SUM_spin2, fitFunctionFileName_spin2);
  BDT_SUM_spin2->enableBDTTransform();
  TMVAInterface* BDT_SUM_spin0 = new TMVAInterface(BDTFileName_odd_spin0, BDTFileName_even_spin0, BDTInputVariables_SUM_spin0, fitFunctionFileName_spin0);
  BDT_SUM_spin0->enableBDTTransform();
  std::map<std::string, double> AllVars_Map;
  std::map<std::string, double> BDTOutput_SUM_Map_spin2;
  std::map<std::string, double> BDTOutput_SUM_Map_spin0;


  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfg_runLumiEventSelector;
    cfg_runLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfg_runLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfg_runLumiEventSelector);
  }

  std::string selEventsFileName_output = cfg_analyze.getParameter<std::string>("selEventsFileName_output");
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

  const double minPt_hadTau_lead    = 40.;
  const double minPt_hadTau_sublead = 30.;
  const double minPt_hadTau_third   = 20.;
  const double minPt_hadTau_fourth  = 20.;

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper * inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);

  std::cout << "Loaded " << inputTree -> getFileCount() << " file(s).\n";

//--- declare event-level variables
  EventInfo eventInfo(isMC, isSignal, isHH_rwgt_allowed, apply_topPtReweighting);
  const std::string default_cat_str = "default";
  std::vector<std::string> evt_cat_strs = { default_cat_str };
  std::vector<std::string> HHWeightNames;

//--- HH scan
  const edm::ParameterSet hhWeight_cfg = cfg_analyze.getParameterSet("hhWeight_cfg");
  const bool apply_HH_rwgt = eventInfo.is_hh_nonresonant() && hhWeight_cfg.getParameter<bool>("apply_rwgt");
  const HHWeightInterface_2 * HHWeight_calc = nullptr;
  if(apply_HH_rwgt)
  {
    HHWeight_calc = new HHWeightInterface_2(hhWeight_cfg);
    evt_cat_strs = HHWeight_calc->get_bm_names();
    HHWeightNames = HHWeight_calc->get_weight_names();
  }
  const size_t Nscan = evt_cat_strs.size();
  if (apply_HH_rwgt)
  {
    std::cout << "Number of points being scanned = " << Nscan << '\n';
    std::cout << "\n Weights booked = " << apply_HH_rwgt << '\n';
    for (const std::string catcat : evt_cat_strs) {
      std::cout << catcat << '\n';
    }
  }
  else
  {
    std::cout << "No HH reweighting applied: " << boost::join(evt_cat_strs, ", ") << '\n';
  }

  const std::vector<edm::ParameterSet> tHweights = cfg_analyze.getParameterSetVector("tHweights");
  if((isMC_tH || isMC_ttH) && ! tHweights.empty())
  {
    eventInfo.loadWeight_tH(tHweights);
  }
  EventInfoReader eventInfoReader(&eventInfo);
  if(apply_topPtReweighting)
  {
    eventInfoReader.setTopPtRwgtBranchName(apply_topPtReweighting_str);
  }
  inputTree -> registerReader(&eventInfoReader);

  ObjectMultiplicity objectMultiplicity;
  ObjectMultiplicityReader objectMultiplicityReader(&objectMultiplicity);
  if(useObjectMultiplicity)
  {
    inputTree -> registerReader(&objectMultiplicityReader);
  }

  hltPathReader hltPathReader_instance({ triggers_2tau });
  inputTree -> registerReader(&hltPathReader_instance);

  if(eventWeightManager)
  {
    inputTree->registerReader(eventWeightManager);
  }

  L1PreFiringWeightReader * l1PreFiringWeightReader = nullptr;
  if(apply_l1PreFireWeight)
  {
    l1PreFiringWeightReader = new L1PreFiringWeightReader(era);
    inputTree->registerReader(l1PreFiringWeightReader);
  }

  BtagSFRatioFacility * btagSFRatioFacility = nullptr;
  if(apply_btagSFRatio)
  {
    const edm::ParameterSet btagSFRatio = cfg_analyze.getParameterSet("btagSFRatio");
    btagSFRatioFacility = new BtagSFRatioFacility(btagSFRatio);
  }

  TrigObjReader trigObjReader(branchName_trigObjs);
  inputTree -> registerReader(&trigObjReader);

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree -> registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree -> registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  electronReader->set_mvaTTH_wp(lep_mva_cut_e);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, isMC, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree -> registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3, isDEBUG);
  RecoHadTauCollectionSelectorFakeable fakeableHadTauSelector(era, -1, isDEBUG);
  fakeableHadTauSelector.set_if_looser(hadTauSelection_part2);
  fakeableHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  fakeableHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorTight tightHadTauSelector(era, -1, isDEBUG);
  tightHadTauSelector.set(hadTauSelection_part2);
  tightHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  switch(hadTauSelection)
  {
    case kFakeable: tauLevel = std::min(tauLevel, get_tau_id_wp_int(fakeableHadTauSelector.getSelector().get())); break;
    case kTight:    tauLevel = std::min(tauLevel, get_tau_id_wp_int(tightHadTauSelector.getSelector().get()));    break;
    default: assert(0);
  }

  RecoJetReader* jetReader = new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  jetReader->setPtMass_central_or_shift(jetPt_option);
  jetReader->read_btag_systematics((central_or_shifts_local.size() > 1 || central_or_shift_main != "central") && isMC);
  inputTree -> registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerByIndex(isDEBUG);
  RecoJetCollectionSelector jetSelector(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era, -1, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree -> registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree -> registerReader(metFilterReader);

  GenLeptonReader * genLeptonReader = nullptr;
  GenHadTauReader * genHadTauReader = nullptr;
  GenPhotonReader * genPhotonReader = nullptr;
  GenJetReader * genJetReader = nullptr;
  LHEInfoReader * lheInfoReader = nullptr;
  PSWeightReader * psWeightReader = nullptr;

  GenParticleReader * genMatchToMuonReader     = nullptr;
  GenParticleReader * genMatchToElectronReader = nullptr;
  GenParticleReader * genMatchToHadTauReader   = nullptr;
  GenParticleReader * genMatchToJetReader      = nullptr;

  if(isMC)
  {
    if(! readGenObjects)
    {
      genLeptonReader = new GenLeptonReader(branchName_genLeptons);
      inputTree -> registerReader(genLeptonReader);
      genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
      inputTree -> registerReader(genHadTauReader);
      genJetReader = new GenJetReader(branchName_genJets);
      inputTree -> registerReader(genJetReader);

      if(genMatchingByIndex)
      {
        genMatchToMuonReader = new GenParticleReader(branchName_muonGenMatch);
        genMatchToMuonReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToMuonReader);

        genMatchToElectronReader = new GenParticleReader(branchName_electronGenMatch);
        genMatchToElectronReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToElectronReader);

        genMatchToHadTauReader = new GenParticleReader(branchName_hadTauGenMatch);
        genMatchToHadTauReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToHadTauReader);

        genMatchToJetReader = new GenParticleReader(branchName_jetGenMatch);
        genMatchToJetReader -> readGenPartFlav(true);
        inputTree -> registerReader(genMatchToJetReader);
      }
      else
      {
        genPhotonReader = new GenPhotonReader(branchName_genPhotons);
        inputTree -> registerReader(genPhotonReader);
      }
    }
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree -> registerReader(lheInfoReader);
    psWeightReader = new PSWeightReader(hasPS, apply_LHE_nom);
    inputTree -> registerReader(psWeightReader);
  }



//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    MuonHistManager* muons_;
    HadTauHistManager* hadTaus_;
    HadTauHistManager* leadHadTau_;
    HadTauHistManager* subleadHadTau_;
    HadTauHistManager* thirdHadTau_;
    HadTauHistManager* fourthHadTau_;
    JetHistManager* jets_;
    JetHistManager* BJets_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    std::map<std::string, EvtHistManager_hh_0l_4tau*> evt_;
    std::map<std::string, SVfit4tauHistManager_MarkovChain*> svFit4tau_woMassConstraint_;
    std::map<std::string, SVfit4tauHistManager_MarkovChain*> svFit4tau_wMassConstraint_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_0l_4tau*>> evt_in_decayModes_;
    std::map<std::string, std::map<std::string, SVfit4tauHistManager_MarkovChain*>> svFit4tau_woMassConstraint_in_decayModes_;
    std::map<std::string, std::map<std::string, SVfit4tauHistManager_MarkovChain*>> svFit4tau_wMassConstraint_in_decayModes_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };

  std::map<std::string, GenEvtHistManager*> genEvtHistManager_beforeCuts;
  std::map<std::string, GenEvtHistManager*> genEvtHistManager_afterCuts;
  std::map<std::string, LHEInfoHistManager*> lheInfoHistManager;
  std::map<std::string, std::map<int, selHistManagerType*>> selHistManagers;
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    const bool skipBooking = central_or_shift != central_or_shift_main;
    std::vector<const GenMatchEntry*> genMatchDefinitions = genMatchInterface.getGenMatchDefinitions();
    for (const GenMatchEntry * genMatchDefinition : genMatchDefinitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += genMatchDefinition->getName();

      int idxHadTau = genMatchDefinition->getIdx();

      selHistManagerType* selHistManager = new selHistManagerType();
      if(! skipBooking)
      {
        selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->electrons_->bookHistograms(fs);
        selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->muons_->bookHistograms(fs);
        selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/hadTaus", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->hadTaus_->bookHistograms(fs);
        selHistManager->leadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadHadTau", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->leadHadTau_->bookHistograms(fs);
        selHistManager->subleadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadHadTau", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->subleadHadTau_->bookHistograms(fs);
        selHistManager->thirdHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/thirdHadTau", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->thirdHadTau_->bookHistograms(fs);
        selHistManager->fourthHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/fourthHadTau", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->fourthHadTau_->bookHistograms(fs);
        selHistManager->jets_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/jets", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jets_->bookHistograms(fs);
        selHistManager->BJets_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/BJets_loose", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->BJets_loose_->bookHistograms(fs);
        selHistManager->BJets_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/BJets_medium", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->BJets_medium_->bookHistograms(fs);
        selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
        selHistManager->met_->bookHistograms(fs);
        selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
        selHistManager->metFilters_->bookHistograms(fs);
      }

      for(const std::string & evt_cat_str: evt_cat_strs)
      {
        if(skipBooking && evt_cat_str != default_cat_str)
        {
          continue;
        }
        const std::string process_string_new = evt_cat_str == default_cat_str ?
          process_string  :
          process_string + evt_cat_str
        ;

        const std::string process_and_genMatchName = boost::replace_all_copy(
          process_and_genMatch, process_string, process_string_new
        );

        selHistManager->evt_[evt_cat_str] = new EvtHistManager_hh_0l_4tau(makeHistManager_cfg(process_and_genMatchName,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, gen_mHH));
        selHistManager->evt_[evt_cat_str]->bookHistograms(fs);
        selHistManager->svFit4tau_woMassConstraint_[evt_cat_str] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_and_genMatchName,
          Form("%s/sel/svFit4tau_woMassConstraint", histogramDir.data()), era_string, central_or_shift));
        selHistManager->svFit4tau_woMassConstraint_[evt_cat_str]->bookHistograms(fs);
        selHistManager->svFit4tau_wMassConstraint_[evt_cat_str] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_and_genMatchName,
          Form("%s/sel/svFit4tau_wMassConstraint", histogramDir.data()), era_string, central_or_shift));
        selHistManager->svFit4tau_wMassConstraint_[evt_cat_str]->bookHistograms(fs);
      }

      const vstring decayModes_evt = eventInfo.getDiHiggsDecayModes();
      if(isSignal)
      {
        for(const std::string & decayMode_evt: decayModes_evt)
        {
          std::string decayMode_and_genMatch = decayMode_evt;
          decayMode_and_genMatch += genMatchDefinition->getName();

          for(const std::string & evt_cat_str: evt_cat_strs)
          {
            if(skipBooking && evt_cat_str != default_cat_str)
            {
              continue;
            }
            const std::string process_string_new = evt_cat_str == default_cat_str ?
              process_string:
              process_string + "_" + evt_cat_str
            ;
            const std::string decayMode_and_genMatchName = boost::replace_all_copy(
              decayMode_and_genMatch, process_string, process_string_new
            );

            selHistManager->evt_in_decayModes_[evt_cat_str][decayMode_evt] = new EvtHistManager_hh_0l_4tau(makeHistManager_cfg(decayMode_and_genMatchName,
              Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, gen_mHH));
            selHistManager->evt_in_decayModes_[evt_cat_str][decayMode_evt]->bookHistograms(fs);
            selHistManager->svFit4tau_woMassConstraint_in_decayModes_[evt_cat_str][decayMode_evt] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(decayMode_and_genMatchName,
              Form("%s/sel/svFit4tau_woMassConstraint", histogramDir.data()), era_string, central_or_shift));
            selHistManager->svFit4tau_woMassConstraint_in_decayModes_[evt_cat_str][decayMode_evt]->bookHistograms(fs);
            selHistManager->svFit4tau_wMassConstraint_in_decayModes_[evt_cat_str][decayMode_evt] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(decayMode_and_genMatchName,
              Form("%s/sel/svFit4tau_wMassConstraint", histogramDir.data()), era_string, central_or_shift));
            selHistManager->svFit4tau_wMassConstraint_in_decayModes_[evt_cat_str][decayMode_evt]->bookHistograms(fs);
          }
        }
      }

      if(! skipBooking)
      {
        edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/evtYield", histogramDir.data()), era_string, central_or_shift);
        cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
        cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
        selHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
        selHistManager->evtYield_->bookHistograms(fs);
        selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
        selHistManager->weights_->bookHistograms(fs,
          { "genWeight", "pileupWeight", "data_to_MC_correction", "triggerWeight", "hadTauEff", "fakeRate" });
      }
      selHistManagers[central_or_shift][idxHadTau] = selHistManager;
    }

    if(isMC && ! skipBooking)
    {
      genEvtHistManager_beforeCuts[central_or_shift] = new GenEvtHistManager(makeHistManager_cfg(process_string,
        Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
      genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs);
      genEvtHistManager_afterCuts[central_or_shift] = new GenEvtHistManager(makeHistManager_cfg(process_string,
        Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
      genEvtHistManager_afterCuts[central_or_shift]->bookHistograms(fs);
       lheInfoHistManager[central_or_shift] = new LHEInfoHistManager(makeHistManager_cfg(process_string,
        Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
      lheInfoHistManager[central_or_shift]->bookHistograms(fs);

      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs, eventWeightManager);
        genEvtHistManager_afterCuts[central_or_shift]->bookHistograms(fs, eventWeightManager);
      }
    }
  }

  NtupleFillerBDT<float, int>* bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;
  if(selectBDT)
  {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift_main)
    );
    for(const std::string & evt_cat_str: HHWeightNames)
      {
        if (!apply_HH_rwgt) continue;
        bdt_filler->register_variable<float_type>(Form(evt_cat_str.c_str()));
      }
    bdt_filler->register_variable<float_type>(
      "tau1_pt", "tau1_eta", "tau1_raw", "tau1_phi",
      "tau2_pt", "tau2_eta", "tau2_raw", "tau2_phi",
      "tau3_pt", "tau3_eta", "tau3_raw", "tau3_phi",
      "tau4_pt", "tau4_eta", "tau4_raw", "tau4_phi",
      "tau1_mva", "tau2_mva", "tau3_mva", "tau4_mva",
      "diHiggsVisMass", "diHiggsMass", "mTauTau",
      "avg_dr_jet",
      "STMET", "HT", "met_LD", "mht", "met_phi", "met", "pt_HH_recoil",
      "deltaEta_tau1_tau2", "deltaEta_tau1_tau3", "deltaEta_tau1_tau4",
      "deltaEta_tau2_tau3", "deltaEta_tau2_tau4", "deltaEta_tau3_tau4",
      "deltaPhi_tau1_tau2", "deltaPhi_tau1_tau3", "deltaPhi_tau1_tau4",
      "deltaPhi_tau2_tau3", "deltaPhi_tau2_tau4", "deltaPhi_tau3_tau4",
      "dr_tau1_tau2", "dr_tau1_tau3", "dr_tau1_tau4",
      "dr_tau2_tau3", "dr_tau2_tau4", "dr_tau3_tau4",
      "m_tau1_tau2", "m_tau1_tau3", "m_tau1_tau4",
      "m_tau2_tau3", "m_tau2_tau4", "m_tau3_tau4",
      "Zee_bestTauHPair_m", "Zee_bestTauHPair_dr", "Zee_bestTauHPair_dPhi",
      "Zee_bestTauHPair_dEta", "Zee_bestTauHPair_pt", "mostZeeLike",
      "pt_bestTauHPair_m", "pt_bestTauHPair_dr", "pt_bestTauHPair_dPhi",
      "pt_bestTauHPair_dEta", "pt_bestTauHPair_pt", "dr_bestTauHPair_m",
      "dr_bestTauHPair_dr", "dr_bestTauHPair_dPhi", "dr_bestTauHPair_dEta",
      "dr_bestTauHPair_pt",
      "Zee_secondTauHPair_m", "Zee_secondTauHPair_dr", "Zee_secondTauHPair_dPhi",
      "Zee_secondTauHPair_dEta", "Zee_secondTauHPair_pt",
      "pt_secondTauHPair_m", "pt_secondTauHPair_dr", "pt_secondTauHPair_dPhi",
      "pt_secondTauHPair_dEta", "pt_secondTauHPair_pt", "dr_secondTauHPair_m",
      "dr_secondTauHPair_dr", "dr_secondTauHPair_dPhi", "dr_secondTauHPair_dEta",
      "dr_secondTauHPair_pt", "max_pt_pair_pt", "min_dr_pair_dr",
      "genWeight", "lheWeight", "pileupWeight", "triggerWeight", "btagWeight",
      "hadTauEffSF", "data_to_MC_correction", "FR_Weight", "hadTau1_frWeight", "hadTau2_frWeight",
      "hadTau3_frWeight", "hadTau4_frWeight", "evtWeight"
    );
    bdt_filler->register_variable<int_type>(
      "nJet", "nBJet_loose", "nBJet_medium"
    );
    bdt_filler->bookTree(fs);
  }

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  std::map<std::string, int> selectedEntries_byGenMatchType;             // key = process_and_genMatch
  std::map<std::string, std::map<std::string, double>> selectedEntries_weighted_byGenMatchType; // key = process_and_genMatch
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);
  cutFlowTableType cutFlowTable;
  const edm::ParameterSet cutFlowTableCfg = makeHistManager_cfg(
    process_string, Form("%s/sel/cutFlow", histogramDir.data()), era_string, central_or_shift_main
  );
  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "object multiplicity",
    "trigger",
    ">= 4 fakeable taus",
    "b-jet veto",
    ">= 4 sel taus",
    "no tight leptons",
    "HLT filter matching",
    "m(ll) > 12 GeV",
    Form("sel lead hadTau pT > %.0f GeV", minPt_hadTau_lead),
    Form("sel sublead hadTau pT > %.0f GeV", minPt_hadTau_sublead),
    Form("sel third hadTau pT > %.0f GeV", minPt_hadTau_third),
    Form("sel fourth hadTau pT > %.0f GeV", minPt_hadTau_fourth),
    "sel hadTau charge", 
    "MEt filters",
    "signal region veto",
  };
  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);

  while(inputTree -> hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())))
  {
    if(inputTree -> canReport(reportEvery))
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);

    if (run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo))
    {
      continue;
    }
    EvtWeightRecorderHH evtWeightRecorder(central_or_shifts_local, central_or_shift_main, isMC);
    cutFlowTable.update("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx() << ": " << eventInfo << '\n';
      if ( inputTree->isOpen() ) {
        std::cout << "input File = " << inputTree -> getCurrentFileName() << '\n';
      }
    }

    if(useObjectMultiplicity)
    {
      if(objectMultiplicity.getNRecoLepton(kTight)             > 0 ||
         objectMultiplicity.getNRecoHadTau(tauId, tauLevel)    < 4  )
      {
        if(isDEBUG || run_lumi_eventSelector)
        {
          std::cout << "event " << eventInfo.str() << " FAILS preliminary object multiplicity cuts\n";
        }
        continue;
      }
    }
    cutFlowTable.update("object multiplicity", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("object multiplicity", evtWeightRecorder.get(central_or_shift_main));

//--- build collections of generator level particles (before any cuts are applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    std::vector<GenPhoton> genPhotons;
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenJet> genJets;

    std::vector<GenParticle> muonGenMatch;
    std::vector<GenParticle> electronGenMatch;
    std::vector<GenParticle> hadTauGenMatch;
    std::vector<GenParticle> jetGenMatch;
    if(isMC && fillGenEvtHistograms)
    {
      if(genLeptonReader)
      {
        genLeptons = genLeptonReader->read();
        for(const GenLepton & genLepton: genLeptons)
        {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch(abs_pdgId)
          {
            case 11: genElectrons.push_back(genLepton); break;
            case 13: genMuons.push_back(genLepton);     break;
            default: assert(0);
          }
        }
      }
      if(genHadTauReader) genHadTaus = genHadTauReader->read();
      if(genPhotonReader) genPhotons = genPhotonReader->read();
      if(genJetReader)    genJets = genJetReader->read();

      if(genMatchToMuonReader)     muonGenMatch = genMatchToMuonReader->read();
      if(genMatchToElectronReader) electronGenMatch = genMatchToElectronReader->read();
      if(genMatchToHadTauReader)   hadTauGenMatch = genMatchToHadTauReader->read();
      if(genMatchToJetReader)      jetGenMatch = genMatchToJetReader->read();
    }

    if(isMC)
    {
      if(apply_genWeight)         evtWeightRecorder.record_genWeight(boost::math::sign(eventInfo.genWeight));
      if(eventWeightManager)      evtWeightRecorder.record_auxWeight(eventWeightManager);
      if(l1PreFiringWeightReader) evtWeightRecorder.record_l1PrefireWeight(l1PreFiringWeightReader);
      if(apply_topPtReweighting)  evtWeightRecorder.record_toppt_rwgt(eventInfo.topPtRwgtSF);
      lheInfoReader->read();
      psWeightReader->read();
      evtWeightRecorder.record_lheScaleWeight(lheInfoReader);
      evtWeightRecorder.record_psWeight(psWeightReader);
      evtWeightRecorder.record_puWeight(&eventInfo);
      evtWeightRecorder.record_nom_tH_weight(&eventInfo);
      evtWeightRecorder.record_lumiScale(lumiScale);
      for(const std::string & central_or_shift: central_or_shifts_local)
      {
        if(central_or_shift != central_or_shift_main)
        {
          continue;
        }
        genEvtHistManager_beforeCuts[central_or_shift]->fillHistograms(
          genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
        );
        if(eventWeightManager)
        {
          genEvtHistManager_beforeCuts[central_or_shift]->fillHistograms(
            eventWeightManager, evtWeightRecorder.get_inclusive(central_or_shift)
          );
        }
      }
    }

    // CV: require DoubleTau trigger in 2017 MC to pass L1 tau pT > 32 GeV threshold
    //    (cf. slide 6 of https://indico.cern.ch/event/700042/contributions/2871830/attachments/1591232/2527113/180129_TauPOGmeeting_TriggerEfficiency_hsert.pdf )
    bool isTriggered_2tau_L1 = true;
    if ( era == Era::k2017 && isMC ) { 
      std::vector<TrigObj> trigObjs = trigObjReader.read();
      int numTrigObjs = countTrigObjs_passingL1(trigObjs, 15, 32.);
      if(run_lumi_eventSelector)
      {
        std::cout << "numTrigObjs = " << numTrigObjs << std::endl;
      }
      isTriggered_2tau_L1 = (numTrigObjs >= 2); 
    } 
    if(run_lumi_eventSelector)
    {
      std::cout << "isTriggered_2tau_L1 = " << isTriggered_2tau_L1 << std::endl;
    }

    bool isTriggered_2tau = hltPaths_isTriggered(triggers_2tau, triggerWhiteList, eventInfo, isMC, isDEBUG) && isTriggered_2tau_L1;
    if(run_lumi_eventSelector)
    {
      std::cout << "isTriggered_2tau = " << isTriggered_2tau << std::endl;
    }

    bool selTrigger_2tau = use_triggers_2tau && isTriggered_2tau;
    if ( !selTrigger_2tau ) {
      if ( run_lumi_eventSelector ) {
  std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
  std::cout << " (selTrigger_2tau = " << selTrigger_2tau << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("trigger", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger", evtWeightRecorder.get(central_or_shift_main));

//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherConePt);
    const std::vector<const RecoMuon*> fakeableMuons = fakeableMuonSelector(preselMuons, isHigherConePt);
    const std::vector<const RecoMuon*> tightMuons = tightMuonSelector(fakeableMuons, isHigherConePt);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselMuons",   preselMuons);
      printCollection("fakeableMuons", fakeableMuons);
      printCollection("tightMuons",    tightMuons);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, preselMuons);
    const std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> preselElectronsUncleaned = preselElectronSelector(electron_ptrs, isHigherConePt);
    const std::vector<const RecoElectron*> fakeableElectrons = fakeableElectronSelector(preselElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(fakeableElectrons, isHigherConePt);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("preselElectrons",   preselElectrons);
      printCollection("preselElectronsUncleaned", preselElectronsUncleaned);
      printCollection("fakeableElectrons", fakeableElectrons);
      printCollection("tightElectrons",    tightElectrons);
    }

    const std::vector<const RecoLepton*> preselLeptons = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> preselLeptonsUncleaned = mergeLeptonCollections(preselElectronsUncleaned, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptons = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptons = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    const std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    const std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    const std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    const std::vector<const RecoHadTau*> fakeableHadTausFull = fakeableHadTauSelector(cleanedHadTaus, isHigherPt);
    const std::vector<const RecoHadTau*> tightHadTausFull = tightHadTauSelector(fakeableHadTausFull, isHigherPt);

    const std::vector<const RecoHadTau*> fakeableHadTaus = pickFirstNobjects(fakeableHadTausFull, 4);
    const std::vector<const RecoHadTau*> tightHadTaus = getIntersection(fakeableHadTaus, tightHadTausFull, isHigherPt);
    const std::vector<const RecoHadTau*> selHadTaus = selectObjects(hadTauSelection, fakeableHadTaus, tightHadTaus);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("fakeableHadTaus", fakeableHadTaus);
      printCollection("tightHadTaus",    tightHadTaus);
    }

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets = jetReader->read();
    const std::vector<const RecoJet*> jet_ptrs = convert_to_ptrs(jets);
    const std::vector<const RecoJet*> cleanedJets = jetCleaningByIndex ?
      jetCleanerByIndex(jet_ptrs, fakeableElectrons, fakeableMuons, selectBDT ? selHadTaus : fakeableHadTausFull) :
      jetCleaner       (jet_ptrs, fakeableElectrons, fakeableMuons, selectBDT ? selHadTaus : fakeableHadTausFull)
    ;
    const std::vector<const RecoJet*> selJets = jetSelector(cleanedJets, isHigherPt);
    const std::vector<const RecoJet*> selBJets_loose = jetSelectorBtagLoose(cleanedJets, isHigherPt);
    const std::vector<const RecoJet*> selBJets_medium = jetSelectorBtagMedium(cleanedJets, isHigherPt);
    int numSelJetsPtGt40 = countHighPtObjects(selJets, 40.);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("uncleanedJets", jet_ptrs);
      printCollection("selJets",       selJets);
    }

//--- build collections of generator level particles (after some cuts are applied, to safe computing time)
    if(isMC && redoGenMatching && ! fillGenEvtHistograms)
    {
      if(genLeptonReader)
      {
        genLeptons = genLeptonReader->read();
        for(const GenLepton & genLepton: genLeptons)
        {
          const int abs_pdgId = std::abs(genLepton.pdgId());
          switch(abs_pdgId)
          {
            case 11: genElectrons.push_back(genLepton); break;
            case 13: genMuons.push_back(genLepton);     break;
            default: assert(0);
          }
        }
      }
      if(genHadTauReader) genHadTaus = genHadTauReader->read();
      if(genPhotonReader) genPhotons = genPhotonReader->read();
      if(genJetReader)    genJets = genJetReader->read();

      if(genMatchToMuonReader)     muonGenMatch = genMatchToMuonReader->read();
      if(genMatchToElectronReader) electronGenMatch = genMatchToElectronReader->read();
      if(genMatchToHadTauReader)   hadTauGenMatch = genMatchToHadTauReader->read();
      if(genMatchToJetReader)      jetGenMatch = genMatchToJetReader->read();
    }

//--- match reconstructed to generator level particles
    if(isMC && redoGenMatching)
    {
      if(genMatchingByIndex)
      {
        muonGenMatcher.addGenLeptonMatchByIndex(preselMuons, muonGenMatch, GenParticleType::kGenMuon);
        muonGenMatcher.addGenHadTauMatch       (preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch          (preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatchByIndex(preselElectrons, electronGenMatch, GenParticleType::kGenElectron);
        electronGenMatcher.addGenPhotonMatchByIndex(preselElectrons, electronGenMatch);
        electronGenMatcher.addGenHadTauMatch       (preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch          (preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatchByIndex(cleanedHadTaus, hadTauGenMatch, GenParticleType::kGenAnyLepton);
        hadTauGenMatcher.addGenHadTauMatch       (cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch          (cleanedHadTaus, genJets);

        jetGenMatcher.addGenLeptonMatch    (selJets, genLeptons);
        jetGenMatcher.addGenHadTauMatch    (selJets, genHadTaus);
        jetGenMatcher.addGenJetMatchByIndex(selJets, jetGenMatch);
      }
      else
      {
        muonGenMatcher.addGenLeptonMatch(preselMuons, genMuons);
        muonGenMatcher.addGenHadTauMatch(preselMuons, genHadTaus);
        muonGenMatcher.addGenJetMatch   (preselMuons, genJets);

        electronGenMatcher.addGenLeptonMatch(preselElectrons, genElectrons);
        electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotons);
        electronGenMatcher.addGenHadTauMatch(preselElectrons, genHadTaus);
        electronGenMatcher.addGenJetMatch   (preselElectrons, genJets);

        hadTauGenMatcher.addGenLeptonMatch(cleanedHadTaus, genLeptons);
        hadTauGenMatcher.addGenHadTauMatch(cleanedHadTaus, genHadTaus);
        hadTauGenMatcher.addGenJetMatch   (cleanedHadTaus, genJets);

        jetGenMatcher.addGenLeptonMatch(selJets, genLeptons);
        jetGenMatcher.addGenHadTauMatch(selJets, genHadTaus);
        jetGenMatcher.addGenJetMatch   (selJets, genJets);
      }
    }

//--- apply preselection
    // require presence of at least four hadronic taus passing fakeable preselection criteria
    // (do not veto events with more than four fakeable selected hadronic tau candidates,
    //  as sample of hadronic tau candidates passing fakeable preselection criteria contains significant contamination from jets)
    if ( !(fakeableHadTausFull.size() >= 4) ) continue;
    cutFlowTable.update(">= 4 fakeable taus", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 4 fakeable taus", evtWeightRecorder.get(central_or_shift_main));
    //const RecoHadTau* fakeableHadTau_lead = fakeableHadTausFull[0];
    //const RecoHadTau* fakeableHadTau_sublead = fakeableHadTausFull[1];
    //const RecoHadTau* fakeableHadTau_third = fakeableHadTausFull[2];
    //const RecoHadTau* fakeableHadTau_fourth = fakeableHadTausFull[3];
    //const hadTauGenMatchEntry& fakeableHadTau_genMatch = getHadTauGenMatch(
    //  hadTauGenMatch_definitions, fakeableHadTau_lead, fakeableHadTau_sublead, fakeableHadTau_third, fakeableHadTau_fourth
    //);

    if ( selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1 ) continue;
    cutFlowTable.update("b-jet veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("b-jet veto", evtWeightRecorder.get(central_or_shift_main));

//--- compute MHT and linear MET discriminant (met_LD)
    const RecoMEt met_uncorr = metReader->read();
    const RecoMEt met = recompute_met(met_uncorr, jets, met_option, isDEBUG);
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptons, fakeableHadTausFull, selJets);
    double met_LD = compMEt_LD(met.p4(), mht_p4);

    double HT = compHT(fakeableLeptons, fakeableHadTaus, selJets);
    double STMET = compSTMEt(fakeableLeptons, fakeableHadTaus, selJets, met.p4());

//--- apply final event selection
    // require presence of four hadronic taus passing tight selection criteria of final event selection
    if ( !(selHadTaus.size() >= 4) )
    {
      if(run_lumi_eventSelector || isDEBUG)
      {
        std::cout << "event " << eventInfo.str() << " FAILS because there aren't enough taus:\n";
        printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update(">= 4 sel taus", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 4 sel taus", evtWeightRecorder.get(central_or_shift_main));

    // require no leptons passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptons.size() == 0) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection.\n";
        printCollection("tightLeptonsFull", tightLeptons);
      }
      continue;
    }
    cutFlowTable.update("no tight leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("no tight leptons", evtWeightRecorder.get(central_or_shift_main));

//--- apply HLT filter
    if(apply_hlt_filter)
    {
      const std::map<hltPathsE, bool> trigger_bits = {
  { hltPathsE::trigger_2tau, selTrigger_2tau },
      };
      if(! hltFilter(trigger_bits, fakeableLeptons, fakeableHadTaus))
      {
        if(run_lumi_eventSelector || isDEBUG)
        {
          std::cout << "event " << eventInfo.str() << " FAILS HLT filter matching\n";
        }
        continue;
      }
    }
    cutFlowTable.update("HLT filter matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("HLT filter matching", evtWeightRecorder.get(central_or_shift_main));

    const RecoHadTau* selHadTau_lead = selHadTaus[0];
    const RecoHadTau* selHadTau_sublead = selHadTaus[1];
    const RecoHadTau* selHadTau_third = selHadTaus[2];
    const RecoHadTau* selHadTau_fourth = selHadTaus[3];
    const hadTauGenMatchEntry& selHadTau_genMatch = getHadTauGenMatch(hadTauGenMatch_definitions, selHadTau_lead, selHadTau_sublead, selHadTau_third, selHadTau_fourth);
    int idxSelHadTau_genMatch = selHadTau_genMatch.idx_;
    assert(idxSelHadTau_genMatch != kGen_HadTauUndefined4);

    if(isMC)
    {
//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
      evtWeightRecorder.record_btagWeight(selJets);
      if(btagSFRatioFacility)
      {
        evtWeightRecorder.record_btagSFRatio(btagSFRatioFacility, selJets.size());
      }

      if(isMC_EWK)
      {
        evtWeightRecorder.record_ewk_jet(selJets);
        evtWeightRecorder.record_ewk_bjet(selBJets_medium);
      }

      int selHadTau_lead_genPdgId = getHadTau_genPdgId(selHadTau_lead);
      int selHadTau_sublead_genPdgId = getHadTau_genPdgId(selHadTau_sublead);
      int selHadTau_third_genPdgId = getHadTau_genPdgId(selHadTau_third);
      int selHadTau_fourth_genPdgId = getHadTau_genPdgId(selHadTau_fourth);

      dataToMCcorrectionInterface->setHadTaus(
        selHadTau_lead_genPdgId, selHadTau_lead->pt(), selHadTau_lead->eta(), 
        selHadTau_sublead_genPdgId, selHadTau_sublead->pt(), selHadTau_sublead->eta(), 
        selHadTau_third_genPdgId, selHadTau_third->pt(), selHadTau_third->eta(), 
        selHadTau_fourth_genPdgId, selHadTau_fourth->pt(), selHadTau_fourth->eta()
      );
      dataToMCcorrectionInterface_hh_0l_4tau_trigger->setHadTaus(
        selHadTau_lead->pt(),    selHadTau_lead->eta(),    selHadTau_lead->phi(),    selHadTau_lead->decayMode(),
        selHadTau_sublead->pt(), selHadTau_sublead->eta(), selHadTau_sublead->phi(), selHadTau_sublead->decayMode(),
        selHadTau_third->pt(),   selHadTau_third->eta(),   selHadTau_third->phi(),   selHadTau_third->decayMode(),
        selHadTau_fourth->pt(),  selHadTau_fourth->eta(),  selHadTau_fourth->phi(),  selHadTau_fourth->decayMode()
      );
      dataToMCcorrectionInterface_hh_0l_4tau_trigger->setTriggerBits(isTriggered_2tau);

//--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_tauTriggerEff(dataToMCcorrectionInterface_hh_0l_4tau_trigger);

//--- apply data/MC corrections for hadronic tau identification efficiency
//    and for e->tau and mu->tau misidentification rates
      evtWeightRecorder.record_hadTauID_and_Iso(dataToMCcorrectionInterface);
      evtWeightRecorder.record_eToTauFakeRate(dataToMCcorrectionInterface);
      evtWeightRecorder.record_muToTauFakeRate(dataToMCcorrectionInterface);
    }

    JetToTauFakeRateInterface* jetToTauFakeRateInterface_lead    = nullptr;
    JetToTauFakeRateInterface* jetToTauFakeRateInterface_sublead = nullptr;
    JetToTauFakeRateInterface* jetToTauFakeRateInterface_third   = nullptr;
    JetToTauFakeRateInterface* jetToTauFakeRateInterface_fourth  = nullptr;
    if(applyFakeRateWeights == kFR_4tau)
    {
      if ( hltFilter(*selHadTau_lead,    filterBit_passesTrigger, era) ) jetToTauFakeRateInterface_lead    = jetToTauFakeRateInterface_passesTrigger;
      else                                                               jetToTauFakeRateInterface_lead    = jetToTauFakeRateInterface_failsTrigger;
      if ( hltFilter(*selHadTau_sublead, filterBit_passesTrigger, era) ) jetToTauFakeRateInterface_sublead = jetToTauFakeRateInterface_passesTrigger;
      else                                                               jetToTauFakeRateInterface_sublead = jetToTauFakeRateInterface_failsTrigger;
      if ( hltFilter(*selHadTau_third,   filterBit_passesTrigger, era) ) jetToTauFakeRateInterface_third   = jetToTauFakeRateInterface_passesTrigger;
      else                                                               jetToTauFakeRateInterface_third   = jetToTauFakeRateInterface_failsTrigger;
      if ( hltFilter(*selHadTau_fourth,  filterBit_passesTrigger, era) ) jetToTauFakeRateInterface_fourth  = jetToTauFakeRateInterface_passesTrigger;
      else                                                               jetToTauFakeRateInterface_fourth  = jetToTauFakeRateInterface_failsTrigger;
      assert(jetToTauFakeRateInterface_lead && jetToTauFakeRateInterface_sublead && jetToTauFakeRateInterface_third && jetToTauFakeRateInterface_fourth);
      evtWeightRecorder.record_jetToTau_FR_lead(jetToTauFakeRateInterface_lead, selHadTau_lead);
      evtWeightRecorder.record_jetToTau_FR_sublead(jetToTauFakeRateInterface_sublead, selHadTau_sublead);
      evtWeightRecorder.record_jetToTau_FR_third(jetToTauFakeRateInterface_third, selHadTau_third);
      evtWeightRecorder.record_jetToTau_FR_fourth(jetToTauFakeRateInterface_fourth, selHadTau_fourth);
      if(!selectBDT){
        bool passesTight_hadTau_lead    = isMatched(*selHadTau_lead, tightHadTausFull);
        bool passesTight_hadTau_sublead = isMatched(*selHadTau_sublead, tightHadTausFull);
        bool passesTight_hadTau_third   = isMatched(*selHadTau_third, tightHadTausFull);
        bool passesTight_hadTau_fourth  = isMatched(*selHadTau_fourth, tightHadTausFull);
        evtWeightRecorder.compute_FR_4tau(passesTight_hadTau_lead, passesTight_hadTau_sublead, passesTight_hadTau_third, passesTight_hadTau_fourth);
      }
    }

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsUncleaned);
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));

    if ( !(selHadTau_lead->pt() > minPt_hadTau_lead) )
    {
      if(run_lumi_eventSelector || isDEBUG)
      {
        std::cout << "event " << eventInfo.str() << " FAILS minPt = " << minPt_hadTau_lead << " < cut on the selected leading tau\n";
      }
      continue;
    }
    cutFlowTable.update(Form("sel lead hadTau pT > %.0f GeV", minPt_hadTau_lead), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(Form("sel lead hadTau pT > %.0f GeV", minPt_hadTau_lead), evtWeightRecorder.get(central_or_shift_main));

    if ( !(selHadTau_sublead->pt() > minPt_hadTau_sublead) )
    {
      if(run_lumi_eventSelector || isDEBUG)
      {
        std::cout << "event " << eventInfo.str() << " FAILS minPt = " << minPt_hadTau_sublead << " < cut on the selected subleading tau\n";
      }
      continue;
    }
    cutFlowTable.update(Form("sel sublead hadTau pT > %.0f GeV", minPt_hadTau_sublead), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(Form("sel sublead hadTau pT > %.0f GeV", minPt_hadTau_sublead), evtWeightRecorder.get(central_or_shift_main));

    if ( !(selHadTau_third->pt() > minPt_hadTau_third) )
    {
      if(run_lumi_eventSelector || isDEBUG)
      {
        std::cout << "event " << eventInfo.str() << " FAILS minPt = " << minPt_hadTau_third << " < cut on the selected third tau\n";
      }
      continue;
    }
    cutFlowTable.update(Form("sel third hadTau pT > %.0f GeV", minPt_hadTau_third), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(Form("sel third hadTau pT > %.0f GeV", minPt_hadTau_third), evtWeightRecorder.get(central_or_shift_main));

    if ( !(selHadTau_fourth->pt() > minPt_hadTau_fourth) )
    {
      if(run_lumi_eventSelector || isDEBUG)
      {
        std::cout << "event " << eventInfo.str() << " FAILS minPt = " << minPt_hadTau_fourth << " < cut on the selected fourth tau\n";
      }
      continue;
    }
    cutFlowTable.update(Form("sel fourth hadTau pT > %.0f GeV", minPt_hadTau_fourth), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(Form("sel fourth hadTau pT > %.0f GeV", minPt_hadTau_fourth), evtWeightRecorder.get(central_or_shift_main));

    int sumHadTauCharge = selHadTau_lead->charge() + selHadTau_sublead->charge() + selHadTau_third->charge() + selHadTau_fourth->charge();
    bool isCharge_hadTau_SS = sumHadTauCharge != 0;
    bool isCharge_hadTau_OS = sumHadTauCharge == 0;
    if ( (hadTauChargeSelection == kOS && isCharge_hadTau_SS) ||
   (hadTauChargeSelection == kSS && isCharge_hadTau_OS) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS hadTau charge selection." << std::endl;
        std::cout << " (leading selHadTau charge = " << selHadTau_lead->charge()
        << ", subleading selHadTau charge = " << selHadTau_sublead->charge()
        << ", third selHadTau charge = " << selHadTau_third->charge() 
        << ", fourth selHadTau charge = " << selHadTau_fourth->charge() << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("sel hadTau charge", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel hadTau charge", evtWeightRecorder.get(central_or_shift_main));

    if ( apply_met_filters ) {
      if ( !metFilterSelector(metFilters) ) {
  if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS MEt filters." << std::endl;
  }
  continue;
      }
    }
    cutFlowTable.update("MEt filters", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("MEt filters", evtWeightRecorder.get(central_or_shift_main));

    bool failsSignalRegionVeto = false;
    if ( isMCClosure_t ) {
      bool applySignalRegionVeto_hadTau = isMCClosure_t && countFakeHadTaus(selHadTaus) >= 1;
      if ( applySignalRegionVeto_hadTau && tightHadTaus.size() >= 4 ) failsSignalRegionVeto = true;
    } else if ( hadTauSelection == kFakeable ) {
      if ( tightHadTaus.size() >= 4 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
  std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
                     "# tight taus = " << tightHadTaus.size() << " >= 3\n"
        ;
  printCollection("tightHadTaus", tightHadTaus);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("signal region veto", evtWeightRecorder.get(central_or_shift_main));

    std::map<std::string, double> weightMapHH;
    std::map<std::string, double> reWeightMapHH;
    double HHWeight = 1.0; // X: for the SM point -- the point explicited on this code

    if(apply_HH_rwgt)
    {
      assert(HHWeight_calc);
      weightMapHH = HHWeight_calc->getWeightMap(eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
      reWeightMapHH = HHWeight_calc->getReWeightMap(eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
      HHWeight = weightMapHH["Weight_SM"];
      evtWeightRecorder.record_bm(HHWeight); // SM by default

      if(isDEBUG)
      {
        std::cout << "mhh = " << eventInfo.gen_mHH          << " : "
          "cost "             << eventInfo.gen_cosThetaStar << " : "
          "weight = "         << HHWeight                   << '\n'
          ;
        std::cout << "Calculated " << weightMapHH.size() << " scan weights\n";
        for(const auto & kv: weightMapHH)
        {
          std::cout << "line = " <<kv.first << "; Weight = " <<  kv.second << '\n';
        }

        std::cout << '\n';
      }
    }
    
    for(const std::string & central_or_shift: central_or_shifts_local)
    {
      const double evtWeight = evtWeightRecorder.get(central_or_shift);
      const bool skipFilling = central_or_shift != central_or_shift_main;
      for(const std::string & evt_cat_str: evt_cat_strs)
      {
	if(skipFilling && evt_cat_str != default_cat_str)
	{
	  continue;
	}
	if(apply_HH_rwgt)
	{
	  reWeightMapHH[evt_cat_str] *= evtWeight;
	}
	else
	{
	  reWeightMapHH[evt_cat_str] = evtWeight;
	}
      }
    }

    
    std::vector<SVfit4tauResult> svFit4tauResults_woMassConstraint = compSVfit4tau(
      *selHadTau_lead, *selHadTau_sublead, *selHadTau_third, *selHadTau_fourth, met, hadTauChargeSelection_string, rnd,  -1., 2.);
    std::vector<SVfit4tauResult> svFit4tauResults_wMassConstraint = compSVfit4tau(
      *selHadTau_lead, *selHadTau_sublead, *selHadTau_third, *selHadTau_fourth, met, hadTauChargeSelection_string, rnd, 125., 2.);
    
    double dihiggsVisMass_sel = (selHadTau_lead->p4() + selHadTau_sublead->p4() + selHadTau_third->p4() + selHadTau_fourth->p4()).mass();
    double dihiggsMass = ( svFit4tauResults_wMassConstraint.size() >= 1 && svFit4tauResults_wMassConstraint[0].isValidSolution_ ) ? 
      svFit4tauResults_wMassConstraint[0].dihiggs_mass_ : -1.;

    // Compute the BDT variables

    // Eta & Phi 
    const double deltaEta_tau1_tau2 = (selHadTau_lead->p4() - selHadTau_sublead->p4()).eta();
    const double deltaEta_tau1_tau3 = (selHadTau_lead->p4() - selHadTau_third->p4()).eta();
    const double deltaEta_tau1_tau4 = (selHadTau_lead->p4() - selHadTau_fourth->p4()).eta();
    const double deltaEta_tau2_tau3 = (selHadTau_sublead->p4() - selHadTau_third->p4()).eta();
    const double deltaEta_tau2_tau4 = (selHadTau_sublead->p4() - selHadTau_fourth->p4()).eta();
    const double deltaEta_tau3_tau4 = (selHadTau_third->p4() - selHadTau_fourth->p4()).eta();
    const double deltaPhi_tau1_tau2 = (selHadTau_lead->p4() - selHadTau_sublead->p4()).phi();
    const double deltaPhi_tau1_tau3 = (selHadTau_lead->p4() - selHadTau_third->p4()).phi();
    const double deltaPhi_tau1_tau4 = (selHadTau_lead->p4() - selHadTau_fourth->p4()).phi();
    const double deltaPhi_tau2_tau3 = (selHadTau_sublead->p4() - selHadTau_third->p4()).phi();
    const double deltaPhi_tau2_tau4 = (selHadTau_sublead->p4() - selHadTau_fourth->p4()).phi();
    const double deltaPhi_tau3_tau4 = (selHadTau_third->p4() - selHadTau_fourth->p4()).phi();

    // masses
    const double m_tau1_tau2 = (selHadTau_lead->p4() + selHadTau_sublead->p4()).mass();
    const double m_tau1_tau3 = (selHadTau_lead->p4() + selHadTau_third->p4()).mass();
    const double m_tau1_tau4 = (selHadTau_lead->p4() + selHadTau_fourth->p4()).mass();
    const double m_tau2_tau3 = (selHadTau_sublead->p4() + selHadTau_third->p4()).mass();
    const double m_tau2_tau4 = (selHadTau_sublead->p4() + selHadTau_fourth->p4()).mass();
    const double m_tau3_tau4 = (selHadTau_third->p4() + selHadTau_fourth->p4()).mass();

    // deltaR-s
    const double dr_tau1_tau2 = deltaR(selHadTau_lead->p4(), selHadTau_sublead->p4());
    const double dr_tau1_tau3 = deltaR(selHadTau_lead->p4(), selHadTau_third->p4());
    const double dr_tau1_tau4 = deltaR(selHadTau_lead->p4(), selHadTau_fourth->p4());
    const double dr_tau2_tau3 = deltaR(selHadTau_sublead->p4(), selHadTau_third->p4());
    const double dr_tau2_tau4 = deltaR(selHadTau_sublead->p4(), selHadTau_fourth->p4());
    const double dr_tau3_tau4 = deltaR(selHadTau_third->p4(), selHadTau_fourth->p4());

    // tau_id
    const int tau1_mva = selHadTau_lead->id_mva(TauID::DeepTau2017v2VSjet);
    const int tau2_mva = selHadTau_sublead->id_mva(TauID::DeepTau2017v2VSjet);
    const int tau3_mva = selHadTau_third->id_mva(TauID::DeepTau2017v2VSjet);
    const int tau4_mva = selHadTau_fourth->id_mva(TauID::DeepTau2017v2VSjet);

    // Other
    const double avg_dr_jet = comp_avg_dr_jet(selJets);
    const std::vector<const RecoJet*> cleanedJets_wrt_leptons = jetCleaner(jet_ptrs, fakeableLeptons);
    const std::vector<const RecoJet*> selJets_btag = jetSelector(cleanedJets_wrt_leptons, isHigherCSV);
    const std::vector<const RecoJet*> selBJets_btag_loose = jetSelectorBtagLoose(selJets_btag, isHigherPt);
    const std::vector<const RecoJet*> selBJets_btag_medium = jetSelectorBtagMedium(selJets_btag, isHigherPt);
    const double pt_HH_recoil = (selHadTau_lead->p4() + selHadTau_sublead->p4() + selHadTau_third->p4() + selHadTau_fourth->p4() + met.p4()).pt();


    // calculate tau mass using 2 most tau-like taus with SVFit
    std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons;
    classic_svFit::MeasuredTauLepton::kDecayType leg1Type = classic_svFit::MeasuredTauLepton::kTauToHadDecay;
    // Find 2 most tau-like taus
    std::vector<const RecoHadTau*> allTau = {selHadTau_lead, selHadTau_sublead, selHadTau_third, selHadTau_fourth};
    std::vector<int> allTau_tauness = { tau1_mva, tau2_mva, tau3_mva, tau4_mva };
    int most_tauLike_loc = std::distance(allTau_tauness.begin(), std::max_element(allTau_tauness.begin(), allTau_tauness.end()));
    const RecoHadTau* mostTau = allTau.at(most_tauLike_loc);
    allTau.erase(allTau.begin() + most_tauLike_loc);
    allTau_tauness.erase(allTau_tauness.begin() + most_tauLike_loc);
    int secondMost_tauLike_loc = std::distance(allTau_tauness.begin(), std::max_element(allTau_tauness.begin(), allTau_tauness.end()));
    const RecoHadTau* secondMostTau = allTau.at(secondMost_tauLike_loc);
    // Preparations for SVFit
    double leg1Mass = mostTau->mass();
    if ( leg1Mass < classic_svFit::chargedPionMass ) leg1Mass = classic_svFit::chargedPionMass;
    if ( leg1Mass > 1.5                            ) leg1Mass = 1.5;
    classic_svFit::MeasuredTauLepton::kDecayType leg2Type = classic_svFit::MeasuredTauLepton::kTauToHadDecay;
    double leg2Mass = secondMostTau->mass();
    if ( leg2Mass < classic_svFit::chargedPionMass ) leg2Mass = classic_svFit::chargedPionMass;
    if ( leg2Mass > 1.5                            ) leg2Mass = 1.5;
    measuredTauLeptons.push_back(classic_svFit::MeasuredTauLepton(leg1Type, mostTau->pt(), mostTau->eta(), mostTau->phi(), leg1Mass));
    measuredTauLeptons.push_back(classic_svFit::MeasuredTauLepton(leg2Type, secondMostTau->pt(), secondMostTau->eta(), secondMostTau->phi(), leg2Mass));
    ClassicSVfit svFitAlgo;
    svFitAlgo.addLogM_dynamic(false);
    svFitAlgo.addLogM_fixed(true, 5.);
    svFitAlgo.integrate(measuredTauLeptons, met.p4().px(), met.p4().py(), met.cov());
    const double mTauTau   = ( svFitAlgo.isValidSolution() ) ? static_cast<classic_svFit::HistogramAdapterDiTau*>(svFitAlgo.getHistogramAdapter())->getMass() : -1.;


/* Smart pairing cases: deltaR, pt, similarity to Higgs, similarity to DY */

    const RecoHadTau* caseOnePairOne_lead;
    const RecoHadTau* caseOnePairOne_sublead;
    double caseOnePairOne_dr;
    double caseOnePairOne_pt;
    const RecoHadTau* caseOnePairTwo_lead;
    const RecoHadTau* caseOnePairTwo_sublead;
    double caseOnePairTwo_dr;
    double caseOnePairTwo_pt;


    const RecoHadTau* caseTwoPairOne_lead;
    const RecoHadTau* caseTwoPairOne_sublead;
    double caseTwoPairOne_dr;
    double caseTwoPairOne_pt;
    const RecoHadTau* caseTwoPairTwo_lead;
    const RecoHadTau* caseTwoPairTwo_sublead;
    double caseTwoPairTwo_dr;
    double caseTwoPairTwo_pt;

    double Zee_bestTauHPair_m;
    double Zee_bestTauHPair_dr;
    double Zee_bestTauHPair_dPhi;
    double Zee_bestTauHPair_dEta;
    double Zee_bestTauHPair_pt;
    double pt_bestTauHPair_m;
    double pt_bestTauHPair_dr;
    double pt_bestTauHPair_dPhi;
    double pt_bestTauHPair_dEta;
    double pt_bestTauHPair_pt;
    double dR_bestTauHPair_m;
    double dR_bestTauHPair_dr;
    double dR_bestTauHPair_dPhi;
    double dR_bestTauHPair_dEta;
    double dR_bestTauHPair_pt;
    double Zee_secondTauHPair_m;
    double Zee_secondTauHPair_dr;
    double Zee_secondTauHPair_dPhi;
    double Zee_secondTauHPair_dEta;
    double Zee_secondTauHPair_pt;
    double pt_secondTauHPair_m;
    double pt_secondTauHPair_dr;
    double pt_secondTauHPair_dPhi;
    double pt_secondTauHPair_dEta;
    double pt_secondTauHPair_pt;
    double dR_secondTauHPair_m;
    double dR_secondTauHPair_dr;
    double dR_secondTauHPair_dPhi;
    double dR_secondTauHPair_dEta;
    double dR_secondTauHPair_pt;

    if ( selHadTau_lead->charge() * selHadTau_sublead->charge() < 0 ){
        caseOnePairOne_lead = selHadTau_lead;
        caseOnePairOne_sublead = selHadTau_sublead;
        caseOnePairTwo_lead = selHadTau_third;
        caseOnePairTwo_sublead = selHadTau_fourth;
        if ( selHadTau_lead->charge() * selHadTau_third->charge() < 0 ){
            caseTwoPairOne_lead = selHadTau_lead;
            caseTwoPairOne_sublead = selHadTau_third;
            caseTwoPairTwo_lead = selHadTau_sublead;
            caseTwoPairTwo_sublead = selHadTau_fourth;
        } else {
            caseTwoPairOne_lead = selHadTau_lead;
            caseTwoPairOne_sublead = selHadTau_fourth;
            caseTwoPairTwo_lead = selHadTau_sublead;
            caseTwoPairTwo_sublead = selHadTau_third;
        }
    } else {
        caseOnePairOne_lead = selHadTau_lead;
        caseOnePairOne_sublead = selHadTau_third;
        caseOnePairTwo_lead = selHadTau_sublead;
        caseOnePairTwo_sublead = selHadTau_fourth;
        caseTwoPairOne_lead = selHadTau_lead;
        caseTwoPairOne_sublead = selHadTau_fourth;
        caseTwoPairTwo_lead = selHadTau_sublead;
        caseTwoPairTwo_sublead = selHadTau_third;
    }

    caseOnePairOne_dr = deltaR(caseOnePairOne_lead->p4(), caseOnePairOne_sublead->p4());
    caseOnePairTwo_dr = deltaR(caseOnePairTwo_lead->p4(), caseOnePairTwo_sublead->p4());
    caseTwoPairOne_dr = deltaR(caseTwoPairOne_lead->p4(), caseTwoPairOne_sublead->p4());
    caseTwoPairTwo_dr = deltaR(caseTwoPairTwo_lead->p4(), caseTwoPairTwo_sublead->p4());

    caseOnePairOne_pt = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).pt();
    caseOnePairTwo_pt = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).pt();
    caseTwoPairOne_pt = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).pt();
    caseTwoPairTwo_pt = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).pt();

/* Pair choices made, so that one of the pairs has the smallest deltaR and that the mass of at least one of the pair is roughly 125GeV */
    const double min_dR = std::min(std::min(caseOnePairOne_dr, caseOnePairTwo_dr), std::min(caseTwoPairOne_dr, caseTwoPairTwo_dr));
    if (min_dR == caseOnePairOne_dr || min_dR == caseOnePairTwo_dr){
        if ((caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass() - 125 < 10 || (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass() - 125 < 10){
            if (caseOnePairOne_dr < caseOnePairTwo_dr){
                dR_bestTauHPair_m = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass();
                dR_bestTauHPair_dr = deltaR(caseOnePairOne_lead->p4(), caseOnePairOne_sublead->p4());
                dR_bestTauHPair_dPhi = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).phi();
                dR_bestTauHPair_dEta = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).eta();
                dR_bestTauHPair_pt = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).pt();

                dR_secondTauHPair_m = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass();
                dR_secondTauHPair_dr = deltaR(caseOnePairTwo_lead->p4(), caseOnePairTwo_sublead->p4());
                dR_secondTauHPair_dPhi = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).phi();
                dR_secondTauHPair_dEta = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).eta();
                dR_secondTauHPair_pt = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).pt();
            } else {
                dR_bestTauHPair_m = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass();
                dR_bestTauHPair_dr = deltaR(caseOnePairTwo_lead->p4(), caseOnePairTwo_sublead->p4());
                dR_bestTauHPair_dPhi = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).phi();
                dR_bestTauHPair_dEta = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).eta();
                dR_bestTauHPair_pt = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).pt();

                dR_secondTauHPair_m = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass();
                dR_secondTauHPair_dr = deltaR(caseOnePairOne_lead->p4(), caseOnePairOne_sublead->p4());
                dR_secondTauHPair_dPhi = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).phi();
                dR_secondTauHPair_dEta = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).eta();
                dR_secondTauHPair_pt = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).pt();
            }
        } else {
            dR_bestTauHPair_m = 0;
            dR_bestTauHPair_dr = 0;
            dR_bestTauHPair_dPhi = 0;
            dR_bestTauHPair_dEta = 0;
            dR_bestTauHPair_pt = 0;

            dR_secondTauHPair_m = 0;
            dR_secondTauHPair_dr = 0;
            dR_secondTauHPair_dPhi = 0;
            dR_secondTauHPair_dEta = 0;
            dR_secondTauHPair_pt = 0;
        }
    } else{
        if ((caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass() - 125 < 10 || (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass() - 125 < 10){
            if (caseTwoPairOne_dr < caseTwoPairTwo_dr){
                dR_bestTauHPair_m = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass();
                dR_bestTauHPair_dr = deltaR(caseTwoPairOne_lead->p4(), caseTwoPairOne_sublead->p4());
                dR_bestTauHPair_dPhi = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).phi();
                dR_bestTauHPair_dEta = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).eta();
                dR_bestTauHPair_pt = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).pt();

                dR_secondTauHPair_m = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass();
                dR_secondTauHPair_dr = deltaR(caseTwoPairTwo_lead->p4(), caseTwoPairTwo_sublead->p4());
                dR_secondTauHPair_dPhi = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).phi();
                dR_secondTauHPair_dEta = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).eta();
                dR_secondTauHPair_pt = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).pt();
            } else {
                dR_bestTauHPair_m = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass();
                dR_bestTauHPair_dr = deltaR(caseTwoPairTwo_lead->p4(), caseTwoPairTwo_sublead->p4());
                dR_bestTauHPair_dPhi = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).phi();
                dR_bestTauHPair_dEta = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).eta();
                dR_bestTauHPair_pt = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).pt();

                dR_secondTauHPair_m = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass();
                dR_secondTauHPair_dr = deltaR(caseTwoPairOne_lead->p4(), caseTwoPairOne_sublead->p4());
                dR_secondTauHPair_dPhi = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).phi();
                dR_secondTauHPair_dEta = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).eta();
                dR_secondTauHPair_pt = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).pt();
            }
        } else {
            dR_bestTauHPair_m = 0;
            dR_bestTauHPair_dr = 0;
            dR_bestTauHPair_dPhi = 0;
            dR_bestTauHPair_dEta = 0;
            dR_bestTauHPair_pt = 0;

            dR_secondTauHPair_m = 0;
            dR_secondTauHPair_dr = 0;
            dR_secondTauHPair_dPhi = 0;
            dR_secondTauHPair_dEta = 0;
            dR_secondTauHPair_pt = 0;
        }
    }

/* Choices based on best deltaR pair end */



/* Pair choices made, so that one of the pairs has the biggest pt and that the mass of at least one of the pair is roughly 125GeV */
    double max_pt = std::max(std::max(caseOnePairOne_pt, caseOnePairTwo_pt), std::max(caseTwoPairOne_pt, caseTwoPairTwo_pt));
    if (max_pt == caseOnePairOne_pt || max_pt == caseOnePairTwo_pt){
        if ((caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass() - 125 < 10 || (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass() - 125 < 10){
            if (caseOnePairOne_dr > caseOnePairTwo_dr){
                pt_bestTauHPair_m = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass();
                pt_bestTauHPair_dr = deltaR(caseOnePairOne_lead->p4(), caseOnePairOne_sublead->p4());
                pt_bestTauHPair_dPhi = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).phi();
                pt_bestTauHPair_dEta = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).eta();
                pt_bestTauHPair_pt = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).pt();

                pt_secondTauHPair_m = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass();
                pt_secondTauHPair_dr = deltaR(caseOnePairTwo_lead->p4(), caseOnePairTwo_sublead->p4());
                pt_secondTauHPair_dPhi = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).phi();
                pt_secondTauHPair_dEta = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).eta();
                pt_secondTauHPair_pt = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).pt();
            } else {
                pt_bestTauHPair_m = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass();
                pt_bestTauHPair_dr = deltaR(caseOnePairTwo_lead->p4(), caseOnePairTwo_sublead->p4());
                pt_bestTauHPair_dPhi = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).phi();
                pt_bestTauHPair_dEta = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).eta();
                pt_bestTauHPair_pt = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).pt();

                pt_secondTauHPair_m = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass();
                pt_secondTauHPair_dr = deltaR(caseOnePairOne_lead->p4(), caseOnePairOne_sublead->p4());
                pt_secondTauHPair_dPhi = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).phi();
                pt_secondTauHPair_dEta = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).eta();
                pt_secondTauHPair_pt = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).pt();
            }
        } else {
            pt_bestTauHPair_m = 0;
            pt_bestTauHPair_dr = 0;
            pt_bestTauHPair_dPhi = 0;
            pt_bestTauHPair_dEta = 0;
            pt_bestTauHPair_pt = 0;

            pt_secondTauHPair_m = 0;
            pt_secondTauHPair_dr = 0;
            pt_secondTauHPair_dPhi = 0;
            pt_secondTauHPair_dEta = 0;
            pt_secondTauHPair_pt = 0;
        }
    } else{
        if ((caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass() - 125 < 10 || (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass() - 125 < 10){
            if (caseTwoPairOne_pt > caseTwoPairTwo_pt){
                pt_bestTauHPair_m = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass();
                pt_bestTauHPair_dr = deltaR(caseTwoPairOne_lead->p4(), caseTwoPairOne_sublead->p4());
                pt_bestTauHPair_dPhi = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).phi();
                pt_bestTauHPair_dEta = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).eta();
                pt_bestTauHPair_pt = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).pt();

                pt_secondTauHPair_m = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass();
                pt_secondTauHPair_dr = deltaR(caseTwoPairTwo_lead->p4(), caseTwoPairTwo_sublead->p4());
                pt_secondTauHPair_dPhi = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).phi();
                pt_secondTauHPair_dEta = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).eta();
                pt_secondTauHPair_pt = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).pt();
            } else {
                pt_bestTauHPair_m = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass();
                pt_bestTauHPair_dr = deltaR(caseTwoPairTwo_lead->p4(), caseTwoPairTwo_sublead->p4());
                pt_bestTauHPair_dPhi = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).phi();
                pt_bestTauHPair_dEta = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).eta();
                pt_bestTauHPair_pt = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).pt();

                pt_secondTauHPair_m = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass();
                pt_secondTauHPair_dr = deltaR(caseTwoPairOne_lead->p4(), caseTwoPairOne_sublead->p4());
                pt_secondTauHPair_dPhi = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).phi();
                pt_secondTauHPair_dEta = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).eta();
                pt_secondTauHPair_pt = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).pt();
            }
        } else {
            pt_bestTauHPair_m = 0;
            pt_bestTauHPair_dr = 0;
            pt_bestTauHPair_dPhi = 0;
            pt_bestTauHPair_dEta = 0;
            pt_bestTauHPair_pt = 0;

            pt_secondTauHPair_m = 0;
            pt_secondTauHPair_dr = 0;
            pt_secondTauHPair_dPhi = 0;
            pt_secondTauHPair_dEta = 0;
            pt_secondTauHPair_pt = 0;
        }
    }

/* Choices based on biggest pt pair end */


/* Find Z->ee like events */


    const double caseOnePairOne_massZee = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass() - 90;
    const double caseOnePairTwo_massZee = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass() - 90;
    const double caseTwoPairOne_massZee = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass() - 90;
    const double caseTwoPairTwo_massZee = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass() - 90;

    const double mostZeeLike = std::min(std::min(caseOnePairOne_massZee, caseOnePairTwo_massZee), std::min(caseTwoPairOne_massZee, caseTwoPairTwo_dr));

    if (mostZeeLike == caseOnePairOne_massZee || mostZeeLike == caseOnePairTwo_massZee){
        if (caseOnePairOne_massZee < caseOnePairTwo_massZee){
            Zee_bestTauHPair_m = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass();
            Zee_bestTauHPair_dr = deltaR(caseOnePairOne_lead->p4(), caseOnePairOne_sublead->p4());
            Zee_bestTauHPair_dPhi = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).phi();
            Zee_bestTauHPair_dEta = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).eta();
            Zee_bestTauHPair_pt = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).pt();

            Zee_secondTauHPair_m = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass();
            Zee_secondTauHPair_dr = deltaR(caseOnePairTwo_lead->p4(), caseOnePairTwo_sublead->p4());
            Zee_secondTauHPair_dPhi = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).phi();
            Zee_secondTauHPair_dEta = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).eta();
            Zee_secondTauHPair_pt = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).pt();
        } else {
            Zee_bestTauHPair_m = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).mass();
            Zee_bestTauHPair_dr = deltaR(caseOnePairTwo_lead->p4(), caseOnePairTwo_sublead->p4());
            Zee_bestTauHPair_dPhi = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).phi();
            Zee_bestTauHPair_dEta = (caseOnePairTwo_lead->p4() - caseOnePairTwo_sublead->p4()).eta();
            Zee_bestTauHPair_pt = (caseOnePairTwo_lead->p4() + caseOnePairTwo_sublead->p4()).pt();

            Zee_secondTauHPair_m = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).mass();
            Zee_secondTauHPair_dr = deltaR(caseOnePairOne_lead->p4(), caseOnePairOne_sublead->p4());
            Zee_secondTauHPair_dPhi = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).phi();
            Zee_secondTauHPair_dEta = (caseOnePairOne_lead->p4() - caseOnePairOne_sublead->p4()).eta();
            Zee_secondTauHPair_pt = (caseOnePairOne_lead->p4() + caseOnePairOne_sublead->p4()).pt();
            }
    } else {
        if (caseTwoPairOne_massZee < caseTwoPairTwo_massZee){
            Zee_bestTauHPair_m = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass();
            Zee_bestTauHPair_dr = deltaR(caseTwoPairOne_lead->p4(), caseTwoPairOne_sublead->p4());
            Zee_bestTauHPair_dPhi = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).phi();
            Zee_bestTauHPair_dEta = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).eta();
            Zee_bestTauHPair_pt = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).pt();

            Zee_secondTauHPair_m = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass();
            Zee_secondTauHPair_dr = deltaR(caseTwoPairTwo_lead->p4(), caseTwoPairTwo_sublead->p4());
            Zee_secondTauHPair_dPhi = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).phi();
            Zee_secondTauHPair_dEta = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).eta();
            Zee_secondTauHPair_pt = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).pt();
        } else {
            Zee_bestTauHPair_m = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).mass();
            Zee_bestTauHPair_dr = deltaR(caseTwoPairTwo_lead->p4(), caseTwoPairTwo_sublead->p4());
            Zee_bestTauHPair_dPhi = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).phi();
            Zee_bestTauHPair_dEta = (caseTwoPairTwo_lead->p4() - caseTwoPairTwo_sublead->p4()).eta();
            Zee_bestTauHPair_pt = (caseTwoPairTwo_lead->p4() + caseTwoPairTwo_sublead->p4()).pt();

            Zee_secondTauHPair_m = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).mass();
            Zee_secondTauHPair_dr = deltaR(caseTwoPairOne_lead->p4(), caseTwoPairOne_sublead->p4());
            Zee_secondTauHPair_dPhi = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).phi();
            Zee_secondTauHPair_dEta = (caseTwoPairOne_lead->p4() - caseTwoPairOne_sublead->p4()).eta();
            Zee_secondTauHPair_pt = (caseTwoPairOne_lead->p4() + caseTwoPairOne_sublead->p4()).pt();
        }
    }

    AllVars_Map["tau1_pt"] =  selHadTau_lead->pt();
    AllVars_Map["tau1_eta"] = selHadTau_lead->eta();
    AllVars_Map["tau1_phi"] = selHadTau_lead->phi();
    AllVars_Map["tau1_raw"] = selHadTau_lead->raw_mva();
    AllVars_Map["tau2_pt"] = selHadTau_sublead->pt();
    AllVars_Map["tau2_eta"] =  selHadTau_sublead->eta();
    AllVars_Map["tau2_phi"] = selHadTau_lead->phi();
    AllVars_Map["tau2_raw"] = selHadTau_sublead->raw_mva();
    AllVars_Map["tau3_pt"] = selHadTau_third->pt();
    AllVars_Map["tau3_eta"] = selHadTau_third->eta();
    AllVars_Map["tau3_phi"] = selHadTau_third->phi();
    AllVars_Map["tau3_raw"] = selHadTau_third->raw_mva();
    AllVars_Map["tau4_pt"] = selHadTau_fourth->pt();
    AllVars_Map["tau4_eta"] = selHadTau_fourth->eta();
    AllVars_Map["tau4_phi"] = selHadTau_fourth->phi();
    AllVars_Map["tau4_raw"] = selHadTau_fourth->raw_mva();
    AllVars_Map["tau1_mva"] = tau1_mva;
    AllVars_Map["tau2_mva"] = tau2_mva;
    AllVars_Map["tau3_mva"] = tau3_mva;
    AllVars_Map["tau4_mva"] = tau4_mva;
    AllVars_Map["diHiggsVisMass"] = dihiggsVisMass_sel;
    AllVars_Map["diHiggsMass"] = dihiggsMass;
    AllVars_Map["mTauTau"] = mTauTau;
    AllVars_Map["avg_dr_jet"] = avg_dr_jet;
    AllVars_Map["STMET"] = STMET;
    AllVars_Map["HT"] = HT;
    AllVars_Map["met_LD"] = met_LD;
    AllVars_Map["mht"] = mht_p4.pt();
    AllVars_Map["met_phi"] = met.phi();
    AllVars_Map["met"] = met.pt();
    AllVars_Map["pt_HH_recoil"] = pt_HH_recoil;
    AllVars_Map["deltaEta_tau1_tau2"] = deltaEta_tau1_tau2;
    AllVars_Map["deltaEta_tau1_tau3"] = deltaEta_tau1_tau3;
    AllVars_Map["deltaEta_tau1_tau4"] = deltaEta_tau1_tau4;
    AllVars_Map["deltaEta_tau2_tau3"] = deltaEta_tau2_tau3;
    AllVars_Map["deltaEta_tau2_tau4"] = deltaEta_tau2_tau4;
    AllVars_Map["deltaEta_tau3_tau4"] = deltaEta_tau3_tau4;
    AllVars_Map["deltaPhi_tau1_tau2"] = deltaPhi_tau1_tau2;
    AllVars_Map["deltaPhi_tau1_tau3"] = deltaPhi_tau1_tau3;
    AllVars_Map["deltaPhi_tau1_tau4"] = deltaPhi_tau1_tau4;
    AllVars_Map["deltaPhi_tau2_tau3"] = deltaPhi_tau2_tau3;
    AllVars_Map["deltaPhi_tau2_tau4"] = deltaPhi_tau2_tau4;
    AllVars_Map["deltaPhi_tau3_tau4"] = deltaPhi_tau3_tau4;
    AllVars_Map["dr_tau1_tau2"] = dr_tau1_tau2;
    AllVars_Map["dr_tau1_tau3"] = dr_tau1_tau3;
    AllVars_Map["dr_tau1_tau4"] = dr_tau1_tau4;
    AllVars_Map["dr_tau2_tau3"] = dr_tau2_tau3;
    AllVars_Map["dr_tau2_tau4"] = dr_tau2_tau4;
    AllVars_Map["dr_tau3_tau4"] = dr_tau3_tau4;
    AllVars_Map["m_tau1_tau2"] = m_tau1_tau2;
    AllVars_Map["m_tau1_tau3"] = m_tau1_tau3;
    AllVars_Map["m_tau1_tau4"] = m_tau1_tau4;
    AllVars_Map["m_tau2_tau3"] = m_tau2_tau3;
    AllVars_Map["m_tau2_tau4"] = m_tau2_tau4;
    AllVars_Map["m_tau3_tau4"] = m_tau3_tau4;
    AllVars_Map["Zee_bestTauHPair_m"] = Zee_bestTauHPair_m;
    AllVars_Map["Zee_bestTauHPair_dr"] = Zee_bestTauHPair_dr;
    AllVars_Map["Zee_bestTauHPair_dPhi"] = Zee_bestTauHPair_dPhi;
    AllVars_Map["Zee_bestTauHPair_dEta"] = Zee_bestTauHPair_dEta;
    AllVars_Map["Zee_bestTauHPair_pt"] = Zee_bestTauHPair_pt;
    AllVars_Map["mostZeeLike"] = mostZeeLike;
    AllVars_Map["pt_bestTauHPair_m"] = pt_bestTauHPair_m;
    AllVars_Map["pt_bestTauHPair_dr"] = pt_bestTauHPair_dr;
    AllVars_Map["pt_bestTauHPair_dPhi"] = pt_bestTauHPair_dPhi;
    AllVars_Map["pt_bestTauHPair_dEta"] = pt_bestTauHPair_dEta;
    AllVars_Map["pt_bestTauHPair_pt"] = pt_bestTauHPair_pt;
    AllVars_Map["Zee_secondTauHPair_m"] = Zee_secondTauHPair_m;
    AllVars_Map["Zee_secondTauHPair_dr"] = Zee_secondTauHPair_dr;
    AllVars_Map["Zee_secondTauHPair_dPhi"] = Zee_secondTauHPair_dPhi;
    AllVars_Map["Zee_secondTauHPair_dEta"] = Zee_secondTauHPair_dEta;
    AllVars_Map["Zee_secondTauHPair_pt"] = Zee_secondTauHPair_pt;
    AllVars_Map["dr_bestTauHPair_m"] = dR_bestTauHPair_m;
    AllVars_Map["dr_bestTauHPair_dr"] = dR_bestTauHPair_dr;
    AllVars_Map["dr_bestTauHPair_dPhi"] = dR_bestTauHPair_dPhi;
    AllVars_Map["dr_bestTauHPair_dEta"] = dR_bestTauHPair_dEta;
    AllVars_Map["dr_bestTauHPair_pt"] = dR_bestTauHPair_pt;
    AllVars_Map["pt_secondTauHPair_m"] = pt_secondTauHPair_m;
    AllVars_Map["pt_secondTauHPair_dr"] = pt_secondTauHPair_dr;
    AllVars_Map["pt_secondTauHPair_dPhi"] = pt_secondTauHPair_dPhi;
    AllVars_Map["pt_secondTauHPair_dEta"] = pt_secondTauHPair_dEta;
    AllVars_Map["pt_secondTauHPair_pt"] = pt_secondTauHPair_pt;
    AllVars_Map["dr_secondTauHPair_m"] = dR_secondTauHPair_m;
    AllVars_Map["dr_secondTauHPair_dr"] = dR_secondTauHPair_dr;
    AllVars_Map["dr_secondTauHPair_dPhi"] = dR_secondTauHPair_dPhi;
    AllVars_Map["dr_secondTauHPair_dEta"] = dR_secondTauHPair_dEta;
    AllVars_Map["dr_secondTauHPair_pt"] = dR_secondTauHPair_pt;
    AllVars_Map["max_pt_pair_pt"] = max_pt;
    AllVars_Map["min_dr_pair_dr"] = min_dR;
    AllVars_Map["nJet"] = selJets.size();
    AllVars_Map["nBJet_loose"] = selBJets_btag_loose.size();
    AllVars_Map["nBJet_medium"] =  selBJets_btag_medium.size();
    AllVars_Map["gen_mHH"] = 250.; // setting a Dummy value which will be reset depending on mass hypothesis 

    std::map<std::string, double> BDTInputs_SUM_spin2 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_SUM_spin2);
    std::map<std::string, double> BDTInputs_SUM_spin0 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_SUM_spin0);

    BDTOutput_SUM_Map_spin2 = CreateBDTOutputMap(gen_mHH, BDT_SUM_spin2, BDTInputs_SUM_spin2, "hypo_spin2", eventInfo.event);
    BDTOutput_SUM_Map_spin0 = CreateBDTOutputMap(gen_mHH, BDT_SUM_spin0, BDTInputs_SUM_spin0, "hypo_spin0", eventInfo.event);
    // -------------------------------


//--- retrieve gen-matching flags
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selHadTaus);

//--- fill histograms with events passing final selection
    for(const std::string & central_or_shift: central_or_shifts_local)
    {
      const double evtWeight = evtWeightRecorder.get(central_or_shift);
      const bool skipFilling = central_or_shift != central_or_shift_main;
      for (const GenMatchEntry* genMatch : genMatches)
      {
        selHistManagerType* selHistManager = selHistManagers[central_or_shift][genMatch->getIdx()];
        assert(selHistManager);
        if(! skipFilling)
        {
          selHistManager->electrons_->fillHistograms(preselElectrons, evtWeight);
          selHistManager->muons_->fillHistograms(preselMuons, evtWeight);
          selHistManager->hadTaus_->fillHistograms({ selHadTau_lead, selHadTau_sublead, selHadTau_third, selHadTau_fourth }, evtWeight);
          selHistManager->leadHadTau_->fillHistograms({ selHadTau_lead }, evtWeight);
          selHistManager->subleadHadTau_->fillHistograms({ selHadTau_sublead }, evtWeight);
          selHistManager->thirdHadTau_->fillHistograms({ selHadTau_third }, evtWeight);
          selHistManager->fourthHadTau_->fillHistograms({ selHadTau_fourth }, evtWeight);
          selHistManager->jets_->fillHistograms(selJets, evtWeight);
          selHistManager->BJets_loose_->fillHistograms(selBJets_loose, evtWeight);
          selHistManager->BJets_medium_->fillHistograms(selBJets_medium, evtWeight);
          selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
        }
        for(const auto & kv: reWeightMapHH)
        {
          selHistManager->evt_[kv.first]->fillHistograms(
            preselElectrons.size(),
            preselMuons.size(),
            selHadTaus.size(),
            selJets.size(),
            numSelJetsPtGt40,
            selBJets_loose.size(),
            selBJets_medium.size(),
            dihiggsVisMass_sel,
            dihiggsMass,
            HT,
            STMET,
            BDTOutput_SUM_Map_spin2,
            BDTOutput_SUM_Map_spin0,
            eventInfo.event,
            kv.second
          );
          selHistManager->svFit4tau_woMassConstraint_[kv.first]->fillHistograms(svFit4tauResults_woMassConstraint, kv.second);
          selHistManager->svFit4tau_wMassConstraint_[kv.first]->fillHistograms(svFit4tauResults_wMassConstraint, kv.second);

          if( isSignal ) {
            const std::string decayModeStr = eventInfo.getDiHiggsDecayModeString();
            if ( !decayModeStr.empty() ) {
              selHistManager->evt_in_decayModes_[kv.first][decayModeStr]->fillHistograms(
                preselElectrons.size(),
                preselMuons.size(),
                selHadTaus.size(),
                selJets.size(),
                numSelJetsPtGt40,
                selBJets_loose.size(),
                selBJets_medium.size(),
                dihiggsVisMass_sel,
                dihiggsMass,
                HT,
                STMET,
                BDTOutput_SUM_Map_spin2,
                BDTOutput_SUM_Map_spin0,
                eventInfo.event,
                kv.second
              );
              selHistManager->svFit4tau_woMassConstraint_in_decayModes_[kv.first][decayModeStr]->fillHistograms(
                svFit4tauResults_woMassConstraint, kv.second
              );
              selHistManager->svFit4tau_wMassConstraint_in_decayModes_[kv.first][decayModeStr]->fillHistograms(
                svFit4tauResults_wMassConstraint, kv.second
              );
            }
          }
        }

        if(! skipFilling)
        {
          selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
          selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
          selHistManager->weights_->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
          selHistManager->weights_->fillHistograms("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift));
          selHistManager->weights_->fillHistograms("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift));
          selHistManager->weights_->fillHistograms("hadTauEff", evtWeightRecorder.get_tauSF(central_or_shift));
          selHistManager->weights_->fillHistograms("fakeRate", evtWeightRecorder.get_FR(central_or_shift));
        }
      }

      if(isMC && ! skipFilling)
      {
        genEvtHistManager_afterCuts[central_or_shift]->fillHistograms(
          genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
        );
        lheInfoHistManager[central_or_shift]->fillHistograms(*lheInfoReader, evtWeight);
        if(eventWeightManager)
        {
          genEvtHistManager_afterCuts[central_or_shift]->fillHistograms(
            eventWeightManager, evtWeightRecorder.get_inclusive(central_or_shift)
          );
        }
      }

      if(bdt_filler)
      {
        double hadTau1_genPt = 0.;
        if(selHadTau_lead->genHadTau()) hadTau1_genPt =  selHadTau_lead->genHadTau()->pt();
        else if ( selHadTau_lead->genLepton()) hadTau1_genPt =  selHadTau_lead->genLepton()->pt();

        double hadTau2_genPt = 0.;
        if(selHadTau_sublead->genHadTau()) hadTau2_genPt =  selHadTau_sublead->genHadTau()->pt();
        else if ( selHadTau_sublead->genLepton()) hadTau2_genPt =  selHadTau_sublead->genLepton()->pt();
        double hadTau3_genPt = 0.;
        if(selHadTau_third->genHadTau()) hadTau3_genPt =  selHadTau_third->genHadTau()->pt();
        else if ( selHadTau_third->genLepton()) hadTau3_genPt =  selHadTau_third->genLepton()->pt();

        double hadTau4_genPt = 0.;
        if(selHadTau_fourth->genHadTau()) hadTau4_genPt =  selHadTau_fourth->genHadTau()->pt();
        else if ( selHadTau_fourth->genLepton()) hadTau4_genPt =  selHadTau_fourth->genLepton()->pt();
        double prob_fake_tau_lead = evtWeightRecorder.get_jetToTau_FR_lead(central_or_shift_main);
        double prob_fake_tau_sublead = evtWeightRecorder.get_jetToTau_FR_sublead(central_or_shift_main);
        double prob_fake_tau_third = evtWeightRecorder.get_jetToTau_FR_third(central_or_shift_main);
        double prob_fake_tau_fourth = evtWeightRecorder.get_jetToTau_FR_fourth(central_or_shift_main);
        double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
        double hadTau1_frWeight = hadTau1_genPt > 0 ? 1.0 : prob_fake_tau_lead;
        double hadTau2_frWeight = hadTau2_genPt > 0 ? 1.0 : prob_fake_tau_sublead;
        double hadTau3_frWeight = hadTau3_genPt > 0 ? 1.0 : prob_fake_tau_third;
        double hadTau4_frWeight = hadTau4_genPt > 0 ? 1.0 : prob_fake_tau_fourth;
        evtWeight_BDT *= hadTau1_frWeight*hadTau2_frWeight*hadTau3_frWeight*hadTau4_frWeight;

        bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
            ("tau1_pt",                  selHadTau_lead->pt())
            ("tau1_eta",                 selHadTau_lead->eta())
            ("tau1_phi",                 selHadTau_lead->phi())
            ("tau1_raw",                 selHadTau_lead->raw_mva())
            ("tau2_pt",                  selHadTau_sublead->pt())
            ("tau2_eta",                 selHadTau_sublead->eta())
            ("tau2_phi",                 selHadTau_lead->phi())
            ("tau2_raw",                 selHadTau_sublead->raw_mva())
            ("tau3_pt",                  selHadTau_third->pt())
            ("tau3_eta",                 selHadTau_third->eta())
            ("tau3_phi",                 selHadTau_third->phi())
            ("tau3_raw",                 selHadTau_third->raw_mva())
            ("tau4_pt",                  selHadTau_fourth->pt())
            ("tau4_eta",                 selHadTau_fourth->eta())
            ("tau4_phi",                 selHadTau_fourth->phi())
            ("tau4_raw",                 selHadTau_fourth->raw_mva())
            ("tau1_mva",                 tau1_mva)
            ("tau2_mva",                 tau2_mva)
            ("tau3_mva",                 tau3_mva)
            ("tau4_mva",                 tau4_mva)
            ("diHiggsVisMass",           dihiggsVisMass_sel)
            ("diHiggsMass",              dihiggsMass)
            ("mTauTau",                  mTauTau)
            ("avg_dr_jet",               avg_dr_jet)
            ("STMET",                    STMET)
            ("HT",                       HT)
            ("met_LD",                   met_LD)
            ("mht",                      mht_p4.pt())
            ("met_phi",                  met.phi())
            ("met",                      met.pt())
            ("pt_HH_recoil",             pt_HH_recoil)
            ("deltaEta_tau1_tau2",       deltaEta_tau1_tau2)
            ("deltaEta_tau1_tau3",       deltaEta_tau1_tau3)
            ("deltaEta_tau1_tau4",       deltaEta_tau1_tau4)
            ("deltaEta_tau2_tau3",       deltaEta_tau2_tau3)
            ("deltaEta_tau2_tau4",       deltaEta_tau2_tau4)
            ("deltaEta_tau3_tau4",       deltaEta_tau3_tau4)
            ("deltaPhi_tau1_tau2",       deltaPhi_tau1_tau2)
            ("deltaPhi_tau1_tau3",       deltaPhi_tau1_tau3)
            ("deltaPhi_tau1_tau4",       deltaPhi_tau1_tau4)
            ("deltaPhi_tau2_tau3",       deltaPhi_tau2_tau3)
            ("deltaPhi_tau2_tau4",       deltaPhi_tau2_tau4)
            ("deltaPhi_tau3_tau4",       deltaPhi_tau3_tau4)
            ("dr_tau1_tau2",             dr_tau1_tau2)
            ("dr_tau1_tau3",             dr_tau1_tau3)
            ("dr_tau1_tau4",             dr_tau1_tau4)
            ("dr_tau2_tau3",             dr_tau2_tau3)
            ("dr_tau2_tau4",             dr_tau2_tau4)
            ("dr_tau3_tau4",             dr_tau3_tau4)
            ("m_tau1_tau2",              m_tau1_tau2)
            ("m_tau1_tau3",              m_tau1_tau3)
            ("m_tau1_tau4",              m_tau1_tau4)
            ("m_tau2_tau3",              m_tau2_tau3)
            ("m_tau2_tau4",              m_tau2_tau4)
            ("m_tau3_tau4",              m_tau3_tau4)
            ("Zee_bestTauHPair_m",       Zee_bestTauHPair_m)
            ("Zee_bestTauHPair_dr",      Zee_bestTauHPair_dr)
            ("Zee_bestTauHPair_dPhi",    Zee_bestTauHPair_dPhi)
            ("Zee_bestTauHPair_dEta",    Zee_bestTauHPair_dEta)
            ("Zee_bestTauHPair_pt",      Zee_bestTauHPair_pt)
            ("mostZeeLike",              mostZeeLike)
            ("pt_bestTauHPair_m",        pt_bestTauHPair_m)
            ("pt_bestTauHPair_dr",       pt_bestTauHPair_dr)
            ("pt_bestTauHPair_dPhi",     pt_bestTauHPair_dPhi)
            ("pt_bestTauHPair_dEta",     pt_bestTauHPair_dEta)
            ("pt_bestTauHPair_pt",       pt_bestTauHPair_pt)
            ("Zee_secondTauHPair_m",     Zee_secondTauHPair_m)
            ("Zee_secondTauHPair_dr",    Zee_secondTauHPair_dr)
            ("Zee_secondTauHPair_dPhi",  Zee_secondTauHPair_dPhi)
            ("Zee_secondTauHPair_dEta",  Zee_secondTauHPair_dEta)
            ("Zee_secondTauHPair_pt",    Zee_secondTauHPair_pt)
            ("dr_bestTauHPair_m",        dR_bestTauHPair_m)
            ("dr_bestTauHPair_dr",       dR_bestTauHPair_dr)
            ("dr_bestTauHPair_dPhi",     dR_bestTauHPair_dPhi)
            ("dr_bestTauHPair_dEta",     dR_bestTauHPair_dEta)
            ("dr_bestTauHPair_pt",       dR_bestTauHPair_pt)
            ("pt_secondTauHPair_m",      pt_secondTauHPair_m)
            ("pt_secondTauHPair_dr",     pt_secondTauHPair_dr)
            ("pt_secondTauHPair_dPhi",   pt_secondTauHPair_dPhi)
            ("pt_secondTauHPair_dEta",   pt_secondTauHPair_dEta)
            ("pt_secondTauHPair_pt",     pt_secondTauHPair_pt)
            ("dr_secondTauHPair_m",      dR_secondTauHPair_m)
            ("dr_secondTauHPair_dr",     dR_secondTauHPair_dr)
            ("dr_secondTauHPair_dPhi",   dR_secondTauHPair_dPhi)
            ("dr_secondTauHPair_dEta",   dR_secondTauHPair_dEta)
            ("dr_secondTauHPair_pt",     dR_secondTauHPair_pt)
            ("max_pt_pair_pt",           max_pt)
            ("min_dr_pair_dr",           min_dR)
            ("nJet",                     selJets.size())
            ("nBJet_loose",              selBJets_btag_loose.size())
            ("nBJet_medium",             selBJets_btag_medium.size())
            ("hadTau1_frWeight",       hadTau1_frWeight)
            ("hadTau2_frWeight",       hadTau2_frWeight)
            ("hadTau3_frWeight",       hadTau3_frWeight)
            ("hadTau4_frWeight",       hadTau4_frWeight)
            ("genWeight", eventInfo.genWeight)
            ("lheWeight", evtWeightRecorder.get_lheScaleWeight(central_or_shift_main))
            ("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift_main))
            ("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift_main))
            ("btagWeight", evtWeightRecorder.get_btag(central_or_shift_main))
            ("hadTauEffSF", evtWeightRecorder.get_tauSF(central_or_shift_main))
            ("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift_main))
            ("FR_Weight", evtWeightRecorder.get_FR(central_or_shift_main))
            ("evtWeight",           evtWeight_BDT)
            (weightMapHH)
          .fill()
          ;

      }
    }

    if ( selEventsFile ) {
      (*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':' << eventInfo.event << '\n';
    }

    ++selectedEntries;
    selectedEntries_weighted += evtWeightRecorder.get(central_or_shift_main);
    std::string process_and_genMatch = process_string;
    process_and_genMatch += selHadTau_genMatch.name_;
    ++selectedEntries_byGenMatchType[process_and_genMatch]; 
    for(const std::string & central_or_shift: central_or_shifts_local)
    {
      selectedEntries_weighted_byGenMatchType[central_or_shift][process_and_genMatch] += evtWeightRecorder.get(central_or_shift);
    }
    histogram_selectedEntries->Fill(0.);
  }

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n\n"
            << "cut-flow table" << std::endl;
  cutFlowTable.print(std::cout);
  std::cout << std::endl;

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    std::cout << "central_or_shift = " << central_or_shift << '\n';
    for(const hadTauGenMatchEntry & hadTauGenMatch_definition: hadTauGenMatch_definitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += hadTauGenMatch_definition.name_;
      std::cout << " " << process_and_genMatch << " = " << selectedEntries_byGenMatchType[process_and_genMatch]
                << " (weighted = " << selectedEntries_weighted_byGenMatchType[central_or_shift][process_and_genMatch] << ")\n";
    }
  }
  std::cout << std::endl;

//--- manually write histograms to output file
  fs.file().cd();
  //histogram_analyzedEntries->Write();
  //histogram_selectedEntries->Write();
  HistManagerBase::writeHistograms();

//--- memory clean-up
  delete dataToMCcorrectionInterface;
  delete dataToMCcorrectionInterface_hh_0l_4tau_trigger;

  delete jetToTauFakeRateInterface_passesTrigger;
  delete jetToTauFakeRateInterface_failsTrigger;

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete hadTauReader;
  delete jetReader;
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genJetReader;
  delete lheInfoReader;
  delete psWeightReader;

  delete bdt_filler;
  for(auto & kv: genEvtHistManager_beforeCuts)
  {
    delete kv.second;
  }
  for(auto & kv: genEvtHistManager_afterCuts)
  {
    delete kv.second;
  }
  for(auto & kv: lheInfoHistManager)
  {
    delete kv.second;
  }
  delete cutFlowHistManager;
  delete eventWeightManager;

  hltPaths_delete(triggers_2tau);
  
  delete inputTree;
  
  clock.Show("analyze_hh_0l_4tau");

  return EXIT_SUCCESS;
}
