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
#include <TROOT.h> // TROOT
#include "TVector3.h"

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
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
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelector.h" // RecoJetCollectionSelector
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorBtag.h" // RecoJetCollectionSelectorBtagLoose, RecoJetCollectionSelectorBtagMedium
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventSelector.h" // RunLumiEventSelector
#include "tthAnalysis/HiggsToTauTau/interface/MEtFilterSelector.h" // MEtFilterSelector
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
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
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_4lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h" // getWeight_4L
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
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLO.h" // HHWeightInterfaceLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceNLO.h" // HHWeightInterfaceNLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceCouplings.h" // HHWeightInterfaceCouplings
#include "tthAnalysis/HiggsToTauTau/interface/BM_list.h" // BMS
#include "tthAnalysis/HiggsToTauTau/interface/NtupleFillerBDT.h" // NtupleFillerBDT
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertex.h" // RecoVertex
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertexReader.h" // RecoVertexReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonFilter.h" // GenPhotonFilter
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventRejector.h" // RunLumiEventRejector

#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_4l.h" // EvtHistManager_hh_4l
#include "hhAnalysis/multilepton/interface/SVfit4tauHistManager_MarkovChain.h" // SVfit4tauHistManager_MarkovChain
#include "hhAnalysis/multilepton/interface/Data_to_MC_CorrectionInterface_hh_1l_3tau_trigger.h"
#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // getMeasuredTauLeptonType, getHadTauDecayMode
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h" // DatacardHistManager_hh

#include "TauAnalysis/ClassicSVfit4tau/interface/ClassicSVfit4tau.h" // ClassicSVfit4tau
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit4tau/interface/svFitHistogramAdapter4tau.h" // HistogramAdapterDiHiggs, HistogramAdapterHiggs

#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h"
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h"

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

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;

enum { kFR_disabled, kFR_4lepton };

const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied

/**
 * @brief Produce datacard and control plots for 4l category of HH "multilepton" (HH->WWWW,WWtt,tttt) analysis.
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

  std::cout << "<analyze_hh_4l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_4l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_4l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_4l");
  AnalysisConfig_hh analysisConfig("HH->multilepton", cfg_analyze);

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");
  bool isMC_ttH = analysisConfig.isMC_ttH();
  bool isMC_tH = analysisConfig.isMC_tH();
  bool isMC_EWK = analysisConfig.isMC_EWK();

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");
  bool isMCClosure_e = histogramDir.find("mcClosure_e") != std::string::npos;
  bool isMCClosure_m = histogramDir.find("mcClosure_m") != std::string::npos;
  std::cout << "isMCClosure: e = " << isMCClosure_e << ", mu = " << isMCClosure_m << std::endl;

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
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_4lepton(true);
  std::cout << "leptonGenMatch_definitions:" << std::endl;
  std::cout << leptonGenMatch_definitions;

  GenMatchInterface genMatchInterface(4, apply_leptonGenMatching, false);

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;

  const double lep_mva_cut_mu = cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e  = cfg_analyze.getParameter<double>("lep_mva_cut_e");
  const std::string lep_mva_wp = cfg_analyze.getParameter<std::string>("lep_mva_wp");

  enum { kOS, kSS };
  std::string leptonChargeSelection_string = cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS" ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS" ) leptonChargeSelection = kSS;
  else throw cms::Exception("analyze_hh_4l")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";
  TRandom3 rnd; // used to randomly kill one of three possible combination of measuredTauLeptons into pairs in case leptonChargeSelection is "SS" or "disabled",
                // to ensure that exactly two possible combination of measuredTauLeptons are considered, regardless of leptonChargeSelection

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
  std::string apply_genPhotonFilter_string = cfg_analyze.getParameter<std::string>("apply_genPhotonFilter");
  GenPhotonFilter genPhotonFilter(apply_genPhotonFilter_string);
  bool apply_genPhotonFilter = apply_genPhotonFilter_string != "disabled";
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
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("lep_mva_wp", lep_mva_wp);
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
  else if ( applyFakeRateWeights_string == "4lepton"  ) applyFakeRateWeights = kFR_4lepton;
  else throw cms::Exception("analyze_hh_4l")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_4lepton) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    cfg_leptonFakeRateWeight.addParameter<std::string>("era", era_string);
    cfg_leptonFakeRateWeight.addParameter<std::vector<std::string>>("central_or_shifts", central_or_shifts_local);
    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight);
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
  std::string branchName_genProxyPhotons = cfg_analyze.getParameter<std::string>("branchName_genProxyPhotons");
  std::string branchName_genFromHardProcess = cfg_analyze.getParameter<std::string>("branchName_genFromHardProcess");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");

  std::string branchName_muonGenMatch     = cfg_analyze.getParameter<std::string>("branchName_muonGenMatch");
  std::string branchName_electronGenMatch = cfg_analyze.getParameter<std::string>("branchName_electronGenMatch");
  std::string branchName_hadTauGenMatch   = cfg_analyze.getParameter<std::string>("branchName_hadTauGenMatch");
  std::string branchName_jetGenMatch      = cfg_analyze.getParameter<std::string>("branchName_jetGenMatch");

  const bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  const bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");
  const bool genMatchingByIndex = cfg_analyze.getParameter<bool>("genMatchingByIndex");

  const bool selectBDT = cfg_analyze.exists("selectBDT") ? cfg_analyze.getParameter<bool>("selectBDT") : false;
  const edm::ParameterSet mvaInfo_res = cfg_analyze.getParameter<edm::ParameterSet>("mvaInfo_res");
  std::vector<double> gen_mHH = analysisConfig.get_HH_resonant_mass_points();
  std::string BDTFileName_spin0_even  = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin0_even");
  std::string BDTFileName_spin0_odd   = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin0_odd");
  std::string fitFunctionFileName_spin0 = mvaInfo_res.getParameter<std::string>("fitFunctionFileName_spin0");
  std::vector<std::string> BDTInputVariables_spin0 = mvaInfo_res.getParameter<std::vector<std::string>>("inputVars_spin0");
  std::string BDTFileName_spin2_even  = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin2_even");
  std::string BDTFileName_spin2_odd   = mvaInfo_res.getParameter<std::string>("BDT_xml_FileName_spin2_odd");
  std::string fitFunctionFileName_spin2 = mvaInfo_res.getParameter<std::string>("fitFunctionFileName_spin2");
  std::vector<std::string> BDTInputVariables_spin2 = mvaInfo_res.getParameter<std::vector<std::string>>("inputVars_spin2");
  const edm::ParameterSet mvaInfo_nonRes = cfg_analyze.getParameter<edm::ParameterSet>("mvaInfo_nonRes");
  std::vector<std::string> nonRes_BMs = cfg_analyze.getParameter<std::vector<std::string>>("nonRes_BMs");
  std::string BDTFileName_nonRes_even  = mvaInfo_nonRes.getParameter<std::string>("BDT_xml_FileName_nonRes_even");
  std::string BDTFileName_nonRes_odd   = mvaInfo_nonRes.getParameter<std::string>("BDT_xml_FileName_nonRes_odd");
  std::vector<std::string> BDTInputVariables_nonRes = mvaInfo_nonRes.getParameter<std::vector<std::string>>("inputVars_nonRes"); // Include all Input Var.s except BM indices
//  const edm::ParameterSet mvaInfo_nonRes_base = cfg_analyze.getParameter<edm::ParameterSet>("mvaInfo_nonRes_base");
//  std::string BDTFileName_nonRes_base_even  = mvaInfo_nonRes_base.getParameter<std::string>("BDT_xml_FileName_nonRes_base_even");
//  std::string BDTFileName_nonRes_base_odd   = mvaInfo_nonRes_base.getParameter<std::string>("BDT_xml_FileName_nonRes_base_odd");
//  std::vector<std::string> BDTInputVariables_nonRes_base = mvaInfo_nonRes_base.getParameter<std::vector<std::string>>("inputVars_nonRes_base"); // Include all Input Var.s except BM indices

  assert(BDTFileName_spin0_odd != "");
  assert(BDTFileName_spin0_even != "");
  assert(fitFunctionFileName_spin0 != "");
  assert(BDTInputVariables_spin0.size() != 0);
  TMVAInterface* BDT_spin0 = new TMVAInterface(BDTFileName_spin0_odd, BDTFileName_spin0_even, BDTInputVariables_spin0, fitFunctionFileName_spin0);
  BDT_spin0->enableBDTTransform();
  std::map<std::string, double> BDTOutput_Map_spin0;

  assert(BDTFileName_spin2_odd != "");
  assert(BDTFileName_spin2_even != "");
  assert(fitFunctionFileName_spin2 != "");
  assert(BDTInputVariables_spin2.size() != 0);
  TMVAInterface* BDT_spin2 = new TMVAInterface(BDTFileName_spin2_odd, BDTFileName_spin2_even, BDTInputVariables_spin2, fitFunctionFileName_spin2);
  BDT_spin2->enableBDTTransform();
  std::map<std::string, double> BDTOutput_Map_spin2;

  assert(BDTFileName_nonRes_odd != "");
  assert(BDTFileName_nonRes_even != "");
  assert(BDTInputVariables_nonRes.size() != 0);
  TMVAInterface* BDT_nonRes = new TMVAInterface(BDTFileName_nonRes_odd, BDTFileName_nonRes_even, BDTInputVariables_nonRes);
  BDT_nonRes->enableBDTTransform();
  std::map<std::string, double> BDTOutput_Map_nonRes;

//  assert(BDTFileName_nonRes_base_odd != "");
//  assert(BDTFileName_nonRes_base_even != "");
//  assert(BDTInputVariables_nonRes_base.size() != 0);
//  TMVAInterface* BDT_nonRes_base = new TMVAInterface(BDTFileName_nonRes_base_odd, BDTFileName_nonRes_base_even, BDTInputVariables_nonRes_base);
//  BDT_nonRes_base->enableBDTTransform();
//  std::map<std::string, double> BDTOutput_Map_nonRes_base;

  std::map<std::string, double> AllVars_Map;

  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  const bool enable_blacklist = cfg_analyze.getParameter<bool>("enable_blacklist");
  RunLumiEventRejector * blacklist = nullptr;
  if(enable_blacklist)
  {
    const edm::ParameterSet blacklist_cfg = cfg_analyze.getParameter<edm::ParameterSet>("blacklist");
    blacklist = new RunLumiEventRejector(blacklist_cfg);
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
  EventInfo eventInfo(analysisConfig);
  if(isMC)
  {
    const double ref_genWeight = cfg_analyze.getParameter<double>("ref_genWeight");
    eventInfo.set_refGetWeight(ref_genWeight);
  }

//--- HH coupling scan
  const edm::ParameterSet hhWeight_cfg = cfg_analyze.getParameterSet("hhWeight_cfg");
  const bool apply_HH_rwgt_lo = analysisConfig.isHH_rwgt_allowed() && hhWeight_cfg.getParameter<bool>("apply_rwgt_lo");
  const bool apply_HH_rwgt_nlo = analysisConfig.isHH_rwgt_allowed() && hhWeight_cfg.getParameter<bool>("apply_rwgt_nlo");
  const HHWeightInterfaceCouplings * const hhWeight_couplings = new HHWeightInterfaceCouplings(hhWeight_cfg);
  const HHWeightInterfaceLO * HHWeightLO_calc = nullptr;
  const HHWeightInterfaceNLO * HHWeightNLO_calc = nullptr;
  std::vector<std::string> HHWeightNames;
  std::vector<std::string> HHBMNames;
  if(apply_HH_rwgt_lo || apply_HH_rwgt_nlo)
  {
    HHWeightNames = hhWeight_couplings->get_weight_names();
    HHBMNames = hhWeight_couplings->get_bm_names();

    if(apply_HH_rwgt_lo)
    {
      HHWeightLO_calc = new HHWeightInterfaceLO(hhWeight_couplings, hhWeight_cfg);
    }

    if(apply_HH_rwgt_nlo)
    {
      HHWeightNLO_calc = new HHWeightInterfaceNLO(hhWeight_couplings, era);
    }
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

  RecoVertex vertex;
  RecoVertexReader vertexReader(&vertex, branchName_vertex);
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
  metReader->set_phiModulationCorrDetails(&eventInfo, &vertex);
  inputTree -> registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree -> registerReader(metFilterReader);

  GenLeptonReader * genLeptonReader = nullptr;
  GenHadTauReader * genHadTauReader = nullptr;
  GenPhotonReader * genPhotonReader = nullptr;
  GenPhotonReader * genProxyPhotonReader = nullptr;
  GenParticleReader * genFromHardProcessReader = nullptr;
  GenParticleReader * genWBosonReader = nullptr;
  GenJetReader * genJetReader = nullptr;
  LHEInfoReader * lheInfoReader = nullptr;
  PSWeightReader * psWeightReader = nullptr;

  GenParticleReader * genMatchToMuonReader     = nullptr;
  GenParticleReader * genMatchToElectronReader = nullptr;
  GenParticleReader * genMatchToHadTauReader   = nullptr;
  GenParticleReader * genMatchToJetReader      = nullptr;

  if(isMC)
  {
    bool readGenPhotons = apply_genPhotonFilter;
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
        readGenPhotons = true;
      }
    }

    if(readGenPhotons) 
    { 
      genPhotonReader = new GenPhotonReader(branchName_genPhotons);
      inputTree -> registerReader(genPhotonReader);
    }

    if(apply_genPhotonFilter)
    {
      genProxyPhotonReader = new GenPhotonReader(branchName_genProxyPhotons);
      inputTree -> registerReader(genProxyPhotonReader);

      genFromHardProcessReader = new GenParticleReader(branchName_genFromHardProcess);
      inputTree -> registerReader(genFromHardProcessReader);
    }

    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree -> registerReader(lheInfoReader);
    psWeightReader = new PSWeightReader(hasPS, apply_LHE_nom);
    inputTree -> registerReader(psWeightReader);

    if(analysisConfig.isMC_VH())
    {
      genWBosonReader = new GenParticleReader(branchName_genWBosons);
      inputTree -> registerReader(genWBosonReader);
    }
  }

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;

//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    MuonHistManager* muons_;
    JetHistManager* jets_;
    JetHistManager* BJets_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    EvtHistManager_hh_4l* evt_;
    SVfit4tauHistManager_MarkovChain* svFit4tau_wMassConstraint_;
    DatacardHistManager_hh* datacard_;
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

      int idxLepton = genMatchDefinition->getIdx();

      selHistManagerType* selHistManager = new selHistManagerType();
      if(! skipBooking)
      {
        selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/electrons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->electrons_->bookHistograms(fs);
        selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/muons", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->muons_->bookHistograms(fs);
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
        
        selHistManager->svFit4tau_wMassConstraint_ = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/svFit4tau_wMassConstraint", histogramDir.data()), era_string, central_or_shift));
        selHistManager->svFit4tau_wMassConstraint_->bookHistograms(fs);
      }
      selHistManager->evt_ = new EvtHistManager_hh_4l(makeHistManager_cfg(process_and_genMatch,
									  Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
      selHistManager->evt_->bookHistograms(fs);

      selHistManager->datacard_ = new DatacardHistManager_hh(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/datacard", histogramDir.data()), era_string, central_or_shift),
        analysisConfig, eventInfo, HHWeightLO_calc, HHWeightNLO_calc,
        isDEBUG);
      selHistManager->datacard_->bookHistograms(fs);

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
        selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
      }
      selHistManagers[central_or_shift][idxLepton] = selHistManager;
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
    if(apply_HH_rwgt_lo || apply_HH_rwgt_lo)
    {
      for(auto bmName : HHWeightNames)
      {
        bdt_filler->register_variable<float_type>(bmName.data());
      }
    }
    bdt_filler->register_variable<float_type>("evtWeight",
					      "genWeight",
					      "lheWeight",
					      "pileupWeight",
					      "triggerWeight",
					      "btagWeight",
					      "leptonEffSF",
					      "data_to_MC_correction",
					      "FR_Weight",
					      "lep1_frWeight",
					      "lep2_frWeight",
					      "lep3_frWeight",
					      "lep4_frWeight",
					      "dihiggsVisMass_sel",                     
                                              "dihiggsMass",                            
                                              "HT",                                     
                                              "STMET",                                  
                                              "lep1_pt",                                
                                              "lep2_pt",                                
                                              "lep3_pt",                                
                                              "lep4_pt",                                
                                              "lep1_conePt",                            
                                              "lep2_conePt",                            
                                              "lep3_conePt",                            
                                              "lep4_conePt",                            
                                              "lep1_eta",                               
                                              "lep2_eta",                               
                                              "lep3_eta",                               
                                              "lep4_eta",                               
                                              "lep1_phi",                               
                                              "lep2_phi",                               
                                              "lep3_phi",                               
                                              "lep4_phi",
					      "lep1_dxy",
					      "lep2_dxy",
					      "lep3_dxy",
					      "lep4_dxy",
					      "lep1_dz",
					      "lep2_dz",
					      "lep3_dz",
					      "lep4_dz",
					      "pt4l",
					      "pt4lParallelHadT",
					      "pt4lPerpendicularHadT",
					      "mt4l",
                                              "maxPtSum_pair1_pt",                      
                                              "maxPtSum_pair1_eta",                     
                                              "maxPtSum_pair1_phi",                     
                                              "maxPtSum_pair1_deltaEtaLep1",            
                                              "maxPtSum_pair1_deltaPhiLep1",            
                                              "maxPtSum_pair1_deltaEta",                
                                              "maxPtSum_pair1_deltaPhi",                
                                              "maxPtSum_pair1_deltaR",                  
                                              "maxPtSum_pair1_deltaPt",                 
                                              "maxPtSum_pair1_m",                       
                                              "maxPtSum_pair2_pt",                      
                                              "maxPtSum_pair2_eta",                     
                                              "maxPtSum_pair2_phi",                     
                                              "maxPtSum_pair2_deltaEtaLep1",            
                                              "maxPtSum_pair2_deltaPhiLep1",            
                                              "maxPtSum_pair2_deltaEta",                
                                              "maxPtSum_pair2_deltaPhi",                
                                              "maxPtSum_pair2_deltaR",                  
                                              "maxPtSum_pair2_deltaPt",                 
                                              "maxPtSum_pair2_m",                       
                                              "maxSubleadPt_pair1_pt",                  
                                              "maxSubleadPt_pair1_eta",                 
                                              "maxSubleadPt_pair1_phi",                 
                                              "maxSubleadPt_pair1_deltaEtaLep1",        
                                              "maxSubleadPt_pair1_deltaPhiLep1",        
                                              "maxSubleadPt_pair1_deltaEta",            
                                              "maxSubleadPt_pair1_deltaPhi",            
                                              "maxSubleadPt_pair1_deltaR",              
                                              "maxSubleadPt_pair1_deltaPt",             
                                              "maxSubleadPt_pair1_m",                   
                                              "maxSubleadPt_pair2_pt",                  
                                              "maxSubleadPt_pair2_eta",                 
                                              "maxSubleadPt_pair2_phi",                 
                                              "maxSubleadPt_pair2_deltaEtaLep1",        
                                              "maxSubleadPt_pair2_deltaPhiLep1",        
                                              "maxSubleadPt_pair2_deltaEta",            
                                              "maxSubleadPt_pair2_deltaPhi",            
                                              "maxSubleadPt_pair2_deltaR",              
                                              "maxSubleadPt_pair2_deltaPt",             
                                              "maxSubleadPt_pair2_m",                   
                                              "minDeltaRSum_pair1_pt",                  
                                              "minDeltaRSum_pair1_eta",                 
                                              "minDeltaRSum_pair1_phi",                 
                                              "minDeltaRSum_pair1_deltaEtaLep1",        
                                              "minDeltaRSum_pair1_deltaPhiLep1",        
                                              "minDeltaRSum_pair1_deltaEta",            
                                              "minDeltaRSum_pair1_deltaPhi",            
                                              "minDeltaRSum_pair1_deltaR",              
                                              "minDeltaRSum_pair1_deltaPt",             
                                              "minDeltaRSum_pair1_m",                   
                                              "minDeltaRSum_pair2_pt",                  
                                              "minDeltaRSum_pair2_eta",                 
                                              "minDeltaRSum_pair2_phi",                 
                                              "minDeltaRSum_pair2_deltaEtaLep1",        
                                              "minDeltaRSum_pair2_deltaPhiLep1",        
                                              "minDeltaRSum_pair2_deltaEta",            
                                              "minDeltaRSum_pair2_deltaPhi",            
                                              "minDeltaRSum_pair2_deltaR",              
                                              "minDeltaRSum_pair2_deltaPt",             
                                              "minDeltaRSum_pair2_m",                   
                                              "minSubclosestDeltaR_pair1_pt",           
                                              "minSubclosestDeltaR_pair1_eta",          
                                              "minSubclosestDeltaR_pair1_phi",          
                                              "minSubclosestDeltaR_pair1_deltaEtaLep1", 
                                              "minSubclosestDeltaR_pair1_deltaPhiLep1", 
                                              "minSubclosestDeltaR_pair1_deltaEta",     
                                              "minSubclosestDeltaR_pair1_deltaPhi",     
                                              "minSubclosestDeltaR_pair1_deltaR",       
                                              "minSubclosestDeltaR_pair1_deltaPt",      
                                              "minSubclosestDeltaR_pair1_m",            
                                              "minSubclosestDeltaR_pair2_pt",           
                                              "minSubclosestDeltaR_pair2_eta",          
                                              "minSubclosestDeltaR_pair2_phi",          
                                              "minSubclosestDeltaR_pair2_deltaEtaLep1", 
                                              "minSubclosestDeltaR_pair2_deltaPhiLep1", 
                                              "minSubclosestDeltaR_pair2_deltaEta",     
                                              "minSubclosestDeltaR_pair2_deltaPhi",     
                                              "minSubclosestDeltaR_pair2_deltaR",       
                                              "minSubclosestDeltaR_pair2_deltaPt",      
                                              "minSubclosestDeltaR_pair2_m",            
                                              "MET",
					      "METParallelHadT",
					      "METPerpendicularHadT",
                                              "METPhi",                                 
                                              "METDeltaPhiLep1",                        
                                              "MET_LD",                                 
                                              "HTmiss"                                  
    );
    bdt_filler->register_variable<int_type>(
					    "numJets",                                  
                                            "numElectrons",                             
                                            "numMuons",
					    "numLeptons",
                                            "numSelJetsPtGt40",                         
                                            "numBJets_loose",                           
                                            "numBJets_medium",                          
                                            "lep1_isElectron",                          
                                            "lep1_charge",                              
                                            "lep2_isElectron",                          
                                            "lep2_charge",                              
                                            "lep3_isElectron",                          
                                            "lep3_charge",                              
                                            "lep4_isElectron",                          
                                            "lep4_charge",                              
                                            "leptonChargeSum",                          
                                            "electronChargeSum",                        
                                            "muonChargeSum",                            
                                            "nSFOS"                                     
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

  std::string ZVeto_string = "Z-boson mass veto";
  if(invert_ZbosonMassVeto) ZVeto_string = "Z-boson mass veto inverted";

  const std::vector<std::string> cuts = {
    "run:ls:event selection",
    "object multiplicity",
    "gen photon filter",
    "trigger",
    ">= 4 presel leptons",
    "b-jet veto",
    ">= 4 sel leptons",
    "trigger & fakeable lepton flavor matching",
    "trigger & dataset matching",
    "HLT filter matching",
    "m(ll) > 12 GeV",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 15 GeV && fourth lepton pT > 10 GeV",
    "sel lepton charge",
    ZVeto_string,
    "H->ZZ*->4l veto",
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
      if(objectMultiplicity.getNRecoLepton(minLeptonSelection) < 4 ||
         objectMultiplicity.getNRecoLepton(kTight)             > 4  )
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
    std::vector<GenPhoton> genPhotonsFinal;
    std::vector<GenPhoton> genProxyPhotons;
    std::vector<GenParticle> genFromHardProcess;
    std::vector<GenJet> genJets;

    std::vector<GenParticle> muonGenMatch;
    std::vector<GenParticle> electronGenMatch;
    std::vector<GenParticle> hadTauGenMatch;
    std::vector<GenParticle> jetGenMatch;
    if(isMC && (fillGenEvtHistograms || apply_genPhotonFilter))
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
      if(genPhotonReader) genPhotons = genPhotonReader->read(apply_genPhotonFilter);
      if(genJetReader)    genJets = genJetReader->read();

      if(genProxyPhotonReader)     genProxyPhotons = genProxyPhotonReader->read(apply_genPhotonFilter);
      if(genFromHardProcessReader) genFromHardProcess = genFromHardProcessReader->read();

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
    genPhotonsFinal = filterByStatus(genPhotons, 1);

    if(!genPhotonFilter(genPhotons, genProxyPhotons, genFromHardProcess))
    {
      if(isDEBUG || run_lumi_eventSelector)
      {
        std::cout << "event " << eventInfo.str() << " FAILS gen photon filter\n";
      }
      continue;
    }
    cutFlowTable.update("gen photon filter", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("gen photon filter", evtWeightRecorder.get(central_or_shift_main));

    eventInfo.reset_productionMode();
    if(genWBosonReader && analysisConfig.isMC_VH())
    {
      const std::vector<GenParticle> genWBosons = genWBosonReader->read();
      eventInfo.set_productionMode(get_VH_productionMode(genWBosons));
    }

    if(isMC)
    {
      if(apply_genWeight)         evtWeightRecorder.record_genWeight(eventInfo);
      if(eventWeightManager)      evtWeightRecorder.record_auxWeight(eventWeightManager);
      if(l1PreFiringWeightReader) evtWeightRecorder.record_l1PrefireWeight(l1PreFiringWeightReader);
      if(apply_topPtReweighting)  evtWeightRecorder.record_toppt_rwgt(eventInfo.topPtRwgtSF);
      if(apply_HH_rwgt_lo)        evtWeightRecorder.record_hhWeight_lo(HHWeightLO_calc, eventInfo, isDEBUG);
      if(apply_HH_rwgt_nlo)       evtWeightRecorder.record_hhWeight_nlo(HHWeightNLO_calc, eventInfo, isDEBUG);
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
          genElectrons, genMuons, genHadTaus, genPhotonsFinal, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
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

    const std::vector<const RecoLepton*> preselLeptons = pickFirstNobjects(preselLeptonsFull, 4);
    const std::vector<const RecoLepton*> fakeableLeptons = pickFirstNobjects(fakeableLeptonsFull, 4);
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

    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("selMuons", selMuons);
      printCollection("selElectrons", selElectrons);
      printCollection("selLeptons", selLeptons);
    }

    const std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    const std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    const std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    const std::vector<const RecoHadTau*> fakeableHadTaus = fakeableHadTauSelector(cleanedHadTaus, isHigherPt);

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets = jetReader->read();
    const std::vector<const RecoJet*> jet_ptrs = convert_to_ptrs(jets);
    const std::vector<const RecoJet*> cleanedJets = jetCleaningByIndex ?
      jetCleanerByIndex(jet_ptrs, selectBDT ? selLeptons_full : fakeableLeptonsFull, fakeableHadTaus) :
      jetCleaner       (jet_ptrs, selectBDT ? selLeptons_full : fakeableLeptonsFull, fakeableHadTaus)
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
      if(genPhotonReader) genPhotonsFinal = genPhotonReader->read();
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
        electronGenMatcher.addGenPhotonMatch(preselElectrons, genPhotonsFinal);
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
    // require exactly two leptons passing loose preselection criteria to avoid overlap with 3l category
    if ( !(preselLeptonsFull.size() >= 4) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS preselLeptons selection." << std::endl;
  printCollection("preselLeptons", preselLeptonsFull);
      }
      continue;
    }
    cutFlowTable.update(">= 4 presel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 4 presel leptons", evtWeightRecorder.get(central_or_shift_main));

    if ( selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1 ) continue;
    cutFlowTable.update("b-jet veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("b-jet veto", evtWeightRecorder.get(central_or_shift_main));

//--- compute MHT and linear MET discriminant (met_LD)
    const RecoMEt met = metReader->read();
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptonsFull, fakeableHadTaus, selJets);
    double met_LD = compMEt_LD(met.p4(), mht_p4);
    
    double HT = compHT(fakeableLeptons, {}, selJets);
    double STMET = compSTMEt(fakeableLeptons, {}, selJets, met.p4());

//--- apply final event selection
    // require exactly two leptons passing tight selection criteria of final event selection
    if ( !(selLeptons.size() >= 4) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS selLeptons selection." << std::endl;
	printCollection("selLeptons", selLeptons);
	//printCollection("preselLeptons", preselLeptons);
      }
      continue;
    }
    cutFlowTable.update(">= 4 sel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 4 sel leptons", evtWeightRecorder.get(central_or_shift_main));

    const RecoLepton* selLepton_lead = selLeptons[0];
    int selLepton_lead_type = getLeptonType(selLepton_lead->pdgId());
    const RecoLepton* selLepton_sublead = selLeptons[1];
    int selLepton_sublead_type = getLeptonType(selLepton_sublead->pdgId());
    const RecoLepton* selLepton_third = selLeptons[2];
    int selLepton_third_type = getLeptonType(selLepton_third->pdgId());
    const RecoLepton* selLepton_fourth = selLeptons[3];
    int selLepton_fourth_type = getLeptonType(selLepton_fourth->pdgId());
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead, selLepton_third, selLepton_fourth);

    double lep1_pt = selLepton_lead->pt();
    double lep2_pt = selLepton_sublead->pt();
    double lep3_pt = selLepton_third->pt();
    double lep4_pt = selLepton_fourth->pt();
    double lep1_conePt = selLepton_lead->cone_pt();
    double lep2_conePt = selLepton_sublead->cone_pt();
    double lep3_conePt = selLepton_third->cone_pt();
    double lep4_conePt = selLepton_fourth->cone_pt();
    double lep1_eta = selLepton_lead->eta();
    double lep2_eta = selLepton_sublead->eta();
    double lep3_eta = selLepton_third->eta();
    double lep4_eta = selLepton_fourth->eta();
    double lep1_phi = selLepton_lead->phi();
    double lep2_phi = selLepton_sublead->phi();
    double lep3_phi = selLepton_third->phi();
    double lep4_phi = selLepton_fourth->phi();
    double lep1_dxy = selLepton_lead->dxy();
    double lep2_dxy = selLepton_sublead->dxy();
    double lep3_dxy = selLepton_third->dxy();
    double lep4_dxy = selLepton_fourth->dxy();
    double lep1_dz = selLepton_lead->dz();
    double lep2_dz = selLepton_sublead->dz();
    double lep3_dz = selLepton_third->dz();
    double lep4_dz = selLepton_fourth->dz();
    Particle::LorentzVector p4l = selLepton_lead->cone_p4()+selLepton_sublead->cone_p4()+selLepton_third->cone_p4()+selLepton_fourth->cone_p4();
    TVector3 pt4lVetor(p4l.px(),p4l.py(),0);
    TVector3 metVector(met.p4().px(),met.p4().py(),0);
    TVector3 hadTVector = -metVector-pt4lVetor;
    TVector3 hadTVectorNorm = hadTVector.Unit();
    double pt4l = p4l.pt();
    double pt4lParallelHadT = pt4lVetor.Dot(hadTVectorNorm);
    double pt4lPerpendicularHadT = pt4lVetor.Perp(hadTVectorNorm);
    double mt4l = (p4l+met.p4()).M();
    double MET = met.pt();
    double METParallelHadT = metVector.Dot(hadTVectorNorm);
    double METPerpendicularHadT = metVector.Perp(hadTVectorNorm);
    double METPhi = met.phi();
    double METDeltaPhiLep1 = std::abs(deltaPhi(met.phi(), lep1_phi));
    double HTmiss = mht_p4.pt();
    int lep1_isElectron = selLepton_lead_type == kElectron;
    int lep1_charge = selLepton_lead->charge();
    int lep2_isElectron = selLepton_sublead_type == kElectron;
    int lep2_charge = selLepton_sublead->charge();
    int lep3_isElectron = selLepton_third_type == kElectron;
    int lep3_charge = selLepton_third->charge();
    int lep4_isElectron = selLepton_fourth_type == kElectron;
    int lep4_charge = selLepton_fourth->charge();
    int leptonChargeSum = selLepton_lead->charge() + selLepton_sublead->charge() + selLepton_third->charge() + selLepton_fourth->charge();
    int electronChargeSum =
      ((selLepton_lead_type == kElectron) ? selLepton_lead->charge() : 0) + ((selLepton_sublead_type == kElectron) ? selLepton_sublead->charge() : 0) +
      ((selLepton_third_type == kElectron) ? selLepton_third->charge() : 0) + ((selLepton_fourth_type == kElectron) ? selLepton_fourth->charge() : 0);
    int muonChargeSum = ((selLepton_lead_type != kElectron) ? selLepton_lead->charge() : 0) + ((selLepton_sublead_type != kElectron) ? selLepton_sublead->charge() : 0) +
      ((selLepton_third_type != kElectron) ? selLepton_third->charge() : 0) + ((selLepton_fourth_type != kElectron) ? selLepton_fourth->charge() : 0);
    int nSFOS = 0;
    if(selLepton_lead->pdgId()==-selLepton_sublead->pdgId())
      nSFOS++;
    if(selLepton_third->pdgId()==-selLepton_fourth->pdgId())
      nSFOS++;
    if(nSFOS==0){
      if(selLepton_lead->pdgId()==-selLepton_third->pdgId())
	nSFOS++;
      if(selLepton_sublead->pdgId()==-selLepton_fourth->pdgId())
	nSFOS++;
    }
    if(nSFOS==0){
      if(selLepton_lead->pdgId()==-selLepton_fourth->pdgId())
	nSFOS++;
      if(selLepton_sublead->pdgId()==-selLepton_third->pdgId())
        nSFOS++;
    }

    Particle::LorentzVector maxPtSum_pair1lep1 = selLepton_lead->cone_p4();
    Particle::LorentzVector maxPtSum_pair2lep1 = selLepton_sublead->cone_p4();
    Particle::LorentzVector maxPtSum_pair1lep2 = selLepton_third->cone_p4();
    Particle::LorentzVector maxPtSum_pair2lep2 = selLepton_fourth->cone_p4();

    Particle::LorentzVector maxSubleadPt_pair1lep1 = selLepton_lead->cone_p4();
    Particle::LorentzVector maxSubleadPt_pair2lep1 = selLepton_sublead->cone_p4();
    Particle::LorentzVector maxSubleadPt_pair1lep2 = selLepton_third->cone_p4();
    Particle::LorentzVector maxSubleadPt_pair2lep2 = selLepton_fourth->cone_p4();

    Particle::LorentzVector minDeltaRSum_pair1lep1 = selLepton_lead->cone_p4();
    Particle::LorentzVector minDeltaRSum_pair2lep1 = selLepton_sublead->cone_p4();
    Particle::LorentzVector minDeltaRSum_pair1lep2 = selLepton_third->cone_p4();
    Particle::LorentzVector minDeltaRSum_pair2lep2 = selLepton_fourth->cone_p4();

    Particle::LorentzVector minSubclosestDeltaR_pair1lep1 = selLepton_lead->cone_p4();
    Particle::LorentzVector minSubclosestDeltaR_pair2lep1 = selLepton_sublead->cone_p4();
    Particle::LorentzVector minSubclosestDeltaR_pair1lep2 = selLepton_third->cone_p4();
    Particle::LorentzVector minSubclosestDeltaR_pair2lep2 = selLepton_fourth->cone_p4();

    Particle::LorentzVector pair1lep1 = selLepton_lead->cone_p4();
    Particle::LorentzVector pair1lep2 = selLepton_third->cone_p4();
    Particle::LorentzVector pair2lep1 = selLepton_sublead->cone_p4();
    Particle::LorentzVector pair2lep2 = selLepton_fourth->cone_p4();

    bool lep1lep2OS = (selLepton_lead->charge() != selLepton_sublead->charge());
    bool lep1lep3OS = (selLepton_lead->charge() != selLepton_third->charge());

    if (lep1lep2OS)
      {
	if (!lep1lep3OS)
	  {
            pair1lep2 = selLepton_fourth->cone_p4();
            pair2lep2 = selLepton_third->cone_p4();
	  }
	if ((pair1lep1 + pair1lep2).mass() < 130 && (pair2lep1 + pair2lep2).mass() < 130)
	  {
	    maxPtSum_pair1lep1 = pair1lep1;
	    maxPtSum_pair2lep1 = pair2lep1;
	    maxPtSum_pair1lep2 = pair1lep2;
	    maxPtSum_pair2lep2 = pair2lep2;

	    maxSubleadPt_pair1lep1 = pair1lep1;
	    maxSubleadPt_pair2lep1 = pair2lep1;
	    maxSubleadPt_pair1lep2 = pair1lep2;
	    maxSubleadPt_pair2lep2 = pair2lep2;

	    minDeltaRSum_pair1lep1 = pair1lep1;
	    minDeltaRSum_pair2lep1 = pair2lep1;
	    minDeltaRSum_pair1lep2 = pair1lep2;
	    minDeltaRSum_pair2lep2 = pair2lep2;

	    minSubclosestDeltaR_pair1lep1 = pair1lep1;
	    minSubclosestDeltaR_pair2lep1 = pair2lep1;
	    minSubclosestDeltaR_pair1lep2 = pair1lep2;
	    minSubclosestDeltaR_pair2lep2 = pair2lep2;
	  }
	else
	  {
            pair1lep1 = selLepton_lead->cone_p4();
            pair1lep2 = selLepton_sublead->cone_p4();
            pair2lep1 = selLepton_third->cone_p4();
            pair2lep2 = selLepton_fourth->cone_p4();
	    if ((pair1lep1 + pair1lep2).mass() < 130 && (pair2lep1 + pair2lep2).mass() < 130)
	      {
		maxPtSum_pair1lep1 = pair1lep1;
		maxPtSum_pair2lep1 = pair2lep1;
		maxPtSum_pair1lep2 = pair1lep2;
		maxPtSum_pair2lep2 = pair2lep2;

		maxSubleadPt_pair1lep1 = pair1lep1;
		maxSubleadPt_pair2lep1 = pair2lep1;
		maxSubleadPt_pair1lep2 = pair1lep2;
		maxSubleadPt_pair2lep2 = pair2lep2;

		minDeltaRSum_pair1lep1 = pair1lep1;
		minDeltaRSum_pair2lep1 = pair2lep1;
		minDeltaRSum_pair1lep2 = pair1lep2;
		minDeltaRSum_pair2lep2 = pair2lep2;

		minSubclosestDeltaR_pair1lep1 = pair1lep1;
		minSubclosestDeltaR_pair2lep1 = pair2lep1;
		minSubclosestDeltaR_pair1lep2 = pair1lep2;
		minSubclosestDeltaR_pair2lep2 = pair2lep2;
	      }
	    else
	      {
		if (lep1lep3OS)
		  {
                    pair1lep1 = selLepton_lead->cone_p4();
                    pair1lep2 = selLepton_third->cone_p4();
                    pair2lep1 = selLepton_sublead->cone_p4();
                    pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
                    pair1lep1 = selLepton_lead->cone_p4();
                    pair1lep2 = selLepton_fourth->cone_p4();
                    pair2lep1 = selLepton_sublead->cone_p4();
                    pair2lep2 = selLepton_third->cone_p4();
		  }
                if ((selLepton_lead->cone_p4() + selLepton_sublead->cone_p4()).pt() + (selLepton_third->cone_p4() + selLepton_fourth->cone_p4()).pt() >
		    (pair1lep1 + pair1lep2).pt() + (pair2lep1 + pair2lep2).pt())
		  {
                    maxPtSum_pair1lep1 = selLepton_lead->cone_p4();
                    maxPtSum_pair1lep2 = selLepton_sublead->cone_p4();
                    maxPtSum_pair2lep1 = selLepton_third->cone_p4();
                    maxPtSum_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
		    maxPtSum_pair1lep1 = pair1lep1;
		    maxPtSum_pair1lep2 = pair1lep2;
		    maxPtSum_pair2lep1 = pair2lep1;
		    maxPtSum_pair2lep2 = pair2lep2;
		  }

                if (std::min((selLepton_lead->cone_p4() + selLepton_sublead->cone_p4()).pt(), (selLepton_third->cone_p4() + selLepton_fourth->cone_p4()).pt()) >
		    std::min((pair1lep1 + pair1lep2).pt(), (pair2lep1 + pair2lep2).pt()))
		  {
                    maxSubleadPt_pair1lep1 = selLepton_lead->cone_p4();
                    maxSubleadPt_pair1lep2 = selLepton_sublead->cone_p4();
                    maxSubleadPt_pair2lep1 = selLepton_third->cone_p4();
                    maxSubleadPt_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
		    maxSubleadPt_pair1lep1 = pair1lep1;
		    maxSubleadPt_pair1lep2 = pair1lep2;
		    maxSubleadPt_pair2lep1 = pair2lep1;
		    maxSubleadPt_pair2lep2 = pair2lep2;
		  }

                if (deltaR(selLepton_lead->cone_p4(), selLepton_sublead->cone_p4()) + deltaR(selLepton_third->cone_p4(), selLepton_fourth->cone_p4()) <
		    deltaR(pair1lep1, pair1lep2) + deltaR(pair2lep1, pair2lep2))
		  {
                    minDeltaRSum_pair1lep1 = selLepton_lead->cone_p4();
                    minDeltaRSum_pair1lep2 = selLepton_sublead->cone_p4();
                    minDeltaRSum_pair2lep1 = selLepton_third->cone_p4();
                    minDeltaRSum_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
		    minDeltaRSum_pair1lep1 = pair1lep1;
		    minDeltaRSum_pair1lep2 = pair1lep2;
		    minDeltaRSum_pair2lep1 = pair2lep1;
		    minDeltaRSum_pair2lep2 = pair2lep2;
		  }

                if (std::max(deltaR(selLepton_lead->cone_p4(), selLepton_sublead->cone_p4()), deltaR(selLepton_third->cone_p4(), selLepton_fourth->cone_p4())) <
		    std::max(deltaR(pair1lep1, pair1lep2), deltaR(pair2lep1, pair2lep2)))
		  {
                    minSubclosestDeltaR_pair1lep1 = selLepton_lead->cone_p4();
                    minSubclosestDeltaR_pair1lep2 = selLepton_sublead->cone_p4();
                    minSubclosestDeltaR_pair2lep1 = selLepton_third->cone_p4();
                    minSubclosestDeltaR_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
		    minSubclosestDeltaR_pair1lep1 = pair1lep1;
		    minSubclosestDeltaR_pair1lep2 = pair1lep2;
		    minSubclosestDeltaR_pair2lep1 = pair2lep1;
		    minSubclosestDeltaR_pair2lep2 = pair2lep2;
		  }
	      }
	  }
      }
    else
      {
	if ((pair1lep1 + pair1lep2).mass() < 130 && (pair2lep1 + pair2lep2).mass() < 130)
	  {
	    maxPtSum_pair1lep1 = pair1lep1;
	    maxPtSum_pair2lep1 = pair2lep1;
	    maxPtSum_pair1lep2 = pair1lep2;
	    maxPtSum_pair2lep2 = pair2lep2;

	    maxSubleadPt_pair1lep1 = pair1lep1;
	    maxSubleadPt_pair2lep1 = pair2lep1;
	    maxSubleadPt_pair1lep2 = pair1lep2;
	    maxSubleadPt_pair2lep2 = pair2lep2;

	    minDeltaRSum_pair1lep1 = pair1lep1;
	    minDeltaRSum_pair2lep1 = pair2lep1;
	    minDeltaRSum_pair1lep2 = pair1lep2;
	    minDeltaRSum_pair2lep2 = pair2lep2;

	    minSubclosestDeltaR_pair1lep1 = pair1lep1;
	    minSubclosestDeltaR_pair2lep1 = pair2lep1;
	    minSubclosestDeltaR_pair1lep2 = pair1lep2;
	    minSubclosestDeltaR_pair2lep2 = pair2lep2;
	  }
	else
	  {
            pair1lep2 = selLepton_fourth->cone_p4();
            pair2lep2 = selLepton_third->cone_p4();
	    if ((pair1lep1 + pair1lep2).mass() < 130 && (pair2lep1 + pair2lep2).mass() < 130)
	      {
		maxPtSum_pair1lep1 = pair1lep1;
		maxPtSum_pair2lep1 = pair2lep1;
		maxPtSum_pair1lep2 = pair1lep2;
		maxPtSum_pair2lep2 = pair2lep2;

		maxSubleadPt_pair1lep1 = pair1lep1;
		maxSubleadPt_pair2lep1 = pair2lep1;
		maxSubleadPt_pair1lep2 = pair1lep2;
		maxSubleadPt_pair2lep2 = pair2lep2;

		minDeltaRSum_pair1lep1 = pair1lep1;
		minDeltaRSum_pair2lep1 = pair2lep1;
		minDeltaRSum_pair1lep2 = pair1lep2;
		minDeltaRSum_pair2lep2 = pair2lep2;

		minSubclosestDeltaR_pair1lep1 = pair1lep1;
		minSubclosestDeltaR_pair2lep1 = pair2lep1;
		minSubclosestDeltaR_pair1lep2 = pair1lep2;
		minSubclosestDeltaR_pair2lep2 = pair2lep2;
	      }
	    else
	      {
                if ((selLepton_lead->cone_p4() + selLepton_third->cone_p4()).pt() + (selLepton_sublead->cone_p4() + selLepton_fourth->cone_p4()).pt() >
                    (selLepton_lead->cone_p4() + selLepton_fourth->cone_p4()).pt() + (selLepton_sublead->cone_p4() + selLepton_third->cone_p4()).pt())
		  {
                    maxPtSum_pair1lep1 = selLepton_lead->cone_p4();
                    maxPtSum_pair1lep2 = selLepton_third->cone_p4();
                    maxPtSum_pair2lep1 = selLepton_sublead->cone_p4();
                    maxPtSum_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
                    maxPtSum_pair1lep1 = selLepton_lead->cone_p4();
                    maxPtSum_pair1lep2 = selLepton_fourth->cone_p4();
                    maxPtSum_pair2lep1 = selLepton_sublead->cone_p4();
                    maxPtSum_pair2lep2 = selLepton_third->cone_p4();
		  }

                if (std::min((selLepton_lead->cone_p4() + selLepton_third->cone_p4()).pt(), (selLepton_sublead->cone_p4() + selLepton_fourth->cone_p4()).pt()) >
                    std::min((selLepton_lead->cone_p4() + selLepton_fourth->cone_p4()).pt(), (selLepton_sublead->cone_p4() + selLepton_third->cone_p4()).pt()))
		  {
                    maxSubleadPt_pair1lep1 = selLepton_lead->cone_p4();
                    maxSubleadPt_pair1lep2 = selLepton_third->cone_p4();
                    maxSubleadPt_pair2lep1 = selLepton_sublead->cone_p4();
                    maxSubleadPt_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
                    maxSubleadPt_pair1lep1 = selLepton_lead->cone_p4();
                    maxSubleadPt_pair1lep2 = selLepton_fourth->cone_p4();
                    maxSubleadPt_pair2lep1 = selLepton_sublead->cone_p4();
                    maxSubleadPt_pair2lep2 = selLepton_third->cone_p4();
		  }

                if (deltaR(selLepton_lead->cone_p4(), selLepton_third->cone_p4()) + deltaR(selLepton_sublead->cone_p4(), selLepton_fourth->cone_p4()) <
                    deltaR(selLepton_lead->cone_p4(), selLepton_fourth->cone_p4()) + deltaR(selLepton_sublead->cone_p4(), selLepton_third->cone_p4()))
		  {
                    minDeltaRSum_pair1lep1 = selLepton_lead->cone_p4();
                    minDeltaRSum_pair1lep2 = selLepton_third->cone_p4();
                    minDeltaRSum_pair2lep1 = selLepton_sublead->cone_p4();
                    minDeltaRSum_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
                    minDeltaRSum_pair1lep1 = selLepton_lead->cone_p4();
                    minDeltaRSum_pair1lep2 = selLepton_fourth->cone_p4();
                    minDeltaRSum_pair2lep1 = selLepton_sublead->cone_p4();
                    minDeltaRSum_pair2lep2 = selLepton_third->cone_p4();
		  }

                if (std::max(deltaR(selLepton_lead->cone_p4(), selLepton_third->cone_p4()), deltaR(selLepton_sublead->cone_p4(), selLepton_fourth->cone_p4())) <
                    std::max(deltaR(selLepton_lead->cone_p4(), selLepton_fourth->cone_p4()), deltaR(selLepton_sublead->cone_p4(), selLepton_third->cone_p4())))
		  {
                    minSubclosestDeltaR_pair1lep1 = selLepton_lead->cone_p4();
                    minSubclosestDeltaR_pair1lep2 = selLepton_third->cone_p4();
                    minSubclosestDeltaR_pair2lep1 = selLepton_sublead->cone_p4();
                    minSubclosestDeltaR_pair2lep2 = selLepton_fourth->cone_p4();
		  }
		else
		  {
                    minSubclosestDeltaR_pair1lep1 = selLepton_lead->cone_p4();
                    minSubclosestDeltaR_pair1lep2 = selLepton_third->cone_p4();
                    minSubclosestDeltaR_pair2lep1 = selLepton_sublead->cone_p4();
                    minSubclosestDeltaR_pair2lep2 = selLepton_fourth->cone_p4();
		  }
	      }
	  }
      }

    double maxPtSum_pair1_pt = (maxPtSum_pair1lep1 + maxPtSum_pair1lep2).pt();
    double maxPtSum_pair1_eta = (maxPtSum_pair1lep1 + maxPtSum_pair1lep2).eta();
    double maxPtSum_pair1_phi = (maxPtSum_pair1lep1 + maxPtSum_pair1lep2).phi();
    double maxPtSum_pair1_deltaEtaLep1 = std::abs((maxPtSum_pair1lep1 + maxPtSum_pair1lep2).eta() - lep1_eta);
    double maxPtSum_pair1_deltaPhiLep1 = std::abs(deltaPhi((maxPtSum_pair1lep1 + maxPtSum_pair1lep2).phi(), lep1_phi));
    double maxPtSum_pair1_deltaEta = std::abs(maxPtSum_pair1lep1.eta() - maxPtSum_pair1lep2.eta());
    double maxPtSum_pair1_deltaPhi = std::abs(deltaPhi(maxPtSum_pair1lep1.phi(), maxPtSum_pair1lep2.phi()));
    double maxPtSum_pair1_deltaR = deltaR(maxPtSum_pair1lep1, maxPtSum_pair1lep2);
    double maxPtSum_pair1_deltaPt = std::abs(maxPtSum_pair1lep1.pt() - maxPtSum_pair1lep2.pt());
    double maxPtSum_pair1_m = (maxPtSum_pair1lep1 + maxPtSum_pair1lep2).mass();
    double maxPtSum_pair2_pt = (maxPtSum_pair2lep1 + maxPtSum_pair2lep2).pt();
    double maxPtSum_pair2_eta = (maxPtSum_pair2lep1 + maxPtSum_pair2lep2).eta();
    double maxPtSum_pair2_phi = (maxPtSum_pair2lep1 + maxPtSum_pair2lep2).phi();
    double maxPtSum_pair2_deltaEtaLep1 = std::abs((maxPtSum_pair2lep1 + maxPtSum_pair2lep2).eta() - lep1_eta);
    double maxPtSum_pair2_deltaPhiLep1 = std::abs(deltaPhi((maxPtSum_pair2lep1 + maxPtSum_pair2lep2).phi(), lep1_phi));
    double maxPtSum_pair2_deltaEta = std::abs(maxPtSum_pair2lep1.eta() - maxPtSum_pair2lep2.eta());
    double maxPtSum_pair2_deltaPhi = std::abs(deltaPhi(maxPtSum_pair2lep1.phi(), maxPtSum_pair2lep2.phi()));
    double maxPtSum_pair2_deltaR = deltaR(maxPtSum_pair2lep1, maxPtSum_pair2lep2);
    double maxPtSum_pair2_deltaPt = std::abs(maxPtSum_pair2lep1.pt() - maxPtSum_pair2lep2.pt());
    double maxPtSum_pair2_m = (maxPtSum_pair2lep1 + maxPtSum_pair2lep2).mass();
    double maxSubleadPt_pair1_pt = (maxSubleadPt_pair1lep1 + maxSubleadPt_pair1lep2).pt();
    double maxSubleadPt_pair1_eta = (maxSubleadPt_pair1lep1 + maxSubleadPt_pair1lep2).eta();
    double maxSubleadPt_pair1_phi = (maxSubleadPt_pair1lep1 + maxSubleadPt_pair1lep2).phi();
    double maxSubleadPt_pair1_deltaEtaLep1 = std::abs((maxSubleadPt_pair1lep1 + maxSubleadPt_pair1lep2).eta() - lep1_eta);
    double maxSubleadPt_pair1_deltaPhiLep1 = std::abs(deltaPhi((maxSubleadPt_pair1lep1 + maxSubleadPt_pair1lep2).phi(), lep1_phi));
    double maxSubleadPt_pair1_deltaEta = std::abs(maxSubleadPt_pair1lep1.eta() - maxSubleadPt_pair1lep2.eta());
    double maxSubleadPt_pair1_deltaPhi = std::abs(deltaPhi(maxSubleadPt_pair1lep1.phi(), maxSubleadPt_pair1lep2.phi()));
    double maxSubleadPt_pair1_deltaR = deltaR(maxSubleadPt_pair1lep1, maxSubleadPt_pair1lep2);
    double maxSubleadPt_pair1_deltaPt = std::abs(maxSubleadPt_pair1lep1.pt() - maxSubleadPt_pair1lep2.pt());
    double maxSubleadPt_pair1_m = (maxSubleadPt_pair1lep1 + maxSubleadPt_pair1lep2).mass();
    double maxSubleadPt_pair2_pt = (maxSubleadPt_pair2lep1 + maxSubleadPt_pair2lep2).pt();
    double maxSubleadPt_pair2_eta = (maxSubleadPt_pair2lep1 + maxSubleadPt_pair2lep2).eta();
    double maxSubleadPt_pair2_phi = (maxSubleadPt_pair2lep1 + maxSubleadPt_pair2lep2).phi();
    double maxSubleadPt_pair2_deltaEtaLep1 = std::abs((maxSubleadPt_pair2lep1 + maxSubleadPt_pair2lep2).eta() - lep1_eta);
    double maxSubleadPt_pair2_deltaPhiLep1 = std::abs(deltaPhi((maxSubleadPt_pair2lep1 + maxSubleadPt_pair2lep2).phi(), lep1_phi));
    double maxSubleadPt_pair2_deltaEta = std::abs(maxSubleadPt_pair2lep1.eta() - maxSubleadPt_pair2lep2.eta());
    double maxSubleadPt_pair2_deltaPhi = std::abs(deltaPhi(maxSubleadPt_pair2lep1.phi(), maxSubleadPt_pair2lep2.phi()));
    double maxSubleadPt_pair2_deltaR = deltaR(maxSubleadPt_pair2lep1, maxSubleadPt_pair2lep2);
    double maxSubleadPt_pair2_deltaPt = std::abs(maxSubleadPt_pair2lep1.pt() - maxSubleadPt_pair2lep2.pt());
    double maxSubleadPt_pair2_m = (maxSubleadPt_pair2lep1 + maxSubleadPt_pair2lep2).mass();
    double minDeltaRSum_pair1_pt = (minDeltaRSum_pair1lep1 + minDeltaRSum_pair1lep2).pt();
    double minDeltaRSum_pair1_eta = (minDeltaRSum_pair1lep1 + minDeltaRSum_pair1lep2).eta();
    double minDeltaRSum_pair1_phi = (minDeltaRSum_pair1lep1 + minDeltaRSum_pair1lep2).phi();
    double minDeltaRSum_pair1_deltaEtaLep1 = std::abs((minDeltaRSum_pair1lep1 + minDeltaRSum_pair1lep2).eta() - lep1_eta);
    double minDeltaRSum_pair1_deltaPhiLep1 = std::abs(deltaPhi((minDeltaRSum_pair1lep1 + minDeltaRSum_pair1lep2).phi(), lep1_phi));
    double minDeltaRSum_pair1_deltaEta = std::abs(minDeltaRSum_pair1lep1.eta() - minDeltaRSum_pair1lep2.eta());
    double minDeltaRSum_pair1_deltaPhi = std::abs(deltaPhi(minDeltaRSum_pair1lep1.phi(), minDeltaRSum_pair1lep2.phi()));
    double minDeltaRSum_pair1_deltaR = deltaR(minDeltaRSum_pair1lep1, minDeltaRSum_pair1lep2);
    double minDeltaRSum_pair1_deltaPt = std::abs(minDeltaRSum_pair1lep1.pt() - minDeltaRSum_pair1lep2.pt());
    double minDeltaRSum_pair1_m = (minDeltaRSum_pair1lep1 + minDeltaRSum_pair1lep2).mass();
    double minDeltaRSum_pair2_pt = (minDeltaRSum_pair2lep1 + minDeltaRSum_pair2lep2).pt();
    double minDeltaRSum_pair2_eta = (minDeltaRSum_pair2lep1 + minDeltaRSum_pair2lep2).eta();
    double minDeltaRSum_pair2_phi = (minDeltaRSum_pair2lep1 + minDeltaRSum_pair2lep2).phi();
    double minDeltaRSum_pair2_deltaEtaLep1 = std::abs((minDeltaRSum_pair2lep1 + minDeltaRSum_pair2lep2).eta() - lep1_eta);
    double minDeltaRSum_pair2_deltaPhiLep1 = std::abs(deltaPhi((minDeltaRSum_pair2lep1 + minDeltaRSum_pair2lep2).phi(), lep1_phi));
    double minDeltaRSum_pair2_deltaEta = std::abs(minDeltaRSum_pair2lep1.eta() - minDeltaRSum_pair2lep2.eta());
    double minDeltaRSum_pair2_deltaPhi = std::abs(deltaPhi(minDeltaRSum_pair2lep1.phi(), minDeltaRSum_pair2lep2.phi()));
    double minDeltaRSum_pair2_deltaR = deltaR(minDeltaRSum_pair2lep1, minDeltaRSum_pair2lep2);
    double minDeltaRSum_pair2_deltaPt = std::abs(minDeltaRSum_pair2lep1.pt() - minDeltaRSum_pair2lep2.pt());
    double minDeltaRSum_pair2_m = (minDeltaRSum_pair2lep1 + minDeltaRSum_pair2lep2).mass();
    double minSubclosestDeltaR_pair1_pt = (minSubclosestDeltaR_pair1lep1 + minSubclosestDeltaR_pair1lep2).pt();
    double minSubclosestDeltaR_pair1_eta = (minSubclosestDeltaR_pair1lep1 + minSubclosestDeltaR_pair1lep2).eta();
    double minSubclosestDeltaR_pair1_phi = (minSubclosestDeltaR_pair1lep1 + minSubclosestDeltaR_pair1lep2).phi();
    double minSubclosestDeltaR_pair1_deltaEtaLep1 = std::abs((minSubclosestDeltaR_pair1lep1 + minSubclosestDeltaR_pair1lep2).eta() - lep1_eta);
    double minSubclosestDeltaR_pair1_deltaPhiLep1 = std::abs(deltaPhi((minSubclosestDeltaR_pair1lep1 + minSubclosestDeltaR_pair1lep2).phi(), lep1_phi));
    double minSubclosestDeltaR_pair1_deltaEta = std::abs(minSubclosestDeltaR_pair1lep1.eta() - minSubclosestDeltaR_pair1lep2.eta());
    double minSubclosestDeltaR_pair1_deltaPhi = std::abs(deltaPhi(minSubclosestDeltaR_pair1lep1.phi(), minSubclosestDeltaR_pair1lep2.phi()));
    double minSubclosestDeltaR_pair1_deltaR = deltaR(minSubclosestDeltaR_pair1lep1, minSubclosestDeltaR_pair1lep2);
    double minSubclosestDeltaR_pair1_deltaPt = std::abs(minSubclosestDeltaR_pair1lep1.pt() - minSubclosestDeltaR_pair1lep2.pt());
    double minSubclosestDeltaR_pair1_m = (minSubclosestDeltaR_pair1lep1 + minSubclosestDeltaR_pair1lep2).mass();
    double minSubclosestDeltaR_pair2_pt = (minSubclosestDeltaR_pair2lep1 + minSubclosestDeltaR_pair2lep2).pt();
    double minSubclosestDeltaR_pair2_eta = (minSubclosestDeltaR_pair2lep1 + minSubclosestDeltaR_pair2lep2).eta();
    double minSubclosestDeltaR_pair2_phi = (minSubclosestDeltaR_pair2lep1 + minSubclosestDeltaR_pair2lep2).phi();
    double minSubclosestDeltaR_pair2_deltaEtaLep1 = std::abs((minSubclosestDeltaR_pair2lep1 + minSubclosestDeltaR_pair2lep2).eta() - lep1_eta);
    double minSubclosestDeltaR_pair2_deltaPhiLep1 = std::abs(deltaPhi((minSubclosestDeltaR_pair2lep1 + minSubclosestDeltaR_pair2lep2).phi(), lep1_phi));
    double minSubclosestDeltaR_pair2_deltaEta = std::abs(minSubclosestDeltaR_pair2lep1.eta() - minSubclosestDeltaR_pair2lep2.eta());
    double minSubclosestDeltaR_pair2_deltaPhi = std::abs(deltaPhi(minSubclosestDeltaR_pair2lep1.phi(), minSubclosestDeltaR_pair2lep2.phi()));
    double minSubclosestDeltaR_pair2_deltaR = deltaR(minSubclosestDeltaR_pair2lep1, minSubclosestDeltaR_pair2lep2);
    double minSubclosestDeltaR_pair2_deltaPt = std::abs(minSubclosestDeltaR_pair2lep1.pt() - minSubclosestDeltaR_pair2lep2.pt());
    double minSubclosestDeltaR_pair2_m = (minSubclosestDeltaR_pair2lep1 + minSubclosestDeltaR_pair2lep2).mass();

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

      dataToMCcorrectionInterface->setLeptons({ selLepton_lead, selLepton_sublead, selLepton_third, selLepton_fourth });

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
    }
    if (leptonFakeRateInterface)
      {
	evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton_lead);
	evtWeightRecorder.record_jetToLepton_FR_sublead(leptonFakeRateInterface, selLepton_sublead);
	evtWeightRecorder.record_jetToLepton_FR_third(leptonFakeRateInterface, selLepton_third);
	evtWeightRecorder.record_jetToLepton_FR_fourth(leptonFakeRateInterface, selLepton_fourth);
      }
    if(!selectBDT){
      if(applyFakeRateWeights == kFR_4lepton)
	{
	  bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
	  bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);
	  bool passesTight_lepton_third = isMatched(*selLepton_third, tightElectrons) || isMatched(*selLepton_third, tightMuons);
	  bool passesTight_lepton_fourth = isMatched(*selLepton_fourth, tightElectrons) || isMatched(*selLepton_fourth, tightMuons);
	  evtWeightRecorder.compute_FR_4l(passesTight_lepton_lead, passesTight_lepton_sublead, passesTight_lepton_third, passesTight_lepton_fourth);
	}
    }

    // require that trigger paths match lepton flavor (for fakeable leptons)
    if ( !((fakeableElectrons.size() >= 3 &&                              (selTrigger_3e    || selTrigger_2e  || selTrigger_1e                                      )) ||
	   (fakeableElectrons.size() >= 2 && fakeableMuons.size() >= 1 && (selTrigger_2e1mu || selTrigger_2e  || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 2 && (selTrigger_1e2mu || selTrigger_2mu || selTrigger_1e1mu || selTrigger_1mu || selTrigger_1e)) ||
	   (                                 fakeableMuons.size() >= 3 && (selTrigger_3mu   || selTrigger_2mu || selTrigger_1mu                                     ))) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS trigger selection for given fakeableLepton multiplicity." << std::endl;
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
    cutFlowTable.update("trigger & fakeable lepton flavor matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger & fakeable lepton flavor matching", evtWeightRecorder.get(central_or_shift_main));

    // Require that trigger paths match primary datasets,
    // to avoid that the same event is selected multiple times when processing different primary datasets (PD).
    // In case the same event passes the triggers paths for more than one primary datasets,
    // the event is selected in the PD of highest priority only. 
    // The ranking of the PDs is as follows: DoubleMuon, MuonEG, DoubleEG, SingleMuon, SingleElectron
    if ( !isMC && !isDEBUG ) 
    {
      //bool isTriggered_SingleElectron = isTriggered_1e && fakeableElectrons.size() >= 1;
      bool isTriggered_SingleMuon = isTriggered_1mu && fakeableMuons.size() >= 1;
      bool isTriggered_DoubleEG = (isTriggered_2e && fakeableElectrons.size() >= 2) || 
                                  (isTriggered_3e && fakeableElectrons.size() >= 3);
      bool isTriggered_DoubleMuon = (isTriggered_2mu && fakeableMuons.size() >= 2) || 
                                    (isTriggered_3mu && fakeableMuons.size() >= 3);
      bool isTriggered_MuonEG = (isTriggered_1e1mu && fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 1) || 
                                (isTriggered_2e1mu && fakeableElectrons.size() >= 2 && fakeableMuons.size() >= 1) || 
                                (isTriggered_1e2mu && fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 2);

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
    cutFlowTable.update("trigger & dataset matching", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("trigger & dataset matching", evtWeightRecorder.get(central_or_shift_main));

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
      if(! hltFilter(trigger_bits, fakeableLeptons, {}))
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
    const double minPt_third = 15.;
    const double minPt_fourth = 10.;
    // CV: according to Giovanni, the pT cuts should be applied on cone_pt
    //    (combined efficiency of single lepton, double lepton, and triple lepton triggers assumed to be high,
    //     even if one or two leptons and fakes and hence cone_pt may be significantly smaller than lepton_pt,
    //     on which pT cuts are applied on trigger level)
    if ( !(selLepton_lead->cone_pt() > minPt_lead && selLepton_sublead->cone_pt() > minPt_sublead &&
           selLepton_third->cone_pt() > minPt_third && selLepton_fourth->cone_pt() > minPt_fourth) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS lepton pT selection." << std::endl;
	std::cout << " (leading selLepton pT = " << selLepton_lead->pt() << ", minPt_lead = " << minPt_lead
		  << ", subleading selLepton pT = " << selLepton_sublead->pt() << ", minPt_sublead = " << minPt_sublead
		  << ", third selLepton pT = " << selLepton_third->pt() << ", minPt_third = " << minPt_third 
		  << ", fourth selLepton pT = " << selLepton_fourth->pt() << ", minPt_fourth = " << minPt_fourth << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 15 GeV && fourth lepton pT > 10 GeV", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 15 GeV && fourth lepton pT > 10 GeV", evtWeightRecorder.get(central_or_shift_main));

    int sumLeptonCharge = selLepton_lead->charge() + selLepton_sublead->charge() + selLepton_third->charge() + selLepton_fourth->charge();
    bool isCharge_SS = std::abs(sumLeptonCharge) >  1;
    bool isCharge_OS = std::abs(sumLeptonCharge) <= 1;
    if ( leptonChargeSelection == kOS && isCharge_SS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge() 
		  << ", fourth selLepton charge = " << selLepton_fourth->charge() << ", leptonChargeSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( leptonChargeSelection == kSS && isCharge_OS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge() 
		  << ", fourth selLepton charge = " << selLepton_fourth->charge() << ", leptonChargeSelection = SS)" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("sel lepton charge", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel lepton charge", evtWeightRecorder.get(central_or_shift_main));

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
    
    const bool failsHtoZZVeto = isfailsHtoZZVeto(preselLeptonsFull);
    if ( failsHtoZZVeto ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS H->ZZ*->4l veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("H->ZZ*->4l veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("H->ZZ*->4l veto", evtWeightRecorder.get(central_or_shift_main));

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
    if ( isMCClosure_e || isMCClosure_m ) {
      bool applySignalRegionVeto = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      if ( applySignalRegionVeto && tightLeptons.size() >= 4 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable ) {
      if ( tightLeptons.size() >= 4 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
	             "# tight leptons = " << tightLeptons.size() << " >= 4\n"
        ;
	printCollection("tightLeptons", tightLeptons);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("signal region veto", evtWeightRecorder.get(central_or_shift_main));

    if(blacklist && (*blacklist)(eventInfo))
    {
      continue;
    }

    // std::vector<SVfit4tauResult> svFit4tauResults_wMassConstraint = compSVfit4tau(
    //   *selLepton_lead, *selLepton_sublead, *selLepton_third, *selLepton_fourth, met, leptonChargeSelection_string, rnd, 125., 2.);
        
    double dihiggsVisMass_sel = (selLepton_lead->cone_p4() + selLepton_sublead->cone_p4() + selLepton_third->cone_p4() + selLepton_fourth->cone_p4()).mass();
    double dihiggsMass = -10; // ( svFit4tauResults_wMassConstraint.size() >= 1 && svFit4tauResults_wMassConstraint[0].isValidSolution_ ) ? 
    //   svFit4tauResults_wMassConstraint[0].dihiggs_mass_ : -1.;

//--- retrieve gen-matching flags
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons);

    //Gathering final BDT Inputs
    
    AllVars_Map["gen_mHH"] = 250.; // setting a Dummy value which will be reset depending on mass hypothesis
    AllVars_Map["numJets"] = selJets.size();                                   
    AllVars_Map["numElectrons"] = selElectrons.size();                         
    AllVars_Map["numMuons"] = selMuons.size();
    AllVars_Map["numLeptons"] = selLeptons.size();
    AllVars_Map["numBJets_loose"] = selBJets_loose.size();                     
    AllVars_Map["numBJets_medium"] = selBJets_medium.size();                   
    AllVars_Map["dihiggsVisMass_sel"] = dihiggsVisMass_sel;                   
    AllVars_Map["dihiggsMass"] = dihiggsMass;                   
    AllVars_Map["HT"] = HT;                                                    
    AllVars_Map["STMET"] = STMET;                                              
    AllVars_Map["lep1_pt"] = lep1_pt;                                          
    AllVars_Map["lep2_pt"] = lep2_pt;                                          
    AllVars_Map["lep3_pt"] = lep3_pt;                                          
    AllVars_Map["lep4_pt"] = lep4_pt;                                          
    AllVars_Map["lep1_conePt"] = lep1_conePt;                                  
    AllVars_Map["lep2_conePt"] = lep2_conePt;                                  
    AllVars_Map["lep3_conePt"] = lep3_conePt;                                  
    AllVars_Map["lep4_conePt"] = lep4_conePt;                                  
    AllVars_Map["lep1_eta"] = lep1_eta;                                       
    AllVars_Map["lep2_eta"] = lep2_eta;                                        
    AllVars_Map["lep3_eta"] = lep3_eta;                                        
    AllVars_Map["lep4_eta"] = lep4_eta;                                        
    AllVars_Map["lep1_phi"] = lep1_phi;                                        
    AllVars_Map["lep2_phi"] = lep2_phi;                                        
    AllVars_Map["lep3_phi"] = lep3_phi;                                        
    AllVars_Map["lep4_phi"] = lep4_phi;
    AllVars_Map["lep1_dxy"] = lep1_dxy;
    AllVars_Map["lep2_dxy"] = lep2_dxy;
    AllVars_Map["lep3_dxy"] = lep3_dxy;
    AllVars_Map["lep4_dxy"] = lep4_dxy;
    AllVars_Map["lep1_dz"] = lep1_dz;
    AllVars_Map["lep2_dz"] = lep2_dz;
    AllVars_Map["lep3_dz"] = lep3_dz;
    AllVars_Map["lep4_dz"] = lep4_dz;
    AllVars_Map["pt4l"] = pt4l;
    AllVars_Map["pt4lParallelHadT"] = pt4lParallelHadT;
    AllVars_Map["pt4lPerpendicularHadT"] = pt4lPerpendicularHadT;
    AllVars_Map["mt4l"] = mt4l;
    AllVars_Map["maxPtSum_pair1_pt"] = maxPtSum_pair1_pt;
    AllVars_Map["maxPtSum_pair1_eta"] = maxPtSum_pair1_eta;
    AllVars_Map["maxPtSum_pair1_phi"] = maxPtSum_pair1_phi;                               
    AllVars_Map["maxPtSum_pair1_deltaEtaLep1"] = maxPtSum_pair1_deltaEtaLep1;             
    AllVars_Map["maxPtSum_pair1_deltaPhiLep1"] = maxPtSum_pair1_deltaPhiLep1;             
    AllVars_Map["maxPtSum_pair1_deltaEta"] = maxPtSum_pair1_deltaEta;                     
    AllVars_Map["maxPtSum_pair1_deltaPhi"] = maxPtSum_pair1_deltaPhi;                     
    AllVars_Map["maxPtSum_pair1_deltaR"] = maxPtSum_pair1_deltaR;                         
    AllVars_Map["maxPtSum_pair1_deltaPt"] = maxPtSum_pair1_deltaPt;                       
    AllVars_Map["maxPtSum_pair1_m"] = maxPtSum_pair1_m;                                   
    AllVars_Map["maxPtSum_pair2_pt"] = maxPtSum_pair2_pt;                                 
    AllVars_Map["maxPtSum_pair2_eta"] = maxPtSum_pair2_eta;                                
    AllVars_Map["maxPtSum_pair2_phi"] = maxPtSum_pair2_phi;                               
    AllVars_Map["maxPtSum_pair2_deltaEtaLep1"] = maxPtSum_pair2_deltaEtaLep1;             
    AllVars_Map["maxPtSum_pair2_deltaPhiLep1"] = maxPtSum_pair2_deltaPhiLep1;             
    AllVars_Map["maxPtSum_pair2_deltaEta"] = maxPtSum_pair2_deltaEta;                     
    AllVars_Map["maxPtSum_pair2_deltaPhi"] = maxPtSum_pair2_deltaPhi;                     
    AllVars_Map["maxPtSum_pair2_deltaR"] = maxPtSum_pair2_deltaR;                         
    AllVars_Map["maxPtSum_pair2_deltaPt"] = maxPtSum_pair2_deltaPt;                       
    AllVars_Map["maxPtSum_pair2_m"] = maxPtSum_pair2_m;
    AllVars_Map["MET"] = MET;
    AllVars_Map["METParallelHadT"] = METParallelHadT;
    AllVars_Map["METPerpendicularHadT"] = METPerpendicularHadT;
    AllVars_Map["METPhi"] = METPhi;                                                                 
    AllVars_Map["METDeltaPhiLep1"] = METDeltaPhiLep1;                                               
    AllVars_Map["MET_LD"] = met_LD;                                                                 
    AllVars_Map["HTmiss"] = HTmiss;                                                                 
    AllVars_Map["lep1_isElectron"] = lep1_isElectron;                                               
    AllVars_Map["lep1_charge"] = lep1_charge;                                                       
    AllVars_Map["lep2_isElectron"] = lep2_isElectron;                                               
    AllVars_Map["lep2_charge"] = lep2_charge;                                                       
    AllVars_Map["lep3_isElectron"] = lep3_isElectron;                                               
    AllVars_Map["lep3_charge"] = lep3_charge;                                                       
    AllVars_Map["lep4_isElectron"] = lep4_isElectron;                                               
    AllVars_Map["lep4_charge"] = lep4_charge;                                                       
    AllVars_Map["electronChargeSum"] = electronChargeSum;                                           
    AllVars_Map["muonChargeSum"] = muonChargeSum;                                                   
    AllVars_Map["nSFOS"] = nSFOS;


    std::map<std::string, double> BDTInputs_spin2 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_spin2, false);
    std::map<std::string, double> BDTInputs_spin0 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_spin0, false);
    std::map<std::string, double> BDTInputs_nonRes = InitializeInputVarMap(AllVars_Map, BDTInputVariables_nonRes, true); // Include all Input Var.s except BM indices
//    std::map<std::string, double> BDTInputs_nonRes_base = InitializeInputVarMap(AllVars_Map, BDTInputVariables_nonRes_base, true);

//    std::vector<double> nonResBase_params;
//    nonResBase_params.push_back(0.);

    BDTOutput_Map_spin2 = CreateResonantBDTOutputMap(gen_mHH, BDT_spin2, BDTInputs_spin2, eventInfo.event, "_spin2");
    BDTOutput_Map_spin0 = CreateResonantBDTOutputMap(gen_mHH, BDT_spin0, BDTInputs_spin0, eventInfo.event, "_spin0");
    BDTOutput_Map_nonRes = CreateNonResonantBDTOutputMap(nonRes_BMs, BDT_nonRes, BDTInputs_nonRes, eventInfo.event, hhWeight_couplings);
//    BDTOutput_Map_nonRes_base = CreateBDTOutputMap(nonResBase_params, BDT_nonRes_base, BDTInputs_nonRes_base, eventInfo.event, true, "_base");

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
          selHistManager->jets_->fillHistograms(selJets, evtWeight);
          selHistManager->BJets_loose_->fillHistograms(selBJets_loose, evtWeight);
          selHistManager->BJets_medium_->fillHistograms(selBJets_medium, evtWeight);
          selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
          // selHistManager->svFit4tau_wMassConstraint_->fillHistograms(svFit4tauResults_wMassConstraint, evtWeight);
        }

	selHistManager->evt_->fillHistograms(selElectrons.size(), selMuons.size(), selLeptons.size(), selJets.size(), numSelJetsPtGt40, selBJets_loose.size(), selBJets_medium.size(), dihiggsVisMass_sel, dihiggsMass, HT, STMET, lep1_pt, lep2_pt, lep3_pt, lep4_pt, lep1_conePt, lep2_conePt, lep3_conePt, lep4_conePt, lep1_eta, lep2_eta, lep3_eta, lep4_eta, lep1_phi, lep2_phi, lep3_phi, lep4_phi, lep1_dxy, lep2_dxy, lep3_dxy, lep4_dxy, lep1_dz, lep2_dz, lep3_dz, lep4_dz, pt4l, pt4lParallelHadT, pt4lPerpendicularHadT, mt4l, maxPtSum_pair1_pt, maxPtSum_pair1_eta, maxPtSum_pair1_phi, maxPtSum_pair1_deltaEtaLep1, maxPtSum_pair1_deltaPhiLep1, maxPtSum_pair1_deltaEta, maxPtSum_pair1_deltaPhi, maxPtSum_pair1_deltaR, maxPtSum_pair1_deltaPt, maxPtSum_pair1_m, maxPtSum_pair2_pt, maxPtSum_pair2_eta, maxPtSum_pair2_phi, maxPtSum_pair2_deltaEtaLep1, maxPtSum_pair2_deltaPhiLep1, maxPtSum_pair2_deltaEta, maxPtSum_pair2_deltaPhi, maxPtSum_pair2_deltaR,maxPtSum_pair2_deltaPt, maxPtSum_pair2_m,MET, METParallelHadT, METPerpendicularHadT, METPhi, METDeltaPhiLep1, met_LD, HTmiss, lep1_isElectron, lep1_charge, lep2_isElectron, lep2_charge, lep3_isElectron, lep3_charge, lep4_isElectron, lep4_charge, leptonChargeSum, electronChargeSum, muonChargeSum, nSFOS, evtWeight);
	
        selHistManager->datacard_->fillHistograms(
						  BDTOutput_Map_spin2,
						  BDTOutput_Map_spin0,
						  BDTOutput_Map_nonRes,
//						  BDTOutput_Map_nonRes_base["Base"],
                                                  -1., // CV: BDTOutput for nonresonant_allBMs case not implemented yet !!
						  evtWeight);

        if(! skipFilling)
        {
          selHistManager->evtYield_->fillHistograms(eventInfo, evtWeight);
          selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
          selHistManager->weights_->fillHistograms("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift));
          selHistManager->weights_->fillHistograms("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift));
          selHistManager->weights_->fillHistograms("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift));
          selHistManager->weights_->fillHistograms("fakeRate", evtWeightRecorder.get_FR(central_or_shift));
        }
      }

      if(isMC && ! skipFilling)
      {
        genEvtHistManager_afterCuts[central_or_shift]->fillHistograms(
          genElectrons, genMuons, genHadTaus, genPhotonsFinal, genJets, evtWeightRecorder.get_inclusive(central_or_shift)
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

    if(bdt_filler)
    {
      double lep1_genLepPt = ( selLepton_lead->genLepton()    ) ? selLepton_lead->genLepton()->pt()    : 0.;
      double lep2_genLepPt = ( selLepton_sublead->genLepton() ) ? selLepton_sublead->genLepton()->pt() : 0.;
      double lep3_genLepPt = ( selLepton_third->genLepton()   ) ? selLepton_third->genLepton()->pt()   : 0.;
      double lep4_genLepPt = ( selLepton_fourth->genLepton()   ) ? selLepton_fourth->genLepton()->pt()   : 0.;

      double prob_fake_lepton_lead = evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
      double prob_fake_lepton_sublead = evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);
      double prob_fake_lepton_third = evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main);
      double prob_fake_lepton_fourth = evtWeightRecorder.get_jetToLepton_FR_fourth(central_or_shift_main);

      double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
      double lep1_frWeight = lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead;
      double lep2_frWeight = lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead;
      double lep3_frWeight = lep3_genLepPt > 0 ? 1.0 : prob_fake_lepton_third;
      double lep4_frWeight = lep4_genLepPt > 0 ? 1.0 : prob_fake_lepton_fourth;
      evtWeight_BDT *= lep1_frWeight*lep2_frWeight*lep3_frWeight*lep4_frWeight;

      std::map<std::string, double> weightMapHH;
      if ( apply_HH_rwgt_lo || apply_HH_rwgt_nlo )
      {
        for ( unsigned int i = 0; i < HHWeightNames.size(); i++ )
        {
          double HHReweight = 1.;
          if ( apply_HH_rwgt_lo )
          {
            assert(HHWeightLO_calc);
            HHReweight *= HHWeightLO_calc->getRelativeWeight(HHBMNames[i], eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
          }
          if ( apply_HH_rwgt_nlo )
          {
            assert(HHWeightNLO_calc);
            HHReweight *= HHWeightNLO_calc->getRelativeWeight_LOtoNLO(HHBMNames[i], eventInfo.gen_mHH, eventInfo.gen_cosThetaStar, isDEBUG);
          }
          weightMapHH[HHWeightNames[i]] = HHReweight;
        }
      }

      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
	("lep1_frWeight",       lep1_frWeight)
	("lep2_frWeight",       lep2_frWeight)
	("lep3_frWeight",       lep3_frWeight)
	("lep4_frWeight",       lep4_frWeight)
	("genWeight" , eventInfo.genWeight)
	("lheWeight" , evtWeightRecorder.get_lheScaleWeight(central_or_shift_main))
	("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift_main))
	("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift_main))
	("btagWeight", evtWeightRecorder.get_btag(central_or_shift_main))
	("leptonEffSF", evtWeightRecorder.get_leptonSF())
	("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift_main))
	("FR_Weight", evtWeightRecorder.get_FR(central_or_shift_main))
	("evtWeight", evtWeight_BDT)                                  
	(weightMapHH)                                                 
	("numJets", selJets.size())                                   
	("numElectrons", selElectrons.size())                         
	("numMuons", selMuons.size())
	("numLeptons", selLeptons.size())
	("numSelJetsPtGt40", numSelJetsPtGt40)                        
	("numBJets_loose", selBJets_loose.size())                     
	("numBJets_medium", selBJets_medium.size())                   
	("dihiggsVisMass_sel", dihiggsVisMass_sel)                    
	("dihiggsMass", dihiggsMass)                                  
	("HT", HT)                                                    
	("STMET", STMET)                                              
	("lep1_pt", lep1_pt)                                          
	("lep2_pt", lep2_pt)                                          
	("lep3_pt", lep3_pt)                                          
	("lep4_pt", lep4_pt)                                          
	("lep1_conePt", lep1_conePt)                                  
	("lep2_conePt", lep2_conePt)                                  
	("lep3_conePt", lep3_conePt)                                  
	("lep4_conePt", lep4_conePt)                                  
	("lep1_eta", lep1_eta)                                        
	("lep2_eta", lep2_eta)                                        
	("lep3_eta", lep3_eta)                                        
	("lep4_eta", lep4_eta)                                        
	("lep1_phi", lep1_phi)                                        
	("lep2_phi", lep2_phi)                                        
	("lep3_phi", lep3_phi)                                        
	("lep4_phi", lep4_phi)
	("lep1_dxy", lep1_dxy)
	("lep2_dxy", lep2_dxy)
	("lep3_dxy", lep3_dxy)
	("lep4_dxy", lep4_dxy)
	("lep1_dz", lep1_dz)
	("lep2_dz", lep2_dz)
	("lep3_dz", lep3_dz)
	("lep4_dz", lep4_dz)
	("pt4l", pt4l)
	("pt4lParallelHadT", pt4lParallelHadT)
	("pt4lPerpendicularHadT", pt4lPerpendicularHadT)
	("mt4l", mt4l)
	("maxPtSum_pair1_pt", maxPtSum_pair1_pt)   
	("maxPtSum_pair1_eta", maxPtSum_pair1_eta)                               
	("maxPtSum_pair1_phi", maxPtSum_pair1_phi)                               
	("maxPtSum_pair1_deltaEtaLep1", maxPtSum_pair1_deltaEtaLep1)             
	("maxPtSum_pair1_deltaPhiLep1", maxPtSum_pair1_deltaPhiLep1)             
	("maxPtSum_pair1_deltaEta", maxPtSum_pair1_deltaEta)                     
	("maxPtSum_pair1_deltaPhi", maxPtSum_pair1_deltaPhi)                     
	("maxPtSum_pair1_deltaR", maxPtSum_pair1_deltaR)                         
	("maxPtSum_pair1_deltaPt", maxPtSum_pair1_deltaPt)                       
	("maxPtSum_pair1_m", maxPtSum_pair1_m)                                   
	("maxPtSum_pair2_pt", maxPtSum_pair2_pt)                                 
	("maxPtSum_pair2_eta", maxPtSum_pair2_eta)                               
	("maxPtSum_pair2_phi", maxPtSum_pair2_phi)                               
	("maxPtSum_pair2_deltaEtaLep1", maxPtSum_pair2_deltaEtaLep1)             
	("maxPtSum_pair2_deltaPhiLep1", maxPtSum_pair2_deltaPhiLep1)             
	("maxPtSum_pair2_deltaEta", maxPtSum_pair2_deltaEta)                     
	("maxPtSum_pair2_deltaPhi", maxPtSum_pair2_deltaPhi)                     
	("maxPtSum_pair2_deltaR", maxPtSum_pair2_deltaR)                         
	("maxPtSum_pair2_deltaPt", maxPtSum_pair2_deltaPt)                       
	("maxPtSum_pair2_m", maxPtSum_pair2_m)                                   
	("maxSubleadPt_pair1_pt", maxSubleadPt_pair1_pt)                         
	("maxSubleadPt_pair1_eta", maxSubleadPt_pair1_eta)                       
	("maxSubleadPt_pair1_phi", maxSubleadPt_pair1_phi)                       
	("maxSubleadPt_pair1_deltaEtaLep1", maxSubleadPt_pair1_deltaEtaLep1)     
	("maxSubleadPt_pair1_deltaPhiLep1", maxSubleadPt_pair1_deltaPhiLep1)     
	("maxSubleadPt_pair1_deltaEta", maxSubleadPt_pair1_deltaEta)             
	("maxSubleadPt_pair1_deltaPhi", maxSubleadPt_pair1_deltaPhi)             
	("maxSubleadPt_pair1_deltaR", maxSubleadPt_pair1_deltaR)                 
	("maxSubleadPt_pair1_deltaPt", maxSubleadPt_pair1_deltaPt)               
	("maxSubleadPt_pair1_m", maxSubleadPt_pair1_m)                           
	("maxSubleadPt_pair2_pt", maxSubleadPt_pair2_pt)                         
	("maxSubleadPt_pair2_eta", maxSubleadPt_pair2_eta)                       
	("maxSubleadPt_pair2_phi", maxSubleadPt_pair2_phi)                       
	("maxSubleadPt_pair2_deltaEtaLep1", maxSubleadPt_pair2_deltaEtaLep1)     
	("maxSubleadPt_pair2_deltaPhiLep1", maxSubleadPt_pair2_deltaPhiLep1)     
	("maxSubleadPt_pair2_deltaEta", maxSubleadPt_pair2_deltaEta)             
	("maxSubleadPt_pair2_deltaPhi", maxSubleadPt_pair2_deltaPhi)             
	("maxSubleadPt_pair2_deltaR", maxSubleadPt_pair2_deltaR)                 
	("maxSubleadPt_pair2_deltaPt", maxSubleadPt_pair2_deltaPt)               
	("maxSubleadPt_pair2_m", maxSubleadPt_pair2_m)                           
	("minDeltaRSum_pair1_pt", minDeltaRSum_pair1_pt)                         
	("minDeltaRSum_pair1_eta", minDeltaRSum_pair1_eta)                       
	("minDeltaRSum_pair1_phi", minDeltaRSum_pair1_phi)                       
	("minDeltaRSum_pair1_deltaEtaLep1", minDeltaRSum_pair1_deltaEtaLep1)     
	("minDeltaRSum_pair1_deltaPhiLep1", minDeltaRSum_pair1_deltaPhiLep1)     
	("minDeltaRSum_pair1_deltaEta", minDeltaRSum_pair1_deltaEta)             
	("minDeltaRSum_pair1_deltaPhi", minDeltaRSum_pair1_deltaPhi)             
	("minDeltaRSum_pair1_deltaR", minDeltaRSum_pair1_deltaR)                 
	("minDeltaRSum_pair1_deltaPt", minDeltaRSum_pair1_deltaPt)               
	("minDeltaRSum_pair1_m", minDeltaRSum_pair1_m)                           
	("minDeltaRSum_pair2_pt", minDeltaRSum_pair2_pt)                         
	("minDeltaRSum_pair2_eta", minDeltaRSum_pair2_eta)                       
	("minDeltaRSum_pair2_phi", minDeltaRSum_pair2_phi)                       
	("minDeltaRSum_pair2_deltaEtaLep1", minDeltaRSum_pair2_deltaEtaLep1)     
	("minDeltaRSum_pair2_deltaPhiLep1", minDeltaRSum_pair2_deltaPhiLep1)     
	("minDeltaRSum_pair2_deltaEta", minDeltaRSum_pair2_deltaEta)             
	("minDeltaRSum_pair2_deltaPhi", minDeltaRSum_pair2_deltaPhi)             
	("minDeltaRSum_pair2_deltaR", minDeltaRSum_pair2_deltaR)                 
	("minDeltaRSum_pair2_deltaPt", minDeltaRSum_pair2_deltaPt)               
	("minDeltaRSum_pair2_m", minDeltaRSum_pair2_m)                           
	("minSubclosestDeltaR_pair1_pt", minSubclosestDeltaR_pair1_pt)           
	("minSubclosestDeltaR_pair1_eta", minSubclosestDeltaR_pair1_eta)         
	("minSubclosestDeltaR_pair1_phi", minSubclosestDeltaR_pair1_phi)         
	("minSubclosestDeltaR_pair1_deltaEtaLep1", minSubclosestDeltaR_pair1_deltaEtaLep1) 
	("minSubclosestDeltaR_pair1_deltaPhiLep1", minSubclosestDeltaR_pair1_deltaPhiLep1) 
	("minSubclosestDeltaR_pair1_deltaEta", minSubclosestDeltaR_pair1_deltaEta)         
	("minSubclosestDeltaR_pair1_deltaPhi", minSubclosestDeltaR_pair1_deltaPhi)         
	("minSubclosestDeltaR_pair1_deltaR", minSubclosestDeltaR_pair1_deltaR)             
	("minSubclosestDeltaR_pair1_deltaPt", minSubclosestDeltaR_pair1_deltaPt)           
	("minSubclosestDeltaR_pair1_m", minSubclosestDeltaR_pair1_m)                       
	("minSubclosestDeltaR_pair2_pt", minSubclosestDeltaR_pair2_pt)                     
	("minSubclosestDeltaR_pair2_eta", minSubclosestDeltaR_pair2_eta)                   
	("minSubclosestDeltaR_pair2_phi", minSubclosestDeltaR_pair2_phi)                   
	("minSubclosestDeltaR_pair2_deltaEtaLep1", minSubclosestDeltaR_pair2_deltaEtaLep1) 
	("minSubclosestDeltaR_pair2_deltaPhiLep1", minSubclosestDeltaR_pair2_deltaPhiLep1) 
	("minSubclosestDeltaR_pair2_deltaEta", minSubclosestDeltaR_pair2_deltaEta)         
	("minSubclosestDeltaR_pair2_deltaPhi", minSubclosestDeltaR_pair2_deltaPhi)         
	("minSubclosestDeltaR_pair2_deltaR", minSubclosestDeltaR_pair2_deltaR)             
	("minSubclosestDeltaR_pair2_deltaPt", minSubclosestDeltaR_pair2_deltaPt)           
	("minSubclosestDeltaR_pair2_m", minSubclosestDeltaR_pair2_m)                       
	("MET", MET)
	("METParallelHadT", METParallelHadT)
	("METPerpendicularHadT", METPerpendicularHadT)
	("METPhi", METPhi)                                                                 
	("METDeltaPhiLep1", METDeltaPhiLep1)                                               
	("MET_LD", met_LD)                                                                 
	("HTmiss", HTmiss)                                                                 
	("lep1_isElectron", lep1_isElectron)                                               
	("lep1_charge", lep1_charge)                                                       
	("lep2_isElectron", lep2_isElectron)                                               
	("lep2_charge", lep2_charge)                                                       
	("lep3_isElectron", lep3_isElectron)                                               
	("lep3_charge", lep3_charge)                                                       
	("lep4_isElectron", lep4_isElectron)                                               
	("lep4_charge", lep4_charge)                                                       
	("leptonChargeSum", leptonChargeSum)                                               
	("electronChargeSum", electronChargeSum)                                           
	("muonChargeSum", muonChargeSum)                                                   
	("nSFOS", nSFOS)                                                                   
        .fill()
        ;

    }

    ++selectedEntries;    
    selectedEntries_weighted += evtWeightRecorder.get(central_or_shift_main);
    std::string process_and_genMatch = process_string;
    process_and_genMatch += selLepton_genMatch.name_;
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
  cutFlowTable.print(std::cout);
  std::cout << std::endl;

  std::cout << "sel. Entries by gen. matching:" << std::endl;
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    std::cout << "central_or_shift = " << central_or_shift << '\n';
    for(const leptonGenMatchEntry & leptonGenMatch_definition: leptonGenMatch_definitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += leptonGenMatch_definition.name_;
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

  delete leptonFakeRateInterface;

  delete run_lumi_eventSelector;
  delete blacklist;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete jetReader;
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genProxyPhotonReader;
  delete genFromHardProcessReader;
  delete genJetReader;
  delete lheInfoReader;
  delete psWeightReader;

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

  clock.Show("analyze_hh_4l");

  return EXIT_SUCCESS;
}
