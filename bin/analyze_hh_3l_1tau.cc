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
#include "TLorentzVector.h"

#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
//#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions.h" // check_mvaInputs, get_mvaInputVariables
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // auxiliary functions for computing input variables of the MVA used for signal extraction in the 3l category

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicity.h" // ObjectMultiplicity
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/LeptonFakeRateInterface.h" // LeptonFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/JetToTauFakeRateInterface.h" // JetToTauFakeRateInterface
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReaderAK8.h" // RecoJetReaderAK8
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
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauCollectionSelectorECalCrack.h" // RecoHadTauSelectorECalCrack
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManagerAK8.h" // JetHistManagerAK8
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
#include "tthAnalysis/HiggsToTauTau/interface/hadTauGenMatchingAuxFunctions.h" // getHadTauGenMatch_definitions_1tau, getHadTauGenMatch
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h" // getWeight_1L, getWeight_2L
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
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface_2.h" // HHWeightInterface
#include "tthAnalysis/HiggsToTauTau/interface/BM_list.h" // BMS
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility

#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_3l_1tau.h" // EvtHistManager_hh_3l_1tau
#include "hhAnalysis/multilepton/interface/SVfit4tauHistManager_MarkovChain.h" // SVfit4tauHistManager_MarkovChain
#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // getMeasuredTauLeptonType, getHadTauDecayMode
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertex.h" // RecoVertex
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertexReader.h" // RecoVertexReader
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "TauAnalysis/ClassicSVfit4tau/interface/ClassicSVfit4tau.h" // ClassicSVfit4tau
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit4tau/interface/svFitHistogramAdapter4tau.h" // HistogramAdapterDiHiggs, HistogramAdapterHiggs

#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h"
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h"

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
#include <array> // std::array<>
#include <tuple> // std::tuple<>, std::get<>(), std::make_tuple()


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

enum { kFR_disabled, kFR_3lepton, kFR_4L, kFR_1tau };

//const int hadTauSelection_antiElectron = 1; // vLoose
//const int hadTauSelection_antiMuon = 1; // Loose
const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied

/**
 * @brief Produce datacard and control plots for 3l_1tau category of HH "multilepton" (HH->WWWW,WWtt,tttt) analysis.
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

  std::cout << "<analyze_hh_3l_1tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_3l_1tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_3l_1tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");
 

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_3l_1tau");

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

  // single lepton triggers
  vstring triggerNames_1e = cfg_analyze.getParameter<vstring>("triggers_1e");
  std::vector<hltPath*> triggers_1e = create_hltPaths(triggerNames_1e, "triggers_1e");
  bool use_triggers_1e = cfg_analyze.getParameter<bool>("use_triggers_1e");
  vstring triggerNames_1mu = cfg_analyze.getParameter<vstring>("triggers_1mu");
  std::vector<hltPath*> triggers_1mu = create_hltPaths(triggerNames_1mu, "triggers_1mu");
  bool use_triggers_1mu = cfg_analyze.getParameter<bool>("use_triggers_1mu");
  // double lepton triggers
  vstring triggerNames_2e = cfg_analyze.getParameter<vstring>("triggers_2e");
  std::vector<hltPath*> triggers_2e = create_hltPaths(triggerNames_2e, "triggers_2e");
  bool use_triggers_2e = cfg_analyze.getParameter<bool>("use_triggers_2e");
  vstring triggerNames_1e1mu = cfg_analyze.getParameter<vstring>("triggers_1e1mu");
  std::vector<hltPath*> triggers_1e1mu = create_hltPaths(triggerNames_1e1mu, "triggers_1e1mu");
  bool use_triggers_1e1mu = cfg_analyze.getParameter<bool>("use_triggers_1e1mu");
  vstring triggerNames_2mu = cfg_analyze.getParameter<vstring>("triggers_2mu");
  std::vector<hltPath*> triggers_2mu = create_hltPaths(triggerNames_2mu, "triggers_2mu");
  bool use_triggers_2mu = cfg_analyze.getParameter<bool>("use_triggers_2mu");
  // triple lepton triggers
  vstring triggerNames_3e = cfg_analyze.getParameter<vstring>("triggers_3e");
  std::vector<hltPath*> triggers_3e = create_hltPaths(triggerNames_3e, "triggers_3e");
  bool use_triggers_3e = cfg_analyze.getParameter<bool>("use_triggers_3e");
  vstring triggerNames_2e1mu = cfg_analyze.getParameter<vstring>("triggers_2e1mu");
  std::vector<hltPath*> triggers_2e1mu = create_hltPaths(triggerNames_2e1mu, "triggers_2e1mu");
  bool use_triggers_2e1mu = cfg_analyze.getParameter<bool>("use_triggers_2e1mu");
  vstring triggerNames_1e2mu = cfg_analyze.getParameter<vstring>("triggers_1e2mu");
  std::vector<hltPath*> triggers_1e2mu = create_hltPaths(triggerNames_1e2mu, "triggers_1e2mu");
  bool use_triggers_1e2mu = cfg_analyze.getParameter<bool>("use_triggers_1e2mu");
  vstring triggerNames_3mu = cfg_analyze.getParameter<vstring>("triggers_3mu");
  std::vector<hltPath*> triggers_3mu = create_hltPaths(triggerNames_3mu, "triggers_3mu");
  bool use_triggers_3mu = cfg_analyze.getParameter<bool>("use_triggers_3mu");

  bool apply_offline_e_trigger_cuts_1e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e");
  bool apply_offline_e_trigger_cuts_1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1mu");
  bool apply_offline_e_trigger_cuts_2e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e");
  bool apply_offline_e_trigger_cuts_1e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e1mu");
  bool apply_offline_e_trigger_cuts_2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2mu");
  bool apply_offline_e_trigger_cuts_3e = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_3e");
  bool apply_offline_e_trigger_cuts_2e1mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_2e1mu");
  bool apply_offline_e_trigger_cuts_1e2mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_1e2mu");
  bool apply_offline_e_trigger_cuts_3mu = cfg_analyze.getParameter<bool>("apply_offline_e_trigger_cuts_3mu");

  const std::string electronSelection_string = cfg_analyze.getParameter<std::string>("electronSelection");
  const std::string muonSelection_string     = cfg_analyze.getParameter<std::string>("muonSelection");
  std::cout << "electronSelection_string = " << electronSelection_string << "\n"
               "muonSelection_string     = " << muonSelection_string     << '\n'
  ;
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);
  
  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_3lepton(true);
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
  std::vector<hadTauGenMatchEntry> hadTauGenMatch_definitions = getHadTauGenMatch_definitions_1tau(true);
  std::cout << "hadTauGenMatch_definitions:" << std::endl;
  std::cout << hadTauGenMatch_definitions;

  GenMatchInterface genMatchInterface(3, apply_leptonGenMatching, false, 1, apply_hadTauGenMatching);

  enum { kOS, kSS };
  std::string chargeSumSelection_string = cfg_analyze.getParameter<std::string>("chargeSumSelection");
  int chargeSumSelection = -1;
  if      ( chargeSumSelection_string == "OS" ) chargeSumSelection = kOS;
  else if ( chargeSumSelection_string == "SS" ) chargeSumSelection = kSS;
  else throw cms::Exception("analyze_hh_3l_1tau")
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
  else if ( applyFakeRateWeights_string == "3lepton"  ) applyFakeRateWeights = kFR_3lepton;
  else if ( applyFakeRateWeights_string == "4L"       ) applyFakeRateWeights = kFR_4L;
  else if ( applyFakeRateWeights_string == "1tau"     ) applyFakeRateWeights = kFR_1tau;
  else throw cms::Exception("analyze_hh_3l_1tau")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_4L || applyFakeRateWeights == kFR_3lepton) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    cfg_leptonFakeRateWeight.addParameter<std::string>("era", era_string);
    cfg_leptonFakeRateWeight.addParameter<std::vector<std::string>>("central_or_shifts", central_or_shifts_local);
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight);
  }

  JetToTauFakeRateInterface* jetToTauFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_4L || applyFakeRateWeights == kFR_1tau || apply_hadTauFakeRateSF ) {
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
  std::string branchName_vertex = cfg_analyze.getParameter<std::string>("branchName_vertex");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");

  std::string branchName_muonGenMatch     = cfg_analyze.getParameter<std::string>("branchName_muonGenMatch");
  std::string branchName_electronGenMatch = cfg_analyze.getParameter<std::string>("branchName_electronGenMatch");
  std::string branchName_hadTauGenMatch   = cfg_analyze.getParameter<std::string>("branchName_hadTauGenMatch");
  std::string branchName_jetGenMatch      = cfg_analyze.getParameter<std::string>("branchName_jetGenMatch");

  const bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  const bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");
  const bool genMatchingByIndex = cfg_analyze.getParameter<bool>("genMatchingByIndex");

  const bool selectBDT = cfg_analyze.exists("selectBDT") ? cfg_analyze.getParameter<bool>("selectBDT") : false;
  std::string BDTFileName_even  = cfg_analyze.getParameter<std::string>("BDT_xml_FileName_even");
  std::string BDTFileName_odd   = cfg_analyze.getParameter<std::string>("BDT_xml_FileName_odd");
  std::string BDTFileName_nonRes_even  = cfg_analyze.getParameter<std::string>("BDT_nonRes_xml_FileName_even");
  std::string BDTFileName_nonRes_odd   = cfg_analyze.getParameter<std::string>("BDT_nonRes_xml_FileName_odd");
  std::string fitFunctionFileName = cfg_analyze.getParameter<std::string>("fitFunctionFileName");
  std::vector<double> gen_mHH = cfg_analyze.getParameter<std::vector<double>>("gen_mHH");
  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  std::string selEventsFileName_output = cfg_analyze.getParameter<std::string>("selEventsFileName_output");
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

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
  std::cout << "Number of points being scanned = " << Nscan << '\n';
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

  RecoVertexReader vertexReader(branchName_vertex);
  inputTree -> registerReader(&vertexReader);

  ObjectMultiplicity objectMultiplicity;
  ObjectMultiplicityReader objectMultiplicityReader(&objectMultiplicity);
  if(useObjectMultiplicity)
  {
    inputTree -> registerReader(&objectMultiplicityReader);
  }
  const int minLeptonSelection = std::min(electronSelection, muonSelection);

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_1mu, triggers_2e, triggers_1e1mu, triggers_2mu, triggers_3e, triggers_2e1mu, triggers_1e2mu, triggers_3mu });
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

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree -> registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  //RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable_hh_multilepton fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree -> registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  //RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable_hh_multilepton fakeableElectronSelector(era, -1, isDEBUG);
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
  RecoHadTauSelectorECalCrack crackVetoHadTauFilter(era, -1, isDEBUG);

  RecoJetReader* jetReader = new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  jetReader->setPtMass_central_or_shift(jetPt_option);
  jetReader->read_btag_systematics((central_or_shifts_local.size() > 1 || central_or_shift_main != "central") && isMC);
  inputTree -> registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerByIndex(isDEBUG);
  RecoJetCollectionSelector jetSelector(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);

  RecoJetCollectionSelectorBtagMedium jetSelector_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelector_bTagMedium(era, -1, isDEBUG);


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

  GenParticleReader * genHiggsReader      = nullptr;
  
  if(isMC)
  {
    genHiggsReader  = new GenParticleReader("GenHiggs");
    genHiggsReader -> readGenPartFlav(false);
    inputTree -> registerReader(genHiggsReader);
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

  //BDT definitions
  std::vector<std::string> BDTInputVariables_SUM =
    {
      "gen_mHH", "mT_nonZlepMET", "mT_SSlephigh", "mT_SSleplow", "mT_SSlepdR", "met_LD", "HT", "diHiggsVisMass", "diHiggsMass", "dR_ltau_minltaupair", "dEta_ltau_minltaupair", "pT_ltau_minltaupair", "m_ltau_minltaupair", "dR_ll_minltaupair", "dEta_ll_minltaupair", "pT_ll_minltaupair", "m_ll_minltaupair", "dR_ltau_minllpair", "dEta_ltau_minllpair", "pT_ltau_minllpair", "m_ltau_minllpair", "dR_ll_minllpair", "dEta_ll_minllpair", "pT_ll_minllpair", "m_ll_minllpair", "mllOS_closestToZ", "SVFit_h1_visMass", "SVFit_h2_visMass", "SVFit_h1_pT", "SVFit_h2_pT", "SVFit_hh_deltaR", "SVFit_hh_deltaEta", "SVFit_hh_pT", "nSFOS", "dR_smartpair1", "dEta_smartpair1", "m_smartpair1", "pT_smartpair1", "pTSum_smartpair1", "dR_smartpair2", "dEta_smartpair2", "m_smartpair2", "pT_smartpair2", "pTSum_smartpair2", "mZ_tau", "nElectron"
    }; 

  std::vector<std::string> BDTInputVariables_nonRes_SUM =
    {
"pTSum_smartpair_ll", "m_smartpair_ll", "diHiggsVisMass", "met_LD", "dR_smartpair_ltau", "mllOS_closestToZ", "pTDiff_smartpair_ll", "HT", "mT_SSlephigh", "m_smartpair_ltau", "pTSum_smartpair_ltau", "dR_smartpair_ll", "nSFOS", "diHiggsMass", "nElectron", "pTDiff_smartpair_ltau", "mT_SSleplow", "mZ_tau", "nodeX"
    }; 
  assert(fitFunctionFileName != "");
  //XGBInterface* BDT_nonRes_SUM = new XGBInterface(BDTFileName_nonRes_odd, BDTFileName_nonRes_even, BDTInputVariables_nonRes_SUM);
  //XGBInterface* BDT_SUM = new XGBInterface(BDTFileName_odd, BDTFileName_even, fitFunctionFileName, BDTInputVariables_SUM);

  std::map<std::string, double> BDTInputs_SUM;
  std::map<std::string, double> BDTInputs_nonRes_SUM;

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;

//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    MuonHistManager* muons_;
    HadTauHistManager* hadTaus_;
    JetHistManager* jets_;
    JetHistManager* BJets_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    std::map<std::string, EvtHistManager_hh_3l_1tau*> evt_;
    std::map<std::string, SVfit4tauHistManager_MarkovChain*> svFit4tau_woMassConstraint_;
    std::map<std::string, SVfit4tauHistManager_MarkovChain*> svFit4tau_wMassConstraint_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_3l_1tau*>> evt_in_decayModes_;
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

      int idxLepton_and_HadTau = genMatchDefinition->getIdx();

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
        selHistManager->evt_[evt_cat_str] = new EvtHistManager_hh_3l_1tau(makeHistManager_cfg(process_and_genMatchName,
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
            selHistManager->evt_in_decayModes_[evt_cat_str][decayMode_evt] = new EvtHistManager_hh_3l_1tau(makeHistManager_cfg(decayMode_and_genMatchName,
	    Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift, gen_mHH));
            selHistManager->evt_in_decayModes_[evt_cat_str][decayMode_evt] -> bookHistograms(fs);
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
        selHistManager->weights_->bookHistograms(fs, {
          "genWeight", "lheWeight", "pileupWeight",
          "triggerWeight", "btagWeight", "leptonEff", "hadTauEff", "data_to_MC_correction",
          "fakeRate" });
      }
      selHistManagers[central_or_shift][idxLepton_and_HadTau] = selHistManager;
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
      "lep1_pt", "lep1_conePt", "lep1_eta", "lep1_tth_mva",
      "mT_lep1", "lep1_phi",
      "lep2_pt", "lep2_conePt", "lep2_eta", "lep2_tth_mva",
      "mT_lep2", "lep2_phi",
      "lep3_pt", "lep3_conePt", "lep3_eta", "lep3_tth_mva",
      "mT_lep3", "lep3_phi",
       "mT_nonZlepMET","mT_SSlephigh","mT_SSleplow","mT_SSlepdR",
      "evtWeight",
      "lep1_frWeight", "lep2_frWeight", "lep3_frWeight",  "hadTau_frWeight",  
      "met", "mht", "met_LD", "HT", "STMET",
      "diHiggsVisMass", "diHiggsMass",
      "tau1_pt", "tau1_eta", "tau1_mva_dR03", "tau1_mva_deepvsj", "tau1_phi",
      "dr_lep1_tau1", "dr_lep2_tau1", "dr_lep3_tau1", "dr_lep1_lep2","dr_lep1_lep3", "dr_lep2_lep3",
      "m_lep1_tau1", "m_lep2_tau1", "m_lep3_tau1",
      "deltaEta_lep1_lep2", "deltaEta_lep1_tau1", "deltaEta_lep2_tau1", "deltaEta_lep1_lep3", "deltaEta_lep2_lep3", "deltaEta_lep3_tau1",
      "deltaPhi_lep1_lep2", "deltaPhi_lep1_tau1", "deltaPhi_lep2_tau1", "deltaPhi_lep1_lep3", "deltaPhi_lep2_lep3", "deltaPhi_lep3_tau1",
      "mlll", "mAll",
      "dR_ltau_minltaupair","dEta_ltau_minltaupair","dPhi_ltau_minltaupair","pT_ltau_minltaupair","m_ltau_minltaupair", "dR_ll_minltaupair","dEta_ll_minltaupair","dPhi_ll_minltaupair","pT_ll_minltaupair","m_ll_minltaupair",
      "dR_ltau_minllpair","dEta_ltau_minllpair","dPhi_ltau_minllpair","pT_ltau_minllpair","m_ltau_minllpair", "dR_ll_minllpair","dEta_ll_minllpair","dPhi_ll_minllpair","pT_ll_minllpair","m_ll_minllpair",
      "mllOS_closestToZ",
      "SVFit_h1_visMass","SVFit_h2_visMass", "SVFit_h1_pT", "SVFit_h2_pT", "SVFit_hh_deltaPhi", "SVFit_hh_deltaR", "SVFit_hh_deltaEta",  "SVFit_hh_pT", "SVFit_hh_cosTheta",
      //"genHiggs1_pt", "genHiggs1_eta","genHiggs1_phi","genHiggs2_pt","genHiggs2_eta","genHiggs2_phi", "genDiHiggs_pt","genDiHiggs_eta","genDiHiggs_phi","genDiHiggs_M","genDiHiggs_dR","genDiHiggs_dPhi","genDiHiggs_dEta","genDiHiggs_cosTheta",
      "nSFOS", "dR_smartpair1", "dEta_smartpair1", "dPhi_smartpair1", "m_smartpair1", "pT_smartpair1", "pTSum_smartpair1", "dR_smartpair2", "dEta_smartpair2", "dPhi_smartpair2", "m_smartpair2", "pT_smartpair2", "pTSum_smartpair2", "dR_smartpair_ltau", "dEta_smartpair_ltau", "dPhi_smartpair_ltau", "m_smartpair_ltau", "pT_smartpair_ltau", "pTSum_smartpair_ltau", "dR_smartpair_ll", "dEta_smartpair_ll", "dPhi_smartpair_ll", "m_smartpair_ll", "pT_smartpair_ll", "pTSum_smartpair_ll", "mZ_tau", "dPhi_nonZlMET", "mindPhiLepMET", "pTDiff_smartpair1", "pTDiff_smartpair2","pTDiff_smartpair_ltau", "pTDiff_smartpair_ll", "SVFit_Z1_visMass","SVFit_Z2_visMass", "pT4l",
      "genWeight" , "lheWeight" , "pileupWeight", "triggerWeight", "btagWeight", "leptonEffSF", "hadTauEffSF", "data_to_MC_correction","FR_Weight"
     );
    bdt_filler->register_variable<int_type>(
      "nJet",
      "lep1_isElectron", "lep1_charge", "lep2_isElectron", "lep2_charge", "lep3_isElectron", "lep3_charge",
      "nElectron", "nMuon", "nTaus"
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
    ">= 3 presel leptons",
    "presel lepton trigger match",
    ">= 1 fakeable taus",
    "b-jet veto",
    ">= 3 sel leptons",
    "<= 3 tight leptons",
    ">= 1 sel taus",
    "tau crack veto",
    "tau pt window",
    "bad tau cuts",
    "fakeable lepton trigger match",
    "HLT filter matching",
    "m(ll) > 12 GeV",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 10 GeV",
    "sel lepton charge",
    "sel lepton+tau charge",
    "Z-boson mass veto",
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

    if(run_lumi_eventSelector)
    {
      std::cout << "processing Entry " << inputTree -> getCurrentMaxEventIdx() << ": " << eventInfo << '\n';
      if(inputTree -> isOpen())
      {
        std::cout << "input File = " << inputTree -> getCurrentFileName() << '\n';
      }
    }

    if(useObjectMultiplicity)
    {
      if(objectMultiplicity.getNRecoLepton(minLeptonSelection) < 3 ||
         objectMultiplicity.getNRecoLepton(kTight)             > 3 ||
         objectMultiplicity.getNRecoHadTau(tauId, tauLevel)    < 1  )
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
    std::vector<GenParticle> genHiggs;
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
      if (bdt_filler) genHiggs = genHiggsReader->read();
      if(isDEBUG)
      {
        printCollection("genLeptons", genLeptons);
        printCollection("genHadTaus", genHadTaus);
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

    bool isTriggered_1e = hltPaths_isTriggered(triggers_1e, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_1mu = hltPaths_isTriggered(triggers_1mu, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_2e = hltPaths_isTriggered(triggers_2e, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_1e1mu = hltPaths_isTriggered(triggers_1e1mu, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_2mu = hltPaths_isTriggered(triggers_2mu, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_3e = hltPaths_isTriggered(triggers_3e, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_2e1mu = hltPaths_isTriggered(triggers_2e1mu, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_1e2mu = hltPaths_isTriggered(triggers_1e2mu, triggerWhiteList, eventInfo, isMC, isDEBUG);
    bool isTriggered_3mu = hltPaths_isTriggered(triggers_3mu, triggerWhiteList, eventInfo, isMC, isDEBUG);
    if ( isDEBUG ) {
      std::cout << "isTriggered:"
		<< " 1e = " << isTriggered_1e << ","
		<< " 1mu = " << isTriggered_1mu << ","
		<< " 2e = " << isTriggered_2e << ","
		<< " 1e1mu = " << isTriggered_1e1mu << ","
		<< " 2mu = " << isTriggered_2mu << ","
		<< " 3e = " << isTriggered_3e << ","
		<< " 2e1mu = " << isTriggered_2e1mu << ","
		<< " 1e2mu = " << isTriggered_1e2mu << ","
		<< " 3mu = " << isTriggered_3mu << std::endl;
    }

    bool selTrigger_1e = use_triggers_1e && isTriggered_1e;
    bool selTrigger_1mu = use_triggers_1mu && isTriggered_1mu;
    bool selTrigger_2e = use_triggers_2e && isTriggered_2e;
    bool selTrigger_1e1mu = use_triggers_1e1mu && isTriggered_1e1mu;
    bool selTrigger_2mu = use_triggers_2mu && isTriggered_2mu;
    bool selTrigger_3e = use_triggers_3e && isTriggered_3e;
    bool selTrigger_2e1mu = use_triggers_2e1mu && isTriggered_2e1mu;
    bool selTrigger_1e2mu = use_triggers_1e2mu && isTriggered_1e2mu;
    bool selTrigger_3mu = use_triggers_3mu && isTriggered_3mu;
    if ( !(selTrigger_1e || selTrigger_1mu   ||
	   selTrigger_2e || selTrigger_1e1mu || selTrigger_2mu   ||
	   selTrigger_3e || selTrigger_2e1mu || selTrigger_1e2mu || selTrigger_3mu) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	std::cout << " (selTrigger_3mu = " << selTrigger_3mu
		  << ", selTrigger_1e2mu = " << selTrigger_1e2mu
		  << ", selTrigger_2e1mu = " << selTrigger_2e1mu
		  << ", selTrigger_3e = " << selTrigger_3e
		  << ", selTrigger_2mu = " << selTrigger_2mu
		  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
		  << ", selTrigger_2e = " << selTrigger_2e
		  << ", selTrigger_1mu = " << selTrigger_1mu
		  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }

//--- rank triggers by priority and ignore triggers of lower priority if a trigger of higher priority has fired for given event;
//    the triggers are ranked by primary dataset (PD).
//    The ranking of the PDs is as follows: DoubleMuon, MuonEG, DoubleEG, SingleMuon, SingleElectron
// CV: see https://cmssdt.cern.ch/lxr/source/HLTrigger/Configuration/python/HLT_GRun_cff.py?v=CMSSW_8_0_24 for association of triggers paths to PD
//     this logic is necessary to avoid that the same event is selected multiple times when processing different primary datasets
    if ( !isMC && !isDEBUG ) {

      //bool isTriggered_SingleElectron = isTriggered_1e;
      bool isTriggered_SingleMuon = isTriggered_1mu;
      bool isTriggered_DoubleEG = isTriggered_2e || isTriggered_3e;
      bool isTriggered_DoubleMuon = isTriggered_2mu || isTriggered_3mu;
      bool isTriggered_MuonEG = isTriggered_1e1mu || isTriggered_2e1mu || isTriggered_1e2mu;

      bool selTrigger_SingleElectron = selTrigger_1e;
      bool selTrigger_SingleMuon = selTrigger_1mu;
      bool selTrigger_DoubleEG = selTrigger_2e || selTrigger_3e;
      //bool selTrigger_DoubleMuon = selTrigger_2mu || selTrigger_3mu;
      bool selTrigger_MuonEG = selTrigger_1e1mu || selTrigger_2e1mu || selTrigger_1e2mu;
      if ( selTrigger_SingleElectron && (isTriggered_SingleMuon || isTriggered_DoubleMuon || isTriggered_MuonEG) ) {
	if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_SingleElectron = " << selTrigger_SingleElectron
		    << ", isTriggered_SingleMuon = " << isTriggered_SingleMuon
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
		    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")" << std::endl;
	}
	continue;
      }
      if ( selTrigger_SingleElectron && isTriggered_DoubleEG && era != Era::k2018 ) {
        if ( run_lumi_eventSelector ) {
          std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
          std::cout << " (selTrigger_SingleElectron = " << selTrigger_SingleElectron
                    << ", isTriggered_DoubleEG = " << isTriggered_DoubleEG << ")" << std::endl;
        }
        continue;
      }
      if ( selTrigger_DoubleEG && (isTriggered_DoubleMuon || isTriggered_MuonEG) ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_DoubleEG = " << selTrigger_DoubleEG
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
		    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")" << std::endl;
	}
	continue;
      }
      if ( selTrigger_SingleMuon && (isTriggered_DoubleEG || isTriggered_DoubleMuon || isTriggered_MuonEG) ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_SingleMuon = " << selTrigger_SingleMuon
		    << ", isTriggered_DoubleEG = " << isTriggered_DoubleEG
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon
		    << ", isTriggered_MuonEG = " << isTriggered_MuonEG << ")" << std::endl;
	}
	continue;
      }
      if ( selTrigger_MuonEG && isTriggered_DoubleMuon ) {
	if ( run_lumi_eventSelector ) {
      std::cout << "event " << eventInfo.str() << " FAILS trigger selection." << std::endl;
	  std::cout << " (selTrigger_MuonEG = " << selTrigger_MuonEG
		    << ", isTriggered_DoubleMuon = " << isTriggered_DoubleMuon << ")" << std::endl;
	}
	continue;
      }
    }
    cutFlowTable.update("trigger", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger", evtWeightRecorder.get(central_or_shift_main));

    if ( (selTrigger_3mu   && !apply_offline_e_trigger_cuts_3mu)   ||
	 (selTrigger_2e1mu && !apply_offline_e_trigger_cuts_2e1mu) ||
	 (selTrigger_1e2mu && !apply_offline_e_trigger_cuts_1e2mu) ||
	 (selTrigger_3e    && !apply_offline_e_trigger_cuts_3e)    ||
	 (selTrigger_2mu   && !apply_offline_e_trigger_cuts_2mu)   ||
	 (selTrigger_1e1mu && !apply_offline_e_trigger_cuts_1e1mu) ||
	 (selTrigger_2e    && !apply_offline_e_trigger_cuts_2e)    ||
	 (selTrigger_1mu   && !apply_offline_e_trigger_cuts_1mu)   ||
	 (selTrigger_1e    && !apply_offline_e_trigger_cuts_1e)    ) {
      fakeableElectronSelector.disable_offline_e_trigger_cuts();
      tightElectronSelector.disable_offline_e_trigger_cuts();
    } else {
      fakeableElectronSelector.enable_offline_e_trigger_cuts();
      tightElectronSelector.enable_offline_e_trigger_cuts();
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

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 3);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 3);
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

    const std::vector<const RecoHadTau*> fakeableHadTaus = pickFirstNobjects(fakeableHadTausFull, 1);
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
    const std::vector<RecoJet> jets_ak4 = jetReader->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4, fakeableLeptons);
    const std::vector<const RecoJet*> selJets = jetSelector(cleanedJets, isHigherPt);
    const std::vector<const RecoJet*> selBJets_loose = jetSelectorBtagLoose(cleanedJets, isHigherPt);
    const std::vector<const RecoJet*> selBJets_medium = jetSelectorBtagMedium(cleanedJets, isHigherPt);
    int numSelJetsPtGt40 = countHighPtObjects(selJets, 40.);
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("uncleanedJets", jet_ptrs);
      printCollection("selJets",       selJets);
    }

    const std::vector<const RecoJet*> selJetsAK4 = jetSelector(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelector_bTagLoose(cleanedJetsAK4_wrtLeptons, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelector_bTagMedium(cleanedJetsAK4_wrtLeptons, isHigherPt);

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
    // require exactly three leptons passing loose preselection criteria to avoid overlap with 4l category
    if ( !(preselLeptonsFull.size() >= 3) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
        printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 3 presel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 3 presel leptons", evtWeightRecorder.get(central_or_shift_main));

    // require that trigger paths match event category (with event category based on preselLeptons)
    if ( !((preselElectrons.size() >= 3 &&                            (selTrigger_3e    || selTrigger_2e  || selTrigger_1e                                      )) ||
	   (preselElectrons.size() >= 2 && preselMuons.size() >= 1 && (selTrigger_2e1mu || selTrigger_2e  || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (preselElectrons.size() >= 1 && preselMuons.size() >= 2 && (selTrigger_1e2mu || selTrigger_2mu || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (                               preselMuons.size() >= 3 && (selTrigger_3mu   || selTrigger_2mu || selTrigger_1mu                                     ))) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given preselLepton multiplicity." << std::endl;
	std::cout << " (#preselElectrons = " << preselElectrons.size()
		  << ", #preselMuons = " << preselMuons.size()
		  << ", selTrigger_3mu = " << selTrigger_3mu
		  << ", selTrigger_1e2mu = " << selTrigger_1e2mu
		  << ", selTrigger_2e1mu = " << selTrigger_2e1mu
		  << ", selTrigger_3e = " << selTrigger_3e
		  << ", selTrigger_2mu = " << selTrigger_2mu
		  << ", selTrigger_1e1mu = " << selTrigger_1e1mu
		  << ", selTrigger_2e = " << selTrigger_2e
		  << ", selTrigger_1mu = " << selTrigger_1mu
		  << ", selTrigger_1e = " << selTrigger_1e << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("presel lepton trigger match", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("presel lepton trigger match", evtWeightRecorder.get(central_or_shift_main));

    // require presence of at least one hadronic tau passing loose preselection criteria
    // (do not veto events with more than one loosely selected hadronic tau candidates,
    //  as sample of hadronic tau candidates passing loose preselection criteria contains significant contamination from jets)
    if ( !(fakeableHadTaus.size() >= 1) ) continue;
    cutFlowTable.update(">= 1 fakeable taus", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 fakeable taus", evtWeightRecorder.get(central_or_shift_main));

    if ( selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1 ) continue;
    cutFlowTable.update("b-jet veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("b-jet veto", evtWeightRecorder.get(central_or_shift_main));

//--- compute MHT and linear MET discriminant (met_LD)
    const RecoMEt met_uncorr = metReader->read();
    const RecoMEt met = recompute_met(met_uncorr, jets, met_option, isDEBUG);
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptonsFull, fakeableHadTausFull, selJets);
    double met_LD = compMEt_LD(met.p4(), mht_p4);

    double HT = compHT(fakeableLeptons, fakeableHadTaus, selJets);
    double STMET = compSTMEt(fakeableLeptons, fakeableHadTaus, selJets, met.p4());

//--- apply final event selection
    // require exactly three leptons passing tight selection criteria of final event selection
    if ( !(selLeptons.size() >= 3) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
	printCollection("selLeptons", selLeptons);
	//printCollection("preselLeptons", preselLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 3 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 3 sel leptons", evtWeightRecorder.get(central_or_shift_main));

    const RecoLepton* selLepton_lead = selLeptons[0];
    int selLepton_lead_type = getLeptonType(selLepton_lead->pdgId());
    const RecoLepton* selLepton_sublead = selLeptons[1];
    int selLepton_sublead_type = getLeptonType(selLepton_sublead->pdgId());
    const RecoLepton* selLepton_third = selLeptons[2];
    int selLepton_third_type = getLeptonType(selLepton_third->pdgId());
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead, selLepton_third);

    // require exactly three leptons passing tight selection criteria, to avoid overlap with 4l channel
    if ( !(tightLeptonsFull.size() <= 3) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection.\n";
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }

    // require that trigger paths match event category (with event category based on fakeableLeptons)
    if ( !((fakeableElectrons.size() >= 3 &&                         (selTrigger_3e    || selTrigger_2e  || selTrigger_1e                                      )) ||
	   (fakeableElectrons.size() >= 2 && fakeableMuons.size() >= 1 && (selTrigger_2e1mu || selTrigger_2e  || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 2 && (selTrigger_1e2mu || selTrigger_2mu || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (                            fakeableMuons.size() >= 3 && (selTrigger_3mu   || selTrigger_2mu || selTrigger_1mu                                     ))) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given preselLepton multiplicity." << std::endl;
	std::cout << " (#fakeableElectrons = " << fakeableElectrons.size()
		  << ", #fakeableMuons = " << fakeableMuons.size()
		  << ", selTrigger_3mu = " << selTrigger_3mu
		  << ", selTrigger_1e2mu = " << selTrigger_1e2mu
		  << ", selTrigger_2e1mu = " << selTrigger_2e1mu
		  << ", selTrigger_3e = " << selTrigger_3e
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

    if ( !(selHadTaus.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS selHadTaus selection." << std::endl;
	printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update(">= 1 sel taus", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 sel taus", evtWeightRecorder.get(central_or_shift_main));

    const RecoHadTau* selHadTau = selHadTaus[0];
    const hadTauGenMatchEntry& selHadTau_genMatch = getHadTauGenMatch(hadTauGenMatch_definitions, selHadTau);

    RecoVertex vertex = vertexReader.read();
    crackVetoHadTauFilter.set_vertex(vertex);
    bool selHadTau_isInCrack = !crackVetoHadTauFilter(*selHadTau);
    if ( selHadTau_isInCrack ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS tau crack veto." << std::endl;
	printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update("tau crack veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("tau crack veto", evtWeightRecorder.get(central_or_shift_main));

    int triggerECalCrackVeto = -1;
    if((TMath::Abs(selHadTau->eta())>0)&&(TMath::Abs(selHadTau->eta())<0.018)){
      triggerECalCrackVeto = 1;
    }
    else if((TMath::Abs(selHadTau->eta())>0.423)&&(TMath::Abs(selHadTau->eta())<0.461)){
      triggerECalCrackVeto = 1;
    }
    else if((TMath::Abs(selHadTau->eta())>0.770)&&(TMath::Abs(selHadTau->eta())<0.806)){
      triggerECalCrackVeto = 1;
    }
    else if((TMath::Abs(selHadTau->eta())>1.127)&&(TMath::Abs(selHadTau->eta())<1.163)){
      triggerECalCrackVeto = 1;
    }
    else if((TMath::Abs(selHadTau->eta())>1.460)&&(TMath::Abs(selHadTau->eta())<1.558)){
      triggerECalCrackVeto = 1;
    }
    else{
      triggerECalCrackVeto = 0;
    }
    if (selHadTau->id_mva(TauID::DeepTau2017v2VSe)<2){
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS cuts against tau fakes from ele." << std::endl;
	printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update("bad tau cuts", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("bad tau cuts", evtWeightRecorder.get(central_or_shift_main));


//--- apply HLT filter
    if(apply_hlt_filter)
    {
      const std::map<hltPathsE, bool> trigger_bits = {
        { hltPathsE::trigger_1e,    selTrigger_1e    },
        { hltPathsE::trigger_1mu,   selTrigger_1mu   },
        { hltPathsE::trigger_2e,    selTrigger_2e    },
        { hltPathsE::trigger_2mu,   selTrigger_2mu   },
        { hltPathsE::trigger_1e1mu, selTrigger_1e1mu },
        { hltPathsE::trigger_1e2mu, selTrigger_1e2mu },
        { hltPathsE::trigger_2e1mu, selTrigger_2e1mu },
        { hltPathsE::trigger_3e,    selTrigger_3e    },
        { hltPathsE::trigger_3mu,   selTrigger_3mu   },
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

      dataToMCcorrectionInterface->setLeptons({ selLepton_lead, selLepton_sublead, selLepton_third });

//--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_leptonTriggerEff(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      evtWeightRecorder.record_leptonIDSF_recoToLoose(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if(electronSelection >= kFakeable && muonSelection >= kFakeable)
      {
        // apply looseToTight SF to leptons matched to generator-level prompt leptons and passing Tight selection conditions
        evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface);
      }

//--- apply data/MC corrections for hadronic tau identification efficiency
//    and for e->tau and mu->tau misidentification rates
      dataToMCcorrectionInterface->setHadTaus({ selHadTau });
      evtWeightRecorder.record_hadTauID_and_Iso(dataToMCcorrectionInterface);
      evtWeightRecorder.record_eToTauFakeRate(dataToMCcorrectionInterface);
      evtWeightRecorder.record_muToTauFakeRate(dataToMCcorrectionInterface);
    }

    bool passesTight_hadTau = isMatched(*selHadTau, tightHadTausFull);
    bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
    bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);
    bool passesTight_lepton_third = isMatched(*selLepton_third, tightElectrons) || isMatched(*selLepton_third, tightMuons);

    if(leptonFakeRateInterface)
    {
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton_lead);
      evtWeightRecorder.record_jetToLepton_FR_sublead(leptonFakeRateInterface, selLepton_sublead);
      evtWeightRecorder.record_jetToLepton_FR_third(leptonFakeRateInterface, selLepton_third);
    }
    if(jetToTauFakeRateInterface)
    {
      evtWeightRecorder.record_jetToTau_FR_lead(jetToTauFakeRateInterface, selHadTau);
    }

    if(!selectBDT){
      if(applyFakeRateWeights == kFR_4L)
	{
	  evtWeightRecorder.compute_FR_3l1tau(
	  passesTight_lepton_lead, passesTight_lepton_sublead, passesTight_lepton_third, passesTight_hadTau
					      );
	}
      else if(applyFakeRateWeights == kFR_3lepton)
	{
	  evtWeightRecorder.compute_FR_3l(passesTight_lepton_lead, passesTight_lepton_sublead, passesTight_lepton_third);
	}
      else if(applyFakeRateWeights == kFR_1tau)
	{
	  evtWeightRecorder.compute_FR_1tau(passesTight_hadTau);
	}
    }
    // CV: apply data/MC ratio for jet->tau fake-rates in case data-driven "fake" background estimation is applied to leptons only
    if(isMC && apply_hadTauFakeRateSF && hadTauSelection == kTight && !(selHadTau->genHadTau() || selHadTau->genLepton()))
    {
      evtWeightRecorder.record_jetToTau_SF_lead(jetToTauFakeRateInterface, selHadTau);
    }

    const bool failsLowMassVeto = isfailsLowMassVeto(preselLeptonsFullUncleaned);
    if ( failsLowMassVeto ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS low mass lepton pair veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("m(ll) > 12 GeV", evtWeightRecorder.get(central_or_shift_main));
    
    const double minPt_lead = 25.;
    const double minPt_sublead = 15.;
    const double minPt_third = 10.;
    if ( !(selLepton_lead->cone_pt() > minPt_lead && selLepton_sublead->cone_pt() > minPt_sublead && selLepton_third->cone_pt() > minPt_third) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
	std::cout << " (leading selLepton pT = " << selLepton_lead->pt() << ", minPt_lead = " << minPt_lead
		  << ", subleading selLepton pT = " << selLepton_sublead->pt() << ", minPt_sublead = " << minPt_sublead
		  << ", third selLepton pT = " << selLepton_third->pt() << ", minPt_third = " << minPt_third << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 10 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 10 GeV", evtWeightRecorder.get(central_or_shift_main));

    int sumLeptonCharge = selLepton_lead->charge() + selLepton_sublead->charge() + selLepton_third->charge();
    if ( std::abs(sumLeptonCharge) != 1 ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge() << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("sel lepton charge", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel lepton charge", evtWeightRecorder.get(central_or_shift_main));

    bool isCharge_SS = sumLeptonCharge*selHadTau->charge() > 0.;
    bool isCharge_OS = sumLeptonCharge*selHadTau->charge() < 0.;
    if ( (chargeSumSelection == kOS && isCharge_SS) || (chargeSumSelection == kSS && isCharge_OS) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton+tau charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge()
		  << ", selHadTau charge = " << selHadTau->charge() << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("sel lepton+tau charge", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel lepton+tau charge", evtWeightRecorder.get(central_or_shift_main));
    // Z-veto (or invertedinverted) 
    const bool failsZbosonMassVeto = isfailsZbosonMassVeto(preselLeptonsFull);
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
    	std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));

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
      if ( applySignalRegionVeto_lepton && tightLeptons.size() >= 3 ) failsSignalRegionVeto = true;
      if ( applySignalRegionVeto_hadTau && tightHadTaus.size() >= 1 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable || hadTauSelection == kFakeable ) {
      if ( tightLeptons.size() >= 3 && tightHadTaus.size() >= 1 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
	             "# tight leptons = " << tightLeptons.size() << " >= 3 and "
                     "# tight taus = " << tightHadTaus.size() << " >= 1\n"
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
	std::cout << "Calculated " << reWeightMapHH.size() << " scan reweights\n";
	for(const auto & kv:reWeightMapHH)
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
    
    //compute bdt filler variables
    std::vector<SVfit4tauResult> svFit4tauResults_woMassConstraint = compSVfit4tau(
      *selLepton_lead, *selLepton_sublead, *selLepton_third, *selHadTau, met, chargeSumSelection_string, rnd,  -1., 2.);
    std::vector<SVfit4tauResult> svFit4tauResults_wMassConstraint = compSVfit4tau(
      *selLepton_lead, *selLepton_sublead, *selLepton_third, *selHadTau, met, chargeSumSelection_string, rnd, 125., 2.);

    std::vector<SVfit4tauResult> svFit4tauResults_wMassConstraint_Z = compSVfit4tau(
      *selLepton_lead, *selLepton_sublead, *selLepton_third, *selHadTau, met, chargeSumSelection_string, rnd, 91.2, 2.);

    double dihiggsVisMass_sel = (selLepton_lead->p4() + selLepton_sublead->p4() + selLepton_third->p4() + selHadTau->p4()).mass();
    double dihiggsMass = ( svFit4tauResults_wMassConstraint.size() >= 1 && svFit4tauResults_wMassConstraint[0].isValidSolution_ ) ? 
      svFit4tauResults_wMassConstraint[0].dihiggs_mass_ : -1.;
    double SVFit_h1_visMass = -1;
    double SVFit_h2_visMass = -1;
    double SVFit_h1_pT = -1;
    double SVFit_h2_pT = -1;
    double SVFit_hh_deltaPhi = -1;
    double SVFit_hh_deltaEta = -1;
    double SVFit_hh_deltaR = -1;
    double SVFit_hh_pT = -1;
    double SVFit_hh_cosTheta = -1;
    if ( svFit4tauResults_wMassConstraint.size() >= 1 && svFit4tauResults_wMassConstraint[0].isValidSolution_ ){
      TLorentzVector h1(1,0,0,1);
      TLorentzVector h2(1,0,0,1);
      h1.SetPtEtaPhiM(svFit4tauResults_wMassConstraint[0].ditau1_pt_, svFit4tauResults_wMassConstraint[0].ditau1_eta_, svFit4tauResults_wMassConstraint[0].ditau1_phi_, svFit4tauResults_wMassConstraint[0].ditau1_mass_);
      h2.SetPtEtaPhiM(svFit4tauResults_wMassConstraint[0].ditau2_pt_, svFit4tauResults_wMassConstraint[0].ditau2_eta_, svFit4tauResults_wMassConstraint[0].ditau2_phi_, svFit4tauResults_wMassConstraint[0].ditau2_mass_);
      SVFit_h1_visMass = svFit4tauResults_wMassConstraint[0].ditau1_visMass_;
      SVFit_h2_visMass = svFit4tauResults_wMassConstraint[0].ditau2_visMass_;;
      SVFit_h1_pT = h1.Pt();
      SVFit_h2_pT = h2.Pt();
      SVFit_hh_deltaPhi = h1.DeltaPhi(h2);
      SVFit_hh_deltaEta = TMath::Abs(h1.Eta()-h2.Eta());
      SVFit_hh_deltaR = h1.DeltaR(h2);
      SVFit_hh_pT = svFit4tauResults_wMassConstraint[0].dihiggs_pt_;
      TVector3 boostvector = (h1+h2).BoostVector();
      h1.Boost(-1*boostvector);
      h2.Boost(-1*boostvector);
      TLorentzVector beamaxis1 = TLorentzVector(0,0,1,1);
      TLorentzVector beamaxis2 = TLorentzVector(0,0,-1,1);
      beamaxis1.Boost(-1*boostvector);
      beamaxis2.Boost(-1*boostvector);
      TVector3 zaxisCS = (beamaxis1.Vect().Unit() - beamaxis2.Vect().Unit()).Unit();
      SVFit_hh_cosTheta = TMath::Abs(h1.Vect().Unit().Dot(zaxisCS));
    }
    double SVFit_Z1_visMass = -1;
    double SVFit_Z2_visMass = -1;
    if ( svFit4tauResults_wMassConstraint_Z.size() >= 1 && svFit4tauResults_wMassConstraint_Z[0].isValidSolution_ ){
      SVFit_Z1_visMass = svFit4tauResults_wMassConstraint_Z[0].ditau1_visMass_;
      SVFit_Z2_visMass = svFit4tauResults_wMassConstraint_Z[0].ditau2_visMass_;;
    }
    //--- retrieve gen-matching flags
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons, selHadTaus);
    //---additional evt variables
    TLorentzVector lep1LV(selLepton_lead->p4().px(),selLepton_lead->p4().py(),selLepton_lead->p4().pz(),selLepton_lead->p4().energy());
    TLorentzVector lep2LV(selLepton_sublead->p4().px(),selLepton_sublead->p4().py(),selLepton_sublead->p4().pz(),selLepton_sublead->p4().energy());
    TLorentzVector lep3LV(selLepton_third->p4().px(),selLepton_third->p4().py(),selLepton_third->p4().pz(),selLepton_third->p4().energy());
    TLorentzVector tau1LV(selHadTau->p4().px(),selHadTau->p4().py(),selHadTau->p4().pz(),selHadTau->p4().energy());
    TLorentzVector metLV(met.p4().px(),met.p4().py(),met.p4().pz(),met.p4().energy());
    double mT_nonZlepMET = -1;
    double mllOS_closestToZ = -1;
    double mZ_tau = -1;
    double dPhi_nonZlMET = -1;
    double mindPhiLepMET = TMath::Min(TMath::Abs(metLV.DeltaPhi(lep1LV)),TMath::Min(TMath::Abs(metLV.DeltaPhi(lep2LV)),TMath::Abs(metLV.DeltaPhi(lep3LV))));

    int nSFOS =0;
    if( ((selLepton_lead->charge()*selLepton_sublead->charge())< 0.)&&(selLepton_lead_type==selLepton_sublead_type)){
      nSFOS = nSFOS + 1;
    }
    if( ((selLepton_lead->charge()*selLepton_third->charge())< 0.)&&(selLepton_lead_type==selLepton_third_type)){
      nSFOS = nSFOS + 1;
    }
    if( ((selLepton_third->charge()*selLepton_sublead->charge())< 0.)&&(selLepton_third_type==selLepton_sublead_type)){
      nSFOS = nSFOS + 1;
    }
    if( ((selLepton_lead->charge()*selLepton_sublead->charge())< 0.)&&(selLepton_lead_type==selLepton_sublead_type)){
      mllOS_closestToZ = (selLepton_lead->p4()+selLepton_sublead->p4()).mass();
      mT_nonZlepMET = comp_MT_met(selLepton_third, met.pt(), met.phi());
      TLorentzVector temppair = tau1LV+lep3LV;
      mZ_tau = std::sqrt(2. * temppair.Pt() * met.pt() * (1. - std::cos(temppair.Phi() - met.phi())));
      dPhi_nonZlMET = TMath::Abs(metLV.DeltaPhi(lep3LV));
    }
    if( ( (selLepton_lead->charge()*selLepton_third->charge()) < 0. ) &&(selLepton_lead_type==selLepton_third_type)&& ( (mllOS_closestToZ <0) || ( TMath::Abs((selLepton_lead->p4()+selLepton_third->p4()).mass()-91.1876)< TMath::Abs(mllOS_closestToZ-91.1876) )) ){
      mllOS_closestToZ = ((selLepton_lead->p4()+selLepton_third->p4()).mass());
      mT_nonZlepMET = comp_MT_met(selLepton_sublead, met.pt(), met.phi());
      TLorentzVector temppair = tau1LV+lep2LV;
      mZ_tau = std::sqrt(2. * temppair.Pt() * met.pt() * (1. - std::cos(temppair.Phi() - met.phi())));
      dPhi_nonZlMET = TMath::Abs(metLV.DeltaPhi(lep2LV));
    }
    if( ( (selLepton_sublead->charge()*selLepton_third->charge()) < 0. ) &&(selLepton_sublead_type==selLepton_third_type)&& ( (mllOS_closestToZ <0) || ( TMath::Abs((selLepton_sublead->p4()+selLepton_third->p4()).mass()-91.1876)< TMath::Abs(mllOS_closestToZ-91.1876) )) ){
      mllOS_closestToZ = ((selLepton_sublead->p4()+selLepton_third->p4()).mass());
      mT_nonZlepMET = comp_MT_met(selLepton_lead, met.pt(), met.phi());
      TLorentzVector temppair = tau1LV+lep1LV;
      mZ_tau = std::sqrt(2. * temppair.Pt() * met.pt() * (1. - std::cos(temppair.Phi() - met.phi())));
      dPhi_nonZlMET = TMath::Abs(metLV.DeltaPhi(lep1LV));
    }
    double mT_SSlephigh= -1;
    double mT_SSleplow= -1;
    //double dr_lss  = -1.;
    double dr_los1 = -1.;
    double dr_los2 = -1.;
    // it does not assume mis-charge identification
    if (selLepton_lead->charge()*selLepton_sublead->charge() > 0){
      //dr_lss  = deltaR(selLepton_sublead -> p4(), selLepton_lead -> p4());
      dr_los1 = deltaR(selLepton_third -> p4(), selLepton_lead -> p4());
      dr_los2 = deltaR(selLepton_third  -> p4(), selLepton_sublead -> p4());
      mT_SSlephigh = comp_MT_met(selLepton_lead, met.pt(), met.phi());
      mT_SSleplow = comp_MT_met(selLepton_sublead, met.pt(), met.phi());
    } 
    else if (selLepton_lead->charge()*selLepton_third->charge() > 0){
      //dr_lss  = deltaR(selLepton_third -> p4(), selLepton_lead -> p4());
      dr_los1 = deltaR(selLepton_sublead -> p4(), selLepton_third -> p4());
      dr_los2 = deltaR(selLepton_sublead  -> p4(), selLepton_lead -> p4());
      mT_SSlephigh = comp_MT_met(selLepton_lead, met.pt(), met.phi());
      mT_SSleplow = comp_MT_met(selLepton_third, met.pt(), met.phi());
    }
    else {
      //dr_lss  = deltaR(selLepton_third -> p4(), selLepton_sublead -> p4());
      dr_los1 = deltaR(selLepton_lead -> p4(), selLepton_sublead -> p4());
      dr_los2 = deltaR(selLepton_lead  -> p4(), selLepton_third -> p4());
      mT_SSlephigh = comp_MT_met(selLepton_sublead, met.pt(), met.phi());
      mT_SSleplow = comp_MT_met(selLepton_third, met.pt(), met.phi());
    }
    double dR_ltau_minltaupair = -1;
    double dEta_ltau_minltaupair = -1;
    double dPhi_ltau_minltaupair = -1;
    double pT_ltau_minltaupair = -1;
    double m_ltau_minltaupair = -1;
    double dR_ll_minltaupair = -1;
    double dEta_ll_minltaupair = -1;
    double dPhi_ll_minltaupair = -1;
    double pT_ll_minltaupair = -1;
    double m_ll_minltaupair = -1;

    double dR_ltau_minllpair = -1;
    double dEta_ltau_minllpair = -1;
    double dPhi_ltau_minllpair = -1;
    double pT_ltau_minllpair = -1;
    double m_ltau_minllpair = -1;
    double dR_ll_minllpair = -1;
    double dEta_ll_minllpair = -1;
    double dPhi_ll_minllpair = -1;
    double pT_ll_minllpair = -1;
    double m_ll_minllpair = -1;

    double mT_SSlepdR = -1;


    if(selLepton_lead->charge()*selLepton_sublead->charge()<0){
      dR_ltau_minltaupair = lep3LV.DeltaR(tau1LV);
      dEta_ltau_minltaupair = TMath::Abs(lep3LV.Eta()-tau1LV.Eta());
      dPhi_ltau_minltaupair = TMath::Abs(lep3LV.DeltaPhi(tau1LV));
      pT_ltau_minltaupair = (lep3LV+tau1LV).Pt();
      m_ltau_minltaupair = (lep3LV+tau1LV).M();
      dR_ll_minltaupair = lep1LV.DeltaR(lep2LV);
      dEta_ll_minltaupair = TMath::Abs(lep1LV.Eta()-lep2LV.Eta());
      dPhi_ll_minltaupair = TMath::Abs(lep1LV.DeltaPhi(lep2LV));
      pT_ll_minltaupair = (lep1LV+lep2LV).Pt();
      m_ll_minltaupair = (lep1LV+lep2LV).M();

      mT_SSlepdR = comp_MT_met(selLepton_third, met.pt(), met.phi()); 
	  
      dR_ltau_minllpair = lep3LV.DeltaR(tau1LV);
      dEta_ltau_minllpair = TMath::Abs(lep3LV.Eta()-tau1LV.Eta());
      dPhi_ltau_minllpair = TMath::Abs(lep3LV.DeltaPhi(tau1LV));
      pT_ltau_minllpair = (lep3LV+tau1LV).Pt();
      m_ltau_minllpair = (lep3LV+tau1LV).M();
      dR_ll_minllpair = lep1LV.DeltaR(lep2LV);
      dEta_ll_minllpair = TMath::Abs(lep1LV.Eta()-lep2LV.Eta());
      dPhi_ll_minllpair = TMath::Abs(lep1LV.DeltaPhi(lep2LV));
      pT_ll_minllpair = (lep1LV+lep2LV).Pt();
      m_ll_minllpair = (lep1LV+lep2LV).M();
    }
    if(selLepton_lead->charge()*selLepton_third->charge()<0){
      double dRll_temp = lep1LV.DeltaR(lep3LV);
      double dRltau_temp = lep2LV.DeltaR(tau1LV);
      if((dR_ll_minllpair<0)||(dRll_temp<dR_ll_minllpair)){
	dR_ltau_minllpair = lep2LV.DeltaR(tau1LV);
	dEta_ltau_minllpair = TMath::Abs(lep2LV.Eta()-tau1LV.Eta());
	dPhi_ltau_minllpair = TMath::Abs(lep2LV.DeltaPhi(tau1LV));
	pT_ltau_minllpair = (lep2LV+tau1LV).Pt();
	m_ltau_minllpair = (lep2LV+tau1LV).M();
	dR_ll_minllpair = lep1LV.DeltaR(lep3LV);
	dEta_ll_minllpair = TMath::Abs(lep1LV.Eta()-lep3LV.Eta());
	dPhi_ll_minllpair = TMath::Abs(lep1LV.DeltaPhi(lep3LV));
	pT_ll_minllpair = (lep1LV+lep3LV).Pt();
	m_ll_minllpair = (lep1LV+lep3LV).M();

	mT_SSlepdR = comp_MT_met(selLepton_sublead, met.pt(), met.phi()); 
      }
      if((dR_ltau_minltaupair<0)||(dRltau_temp<dR_ltau_minltaupair)){
	dR_ltau_minltaupair = lep2LV.DeltaR(tau1LV);
	dEta_ltau_minltaupair = TMath::Abs(lep2LV.Eta()-tau1LV.Eta());
	dPhi_ltau_minltaupair = TMath::Abs(lep2LV.DeltaPhi(tau1LV));
	pT_ltau_minltaupair = (lep2LV+tau1LV).Pt();
	m_ltau_minltaupair = (lep2LV+tau1LV).M();
	dR_ll_minltaupair = lep1LV.DeltaR(lep3LV);
	dEta_ll_minltaupair = TMath::Abs(lep1LV.Eta()-lep3LV.Eta());
	dPhi_ll_minltaupair = TMath::Abs(lep1LV.DeltaPhi(lep3LV));
	pT_ll_minltaupair = (lep1LV+lep3LV).Pt();
	m_ll_minltaupair = (lep1LV+lep3LV).M();
      }
    }
    if(selLepton_sublead->charge()*selLepton_third->charge()<0){
      double dRll_temp = lep2LV.DeltaR(lep3LV);
      double dRltau_temp = lep1LV.DeltaR(tau1LV);
      if((dR_ll_minllpair<0)||(dRll_temp<dR_ll_minllpair)){
	dR_ltau_minllpair = lep1LV.DeltaR(tau1LV);
	dEta_ltau_minllpair = TMath::Abs(lep1LV.Eta()-tau1LV.Eta());
	dPhi_ltau_minllpair = TMath::Abs(lep1LV.DeltaPhi(tau1LV));
	pT_ltau_minllpair =( lep1LV+tau1LV).Pt();
	m_ltau_minllpair = (lep1LV+tau1LV).M();
	dR_ll_minllpair = lep2LV.DeltaR(lep3LV);
	dEta_ll_minllpair = TMath::Abs(lep2LV.Eta()-lep3LV.Eta());
	dPhi_ll_minllpair = TMath::Abs(lep2LV.DeltaPhi(lep3LV));
	pT_ll_minllpair = (lep2LV+lep3LV).Pt();
	m_ll_minllpair = (lep2LV+lep3LV).M();

	mT_SSlepdR = comp_MT_met(selLepton_lead, met.pt(), met.phi()); 
      }
      if((dR_ltau_minltaupair<0)||(dRltau_temp<dR_ltau_minltaupair)){
	dR_ltau_minltaupair = lep1LV.DeltaR(tau1LV);
	dEta_ltau_minltaupair = TMath::Abs(lep1LV.Eta()-tau1LV.Eta());
	dPhi_ltau_minltaupair = TMath::Abs(lep1LV.DeltaPhi(tau1LV));
	pT_ltau_minltaupair = (lep1LV+tau1LV).Pt();
	m_ltau_minltaupair = (lep1LV+tau1LV).M();
	dR_ll_minltaupair = lep2LV.DeltaR(lep3LV);
	dEta_ll_minltaupair = TMath::Abs(lep2LV.Eta()-lep3LV.Eta());
	dPhi_ll_minltaupair = TMath::Abs(lep2LV.DeltaPhi(lep3LV));
	pT_ll_minltaupair = (lep2LV+lep3LV).Pt();
	m_ll_minltaupair = (lep2LV+lep3LV).M();
      }
    }
    TLorentzVector p1_p1LV;
    TLorentzVector p1_p2LV;
    TLorentzVector p2_p1LV;
    TLorentzVector p2_p2LV;
    if(selHadTau->charge()*selLepton_lead->charge()<0){
      if(selHadTau->charge()*selLepton_sublead->charge()<0){
	if( (((tau1LV+lep2LV).M()<125)&&((lep1LV+lep3LV).M()<125)) || ( !( ((tau1LV+lep1LV).M()<125)&&((lep2LV+lep3LV).M()<125) ) ) ){
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep2LV;
	  p2_p1LV =lep1LV;
	  p2_p2LV =lep3LV;
	}
	else{
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep1LV;
	  p2_p1LV =lep2LV;
	  p2_p2LV =lep3LV;
	}
      }
      else{
	if( (((tau1LV+lep3LV).M()<125)&&((lep1LV+lep2LV).M()<125)) || ( !( ((tau1LV+lep1LV).M()<125)&&((lep2LV+lep3LV).M()<125) ) ) ){
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep3LV;
	  p2_p1LV =lep1LV;
	  p2_p2LV =lep2LV;
	}
	else{
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep1LV;
	  p2_p1LV =lep2LV;
	  p2_p2LV =lep3LV;
	}
      }
    }
    else{
      if( ((tau1LV+lep2LV).Pt()+(lep1LV+lep3LV).Pt())>((tau1LV+lep3LV).Pt()+(lep1LV+lep2LV).Pt())){
	if( (((tau1LV+lep2LV).M()<125)&&((lep1LV+lep3LV).M()<125)) || ( !( ((tau1LV+lep3LV).M()<125)&&((lep1LV+lep2LV).M()<125) ) ) ){
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep2LV;
	  p2_p1LV =lep1LV;
	  p2_p2LV =lep3LV;
	}
	else{
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep3LV;
	  p2_p1LV =lep1LV;
	  p2_p2LV =lep2LV;
	}
      }
      else{
	if( (((tau1LV+lep3LV).M()<125)&&((lep1LV+lep2LV).M()<125)) || ( !( ((tau1LV+lep2LV).M()<125)&&((lep1LV+lep3LV).M()<125) ) ) ){
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep3LV;
	  p2_p1LV =lep1LV;
	  p2_p2LV =lep2LV;
	}
	else{
	  p1_p1LV =tau1LV;
	  p1_p2LV =lep2LV;
	  p2_p1LV =lep1LV;
	  p2_p2LV =lep3LV;
	}
      }
    }
    double dR_smartpair1 = -1;
    double dEta_smartpair1 = -1;
    double dPhi_smartpair1 = -1;
    double m_smartpair1 = -1;
    double pT_smartpair1 = -1;
    double pTSum_smartpair1 = -1;
    double dR_smartpair2 = -1;
    double dEta_smartpair2 = -1;
    double dPhi_smartpair2 = -1;
    double m_smartpair2 = -1;
    double pT_smartpair2 = -1;
    double pTSum_smartpair2 = -1;
    double pTDiff_smartpair1 = -1;
    double pTDiff_smartpair2 = -1;

    double dR_smartpair_ltau = -1;
    double dEta_smartpair_ltau = -1;
    double dPhi_smartpair_ltau = -1;
    double m_smartpair_ltau = -1;
    double pT_smartpair_ltau = -1;
    double pTSum_smartpair_ltau = -1;
    double dR_smartpair_ll = -1;
    double dEta_smartpair_ll = -1;
    double dPhi_smartpair_ll = -1;
    double m_smartpair_ll = -1;
    double pT_smartpair_ll = -1;
    double pTSum_smartpair_ll = -1;
    double pTDiff_smartpair_ltau = -1;
    double pTDiff_smartpair_ll = -1;

    dR_smartpair_ltau = p1_p1LV.DeltaR(p1_p2LV);
    dEta_smartpair_ltau = TMath::Abs(p1_p1LV.Eta()-p1_p2LV.Eta());
    dPhi_smartpair_ltau = TMath::Abs(p1_p1LV.DeltaPhi(p1_p2LV));
    m_smartpair_ltau = (p1_p1LV+p1_p2LV).M();
    pT_smartpair_ltau =(p1_p1LV+p1_p2LV).Pt();
    pTSum_smartpair_ltau = p1_p1LV.Pt()+p1_p2LV.Pt();
    pTDiff_smartpair_ltau = TMath::Abs(p1_p1LV.Pt()-p1_p2LV.Pt());
    dR_smartpair_ll = p2_p1LV.DeltaR(p2_p2LV);
    dEta_smartpair_ll = TMath::Abs(p2_p1LV.Eta()-p2_p2LV.Eta());
    dPhi_smartpair_ll = TMath::Abs(p2_p1LV.DeltaPhi(p2_p2LV));
    m_smartpair_ll = (p2_p1LV+p2_p2LV).M();
    pT_smartpair_ll =(p2_p1LV+p2_p2LV).Pt();
    pTSum_smartpair_ll = p2_p1LV.Pt()+p2_p2LV.Pt();
    pTDiff_smartpair_ll = TMath::Abs(p2_p1LV.Pt()-p2_p2LV.Pt());




    if((p1_p1LV+p1_p2LV).Pt()>(p2_p1LV+p2_p2LV).Pt()){
      dR_smartpair1 = p1_p1LV.DeltaR(p1_p2LV);
      dEta_smartpair1 = TMath::Abs(p1_p1LV.Eta()-p1_p2LV.Eta());
      dPhi_smartpair1 = TMath::Abs(p1_p1LV.DeltaPhi(p1_p2LV));
      m_smartpair1 = (p1_p1LV+p1_p2LV).M();
      pT_smartpair1 =(p1_p1LV+p1_p2LV).Pt();
      pTSum_smartpair1 = p1_p1LV.Pt()+p1_p2LV.Pt();
      pTDiff_smartpair1 = TMath::Abs(p1_p1LV.Pt()-p1_p2LV.Pt());
      dR_smartpair2 = p2_p1LV.DeltaR(p2_p2LV);
      dEta_smartpair2 = TMath::Abs(p2_p1LV.Eta()-p2_p2LV.Eta());
      dPhi_smartpair2 = TMath::Abs(p2_p1LV.DeltaPhi(p2_p2LV));
      m_smartpair2 = (p2_p1LV+p2_p2LV).M();
      pT_smartpair2 =(p2_p1LV+p2_p2LV).Pt();
      pTSum_smartpair2 = p2_p1LV.Pt()+p2_p2LV.Pt();
      pTDiff_smartpair2 = TMath::Abs(p2_p1LV.Pt()-p2_p2LV.Pt());
    }
    else{
      dR_smartpair2 = p1_p1LV.DeltaR(p1_p2LV);
      dEta_smartpair2 = TMath::Abs(p1_p1LV.Eta()-p1_p2LV.Eta());
      dPhi_smartpair2 = TMath::Abs(p1_p1LV.DeltaPhi(p1_p2LV));
      m_smartpair2 = (p1_p1LV+p1_p2LV).M();
      pT_smartpair2 =(p1_p1LV+p1_p2LV).Pt();
      pTSum_smartpair2 = p1_p1LV.Pt()+p1_p2LV.Pt();
      pTDiff_smartpair2 = TMath::Abs(p1_p1LV.Pt()-p1_p2LV.Pt());
      dR_smartpair1 = p2_p1LV.DeltaR(p2_p2LV);
      dEta_smartpair1 = TMath::Abs(p2_p1LV.Eta()-p2_p2LV.Eta());
      dPhi_smartpair1 = TMath::Abs(p2_p1LV.DeltaPhi(p2_p2LV));
      m_smartpair1 = (p2_p1LV+p2_p2LV).M();
      pT_smartpair1 =(p2_p1LV+p2_p2LV).Pt();
      pTSum_smartpair1 = p2_p1LV.Pt()+p2_p2LV.Pt();
      pTDiff_smartpair1 = TMath::Abs(p2_p1LV.Pt()-p2_p2LV.Pt());
    }

    double mlll = (selLepton_lead->p4()+selLepton_sublead->p4()+selLepton_third->p4()).mass();
    double mAll = (selLepton_lead->p4()+selLepton_sublead->p4()+selLepton_third->p4()+ selHadTau->p4()).mass();
    double pT4l = (selLepton_lead->p4()+selLepton_sublead->p4()+selLepton_third->p4()+ selHadTau->p4()).pt(); 
    // tau pt debugging
    double m_OS_etau_closestToZ = -1;
    double m_etau_closestToZ = -1;
    int trigger_eTauZVezto = -1;
    int triggerBadTauVeto= -1;
    for(unsigned int i=0;i<selElectrons.size();i++){
      double m_Z_temp = (selElectrons[i]->p4()+selHadTau->p4()).mass();
      if( (m_etau_closestToZ ==-1) || (TMath::Abs(m_etau_closestToZ-91.2)>TMath::Abs(m_Z_temp-91.2)))
	{
	  m_etau_closestToZ = m_Z_temp;
	}
      if( ( (m_OS_etau_closestToZ ==-1) || (TMath::Abs(m_OS_etau_closestToZ-91.2)>TMath::Abs(m_Z_temp-91.2))) && (selElectrons[i]->charge()!=selHadTau->charge()) )
	{
	  m_OS_etau_closestToZ = m_Z_temp;
	}
    }
    if (TMath::Abs(m_OS_etau_closestToZ-91.2)<10){
      trigger_eTauZVezto=1;
    }
    else{
      trigger_eTauZVezto=0;
    }
    triggerBadTauVeto = triggerECalCrackVeto*trigger_eTauZVezto;
    double tau_antiElectron_matched = -1;
    double tau_antiElectron_unmatched = -1;
    if(TMath::Abs(getHadTau_genPdgId(selHadTau))==11){
      //tau_antiElectron_matched=selHadTau->antiElectron();
      tau_antiElectron_matched=selHadTau->id_mva(TauID::DeepTau2017v2VSe);
    }
    else{
      tau_antiElectron_unmatched=selHadTau->id_mva(TauID::DeepTau2017v2VSe);
      //tau_antiElectron_unmatched=selHadTau->antiElectron();
    }
    
    double m_l1tau = (selLepton_lead->p4()+selHadTau->p4()).mass();
    double m_l2tau = (selLepton_sublead->p4()+selHadTau->p4()).mass();
    double m_l3tau = (selLepton_third->p4()+selHadTau->p4()).mass();
    double m_ltau_closestToZ = m_l1tau;
    double m_OS_ltau_closestToZ = -1;
    if(selLepton_lead->charge()!=selHadTau->charge()) m_OS_ltau_closestToZ = m_l1tau;
    if(TMath::Abs(m_l2tau-91.2)<TMath::Abs(m_ltau_closestToZ-91.2)) m_ltau_closestToZ = m_l2tau; 
    if(TMath::Abs(m_l3tau-91.2)<TMath::Abs(m_ltau_closestToZ-91.2)) m_ltau_closestToZ = m_l3tau; 
    if((selLepton_sublead->charge()!=selHadTau->charge())&&((m_OS_ltau_closestToZ==-1)||(TMath::Abs(m_l2tau-91.2)<TMath::Abs(m_OS_ltau_closestToZ-91.2)))) m_OS_ltau_closestToZ = m_l2tau; 
    if((selLepton_third->charge()!=selHadTau->charge())&&((m_OS_ltau_closestToZ==-1)||(TMath::Abs(m_l3tau-91.2)<TMath::Abs(m_OS_ltau_closestToZ-91.2)))) m_OS_ltau_closestToZ = m_l3tau; 

    //BDT stuff
      BDTInputs_SUM["gen_mHH"]          =       250.; // setting a Dummy value which will be reset depending on mass hypothesis
      BDTInputs_SUM["mT_nonZlepMET"]          = mT_nonZlepMET;
      BDTInputs_SUM["mT_SSlephigh"]          = mT_SSlephigh;
      BDTInputs_SUM["mT_SSleplow"]          = mT_SSleplow;
      BDTInputs_SUM["mT_SSlepdR"]          = mT_SSlepdR;
      BDTInputs_SUM["met_LD"]          = met_LD;
      BDTInputs_SUM["HT"]          = HT;
      BDTInputs_SUM["diHiggsVisMass"]          = dihiggsVisMass_sel;
      BDTInputs_SUM["diHiggsMass"]          = dihiggsMass;
      BDTInputs_SUM["dR_ltau_minltaupair"]          = dR_ltau_minltaupair;
      BDTInputs_SUM["dEta_ltau_minltaupair"]          = dEta_ltau_minltaupair;
      BDTInputs_SUM["pT_ltau_minltaupair"]          = pT_ltau_minltaupair;
      BDTInputs_SUM["m_ltau_minltaupair"]          =m_ltau_minltaupair;
      BDTInputs_SUM["dR_ll_minltaupair"]          = dR_ll_minltaupair;
      BDTInputs_SUM["dEta_ll_minltaupair"]          = dEta_ll_minltaupair;
      BDTInputs_SUM["pT_ll_minltaupair"]          = pT_ll_minltaupair;
      BDTInputs_SUM["m_ll_minltaupair"]          = m_ll_minltaupair;
      BDTInputs_SUM["dR_ltau_minllpair"]          = dR_ltau_minllpair;
      BDTInputs_SUM["dEta_ltau_minllpair"]          = dEta_ltau_minllpair;
      BDTInputs_SUM["pT_ltau_minllpair"]          = pT_ltau_minllpair;
      BDTInputs_SUM["m_ltau_minllpair"]          = m_ltau_minllpair;
      BDTInputs_SUM["dR_ll_minllpair"]          = dR_ll_minllpair;
      BDTInputs_SUM["dEta_ll_minllpair"]          = dEta_ll_minllpair; 
      BDTInputs_SUM["pT_ll_minllpair"]          = pT_ll_minllpair;
      BDTInputs_SUM["m_ll_minllpair"]          = m_ll_minllpair;
      BDTInputs_SUM["mllOS_closestToZ"]          = mllOS_closestToZ;
      BDTInputs_SUM["SVFit_h1_visMass"]          = SVFit_h1_visMass;
      BDTInputs_SUM["SVFit_h2_visMass"]          = SVFit_h2_visMass;
      BDTInputs_SUM["SVFit_h1_pT"]          = SVFit_h1_pT;
      BDTInputs_SUM["SVFit_h2_pT"]          = SVFit_h2_pT;
      BDTInputs_SUM["SVFit_hh_deltaR"]          =SVFit_hh_deltaR;
      BDTInputs_SUM["SVFit_hh_deltaEta"]          = SVFit_hh_deltaEta;
      BDTInputs_SUM["SVFit_hh_pT"]          = SVFit_hh_pT;
      BDTInputs_SUM["nSFOS"]          = nSFOS;
      BDTInputs_SUM["dR_smartpair1"]          = dR_smartpair1;
      BDTInputs_SUM["dEta_smartpair1"]          = dEta_smartpair1;
      BDTInputs_SUM["m_smartpair1"]          = m_smartpair1;
      BDTInputs_SUM["pT_smartpair1"]          = pT_smartpair1;
      BDTInputs_SUM["pTSum_smartpair1"]          = pTSum_smartpair1;
      BDTInputs_SUM["dR_smartpair2"]          = dR_smartpair2;
      BDTInputs_SUM["dEta_smartpair2"]          = dEta_smartpair2;
      BDTInputs_SUM["m_smartpair2"]          = m_smartpair2;
      BDTInputs_SUM["pT_smartpair2"]          = pT_smartpair2;
      BDTInputs_SUM["pTSum_smartpair2"]          = pTSum_smartpair2;
      BDTInputs_SUM["mZ_tau"]          = mZ_tau;
      BDTInputs_SUM["nElectron"]          = selElectrons.size();

    if ( isDEBUG ) {
      std::cout << "Input variables ";
      for (auto elem : BDTInputs_SUM ) std::cout << elem.first << " " << elem.second << "\n";
      std::cout << std::endl;
    }


      BDTInputs_nonRes_SUM["pTSum_smartpair_ll"]          = pTSum_smartpair_ll;
      BDTInputs_nonRes_SUM["m_smartpair_ll"]          = m_smartpair_ll;
      BDTInputs_nonRes_SUM["diHiggsVisMass"]          = dihiggsVisMass_sel;
      BDTInputs_nonRes_SUM["met_LD"]          = met_LD;
      BDTInputs_nonRes_SUM["dR_smartpair_ltau"]          = dR_smartpair_ltau;
      BDTInputs_nonRes_SUM["mllOS_closestToZ"]          = mllOS_closestToZ;
      BDTInputs_nonRes_SUM["pTDiff_smartpair_ll"]          = pTDiff_smartpair_ll;   
      BDTInputs_nonRes_SUM["HT"]          = HT;
      BDTInputs_nonRes_SUM["mT_SSlephigh"]          = mT_SSlephigh;
      BDTInputs_nonRes_SUM["m_smartpair_ltau"]          = m_smartpair_ltau;
      BDTInputs_nonRes_SUM["pTSum_smartpair_ltau"]          = pTSum_smartpair_ltau;
      BDTInputs_nonRes_SUM["dR_smartpair_ll"]          = dR_smartpair_ll;
      BDTInputs_nonRes_SUM["nSFOS"]          = nSFOS;
      BDTInputs_nonRes_SUM["diHiggsMass"]          = dihiggsMass;
      BDTInputs_nonRes_SUM["nElectron"]          = selElectrons.size();
      BDTInputs_nonRes_SUM["pTDiff_smartpair_ltau"]          = pTDiff_smartpair_ltau;
      BDTInputs_nonRes_SUM["mT_SSleplow"]          = mT_SSleplow;
      BDTInputs_nonRes_SUM["mZ_tau"]          = mZ_tau;
      BDTInputs_nonRes_SUM["nodeX"]          = 0.0; //dummy vallue

    if ( isDEBUG ) {
      std::cout << "Input variables ";
      for (auto elem : BDTInputs_nonRes_SUM ) std::cout << elem.first << " " << elem.second << "\n";
      std::cout << std::endl;
    }


    std::map<std::string, double> BDTOutput_SUM_Map;
    std::map<std::string, double> BDTOutput_nonRes_SUM_Map;

    for(unsigned int i=0; i<gen_mHH.size(); i++){ // Loop over signal masses
      BDTInputs_SUM["gen_mHH"] = gen_mHH[i];
      unsigned int mass_int = (int)gen_mHH[i]; // Conversion from double to unsigned int
      std::string key = "";
      ostringstream temp;
      temp << mass_int;
      key = temp.str(); // Conversion from unsigned int to string
      std::string key_final = "BDTOutput_" + key;
      //BDTOutput_SUM_Map.insert( std::make_pair(key_final, (*BDT_SUM)(BDTInputs_SUM, eventInfo.event)) );
      BDTOutput_SUM_Map.insert( std::make_pair(key_final, 1.) );
    }
    for(unsigned int i=0; i<BMS.size(); i++){ // Loop over different nodes
      BDTInputs_nonRes_SUM["nodeX"] = i;
      std::string key_final = "BDTOutput_nonRes_" + BMS[i];
      //BDTOutput_nonRes_SUM_Map.insert( std::make_pair(key_final, (*BDT_nonRes_SUM)(BDTInputs_nonRes_SUM, eventInfo.event)) );
      BDTOutput_nonRes_SUM_Map.insert( std::make_pair(key_final, 1.) );
    }
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
          selHistManager->muons_->fillHistograms(selMuons, evtWeight);
          selHistManager->hadTaus_->fillHistograms(selHadTaus, evtWeight);
          selHistManager->jets_->fillHistograms(selJets, evtWeight);
          selHistManager->BJets_loose_->fillHistograms(selBJets_loose, evtWeight);
          selHistManager->BJets_medium_->fillHistograms(selBJets_medium, evtWeight);
          selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
        }
	for(const auto & kv: reWeightMapHH)
        {
	  if(selectBDT) continue;
          selHistManager->evt_[kv.first]->fillHistograms(
            selElectrons.size(),
            selMuons.size(),
            selHadTaus.size(),
            selJets.size(),
            numSelJetsPtGt40,
            selBJets_loose.size(),
            selBJets_medium.size(),
            dihiggsVisMass_sel,
            dihiggsMass,
            HT,
            STMET,
            kv.second,
	    mht_p4.pt(),
	    met.pt(),
	    met_LD,
	    mT_nonZlepMET,
	    mT_SSlephigh,
	    mT_SSleplow,
	    mT_SSlepdR,
	    mllOS_closestToZ,
	    SVFit_h1_visMass, 
	    SVFit_h2_visMass,
	    SVFit_h1_pT, 
	    SVFit_h2_pT, 
	    SVFit_hh_deltaPhi, 
	    SVFit_hh_deltaEta,
	    SVFit_hh_deltaR,
	    SVFit_hh_pT,
	    SVFit_hh_cosTheta,
	    m_ltau_minltaupair,
	    pT_ltau_minltaupair,
	    dR_ltau_minltaupair,
	    dEta_ltau_minltaupair,
	    dPhi_ltau_minltaupair,
	    m_ll_minltaupair,
	    pT_ll_minltaupair,
	    dR_ll_minltaupair,
	    dEta_ll_minltaupair,
	    dPhi_ll_minltaupair,
	    m_ltau_minllpair,
	    pT_ltau_minllpair,
	    dR_ltau_minllpair,
	    dEta_ltau_minllpair,
	    dPhi_ltau_minllpair,
	    m_ll_minllpair,
	    pT_ll_minllpair,
	    dR_ll_minllpair,
	    dEta_ll_minllpair,
	    dPhi_ll_minllpair,
	    mlll,
	    mAll,
	    dr_los1,
	    dr_los2,
	    m_OS_etau_closestToZ,
	    m_etau_closestToZ,
	    trigger_eTauZVezto,
	    triggerECalCrackVeto,
	    triggerBadTauVeto,
	    m_ltau_closestToZ,
	    m_OS_ltau_closestToZ,
	    tau_antiElectron_matched,
	    tau_antiElectron_unmatched,
	    dR_smartpair1,
	    dR_smartpair2,
	    dR_smartpair_ll,
	    dR_smartpair_ltau,
	    dPhi_smartpair1,
	    dPhi_smartpair2,
	    dPhi_smartpair_ll,
	    dPhi_smartpair_ltau,
	    dEta_smartpair1,
	    dEta_smartpair2,
	    dEta_smartpair_ll,
	    dEta_smartpair_ltau,
	    pT_smartpair1,
	    pT_smartpair2,
	    pT_smartpair_ll,
	    pT_smartpair_ltau,
	    pTSum_smartpair1,
	    pTSum_smartpair2,
	    pTSum_smartpair_ll,
	    pTSum_smartpair_ltau,
	    pTDiff_smartpair1,
	    pTDiff_smartpair2,
	    pTDiff_smartpair_ll,
	    pTDiff_smartpair_ltau,
	    nSFOS,
	    mZ_tau,
	    dPhi_nonZlMET,
	    mindPhiLepMET,
	    pT4l,
	    BDTOutput_SUM_Map,
	    BDTOutput_nonRes_SUM_Map,
	    eventInfo.event
					 );
          selHistManager->svFit4tau_woMassConstraint_[kv.first]->fillHistograms(svFit4tauResults_woMassConstraint, kv.second);
          selHistManager->svFit4tau_wMassConstraint_[kv.first]->fillHistograms(svFit4tauResults_wMassConstraint, kv.second);

          if(isSignal)
          {
            const std::string decayModeStr = eventInfo.getDiHiggsDecayModeString();
            if((! decayModeStr.empty()) && !selectBDT)
            {
              selHistManager->evt_in_decayModes_[kv.first][decayModeStr]->fillHistograms(
                selElectrons.size(),
                selMuons.size(),
                selHadTaus.size(),
                selJets.size(),
                numSelJetsPtGt40,
                selBJets_loose.size(),
                selBJets_medium.size(),
                dihiggsVisMass_sel,
                dihiggsMass,
                HT,
                STMET,
                kv.second,
		mht_p4.pt(),
		met.pt(),
		met_LD,
		mT_nonZlepMET,
		mT_SSlephigh,
		mT_SSleplow,
		mT_SSlepdR,
		mllOS_closestToZ,
		SVFit_h1_visMass, 
		SVFit_h2_visMass,
		SVFit_h1_pT, 
		SVFit_h2_pT, 
		SVFit_hh_deltaPhi, 
		SVFit_hh_deltaEta,
		SVFit_hh_deltaR,
		SVFit_hh_pT,
		SVFit_hh_cosTheta,
		m_ltau_minltaupair,
		pT_ltau_minltaupair,
		dR_ltau_minltaupair,
		dEta_ltau_minltaupair,
		dPhi_ltau_minltaupair,
		m_ll_minltaupair,
		pT_ll_minltaupair,
		dR_ll_minltaupair,
		dEta_ll_minltaupair,
		dPhi_ll_minltaupair,
		m_ltau_minllpair,
		pT_ltau_minllpair,
		dR_ltau_minllpair,
		dEta_ltau_minllpair,
		dPhi_ltau_minllpair,
		m_ll_minllpair,
		pT_ll_minllpair,
		dR_ll_minllpair,
		dEta_ll_minllpair,
		dPhi_ll_minllpair,
	        mlll,
	        mAll,
		dr_los1,
	        dr_los2,
		m_OS_etau_closestToZ,
		m_etau_closestToZ,
		trigger_eTauZVezto,
		triggerECalCrackVeto,
		triggerBadTauVeto,
		m_ltau_closestToZ,
		m_OS_ltau_closestToZ,
		tau_antiElectron_matched,
		tau_antiElectron_unmatched,
		dR_smartpair1,
		dR_smartpair2,
		dR_smartpair_ll,
		dR_smartpair_ltau,
		dPhi_smartpair1,
		dPhi_smartpair2,
		dPhi_smartpair_ll,
		dPhi_smartpair_ltau,
		dEta_smartpair1,
		dEta_smartpair2,
		dEta_smartpair_ll,
		dEta_smartpair_ltau,
		pT_smartpair1,
		pT_smartpair2,
		pT_smartpair_ll,
		pT_smartpair_ltau,
		pTSum_smartpair1,
		pTSum_smartpair2,
		pTSum_smartpair_ll,
		pTSum_smartpair_ltau,
		pTDiff_smartpair1,
		pTDiff_smartpair2,
		pTDiff_smartpair_ll,
		pTDiff_smartpair_ltau,
		nSFOS,
		mZ_tau,
		dPhi_nonZlMET,
		mindPhiLepMET,
		pT4l,
		BDTOutput_SUM_Map,
		BDTOutput_nonRes_SUM_Map,
		eventInfo.event
              );
              selHistManager->svFit4tau_woMassConstraint_in_decayModes_[kv.first][decayModeStr]->fillHistograms(svFit4tauResults_woMassConstraint, kv.second);
              selHistManager->svFit4tau_wMassConstraint_in_decayModes_[kv.first][decayModeStr]->fillHistograms(svFit4tauResults_wMassConstraint, kv.second);
            }
          }
        }

        if(! skipFilling)
        {
          selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
          selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
          selHistManager->weights_->fillHistograms("lheWeight", evtWeightRecorder.get_lheScaleWeight(central_or_shift));
          selHistManager->weights_->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
          selHistManager->weights_->fillHistograms("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift));
          selHistManager->weights_->fillHistograms("btagWeight", evtWeightRecorder.get_btag(central_or_shift));
          selHistManager->weights_->fillHistograms("leptonEff", evtWeightRecorder.get_leptonSF());
          selHistManager->weights_->fillHistograms("hadTauEff", evtWeightRecorder.get_tauSF(central_or_shift));
          selHistManager->weights_->fillHistograms("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift));
          selHistManager->weights_->fillHistograms("fakeRate", evtWeightRecorder.get_FR(central_or_shift));
        }
      }
      if (isDEBUG)  std::cout << "FR_WEIGHT "<< evtWeightRecorder.get_FR(central_or_shift) << std::endl;
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
    }

    if ( selEventsFile ) {
      (*selEventsFile) << eventInfo.run << ':' << eventInfo.lumi << ':' << eventInfo.event << '\n';
    }
    //compute BDT variables:
    if(bdt_filler){
      // double genHiggs1_pt = -1;
      // double genHiggs1_eta = -1;
      // double genHiggs1_phi = -1;
      // double genHiggs2_pt = -1;
      // double genHiggs2_eta = -1;
      // double genHiggs2_phi = -1;
      // double genDiHiggs_pt = -1;
      // double genDiHiggs_eta = -1;
      // double genDiHiggs_phi = -1;
      // double genDiHiggs_M = -1;
      // double genDiHiggs_dR = -1;
      // double genDiHiggs_dEta = -1;
      // double genDiHiggs_dPhi = -1;
      // double genDiHiggs_cosTheta = -1;
      // if (isSignal && (genHiggs.size()>1)){
      // 	genHiggs1_pt = genHiggs[0].pt();
      // 	genHiggs1_eta = genHiggs[0].eta();
      // 	genHiggs1_phi = genHiggs[0].phi();
      // 	genHiggs2_pt = genHiggs[1].pt();
      // 	genHiggs2_eta = genHiggs[1].eta();
      // 	genHiggs2_phi = genHiggs[1].phi();
      // 	genDiHiggs_pt = (genHiggs[0].p4()+genHiggs[1].p4()).pt();
      // 	genDiHiggs_eta = (genHiggs[0].p4()+genHiggs[1].p4()).eta();
      // 	genDiHiggs_phi = (genHiggs[0].p4()+genHiggs[1].p4()).phi();
      // 	genDiHiggs_M = (genHiggs[0].p4()+genHiggs[1].p4()).mass();
      // 	TLorentzVector h1(1,0,0,1);
      // 	h1.SetPtEtaPhiM(genHiggs[0].pt(),genHiggs[0].eta(),genHiggs[0].phi(),genHiggs[0].mass());
      // 	TLorentzVector h2(1,0,0,1);
      // 	h2.SetPtEtaPhiM(genHiggs[1].pt(),genHiggs[1].eta(),genHiggs[1].phi(),genHiggs[1].mass());
      // 	genDiHiggs_dR = h1.DeltaR(h2);
      // 	genDiHiggs_dEta = TMath::Abs(h1.Eta()-h2.Eta());
      // 	genDiHiggs_dPhi = h1.DeltaPhi(h2);
      // 	TVector3 boostvector = (h1+h2).BoostVector();
      // 	h1.Boost(-1*boostvector);
      // 	h2.Boost(-1*boostvector);
      // 	TLorentzVector beamaxis1 = TLorentzVector(0,0,1,1);
      // 	TLorentzVector beamaxis2 = TLorentzVector(0,0,-1,1);
      // 	beamaxis1.Boost(-1*boostvector);
      // 	beamaxis2.Boost(-1*boostvector);
      // 	TVector3 zaxisCS = (beamaxis1.Vect().Unit() - beamaxis2.Vect().Unit()).Unit();
      // 	genDiHiggs_cosTheta = TMath::Abs(h1.Vect().Unit().Dot(zaxisCS));
      // }
      int lep1_isElectron = -1;
      if (std::abs(selLepton_lead_type) == 11) lep1_isElectron = 1;
      else if (std::abs(selLepton_lead_type) == 13) lep1_isElectron = 0;
      int lep2_isElectron = -1;
      if (std::abs(selLepton_sublead_type) == 11) lep2_isElectron = 1;
      else if (std::abs(selLepton_sublead_type) == 13) lep2_isElectron = 0;
      int lep3_isElectron = -1;
      if (std::abs(selLepton_third_type) == 11) lep3_isElectron = 1;
      else if (std::abs(selLepton_third_type) == 13) lep3_isElectron = 0;

      std::cout << "mhh = " << eventInfo.gen_mHH          << " : "
	"cost "             << eventInfo.gen_cosThetaStar << '\n';
      for(unsigned int i =0; i< genHiggs.size();i++){
	std::cout << "higgs " << i << " mass: "<<genHiggs[i].mass() << std::endl;
      }
      int numSameFlavor_OS_3l = 0;
      //double mSFOS2l = 0.;
      for (int iLepton1 = 0; iLepton1 < 3; iLepton1++) {
	for (int iLepton2 = iLepton1+1; iLepton2 < 3; iLepton2++) {
	  if ( selLeptons[iLepton1]->pdgId() == - selLeptons[iLepton2]->pdgId() ) { // pair of same flavor leptons of opposite charge
	    numSameFlavor_OS_3l++;
	    // mSFOS2l = (selLeptons[iLepton1]->p4() + selLeptons[iLepton2]->p4()).mass();
	  }
	}
      }
      const double deltaEta_lep1_lep2 = (selLepton_lead->p4() - selLepton_sublead->p4()).eta();
      const double deltaEta_lep1_tau1 = (selLepton_lead->p4() - selHadTau->p4()).eta();
      const double deltaEta_lep2_tau1 = (selLepton_sublead->p4() - selHadTau->p4()).eta();
      const double deltaEta_lep1_lep3 = (selLepton_lead->p4() - selLepton_third->p4()).eta();
      const double deltaEta_lep2_lep3 = (selLepton_sublead->p4() - selLepton_third->p4()).eta();
      const double deltaEta_lep3_tau1 = (selLepton_third->p4() - selHadTau->p4()).eta();
      const double deltaPhi_lep1_lep2 = lep1LV.DeltaPhi(lep2LV);
      const double deltaPhi_lep1_tau1 = lep1LV.DeltaPhi(tau1LV);
      const double deltaPhi_lep2_tau1 = lep2LV.DeltaPhi(tau1LV);
      const double deltaPhi_lep1_lep3 = lep1LV.DeltaPhi(lep3LV);
      const double deltaPhi_lep2_lep3 = lep2LV.DeltaPhi(lep3LV);
      const double deltaPhi_lep3_tau1 = lep3LV.DeltaPhi(tau1LV);
      const double m_lep1_tau1 = (selLepton_lead->p4() + selHadTau->p4()).mass();
      const double m_lep2_tau1 = (selLepton_sublead->p4() + selHadTau->p4()).mass();
      const double m_lep3_tau1 = (selLepton_third->p4() + selHadTau->p4()).mass();
      const double dr_lep1_tau1 = deltaR(selLepton_lead->p4(),    selHadTau->p4());
      const double dr_lep2_tau1 = deltaR(selLepton_sublead->p4(), selHadTau->p4());
      const double dr_lep3_tau1 = deltaR(selLepton_third->p4(), selHadTau->p4());
      const double dr_lep1_lep2 = deltaR(selLepton_lead->p4(), selLepton_sublead->p4());
      const double dr_lep1_lep3 = deltaR(selLepton_lead->p4(), selLepton_third->p4());
      const double dr_lep2_lep3 = deltaR(selLepton_sublead->p4(), selLepton_third->p4());

      double lep1_genLepPt = ( selLepton_lead->genLepton()    ) ? selLepton_lead->genLepton()->pt()    : 0.;
      double lep2_genLepPt = ( selLepton_sublead->genLepton() ) ? selLepton_sublead->genLepton()->pt() : 0.;
      double lep3_genLepPt = ( selLepton_third->genLepton()   ) ? selLepton_third->genLepton()->pt()   : 0.;
      double hadTau_genPt = 0.;
      if(selHadTau->genHadTau()) hadTau_genPt =  selHadTau->genHadTau()->pt();
      else if ( selHadTau->genLepton()) hadTau_genPt =  selHadTau->genLepton()->pt();
      
      //FR weights for bdt ntuple
      double prob_fake_lepton_lead = evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
      double prob_fake_lepton_sublead = evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);
      double prob_fake_lepton_third = evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main);
      double prob_fake_tau_lead = evtWeightRecorder.get_jetToTau_FR_lead(central_or_shift_main);
      const double lep1_conePt = comp_lep_conePt(*selLepton_lead);
      const double lep2_conePt = comp_lep_conePt(*selLepton_sublead);
      const double lep3_conePt = comp_lep_conePt(*selLepton_third);
      // const double mindr_lep1_jet = comp_mindr_jet(*selLepton_lead, selJetsAK4);
      // const double mindr_lep2_jet = comp_mindr_jet(*selLepton_sublead, selJetsAK4);
      // const double mindr_lep3_jet = comp_mindr_jet(*selLepton_third, selJetsAK4);
      // const double avg_dr_jet = comp_avg_dr_jet(selJetsAK4);
      double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
      double lep1_frWeight = lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead;
      double lep2_frWeight = lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead;
      double lep3_frWeight = lep3_genLepPt > 0 ? 1.0 : prob_fake_lepton_third;
      double hadTau_frWeight = hadTau_genPt > 0 ? 1.0 : prob_fake_tau_lead;
      evtWeight_BDT *= lep1_frWeight*lep2_frWeight*lep3_frWeight*hadTau_frWeight;
      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
        ("lep1_pt",             selLepton_lead -> pt())
	("lep1_conePt",         lep1_conePt)
	("lep1_eta",            selLepton_lead -> eta())
	("lep1_tth_mva",        selLepton_lead -> mvaRawTTH())
        ("mT_lep1",             comp_MT_met(selLepton_lead, met.pt(), met.phi()))
	("lep1_phi",            selLepton_lead -> phi())
	("lep2_pt",             selLepton_sublead -> pt())
	("lep2_conePt",         lep2_conePt)
	("lep2_eta",            selLepton_sublead -> eta())
	("lep2_tth_mva",        selLepton_sublead -> mvaRawTTH())
        ("mT_lep2",             comp_MT_met(selLepton_sublead, met.pt(), met.phi()))
	("lep2_phi",            selLepton_sublead -> phi())
	("lep3_pt",             selLepton_third -> pt())
	("lep3_conePt",         lep3_conePt)
	("lep3_eta",            selLepton_third -> eta())
	("lep3_tth_mva",        selLepton_third -> mvaRawTTH())
        ("mT_lep3",             comp_MT_met(selLepton_third, met.pt(), met.phi()))
	("lep3_phi",            selLepton_third -> phi())
	("lep1_frWeight",       lep1_frWeight)
	("lep2_frWeight",       lep2_frWeight)
	("lep3_frWeight",       lep3_frWeight)
	("hadTau_frWeight",       hadTau_frWeight)
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
	("nJet",                selJetsAK4.size())
	("met",                 met.pt())
	("mht",                 mht_p4.pt())
	("met_LD",              met_LD)
	("HT",                  HT)
	("STMET",               STMET)
	("diHiggsVisMass",      dihiggsVisMass_sel)
	("diHiggsMass",         dihiggsMass)
	("nElectron",           selElectrons.size())
	("nMuon",               selMuons.size())
	("nTaus",               selHadTaus.size())
	("deltaEta_lep1_lep2", deltaEta_lep1_lep2)
	("deltaEta_lep1_tau1", deltaEta_lep1_tau1)
	("deltaEta_lep2_tau1", deltaEta_lep2_tau1)
	("deltaEta_lep1_lep3", deltaEta_lep1_lep3)
	("deltaEta_lep2_lep3", deltaEta_lep2_lep3)
	("deltaEta_lep3_tau1", deltaEta_lep3_tau1)
	("deltaPhi_lep1_lep2", deltaPhi_lep1_lep2)
	("deltaPhi_lep1_tau1", deltaPhi_lep1_tau1)
	("deltaPhi_lep2_tau1", deltaPhi_lep2_tau1)
	("deltaPhi_lep1_lep3", deltaPhi_lep1_lep3)
	("deltaPhi_lep2_lep3", deltaPhi_lep2_lep3)
	("deltaPhi_lep3_tau1", deltaPhi_lep3_tau1)
	("tau1_pt",                  selHadTau->pt())
	("tau1_eta",                 selHadTau->eta())
	("tau1_phi",                 selHadTau->phi())
	("tau1_mva_dR03",                 selHadTau->id_mva(TauID::MVAoldDMdR032017v2))
	("tau1_mva_deepvsj",         selHadTau->id_mva(TauID::DeepTau2017v2VSjet))
	("dr_lep1_tau1",             dr_lep1_tau1)
	("dr_lep2_tau1",             dr_lep2_tau1)
	("dr_lep3_tau1",             dr_lep3_tau1)
	("dr_lep1_lep2",             dr_lep1_lep2)
	("dr_lep1_lep3",             dr_lep1_lep3)
	("dr_lep2_lep3",             dr_lep2_lep3)
	("m_lep1_tau1",              m_lep1_tau1)
	("m_lep2_tau1",              m_lep2_tau1)
	("m_lep3_tau1",              m_lep3_tau1)
	("mlll",                     mlll)
	("mAll",                     mAll)
	("dR_ltau_minllpair",          dR_ltau_minllpair)
	("dPhi_ltau_minllpair",        dPhi_ltau_minllpair)
	("dEta_ltau_minllpair",        dEta_ltau_minllpair)
	("pT_ltau_minllpair",          pT_ltau_minllpair)
	("m_ltau_minllpair",          m_ltau_minllpair)
	("dR_ll_minllpair",          dR_ll_minllpair)
	("dPhi_ll_minllpair",        dPhi_ll_minllpair)
	("dEta_ll_minllpair",        dEta_ll_minllpair)
	("pT_ll_minllpair",          pT_ll_minllpair)
	("m_ll_minllpair",          m_ll_minllpair)
	("dR_ltau_minltaupair",          dR_ltau_minltaupair)
	("dPhi_ltau_minltaupair",        dPhi_ltau_minltaupair)
	("dEta_ltau_minltaupair",        dEta_ltau_minltaupair)
	("pT_ltau_minltaupair",          pT_ltau_minltaupair)
	("m_ltau_minltaupair",          m_ltau_minltaupair)
	("dR_ll_minltaupair",          dR_ll_minltaupair)
	("dPhi_ll_minltaupair",        dPhi_ll_minltaupair)
	("dEta_ll_minltaupair",        dEta_ll_minltaupair)
	("pT_ll_minltaupair",          pT_ll_minltaupair)
	("m_ll_minltaupair",          m_ll_minltaupair)
	("mllOS_closestToZ",        mllOS_closestToZ)
	("SVFit_h1_visMass",        SVFit_h1_visMass)
	("SVFit_h2_visMass",        SVFit_h2_visMass)
	("SVFit_h1_pT",             SVFit_h1_pT) 
	("SVFit_h2_pT",             SVFit_h2_pT)
	("SVFit_hh_deltaPhi",       SVFit_hh_deltaPhi)
	("SVFit_hh_deltaR",         SVFit_hh_deltaR)
	("SVFit_hh_deltaEta",       SVFit_hh_deltaEta)
	("SVFit_hh_pT",             SVFit_hh_pT)
	("SVFit_hh_cosTheta",       SVFit_hh_cosTheta)
	("mT_nonZlepMET",           mT_nonZlepMET)
	("mT_SSlephigh",            mT_SSlephigh)
	("mT_SSleplow",             mT_SSleplow)
	("mT_SSlepdR",              mT_SSlepdR)
	// ("genHiggs1_pt",            genHiggs1_pt)
	// ("genHiggs1_eta",           genHiggs1_eta)
	// ("genHiggs1_phi",           genHiggs1_phi)
	// ("genHiggs2_pt",            genHiggs2_pt)
	// ("genHiggs2_eta",           genHiggs2_eta)
	// ("genHiggs2_phi",           genHiggs2_phi)
	// ("genDiHiggs_pt",           genDiHiggs_pt)
	// ("genDiHiggs_eta",          genDiHiggs_eta)
	// ("genDiHiggs_phi",          genDiHiggs_phi)
	// ("genDiHiggs_M",            genDiHiggs_M)
	// ("genDiHiggs_dR",           genDiHiggs_dR)
	// ("genDiHiggs_dEta",         genDiHiggs_dEta)
	// ("genDiHiggs_dPhi",         genDiHiggs_dPhi)
	// ("genDiHiggs_cosTheta",     genDiHiggs_cosTheta)
	("nSFOS",                   nSFOS)
	("dR_smartpair1",           dR_smartpair1)
	("dEta_smartpair1",         dEta_smartpair1)
	("dPhi_smartpair1",         dPhi_smartpair1)
	("m_smartpair1",            m_smartpair1)
	("pT_smartpair1",           pT_smartpair1)
	("pTSum_smartpair1",        pTSum_smartpair1)
	("dR_smartpair2",           dR_smartpair2)
	("dEta_smartpair2",         dEta_smartpair2)
	("dPhi_smartpair2",         dPhi_smartpair2)
	("m_smartpair2",            m_smartpair2)
	("pT_smartpair2",           pT_smartpair2)
	("pTSum_smartpair2",        pTSum_smartpair2)
	("dR_smartpair_ltau",           dR_smartpair_ltau)
	("dEta_smartpair_ltau",         dEta_smartpair_ltau)
	("dPhi_smartpair_ltau",         dPhi_smartpair_ltau)
	("m_smartpair_ltau",            m_smartpair_ltau)
	("pT_smartpair_ltau",           pT_smartpair_ltau)
	("pTSum_smartpair_ltau",        pTSum_smartpair_ltau)
	("dR_smartpair_ll",           dR_smartpair_ll)
	("dEta_smartpair_ll",         dEta_smartpair_ll)
	("dPhi_smartpair_ll",         dPhi_smartpair_ll)
	("m_smartpair_ll",            m_smartpair_ll)
	("pT_smartpair_ll",           pT_smartpair_ll)
	("pTSum_smartpair_ll",        pTSum_smartpair_ll)
	("mZ_tau",                  mZ_tau)
	("dPhi_nonZlMET",           dPhi_nonZlMET)
	( "mindPhiLepMET",          mindPhiLepMET)
	("pTDiff_smartpair1",        pTDiff_smartpair1)
	("pTDiff_smartpair2",        pTDiff_smartpair2)
	("pTDiff_smartpair_ltau",        pTDiff_smartpair_ltau)
	("pTDiff_smartpair_ll",        pTDiff_smartpair_ll)
	("SVFit_Z1_visMass",        SVFit_Z1_visMass)
	("SVFit_Z2_visMass",        SVFit_Z2_visMass)
	("lep1_isElectron",         lep1_isElectron)
	("lep2_isElectron",         lep2_isElectron)
	("lep3_isElectron",         lep3_isElectron)
	("lep1_charge",             selLepton_lead->charge())
	("lep2_charge",             selLepton_sublead->charge())
	("lep3_charge",             selLepton_third->charge())
	("pT4l",                    pT4l)
	(weightMapHH)
        .fill()
      ;
    }

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
    if(isDEBUG)
    {
      std::cout << evtWeightRecorder << '\n';
    }
  }

  std::cout << "max num. Entries = " << inputTree -> getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree -> getProcessedFileCount() << " file(s) (out of "
            << inputTree -> getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n\n"
            << "cut-flow table" << std::endl;

  std::cout << "cut-flow table" << std::endl;
  cutFlowTable.print(std::cout);
  std::cout << std::endl;

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    std::cout << "central_or_shift = " << central_or_shift << '\n';
    for(const leptonGenMatchEntry & leptonGenMatch_definition: leptonGenMatch_definitions)
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

  hltPaths_delete(triggers_1e);
  hltPaths_delete(triggers_2e);
  hltPaths_delete(triggers_1mu);
  hltPaths_delete(triggers_2mu);
  hltPaths_delete(triggers_1e1mu);

  delete inputTree;

  clock.Show("analyze_hh_3l_1tau");

  return EXIT_SUCCESS;
}
