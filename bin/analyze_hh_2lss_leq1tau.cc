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

#include <TLorentzVector.h> // TLorentzVector
#include <TVector3.h>
#include <TBenchmark.h> // TBenchmark
#include <TString.h> // TString, Form
#include <TError.h> // gErrorAbortLevel, kError
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
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarCorrelationHistManager.h" // MVAInputVarCorrelationHistManager, getKeys()
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_3lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // comp_lep1_conePt, comp_lep2_conePt
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
#include "tthAnalysis/HiggsToTauTau/interface/ChargeMisIdRate.h" // ChargeMisIdRate
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface 
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceLO.h" // HHWeightInterfaceLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceNLO.h" // HHWeightInterfaceNLO
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterfaceCouplings.h" // HHWeightInterfaceCouplings
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertex.h" // RecoVertex
#include "tthAnalysis/HiggsToTauTau/interface/RecoVertexReader.h" // RecoVertexReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonFilter.h" // GenPhotonFilter
#include "tthAnalysis/HiggsToTauTau/interface/RunLumiEventRejector.h" // RunLumiEventRejector

#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorAK8.h" // RecoJetSelectorAK8
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_2lss_leq1tau.h" // EvtHistManager_hh_2lss_leq1tau
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH
#include "hhAnalysis/multilepton/interface/AnalysisConfig_hh.h" // AnalysisConfig_hh
#include "hhAnalysis/multilepton/interface/DatacardHistManager_hh.h" // DatacardHistManager_hh
#include "hhAnalysis/multilepton/interface/HHGenKinematicsHistManager.h" // HHGenKinematicsHistManager

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

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

enum { kFR_disabled, kFR_2lepton };

//const int hadTauSelection_antiElectron = 1; // vLoose
//const int hadTauSelection_antiMuon = 1; // Loose
const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied

const int printLevel = 1;


double calculateAbsDeltaPhi(double phi1, double phi2)
{
  double dPhi = std::abs(phi1 - phi2);
  if (dPhi > TMath::Pi()) dPhi = 2*TMath::Pi() - dPhi;
  return dPhi;
}

bool hasOverlapJets(const RecoJet *jet, std::vector<const RecoSubjetAK8*> selSubjetsAK8) {
  bool hasOverlap = false;
  for (size_t i=0; i < selSubjetsAK8.size(); i++) {
    if (deltaR(jet->p4(), selSubjetsAK8[i]->p4()) < 0.3) hasOverlap = true;
  }
  return hasOverlap;
}

void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& particles)
{
  for ( size_t idxParticle = 0; idxParticle < particles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << particles[idxParticle];
    std::cout << std::endl;
  }
}

void printWjj(const std::vector<const RecoJetAK8*>& jets_ak8, const RecoJetCollectionSelectorAK8_hh_Wjj& jetSelectorAK8_Wjj, 
	      const std::vector<GenParticle>& genWBosons, const std::vector<GenParticle>& genWJets)
{
  std::cout << "<printWjj>:" << std::endl;
  std::cout << "#genWBosons = " << genWBosons.size() << std::endl;
  for ( size_t idxWBoson = 0; idxWBoson < genWBosons.size(); ++idxWBoson ) {
    const GenParticle& genWBoson = genWBosons[idxWBoson];
    std::cout << " genWBoson #" << idxWBoson << ": pT = " << genWBoson.pt() << ", eta = " << genWBoson.eta() << ", phi = " << genWBoson.phi() << std::endl;   
  }
  std::cout << "#genWJets = " << genWJets.size() << std::endl;  
  for ( size_t idxWJet = 0; idxWJet < genWJets.size(); ++idxWJet ) {
    const GenParticle& genWJet = genWJets[idxWJet];
    std::cout << " genWJet #" << idxWJet << ": pT = " << genWJet.pt() << ", eta = " << genWJet.eta() << ", phi = " << genWJet.phi() << std::endl;   
  }
  if ( genWBosons.size() == 1 ) {
    bool isMatched = false;
    Particle::LorentzVector genWjjP4 = genWBosons[0].p4();
    std::cout << "genWjj: pT = " << genWjjP4.pt() << ", eta = " << genWjjP4.eta() << ", phi = " << genWjjP4.phi() << std::endl;
    for ( std::vector<const RecoJetAK8*>::const_iterator jet_ak8 = jets_ak8.begin();
	  jet_ak8 != jets_ak8.end(); ++jet_ak8 ) {
      double dR = deltaR(genWjjP4, (*jet_ak8)->p4());
      if ( dR < 0.8 ) {
	std::cout << "matches reconstructed AK8 jet: pT = " << (*jet_ak8)->pt() << ", eta = " << (*jet_ak8)->eta() << ", phi = " << (*jet_ak8)->phi() << ","
		  << " msoftdrop = " << (*jet_ak8)->msoftdrop() << ", tau21 = " << (*jet_ak8)->tau2()/(*jet_ak8)->tau1() << ", which ";
	if ( jetSelectorAK8_Wjj.getSelector()(**jet_ak8) ) {
	  std::cout << "PASSES";
	  isMatched = true;
	} else { 
	  std::cout << "FAILS";
	}
	std::cout << " the W->jj jet selection." << std::endl;
	std::cout << "generator-level subjets:" << std::endl;
	for ( std::vector<GenParticle>::const_iterator genWJet1 = genWJets.begin();
	      genWJet1 != genWJets.end(); ++genWJet1 ) {
	  for ( std::vector<GenParticle>::const_iterator genWJet2 = genWJet1 + 1;
		genWJet2 != genWJets.end(); ++genWJet2 ) {
	    if ( deltaR(genWJet1->p4() + genWJet2->p4(), genWjjP4) < 1.e-1 && std::fabs((genWJet1->p4() + genWJet2->p4()).mass() - genWjjP4.mass()) < 1.e+1 ) {
	      std::cout << " genWJet #1: pT = " << genWJet1->pt() << ", eta = " << genWJet1->eta() << ", phi = " << genWJet1->phi() << std::endl;   
	      std::cout << " genWJet #2: pT = " << genWJet2->pt() << ", eta = " << genWJet2->eta() << ", phi = " << genWJet2->phi() << std::endl;   
	    }
	  } 
	}  
	std::cout << "reconstructed subjets:" << std::endl;
	const RecoSubjetAK8* subjet1 = (*jet_ak8)->subJet1();
	if ( subjet1 ) std::cout << " subjet #1: pT = " << subjet1->pt() << ", eta = " << subjet1->eta() << ", phi = " << subjet1->phi() << std::endl;
	const RecoSubjetAK8* subjet2 = (*jet_ak8)->subJet2();
	if ( subjet2 ) std::cout << " subjet #2: pT = " << subjet2->pt() << ", eta = " << subjet2->eta() << ", phi = " << subjet2->phi() << std::endl;
      }
    }
    if ( genWjjP4.pt() > 100. && !isMatched ) std::cout << "--> DEBUG (Wjj) !!" << std::endl;    
  }
}

/**
 * @brief Produce datacard and control plots for 2lss category of HH analysis.
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

  std::cout << "<analyze_hh_2lss_leq1tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_2lss_leq1tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_2lss_leq1tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_2lss_leq1tau");
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
  else throw cms::Exception("analyze_hh_2lss_leq1tau")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";

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

  GenMatchInterface genMatchInterface(2, apply_leptonGenMatching, true);

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;

  const double lep_mva_cut_mu = cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e  = cfg_analyze.getParameter<double>("lep_mva_cut_e");
  const std::string lep_mva_wp = cfg_analyze.getParameter<std::string>("lep_mva_wp");

  const int minNumJets = cfg_analyze.getParameter<int>("minNumJets");
  const int maxNumTaus = cfg_analyze.getParameter<int>("maxNumTaus");
  std::cout << "minNumJets = " << minNumJets << ",  maxNumTaus = " << maxNumTaus << '\n';

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
  const int fatJetPt_option = useNonNominal_jetmet ? kFatJet_central_nonNominal : getFatJet_option(central_or_shift_main, isMC);
  const int hadTauPt_option = useNonNominal_jetmet ? kHadTauPt_uncorrected      : getHadTauPt_option(central_or_shift_main);

  std::cout
    << "central_or_shift = "    << central_or_shift_main << "\n"
       " -> hadTauPt_option = " << hadTauPt_option       << "\n"
       " -> met_option      = " << met_option            << "\n"
       " -> jetPt_option    = " << jetPt_option          << "\n"
       "--> fatJetPt_option = " << fatJetPt_option       << '\n'
  ;

  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", hadTauSelection_antiMuon);
  cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG", isDEBUG);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("lep_mva_wp", lep_mva_wp);
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case Era::k2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case Era::k2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case Era::k2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_hh_2lss_leq1tau", __LINE__) << "Invalid era = " << static_cast<int>(era);
  }
  const ChargeMisIdRate chargeMisIdRate(era, lep_mva_wp);

  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "2lepton"  ) applyFakeRateWeights = kFR_2lepton;
  else throw cms::Exception("analyze_hh_2lss_leq1tau")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";

  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_2lepton ) {
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
  //std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  //std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8");
  //std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8");
  std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8 = cfg_analyze.getParameter<std::string>("branchName_jets_ak8_Wjj");
  std::string branchName_subjets_ak8 = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8_Wjj");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");
  std::string branchName_vertex = cfg_analyze.getParameter<std::string>("branchName_vertex");

  std::string branchName_genLeptons = cfg_analyze.getParameter<std::string>("branchName_genLeptons");
  std::string branchName_genHadTaus = cfg_analyze.getParameter<std::string>("branchName_genHadTaus");
  std::string branchName_genPhotons = cfg_analyze.getParameter<std::string>("branchName_genPhotons");
  std::string branchName_genProxyPhotons = cfg_analyze.getParameter<std::string>("branchName_genProxyPhotons");
  std::string branchName_genFromHardProcess = cfg_analyze.getParameter<std::string>("branchName_genFromHardProcess");
  std::string branchName_genJets = cfg_analyze.getParameter<std::string>("branchName_genJets");

  std::string branchName_muonGenMatch     = cfg_analyze.getParameter<std::string>("branchName_muonGenMatch");
  std::string branchName_electronGenMatch = cfg_analyze.getParameter<std::string>("branchName_electronGenMatch");
  std::string branchName_hadTauGenMatch   = cfg_analyze.getParameter<std::string>("branchName_hadTauGenMatch");
  std::string branchName_jetGenMatch      = cfg_analyze.getParameter<std::string>("branchName_jetGenMatch");

  bool redoGenMatching = cfg_analyze.getParameter<bool>("redoGenMatching");
  bool jetCleaningByIndex = cfg_analyze.getParameter<bool>("jetCleaningByIndex");
  bool genMatchingByIndex = cfg_analyze.getParameter<bool>("genMatchingByIndex");

  std::string branchName_genHiggses = cfg_analyze.getParameter<std::string>("branchName_genHiggses");

  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");
 
  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfg_runLumiEventSelector;
    cfg_runLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfg_runLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfg_runLumiEventSelector);
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

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s)." << std::endl;

//--- declare event-level variables
  EventInfo eventInfo(analysisConfig);
  if(isMC)
  {
    const double ref_genWeight = cfg_analyze.getParameter<double>("ref_genWeight");
    eventInfo.set_refGetWeight(ref_genWeight);
  }

//--- HH coupling scan
  const bool isMC_ggf_HH_nonresonant = process_string.find("signal_ggf_nonresonant") != std::string::npos;
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
    //hhWeight_couplings = new HHWeightInterfaceCouplings(hhWeight_cfg);
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
  inputTree->registerReader(&eventInfoReader);

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

  hltPathReader hltPathReader_instance({ triggers_1e, triggers_2e, triggers_1mu, triggers_2mu, triggers_1e1mu });
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
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era, -1, isDEBUG);
  //RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorFakeable_hh_multilepton fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era, -1, isDEBUG);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3, isDEBUG);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era, -1, isDEBUG);
  //RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorFakeable_hh_multilepton fakeableElectronSelector(era, -1, isDEBUG);
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

  RecoJetReader* jetReader = new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  jetReader->setPtMass_central_or_shift(jetPt_option);
  jetReader->read_btag_systematics((central_or_shifts_local.size() > 1 || central_or_shift_main != "central") && isMC);
  inputTree->registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerByIndex(isDEBUG);
  RecoJetCollectionSelector jetSelector(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorVBF(era, -1, isDEBUG);
  //jetSelectorVBF.getSelector().set_min_pt(30.);
  jetSelectorVBF.getSelector().set_max_absEta(4.7);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era, -1, isDEBUG);

  RecoJetReaderAK8* jetReaderAK8 = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8, branchName_subjets_ak8);
  jetReaderAK8->set_central_or_shift(fatJetPt_option);
  jetReaderAK8->ignoreSys(kFatJetNone);
  inputTree->registerReader(jetReaderAK8);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8 jetSelectorAK8(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG); // Need to redefine new class RecoJetCollectionSelectorAK8_WWWW_Wjj
  std::cout << "branchName_jets_ak8: " << branchName_jets_ak8 << ", "
	    << "branchName_subjets_ak8: " << branchName_subjets_ak8 << "\n";
  if ( branchName_jets_ak8.find("AK8LS") != std::string::npos    &&
       branchName_subjets_ak8 .find("AK8LS") != std::string::npos )
  {
    jetSelectorAK8_Wjj.disableDeltaRCut_between_AK8Subjets_NearestLepton();
    std::cout << "\t diable dR(AK8subjets, nearestLepton) cut ***** \n";
  }
  else
  {
    jetSelectorAK8_Wjj.enableDeltaRCut_between_AK8Subjets_NearestLepton();
    std::cout << "\t enable dR(AK8subjets, nearestLepton) cut ***** \n";
  }
  
  GenParticleReader* genWBosonReader = nullptr;
  GenParticleReader* genWJetReader = nullptr;
  if ( isMC ) {
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }


//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  metReader->set_phiModulationCorrDetails(&eventInfo, &vertex);
  inputTree->registerReader(metReader);

  MEtFilter metFilters;
  MEtFilterReader* metFilterReader = new MEtFilterReader(&metFilters, era);
  inputTree -> registerReader(metFilterReader);

//--- declare generator level information
  GenLeptonReader * genLeptonReader = nullptr;
  GenHadTauReader * genHadTauReader = nullptr;
  GenPhotonReader * genPhotonReader = nullptr;
  GenPhotonReader * genProxyPhotonReader = nullptr;
  GenParticleReader * genFromHardProcessReader = nullptr;
  GenJetReader * genJetReader = nullptr;
  GenParticleReader * genHiggsReader = nullptr;
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

    genHiggsReader = new GenParticleReader(branchName_genHiggses);
    inputTree->registerReader(genHiggsReader);
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree->registerReader(lheInfoReader);
    psWeightReader = new PSWeightReader(hasPS, apply_LHE_nom);
    inputTree -> registerReader(psWeightReader);
  }






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
  /*
  const edm::ParameterSet mvaInfo_nonRes_base = cfg_analyze.getParameter<edm::ParameterSet>("mvaInfo_nonRes_base");
  std::string BDTFileName_nonRes_base_even  = mvaInfo_nonRes_base.getParameter<std::string>("BDT_xml_FileName_nonRes_base_even");
  std::string BDTFileName_nonRes_base_odd   = mvaInfo_nonRes_base.getParameter<std::string>("BDT_xml_FileName_nonRes_base_odd");
  std::vector<std::string> BDTInputVariables_nonRes_base = mvaInfo_nonRes_base.getParameter<std::vector<std::string>>("inputVars_nonRes_base"); // Include all Input Var.s except BM indices
  */

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
  /*
  assert(BDTFileName_nonRes_base_odd != "");
  assert(BDTFileName_nonRes_base_even != "");
  assert(BDTInputVariables_nonRes_base.size() != 0);
  TMVAInterface* BDT_nonRes_base = new TMVAInterface(BDTFileName_nonRes_base_odd, BDTFileName_nonRes_base_even, BDTInputVariables_nonRes_base);
  BDT_nonRes_base->enableBDTTransform();
  std::map<std::string, double> BDTOutput_Map_nonRes_base;
  */
  std::map<std::string, double> AllVars_Map;

  /////////////////////




  /*
  //--- initialize BDTs
  std::string BDTFileName = "hhAnalysis/multilepton/data/hh_2lss_XGB_noTopness_evtLevelSUM_HH_res_10Var.pkl";
  std::vector<std::string> BDTInputVariables_SUM =
    {"jetMass_sel", 
     "leptonPairMass_sel",
     "HT",
     "mindr_lep1_jet", 
     "mT_lep1",
     "mindr_lep2_jet", 
     "mT_lep2",
     "dR_ll",
     "max_lep_eta",
     "gen_mHH",
    };
  XGBInterface BDT_SUM(BDTFileName, BDTInputVariables_SUM);
  std::map<std::string, double> BDTInputs_SUM;
  */

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  std::cout << "selEventsFileName_output = " << selEventsFileName_output << std::endl;

  vstring categories_evt = {
    //"hh_2lss_0tau", "hh_2lss_1tau"
  };
  
//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    ElectronHistManager* leadElectron_;
    ElectronHistManager* subleadElectron_;
    MuonHistManager* muons_;
    MuonHistManager* leadMuon_;
    MuonHistManager* subleadMuon_;
    JetHistManager* jets_;
    JetHistManager* leadJet_;
    JetHistManager* subleadJet_;
    JetHistManagerAK8* jetsAK8_Wjj_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    EvtHistManager_hh_2lss_leq1tau* evt_;
    std::map<std::string, EvtHistManager_hh_2lss_leq1tau*> evt_in_categories_;
    DatacardHistManager_hh* datacard_;
    MVAInputVarCorrelationHistManager* mvaInputVarCorrelation_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };

  std::map<std::string, GenEvtHistManager*> genEvtHistManager_beforeCuts;
  std::map<std::string, GenEvtHistManager*> genEvtHistManager_afterCuts;
  std::map<std::string, LHEInfoHistManager*> lheInfoHistManager;
  std::map<std::string, std::map<int, selHistManagerType*>> selHistManagers;

  HHGenKinematicsHistManager* genKinematicsHistManager_HH = NULL;
  if ( isMC_ggf_HH_nonresonant )
  {
    genKinematicsHistManager_HH = new HHGenKinematicsHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/genKinematics_HH", histogramDir.data()), era_string, central_or_shift_main),
      analysisConfig, eventInfo, hhWeight_couplings, HHWeightLO_calc, HHWeightNLO_calc);
    genKinematicsHistManager_HH->bookHistograms(fs);
  }
    
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
        selHistManager->jets_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/jets", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jets_->bookHistograms(fs);
        selHistManager->leadJet_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/leadJet", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
        selHistManager->leadJet_->bookHistograms(fs);
        selHistManager->subleadJet_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/subleadJet", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
        selHistManager->subleadJet_->bookHistograms(fs);
        selHistManager->jetsAK8_Wjj_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/jetsAK8_Wjj", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jetsAK8_Wjj_->bookHistograms(fs);
        selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
        selHistManager->met_->bookHistograms(fs);
        selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
        selHistManager->metFilters_->bookHistograms(fs);
      }
      if(! skipBooking)
      {
        selHistManager->evt_ = new EvtHistManager_hh_2lss_leq1tau(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
        selHistManager->evt_->bookHistograms(fs);

	for(const std::string & category: categories_evt)
	{
	  std::cout << "\t category: " << category << std::endl;
	  TString histogramDir_category = histogramDir.data();
	  histogramDir_category.ReplaceAll("hh_2lss", Form("%s", category.data()));
	
	  selHistManager->evt_in_categories_[category] = new EvtHistManager_hh_2lss_leq1tau(makeHistManager_cfg(process_and_genMatch,
	      Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift));
	  selHistManager->evt_in_categories_[category]->bookHistograms(fs);
	}	
      }
      
      selHistManager->datacard_ = new DatacardHistManager_hh(makeHistManager_cfg(process_and_genMatch,
        Form("%s/sel/datacard", histogramDir.data()), era_string, central_or_shift),
        analysisConfig, eventInfo, HHWeightLO_calc, HHWeightNLO_calc,
        isDEBUG);
      selHistManager->datacard_->bookHistograms(fs);

      if(! skipBooking)
      {
        selHistManager->mvaInputVarCorrelation_ = new MVAInputVarCorrelationHistManager(makeHistManager_cfg(process_and_genMatch,
            Form("%s/sel/mvaInputVarCorrelation", histogramDir.data()), era_string, central_or_shift));
        // CV: make correlation plot for MVA input variables used for non-resonant HH signal extraction,
        //     as defined in hhAnalysis/multilepton/data/BDT_2lss/nonres_default_Sandeep_9vars_usingLepConePt/2lss_even_half_model_nonres_default.xml
        selHistManager->mvaInputVarCorrelation_->bookHistograms(fs, {
	    // v6
	    "leptonPairMass_sel", "dihiggsVisMass_sel", "met_LD",
	    "dR_ll", "dR_l_Wjets_min", "dR_l_leadWjet_min", "dR_l_Wjets_max",
	    "dR_l_leadWjet_max", "dR_2j_fromW1", "mT_lep1",
	    // v7p2
	    "lep1_conePt", "lep2_conePt", "mindr_lep1_jet", "HT", "mindr_lep2_jet",
	     "mht", "mass_2j_fromW1"
        });
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

  std::cout << "Book BDT filling" << std::endl;
  NtupleFillerBDT<float, int>* bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type int_type;

  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
     makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift_main)
    );
    if(apply_HH_rwgt_lo || apply_HH_rwgt_nlo)
    {
      for(auto bmName : HHWeightNames)
      {
        bdt_filler->register_variable<float_type>(bmName.data());
      }
    }
    bdt_filler->register_variable<float_type>(
      "dihiggsVisMass_sel", "dihiggsMass_wMet_sel", "jetMass_sel", "leptonPairMass_sel", "leptonPairCharge_sel",
      "met", "mht", "met_LD",
      "HT", "STMET",
      "evtWeight",
      "lep1_pt", "lep1_conePt", "lep1_eta", "mindr_lep1_jet", "mT_lep1",
      "lep2_pt", "lep2_conePt", "lep2_eta", "mindr_lep2_jet", "mT_lep2",
      "dR_ll", "pT_ll", "max_lep_eta",
      "pT_llMEt", "Smin_llMEt",
      "vbf_m_jj", "vbf_dEta_jj",
      //
      "dPhi_ll",
      "mass_2j_fromW1", "mass_2j_fromW2", "dR_2j_fromW1", "dR_2j_fromW2",
      "dR_Wjets_min", "dR_Wjets_max", "dR_l_Wjets_min",
      "dR_l_Wjets_max", "dR_l_AK4jets_min", "dR_l_AK4jets_max", "dR_l_leadWjet_min", "dR_l_leadWjet_max", "dR_l_leadAK4jet_min", "dR_l_leadAK4jet_max",      
      //
      "THWeight", "mhh_gen", "costS_gen",
      "genWeight" , "lheWeight" , "pileupWeight", "triggerWeight", "btagWeight", "leptonEffSF", "data_to_MC_correction","FR_Weight", "lep1_frWeight", "lep2_frWeight", "evtWeight"
    );
    bdt_filler->register_variable<int_type>(
      "BM", "nJet", "nJet_vbf", "isVBF", "nLep", "nLep_loose", "nElec",
      //
      "nElectrons_in_2lss",
      "nAK8_w2subjets", "nWJets_selected",
      "nTaus",
      "eventCategory"
    );
    bdt_filler->bookTree(fs);
  }



  std::vector<string> vResSpins = {"spin0", "spin2"};
  
  const bool fillBDTOutputTree = false;
  NtupleFillerBDT<float, int> * bdtOutput_filler = nullptr;
  typedef std::remove_pointer<decltype(bdtOutput_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdtOutput_filler)>::type::int_type   int_type;
  if ( fillBDTOutputTree )
  {
    std::cout << "Fill bdtOutput_filler: ";
    bdtOutput_filler = new std::remove_pointer<decltype(bdtOutput_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple_BDTOutput", histogramDir.data()), era_string, central_or_shift_main)
      );
    
    for (size_t iSpin = 0; iSpin < vResSpins.size(); iSpin++)
    {
      for (size_t imHH=0; imHH < gen_mHH.size(); imHH++)
      {
	TString sNodeName = Form("BDTOutput_%g_%s",gen_mHH[imHH],vResSpins[iSpin].c_str());
	std::cout << sNodeName << ", ";
	bdtOutput_filler->register_variable<float_type>(sNodeName.Data());
      }
      std::cout << "\n";
    }
    
    for (size_t ibm = 0; ibm < nonRes_BMs.size(); ibm++)
    {
      TString sNodeName = Form("BDTOutput_nonres_%s",nonRes_BMs[ibm].c_str());
      std::cout << sNodeName << ", ";
      bdtOutput_filler->register_variable<float_type>(sNodeName.Data());
    }
    std::cout << "\n";

    bdtOutput_filler->register_variable<float_type>("evtWeight");
    if(apply_HH_rwgt_lo || apply_HH_rwgt_nlo)
    {
      for(auto bmName : HHWeightNames)
      {
        bdtOutput_filler->register_variable<float_type>(bmName.data());
      }
    } 
    
    bdtOutput_filler -> bookTree(fs);
  }



  

  std::vector<double> NormBM;
  int BM = -10;

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
    "gen photon filter",
    "trigger",
    ">= 2 presel leptons",    
    "b-jet veto",
    "sel tau veto",
    ">= 2 sel leptons",
    "<= 2 tight leptons",
    "trigger & fakeable lepton flavor matching",
    "trigger & dataset matching",
    "HLT filter matching",
    "m(ll) > 12 GeV",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV",
    "tight lepton charge",
    "sel lepton-pair SS/OS charge",
    ">= N jets",
    "event category criteria passed: boosted / semiboosted / resolved",
    "Z-boson mass veto",
    "H->ZZ*->4l veto",
    "met LD",
    "MEt filters",
    "signal region veto",
    "nonRes SM BDT > 0.7",
  };
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
    histogram_analyzedEntries->Fill(0.);

    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) )
    {
      continue;
    }
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
         objectMultiplicity.getNRecoLepton(kTight)             > 2  )
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
    std::vector<GenParticle> genHiggses;

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
      if(genHiggsReader)  genHiggses = genHiggsReader->read();

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
    std::vector<GenParticle> genWBosons;
    std::vector<GenParticle> genWJets;
    if ( isMC ) {
      genWBosons = genWBosonReader->read();
      genWJets = genWJetReader->read();

      if(analysisConfig.isMC_VH())
      {
        eventInfo.set_productionMode(get_VH_productionMode(genWBosons));
      }
    }
    
    if ( isDEBUG ) {
      dumpGenParticles("genWBoson", genWBosons);
      dumpGenParticles("genWJet", genWJets);
    }

    double mhh_gen = 0.;
    double costS_gen = 0.;
    double THWeight = 1.0;


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

 
      if (genKinematicsHistManager_HH)
      {
	double hhWeight1 =
	  evtWeightRecorder.get_genWeight() *
	  evtWeightRecorder.get_hhWeight_lo() *
	  evtWeightRecorder.get_hhWeight_nlo() *
	  evtWeightRecorder.get_lumiScale(central_or_shift_main);
      
	if (printLevel > 5) {
	  std::cout << "evtWeightRecorder.get_genWeight(): " << evtWeightRecorder.get_genWeight()
		    << ", evtWeightRecorder.get_hhWeight_lo(): " << evtWeightRecorder.get_hhWeight_lo()
		    << ", evtWeightRecorder.get_hhWeight_nlo(): " << evtWeightRecorder.get_hhWeight_nlo()
		    << ",  hhWeight1: " << hhWeight1
		    << "\n";
	}

	genKinematicsHistManager_HH->fillHistograms(hhWeight1);
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
    const std::vector<const RecoHadTau*> fakeableHadTaus = fakeableHadTauSelector(cleanedHadTaus, isHigherPt);
    const std::vector<const RecoHadTau*> selHadTaus = tightHadTauSelector(cleanedHadTaus, isHigherPt);

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
      jetCleanerByIndex(jet_ptrs, selectBDT ? selLeptons_full : fakeableLeptonsFull, fakeableHadTaus) :
      jetCleaner       (jet_ptrs, selectBDT ? selLeptons_full : fakeableLeptonsFull, fakeableHadTaus)
    ;
    const std::vector<const RecoJet*> selJets = jetSelector(cleanedJets, isHigherPt);
    const std::vector<const RecoJet*> selBJets_loose = jetSelectorBtagLoose(cleanedJets, isHigherPt);
    const std::vector<const RecoJet*> selBJets_medium = jetSelectorBtagMedium(cleanedJets, isHigherPt);
    int numSelJetsPtGt40 = countHighPtObjects(selJets, 40.);

    const std::vector<const RecoJet*> cleanedJetsVBF = jetCleaner(jet_ptrs, fakeableLeptons);
    const std::vector<const RecoJet*> selJetsVBF = jetSelectorVBF(cleanedJetsVBF, isHigherPt);


    


    
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
      if(genPhotonReader) genPhotonsFinal = genPhotonReader->read();
      if(genJetReader)    genJets = genJetReader->read();
      if(genHiggsReader)  genHiggses = genHiggsReader->read();

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

    if ( selBJets_loose.size() >= 2 || selBJets_medium.size() >= 1 )
      {
	continue;
      }
    cutFlowTable.update("b-jet veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("b-jet veto", evtWeightRecorder.get(central_or_shift_main));

    //if ( selHadTaus.size() > 0 ) {
    if ( (int)selHadTaus.size() > maxNumTaus ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS selHadTaus veto." << std::endl;
        printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update("sel tau veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel tau veto", evtWeightRecorder.get(central_or_shift_main));

//--- compute MHT and linear MET discriminant (met_LD)
    const RecoMEt met = metReader->read();
    const Particle::LorentzVector& metP4 = met.p4();
    Particle::LorentzVector mhtP4 = compMHT(fakeableLeptonsFull, fakeableHadTaus, selJets);
    double met_LD = compMEt_LD(metP4, mhtP4);

    /*
    Particle::LorentzVector selJetP4;
    double mass_jj_W = 0;
    for ( std::vector<const RecoJet*>::const_iterator selJet1_W = selJets.begin();
          selJet1_W != selJets.end(); ++selJet1_W ) {
      for ( std::vector<const RecoJet*>::const_iterator selJet2_W = selJet1_W + 1;
            selJet2_W != selJets.end(); ++selJet2_W ) {
        double mass_jj = ((*selJet1_W)->p4() + (*selJet2_W)->p4()).mass();
	if ( std::fabs(mass_jj - w_mass) < std::fabs(mass_jj_W - w_mass) || mass_jj_W==0) {
	  mass_jj_W = mass_jj;
	  selJetP4 = (*selJet1_W)->p4() + (*selJet2_W)->p4();
	  int counter = 0;
	  for ( std::vector<const RecoJet*>::const_iterator selJet3_4 = selJets.begin();
		selJet3_4 != selJets.end(); ++selJet3_4 ) {
	    if ((*selJet3_4)!=(*selJet1_W) && (*selJet3_4)!=(*selJet2_W)){
	      counter++;
	      if (counter <= 2){
		selJetP4 += (*selJet3_4)->p4();
	      }
	    }
	  }
	}
      }
      }*/

    double HT = compHT(fakeableLeptons, {}, selJets);
    double STMET = compSTMEt(fakeableLeptons, {}, selJets, met.p4());

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
    const Particle::LorentzVector& selLeptonP4_lead = selLepton_lead->cone_p4();
    const RecoLepton* selLepton_sublead = selLeptons[1];
    const Particle::LorentzVector& selLeptonP4_sublead = selLepton_sublead->cone_p4();
    const leptonChargeFlipGenMatchEntry& selLepton_genMatch = getLeptonChargeFlipGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead);

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

// require that trigger paths match lepton flavor (for fakeable leptons)
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
      bool isTriggered_DoubleEG = isTriggered_2e && fakeableElectrons.size() >= 2;
      bool isTriggered_DoubleMuon = isTriggered_2mu && fakeableMuons.size() >= 2;
      bool isTriggered_MuonEG = isTriggered_1e1mu && fakeableElectrons.size() >= 1 && fakeableMuons.size() >= 1;

      bool selTrigger_SingleElectron = selTrigger_1e;
      bool selTrigger_SingleMuon = selTrigger_1mu;
      bool selTrigger_DoubleEG = selTrigger_2e;
      //bool selTrigger_DoubleMuon = selTrigger_2mu;
      bool selTrigger_MuonEG = selTrigger_1e1mu;

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

      dataToMCcorrectionInterface->setLeptons({ selLepton_lead, selLepton_sublead }, true);

//--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_leptonTriggerEff(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      evtWeightRecorder.record_leptonIDSF_recoToLoose(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if(electronSelection >= kFakeable && muonSelection >= kFakeable)
      {
        // apply looseToTight SF to leptons matched to generator-level prompt leptons and passing Tight selection conditions
        evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface, false);
      }
    }

    bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
    bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);

    if(leptonFakeRateInterface)
    {
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton_lead);
      evtWeightRecorder.record_jetToLepton_FR_sublead(leptonFakeRateInterface, selLepton_sublead);
    }

    if(!selectBDT){
      if(applyFakeRateWeights == kFR_2lepton)
	{
	  evtWeightRecorder.compute_FR_2l(passesTight_lepton_lead, passesTight_lepton_sublead);
	}
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

    bool failsTightChargeCut = false;
    for ( std::vector<const RecoLepton*>::const_iterator lepton = fakeableLeptons.begin();
          lepton != fakeableLeptons.end(); ++lepton ) {
      if ( (*lepton)->is_electron() ) {
        const RecoElectron* electron = dynamic_cast<const RecoElectron*>(*lepton);
        assert(electron);
        if ( electron->tightCharge() < 2 )
	  {
	    failsTightChargeCut = true;
	    break;
	  }
      }
      else if ( (*lepton)->is_muon() ) {
        const RecoMuon* muon = dynamic_cast<const RecoMuon*>(*lepton);
        assert(muon);
	if ( muon->tightCharge() < 2 )
	  {
	    failsTightChargeCut = true;
	    break;
	  }
      }
    }
    if ( failsTightChargeCut ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS tight lepton charge requirement." << std::endl;
      }
      //if (!selectBDT)
      continue;
    }
    cutFlowTable.update("tight lepton charge", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("tight lepton charge", evtWeightRecorder.get(central_or_shift_main));

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
    if ( leptonChargeSelection == kOS ) {
      const double prob_chargeMisID_sum = chargeMisIdRate.get(selLepton_lead, selLepton_sublead);
      evtWeightRecorder.record_chargeMisIdProb(prob_chargeMisID_sum);

      // Karl: reject the event, if the applied probability of charge misidentification is 0;
      //       we assume that the event weight was not 0 before including the charge flip weights
      //       Note that this can happen only if both selected leptons are muons (their misId prob is 0).
      if(prob_chargeMisID_sum == 0.)
      {
        if(run_lumi_eventSelector)
        {
          std::cout << "event " << eventInfo.str() << " FAILS charge flip selection\n"
                       "(leading lepton charge (pdgId) = " << selLepton_lead->charge() << " (" << selLepton_lead->pdgId()
                    << "); "
                       "subleading lepton charge (pdgId) = " << selLepton_sublead->charge() << " (" << selLepton_sublead->pdgId()
                    << "))\n"
          ;
        }
        continue;
      }
    }
    cutFlowTable.update(Form("sel lepton-pair %s charge", leptonChargeSelection_string.data()), evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel lepton-pair OS/SS charge", evtWeightRecorder.get(central_or_shift_main));






    std::vector<RecoJetAK8> jets_ak8 = jetReaderAK8->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8 = convert_to_ptrs(jets_ak8);
    std::vector<const RecoJetAK8*> selJetsAK8 = jetSelectorAK8(jet_ptrs_ak8, isHigherPt);
    
    jetSelectorAK8_Wjj.getSelector().set_leptons({selLeptons[0], selLeptons[1]});
    std::vector<const RecoJetAK8*> selJetsAK8_Wjj = jetSelectorAK8_Wjj(jet_ptrs_ak8, isHigherPt);    
    std::vector<const RecoJetAK8*> selJetsAK8_Wjj_selected;

    std::vector<const RecoJetBase*> selJets_Wjj_WPairwise;
    //const RecoJetBase* selJet1_Wjj   = nullptr;
    //const RecoJetBase* selJet2_Wjj   = nullptr;

    bool isEventBoosted     = false;
    bool isEventSemiboosted = false;
    bool isEventResolved    = false;
    
    double mass_jj_W = 0;
     
    if ( isDEBUG || run_lumi_eventSelector ) {
      printCollection("uncleaned AK8 jets", jet_ptrs_ak8);
      //printWjj(jet_ptrs_ak8, jetSelectorAK8_Wjj, genWBosons, genWJets);
    }


    // fill selJetsAK8_Wjj_selected
    for (size_t i=0; i<selJetsAK8_Wjj.size(); i++) {
      if (selJetsAK8_Wjj[i] && selJetsAK8_Wjj[i]->subJet1() && selJetsAK8_Wjj[i]->subJet2()) {
	selJetsAK8_Wjj_selected.push_back(selJetsAK8_Wjj[i]);
      }      
    }

    if (selJetsAK8_Wjj_selected.size() >= 2) // boosted category ----------------------------------------------------------------------------------------------------------------------
    { 
      selJets_Wjj_WPairwise.push_back(selJetsAK8_Wjj_selected[0]->subJet1());
      selJets_Wjj_WPairwise.push_back(selJetsAK8_Wjj_selected[0]->subJet2());

      selJets_Wjj_WPairwise.push_back(selJetsAK8_Wjj_selected[1]->subJet1());
      selJets_Wjj_WPairwise.push_back(selJetsAK8_Wjj_selected[1]->subJet2());
      isEventBoosted = true;

      if (printLevel > 5)
      {
	std::cout << "isEventBoosted:  selJets.size() " << selJets.size() << ", selJetsAK8_Wjj_selected.size() " << selJetsAK8_Wjj_selected.size() << ", selJets_Wjj_WPairwise.size() " << selJets_Wjj_WPairwise.size() << "\n";
      }      
    }
    else if (selJetsAK8_Wjj_selected.size() == 1) // semiboosted category --------------------------------------------------------------------------------------
    {
      isEventSemiboosted = true;
      
      std::vector<const RecoSubjetAK8*> selSubjetsAK8 = { selJetsAK8_Wjj_selected[0]->subJet1(), selJetsAK8_Wjj_selected[0]->subJet2() };
      double dm_min = 9999.;
      size_t idxWJet1 = 9999;
      size_t idxWJet2 = 9999;
      for (size_t iJet1=0; iJet1 < selJets.size(); iJet1++ ) {
	const RecoJet *jet1 = selJets[iJet1];
	if (hasOverlapJets(jet1, selSubjetsAK8)) continue;
	
	for (size_t iJet2=iJet1+1; iJet2 < selJets.size(); iJet2++ ) {
	  const RecoJet *jet2 = selJets[iJet2];
	  if (hasOverlapJets(jet2, selSubjetsAK8)) continue;

	  double dm = std::fabs((jet1->p4() + jet2->p4()).mass() - w_mass);
	  if (dm < dm_min) {
	    dm_min = dm;
	    idxWJet1 = iJet1;
	    idxWJet2 = iJet2;
	    }	  
	}
      }      
      
      selJets_Wjj_WPairwise.push_back(selJetsAK8_Wjj_selected[0]->subJet1());
      selJets_Wjj_WPairwise.push_back(selJetsAK8_Wjj_selected[0]->subJet2());
      
      if (idxWJet1 != 9999 && idxWJet2 != 9999) // for 2 AK4 jets case
      { 
	selJets_Wjj_WPairwise.push_back(selJets[idxWJet1]);
	selJets_Wjj_WPairwise.push_back(selJets[idxWJet2]);
      }
      else if ( selJets.size() > 0 && ! hasOverlapJets(selJets[0], selSubjetsAK8) ) // for 1 AK4 jet case 
      { 
	selJets_Wjj_WPairwise.push_back(selJets[0]);
	isEventSemiboosted = true;
	
	if (printLevel > 5)
	{
	  std::cout << "isEventSemiboosted 1 AK4 :  selJets.size() " << selJets.size() << ", selJetsAK8_Wjj_selected.size() " << selJetsAK8_Wjj_selected.size() << ", selJets_Wjj_WPairwise.size() " << selJets_Wjj_WPairwise.size() << "\n";
	}
      }
      
    }
    else if (selJetsAK8_Wjj_selected.size() == 0 && (int)selJets.size() >= minNumJets) // resolved category --------------------------------------------------------------------------------------
    {
      isEventResolved = true;
      
      double dm_min = 9999.;
      size_t idxWJet1 = 9999;
      size_t idxWJet2 = 9999;
      size_t idxWJet3 = 9999;
      size_t idxWJet4 = 9999;
      
      // 1st W->jj pair
      for (size_t iJet1=0; iJet1 < selJets.size(); iJet1++ ) {
	const RecoJet *jet1 = selJets[iJet1];
	
	for (size_t iJet2=iJet1+1; iJet2 < selJets.size(); iJet2++ ) {
	  const RecoJet *jet2 = selJets[iJet2];

	  double dm = std::fabs((jet1->p4() + jet2->p4()).mass() - w_mass);
	  if (dm < dm_min) {
	    dm_min = dm;
	    idxWJet1 = iJet1;
	    idxWJet2 = iJet2;
	  }  
	}
      }      

      // 2nd W->jj pair
      dm_min = 9999.;
      for (size_t iJet3=0; iJet3 < selJets.size(); iJet3++ ) {
	if (iJet3 == idxWJet1 || iJet3 == idxWJet2) continue;
	const RecoJet *jet3 = selJets[iJet3];
	
	for (size_t iJet4=iJet3+1; iJet4 < selJets.size(); iJet4++ ) {
	  if (iJet4 == idxWJet1 || iJet4 == idxWJet2) continue;
	  const RecoJet *jet4 = selJets[iJet4];

	  double dm = std::fabs((jet3->p4() + jet4->p4()).mass() - w_mass);
	  if (dm < dm_min) {
	    dm_min = dm;
	    idxWJet3 = iJet3;
	    idxWJet4 = iJet4;
	  }
	}
      }
      
      if (idxWJet1 != 9999 && idxWJet2 != 9999 && idxWJet3 != 9999 && idxWJet4 != 9999) // nAK4 >= 4
      {
	selJets_Wjj_WPairwise.push_back(selJets[idxWJet1]);
	selJets_Wjj_WPairwise.push_back(selJets[idxWJet2]);

	selJets_Wjj_WPairwise.push_back(selJets[idxWJet3]);
	selJets_Wjj_WPairwise.push_back(selJets[idxWJet4]);
      }
      else if (idxWJet1 != 9999 && idxWJet2 != 9999) // nAK4: 2 or 3
      {
	selJets_Wjj_WPairwise.push_back(selJets[idxWJet1]);
	selJets_Wjj_WPairwise.push_back(selJets[idxWJet2]);

	// for nAK4 = 3
	for (size_t iJet3=0; iJet3 < selJets.size(); iJet3++ ) {
	  bool isJetSelected = false;

	  for (size_t iJetSelected = 0; iJetSelected < selJets_Wjj_WPairwise.size(); iJetSelected++) {
	    if (selJets[iJet3] == selJets_Wjj_WPairwise[iJetSelected]) isJetSelected = true;
	  }

	  if ( ! isJetSelected ) selJets_Wjj_WPairwise.push_back(selJets[iJet3]);
	}
	
	if (selJets_Wjj_WPairwise.size() > 2 && selJets.size() <= 2)
	{
	  throw cms::Exception("analyze_hh_2lss_leq1tau")
	    << "ERROR:  selJets_Wjj_WPairwise.size() > 2 && selJets.size() <= 2  !!\n";
	}
	
	if (selJets_Wjj_WPairwise.size() > 3)
	{
	  throw cms::Exception("analyze_hh_2lss_leq1tau")
	    << "ERROR:  selJets_Wjj_WPairwise.size() > 3, but idxWJet3 == 9999 && idxWJet4 == 9999  !!\n";
	}
      }
      else
      {
	throw cms::Exception("analyze_hh_2lss_leq1tau")
	  << "ERROR:  selJets.size() " << selJets.size() << " but idxWJet1 == 9999 && idxWJet2 == 9999  !!\n";
      }      
    }

    Particle::LorentzVector selJetP4;
    for (size_t iJet = 0; iJet < selJets_Wjj_WPairwise.size(); iJet++) selJetP4 += selJets_Wjj_WPairwise[iJet]->p4();

    
    if ( !((int)selJets_Wjj_WPairwise.size() >= minNumJets) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS selJets selection." << std::endl;
	printCollection("selJets", selJets);
	printCollection("selJets_Wjj_WPairwise", selJets_Wjj_WPairwise);
      }
      continue;
    }
    cutFlowTable.update(">= N jets", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= N jets", evtWeightRecorder.get(central_or_shift_main));
    

    if (isEventBoosted) {
      cutFlowTable.update("event category criteria passed: boosted", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("event category criteria passed: boosted", evtWeightRecorder.get(central_or_shift_main));
    }
    if (isEventSemiboosted) {
      cutFlowTable.update("event category criteria passed: semiboosted", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("event category criteria passed: semiboosted", evtWeightRecorder.get(central_or_shift_main));
    }
    if (isEventResolved) {
      cutFlowTable.update("event category criteria passed: resolved", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("event category criteria passed: resolved", evtWeightRecorder.get(central_or_shift_main));
    }


    if ( !(isEventBoosted || isEventSemiboosted || isEventResolved)) continue;
    
    cutFlowTable.update("event category criteria passed: boosted / semiboosted / resolved", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("event category criteria passed: boosted / semiboosted / resolved", evtWeightRecorder.get(central_or_shift_main));

   





    const bool failsZbosonMassVeto = isfailsZbosonMassVeto(preselLeptonsFull, false, isDEBUG) || (
        selLepton_lead->is_electron() &&
        selLepton_sublead->is_electron() &&
        isfailsZbosonMassVeto({ selLepton_lead, selLepton_sublead }, true, isDEBUG)
      )
    ;    
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));

    const bool failsHtoZZVeto = isfailsHtoZZVeto(preselLeptonsFull);
    if ( failsHtoZZVeto ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS H->ZZ*->4l veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("H->ZZ*->4l veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("H->ZZ*->4l veto", evtWeightRecorder.get(central_or_shift_main));

    if ( !(selLepton_lead->is_muon() || selLepton_sublead->is_muon() || met_LD >= 30.) ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS MET LD selection.\n"
	  " (LD = " << met_LD << ")\n"
	  ;
      }
      continue;
    }
    cutFlowTable.update("met LD", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("met LD", evtWeightRecorder.get(central_or_shift_main));

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
      bool applySignalRegionVeto_lepton = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1); // Revet to the old MCClosure condition
      if ( applySignalRegionVeto_lepton && tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable ) {
      if ( tightLeptons.size() >= 2 ) failsSignalRegionVeto = true;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
                     "# tight leptons = " << tightLeptons.size() << " >= 2\n"
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

    // compute signal extraction observables
    double dihiggsVisMass_sel = (selJetP4 + selLepton_lead->cone_p4() + selLepton_sublead->cone_p4()).mass();
    double dihiggsMass_wMet_sel = (selJetP4 + selLepton_lead->cone_p4() + selLepton_sublead->cone_p4() + met.p4()).mass();
    double jetMass_sel = mass_jj_W;

    //--- compute variables BDTs used to discriminate . . .
    const double mindr_lep1_jet  = comp_mindr_jet(*selLepton_lead, selJets);
    const double mindr_lep2_jet  = comp_mindr_jet(*selLepton_sublead, selJets);
    Particle::LorentzVector llP4 = selLeptonP4_lead + selLeptonP4_sublead;
    double pT_ll = llP4.pt();
    double pT_llMEt = (llP4 + metP4).pt();
    double Smin_llMEt = comp_Smin(llP4, metP4.px(), metP4.py());


    int nElectrons_in_2lss = 0;
    for (size_t i=0; i<2; i++)
    {
      if (abs(selLeptons[i]->pdgId()) == 11) nElectrons_in_2lss++;
    }
    double leptonPairMass_sel = (selLepton_lead->cone_p4() + selLepton_sublead->cone_p4()).mass();
    double leptonPairCharge_sel = selLepton_lead->charge() + selLepton_sublead->charge();
    double dR_ll = deltaR(selLeptonP4_lead, selLeptonP4_sublead);
    double dPhi_ll = calculateAbsDeltaPhi(selLeptonP4_lead.phi(), selLeptonP4_sublead.phi());
    

    //int nAK4 = selJets.size();
    int nAK8_w2subjets = selJetsAK8_Wjj_selected.size();
    int nWJets_selected = selJets_Wjj_WPairwise.size();
    double mass_2j_fromW1 = -1;
    double mass_2j_fromW2 = -1;
    double dR_2j_fromW1   = -1;
    double dR_2j_fromW2   = -1;

    if (selJets_Wjj_WPairwise.size() >= 2)
    {
      mass_2j_fromW1 = (selJets_Wjj_WPairwise[0]->p4() + selJets_Wjj_WPairwise[1]->p4()).mass();
      dR_2j_fromW1   = deltaR(selJets_Wjj_WPairwise[0]->p4(), selJets_Wjj_WPairwise[1]->p4());
    }
    if (selJets_Wjj_WPairwise.size() >= 4)
    {
      mass_2j_fromW2 = (selJets_Wjj_WPairwise[2]->p4() + selJets_Wjj_WPairwise[3]->p4()).mass();
      dR_2j_fromW2   = deltaR(selJets_Wjj_WPairwise[2]->p4(), selJets_Wjj_WPairwise[3]->p4());
    }

    double dR_Wjets_min = 99999.;
    double dR_Wjets_max = -1;
    double dR_l_Wjets_min = 99999.;
    double dR_l_Wjets_max = -1;
    double dR_l_AK4jets_min = 99999.;
    double dR_l_AK4jets_max = -1;
    double dR_l_leadWjet_min = 99999.;
    double dR_l_leadWjet_max = -1;
    double dR_l_leadAK4jet_min = 99999.;
    double dR_l_leadAK4jet_max = -1;

    const RecoJetBase* selJet_Wjj_WPairwise_ptLead = nullptr;
    double pt_selJet_Wjj_WPairwise_ptLead = 0;
    for (size_t iJet1 = 0; iJet1 < selJets_Wjj_WPairwise.size(); iJet1++)
    {
      // selJet_Wjj_WPairwise_ptLead
      if (selJets_Wjj_WPairwise[iJet1]->pt() > pt_selJet_Wjj_WPairwise_ptLead )
      {
	selJet_Wjj_WPairwise_ptLead    = selJets_Wjj_WPairwise[iJet1];
	pt_selJet_Wjj_WPairwise_ptLead = selJets_Wjj_WPairwise[iJet1]->pt();
      }

      // dR_Wjets 
      for (size_t iJet2 = iJet1+1; iJet2 < selJets_Wjj_WPairwise.size(); iJet2++)
      {
	double  dr = deltaR(selJets_Wjj_WPairwise[iJet1]->p4(), selJets_Wjj_WPairwise[iJet2]->p4());
	if (dr < dR_Wjets_min) dR_Wjets_min = dr;
	if (dr > dR_Wjets_max) dR_Wjets_max = dr;	
      }
    }

    for (size_t iLep = 0; iLep < 2; iLep++)
    {
      double dr;

      // dR_l_Wjets min, max
      for (size_t iJet = 0; iJet < selJets_Wjj_WPairwise.size(); iJet++)
      {
	dr = deltaR(selLeptons[iLep]->p4(), selJets_Wjj_WPairwise[iJet]->p4());
	if (dr < dR_l_Wjets_min) dR_l_Wjets_min = dr;
	if (dr > dR_l_Wjets_max) dR_l_Wjets_max = dr;
      }

      // dR_l_leadWjet min, max
      dr = deltaR(selLeptons[iLep]->p4(), selJet_Wjj_WPairwise_ptLead->p4());
      if (dr < dR_l_leadWjet_min) dR_l_leadWjet_min = dr;
      if (dr > dR_l_leadWjet_max) dR_l_leadWjet_max = dr;

      // dR_l_AK4jets
      for (size_t iJet = 0; iJet < selJets.size(); iJet++)
      {
	dr = deltaR(selLeptons[iLep]->p4(), selJets[iJet]->p4());
	if (dr < dR_l_AK4jets_min) dR_l_AK4jets_min = dr;
	if (dr > dR_l_AK4jets_max) dR_l_AK4jets_max = dr;
      }

      // dR_l_leadAK4jet min, max
      if (selJets.size() > 0)
      {
	dr = deltaR(selLeptons[iLep]->p4(), selJets[0]->p4());
	if (dr < dR_l_leadAK4jet_min) dR_l_leadAK4jet_min = dr;
	if (dr > dR_l_leadAK4jet_max) dR_l_leadAK4jet_max = dr;
      }
    }

    double lep1_conePt = comp_lep_conePt(*selLepton_lead);
    double mT_lep1     = std::min(150., comp_MT_met(selLepton_lead, met.pt(), met.phi()));
    //
    double lep2_conePt = comp_lep_conePt(*selLepton_sublead);
    double mT_lep2     = std::min(150., comp_MT_met(selLepton_sublead, met.pt(), met.phi()));
    //
    double max_lep_eta = TMath::Max(std::abs(selLepton_lead -> eta()), std::abs(selLepton_sublead -> eta()));

    double mT_lep1_met = mT_lep1;
    double mT_lep2_met = mT_lep2;
    

    int eventCategory = 0;
    if      ( isEventBoosted )     eventCategory = 1;
    else if ( isEventSemiboosted ) eventCategory = 2;
    else if ( isEventResolved )    eventCategory = 3;
    
    
    std::vector<std::string> evtCategories;
    /*
    if      (selHadTaus.size() == 0) evtCategories.push_back("hh_2lss_0tau");
    else if (selHadTaus.size() == 1) evtCategories.push_back("hh_2lss_1tau");
    */
    int nTaus = (int)selHadTaus.size();

    
    /*
    //--- compute output of BDTs
    BDTInputs_SUM["jetMass_sel"]          = jetMass_sel;
    BDTInputs_SUM["leptonPairMass_sel"]   = leptonPairMass_sel;
    BDTInputs_SUM["HT"]                   = HT;
    BDTInputs_SUM["mindr_lep1_jet"]       = std::min(10., mindr_lep1_jet);
    BDTInputs_SUM["mT_lep1"]              = comp_MT_met(selLepton_lead, met.pt(), met.phi());
    BDTInputs_SUM["mindr_lep2_jet"]       = std::min(10., mindr_lep2_jet);
    BDTInputs_SUM["mT_lep2"]              = comp_MT_met(selLepton_sublead, met.pt(), met.phi());
    BDTInputs_SUM["dR_ll"]                = dR_ll;
    BDTInputs_SUM["max_lep_eta"]          = TMath::Max(std::abs(selLepton_lead -> eta()), std::abs(selLepton_sublead -> eta()));

    //double BDTOutput_SUM = BDT_SUM(BDTInputs_SUM);
    std::vector<double> BDTOutput_SUM;
    for (size_t i=0; i<gen_mHH.size(); i++){
      BDTInputs_SUM["gen_mHH"] = gen_mHH[i];
      BDTOutput_SUM.push_back( BDT_SUM(BDTInputs_SUM));
    }
    */

    double vbf_dEta_jj = -1.;
    double vbf_m_jj = -1.;
    bool isVBF = false;
    for ( std::vector<const RecoJet*>::const_iterator selJetVBF1 = selJetsVBF.begin();
          selJetVBF1 != selJetsVBF.end(); ++selJetVBF1 ) {
      for ( std::vector<const RecoJet*>::const_iterator selJetVBF2 = selJetVBF1 + 1;
            selJetVBF2 != selJetsVBF.end(); ++selJetVBF2 ) {
        double dEta_jj = TMath::Abs((*selJetVBF1)->eta() - (*selJetVBF2)->eta());
        double m_jj = ((*selJetVBF1)->p4() + (*selJetVBF2)->p4()).mass();
        if ( dEta_jj > 4. && m_jj > 500. ) {
          if ( dEta_jj > vbf_dEta_jj ) vbf_dEta_jj = dEta_jj;
          if ( m_jj    > vbf_m_jj    ) vbf_m_jj    = m_jj;
          isVBF = true;
        }
      }
    }





    //Gathering final BDT Inputs

    AllVars_Map["gen_mHH"]                                   =       250.; // setting a Dummy value which will be reset depending on mass hypothesis

    AllVars_Map["dihiggsVisMass_sel"] =              dihiggsVisMass_sel;
    AllVars_Map["dihiggsMass_wMet_sel"] =            dihiggsMass_wMet_sel;
    AllVars_Map["jetMass_sel"] =                     jetMass_sel;
    AllVars_Map["leptonPairMass_sel"] =              leptonPairMass_sel;
    AllVars_Map["leptonPairCharge_sel"] =            leptonPairCharge_sel;
    AllVars_Map["met"] =                             metP4.pt();
    AllVars_Map["mht"] =                             mhtP4.pt();
    AllVars_Map["met_LD"] =                          met_LD;
    AllVars_Map["HT"] =                              HT;
    AllVars_Map["STMET"] =                           STMET;
    AllVars_Map["evtWeight"] =                       evtWeightRecorder.get(central_or_shift_main);
    AllVars_Map["lep1_pt"] =                         selLepton_lead->pt();
    AllVars_Map["lep1_conePt"] =                     lep1_conePt;
    AllVars_Map["lep1_eta"] =                        selLepton_lead->eta();
    AllVars_Map["mindr_lep1_jet"] =                  std::min(10., mindr_lep1_jet) ;
    AllVars_Map["mT_lep1"] =                         mT_lep1;
    AllVars_Map["lep2_pt"] =                         selLepton_sublead->pt();
    AllVars_Map["lep2_conePt"] =                     lep2_conePt;
    AllVars_Map["lep2_eta"] =                        selLepton_sublead->eta();
    AllVars_Map["mindr_lep2_jet"] =                  std::min(10., mindr_lep2_jet) ;
    AllVars_Map["mT_lep2"] =                         mT_lep2;
    AllVars_Map["dR_ll"] =                           dR_ll;
    AllVars_Map["pT_ll"] =                           pT_ll;
    AllVars_Map["max_lep_eta"] =                     TMath::Max(std::abs(selLepton_lead -> eta()), std::abs(selLepton_sublead -> eta()));
    AllVars_Map["pT_llMEt"] =                        pT_llMEt;
    AllVars_Map["Smin_llMEt"] =                      Smin_llMEt;
    AllVars_Map["vbf_dEta_jj"] =                     vbf_dEta_jj;
    AllVars_Map["vbf_m_jj"] =                        vbf_m_jj;
    AllVars_Map["nJet"] =                            comp_n_jet25_recl(selJets);
    AllVars_Map["nJet_vbf"] =                        selJetsVBF.size();
    AllVars_Map["isVBF"] =                           isVBF;
    AllVars_Map["nLep"] =                            selLeptons.size();
    AllVars_Map["THWeight"] =                        THWeight;

    //AllVars_Map["leptonPairMass_sel"] =            leptonPairMass_sel;
    //AllVars_Map["dihiggsVisMass_sel"] =            dihiggsVisMass_sel;
    //AllVars_Map["met_LD"] =                          met_LD;
    //AllVars_Map["dR_ll"] =                           dR_ll;
    AllVars_Map["dR_l_Wjets_min"] =                  dR_l_Wjets_min;

    AllVars_Map["dR_l_leadWjet_min"] =               dR_l_leadWjet_min;
    AllVars_Map["dR_l_Wjets_max"] =                  dR_l_Wjets_max;
    AllVars_Map["dR_l_leadWjet_max"] =               dR_l_leadWjet_max;
    AllVars_Map["dR_2j_fromW1"] =                    dR_2j_fromW1;

    AllVars_Map["mass_2j_fromW1"] =                  mass_2j_fromW1;
    //AllVars_Map["mT_lep1"] =                         mT_lep1;

    


    std::map<std::string, double> BDTInputs_spin2 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_spin2, false);
    std::map<std::string, double> BDTInputs_spin0 = InitializeInputVarMap(AllVars_Map, BDTInputVariables_spin0, false);
    std::map<std::string, double> BDTInputs_nonRes = InitializeInputVarMap(AllVars_Map, BDTInputVariables_nonRes, true); // Include all Input Var.s except BM indices
    //std::map<std::string, double> BDTInputs_nonRes_base = InitializeInputVarMap(AllVars_Map, BDTInputVariables_nonRes_base, true); 
    
    std::vector<double> nonResBase_params;
    nonResBase_params.push_back(0.);

    BDTOutput_Map_spin2 = CreateResonantBDTOutputMap(gen_mHH, BDT_spin2, BDTInputs_spin2, eventInfo.event, "_spin2");
    BDTOutput_Map_spin0 = CreateResonantBDTOutputMap(gen_mHH, BDT_spin0, BDTInputs_spin0, eventInfo.event, "_spin0");
    BDTOutput_Map_nonRes = CreateNonResonantBDTOutputMap(nonRes_BMs, BDT_nonRes, BDTInputs_nonRes, eventInfo.event, hhWeight_couplings);
    //BDTOutput_Map_nonRes_base = CreateBDTOutputMap(nonResBase_params, BDT_nonRes_base, BDTInputs_nonRes_base, eventInfo.event, true, "_base");

    

    /*
    //#########################################################################
    //#########################################################################
    //#########################################################################    
    if (BDTOutput_Map_nonRes["SM"] < 0.7) continue;
    //printf("SM BDT (%g) above 0.7 \n",BDTOutput_Map_nonRes["SM"]);
    cutFlowTable.update("nonRes SM BDT > 0.7", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("nonRes SM BDT > 0.7", evtWeightRecorder.get(central_or_shift_main));
    //#########################################################################
    //#########################################################################
    //#########################################################################    
    */

    
//--- retrieve gen-matching flags
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons);

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
          selHistManager->jets_->fillHistograms(selJets, evtWeight);
          selHistManager->leadJet_->fillHistograms(selJets, evtWeight);
          selHistManager->subleadJet_->fillHistograms(selJets, evtWeight);
          if ( ! selJetsAK8_Wjj_selected.empty() ) {
            selHistManager->jetsAK8_Wjj_->fillHistograms(selJetsAK8_Wjj_selected, evtWeight);
          }
          selHistManager->met_->fillHistograms(met, mhtP4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
	}
	if(! skipFilling )
        {
          selHistManager->evt_->fillHistograms(
            selElectrons.size(),
            selMuons.size(),
            selJets.size(),
            numSelJetsPtGt40,
            dihiggsVisMass_sel,
            dihiggsMass_wMet_sel,
            jetMass_sel,
            leptonPairMass_sel,
            ( selLepton_lead->is_electron() && selLepton_sublead->is_electron() ) ? leptonPairMass_sel : -1.,
            ( selLepton_lead->is_muon()     && selLepton_sublead->is_muon()     ) ? leptonPairMass_sel : -1.,
            leptonPairCharge_sel,
            HT,
            STMET,
	    //
	    //
	    //
	    nElectrons_in_2lss,
	    //leptonPairMass_sel,
	    //leptonPairCharge_sel,
	    dR_ll,
	    dPhi_ll,
	    //
	    //nAK4,
	    nAK8_w2subjets,
	    nWJets_selected,
	    //
	    mass_2j_fromW1,
	    mass_2j_fromW2,
	    dR_2j_fromW1,
	    dR_2j_fromW2,
	    //
	    dR_Wjets_min,
	    dR_Wjets_max,
	    dR_l_Wjets_min,
	    dR_l_Wjets_max,
	    dR_l_AK4jets_min,
	    dR_l_AK4jets_max,
	    dR_l_leadWjet_min,
	    dR_l_leadWjet_max,
	    dR_l_leadAK4jet_min,
	    dR_l_leadAK4jet_max,
	    //
	    metP4.pt(),
	    mhtP4.pt(),
	    met_LD,
	    //HT,
            //STMET,
	    //
	    mT_lep1_met,
	    mT_lep2_met,
	    //
	    eventCategory,
	    //
	    nTaus,
	    //
	    //
	    mindr_lep1_jet,
	    mindr_lep2_jet,
	    pT_ll,
	    max_lep_eta,
	    pT_llMEt,
	    Smin_llMEt,
	    lep1_conePt,
	    selLepton_lead->eta(),
	    lep2_conePt,
	    selLepton_sublead->eta(),
	    //
	    //
	    //
 	    BDTOutput_Map_spin0,
	    BDTOutput_Map_spin2,
	    BDTOutput_Map_nonRes,
	    //
	    //
           evtWeight);

	  for(const std::string & category: evtCategories)
	  {
	    EvtHistManager_hh_2lss_leq1tau* selHistManager_evt_category = selHistManager->evt_in_categories_[category];

	    if (selHistManager_evt_category)
	    {
	      selHistManager_evt_category->fillHistograms(
		selElectrons.size(),
		selMuons.size(),
		selJets.size(),
		numSelJetsPtGt40,
		dihiggsVisMass_sel,
		dihiggsMass_wMet_sel,
		jetMass_sel,
		leptonPairMass_sel,
		( selLepton_lead->is_electron() && selLepton_sublead->is_electron() ) ? leptonPairMass_sel : -1.,
		( selLepton_lead->is_muon()     && selLepton_sublead->is_muon()     ) ? leptonPairMass_sel : -1.,
		leptonPairCharge_sel,
		HT,
		STMET,
		//
		//
		//
		nElectrons_in_2lss,
		//leptonPairMass_sel,
		//leptonPairCharge_sel,
		dR_ll,
		dPhi_ll,
		//
		//nAK4,
		nAK8_w2subjets,
		nWJets_selected,
		//
		mass_2j_fromW1,
		mass_2j_fromW2,
		dR_2j_fromW1,
		dR_2j_fromW2,
		//
		dR_Wjets_min,
		dR_Wjets_max,
		dR_l_Wjets_min,
		dR_l_Wjets_max,
		dR_l_AK4jets_min,
		dR_l_AK4jets_max,
		dR_l_leadWjet_min,
		dR_l_leadWjet_max,
		dR_l_leadAK4jet_min,
		dR_l_leadAK4jet_max,
		//
		metP4.pt(),
		mhtP4.pt(),
		met_LD,
		//HT,
		//STMET,
		//
		mT_lep1_met,
		mT_lep2_met,
		//		
		eventCategory,
		//
		nTaus,
		//
		//	    
		mindr_lep1_jet,
		mindr_lep2_jet,
		pT_ll,
		max_lep_eta,
		pT_llMEt,
		Smin_llMEt,
		lep1_conePt,
		selLepton_lead->eta(),
		lep2_conePt,
		selLepton_sublead->eta(),
		//
		//
		//
		BDTOutput_Map_spin0,
		BDTOutput_Map_spin2,
		BDTOutput_Map_nonRes,
	    //
	    //
		evtWeight);
	    }
	  }
	  
        }
	
	selHistManager->datacard_->fillHistograms(
          BDTOutput_Map_spin2,
          BDTOutput_Map_spin0,
          BDTOutput_Map_nonRes,
          //BDTOutput_Map_nonRes_base["Base"],
	  -1., // CV: BDTOutput for nonresonant_allBMs case not implemented yet !!
          evtWeight);

        if(! skipFilling)
        {
          //static std::map<selHistManagerType*, bool> mvaInputVarCorrelation_isBooked; // key = selHistManager
          //if ( !mvaInputVarCorrelation_isBooked[selHistManager] )
          //{
          //  selHistManager->mvaInputVarCorrelation_->bookHistograms(fs, getKeys(AllVars_Map));
          //  mvaInputVarCorrelation_isBooked[selHistManager] = true;
          //}
          selHistManager->mvaInputVarCorrelation_->fillHistograms(AllVars_Map, evtWeight);
        }

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


    if ( bdt_filler ) {
      double lep1_genLepPt = ( selLepton_lead->genLepton()    ) ? selLepton_lead->genLepton()->pt()    : 0.;
      double lep2_genLepPt = ( selLepton_sublead->genLepton() ) ? selLepton_sublead->genLepton()->pt() : 0.;
      double prob_fake_lepton_lead = evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
      double prob_fake_lepton_sublead = evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);
      double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
      double lep1_frWeight = lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead;
      double lep2_frWeight = lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead;
      evtWeight_BDT *= lep1_frWeight*lep2_frWeight;

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
	("dihiggsVisMass_sel",             dihiggsVisMass_sel)
	("dihiggsMass_wMet_sel",           dihiggsMass_wMet_sel)
	("jetMass_sel",                    jetMass_sel)
	("leptonPairMass_sel",             leptonPairMass_sel)
	("leptonPairCharge_sel",           leptonPairCharge_sel)
	("met",                            metP4.pt())
        ("mht",                            mhtP4.pt())
        ("met_LD",                         met_LD)
        ("HT",                             HT)
        ("STMET",                          STMET)
        ("evtWeight",                      evtWeightRecorder.get(central_or_shift_main))
	("lep1_pt",                        selLepton_lead->pt())
        ("lep1_conePt",                    lep1_conePt)
	("lep1_eta",                       selLepton_lead->eta())
	("mindr_lep1_jet",                 std::min(10., mindr_lep1_jet) )
        ("mT_lep1",                        mT_lep1)
	("lep2_pt",                        selLepton_sublead->pt())
        ("lep2_conePt",                    lep2_conePt)
	("lep2_eta",                       selLepton_sublead->eta())
	("mindr_lep2_jet",                 std::min(10., mindr_lep2_jet) )
        ("mT_lep2",                        mT_lep2)
	("dR_ll",                          dR_ll)
	("pT_ll",                          pT_ll)
	("max_lep_eta",                    TMath::Max(std::abs(selLepton_lead -> eta()), std::abs(selLepton_sublead -> eta())))
	("pT_llMEt",                       pT_llMEt)
	("Smin_llMEt",                     Smin_llMEt)
	("vbf_dEta_jj",                    vbf_dEta_jj)
	("vbf_m_jj",                       vbf_m_jj)
	("nJet",                           comp_n_jet25_recl(selJets))
	("nJet_vbf",                       selJetsVBF.size())
	("isVBF",                          isVBF)
	("nLep",                           selLeptons.size())
        ("nLep_loose",                     preselLeptonsFull.size())
        ("nElec",                          selElectrons.size())
	//
	//
	//	
	("nElectrons_in_2lss",             nElectrons_in_2lss)
	//("leptonPairCharge_sel",          leptonPairCharge_sel)
	//("leptonPairMass_sel",            leptonPairMass_sel)
	//("dR_ll",                         dR_ll)
	("dPhi_ll",                        dPhi_ll)
	//
	//("nAK4",                          nAK4)
	("nAK8_w2subjets",                 nAK8_w2subjets)
	("nWJets_selected",                nWJets_selected)
	//
	("mass_2j_fromW1",                 mass_2j_fromW1)
	("mass_2j_fromW2",                 mass_2j_fromW2)
	("dR_2j_fromW1",                   dR_2j_fromW1)
	("dR_2j_fromW2",                   dR_2j_fromW2)
	//
	("dR_Wjets_min",                   dR_Wjets_min)
	("dR_Wjets_max",                   dR_Wjets_max)
	("dR_l_Wjets_min",                 dR_l_Wjets_min)

	("dR_l_Wjets_max",                 dR_l_Wjets_max)
	("dR_l_AK4jets_min",               dR_l_AK4jets_min)
	("dR_l_AK4jets_max",               dR_l_AK4jets_max)
	("dR_l_leadWjet_min",              dR_l_leadWjet_min)
	("dR_l_leadWjet_max",              dR_l_leadWjet_max)
	("dR_l_leadAK4jet_min",            dR_l_leadAK4jet_min)
	("dR_l_leadAK4jet_max",            dR_l_leadAK4jet_max)
	//
	//("met",                            metP4.pt())
        //("mht",                            mhtP4.pt())
        //("met_LD",                         met_LD)
        //("HT",                             HT)
        //("STMET",                          STMET)
	//
	("nTaus",                          nTaus)
	("eventCategory",                  eventCategory)
	//
	//
	//
	("THWeight",                       THWeight)
	("BM",                             BM)
	("mhh_gen",                        mhh_gen)
	("costS_gen",                      costS_gen)
	("lep1_frWeight",       lep1_frWeight)
	("lep2_frWeight",       lep2_frWeight)
	("genWeight" , eventInfo.genWeight)
	("lheWeight" , evtWeightRecorder.get_lheScaleWeight(central_or_shift_main))
	("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift_main))
	("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift_main))
	("btagWeight", evtWeightRecorder.get_btag(central_or_shift_main))
	("leptonEffSF", evtWeightRecorder.get_leptonSF())
	("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift_main))
	("FR_Weight", evtWeightRecorder.get_FR(central_or_shift_main))
        ("evtWeight",           evtWeight_BDT)
	(weightMapHH)
        .fill()
	;
    }


    if ( fillBDTOutputTree )
    {
      double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
      
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

      std::map<std::string, double> bdtOutputMap;
      // spin0
      for (size_t imHH=0; imHH < gen_mHH.size(); imHH++)
      {
	TString sNodeName0 = Form("%g_%s",gen_mHH[imHH],vResSpins[0].c_str());
	TString sNodeName = Form("BDTOutput_%s",sNodeName0.Data());
	bdtOutputMap[sNodeName.Data()] = BDTOutput_Map_spin0[sNodeName0.Data()];
      }
      
      // spin2
      for (size_t imHH=0; imHH < gen_mHH.size(); imHH++)
      {
	TString sNodeName0 = Form("%g_%s",gen_mHH[imHH],vResSpins[1].c_str());
	TString sNodeName = Form("BDTOutput_%s",sNodeName0.Data());
	bdtOutputMap[sNodeName.Data()] = BDTOutput_Map_spin2[sNodeName0.Data()];
      }

      // nonres
      for (size_t ibm = 0; ibm < nonRes_BMs.size(); ibm++)
      {
	TString sNodeName = Form("BDTOutput_nonres_%s",nonRes_BMs[ibm].c_str());
	bdtOutputMap[sNodeName.Data()] = BDTOutput_Map_nonRes[nonRes_BMs[ibm].c_str()];	
      }
      
      bdtOutput_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
	("evtWeight",             evtWeight_BDT)
	(weightMapHH)
	(bdtOutputMap)
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
    for(const leptonChargeFlipGenMatchEntry & leptonGenMatch_definition: leptonGenMatch_definitions)
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
  delete hadTauReader;
  delete jetReader;
  delete jetReaderAK8; 
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
  delete genProxyPhotonReader;
  delete genFromHardProcessReader;
  delete genJetReader;
  delete genHiggsReader;
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

  clock.Show("analyze_hh_2lss_leq1tau");

  return EXIT_SUCCESS;
}

