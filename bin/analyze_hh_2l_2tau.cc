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
#include <TLorentzVector.h> // TLorentzVector
#include <TROOT.h> // TROOT

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicity.h" // ObjectMultiplicity
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h" // JetToTauFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterReader.h" // MEtFilterReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
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
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_3lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/hadTauGenMatchingAuxFunctions.h" // getHadTauGenMatch_definitions_3tau, getHadTauGenMatch_string, getHadTauGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/hltPath.h" // hltPath, create_hltPaths, hltPaths_isTriggered, hltPaths_delete
#include "tthAnalysis/HiggsToTauTau/interface/hltPathReader.h" // hltPathReader
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2016.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2017.h"
#include "tthAnalysis/HiggsToTauTau/interface/Data_to_MC_CorrectionInterface_2018.h"
#include "tthAnalysis/HiggsToTauTau/interface/lutAuxFunctions.h" // loadTH2, get_sf_from_TH2
#include "tthAnalysis/HiggsToTauTau/interface/cutFlowTable.h" // cutFlowTableType
#include "tthAnalysis/HiggsToTauTau/interface/L1PreFiringWeightReader.h" // L1PreFiringWeightReader
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/hltFilter.h" // hltFilter()
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_*()
#include "tthAnalysis/HiggsToTauTau/interface/Topness.h" // Topness
#include "tthAnalysis/HiggsToTauTau/interface/backgroundEstimation.h" // prob_chargeMisId
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface_2.h" // HHWeightInterface
#include "tthAnalysis/HiggsToTauTau/interface/BM_list.h" // BMS
#include "tthAnalysis/HiggsToTauTau/interface/TensorFlowInterface.h" // TensorFlowInterface
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility

#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2l_2tau.h" // EvtHistManager_hh_2l_2tau
#include "hhAnalysis/multilepton/interface/SVfit4tauHistManager_MarkovChain.h" // SVfit4tauHistManager_MarkovChain
#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // getMeasuredTauLeptonType, getHadTauDecayMode
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "TauAnalysis/ClassicSVfit4tau/interface/svFitHistogramAdapter4tau.h" // HistogramAdapterDiHiggs, HistogramAdapterHiggs

#include "TauAnalysis/ClassicSVfit/interface/ClassicSVfit.h" // ClassicSVfit
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit/interface/svFitHistogramAdapter.h"
#include "TauAnalysis/ClassicSVfit/interface/svFitAuxFunctions.h"

#include <boost/range/algorithm/copy.hpp> // boost::copy()
#include <boost/range/adaptor/map.hpp> // boost::adaptors::map_keys
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

#include <sstream>
#include <map>
#include <iterator>


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

enum { kFR_disabled, kFR_2lepton, kFR_4L, kFR_2tau };

//const int hadTauSelection_antiElectron = 1; // vLoose
//const int hadTauSelection_antiMuon = 1; // Loose
const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied

struct HadTauHistManagerWrapper_eta
{
  HadTauHistManager* histManager_;
  double etaMin_;
  double etaMax_;
};

/**
 * @brief Produce datacard and control plots for 2l_2tau category of HH "multilepton" (HH->WWWW,WWtt,tttt) analysis.
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

  std::cout << "<analyze_hh_2l_2tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_2l_2tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_2l_2tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_2l_2tau");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isMC_ttH = process_string == "TTH";
  bool isMC_tH = process_string == "TH";
  bool isMC_EWK = process_string == "WZ" || process_string == "ZZ";
  bool isSignal = boost::starts_with(process_string, "signal_") && process_string.find("_hh_") != std::string::npos;
  bool isHH_rwgt_allowed = boost::starts_with(process_string, "signal_ggf_nonresonant_") && process_string.find("cHHH") == std::string::npos;

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;
  bool isMCClosure_t = histogramDir.find("mcClosure_t") != std::string::npos;

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e);
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e);
  bool use_triggers_2e = cfg_analyze.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu);
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu);
  bool use_triggers_2mu = cfg_analyze.getParameter<bool>("use_triggers_2mu");
  vstring triggerNames_1e1mu = cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu);
  bool use_triggers_1e1mu = cfg_analyze.getParameter<bool>("use_triggers_1e1mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_2e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_1e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");

  enum { kOS, kSS, kDisabled };
  std::string leptonChargeSelection_string = cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS"       ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS"       ) leptonChargeSelection = kSS;
  else if ( leptonChargeSelection_string == "disabled" ) leptonChargeSelection = kDisabled;
  else throw cms::Exception("analyze_hh_2l_2tau")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";
  std::string hadTauChargeSelection_string = cfg_analyze.getParameter<std::string>("hadTauChargeSelection");
  int hadTauChargeSelection = -1;
  if      ( hadTauChargeSelection_string == "OS"       ) hadTauChargeSelection = kOS;
  else if ( hadTauChargeSelection_string == "SS"       ) hadTauChargeSelection = kSS;
  else if ( hadTauChargeSelection_string == "disabled" ) hadTauChargeSelection = kDisabled;
  else throw cms::Exception("analyze_hh_2l_2tau")
    << "Invalid Configuration parameter 'hadTauChargeSelection' = " << hadTauChargeSelection_string << " !!\n";

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonChargeFlipGenMatchEntry> leptonGenMatch_definitions = getLeptonChargeFlipGenMatch_definitions_2lepton(true);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

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
  std::vector<hadTauGenMatchEntry> hadTauGenMatch_definitions = getHadTauGenMatch_definitions_2tau(true);
  std::cout << "hadTauGenMatch_definitions:" << std::endl;
  std::cout << hadTauGenMatch_definitions;

  GenMatchInterface genMatchInterface(2, apply_leptonGenMatching, true, 2, apply_hadTauGenMatching);

  std::string chargeSumSelection_string = cfg_analyze.getParameter<std::string>("chargeSumSelection");
  int chargeSumSelection = -1;
  if      ( chargeSumSelection_string == "OS"       ) chargeSumSelection = kOS;
  else if ( chargeSumSelection_string == "SS"       ) chargeSumSelection = kSS;
  else if ( chargeSumSelection_string == "disabled" ) chargeSumSelection = kDisabled;
  else throw cms::Exception("analyze_hh_2l_2tau")
    << "Invalid Configuration parameter 'chargeSumSelection' = " << chargeSumSelection_string << " !!\n";
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
  bool apply_hadTauFakeRateSF = cfg_analyze.getParameter<bool>("apply_hadTauFakeRateSF");
  const bool useNonNominal = cfg_analyze.getParameter<bool>("useNonNominal");
  const bool useNonNominal_jetmet = useNonNominal || ! isMC;
  bool invert_ZbosonMassVeto = cfg_analyze.getParameter<bool>("invert_ZbosonMassVeto");


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
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", isDEBUG);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case Era::k2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case Era::k2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case Era::k2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_0l_2tau", __LINE__) << "Invalid era = " << static_cast<int>(era);
  }

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "2lepton"  ) applyFakeRateWeights = kFR_2lepton;
  else if ( applyFakeRateWeights_string == "4L"       ) applyFakeRateWeights = kFR_4L;
  else if ( applyFakeRateWeights_string == "2tau"     ) applyFakeRateWeights = kFR_2tau;
  else throw cms::Exception("analyze_hh_2l_2tau")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_2lepton || applyFakeRateWeights == kFR_4L ) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    cfg_leptonFakeRateWeight.addParameter<std::string>("era", era_string);
    cfg_leptonFakeRateWeight.addParameter<std::vector<std::string>>("central_or_shifts", central_or_shifts_local);
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight);
  }

  JetToTauFakeRateInterface* jetToTauFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_4L || applyFakeRateWeights == kFR_2tau ) {
    edm::ParameterSet cfg_hadTauFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("hadTauFakeRateWeight");
    cfg_hadTauFakeRateWeight.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
    jetToTauFakeRateInterface = new JetToTauFakeRateInterface(cfg_hadTauFakeRateWeight);
  }

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");

  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

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

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)." << std::endl;

//--- declare event-level variables
  EventInfo eventInfo(isMC, isSignal, isHH_rwgt_allowed, apply_topPtReweighting);
  const std::string default_cat_str = "default";
  std::vector<std::string> evt_cat_strs = { default_cat_str };
  std::vector<std::string> HHWeightNames;

//--- HH scan
  const edm::ParameterSet hhWeight_cfg = cfg_analyze.getParameterSet("hhWeight_cfg");
  //std::cout << " eventInfo.is_hh_nonresonant() " << eventInfo.is_hh_nonresonant() << std::endl;
  //std::cout << " hhWeight_cfg.getParameter<bool>(apply_rwgt) " << hhWeight_cfg.getParameter<bool>("apply_rwgt") << std::endl;
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
    std::cout << Nscan << " points being scanned: " << boost::join(evt_cat_strs, ", ") << '\n';
    std::cout << "\n Weights booked = " << apply_HH_rwgt << '\n';
    for (const std::string catcat : evt_cat_strs) {
      std::cout << catcat << '\n';
    }
  }
  else
  {
    std::cout << "No HH reweighting applied: " << boost::join(evt_cat_strs, ", ") << '\n';
  }


  std::cout<< "evt_cat_strs.size() " << evt_cat_strs.size() << std::endl;

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
  inputTree->registerReader(&eventInfoReader);

  ObjectMultiplicity objectMultiplicity;
  ObjectMultiplicityReader objectMultiplicityReader(&objectMultiplicity);
  if(useObjectMultiplicity)
  {
    inputTree -> registerReader(&objectMultiplicityReader);
  }
  const int minLeptonSelection = std::min(electronSelection, muonSelection);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
  inputTree -> registerReader(&hltPathReader_instance);

  if(eventWeightManager)
  {
    inputTree->registerReader(eventWeightManager);
    eventWeightManager->set_central_or_shift(central_or_shift_main);
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

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era, -1, isDEBUG);
  electronReader->set_mvaTTH_wp(lep_mva_cut_e);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, isMC, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree->registerReader(hadTauReader);
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
  RecoHadTauSelectorTight tightHadTauFilter(era, -1, isDEBUG);
  tightHadTauFilter.set(hadTauSelection_part2);
  tightHadTauFilter.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauFilter.set_min_antiMuon(hadTauSelection_antiMuon);
  switch(hadTauSelection)
  {
    case kFakeable: tauLevel = std::min(tauLevel, get_tau_id_wp_int(fakeableHadTauSelector.getSelector().get())); break;
    case kTight:    tauLevel = std::min(tauLevel, get_tau_id_wp_int(tightHadTauSelector.getSelector().get()));    break;
    default: assert(0);
  }

  RecoJetReader* jetReader = new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  jetReader->setPtMass_central_or_shift(jetPt_option);
  jetReader->read_btag_systematics((central_or_shifts_local.size() > 1 || central_or_shift_main != "central") && isMC);
  inputTree->registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerByIndex(isDEBUG);
  RecoJetCollectionSelector jetSelector(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era, -1, isDEBUG);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree->registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree -> registerReader(metFilterReader);

//--- declare generator level information
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
      inputTree->registerReader(genLeptonReader);
      genHadTauReader = new GenHadTauReader(branchName_genHadTaus);
      inputTree->registerReader(genHadTauReader);
      genJetReader = new GenJetReader(branchName_genJets);
      inputTree->registerReader(genJetReader);

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
    inputTree->registerReader(lheInfoReader);
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
    ElectronHistManager* leadElectron_;
    ElectronHistManager* subleadElectron_;
    MuonHistManager* muons_;
    MuonHistManager* leadMuon_;
    MuonHistManager* subleadMuon_;
    HadTauHistManager* hadTaus_;
    HadTauHistManager* leadHadTau_;
    HadTauHistManager* subleadHadTau_;
    JetHistManager* jets_;
    JetHistManager* BJets_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    std::map<std::string, EvtHistManager_hh_2l_2tau*> evt_;
    std::map<std::string, SVfit4tauHistManager_MarkovChain*> svFit4tau_wMassConstraint_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_2l_2tau*>> evt_in_decayModes_;
    std::map<std::string, std::map<std::string, SVfit4tauHistManager_MarkovChain*>> svFit4tau_wMassConstraint_in_decayModes_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_2l_2tau*>> evt_in_categories_;
    std::map<std::string, std::map<std::string, SVfit4tauHistManager_MarkovChain*>> svFit4tau_wMassConstraint_in_categories_;
    GenEvtHistManager* genEvtHistManager_afterCuts_;
    LHEInfoHistManager* lheInfoHistManager_afterCuts_;
    std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_afterCuts_in_categories_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };

  std::map<std::string, GenEvtHistManager*> genEvtHistManager_beforeCuts;
  std::map<std::string, LHEInfoHistManager*> lheInfoHistManager_beforeCuts;
  std::map<std::string, std::map<int, selHistManagerType*>> selHistManagers;
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    const bool skipBooking = central_or_shift != central_or_shift_main;
    std::vector<const GenMatchEntry*> genMatchDefinitions = genMatchInterface.getGenMatchDefinitions();
    for (const GenMatchEntry * genMatchDefinition : genMatchDefinitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += genMatchDefinition->getName();

      int idxLepton_and_HadTau = genMatchDefinition->getIdx();

      selHistManagerType* selHistManager = new selHistManagerType();
      if(! skipBooking)
      {
        selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->electrons_->bookHistograms(fs);
        selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->leadElectron_->bookHistograms(fs);
        selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadElectron", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->subleadElectron_->bookHistograms(fs);
        selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->muons_->bookHistograms(fs);
        selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->leadMuon_->bookHistograms(fs);
        selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadMuon", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->subleadMuon_->bookHistograms(fs);
        selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/hadTaus", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->hadTaus_->bookHistograms(fs);
        selHistManager->leadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadHadTau", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->leadHadTau_->bookHistograms(fs);
        selHistManager->subleadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadHadTau", histogramDir.data()), era_string, central_or_shift, "minimalHistograms"));
        selHistManager->subleadHadTau_->bookHistograms(fs);
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
        selHistManager->evt_[evt_cat_str] = new EvtHistManager_hh_2l_2tau(makeHistManager_cfg(process_and_genMatchName,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, gen_mHH));
        selHistManager->evt_[evt_cat_str]->bookHistograms(fs);
        selHistManager->svFit4tau_wMassConstraint_[evt_cat_str] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_and_genMatchName,
          Form("%s/sel/svFit4tau_wMassConstraint", histogramDir.data()), era_string, central_or_shift));
        selHistManager->svFit4tau_wMassConstraint_[evt_cat_str]->bookHistograms(fs);
      }

      selHistManager->genEvtHistManager_afterCuts_ = nullptr;
      selHistManager->lheInfoHistManager_afterCuts_ = nullptr;
      if(isMC && ! skipBooking)
      {
        selHistManager->genEvtHistManager_afterCuts_ = new GenEvtHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
        selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs);
        selHistManager->lheInfoHistManager_afterCuts_ = new LHEInfoHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/lheInfo", histogramDir.data()), era_string, central_or_shift));
        selHistManager->lheInfoHistManager_afterCuts_->bookHistograms(fs);

        if(eventWeightManager)
        {
          selHistManager->genEvtHistManager_afterCuts_->bookHistograms(fs, eventWeightManager);
        }
      }
      vstring categories_evt = {
        "2lSS_2tau", "2lOS_2tau",
        "2e_2tau", "1e1mu_2tau", "2mu_2tau",
        "2eSS_2tau", "2eOS_2tau", "1e1muSS_2tau", "1e1muOS_2tau", "2muSS_2tau", "2muOS_2tau",
        "2lOS_2tau_wChargeFlipWeights", "2eOS_2tau_wChargeFlipWeights", "1e1muOS_2tau_wChargeFlipWeights", "2muOS_2tau_wChargeFlipWeights"
      };
      for(const std::string & category: categories_evt)
      {
        TString histogramDir_category = histogramDir.data();
        histogramDir_category.ReplaceAll("2l_2tau", category.data());

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
          selHistManager->evt_in_categories_[evt_cat_str][category] = new EvtHistManager_hh_2l_2tau(makeHistManager_cfg(process_and_genMatchName,
            Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift, gen_mHH)); // Added the signal mass vector
          selHistManager->evt_in_categories_[evt_cat_str][category]->bookHistograms(fs);
          selHistManager->svFit4tau_wMassConstraint_in_categories_[evt_cat_str][category] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_and_genMatchName,
            Form("%s/sel/svFit4tau_wMassConstraint", histogramDir_category.Data()), era_string, central_or_shift));
          selHistManager->svFit4tau_wMassConstraint_in_categories_[evt_cat_str][category]->bookHistograms(fs);
        }
        if(isMC && ! skipBooking)
        {
          selHistManager->lheInfoHistManager_afterCuts_in_categories_[category] = new LHEInfoHistManager(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/lheInfo", histogramDir_category.Data()), era_string, central_or_shift));
          selHistManager->lheInfoHistManager_afterCuts_in_categories_[category]->bookHistograms(fs);
        }
      }
      edm::ParameterSet cfg_EvtYieldHistManager_sel = makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/evtYield", histogramDir.data()), era_string, central_or_shift);
      cfg_EvtYieldHistManager_sel.addParameter<edm::ParameterSet>("runPeriods", cfg_EvtYieldHistManager);
      cfg_EvtYieldHistManager_sel.addParameter<bool>("isMC", isMC);
      selHistManager->evtYield_ = new EvtYieldHistManager(cfg_EvtYieldHistManager_sel);
      selHistManager->evtYield_->bookHistograms(fs);
      selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/weights", histogramDir.data()), era_string, central_or_shift));
      selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
      selHistManagers[central_or_shift][idxLepton_and_HadTau] = selHistManager;
    }
    if(isMC && ! skipBooking)
    {
      genEvtHistManager_beforeCuts[central_or_shift] = new GenEvtHistManager(makeHistManager_cfg(process_string,
        Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
      genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs);
      lheInfoHistManager_beforeCuts[central_or_shift] = new LHEInfoHistManager(makeHistManager_cfg(process_string,
        Form("%s/unbiased/lheInfo", histogramDir.data()), era_string, central_or_shift));
      lheInfoHistManager_beforeCuts[central_or_shift]->bookHistograms(fs);

      if(eventWeightManager)
      {
        genEvtHistManager_beforeCuts[central_or_shift]->bookHistograms(fs, eventWeightManager);
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
      "lep1_pt", "lep1_conePt", "lep1_eta", "lep1_tth_mva", "mT_lep1", "lep1_phi",
      "lep2_pt", "lep2_conePt", "lep2_eta", "lep2_tth_mva", "mT_lep2", "lep2_phi",
      "tau1_pt", "tau1_eta", "tau1_mva", "tau1_phi",
      "tau2_pt", "tau2_eta", "tau2_mva", "tau2_phi",
      "dr_lep1_tau1", "dr_lep1_tau2", "dr_lep2_tau1", "dr_lep2_tau2",
      "dr_leps", "dr_taus", "avg_dr_jet",
      "met", "mht", "met_LD", "HT", "STMET", "met_phi",
      "Smin_llMEt", "m_ll", "pT_ll", "pT_llMEt", "Smin_lltautau", "mTauTau",
      "mTauTauVis", "ptTauTauVis", "diHiggsVisMass", "diHiggsMass",
      "logTopness_publishedChi2", "logTopness_fixedChi2",
      "m_lep1_tau1", "m_lep2_tau1", "m_lep1_tau2", "m_lep2_tau2", "pt_HH_recoil",
      "deltaEta_lep1_lep2", "deltaEta_lep1_tau1", "deltaEta_lep1_tau2", "deltaEta_lep2_tau1", "deltaEta_lep2_tau2", "deltaEta_tau1_tau2",
      "deltaPhi_lep1_lep2", "deltaPhi_lep1_tau1", "deltaPhi_lep1_tau2", "deltaPhi_lep2_tau1", "deltaPhi_lep2_tau2", "deltaPhi_tau1_tau2",
      "dr_lep1_tau1_tau2_min", "dr_lep1_tau1_tau2_max", "dr_lep2_tau1_tau2_min", "dr_lep2_tau1_tau2_max",
      "dr_lep_tau_min_OS", "dr_lep_tau_min_SS","lep1_frWeight", "lep2_frWeight", "hadTau1_frWeight",  "hadTau2_frWeight", "evtWeight",
      "genWeight" , "lheWeight" , "pileupWeight", "triggerWeight", "btagWeight", "leptonEffSF", "hadTauEffSF", "data_to_MC_correction","FR_Weight" 
    );
    bdt_filler->register_variable<int_type>(
      "nJet", "nBJet_loose", "nBJet_medium",
      "lep1_isElectron", "lep1_charge", "lep2_isElectron", "lep2_charge",
      "nElectron", "nMuon"
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

  std::vector<std::string> cuts_temp = {};
  if(invert_ZbosonMassVeto){
    cuts_temp = {
      "run:ls:event selection",
      "object multiplicity",
      "trigger",
      ">= 2 presel leptons",
      ">= 2 sel leptons",
      "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
      "<= 2 tight leptons",
      ">= 2 sel taus",
      "tau-pair OS/SS charge",
      "sel lepton+tau charge",
      "fakeable lepton trigger match",
      "HLT filter matching",
      "b-jet veto",
      "m(ll) > 12 GeV",
      "Z-boson mass veto inverted",
      "MEt filters",
      "signal region veto",
    };
  }else{
    cuts_temp = {
      "run:ls:event selection",
      "object multiplicity",
      "trigger",
      ">= 2 presel leptons",
      ">= 2 sel leptons",
      "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
      "<= 2 tight leptons",
      ">= 2 sel taus",
      "tau-pair OS/SS charge",
      "sel lepton+tau charge",
      "fakeable lepton trigger match",
      "HLT filter matching",
      "b-jet veto",
      "m(ll) > 12 GeV",
      "Z-boson mass veto",
      "MEt filters",
      "signal region veto",
    };
  }

  const std::vector<std::string> cuts = cuts_temp;

  CutFlowTableHistManager * cutFlowHistManager = new CutFlowTableHistManager(cutFlowTableCfg, cuts);
  cutFlowHistManager->bookHistograms(fs);
  while ( inputTree->hasNextEvent() && (! run_lumi_eventSelector || (run_lumi_eventSelector && ! run_lumi_eventSelector -> areWeDone())) ) {
    if(inputTree -> canReport(reportEvery))
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx()
                << " or " << inputTree -> getCurrentEventIdx() << " entry in #"
                << (inputTree -> getProcessedFileCount() - 1)
                << " (" << eventInfo
                << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    //if (analyzedEntries > 1) break;
    histogram_analyzedEntries->Fill(0.);

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) continue;
    EvtWeightRecorderHH evtWeightRecorder(central_or_shifts_local, central_or_shift_main, isMC);
    cutFlowTable.update("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("run:ls:event selection", evtWeightRecorder.get(central_or_shift_main));

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry #" << inputTree->getCumulativeMaxEventCount() << ": " << eventInfo << std::endl;
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << std::endl;
      }
    }

    if(useObjectMultiplicity)
    {
      if(objectMultiplicity.getNRecoLepton(minLeptonSelection) < 2 ||
         objectMultiplicity.getNRecoLepton(kTight)             > 2 ||
         objectMultiplicity.getNRecoHadTau(tauId, tauLevel)    < 2  )
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
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenPhoton> genPhotons;
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

      if(isDEBUG)
      {
        printCollection("genLeptons", genLeptons);
        printCollection("genHadTaus", genHadTaus);
        printCollection("genPhotons", genPhotons);
        printCollection("genJets", genJets);
      }
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

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_2e = hltPaths_isTriggered(triggers_2e, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_2mu = hltPaths_isTriggered(triggers_2mu, triggerWhiteList, eventInfo, isMC);
    bool isTriggered_1e1mu = hltPaths_isTriggered(triggers_1e1mu, triggerWhiteList, eventInfo, isMC);

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_2e = use_triggers_2e && isTriggered_2e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_2mu = use_triggers_2mu && isTriggered_2mu;
    bool selTrigger_1e1mu = use_triggers_1e1mu && isTriggered_1e1mu;
    if ( !(selTrigger_1e || selTrigger_2e || selTrigger_1mu || selTrigger_2mu || selTrigger_1e1mu) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
        std::cout << " (selTrigger_1e = " << selTrigger_1e
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu << ")" << std::endl;
      }
      continue;
    }

//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the ranking of the triggers is as follows: 2mu, 1e1mu, 2e, 1mu, 1e
// CV: this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {
      if ( selTrigger_1e && (isTriggered_1mu || isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e = " << selTrigger_1e
                    << ", isTriggered_1mu = " << isTriggered_1mu
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1e && isTriggered_2e && era != Era::k2018 ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e = " << selTrigger_1e
                    << ", isTriggered_2e = " << isTriggered_2e << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_2e && (isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_2e = " << selTrigger_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1mu && (isTriggered_2e || isTriggered_2mu || isTriggered_1e1mu) ) {
        if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1mu = " << selTrigger_1mu
                    << ", isTriggered_2e = " << isTriggered_2e
                    << ", isTriggered_2mu = " << isTriggered_2mu
                    << ", isTriggered_1e1mu = " << isTriggered_1e1mu << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_1e1mu && isTriggered_2mu ) {
        if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_1e1mu = " << selTrigger_1e1mu
                    << ", isTriggered_2mu = " << isTriggered_2mu << ")" << std::endl;
        }
        continue;
      }
    }
    cutFlowTable.update("trigger", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger", evtWeightRecorder.get(central_or_shift_main));

    if ( (selTrigger_2e    && !apply_offline_e_trigger_cuts_2e)    ||
         (selTrigger_1e1mu && !apply_offline_e_trigger_cuts_1e1mu) ||
         (selTrigger_1e    && !apply_offline_e_trigger_cuts_1e)    ||
         (selTrigger_1mu   && !apply_offline_e_trigger_cuts_1mu)   ||
         (selTrigger_2mu   && !apply_offline_e_trigger_cuts_2mu)  ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      tightElectronSelector.enable_offline_e_trigger_cuts();
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
    }

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

    const std::vector<const RecoLepton*> preselLeptonsFull = mergeLeptonCollections(preselElectrons, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> preselLeptonsFullUncleaned = mergeLeptonCollections(preselElectronsUncleaned, preselMuons, isHigherConePt);
    const std::vector<const RecoLepton*> fakeableLeptonsFull = mergeLeptonCollections(fakeableElectrons, fakeableMuons, isHigherConePt);
    const std::vector<const RecoLepton*> tightLeptonsFull = mergeLeptonCollections(tightElectrons, tightMuons, isHigherConePt);

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 2);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 2);
    const std::vector<const RecoLepton*> tightLeptons = getIntersection(fakeableLeptons, tightLeptonsFull, isHigherConePt);

    std::vector<const RecoLepton*> selLeptons;
    std::vector<const RecoMuon*> selMuons;
    std::vector<const RecoElectron*> selElectrons;
    if(electronSelection == muonSelection)
    {
      // for SR, flip region and fake CR
      // doesn't matter if we supply electronSelection or muonSelection here
      selLeptons = selectObjects(muonSelection, preselLeptons, fakeableLeptons, tightLeptons);
      selMuons = getIntersection(preselMuons, selLeptons, isHigherConePt);
      selElectrons = getIntersection(preselElectrons, selLeptons, isHigherConePt);
    }
    else
    {
      // for MC closure
      // make sure that neither electron nor muon selections are loose
      assert(electronSelection != kLoose && muonSelection != kLoose);
      selMuons = selectObjects(muonSelection, preselMuons, fakeableMuons, tightMuons);
      selElectrons = selectObjects(electronSelection, preselElectrons, fakeableElectrons, tightElectrons);
    }
    const std::vector<const RecoLepton*> selLeptons_full = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);
    if(!(electronSelection == muonSelection)) selLeptons = getIntersection(fakeableLeptons, selLeptons_full, isHigherConePt);

    const std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    const std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    const std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    const std::vector<const RecoHadTau*> fakeableHadTausFull = fakeableHadTauSelector(cleanedHadTaus, isHigherPt);
    const std::vector<const RecoHadTau*> tightHadTausFull = tightHadTauSelector(fakeableHadTausFull, isHigherPt);

    const std::vector<const RecoHadTau*> fakeableHadTaus = pickFirstNobjects(fakeableHadTausFull, 2);
    const std::vector<const RecoHadTau*> tightHadTaus = getIntersection(fakeableHadTaus, tightHadTausFull, isHigherPt);
    const std::vector<const RecoHadTau*> selHadTaus = selectObjects(hadTauSelection, fakeableHadTaus, tightHadTaus);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("fakeableHadTaus", fakeableHadTaus);
      printCollection("tightHadTaus",    tightHadTaus);
    }

    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("selMuons", selMuons);
      printCollection("selElectrons", selElectrons);
      printCollection("selLeptons", selLeptons);
      printCollection("selHadTaus", selHadTaus);
    }

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets = jetReader->read();
    const std::vector<const RecoJet*> jet_ptrs = convert_to_ptrs(jets);
    const std::vector<const RecoJet*> cleanedJets = jetCleaningByIndex ?
      jetCleanerByIndex(jet_ptrs, selectBDT ? selLeptons_full : fakeableLeptonsFull, selectBDT ? selHadTaus : fakeableHadTausFull) :
      jetCleaner       (jet_ptrs, selectBDT ? selLeptons_full : fakeableLeptonsFull, selectBDT ? selHadTaus : fakeableHadTausFull)
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

//--- build collections of generator level particles (after some cuts are applied, to save computing time)
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
    // require exactly two leptons passing loose preselection criteria
    if ( !(preselLeptonsFull.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 2 presel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 2 presel leptons", evtWeightRecorder.get(central_or_shift_main));

//--- compute MHT and linear MET discriminant (met_LD)
    const RecoMEt met_uncorr = metReader->read();
    const RecoMEt met = recompute_met(met_uncorr, jets, met_option, isDEBUG);
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptonsFull, fakeableHadTausFull, selJets);
    double met_LD = compMEt_LD(met.p4(), mht_p4);
    double HT = compHT(fakeableLeptons, fakeableHadTaus, selJets);
    double STMET = compSTMEt(fakeableLeptons, fakeableHadTaus, selJets, met.p4());

//--- apply final event selection
    // require exactly two leptons passing tight selection criteria of final event selection
    if ( !(selLeptons.size() >= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
        printCollection("selLeptons", selLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 2 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 2 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    const RecoLepton* selLepton_lead = selLeptons[0];
    int selLepton_lead_type = getLeptonType(selLepton_lead->pdgId());
    const RecoLepton* selLepton_sublead = selLeptons[1];
    int selLepton_sublead_type = getLeptonType(selLepton_sublead->pdgId());
    const leptonChargeFlipGenMatchEntry& selLepton_genMatch = getLeptonChargeFlipGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead);

    const double minPt_lead = 25.;
    const double minPt_sublead = 15.;
    if ( !(selLepton_lead->cone_pt() > minPt_lead && selLepton_sublead->cone_pt() > minPt_sublead) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
        std::cout << " (leading selLepton pT = " << selLepton_lead->pt() << ", minPt_lead = " << minPt_lead
                  << ", subleading selLepton pT = " << selLepton_sublead->pt() << ", minPt_sublead = " << minPt_sublead << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV", evtWeightRecorder.get(central_or_shift_main));

    bool isLeptonCharge_SS = selLepton_lead->charge()*selLepton_sublead->charge() > 0;
    bool isLeptonCharge_OS = selLepton_lead->charge()*selLepton_sublead->charge() < 0;
    if ( leptonChargeSelection == kOS && isLeptonCharge_SS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = " << selLepton_sublead->charge() << ", leptonChargeSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( leptonChargeSelection == kSS && isLeptonCharge_OS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = " << selLepton_sublead->charge() << ", leptonChargeSelection = SS)" << std::endl;
      }
      continue;
    }


    // require exactly two leptons passing tight selection criteria, to avoid overlap with other channels
    if ( !(tightLeptonsFull.size() <= 2) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection." << std::endl;
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update("<= 2 tight leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("<= 2 tight leptons", evtWeightRecorder.get(central_or_shift_main));

    if ( !(selHadTaus.size() >= 2) ) continue;
    cutFlowTable.update(">= 2 sel taus", evtWeightRecorder.get(central_or_shift_main));

    const RecoHadTau* selHadTau_lead = selHadTaus[0];
    const RecoHadTau* selHadTau_sublead = selHadTaus[1];
    const hadTauGenMatchEntry& selHadTau_genMatch = getHadTauGenMatch(hadTauGenMatch_definitions, selHadTau_lead, selHadTau_sublead);

    bool isCharge_hadTau_SS = selHadTau_lead->charge()*selHadTau_sublead->charge() > 0;
    bool isCharge_hadTau_OS = selHadTau_lead->charge()*selHadTau_sublead->charge() < 0;
    if ( hadTauChargeSelection == kOS && isCharge_hadTau_SS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS hadTau charge selection." << std::endl;
        std::cout << " (leading selHadTau charge = " << selHadTau_lead->charge()
                  << ", subleading selHadTau charge = " << selHadTau_sublead->charge() << ", hadTauChargeSelection = SS)" << std::endl;
      }
      continue;
    }
    if ( hadTauChargeSelection == kSS && isCharge_hadTau_OS ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS hadTau charge selection." << std::endl;
        std::cout << " (leading selHadTau charge = " << selHadTau_lead->charge()
                  << ", subleading selHadTau charge = " << selHadTau_sublead->charge() << ", hadTauChargeSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( hadTauChargeSelection != kDisabled ) {
      cutFlowTable.update(Form("tau-pair %s charge", hadTauChargeSelection_string.data()), evtWeightRecorder.get(central_or_shift_main));
    }
    cutFlowHistManager->fillHistograms("tau-pair OS/SS charge", evtWeightRecorder.get(central_or_shift_main));

    if ( (chargeSumSelection == kOS && std::abs(selLepton_lead->charge() + selLepton_sublead->charge() + selHadTau_lead->charge() + selHadTau_sublead->charge()) != 0) ||
         (chargeSumSelection == kSS && std::abs(selLepton_lead->charge() + selLepton_sublead->charge() + selHadTau_lead->charge() + selHadTau_sublead->charge()) == 0) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS lepton+tau charge selection." << std::endl;
        std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
                  << ", subleading selLepton charge = " << selLepton_sublead->charge()
                  << ", leading selHadTau charge = " << selHadTau_lead->charge()
                  << ", subleading selHadTau charge = " << selHadTau_sublead->charge() << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update(Form("sel lepton+tau %s charge", chargeSumSelection_string.data()), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel lepton+tau charge", evtWeightRecorder.get(central_or_shift_main));


    // require that trigger paths match event category (with event category based on fakeableLeptons)
    if ( !((fakeableElectrons.size() >= 2 &&                              (selTrigger_2e    || selTrigger_1e                  )) ||
           (fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 1 && (selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
           (                                 fakeableMuons.size() >= 2 && (selTrigger_2mu   || selTrigger_1mu                 ))) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
        std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
                  << ", #fakeableMuons = " << fakeableMuons.size()
                  << ", selTrigger_2mu = " << selTrigger_2mu
                  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
                  << ", selTrigger_2e = " << selTrigger_2e
                  << ", selTrigger_1mu = " << selTrigger_1mu
                  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("fakeable lepton trigger match", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("fakeable lepton trigger match", evtWeightRecorder.get(central_or_shift_main));


//--- apply HLT filter
    if(apply_hlt_filter)
    {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,    selTrigger_1e    },
        { hltPathsE::trigger_1mu,   selTrigger_1mu   },
        { hltPathsE::trigger_2e,    selTrigger_2e    },
        { hltPathsE::trigger_2mu,   selTrigger_2mu   },
        { hltPathsE::trigger_1e1mu, selTrigger_1e1mu },
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

      dataToMCcorrectionInterface->setLeptons(
        selLepton_lead_type, selLepton_lead->pt(), selLepton_lead->cone_pt(), selLepton_lead->eta(),
        selLepton_sublead_type, selLepton_sublead->pt(), selLepton_sublead->cone_pt(), selLepton_sublead->eta()
      );

//--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_leptonTriggerEff(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      evtWeightRecorder.record_leptonIDSF_recoToLoose(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if(electronSelection == kFakeable && muonSelection == kFakeable)
      {
        evtWeightRecorder.record_leptonSF(dataToMCcorrectionInterface->getSF_leptonID_and_Iso_fakeable_to_loose());
      }
      else if(electronSelection >= kFakeable && muonSelection >= kFakeable)
      {
        // apply loose-to-tight lepton ID SFs if either of the following is true:
        // 1) both electron and muon selections are tight -> corresponds to SR
        // 2) electron selection is relaxed to fakeable and muon selection is kept as tight -> corresponds to MC closure w/ relaxed e selection
        // 3) muon selection is relaxed to fakeable and electron selection is kept as tight -> corresponds to MC closure w/ relaxed mu selection
        // we allow (2) and (3) so that the MC closure regions would more compatible w/ the SR (1) in comparison
        evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface);
      }

//--- apply data/MC corrections for hadronic tau identification efficiency
//    and for e->tau and mu->tau misidentification rates
      int selHadTau_lead_genPdgId = getHadTau_genPdgId(selHadTau_lead);
      int selHadTau_sublead_genPdgId = getHadTau_genPdgId(selHadTau_sublead);
      dataToMCcorrectionInterface->setHadTaus(
        selHadTau_lead_genPdgId, selHadTau_lead->pt(), selHadTau_lead->eta(),
        selHadTau_sublead_genPdgId, selHadTau_sublead->pt(), selHadTau_sublead->eta()
      );
      evtWeightRecorder.record_hadTauID_and_Iso(dataToMCcorrectionInterface);
      evtWeightRecorder.record_eToTauFakeRate(dataToMCcorrectionInterface);
      evtWeightRecorder.record_muToTauFakeRate(dataToMCcorrectionInterface);
    }

    bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
    bool passesTight_hadTau_lead = isMatched(*selHadTau_lead, tightHadTausFull);
    bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);
    bool passesTight_hadTau_sublead = isMatched(*selHadTau_sublead, tightHadTausFull);

    if(leptonFakeRateInterface)
    {
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton_lead);
      evtWeightRecorder.record_jetToLepton_FR_sublead(leptonFakeRateInterface, selLepton_sublead);
    }

    if(jetToTauFakeRateInterface)
    {
      evtWeightRecorder.record_jetToTau_FR_lead(jetToTauFakeRateInterface, selHadTau_lead);
      evtWeightRecorder.record_jetToTau_FR_sublead(jetToTauFakeRateInterface, selHadTau_sublead);
    }
    if(!selectBDT){
      if(applyFakeRateWeights == kFR_4L)
	{
	  evtWeightRecorder.compute_FR_2l2tau(
					      passesTight_lepton_lead, passesTight_lepton_sublead, passesTight_hadTau_lead, passesTight_hadTau_sublead
					      );
	}
      else if(applyFakeRateWeights == kFR_2lepton)
	{
	  evtWeightRecorder.compute_FR_2l(passesTight_lepton_lead, passesTight_lepton_sublead);
	}
      else if(applyFakeRateWeights == kFR_2tau)
	{
	  evtWeightRecorder.compute_FR_2tau(passesTight_hadTau_lead, passesTight_hadTau_sublead);
	}
    }
    // CV: apply data/MC ratio for jet->tau fake-rates in case data-driven "fake" background estimation is applied to leptons only
    if(isMC && apply_hadTauFakeRateSF && hadTauSelection == kTight)
    {
      if(! (selHadTau_lead->genHadTau() || selHadTau_lead->genLepton()) && jetToTauFakeRateInterface)
      {
        evtWeightRecorder.record_jetToTau_SF_lead(jetToTauFakeRateInterface, selHadTau_lead);
      }
      if(! (selHadTau_sublead->genHadTau() || selHadTau_sublead->genLepton()) && jetToTauFakeRateInterface)
      {
        evtWeightRecorder.record_jetToTau_SF_sublead(jetToTauFakeRateInterface, selHadTau_sublead);
      }
    }


    if ( selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1 )
    {
      if(run_lumi_eventSelector)
      {
        std::cout << "event " << eventInfo.str() << " FAILS b-jet veto\n";
      }
      continue;
    }
    cutFlowTable.update("b-jet veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("b-jet veto", evtWeightRecorder.get(central_or_shift_main));

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsFullUncleaned);
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));

    const bool failsZbosonMassVeto = isfailsZbosonMassVeto(preselLeptonsFull);
    if(invert_ZbosonMassVeto){
      if ( !failsZbosonMassVeto ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS inverted Z-boson veto." << std::endl;
	}
	continue;
      }
      cutFlowTable.update("Z-boson mass veto inverted", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("Z-boson mass veto inverted", evtWeightRecorder.get(central_or_shift_main));
    }else{
      if ( failsZbosonMassVeto ) {
	if ( run_lumi_eventSelector ) {
	  std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
	}
	continue;
      }
      cutFlowTable.update("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));
    }


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
    if ( isMCClosure_e || isMCClosure_m || isMCClosure_t ) {
      bool applySignalRegionVeto_lepton = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      bool applySignalRegionVeto_hadTau = isMCClosure_t && countFakeHadTaus(selHadTaus) >= 1;
      if ( applySignalRegionVeto_lepton && tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
      if ( applySignalRegionVeto_hadTau && tightHadTaus.size() >= 2 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable || hadTauSelection == kFakeable ) {
      if ( tightLeptons.size() >= 2 && tightHadTaus.size() >= 2 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
                     "# tight leptons = " << tightLeptons.size() << " >= 2 and "
                     "# tight taus = " << tightHadTaus.size() << " >= 2\n"
        ;
        printCollection("tightLeptons", tightLeptons);
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
    } else { // Siddesh lines
      for(const std::string & evt_cat_str: evt_cat_strs) {
	if(evt_cat_str != default_cat_str)
	  {
	    continue;
	  }
	
	reWeightMapHH[evt_cat_str] = evtWeightRecorder.get(central_or_shift_main);
	std::cout << "\t evt_cat_str: " << evt_cat_str << ", reWeightMapHH: " << reWeightMapHH[evt_cat_str] << std::endl;
      }
    }

    std::cout<<"reWeightMapHH.size() " << reWeightMapHH.size() << std::endl;

    const Particle::LorentzVector tautau_p4 = selHadTau_lead->p4() + selHadTau_sublead->p4();
    const double mTauTauVis_sel = tautau_p4.mass();

    double leptonPairCharge_sel = selLepton_lead->charge() + selLepton_sublead->charge();
    double hadTauPairCharge_sel = selHadTau_lead->charge() + selHadTau_sublead->charge();

    bool isCharge_lepton_SS = selLepton_lead->charge()*selLepton_sublead->charge() > 0;
    bool isCharge_lepton_OS = selLepton_lead->charge()*selLepton_sublead->charge() < 0;


    std::vector<SVfit4tauResult> svFit4tauResults_woMassConstraint = compSVfit4tau(
      *selLepton_lead, *selLepton_sublead, *selHadTau_lead, *selHadTau_sublead, met, chargeSumSelection_string, rnd,  -1., 2.);
    std::vector<SVfit4tauResult> svFit4tauResults_wMassConstraint = compSVfit4tau(
      *selLepton_lead, *selLepton_sublead, *selHadTau_lead, *selHadTau_sublead, met, chargeSumSelection_string, rnd, 125., 2.);

    double dihiggsVisMass_sel = (selLepton_lead->p4() + selLepton_sublead->p4() + selHadTau_lead->p4() + selHadTau_sublead->p4()).mass();
    
    double dihiggsMass = ( svFit4tauResults_wMassConstraint.size() >= 1 && svFit4tauResults_wMassConstraint[0].isValidSolution_ ) ?
      svFit4tauResults_wMassConstraint[0].dihiggs_mass_ : -1.;

    // pre-compute BDT variables-1
    const double deltaEta_lep1_lep2 = (selLepton_lead->p4() - selLepton_sublead->p4()).eta();
    const double deltaEta_lep1_tau1 = (selLepton_lead->p4() - selHadTau_lead->p4()).eta();
    const double deltaEta_lep1_tau2 = (selLepton_lead->p4() - selHadTau_sublead->p4()).eta();
    const double deltaEta_lep2_tau1 = (selLepton_sublead->p4() - selHadTau_lead->p4()).eta();
    const double deltaEta_lep2_tau2 = (selLepton_sublead->p4() - selHadTau_sublead->p4()).eta();
    const double deltaEta_tau1_tau2 = (selHadTau_lead->p4() - selHadTau_sublead->p4()).eta();
    const double deltaPhi_lep1_lep2 = (selLepton_lead->p4() - selLepton_sublead->p4()).phi();
    const double deltaPhi_lep1_tau1 = (selLepton_lead->p4() - selHadTau_lead->p4()).phi();
    const double deltaPhi_lep1_tau2 = (selLepton_lead->p4() - selHadTau_sublead->p4()).phi();
    const double deltaPhi_lep2_tau1 = (selLepton_sublead->p4() - selHadTau_lead->p4()).phi();
    const double deltaPhi_lep2_tau2 = (selLepton_sublead->p4() - selHadTau_sublead->p4()).phi();
    const double deltaPhi_tau1_tau2 = (selHadTau_lead->p4() - selHadTau_sublead->p4()).phi();
    const double m_lep1_tau1 = (selLepton_lead->p4() + selHadTau_lead->p4()).mass();
    const double m_lep2_tau1 = (selLepton_sublead->p4() + selHadTau_lead->p4()).mass();
    const double m_lep1_tau2 = (selLepton_lead->p4() + selHadTau_sublead->p4()).mass();
    const double m_lep2_tau2 = (selLepton_sublead->p4() + selHadTau_sublead->p4()).mass();
    const double pt_HH_recoil = (selLepton_lead->p4() + selLepton_sublead->p4() + selHadTau_lead->p4() + selHadTau_sublead->p4() - met.p4()).pt();
    const double mT_lep1 = comp_MT_met(selLepton_lead, met.pt(), met.phi());
    const double mT_lep2 = comp_MT_met(selLepton_sublead, met.pt(), met.phi());
    const double dr_lep1_tau1 = deltaR(selLepton_lead->p4(),    selHadTau_lead->p4());
    const double dr_lep2_tau1 = deltaR(selLepton_sublead->p4(), selHadTau_lead->p4());
    const double dr_lep1_tau2 = deltaR(selLepton_lead->p4(),    selHadTau_sublead->p4());
    const double dr_lep2_tau2 = deltaR(selLepton_sublead->p4(), selHadTau_sublead->p4());
    const double dr_lep1_tau1_tau2_min = std::min(dr_lep1_tau1, dr_lep1_tau2);
    const double dr_lep1_tau1_tau2_max = std::max(dr_lep1_tau1, dr_lep1_tau2);
    const double dr_lep2_tau1_tau2_min = std::min(dr_lep2_tau1, dr_lep2_tau2);
    const double dr_lep2_tau1_tau2_max = std::max(dr_lep2_tau1, dr_lep2_tau2);
    double dr_lep_tau_min_OS = 0.;
    if(isCharge_lepton_OS){
      dr_lep_tau_min_OS = std::min(std::min(dr_lep1_tau1, dr_lep1_tau2), std::min(dr_lep2_tau1, dr_lep2_tau2));
    }else{
      dr_lep_tau_min_OS = -1.;
    }
    double dr_lep_tau_min_SS = 0.;
    if(isCharge_lepton_SS){
      dr_lep_tau_min_SS = std::min(std::min(dr_lep1_tau1, dr_lep1_tau2), std::min(dr_lep2_tau1, dr_lep2_tau2));
    }else{
      dr_lep_tau_min_SS = -1.;
    }
    const double dr_leps = deltaR(selLepton_lead->p4(), selLepton_sublead->p4());
    const double dr_taus = deltaR(selHadTau_lead->p4(), selHadTau_sublead->p4());
    const double avg_dr_jet = comp_avg_dr_jet(selJets);
    const Particle::LorentzVector ll_p4 = selLepton_lead->p4() + selLepton_sublead->p4();
    const double Smin_llMEt = comp_Smin(ll_p4, met.p4().px(), met.p4().py());
    const double ptTauTauVis_sel = (selHadTau_lead->p4() + selHadTau_sublead->p4()).pt();
    const Particle::LorentzVector lltautau_p4 = ll_p4 + tautau_p4;
    const double Smin_lltautau = comp_Smin(lltautau_p4, met.p4().px(), met.p4().py());
    const std::vector<const RecoJet*> cleanedJets_wrt_leptons = jetCleaner(jet_ptrs, fakeableLeptons);
    const std::vector<const RecoJet*> selJets_btag = jetSelector(cleanedJets_wrt_leptons, isHigherCSV);
    const std::vector<const RecoJet*> selBJets_btag_loose = jetSelectorBtagLoose(selJets_btag, isHigherPt);
    const std::vector<const RecoJet*> selBJets_btag_medium = jetSelectorBtagMedium(selJets_btag, isHigherPt);
    const RecoJet * selBJet_lead    = selJets_btag.size() > 0 ? selJets_btag.at(0) : nullptr;
    const RecoJet * selBJet_sublead = selJets_btag.size() > 1 ? selJets_btag.at(1) : nullptr;

    //--- reconstruct mass of tau-pair using SVfit algorithm
    //
    //    NOTE: SVfit needs to be run after all event selection cuts are applied,
    //          because the algorithm takes O(1 second per event) to run
    //
    std::vector<classic_svFit::MeasuredTauLepton> measuredTauLeptons;
    classic_svFit::MeasuredTauLepton::kDecayType leg1Type = classic_svFit::MeasuredTauLepton::kTauToHadDecay;
    double leg1Mass = selHadTau_lead->mass();
    if ( leg1Mass < classic_svFit::chargedPionMass ) leg1Mass = classic_svFit::chargedPionMass;
    if ( leg1Mass > 1.5                            ) leg1Mass = 1.5;
    classic_svFit::MeasuredTauLepton::kDecayType leg2Type = classic_svFit::MeasuredTauLepton::kTauToHadDecay;
    double leg2Mass = selHadTau_sublead->mass();
    if ( leg2Mass < classic_svFit::chargedPionMass ) leg2Mass = classic_svFit::chargedPionMass;
    if ( leg2Mass > 1.5                            ) leg2Mass = 1.5;
    measuredTauLeptons.push_back(classic_svFit::MeasuredTauLepton(leg1Type, selHadTau_lead->pt(), selHadTau_lead->eta(), selHadTau_lead->phi(), leg1Mass));
    measuredTauLeptons.push_back(classic_svFit::MeasuredTauLepton(leg2Type, selHadTau_sublead->pt(), selHadTau_sublead->eta(), selHadTau_sublead->phi(), leg2Mass));
    ClassicSVfit svFitAlgo;
    svFitAlgo.addLogM_dynamic(false);
    svFitAlgo.addLogM_fixed(true, 5.);
    svFitAlgo.integrate(measuredTauLeptons, met.p4().px(), met.p4().py(), met.cov());


    // pre-compute BDT variables-2
    //double mTauTau = -1.; // CV: temporarily comment-out the following line, to make code compile with "old" and "new" version of ClassicSVfit
    const double mTauTau   = ( svFitAlgo.isValidSolution() ) ? static_cast<classic_svFit::HistogramAdapterDiTau*>(svFitAlgo.getHistogramAdapter())->getMass() : -1.;
    Topness topness_publishedChi2(Topness::kPublishedChi2);
    if(selBJet_lead && selBJet_sublead)
    {
      topness_publishedChi2.fit(
        selLepton_lead->p4(), selLepton_sublead->p4(),
        selBJet_lead->p4(),   selBJet_sublead->p4(),
        met.p4().px(),        met.p4().py()
      );
    }
    const double logTopness_publishedChi2 =
      topness_publishedChi2.isValidSolution() ? topness_publishedChi2.logTopness() : -99.;
    
    Topness topness_fixedChi2(Topness::kFixedChi2);
    if(selBJet_lead && selBJet_sublead)
    {
      topness_fixedChi2.fit(
        selLepton_lead->p4(), selLepton_sublead->p4(),
        selBJet_lead->p4(),   selBJet_sublead->p4(),
        met.p4().px(),        met.p4().py()
      );
    }
    const double logTopness_fixedChi2 =
      topness_fixedChi2.isValidSolution() ? topness_fixedChi2.logTopness() : -99.;
    

    //-----------Filling Map with all BDT Training Variables-----------
    AllVars_Map["deltaEta_lep1_lep2"] = deltaEta_lep1_lep2;
    AllVars_Map["deltaEta_lep1_tau1"] = deltaEta_lep1_tau1;
    AllVars_Map["deltaEta_lep1_tau2"] = deltaEta_lep1_tau2;
    AllVars_Map["deltaEta_lep2_tau1"] = deltaEta_lep2_tau1;
    AllVars_Map["deltaEta_lep2_tau2"] = deltaEta_lep2_tau2;
    AllVars_Map["deltaEta_tau1_tau2"] = deltaEta_tau1_tau2;
    AllVars_Map["deltaPhi_lep1_lep2"] = deltaPhi_lep1_lep2;
    AllVars_Map["deltaPhi_lep1_tau1"] = deltaPhi_lep1_tau1;
    AllVars_Map["deltaPhi_lep1_tau2"] = deltaPhi_lep1_tau2;
    AllVars_Map["deltaPhi_lep2_tau1"] = deltaPhi_lep2_tau1;
    AllVars_Map["deltaPhi_lep2_tau2"] = deltaPhi_lep2_tau2;
    AllVars_Map["deltaPhi_tau1_tau2"] = deltaPhi_tau1_tau2;
    AllVars_Map["dr_lep1_tau1_tau2_min"] = dr_lep1_tau1_tau2_min;
    AllVars_Map["dr_lep1_tau1_tau2_max"] = dr_lep1_tau1_tau2_max;
    AllVars_Map["dr_lep2_tau1_tau2_min"] = dr_lep2_tau1_tau2_min;
    AllVars_Map["dr_lep2_tau1_tau2_max"] = dr_lep2_tau1_tau2_max;
    AllVars_Map["dr_lep_tau_min_OS"] = dr_lep_tau_min_OS;
    AllVars_Map["dr_lep_tau_min_SS"] = dr_lep_tau_min_SS;
    AllVars_Map["pt_HH_recoil"] = pt_HH_recoil;
    AllVars_Map["lep1_pt"] = selLepton_lead->pt();
    AllVars_Map["lep1_conePt"] = selLepton_lead->cone_pt();
    AllVars_Map["lep1_eta"] = selLepton_lead->eta();
    AllVars_Map["lep1_phi"] = selLepton_lead->phi();
    AllVars_Map["lep1_tth_mva"] = selLepton_lead->mvaRawTTH();
    AllVars_Map["mT_lep1"] = mT_lep1;
    AllVars_Map["lep2_pt"] = selLepton_sublead->pt();
    AllVars_Map["lep2_conePt"] = selLepton_sublead->cone_pt();
    AllVars_Map["lep2_eta"] = selLepton_sublead->eta();
    AllVars_Map["lep2_phi"] = selLepton_lead->phi();
    AllVars_Map["lep2_tth_mva"] = selLepton_sublead->mvaRawTTH();
    AllVars_Map["mT_lep2"] = mT_lep2;
    AllVars_Map["tau1_pt"] = selHadTau_lead->pt();
    AllVars_Map["tau1_eta"] = selHadTau_lead->eta();
    AllVars_Map["tau1_phi"] = selHadTau_lead->phi();
    AllVars_Map["tau1_mva"] = selHadTau_lead->id_mva(TauID::MVAoldDMdR032017v2);
    AllVars_Map["tau2_pt"] = selHadTau_sublead->pt();
    AllVars_Map["tau2_eta"] = selHadTau_sublead->eta();
    AllVars_Map["tau2_phi"] = selHadTau_lead->phi();
    AllVars_Map["tau2_mva"] = selHadTau_sublead->id_mva(TauID::MVAoldDMdR032017v2);
    AllVars_Map["dr_lep1_tau1"] = dr_lep1_tau1;
    AllVars_Map["dr_lep2_tau1"] = dr_lep2_tau1;
    AllVars_Map["dr_lep1_tau2"] = dr_lep1_tau2;
    AllVars_Map["dr_lep2_tau2"] = dr_lep2_tau2;
    AllVars_Map["m_lep1_tau1"] = m_lep1_tau1;
    AllVars_Map["m_lep2_tau1"] = m_lep2_tau1;
    AllVars_Map["m_lep1_tau2"] = m_lep1_tau2;
    AllVars_Map["m_lep2_tau2"] = m_lep2_tau2;
    AllVars_Map["dr_leps"] = dr_leps;
    AllVars_Map["dr_taus"] = dr_taus;
    AllVars_Map["avg_dr_jet"] = avg_dr_jet;
    AllVars_Map["met"] = met.pt();
    AllVars_Map["met_phi"] = met.phi();
    AllVars_Map["mht"] = mht_p4.pt();
    AllVars_Map["met_LD"] = met_LD;
    AllVars_Map["HT"] = HT;
    AllVars_Map["STMET"] = STMET;
    AllVars_Map["m_ll"] = ll_p4.mass();
    AllVars_Map["pT_ll"] = ll_p4.pt();
    AllVars_Map["pT_llMEt"] = (ll_p4 + met.p4()).pt();
    AllVars_Map["Smin_llMEt"] = Smin_llMEt;
    AllVars_Map["Smin_lltautau"] = Smin_lltautau;
    AllVars_Map["mTauTauVis"] = mTauTauVis_sel;
    AllVars_Map["mTauTau"] = mTauTau;
    AllVars_Map["ptTauTauVis"] = ptTauTauVis_sel;
    AllVars_Map["diHiggsVisMass"] = dihiggsVisMass_sel;
    AllVars_Map["diHiggsMass"] = dihiggsMass;
    AllVars_Map["logTopness_publishedChi2"] = logTopness_publishedChi2;
    AllVars_Map["logTopness_fixedChi2"] = logTopness_fixedChi2;
    AllVars_Map["nJet"] = selJets.size();
    AllVars_Map["nElectron"] = selElectrons.size();
    AllVars_Map["nMuon"] = selMuons.size();
    AllVars_Map["nBJet_loose"] = selBJets_btag_loose.size();
    AllVars_Map["nBJet_medium"] = selBJets_btag_medium.size();
    AllVars_Map["lep1_isElectron"] = selLepton_lead_type == kElectron;
    AllVars_Map["lep1_charge"] = selLepton_lead->charge();
    AllVars_Map["lep2_isElectron"] = selLepton_sublead_type == kElectron;
    AllVars_Map["lep2_charge"] = selLepton_sublead->charge();
    AllVars_Map["gen_mHH"] = 250.; // setting a Dummy value which will be reset depending on mass hypothesis 

    std::map<std::string, double> BDTInputs_SUM_spin2 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_SUM_spin2);
    std::map<std::string, double> BDTInputs_SUM_spin0 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_SUM_spin0);

    BDTOutput_SUM_Map_spin2 = CreateBDTOutputMap(gen_mHH, BDT_SUM_spin2, BDTInputs_SUM_spin2, "hypo_spin2", eventInfo.event);
    BDTOutput_SUM_Map_spin0 = CreateBDTOutputMap(gen_mHH, BDT_SUM_spin0, BDTInputs_SUM_spin0, "hypo_spin0", eventInfo.event);
    // -------------------------------

//--- retrieve gen-matching flags
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons, selHadTaus);

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
          selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
          if ( selElectrons.size() >= 1 ) {
            selHistManager->leadElectron_->fillHistograms({ selElectrons[0] }, evtWeight);
          }
          if ( selElectrons.size() >= 2 ) {
            selHistManager->subleadElectron_->fillHistograms({ selElectrons[1] }, evtWeight);
          }
          selHistManager->muons_->fillHistograms(selMuons, evtWeight);
          if ( selMuons.size() >= 1 ) {
            selHistManager->leadMuon_->fillHistograms({ selMuons[0] }, evtWeight);
          }
          if ( selMuons.size() >= 2 ) {
            selHistManager->subleadMuon_->fillHistograms({ selMuons[1] }, evtWeight);
          }
          selHistManager->hadTaus_->fillHistograms(selHadTaus, evtWeight);
          selHistManager->leadHadTau_->fillHistograms({ selHadTau_lead }, evtWeight);
          selHistManager->subleadHadTau_->fillHistograms({ selHadTau_sublead }, evtWeight);
          selHistManager->jets_->fillHistograms(selJets, evtWeight);
          selHistManager->BJets_loose_->fillHistograms(selBJets_loose, evtWeight);
          selHistManager->BJets_medium_->fillHistograms(selBJets_medium, evtWeight);
          selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
        }

        std::vector<std::string> categories;
        if      ( isCharge_lepton_SS ) categories.push_back("2lSS_2tau");
        else if ( isCharge_lepton_OS ){
          categories.push_back("2lOS_2tau");
          categories.push_back("2lOS_2tau_wChargeFlipWeights");
        } else assert(0);
        if ( selMuons.size() >= 2 ) {
          categories.push_back("2mu_2tau");
          if      ( isCharge_lepton_SS ) categories.push_back("2muSS_2tau");
          else if ( isCharge_lepton_OS ){
            categories.push_back("2muOS_2tau");
            categories.push_back("2muOS_2tau_wChargeFlipWeights");
          } else assert(0);
        } else if ( selMuons.size() >= 1 && selElectrons.size() >= 1 ) {
          categories.push_back("1e1mu_2tau");
          if      ( isCharge_lepton_SS ) categories.push_back("1e1muSS_2tau");
          else if ( isCharge_lepton_OS ){
            categories.push_back("1e1muOS_2tau");
            categories.push_back("1e1muOS_2tau_wChargeFlipWeights");
          } else assert(0);
        } else if ( selElectrons.size() >= 2 ) {
          categories.push_back("2e_2tau");
          if      ( isCharge_lepton_SS ) categories.push_back("2eSS_2tau");
          else if ( isCharge_lepton_OS ){
            categories.push_back("2eOS_2tau");
            categories.push_back("2eOS_2tau_wChargeFlipWeights");
          } else assert(0);
        } else assert(0);

	for(const auto & kv: reWeightMapHH)
	  { 
	    selHistManager->evt_[kv.first]->fillHistograms(
							   selElectrons.size(),
							   selMuons.size(),
							   selHadTaus.size(),
							   selJets.size(),
							   numSelJetsPtGt40,
							   selBJets_loose.size(),
							   selBJets_medium.size(),
							   mTauTauVis_sel,
							   leptonPairCharge_sel,
							   hadTauPairCharge_sel,
							   dihiggsVisMass_sel,
							   dihiggsMass,
							   HT,
							   STMET,
							   BDTOutput_SUM_Map_spin2,
							   BDTOutput_SUM_Map_spin0,
							   eventInfo.event,
							   kv.second
							   );
	    selHistManager->svFit4tau_wMassConstraint_[kv.first]->fillHistograms(svFit4tauResults_wMassConstraint, kv.second);
	  } 
        if(isMC && ! skipFilling)
        {
          selHistManager->genEvtHistManager_afterCuts_->fillHistograms(
            genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
          );
          selHistManager->lheInfoHistManager_afterCuts_->fillHistograms(*lheInfoReader, evtWeight);

          if(eventWeightManager)
          {
            selHistManager->genEvtHistManager_afterCuts_->fillHistograms(eventWeightManager, evtWeightRecorder.get_inclusive(central_or_shift));
          }
        }
        if(! skipFilling)
        {
          selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
          selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
          selHistManager->weights_->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
          selHistManager->weights_->fillHistograms("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift));
          selHistManager->weights_->fillHistograms("data_to_MC_correction", evtWeightRecorder.get_tauSF(central_or_shift));
          selHistManager->weights_->fillHistograms("fakeRate", evtWeightRecorder.get_FR(central_or_shift));
        }

        for(const std::string & category: categories)
        {
          double evtWeight_chargeFlip = 1.;
          if ( category.find("_wChargeFlipWeights") != std::string::npos )
	    {
	      double prob_chargeMisId_lead = prob_chargeMisId(era, getLeptonType(selLepton_lead->pdgId()), selLepton_lead->pt(), selLepton_lead->eta());
	      double prob_chargeMisId_sublead = prob_chargeMisId(era, getLeptonType(selLepton_sublead->pdgId()), selLepton_sublead->pt(), selLepton_sublead->eta());
	      evtWeight_chargeFlip *= ( prob_chargeMisId_lead + prob_chargeMisId_sublead);
	    }
	  for(const auto & kv: reWeightMapHH)
	    {
	      double evtWeight_category = kv.second * evtWeight_chargeFlip;
	      if ( category.find("_wChargeFlipWeights") != std::string::npos )
		{
		  double prob_chargeMisId_lead = prob_chargeMisId(era, getLeptonType(selLepton_lead->pdgId()), selLepton_lead->pt(), selLepton_lead->eta());
		  double prob_chargeMisId_sublead = prob_chargeMisId(era, getLeptonType(selLepton_sublead->pdgId()), selLepton_sublead->pt(), selLepton_sublead->eta());
		  evtWeight_category *= ( prob_chargeMisId_lead + prob_chargeMisId_sublead);
		}
	      if(selHistManager->evt_in_categories_.find(category) != selHistManager->evt_in_categories_.end())
		{
		  selHistManager->evt_in_categories_[kv.first][category]->fillHistograms(
											 selElectrons.size(),
											 selMuons.size(),
											 selHadTaus.size(),
											 selJets.size(),
											 numSelJetsPtGt40,
											 selBJets_loose.size(),
											 selBJets_medium.size(),
											 mTauTauVis_sel,
											 leptonPairCharge_sel,
											 hadTauPairCharge_sel,
											 dihiggsVisMass_sel,
											 dihiggsMass,
											 HT,
											 STMET,
											 BDTOutput_SUM_Map_spin2,
											 BDTOutput_SUM_Map_spin0,
											 eventInfo.event,
											 evtWeight_category
											 );
		  selHistManager->svFit4tau_wMassConstraint_in_categories_[kv.first][category]->fillHistograms(svFit4tauResults_wMassConstraint, evtWeight_category);
		}
	    }
          if(isMC && ! skipFilling)
	    {
	      selHistManager->lheInfoHistManager_afterCuts_in_categories_[category]->fillHistograms(*lheInfoReader, evtWeight * evtWeight_chargeFlip);
	    }
        }
      }
    }

    if ( selEventsFile ) {
      (*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':' << eventInfo.event << '\n';
    }
//--------------Histogram filling section ends ------


// --------- bdt filler section begins    
    if(bdt_filler)
    {
      double lep1_genLepPt = ( selLepton_lead->genLepton()    ) ? selLepton_lead->genLepton()->pt()    : 0.;
      double lep2_genLepPt = ( selLepton_sublead->genLepton() ) ? selLepton_sublead->genLepton()->pt() : 0.;
      double hadTau1_genPt = 0.;
      if(selHadTau_sublead->genHadTau()) hadTau1_genPt =  selHadTau_sublead->genHadTau()->pt();
      else if ( selHadTau_sublead->genLepton()) hadTau1_genPt =  selHadTau_sublead->genLepton()->pt();
      double hadTau2_genPt = 0.;
      if(selHadTau_sublead->genHadTau()) hadTau2_genPt =  selHadTau_sublead->genHadTau()->pt();
      else if ( selHadTau_sublead->genLepton()) hadTau2_genPt =  selHadTau_sublead->genLepton()->pt();
      
      //FR weights for bdt ntuple
      double prob_fake_lepton_lead = evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
      double prob_fake_lepton_sublead = evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);
      double prob_fake_tau_lead = evtWeightRecorder.get_jetToTau_FR_lead(central_or_shift_main);
      double prob_fake_tau_sublead = evtWeightRecorder.get_jetToTau_FR_sublead(central_or_shift_main);
      double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
      double lep1_frWeight = lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead;
      double lep2_frWeight = lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead;
      double hadTau1_frWeight = hadTau1_genPt > 0 ? 1.0 : prob_fake_tau_lead;
      double hadTau2_frWeight = hadTau2_genPt > 0 ? 1.0 : prob_fake_tau_sublead;
      evtWeight_BDT *= lep1_frWeight*lep2_frWeight*hadTau1_frWeight*hadTau2_frWeight;
      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
	  ("deltaEta_lep1_lep2", deltaEta_lep1_lep2)
	  ("deltaEta_lep1_tau1", deltaEta_lep1_tau1)
	  ("deltaEta_lep1_tau2", deltaEta_lep1_tau2)
	  ("deltaEta_lep2_tau1", deltaEta_lep2_tau1)
	  ("deltaEta_lep2_tau2", deltaEta_lep2_tau2)
	  ("deltaEta_tau1_tau2", deltaEta_tau1_tau2)
	  ("deltaPhi_lep1_lep2", deltaPhi_lep1_lep2)
	  ("deltaPhi_lep1_tau1", deltaPhi_lep1_tau1)
	  ("deltaPhi_lep1_tau2", deltaPhi_lep1_tau2)
	  ("deltaPhi_lep2_tau1", deltaPhi_lep2_tau1)
	  ("deltaPhi_lep2_tau2", deltaPhi_lep2_tau2)
	  ("deltaPhi_tau1_tau2", deltaPhi_tau1_tau2)
	  ("dr_lep1_tau1_tau2_min", dr_lep1_tau1_tau2_min)
	  ("dr_lep1_tau1_tau2_max", dr_lep1_tau1_tau2_max)
	  ("dr_lep2_tau1_tau2_min", dr_lep2_tau1_tau2_min)
	  ("dr_lep2_tau1_tau2_max", dr_lep2_tau1_tau2_max)
	  ("dr_lep_tau_min_OS", dr_lep_tau_min_OS)
	  ("dr_lep_tau_min_SS", dr_lep_tau_min_SS)
	  ("pt_HH_recoil",             pt_HH_recoil)
          ("lep1_pt",                  selLepton_lead->pt())
          ("lep1_conePt",              selLepton_lead->cone_pt())
          ("lep1_eta",                 selLepton_lead->eta())
          ("lep1_phi",                 selLepton_lead->phi())
          ("lep1_tth_mva",             selLepton_lead->mvaRawTTH())
          ("mT_lep1",                  mT_lep1)
          ("lep2_pt",                  selLepton_sublead->pt())
          ("lep2_conePt",              selLepton_sublead->cone_pt())
          ("lep2_eta",                 selLepton_sublead->eta())
          ("lep2_phi",                 selLepton_lead->phi())
          ("lep2_tth_mva",             selLepton_sublead->mvaRawTTH())
          ("mT_lep2",                  mT_lep2)
          ("tau1_pt",                  selHadTau_lead->pt())
          ("tau1_eta",                 selHadTau_lead->eta())
          ("tau1_phi",                 selHadTau_lead->phi())
          ("tau1_mva",                 selHadTau_lead->id_mva(TauID::MVAoldDMdR032017v2))
          ("tau2_pt",                  selHadTau_sublead->pt())
          ("tau2_eta",                 selHadTau_sublead->eta())
          ("tau2_phi",                 selHadTau_lead->phi())
          ("tau2_mva",                 selHadTau_sublead->id_mva(TauID::MVAoldDMdR032017v2))
          ("dr_lep1_tau1",             dr_lep1_tau1)
          ("dr_lep2_tau1",             dr_lep2_tau1)
          ("dr_lep1_tau2",             dr_lep1_tau2)
          ("dr_lep2_tau2",             dr_lep2_tau2)
	  ("m_lep1_tau1",              m_lep1_tau1)
	  ("m_lep2_tau1",              m_lep2_tau1)
	  ("m_lep1_tau2",              m_lep1_tau2)
	  ("m_lep2_tau2",              m_lep2_tau2)
          ("dr_leps",                  dr_leps)
          ("dr_taus",                  dr_taus)
          ("avg_dr_jet",               avg_dr_jet)
          ("met",                      met.pt())
          ("met_phi",                  met.phi())
          ("mht",                      mht_p4.pt())
          ("met_LD",                   met_LD)
          ("HT",                       HT)
          ("STMET",                    STMET)
          ("m_ll",                     ll_p4.mass())
          ("pT_ll",                    ll_p4.pt())
          ("pT_llMEt",                 (ll_p4 + met.p4()).pt())
          ("Smin_llMEt",               Smin_llMEt)
          ("Smin_lltautau",            Smin_lltautau)
          ("mTauTauVis",               mTauTauVis_sel)
          ("mTauTau",                  mTauTau)
          ("ptTauTauVis",              ptTauTauVis_sel)
          ("diHiggsVisMass",           dihiggsVisMass_sel)
          ("diHiggsMass",              dihiggsMass)
          ("nJet",                     selJets.size())
          ("nBJet_loose",              selBJets_btag_loose.size())
          ("nBJet_medium",             selBJets_btag_medium.size())
          ("lep1_isElectron",          selLepton_lead_type == kElectron)
          ("lep1_charge",              selLepton_lead->charge())
          ("lep2_isElectron",          selLepton_sublead_type == kElectron)
          ("lep2_charge",              selLepton_sublead->charge())
          ("logTopness_publishedChi2", logTopness_publishedChi2)
          ("logTopness_fixedChi2",     logTopness_fixedChi2)
	  ("lep1_frWeight",       lep1_frWeight)
	  ("lep2_frWeight",       lep2_frWeight)
    	  ("hadTau1_frWeight",       hadTau1_frWeight)
    	  ("hadTau2_frWeight",       hadTau2_frWeight)
    	  ("genWeight" , eventInfo.genWeight)
    	  ("lheWeight" , evtWeightRecorder.get_lheScaleWeight(central_or_shift_main))
    	  ("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift_main))
    	  ("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift_main))
    	  ("btagWeight", evtWeightRecorder.get_btag(central_or_shift_main))
    	  ("leptonEffSF", evtWeightRecorder.get_leptonSF())
    	  ("hadTauEffSF", evtWeightRecorder.get_tauSF(central_or_shift_main))
    	  ("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift_main))
    	  ("FR_Weight", evtWeightRecorder.get_FR(central_or_shift_main))
          ("evtWeight",           evtWeight_BDT)
          ("nElectron",                selElectrons.size())
          ("nMuon",                    selMuons.size())
	  (weightMapHH)
        .fill()
	;

    }
// --------- bdt filler section ends    

    ++selectedEntries;
    selectedEntries_weighted += evtWeightRecorder.get(central_or_shift_main);
    std::string process_and_genMatch = process_string;
    process_and_genMatch += selLepton_genMatch.name_;
    process_and_genMatch += "&";
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
    for(const leptonChargeFlipGenMatchEntry & leptonGenMatch_definition: leptonGenMatch_definitions)
    {
      for(const hadTauGenMatchEntry & hadTauGenMatch_definition: hadTauGenMatch_definitions)
      {
	std::string process_and_genMatch = process_string;
        process_and_genMatch += leptonGenMatch_definition.name_;
        process_and_genMatch += "&";
        process_and_genMatch += hadTauGenMatch_definition.name_;
        std::cout << " " << process_and_genMatch << " = " << selectedEntries_byGenMatchType[process_and_genMatch]
                  << " (weighted = " << selectedEntries_weighted_byGenMatchType[central_or_shift][process_and_genMatch] << ")\n";
      }
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

  delete leptonFakeRateInterface;
  delete jetToTauFakeRateInterface;

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
  delete cutFlowHistManager;
  delete eventWeightManager;

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);
  hltPaths_delete(triggers_1e1mu);

  delete inputTree;

  clock.Show("analyze_hh_2l_2tau");

  return EXIT_SUCCESS;
}
