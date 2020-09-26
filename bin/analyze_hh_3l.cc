/*   versionL With AK8LS without H_WW_jj selector
 *   Date: 20200401
 */

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
#include <TLorentzVector.h>
#include <TMath.h>
#include <TROOT.h> // TROOT

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/ObjectMultiplicity.h" // ObjectMultiplicity
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/TMVAInterface.h" // TMVAInterface
#include "tthAnalysis/HiggsToTauTau/interface/XGBInterface.h" // XGBInterface
#include "tthAnalysis/HiggsToTauTau/interface/mvaAuxFunctions.h" // check_mvaInputs, get_mvaInputVariables
#include "tthAnalysis/HiggsToTauTau/interface/mvaInputVariables.h" // auxiliary functions for computing input variables of the MVA used for signal extraction in the 3l category
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
#include "tthAnalysis/HiggsToTauTau/interface/MVAInputVarHistManager.h" // MVAInputVarHistManager
#include "tthAnalysis/HiggsToTauTau/interface/EvtYieldHistManager.h" // EvtYieldHistManager
#include "tthAnalysis/HiggsToTauTau/interface/CutFlowTableHistManager.h" // CutFlowTableHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/LHEInfoHistManager.h" // LHEInfoHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // getBTagWeight_option, getHadTau_genPdgId, isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/leptonGenMatchingAuxFunctions.h" // getLeptonGenMatch_definitions_3lepton, getLeptonGenMatch_string, getLeptonGenMatch_int
#include "tthAnalysis/HiggsToTauTau/interface/GenMatchInterface.h" // GenMatchInterface
#include "tthAnalysis/HiggsToTauTau/interface/fakeBackgroundAuxFunctions.h" // getWeight_3L
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
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // findGenLepton_and_NeutrinoFromWBoson
#include "tthAnalysis/HiggsToTauTau/interface/HHWeightInterface_2.h" // HHWeightInterface
#include "tthAnalysis/HiggsToTauTau/interface/BtagSFRatioFacility.h" // BtagSFRatioFacility

#include "tthAnalysis/HiggsToTauTau/interface/RecoJetCollectionSelectorAK8.h" // RecoJetSelectorAK8
#include "hhAnalysis/multilepton/interface/RecoJetCollectionSelectorAK8_hh_Wjj.h" // RecoJetSelectorAK8_hh_Wjj
#include "hhAnalysis/multilepton/interface/EvtHistManager_hh_3l.h" // EvtHistManager_hh_3l
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader
#include "hhAnalysis/multilepton/interface/EvtWeightRecorderHH.h" // EvtWeightRecorderHH

#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h" // RecoElectronCollectionSelectorFakeable
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h" // RecoMuonCollectionSelectorFakeable

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
#include <TH2.h> // TH2

typedef math::PtEtaPhiMLorentzVector LV;
typedef std::vector<std::string> vstring;

enum { kFR_disabled, kFR_3lepton };

//const int hadTauSelection_antiElectron = 1; // vLoose
//const int hadTauSelection_antiMuon = 1; // Loose
const int hadTauSelection_antiElectron = -1; // not applied
const int hadTauSelection_antiMuon = -1; // not applied


void dumpGenParticles(const std::string& label, const std::vector<GenParticle>& particles)
{
  for ( size_t idxParticle = 0; idxParticle < particles.size(); ++idxParticle ) {
    std::cout << label << " #" << idxParticle << ":" << " ";
    std::cout << particles[idxParticle];
    std::cout << std::endl;
  }
}
/*
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

  for ( size_t idxWBoson = 0; idxWBoson < genWBosons.size(); ++idxWBoson ) {
    bool isMatched = false;
    Particle::LorentzVector genWjjP4 = genWBosons[idxWBoson].p4();
    std::cout << "genWBoson id: " << idxWBoson << std::endl;
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
*/
/*
std::pair<const GenLepton*, const GenParticle*> 
findGenLepton_and_NeutrinoFromWBoson_1(const GenParticle* genWBoson, const std::vector<GenLepton>& genLeptons, const std::vector<GenParticle>& genNeutrinos)
{
  const GenLepton* genLeptonFromWBoson = nullptr;
  const GenParticle* genNeutrinoFromWBoson = nullptr;
  double minDeltaMass = 1.e+3;
  for ( std::vector<GenLepton>::const_iterator genLepton = genLeptons.begin();
	genLepton != genLeptons.end(); ++genLepton ) {
    for ( std::vector<GenParticle>::const_iterator genNeutrino = genNeutrinos.begin();
	  genNeutrino != genNeutrinos.end(); ++genNeutrino ) {
      Particle::LorentzVector genLepton_and_NeutrinoP4 = genLepton->p4() + genNeutrino->p4();
      double deltaMass = TMath::Abs(genLepton_and_NeutrinoP4.mass() - genWBoson->mass());
      double dR = deltaR(genLepton_and_NeutrinoP4, genWBoson->p4());
      //if ( deltaMass < 5 && deltaMass < minDeltaMass && dR < 1. ) {
      if ( deltaMass < 1. && deltaMass < minDeltaMass && dR < 0.01 ) {
	genLeptonFromWBoson = &(*genLepton);
	genNeutrinoFromWBoson = &(*genNeutrino);
	minDeltaMass = deltaMass;
      }
    }
  }
  if (genLeptonFromWBoson && genNeutrinoFromWBoson && 0==1) {
    std::cout<<"W->l nu matching: m(W):"<<genWBoson->mass()<<", m(l nu): "<<(genLeptonFromWBoson->p4()+genNeutrinoFromWBoson->p4()).mass()<<", dR(W, l nu): "<<deltaR((genLeptonFromWBoson->p4()+genNeutrinoFromWBoson->p4()), genWBoson->p4())<<std::endl;
  }
  return std::pair<const GenLepton*, const GenParticle*>(genLeptonFromWBoson, genNeutrinoFromWBoson);
}
*/

/**
 * @brief Produce datacard and control plots for 3l categories.
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

  std::cout << "<analyze_hh_3l>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_hh_3l");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_hh_3l")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_hh_3l");

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
  const int electronSelection = get_selection(electronSelection_string);
  const int muonSelection     = get_selection(muonSelection_string);

  bool apply_leptonGenMatching = cfg_analyze.getParameter<bool>("apply_leptonGenMatching");
  std::vector<leptonGenMatchEntry> leptonGenMatch_definitions = getLeptonGenMatch_definitions_3lepton(true);
  std::cout << leptonGenMatch_definitions;

  GenMatchInterface genMatchInterface(3, apply_leptonGenMatching, false);

  std::cout << "analyze_hh_3l:: Siddh here1" << std::endl;

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;

  const double lep_mva_cut_mu = cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e  = cfg_analyze.getParameter<double>("lep_mva_cut_e");
  

  enum { kOS, kSS };
  std::string leptonChargeSelection_string = cfg_analyze.getParameter<std::string>("leptonChargeSelection");
  int leptonChargeSelection = -1;
  if      ( leptonChargeSelection_string == "OS" ) leptonChargeSelection = kOS;
  else if ( leptonChargeSelection_string == "SS" ) leptonChargeSelection = kSS;
  else throw cms::Exception("analyze_hh_3l")
    << "Invalid Configuration parameter 'leptonChargeSelection' = " << leptonChargeSelection_string << " !!\n";

  std::cout << "analyze_hh_3l:: Siddh here2" << std::endl;
  
  //const int minNumJets = 1;

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
  std::cout << "analyze_hh_3l:: Siddh here3" << std::endl;
  
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
  std::cout << "analyze_hh_3l:: Siddh here4" << std::endl;
  
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
  std::cout << "analyze_hh_3l:: Siddh here5" << std::endl;
  
  edm::ParameterSet cfg_dataToMCcorrectionInterface;
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("era", era_string);
  cfg_dataToMCcorrectionInterface.addParameter<std::string>("hadTauSelection", hadTauSelection_part2);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiElectron", hadTauSelection_antiElectron);
  cfg_dataToMCcorrectionInterface.addParameter<int>("hadTauSelection_antiMuon", hadTauSelection_antiMuon);
  //cfg_dataToMCcorrectionInterface.addParameter<bool>("isDEBUG","True");
  Data_to_MC_CorrectionInterface_Base * dataToMCcorrectionInterface = nullptr;
  switch(era)
  {
    case Era::k2016: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2016(cfg_dataToMCcorrectionInterface); break;
    case Era::k2017: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2017(cfg_dataToMCcorrectionInterface); break;
    case Era::k2018: dataToMCcorrectionInterface = new Data_to_MC_CorrectionInterface_2018(cfg_dataToMCcorrectionInterface); break;
    default: throw cmsException("analyze_hh_3l", __LINE__) << "Invalid era = " << static_cast<int>(era);
  }
  std::cout << "analyze_hh_3l:: Siddh here6" << std::endl;
  std::string applyFakeRateWeights_string = cfg_analyze.getParameter<std::string>("applyFakeRateWeights");
  int applyFakeRateWeights = -1;
  if      ( applyFakeRateWeights_string == "disabled" ) applyFakeRateWeights = kFR_disabled;
  else if ( applyFakeRateWeights_string == "3lepton"  ) applyFakeRateWeights = kFR_3lepton;
  else throw cms::Exception("analyze_hh_3l")
    << "Invalid Configuration parameter 'applyFakeRateWeights' = " << applyFakeRateWeights_string << " !!\n";
  std::cout << "analyze_hh_3l:: Siddh here7  applyFakeRateWeights_string:" << applyFakeRateWeights_string  << ", applyFakeRateWeights: " << applyFakeRateWeights << ", kFR_3lepton: " << kFR_3lepton  << std::endl;
  
  LeptonFakeRateInterface* leptonFakeRateInterface = 0;
  if ( applyFakeRateWeights == kFR_3lepton) {
    edm::ParameterSet cfg_leptonFakeRateWeight = cfg_analyze.getParameter<edm::ParameterSet>("leptonFakeRateWeight");
    std::cout << "analyze_hh_3l:: Siddh here7_1 " << std::endl;
    cfg_leptonFakeRateWeight.addParameter<std::string>("era", era_string);

    std::cout << "analyze_hh_3l:: Siddh here7_2 " << std::endl;

    cfg_leptonFakeRateWeight.addParameter<std::vector<std::string>>("central_or_shifts", central_or_shifts_local);

    leptonFakeRateInterface = new LeptonFakeRateInterface(cfg_leptonFakeRateWeight);
  }
  std::cout << "analyze_hh_3l:: Siddh here8" << std::endl;
  
  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");
  edm::ParameterSet cfg_EvtYieldHistManager = cfg_analyze.getParameter<edm::ParameterSet>("cfgEvtYieldHistManager");
  
  std::string branchName_electrons = cfg_analyze.getParameter<std::string>("branchName_electrons");
  std::string branchName_muons = cfg_analyze.getParameter<std::string>("branchName_muons");
  std::string branchName_hadTaus = cfg_analyze.getParameter<std::string>("branchName_hadTaus");
  //std::string branchName_jets = cfg_analyze.getParameter<std::string>("branchName_jets");
  std::string branchName_jets_ak4 = cfg_analyze.getParameter<std::string>("branchName_jets_ak4");
  std::string branchName_jets_ak8_Wjj = cfg_analyze.getParameter<std::string>("branchName_jets_ak8_Wjj");
  std::string branchName_subjets_ak8_Wjj = cfg_analyze.getParameter<std::string>("branchName_subjets_ak8_Wjj");
  std::string branchName_met = cfg_analyze.getParameter<std::string>("branchName_met");

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

  std::string branchName_genHiggses = cfg_analyze.getParameter<std::string>("branchName_genHiggses");
  std::string branchName_genNeutrinos = cfg_analyze.getParameter<std::string>("branchName_genNeutrinos");
  
  std::string branchName_genWBosons = cfg_analyze.getParameter<std::string>("branchName_genWBosons");
  std::string branchName_genWJets = cfg_analyze.getParameter<std::string>("branchName_genWJets");
  
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
  std::cout << "Number of points being scanned = " << Nscan << '\n';
  if (apply_HH_rwgt)
    {
      std::cout << "\n Weights booked = " << apply_HH_rwgt << '\n';
      for (const std::string catcat : evt_cat_strs) {
	std::cout << catcat << '\n';
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

  RecoJetReader* jetReaderAK4 = new RecoJetReader(era, isMC, branchName_jets_ak4, readGenObjects);
  jetReaderAK4->setPtMass_central_or_shift(jetPt_option);
  jetReaderAK4->read_btag_systematics((central_or_shifts_local.size() > 1 || central_or_shift_main != "central") && isMC);
  inputTree->registerReader(jetReaderAK4);
  RecoJetCollectionGenMatcher jetGenMatcherAK4;
  RecoJetCollectionCleaner jetCleanerAK4_dR04(0.4, isDEBUG);
  RecoJetCollectionCleanerByIndex jetCleanerAK4_byIndex(isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR08(0.8, isDEBUG);
  RecoJetCollectionCleaner jetCleanerAK4_dR12(1.2, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4(era, -1, isDEBUG);
  RecoJetCollectionSelector jetSelectorAK4_vbf(era, -1, isDEBUG);
  jetSelectorAK4_vbf.getSelector().set_max_absEta(4.7);
  RecoJetCollectionSelectorBtagLoose jetSelectorAK4_bTagLoose(era, -1, isDEBUG);
  RecoJetCollectionSelectorBtagMedium jetSelectorAK4_bTagMedium(era, -1, isDEBUG);
  
  // refer analyze_hh_bb1l.cc macro
  RecoJetReaderAK8* jetReaderAK8_Wjj = new RecoJetReaderAK8(era, isMC, branchName_jets_ak8_Wjj, branchName_subjets_ak8_Wjj);
  // TO-DO: implement jet energy scale uncertainties, b-tag weights,  
  //        and jet  pT and (softdrop) mass corrections described in Section 3.4.3 of AN-2018/058 (v4)
  inputTree->registerReader(jetReaderAK8_Wjj);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR08(0.8, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR12(1.2, isDEBUG);
  RecoJetCollectionCleanerAK8 jetCleanerAK8_dR16(1.6, isDEBUG);
  RecoJetCollectionSelectorAK8 jetSelectorAK8(era, -1, isDEBUG);
  RecoJetCollectionSelectorAK8_hh_Wjj jetSelectorAK8_Wjj(era, -1, isDEBUG);
  
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
  GenParticleReader * genHiggsReader = nullptr;
  GenParticleReader * genNeutrinoReader = nullptr;
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
      inputTree -> registerReader(genPhotonReader);
      genJetReader = new GenJetReader(branchName_genJets);
      inputTree -> registerReader(genJetReader);
      genNeutrinoReader = new GenParticleReader(branchName_genNeutrinos);
      inputTree->registerReader(genNeutrinoReader);

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
    genHiggsReader = new GenParticleReader(branchName_genHiggses);
    inputTree->registerReader(genHiggsReader);
    lheInfoReader = new LHEInfoReader(hasLHE);
    inputTree -> registerReader(lheInfoReader);
    psWeightReader = new PSWeightReader(hasPS, apply_LHE_nom);
    inputTree -> registerReader(psWeightReader);
  }

  GenParticleReader* genWBosonReader = nullptr;
  GenParticleReader* genWJetReader = nullptr;
  if ( isMC ) {
    genWBosonReader = new GenParticleReader(branchName_genWBosons);
    inputTree->registerReader(genWBosonReader);
    genWJetReader = new GenParticleReader(branchName_genWJets);
    inputTree->registerReader(genWJetReader);
  }

  //std::string mvaFileName_hh_3l_SUMBk_HH_pkl = "hhAnalysis/multilepton/data/3l_0tau_HH_XGB_noTopness_evtLevelSUM_HH_res_26Var.pkl"; 
  std::string mvaFileName_hh_3l_SUMBk_HH_xml = "hhAnalysis/multilepton/data/3l_0tau_HH_XGB_noTopness_evtLevelSUM_HH_res_26Var.xml";
  std::vector<std::string> mvaInputs_hh_3l_SUMBk_HH = {
    "lep1_conePt", "lep1_eta", "mindr_lep1_jet", "mT_lep1",
    "lep2_conePt", "lep2_eta", "mindr_lep2_jet", "mT_lep2",
    "lep3_conePt", "lep3_eta", "mindr_lep3_jet", "mT_lep3",
    "avg_dr_jet", "dr_leps", "dr_lss", "dr_los1", "dr_los2",
    "met_LD", "m_jj", "diHiggsMass", "mTMetLepton1", "mTMetLepton2",
    "nJet", "nElectron", "sumLeptonCharge", "numSameFlavor_OS"
  };
  //XGBInterface mva_xgb_hh_3l_SUMBk_HH(mvaFileName_hh_3l_SUMBk_HH_pkl, mvaInputs_hh_3l_SUMBk_HH);
  TMVAInterface *mva_tmva_hh_3l_SUMBk_HH = new TMVAInterface(mvaFileName_hh_3l_SUMBk_HH_xml, mvaInputs_hh_3l_SUMBk_HH);
  mva_tmva_hh_3l_SUMBk_HH->enableBDTTransform();

  bool selectBDT = ( cfg_analyze.exists("selectBDT") ) ? cfg_analyze.getParameter<bool>("selectBDT") : false;

//--- open output file containing run:lumi:event numbers of events passing final event selection criteria
  std::ostream* selEventsFile = ( selEventsFileName_output != "" ) ? new std::ofstream(selEventsFileName_output.data(), std::ios::out) : 0;
  
  std::cout << "process: " << process_string << std::endl;

  vstring categories_evt = {
    "hh_WjjBoosted", "hh_WjjResolved", "hh_WjjHasOnly1j",
    //"hh_3lneg", "hh_3lpos",
    //"hh_3l_nonVBF", "hh_3l_VBF"
    "hh_3e", "hh_3mu", "hh_2e1mu", "hh_1e2mu",
  };

  bool skipHHDecayModeHistograms = true;
  
//--- declare histograms
  struct selHistManagerType
  {
    ElectronHistManager* electrons_;
    std::map<std::string, ElectronHistManager*> electrons_in_categories_;
    MuonHistManager* muons_;
    std::map<std::string, MuonHistManager*> muons_in_categories_;
    HadTauHistManager* hadTaus_;
    JetHistManager* jetsAK4_;
    JetHistManager* leadJetAK4_;
    JetHistManager* subleadJetAK4_;
    JetHistManagerAK8* jetsAK8_Wjj_;
    JetHistManager* BJetsAK4_loose_;
    JetHistManager* leadBJetAK4_loose_;
    JetHistManager* subleadBJetAK4_loose_;
    JetHistManager* BJetsAK4_medium_;
    MEtHistManager* met_;
    MEtFilterHistManager* metFilters_;
    std::map<std::string, EvtHistManager_hh_3l*> evt_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_3l*>> evt_in_categories_;
    std::map<std::string, std::map<std::string, EvtHistManager_hh_3l*>> evt_in_decayModes_;
    std::map<std::string, std::map<std::string, std::map<std::string, EvtHistManager_hh_3l*>>> evt_in_categories_and_decayModes_;
    EvtYieldHistManager* evtYield_;
    WeightHistManager* weights_;
  };

  std::map<std::string, GenEvtHistManager*> genEvtHistManager_beforeCuts;
  std::map<std::string, GenEvtHistManager*> genEvtHistManager_afterCuts;
  std::map<std::string, LHEInfoHistManager*> lheInfoHistManager;
  std::map<std::string, std::map<int, selHistManagerType*>> selHistManagers;

  std::map<int, TH1*> hMEt_All_0 ;
  std::map<int, TH1*> hHt_All_0;
  std::map<int, TH1*> hMEt_LD_All_0;
  std::map<int, TH1*> hHT_All_0;
  std::map<int, TH1*> hSTMET_All_0;
  //
  std::map<int, TH1*> hMEt_SFOS_0;
  std::map<int, TH1*> hHt_SFOS_0;
  std::map<int, TH1*> hMEt_LD_SFOS_0;
  std::map<int, TH1*> hHT_SFOS_0;
  std::map<int, TH1*> hSTMET_SFOS_0;
  //
  std::map<int, TH1*> hMEt_All_1;
  std::map<int, TH1*> hHt_All_1;
  std::map<int, TH1*> hMEt_LD_All_1;
  std::map<int, TH1*> hHT_All_1;
  std::map<int, TH1*> hSTMET_All_1;
  //
  std::map<int, TH1*> hMEt_SFOS_1;
  std::map<int, TH1*> hHt_SFOS_1;
  std::map<int, TH1*> hMEt_LD_SFOS_1;
  std::map<int, TH1*> hHT_SFOS_1;
  std::map<int, TH1*> hSTMET_SFOS_1;
  //
  std::map<int, TH1*> hm_2lpreselUnclean_0;
  std::map<int, TH1*> hm_2lpreselUnclean_1;
  std::map<int, TH1*> hm_SFOS2lpresel_0;
  std::map<int, TH1*> hm_SFOS2lpresel_1;
  std::map<int, TH1*> hm_SFOS4lpresel_0;
  std::map<int, TH1*> hm_SFOS4lpresel_1;

  //TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  //std::map<std::string, std::map<int, TH1*>> hMEt_All_0;

  
  for(const std::string & central_or_shift: central_or_shifts_local)
  {
    const bool skipBooking = central_or_shift != central_or_shift_main;
    std::vector<const GenMatchEntry*> genMatchDefinitions = genMatchInterface.getGenMatchDefinitions();
    for (const GenMatchEntry * genMatchDefinition : genMatchDefinitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += genMatchDefinition->getName();      
      
      int idxLepton = genMatchDefinition->getIdx();

      std::cout << "process_and_genMatch: " << process_and_genMatch << ", \t histogramDir: " << histogramDir.data()
		<< ",\t idxLepton: " << idxLepton << std::endl;

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
        selHistManager->jetsAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/jetsAK4", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jetsAK4_->bookHistograms(fs);
        selHistManager->leadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
        selHistManager->leadJetAK4_->bookHistograms(fs);
        selHistManager->subleadJetAK4_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadJetAK4", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
        selHistManager->subleadJetAK4_->bookHistograms(fs);
        selHistManager->jetsAK8_Wjj_ = new JetHistManagerAK8(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/jetsAK8_Wjj", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->jetsAK8_Wjj_->bookHistograms(fs);
        selHistManager->BJetsAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/BJetsAK4_loose", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->BJetsAK4_loose_->bookHistograms(fs);
        selHistManager->leadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/leadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 0));
        selHistManager->leadBJetAK4_loose_->bookHistograms(fs);
        selHistManager->subleadBJetAK4_loose_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/subleadBJetAK4_loose", histogramDir.data()), era_string, central_or_shift, "minimalHistograms", 1));
        selHistManager->subleadBJetAK4_loose_->bookHistograms(fs);
        selHistManager->BJetsAK4_medium_ = new JetHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/BJetsAK4_medium", histogramDir.data()), era_string, central_or_shift, "allHistograms"));
        selHistManager->BJetsAK4_medium_->bookHistograms(fs);
        selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/met", histogramDir.data()), era_string, central_or_shift));
        selHistManager->met_->bookHistograms(fs);
        selHistManager->metFilters_ = new MEtFilterHistManager(makeHistManager_cfg(process_and_genMatch,
          Form("%s/sel/metFilters", histogramDir.data()), era_string, central_or_shift));
        selHistManager->metFilters_->bookHistograms(fs);
      }

      for(const std::string & evt_cat_str: evt_cat_strs)
      {
	std::cout << "\t evt_cat_str: " << evt_cat_str << std::endl;
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
	std::cout << "\t evt_cat_str: " << evt_cat_str << "\t process_string_new: " << process_string_new << ", process_and_genMatchName: " << process_and_genMatchName << std::endl;
        selHistManager->evt_[evt_cat_str] = new EvtHistManager_hh_3l(makeHistManager_cfg(process_and_genMatchName,
          Form("%s/sel/evt", histogramDir.data()), era_string, central_or_shift));
        selHistManager->evt_[evt_cat_str]->bookHistograms(fs);
      }

      // additional histograms
      //book1D(dir, "numElectrons",    "numElectrons",      5, -0.5,  +4.5);
      
      
      for(const std::string & category: categories_evt)
      {
	std::cout << "\t category: " << category << std::endl;
        TString histogramDir_category = histogramDir.data();
        histogramDir_category.ReplaceAll("hh_3l", Form("%s", category.data()));

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
	  std::cout << "\t\t evt_cat_str: " << evt_cat_str << "\t process_string_new: " << process_string_new << ", process_and_genMatchName: " << process_and_genMatchName << std::endl;
          selHistManager->evt_in_categories_[evt_cat_str][category] = new EvtHistManager_hh_3l(makeHistManager_cfg(process_and_genMatchName,
            Form("%s/sel/evt", histogramDir_category.Data()), era_string, central_or_shift));
          selHistManager->evt_in_categories_[evt_cat_str][category]->bookHistograms(fs);
        }
      }
      const vstring decayModes_evt = eventInfo.getDiHiggsDecayModes();
      if(isSignal && !skipHHDecayModeHistograms)
      {
        for(const std::string & decayMode_evt: decayModes_evt)
        {
          std::string decayMode_and_genMatch = process_string;
	  decayMode_and_genMatch += ("_DecayMode_" + decayMode_evt);
	  decayMode_and_genMatch += genMatchDefinition->getName();
	  std::cout << "\t decayMode_evt: " << decayMode_evt
		    << ", decayMode_and_genMatch: " << decayMode_and_genMatch << std::endl;
	  
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
	    std::cout << "\t\t evt_cat_str: " << evt_cat_str << "\t process_string_new: " << process_string_new << ", decayMode_and_genMatchName: " << decayMode_and_genMatchName << std::endl;
            selHistManager -> evt_in_decayModes_[evt_cat_str][decayMode_evt] = new EvtHistManager_hh_3l(makeHistManager_cfg(
              decayMode_and_genMatchName,
              Form("%s/sel/evt", histogramDir.data()),
              era_string,
              central_or_shift
            ));
            selHistManager -> evt_in_decayModes_[evt_cat_str][decayMode_evt] -> bookHistograms(fs);

            for(const std::string & category: categories_evt)
            {
              TString histogramDir_category = histogramDir.data();
              histogramDir_category.ReplaceAll("hh_3l", Form("%s", category.data()));
              selHistManager -> evt_in_categories_and_decayModes_[evt_cat_str][category][decayMode_evt] = new EvtHistManager_hh_3l(makeHistManager_cfg(
                decayMode_and_genMatchName,
                Form("%s/sel/evt", histogramDir_category.Data()),
                era_string,
                central_or_shift
              ));
              selHistManager -> evt_in_categories_and_decayModes_[evt_cat_str][category][decayMode_evt] -> bookHistograms(fs);
            }
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
        selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight", "triggerWeight", "data_to_MC_correction", "fakeRate" });
      }
      selHistManagers[central_or_shift][idxLepton] = selHistManager;

      if (central_or_shift == central_or_shift_main) {
	//TFileDirectory subD1   = fs.mkdir(Form("%s/sel/evt/%s", histogramDir.data(),process_string.data()));
	TFileDirectory subD1   = fs.mkdir(Form("%s/sel/evt/%s", histogramDir.data(),process_and_genMatch.data()));
	hMEt_All_0[idxLepton]        = subD1.make<TH1D>("hMEt_All_0", "hMEt_All_0", 200, 0.,500.);
	hHt_All_0[idxLepton]         = subD1.make<TH1D>("hHt_All_0", "hHt_All_0", 200, 0.,500.);
	hMEt_LD_All_0[idxLepton]     = subD1.make<TH1D>("hMEt_LD_All_0", "hMEt_LD_All_0", 200, 0.,500.);
	hHT_All_0[idxLepton]         = subD1.make<TH1D>("hHT_All_0", "hHT_All_0", 200, 0.,1000.);
	hSTMET_All_0[idxLepton]      = subD1.make<TH1D>("hSTMET_All_0", "hSTMET_All_0", 200, 0.,1000.);
	//
	hMEt_SFOS_0[idxLepton]       = subD1.make<TH1D>("hMEt_SFOS_0", "hMEt_SFOS_0", 200, 0.,500.);
	hHt_SFOS_0[idxLepton]        = subD1.make<TH1D>("hHt_SFOS_0", "hHt_SFOS_0", 200, 0.,500.);
	hMEt_LD_SFOS_0[idxLepton]    = subD1.make<TH1D>("hMEt_LD_SFOS_0", "hMEt_LD_SFOS_0", 200, 0.,500.);
	hHT_SFOS_0[idxLepton]        = subD1.make<TH1D>("hHT_SFOS_0", "hHT_SFOS_0", 200, 0.,1000.);
	hSTMET_SFOS_0[idxLepton]     = subD1.make<TH1D>("hSTMET_SFOS_0", "hSTMET_SFOS_0", 200, 0.,1000.);
	//
	hMEt_All_1[idxLepton]        = subD1.make<TH1D>("hMEt_All_1", "hMEt_All_1", 200, 0.,500.);
	hHt_All_1[idxLepton]         = subD1.make<TH1D>("hHt_All_1", "hHt_All_1", 200, 0.,500.);
	hMEt_LD_All_1[idxLepton]     = subD1.make<TH1D>("hMEt_LD_All_1", "hMEt_LD_All_1", 200, 0.,500.);
	hHT_All_1[idxLepton]         = subD1.make<TH1D>("hHT_All_1", "hHT_All_1", 200, 0.,1000.);
	hSTMET_All_1[idxLepton]      = subD1.make<TH1D>("hSTMET_All_1", "hSTMET_All_1", 200, 0.,1000.);
	//
	hMEt_SFOS_1[idxLepton]       = subD1.make<TH1D>("hMEt_SFOS_1", "hMEt_SFOS_1", 200, 0.,500.);
	hHt_SFOS_1[idxLepton]        = subD1.make<TH1D>("hHt_SFOS_1", "hHt_SFOS_1", 200, 0.,500.);
	hMEt_LD_SFOS_1[idxLepton]    = subD1.make<TH1D>("hMEt_LD_SFOS_1", "hMEt_LD_SFOS_1", 200, 0.,500.);
	hHT_SFOS_1[idxLepton]        = subD1.make<TH1D>("hHT_SFOS_1", "hHT_SFOS_1", 200, 0.,1000.);
	hSTMET_SFOS_1[idxLepton]     = subD1.make<TH1D>("hSTMET_SFOS_1", "hSTMET_SFOS_1", 200, 0.,1000.);
	//
	hm_2lpreselUnclean_0[idxLepton]     = subD1.make<TH1D>("hm_2lpreselUnclean_0",    "hm_2lpreselUnclean_0",     200, 0.,200.);
	hm_2lpreselUnclean_1[idxLepton]     = subD1.make<TH1D>("hm_2lpreselUnclean_1",    "hm_2lpreselUnclean_1",     200, 0.,200.);
	hm_SFOS2lpresel_0[idxLepton]        = subD1.make<TH1D>("hm_SFOS2lpresel_0",       "hm_SFOS2lpresel_0",        200, 0.,200.);
	hm_SFOS2lpresel_1[idxLepton]        = subD1.make<TH1D>("hm_SFOS2lpresel_1",       "hm_SFOS2lpresel_1",        200, 0.,200.);
	hm_SFOS4lpresel_0[idxLepton]        = subD1.make<TH1D>("hm_SFOS4lpresel_0",       "hm_SFOS4lpresel_0",        200, 0.,500.);
	hm_SFOS4lpresel_1[idxLepton]        = subD1.make<TH1D>("hm_SFOS4lpresel_1",       "hm_SFOS4lpresel_1",        200, 0.,500.);
      }
      
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

  
  
  NtupleFillerBDT<float, int> * bdt_filler = nullptr;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::float_type float_type;
  typedef std::remove_pointer<decltype(bdt_filler)>::type::int_type   int_type;
  if ( selectBDT ) {
    bdt_filler = new std::remove_pointer<decltype(bdt_filler)>::type(
      makeHistManager_cfg(process_string, Form("%s/sel/evtntuple", histogramDir.data()), era_string, central_or_shift_main)
    );
    for(const std::string & evt_cat_str: HHWeightNames)
      {
    	if (!apply_HH_rwgt) continue;
	bdt_filler->register_variable<float_type>(Form(evt_cat_str.c_str()));
      }
    bdt_filler -> register_variable<float_type>(
      "lep1_pt", "lep1_conePt", "lep1_eta", "mindr_lep1_jet", "mT_MEtLep1",
      "lep2_pt", "lep2_conePt", "lep2_eta", "mindr_lep2_jet", "mT_MEtLep2",
      "lep3_pt", "lep3_conePt", "lep3_eta", "mindr_lep3_jet", "mT_MEtLep3",
      //
      "jet1_pt", "jet2_pt", "jet1plus2pt", "jet1_m", "jet2_m",
      //
      "avg_dr_jet", "dr_Wjj",
      //
      "dr_l12", "dr_l23", "dr_l13", "dr_lss", "dr_los_min", "dr_los_max",
      //
      "dr_WjjLepIdx3", "dr_Wjet1LepIdx3", "dr_Wjet2LepIdx3", "dr_LepIdx3WjetNear", "dr_LepIdx3WjetFar",
      //
      "met", "mht", "met_LD", "HT", "STMET",
      //
      "mSFOS2l", "m_jj", "diHiggsVisMass", "diHiggsMass", "mTMetLepton1", "mTMetLepton2",
      //
      "lep1_genLepPt", "lep2_genLepPt", "lep3_genLepPt",
      "lep1_fake_prob", "lep2_fake_prob", "lep3_fake_prob",
      "lep1_frWeight", "lep2_frWeight", "lep3_frWeight",
      //
      "mT_LeptonIdx1_Met_Approach0", "mT_LeptonIdx2_Met_Approach0", "mT_LeptonIdx3_Met_Approach0",
      "m_LeptonIdx1_LeptonIdx2_Approach0", "m_LeptonIdx2_LeptonIdx3_Approach0", "m_LeptonIdx1_LeptonIdx3_Approach0",
      "dPhi_LeptonIdx1_LeptonIdx2_Approach0", "dPhi_LeptonIdx2_LeptonIdx3_Approach0", "dPhi_LeptonIdx1_LeptonIdx3_Approach0",
      "dr_LeptonIdx1_LeptonIdx2_Approach0", "dr_LeptonIdx2_LeptonIdx3_Approach0", "dr_LeptonIdx1_LeptonIdx3_Approach0",
      "m_LeptonIdx3_Jet1_Approach0", "dr_LeptonIdx3_Jet1_Approach0",
      "m_LeptonIdx3_JetNear_Approach0", "dr_LeptonIdx3_JetNear_Approach0",
      //
      "mT_LeptonIdx1_Met_Approach2", "mT_LeptonIdx2_Met_Approach2", "mT_LeptonIdx3_Met_Approach2",
      "m_LeptonIdx1_LeptonIdx2_Approach2", "m_LeptonIdx2_LeptonIdx3_Approach2", "m_LeptonIdx1_LeptonIdx3_Approach2",
      "dPhi_LeptonIdx1_LeptonIdx2_Approach2", "dPhi_LeptonIdx2_LeptonIdx3_Approach2", "dPhi_LeptonIdx1_LeptonIdx3_Approach2",
      "dr_LeptonIdx1_LeptonIdx2_Approach2", "dr_LeptonIdx2_LeptonIdx3_Approach2", "dr_LeptonIdx1_LeptonIdx3_Approach2",
      "m_LeptonIdx3_Jet1_Approach2", "dr_LeptonIdx3_Jet1_Approach2",
      "m_LeptonIdx3_JetNear_Approach2", "dr_LeptonIdx3_JetNear_Approach2",      
      //
      "lumiScale", "genWeight", "evtWeight", "lheWeight", "pileupWeight", "triggerWeight", "btagWeight", "leptonEffSF", "data_to_MC_correction", "FR_Weight",
      "lep1_frWeight","lep2_frWeight","lep3_frWeight"
						);
    bdt_filler -> register_variable<int_type>(
      "nElectron", "nMuon", "nLepton", "nJetAK4", "nBJetLoose", "nBJetMedium", "nJetAK8", "nJetAK8_wSelectorAK8_Wjj",
      "sumLeptonCharge_3l", "sumLeptonCharge_FullSel", "numSameFlavor_OS_3l", "numSameFlavor_OS_FullPresel", 
      "lep1_isTight", "lep2_isTight", "lep3_isTight",
      "eventCategory"
					      );
    bdt_filler -> bookTree(fs);
  }
  
  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  std::map<std::string, int> selectedEntries_byGenMatchType;             // key = process_and_genMatch
  std::map<std::string, std::map<std::string, double>> selectedEntries_weighted_byGenMatchType; // key = process_and_genMatch

  std::map<std::string, int> selectedEntries_byDecayModeType;             // key = decayMode_and_genMatch
  std::map<std::string, std::map<std::string, double>> selectedEntries_weighted_byDecayModeType; // key = decayMode_and_genMatch
  
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
    ">= 3 sel leptons",
    "<= 3 tight sel leptons"
    "fakeable lepton trigger match",
    "HLT filter matching",
    "b-jet veto",
    "sel tau veto",
    "lead lepton pT > 25 GeV && sublead lepton pT > 15 GeV && third lepton pT > 10 GeV",
    "sel lepton charge",
    ">= 1 jets from W->jj",
    "m(ll) > 12 GeV",
    "Z-boson mass veto",
    "H->ZZ*->4l veto",
    "met LD",
    "MEt filters",
    "signal region veto",
    "After all cuts: evt category isWjjBoosted",
    "After all cuts: evt category isWjjResolved",
    "After all cuts: evt category isWjjHasOnly1j"
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
         objectMultiplicity.getNRecoLepton(kTight)             > 3  )
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
    std::vector<GenParticle> genNeutrinos;
    std::vector<GenParticle> genHiggses;

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
      if(genHadTauReader)   genHadTaus = genHadTauReader->read();
      if(genPhotonReader)   genPhotons = genPhotonReader->read();
      if(genJetReader)      genJets = genJetReader->read();
      if(genHiggsReader)    genHiggses = genHiggsReader->read();
      if(genNeutrinoReader) genNeutrinos = genNeutrinoReader->read();

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
	printCollection("genHiggses", genHiggses);
      }
    }

    std::vector<GenParticle> genWBosons;
    std::vector<GenParticle> genWJets;
    if ( isMC ) {
      genWBosons = genWBosonReader->read();
      genWJets = genWJetReader->read();
    }
    
    if ( isDEBUG ) {
      dumpGenParticles("genWBoson", genWBosons);
      dumpGenParticles("genWJet", genWJets);
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
    if(electronSelection == muonSelection)
    {
      // for SR, flip region and fake CR
      // doesn't matter if we supply electronSelection or muonSelection here
      selLeptons = selectObjects(muonSelection, preselLeptons, fakeableLeptons, tightLeptons);
    }
    else
    {
      // for MC closure
      // make sure that neither electron nor muon selections are loose
      assert(electronSelection != kLoose && muonSelection != kLoose);
      std::vector<const RecoMuon*> selMuonsFull = selectObjects(muonSelection, preselMuons, fakeableMuons, tightMuons);
      std::vector<const RecoElectron*> selElectronsFull = selectObjects(electronSelection, preselElectrons, fakeableElectrons, tightElectrons);
      const std::vector<const RecoLepton*> selLeptonsFull = mergeLeptonCollections(selElectronsFull, selMuonsFull, isHigherConePt);
      selLeptons = getIntersection(fakeableLeptons, selLeptonsFull, isHigherConePt);
    }
    std::vector<const RecoMuon*> selMuons = getIntersection(preselMuons, selLeptons, isHigherConePt);
    std::vector<const RecoElectron*> selElectrons = getIntersection(preselElectrons, selLeptons, isHigherConePt);

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
    const std::vector<RecoJet> jets_ak4 = jetReaderAK4->read();
    const std::vector<const RecoJet*> jet_ptrs_ak4 = convert_to_ptrs(jets_ak4);
    const std::vector<const RecoJet*> cleanedJetsAK4_wrtLeptons = jetCleanerAK4_dR04(jet_ptrs_ak4, fakeableLeptons);
    const std::vector<const RecoJet*> cleanedJetsAK4 = jetCleaningByIndex ?
      jetCleanerAK4_byIndex(jet_ptrs_ak4, selectBDT ? selLeptons : fakeableLeptons, fakeableHadTaus) :
      jetCleanerAK4_dR04   (jet_ptrs_ak4, selectBDT ? selLeptons : fakeableLeptons, fakeableHadTaus)
    ;
    const std::vector<const RecoJet*> selJetsAK4 = jetSelectorAK4(cleanedJetsAK4, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_loose = jetSelectorAK4_bTagLoose(cleanedJetsAK4, isHigherPt);
    const std::vector<const RecoJet*> selBJetsAK4_medium = jetSelectorAK4_bTagMedium(cleanedJetsAK4, isHigherPt);
    //int numSelJetsPtGt40 = countHighPtObjects(selJetsAK4, 40.);
    
    if(isDEBUG || run_lumi_eventSelector)
    {
      printCollection("uncleanedJetsAK4", jet_ptrs_ak4);
      printCollection("selJetsAK4",       selJetsAK4);
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
      if(genHadTauReader)   genHadTaus = genHadTauReader->read();
      if(genPhotonReader)   genPhotons = genPhotonReader->read();
      if(genJetReader)      genJets = genJetReader->read();
      if(genHiggsReader)    genHiggses = genHiggsReader->read();
      if(genNeutrinoReader) genNeutrinos = genNeutrinoReader->read();

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
	/*
        jetGenMatcherAK4.addGenLeptonMatch    (cleanedJetsAK4_wrtLeptons, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch    (cleanedJetsAK4_wrtLeptons, genHadTaus);
        jetGenMatcherAK4.addGenJetMatchByIndex(cleanedJetsAK4_wrtLeptons, jetGenMatch);
	*/
	jetGenMatcherAK4.addGenLeptonMatch    (selJetsAK4, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch    (selJetsAK4, genHadTaus);
        jetGenMatcherAK4.addGenJetMatchByIndex(selJetsAK4, jetGenMatch);

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
	/*
        jetGenMatcherAK4.addGenLeptonMatch(cleanedJetsAK4_wrtLeptons, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch(cleanedJetsAK4_wrtLeptons, genHadTaus);
        jetGenMatcherAK4.addGenJetMatch   (cleanedJetsAK4_wrtLeptons, genJets);
	*/
        jetGenMatcherAK4.addGenLeptonMatch(selJetsAK4, genLeptons);
        jetGenMatcherAK4.addGenHadTauMatch(selJetsAK4, genHadTaus);
        jetGenMatcherAK4.addGenJetMatch   (selJetsAK4, genJets);
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


//--- compute MHT and linear MET discriminant (met_LD)
    const RecoMEt met_uncorr = metReader->read();
    const RecoMEt met = recompute_met(met_uncorr, jets_ak4, met_option, isDEBUG);
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptonsFull, fakeableHadTaus, selJetsAK4);
    double met_LD = compMEt_LD(met.p4(), mht_p4);

    double HT = compHT(fakeableLeptons, {}, selJetsAK4);
    double STMET = compSTMEt(fakeableLeptons, {}, selJetsAK4, met.p4());



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
    const RecoLepton* selLepton_sublead = selLeptons[1];
    const RecoLepton* selLepton_third = selLeptons[2];
    const leptonGenMatchEntry& selLepton_genMatch = getLeptonGenMatch(leptonGenMatch_definitions, selLepton_lead, selLepton_sublead, selLepton_third);

    if(isMC)
    {
//--- compute event-level weight for data/MC correction of b-tagging efficiency and mistag rate
//   (using the method "Event reweighting using scale factors calculated with a tag and probe method",
//    described on the BTV POG twiki https://twiki.cern.ch/twiki/bin/view/CMS/BTagShapeCalibration )
      evtWeightRecorder.record_btagWeight(selJetsAK4);
      if(btagSFRatioFacility)
      {
        evtWeightRecorder.record_btagSFRatio(btagSFRatioFacility, selJetsAK4.size());
      }

      if(isMC_EWK)
      {
        evtWeightRecorder.record_ewk_jet(selJetsAK4);
        evtWeightRecorder.record_ewk_bjet(selBJetsAK4_medium);
      }

      dataToMCcorrectionInterface->setLeptons({ selLepton_lead, selLepton_sublead, selLepton_third });

//--- apply data/MC corrections for trigger efficiency
      evtWeightRecorder.record_leptonTriggerEff(dataToMCcorrectionInterface);

//--- apply data/MC corrections for efficiencies for lepton to pass loose identification and isolation criteria
      evtWeightRecorder.record_leptonIDSF_recoToLoose(dataToMCcorrectionInterface);

      //std::cout << "Siddh_leptonIDSF:  " << eventInfo << std::endl; 
//--- apply data/MC corrections for efficiencies of leptons passing the loose identification and isolation criteria
//    to also pass the tight identification and isolation criteria
      if(electronSelection == kFakeable && muonSelection == kFakeable)
      {
        //evtWeightRecorder.record_leptonSF(dataToMCcorrectionInterface->getSF_leptonID_and_Iso_looseToFakeable());
	evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface); 
	if ( run_lumi_eventSelector ) {
	  std::cout << "electronSelection == kFakeable && muonSelection == kFakeable:  dataToMCcorrectionInterface->getSF_leptonID_and_Iso_looseToFakeable(): " << dataToMCcorrectionInterface->getSF_leptonID_and_Iso_looseToFakeable() << std::endl;
	}
      }
      else if(electronSelection >= kFakeable && muonSelection >= kFakeable)
      {
        // apply loose-to-tight lepton ID SFs if either of the following is true:
        // 1) both electron and muon selections are tight -> corresponds to SR
        // 2) electron selection is relaxed to fakeable and muon selection is kept as tight -> corresponds to MC closure w/ relaxed e selection
        // 3) muon selection is relaxed to fakeable and electron selection is kept as tight -> corresponds to MC closure w/ relaxed mu selection
        // we allow (2) and (3) so that the MC closure regions would more compatible w/ the SR (1) in comparison
        evtWeightRecorder.record_leptonIDSF_looseToTight(dataToMCcorrectionInterface); // <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< TEST ONLY 
      }
    }

    if(applyFakeRateWeights == kFR_3lepton)
    {
      bool passesTight_lepton_lead = isMatched(*selLepton_lead, tightElectrons) || isMatched(*selLepton_lead, tightMuons);
      bool passesTight_lepton_sublead = isMatched(*selLepton_sublead, tightElectrons) || isMatched(*selLepton_sublead, tightMuons);
      bool passesTight_lepton_third = isMatched(*selLepton_third, tightElectrons) || isMatched(*selLepton_third, tightMuons);
      evtWeightRecorder.record_jetToLepton_FR_lead(leptonFakeRateInterface, selLepton_lead);
      evtWeightRecorder.record_jetToLepton_FR_sublead(leptonFakeRateInterface, selLepton_sublead);
      evtWeightRecorder.record_jetToLepton_FR_third(leptonFakeRateInterface, selLepton_third);
      if(!selectBDT){
      evtWeightRecorder.compute_FR_3l(passesTight_lepton_lead, passesTight_lepton_sublead, passesTight_lepton_third);
      }
    }

    // require exactly three leptons passing tight selection criteria, to avoid overlap with 4l channel
    if ( !(tightLeptonsFull.size() <= 3) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS tightLeptons selection.\n";
        printCollection("tightLeptonsFull", tightLeptonsFull);
      }
      continue;
    }
     cutFlowTable.update("<= 3 tight sel leptons", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("<= 3 tight sel leptons", evtWeightRecorder.get(central_or_shift_main));
   

    // require that trigger paths match event category (with event category based on fakeableLeptons)
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


    if ( (selBJetsAK4_loose.size() >= 2 || selBJetsAK4_medium.size() >= 1) ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS selBJets selection." << std::endl;
	printCollection("selJetsAK4", selJetsAK4);
	printCollection("selBJetsAK4_loose", selBJetsAK4_loose);
	printCollection("selBJetsAK4_medium", selBJetsAK4_medium);
      }
      continue;
    }
    cutFlowTable.update("b-jet veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("b-jet veto", evtWeightRecorder.get(central_or_shift_main));

    
    if ( selHadTaus.size() > 0 ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS selHadTaus veto." << std::endl;
	printCollection("selHadTaus", selHadTaus);
      }
      continue;
    }
    cutFlowTable.update("sel tau veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel tau veto", evtWeightRecorder.get(central_or_shift_main));


    const double minPt_lead = 25.;
    const double minPt_sublead = 15.;
    const double minPt_third = 10.;
    // CV: according to Giovanni, the pT cuts should be applied on cone_pt
    //    (combined efficiency of single lepton, double lepton, and triple lepton triggers assumed to be high,
    //     even if one or two leptons and fakes and hence cone_pt may be significantly smaller than lepton_pt,
    //     on which pT cuts are applied on trigger level)
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

    int sumLeptonCharge_3l = selLepton_lead->charge() + selLepton_sublead->charge() + selLepton_third->charge();
    bool isCharge_SS = std::abs(sumLeptonCharge_3l) >  1;
    bool isCharge_OS = std::abs(sumLeptonCharge_3l) <= 1;
    if ( leptonChargeSelection == kOS && isCharge_SS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge() << ", leptonChargeSelection = OS)" << std::endl;
      }
      continue;
    }
    if ( leptonChargeSelection == kSS && isCharge_OS ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS lepton charge selection." << std::endl;
	std::cout << " (leading selLepton charge = " << selLepton_lead->charge()
		  << ", subleading selLepton charge = " << selLepton_sublead->charge()
		  << ", third selLepton charge = " << selLepton_third->charge() << ", leptonChargeSelection = SS)" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("sel lepton charge", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("sel lepton charge", evtWeightRecorder.get(central_or_shift_main));



    std::vector<RecoJetAK8> jets_ak8_Wjj = jetReaderAK8_Wjj->read();
    std::vector<const RecoJetAK8*> jet_ptrs_ak8_Wjj = convert_to_ptrs(jets_ak8_Wjj);    
    std::vector<const RecoJetAK8*> selJetsAK8_selectorAK8 = jetSelectorAK8(jet_ptrs_ak8_Wjj, isHigherPt); 
    
    if(isDEBUG || run_lumi_eventSelector) 
    {
      printCollection("uncleaned AK8 jets (Wjj)", jet_ptrs_ak8_Wjj);        
    }

    bool isWjjBoosted = false;
    bool isWjjResolved = false;
    bool isWjjHasOnly1j = false;
    
    double AK8JetPt_max = -1.;
    const RecoJetAK8* AK8JetLead = nullptr;
    size_t idxLepton_H_WW_ljj_1 = 9999;
    //for (size_t ijet = 0; ijet < jet_ptrs_ak8_Wjj.size(); ++ijet) {
    for (size_t ijet = 0; ijet < selJetsAK8_selectorAK8.size(); ++ijet) {
      //std::cout << "\tijet: " << ijet << ", pt: " << jet_ptrs_ak8_Wjj[ijet]->pt() << std::endl;
      if (jet_ptrs_ak8_Wjj[ijet]->pt() > AK8JetPt_max) {
	AK8JetPt_max = jet_ptrs_ak8_Wjj[ijet]->pt();
	AK8JetLead = jet_ptrs_ak8_Wjj[ijet];
      }
    }
    
    
    // Seperate out H->WW->lNu jj lepton from H->WW->2l2Nu leptons
    // lepton pair with least dR would be from H->WW->2l2Nu, so the remained lepton would be from H->WW->lNu jj
    // Approach - 0 : Not used    
    size_t idxLepton_H_WW_ljj = 9999;
    size_t idxLepton1_H_WW_ll = 9999;
    size_t idxLepton2_H_WW_ll = 9999;
    double mindRLepton_H_WW_ll = 9999.;
    //size_t idxLepton1_H_WW_ll = -1, idxLepton2_H_WW_ll = -1;
    for (size_t idxLepton1 = 0; idxLepton1 < 3; ++idxLepton1) {
      //std::cout<<"idxLepton1: "<<idxLepton1<<std::endl;
      for (size_t idxLepton2 = idxLepton1+1; idxLepton2 < 3; ++idxLepton2) {
	double dr = deltaR(selLeptons[idxLepton1]->p4(), selLeptons[idxLepton2]->p4());
	if ((selLeptons[idxLepton1]->charge() * selLeptons[idxLepton2]->charge() < 0.) &&
	    (dr < mindRLepton_H_WW_ll) ) {
	  mindRLepton_H_WW_ll = dr;
	  idxLepton1_H_WW_ll  = idxLepton1;
	  idxLepton2_H_WW_ll  = idxLepton2;
	  idxLepton_H_WW_ljj  = 0;
	  if (idxLepton_H_WW_ljj == idxLepton1) idxLepton_H_WW_ljj++;
	  if (idxLepton_H_WW_ljj == idxLepton2) idxLepton_H_WW_ljj++;
	  //idxLepton1_H_WW_ll = idxLepton1;
	  //idxLepton2_H_WW_ll = idxLepton2;
	}
      }
    }
    if ( isDEBUG ) {
      std::cout << "idxLepton_H_WW_ljj: " << idxLepton_H_WW_ljj
		<< ", idxLepton1_H_WW_ll: " << idxLepton1_H_WW_ll
		<< ", idxLepton2_H_WW_ll: " << idxLepton2_H_WW_ll
		<< std::endl;
    }
 

    // Seperate out H->WW->lNu jj lepton from H->WW->2l2Nu leptons
    // lepton pair with least dR would be from H->WW->2l2Nu, so the remained lepton would be from H->WW->lNu jj
    // Approach - I
    if (AK8JetLead) {
      for (size_t idxLepton1 = 0; idxLepton1 < 3; ++idxLepton1) {
	for (size_t idxLepton2 = idxLepton1+1; idxLepton2 < 3; ++idxLepton2) {
	  // no need to check opposite-sign lepton pair
	  if (selLeptons[idxLepton1]->charge() * selLeptons[idxLepton2]->charge() < 0.) continue;

	  if ( deltaR(AK8JetLead->p4(), selLeptons[idxLepton1]->p4()) <
	       deltaR(AK8JetLead->p4(), selLeptons[idxLepton2]->p4()) ) {
	    idxLepton_H_WW_ljj_1 = idxLepton1;
	  } else {
	    idxLepton_H_WW_ljj_1 = idxLepton2;
	  }
	}
      }
    }
    if ( isDEBUG ) std::cout << "idxLepton_H_WW_ljj_1: " << idxLepton_H_WW_ljj_1 << std::endl;
    
    const RecoLepton* selLepton_H_WW_ljj = nullptr;
    const RecoLepton* selLepton1_H_WW_ll = nullptr;
    const RecoLepton* selLepton2_H_WW_ll = nullptr;
    std::vector<const RecoJetAK8*> selJetsAK8_Wjj_wSelectorAK8_Wjj;
    std::vector<const RecoJetAK8*> selJetsAK8_Wjj;
    std::vector<const RecoJet*> selJetsAK4_Wjj;
    const RecoJetAK8* selJetAK8_Wjj = nullptr;
    const RecoJetBase* selJet1_Wjj = nullptr;
    const RecoJetBase* selJet2_Wjj = nullptr;


     if (idxLepton_H_WW_ljj < 3) { // Approach - 0 
       selLepton_H_WW_ljj = selLeptons[idxLepton_H_WW_ljj]; 
       selLepton1_H_WW_ll = selLeptons[idxLepton1_H_WW_ll];
       selLepton2_H_WW_ll = selLeptons[idxLepton2_H_WW_ll];
     }
     

    jetSelectorAK8_Wjj.getSelector().set_leptons({selLeptons[0], selLeptons[1], selLeptons[2]});
    selJetsAK8_Wjj_wSelectorAK8_Wjj = jetSelectorAK8_Wjj(jet_ptrs_ak8_Wjj, isHigherPt);
    
    selJetsAK8_Wjj = selJetsAK8_Wjj_wSelectorAK8_Wjj; // using AK8LS_H_WW_jj selector
    //selJetsAK8_Wjj = jet_ptrs_ak8_Wjj; // without using AK8LS_H_WW_jj selector, just use AK8LS
    //selJetsAK8_Wjj = selJetsAK8_selectorAK8; // without using AK8LS_H_WW_jj selector, just use AK8LS
     
    selJetsAK4_Wjj = jetSelectorAK4(cleanedJetsAK4, isHigherPt);


    
    if (selJetsAK8_Wjj.size() >= 1 && selJetsAK8_Wjj[0] && selJetsAK8_Wjj[0]->subJet1() && selJetsAK8_Wjj[0]->subJet2()) {  // using AK8LS_H_WW_jj selector
      selJetAK8_Wjj = selJetsAK8_Wjj[0];
      selJet1_Wjj = selJetAK8_Wjj->subJet1();
      selJet2_Wjj = selJetAK8_Wjj->subJet2();
      isWjjBoosted = true;
      assert(selJet1_Wjj && selJet2_Wjj);
    } else {      
      double minRank = 1.e+3;
      // Question: use selJetsAK4 (cleaned w.r.t fakable lepton and tau jets) or selJetsAK4_Wjj (cleaned w.r.t fakable lepton only) for non-boosted AK4 jets
      for ( std::vector<const RecoJet*>::const_iterator selJet1 = selJetsAK4_Wjj.begin();
	    selJet1 != selJetsAK4_Wjj.end(); ++selJet1 ) {
	for ( std::vector<const RecoJet*>::const_iterator selJet2 = selJet1 + 1;
	      selJet2 != selJetsAK4_Wjj.end(); ++selJet2 ) {
	  Particle::LorentzVector jjP4 = (*selJet1)->p4() + (*selJet2)->p4();
	  double m_jj = jjP4.mass();
	  double pT_jj = jjP4.pt();
	  double rank = TMath::Abs(m_jj - wBosonMass)/TMath::Sqrt(TMath::Max(10., pT_jj));
	  if ( rank < minRank ) {
	    selJet1_Wjj = (*selJet1);
	    selJet2_Wjj = (*selJet2);
	    minRank = rank;
	  }
	} 
      }
      if ( !selJet1_Wjj && selJetsAK4_Wjj.size() >= 1 ) selJet1_Wjj = selJetsAK4_Wjj[0];
      if ( !selJet2_Wjj && selJetsAK4_Wjj.size() >= 2 ) selJet2_Wjj = selJetsAK4_Wjj[1];
      if ( selJet1_Wjj && selJet2_Wjj ) {
	isWjjResolved = true;
      }
      else {
	if (selJetsAK4_Wjj.size() == 1) {
	  selJet1_Wjj = selJetsAK4_Wjj[0];
	  isWjjHasOnly1j = true;
	}
      }
      if ( isDEBUG ) {
	std::cout << "found resolved W->jj decay:" << std::endl;
	std::cout << "AK4 jet #1:";
	if ( selJet1_Wjj ) std::cout << " pT = " << selJet1_Wjj->pt() << ", eta = " << selJet1_Wjj->eta() << ", phi = " << selJet1_Wjj->phi() << std::endl;
	else std::cout << " N/A" << std::endl;
	std::cout << "AK4 jet #2:";
	if ( selJet2_Wjj ) std::cout << " pT = " << selJet2_Wjj->pt() << ", eta = " << selJet2_Wjj->eta() << ", phi = " << selJet2_Wjj->phi() << std::endl;
	else std::cout << " N/A" << std::endl;
      }
    }

    if (isWjjBoosted)   cutFlowTable.update("AK8 hh_Wjj selector isWjjBoosted", evtWeightRecorder.get(central_or_shift_main));
    if (isWjjResolved)  cutFlowTable.update("AK8 hh_Wjj selector isWjjResolved", evtWeightRecorder.get(central_or_shift_main));
    if (isWjjHasOnly1j) cutFlowTable.update("AK8 hh_Wjj selector isWjjHasOnly1j", evtWeightRecorder.get(central_or_shift_main));
    
    if ( !(selJet1_Wjj || selJet2_Wjj) ) {
      if ( run_lumi_eventSelector ) {
        std::cout << "event " << eventInfo.str() << " FAILS >= 1 jets from W->jj selection\n";
      }
      continue;
    }
    cutFlowTable.update(">= 1 jets from W->jj", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms(">= 1 jets from W->jj", evtWeightRecorder.get(central_or_shift_main));




    
//--- retrieve gen-matching flags    
    std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons);
    int genMatchIdx_0 = 2; // 0: fakes, 1: Convs, 2: non-fakes
    
    if (genMatches.size() != 1) {
      std::cout << "analyze_hh_3l: GenMatches in an event: " << genMatches.size() << "\t\t\t ERROR: Code is not ready for it ****" << std::endl;
      throw cmsException("analyze_hh_3l", __LINE__) << " GenMatches in an event: " << genMatches.size() << "\t\t\t ERROR: Code is not ready for it **** \n";
    }
    
    for (const GenMatchEntry* genMatch : genMatches) {
      //cutFlowTable.update(Form("GenMatch entry Idx %i",genMatch->getIdx()), evtWeightRecorder.get(central_or_shift_main));
      genMatchIdx_0 = genMatch->getIdx();
    }

    
    //Check: failsLowMassVeto
    for(auto lepton1_it = preselLeptonsFullUncleaned.begin(); lepton1_it != preselLeptonsFullUncleaned.end(); ++lepton1_it) {
      const RecoLepton * lepton1 = *lepton1_it;
      for(auto lepton2_it = lepton1_it + 1; lepton2_it != preselLeptonsFullUncleaned.end(); ++lepton2_it) {
	const RecoLepton * lepton2 = *lepton2_it;
	const double mass = (lepton1->p4() + lepton2->p4()).mass();
	hm_2lpreselUnclean_0[genMatchIdx_0]->Fill(mass, evtWeightRecorder.get(central_or_shift_main));
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

    

    for(auto lepton1_it = preselLeptonsFullUncleaned.begin(); lepton1_it != preselLeptonsFullUncleaned.end(); ++lepton1_it) {
      const RecoLepton * lepton1 = *lepton1_it;
      for(auto lepton2_it = lepton1_it + 1; lepton2_it != preselLeptonsFullUncleaned.end(); ++lepton2_it) {
	const RecoLepton * lepton2 = *lepton2_it;
	const double mass = (lepton1->p4() + lepton2->p4()).mass();
	hm_2lpreselUnclean_1[genMatchIdx_0]->Fill(mass, evtWeightRecorder.get(central_or_shift_main));
      }
    }
    
    
    bool isSameFlavor_OS = false;
    double massSameFlavor_OS = -1.;
    int  numSameFlavor_OS_Full = 0;
    for ( std::vector<const RecoLepton*>::const_iterator lepton1 = preselLeptonsFull.begin();
    lepton1 != preselLeptonsFull.end(); ++lepton1 ) {
      for ( std::vector<const RecoLepton*>::const_iterator lepton2 = lepton1 + 1;
      lepton2 != preselLeptonsFull.end(); ++lepton2 ) {
        if ( (*lepton1)->pdgId() == -(*lepton2)->pdgId() ) { // pair of same flavor leptons of opposite charge
          isSameFlavor_OS = true;
	  numSameFlavor_OS_Full++;
          double mass = ((*lepton1)->p4() + (*lepton2)->p4()).mass();
	  hm_SFOS2lpresel_0[genMatchIdx_0]->Fill(mass, evtWeightRecorder.get(central_or_shift_main));
          if ( std::fabs(mass - z_mass) < std::fabs(massSameFlavor_OS - z_mass) ) massSameFlavor_OS = mass;
        }
      }
    }

    bool failsZbosonMassVeto = isSameFlavor_OS && std::fabs(massSameFlavor_OS - z_mass) < z_window;
    if ( failsZbosonMassVeto ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS Z-boson veto." << std::endl;
      }
      continue;
    }
    cutFlowTable.update("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("Z-boson mass veto", evtWeightRecorder.get(central_or_shift_main));

    for ( std::vector<const RecoLepton*>::const_iterator lepton1 = preselLeptonsFull.begin();
	  lepton1 != preselLeptonsFull.end(); ++lepton1 ) {
      for ( std::vector<const RecoLepton*>::const_iterator lepton2 = lepton1 + 1;
	    lepton2 != preselLeptonsFull.end(); ++lepton2 ) {
        if ( (*lepton1)->pdgId() == -(*lepton2)->pdgId() ) { // pair of same flavor leptons of opposite charge
	  double mass = ((*lepton1)->p4() + (*lepton2)->p4()).mass();
	  hm_SFOS2lpresel_1[genMatchIdx_0]->Fill(mass, evtWeightRecorder.get(central_or_shift_main));
        }
      }
    }


    

    // Check: isfailsHtoZZVeto
    for(auto lepton1_it = preselLeptonsFull.begin(); lepton1_it != preselLeptonsFull.end(); ++lepton1_it) {
      const RecoLepton * lepton1 = *lepton1_it;
      for(auto lepton2_it = lepton1_it + 1; lepton2_it != preselLeptonsFull.end(); ++lepton2_it) {
	const RecoLepton * lepton2 = *lepton2_it;
	if(lepton1->pdgId() == -lepton2->pdgId()) {
	  // first pair of same flavor leptons of opposite charge
	  for(auto lepton3_it = preselLeptonsFull.begin(); lepton3_it != preselLeptonsFull.end(); ++lepton3_it) {
	    const RecoLepton * lepton3 = *lepton3_it;
	    if(lepton3 == lepton1 || lepton3 == lepton2) {
	      continue;
	    }
	    for(auto lepton4_it = lepton3_it + 1; lepton4_it != preselLeptonsFull.end(); ++lepton4_it) {
	      const RecoLepton * lepton4 = *lepton4_it;
	      if(lepton4 == lepton1 || lepton4 == lepton2) {
		continue;
	      }
	      
	      if(lepton3->pdgId() == -lepton4->pdgId()) {
		// second pair of same flavor leptons of opposite charge
		const double mass = (lepton1->p4() + lepton2->p4() + lepton3->p4() + lepton4->p4()).mass();
		hm_SFOS4lpresel_0[genMatchIdx_0]->Fill(mass, evtWeightRecorder.get(central_or_shift_main));
	      }
	    }
	  }
	}
      }
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

    for(auto lepton1_it = preselLeptonsFull.begin(); lepton1_it != preselLeptonsFull.end(); ++lepton1_it) {
      const RecoLepton * lepton1 = *lepton1_it;
      for(auto lepton2_it = lepton1_it + 1; lepton2_it != preselLeptonsFull.end(); ++lepton2_it) {
	const RecoLepton * lepton2 = *lepton2_it;
	if(lepton1->pdgId() == -lepton2->pdgId()) {
	  // first pair of same flavor leptons of opposite charge
	  for(auto lepton3_it = preselLeptonsFull.begin(); lepton3_it != preselLeptonsFull.end(); ++lepton3_it) {
	    const RecoLepton * lepton3 = *lepton3_it;
	    if(lepton3 == lepton1 || lepton3 == lepton2) {
	      continue;
	    }
	    for(auto lepton4_it = lepton3_it + 1; lepton4_it != preselLeptonsFull.end(); ++lepton4_it) {
	      const RecoLepton * lepton4 = *lepton4_it;
	      if(lepton4 == lepton1 || lepton4 == lepton2) {
		continue;
	      }
	      
	      if(lepton3->pdgId() == -lepton4->pdgId()) {
		// second pair of same flavor leptons of opposite charge
		const double mass = (lepton1->p4() + lepton2->p4() + lepton3->p4() + lepton4->p4()).mass();
		hm_SFOS4lpresel_1[genMatchIdx_0]->Fill(mass, evtWeightRecorder.get(central_or_shift_main));
	      }
	    }
	  }
	}
      }
    }




    



    const bool isSameFlavor_OS_FO = isSFOS(fakeableLeptons);
    hMEt_All_0[genMatchIdx_0]->Fill(met.pt(),      evtWeightRecorder.get(central_or_shift_main));
    hHt_All_0[genMatchIdx_0]->Fill(mht_p4.pt(),    evtWeightRecorder.get(central_or_shift_main));
    hMEt_LD_All_0[genMatchIdx_0]->Fill(met_LD,     evtWeightRecorder.get(central_or_shift_main));
    hHT_All_0[genMatchIdx_0]->Fill(HT,             evtWeightRecorder.get(central_or_shift_main));
    hSTMET_All_0[genMatchIdx_0]->Fill(STMET,       evtWeightRecorder.get(central_or_shift_main));
    if (isSameFlavor_OS_FO) {
      hMEt_SFOS_0[genMatchIdx_0]->Fill(met.pt(),   evtWeightRecorder.get(central_or_shift_main));
      hHt_SFOS_0[genMatchIdx_0]->Fill(mht_p4.pt(), evtWeightRecorder.get(central_or_shift_main));
      hMEt_LD_SFOS_0[genMatchIdx_0]->Fill(met_LD,  evtWeightRecorder.get(central_or_shift_main));
      hHT_SFOS_0[genMatchIdx_0]->Fill(HT,          evtWeightRecorder.get(central_or_shift_main));
      hSTMET_SFOS_0[genMatchIdx_0]->Fill(STMET,    evtWeightRecorder.get(central_or_shift_main));
    }
    
    double met_LD_cut = 0.;
    if      ( selJetsAK4.size() >= 4 ) met_LD_cut = -1.; // MET LD cut not applied
    else if ( isSameFlavor_OS_FO     ) met_LD_cut = 45.;
    else                               met_LD_cut = 30.;
    if ( met_LD_cut > 0 && met_LD < met_LD_cut ) {
      if ( run_lumi_eventSelector ) {
    std::cout << "event " << eventInfo.str() << " FAILS MET LD selection." << std::endl;
	std::cout << " (met_LD = " << met_LD << ", met_LD_cut = " << met_LD_cut << ")" << std::endl;
      }
      continue;
    }
    cutFlowTable.update("met LD", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("met LD", evtWeightRecorder.get(central_or_shift_main));

    hMEt_All_1[genMatchIdx_0]->Fill(met.pt(),      evtWeightRecorder.get(central_or_shift_main));
    hHt_All_1[genMatchIdx_0]->Fill(mht_p4.pt(),    evtWeightRecorder.get(central_or_shift_main));
    hMEt_LD_All_1[genMatchIdx_0]->Fill(met_LD,     evtWeightRecorder.get(central_or_shift_main));
    hHT_All_1[genMatchIdx_0]->Fill(HT,             evtWeightRecorder.get(central_or_shift_main));
    hSTMET_All_1[genMatchIdx_0]->Fill(STMET,       evtWeightRecorder.get(central_or_shift_main));
    if (isSameFlavor_OS_FO) {
      hMEt_SFOS_1[genMatchIdx_0]->Fill(met.pt(),   evtWeightRecorder.get(central_or_shift_main));
      hHt_SFOS_1[genMatchIdx_0]->Fill(mht_p4.pt(), evtWeightRecorder.get(central_or_shift_main));
      hMEt_LD_SFOS_1[genMatchIdx_0]->Fill(met_LD,  evtWeightRecorder.get(central_or_shift_main));
      hHT_SFOS_1[genMatchIdx_0]->Fill(HT,          evtWeightRecorder.get(central_or_shift_main));
      hSTMET_SFOS_1[genMatchIdx_0]->Fill(STMET,    evtWeightRecorder.get(central_or_shift_main));
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
    if ( isMCClosure_e || isMCClosure_m ) {
      bool applySignalRegionVeto = (isMCClosure_e && countFakeElectrons(selLeptons) >= 1) || (isMCClosure_m && countFakeMuons(selLeptons) >= 1);
      if ( applySignalRegionVeto && tightLeptons.size() >= 3 ) failsSignalRegionVeto = true;
      //std::cout << "applySignalRegionVeto: " << applySignalRegionVeto << std::endl; 
    } else if ( electronSelection == kFakeable || muonSelection == kFakeable ) {
      if ( tightLeptons.size() >= 3 ) failsSignalRegionVeto = true;
    }
    if ( run_lumi_eventSelector ) {
      std::cout << "isMCClosure_e: " << isMCClosure_e << ", isMCClosure_m: " << isMCClosure_m
		<< ", countFakeElectrons(selLeptons): " << countFakeElectrons(selLeptons)
		<< ", countFakeMuons(selLeptons): " << countFakeMuons(selLeptons)
		<< ", tightLeptons.size(): " << tightLeptons.size()
		<< ", electronSelection: " << electronSelection
		<< ", muonSelection: " << muonSelection
		<< ", failsSignalRegionVeto: " << failsSignalRegionVeto
		<< std::endl;
    }
    if ( failsSignalRegionVeto ) {
      if ( run_lumi_eventSelector ) {
	std::cout << "event " << eventInfo.str() << " FAILS overlap w/ the SR: "
	             "# tight leptons = " << tightLeptons.size() << " >= 3\n"
        ;
	printCollection("tightLeptons", tightLeptons);
      }
      continue; // CV: avoid overlap with signal region
    }
    cutFlowTable.update("signal region veto", evtWeightRecorder.get(central_or_shift_main));
    cutFlowHistManager->fillHistograms("signal region veto", evtWeightRecorder.get(central_or_shift_main));

    if ( run_lumi_eventSelector ) {
      std::cout << "hereSiddh:: " << eventInfo << "\t genMatchIdx_0: " << genMatchIdx_0;
      std::cout << "\nevtWeightRecorder: " << evtWeightRecorder << std::endl; 
    }

    int nEle_3selLep = 0, nMu_3selLep = 0;
    for (size_t i=0; i<3; i++) {
      //std::cout << "lep pdgId: " << selLeptons[i]->pdgId() << std::endl;
      if (abs(selLeptons[i]->pdgId()) == 11) nEle_3selLep++;
      if (abs(selLeptons[i]->pdgId()) == 13) nMu_3selLep++;
    }
    //std::cout << "nEle_3selLep: " << nEle_3selLep << ",  nMu_3selLep: " << nMu_3selLep << std::endl;
  
    std::vector<std::string> evtCategories;		
    if      (isWjjBoosted)   evtCategories.push_back("hh_WjjBoosted");
    else if (isWjjResolved)  evtCategories.push_back("hh_WjjResolved");
    else if (isWjjHasOnly1j) evtCategories.push_back("hh_WjjHasOnly1j");    
    /*if      ( sumLeptonCharge_3l < 0 ) evtCategories.push_back("hh_3lneg");
    else if ( sumLeptonCharge_3l > 0 ) evtCategories.push_back("hh_3lpos");
    if (isVBF) evtCategories.push_back("hh_3l_VBF");	 
    else       evtCategories.push_back("hh_3l_nonVBF");*/
    if      (nEle_3selLep == 3 && nMu_3selLep == 0) evtCategories.push_back("hh_3e");
    else if (nEle_3selLep == 2 && nMu_3selLep == 1) evtCategories.push_back("hh_2e1mu");
    else if (nEle_3selLep == 1 && nMu_3selLep == 2) evtCategories.push_back("hh_1e2mu");
    else if (nEle_3selLep == 0 && nMu_3selLep == 3) evtCategories.push_back("hh_3mu");
    else {
      printf("Invalid event category\t\t nEle_3selLep %d, nMu_3selLep %d",nEle_3selLep,nMu_3selLep);
    }
    //sTmp123 += Form(" isVBF: %i, ",(int)isVBF);

    if ( run_lumi_eventSelector ) {
      std::cout << "evtCategories: ";
      for (size_t i=0; i<evtCategories.size(); i++) std::cout << evtCategories[i] << ",  ";
      std::cout << std::endl;
    }

    for (size_t i=0; i<evtCategories.size(); i++) {
      if (evtCategories[i].compare("hh_3e")    == 0 ||
	  evtCategories[i].compare("hh_2e1mu") == 0 ||
	  evtCategories[i].compare("hh_1e2mu") == 0 ||
	  evtCategories[i].compare("hh_3mu")   == 0  ) {
	if (genMatchIdx_0 == 0) {
	  cutFlowTable.update(Form("signal region veto,  %s ,  genMatchIdx %d",evtCategories[i].data(),genMatchIdx_0), evtWeightRecorder.get(central_or_shift_main));
	}
      } 
    }
    if (genMatchIdx_0 == 0) {
      cutFlowTable.update(Form("signal region veto,  3l ,  genMatchIdx %d",genMatchIdx_0), evtWeightRecorder.get(central_or_shift_main));
    }
    //printf("nselLeptons: %zu, tightLeptons: %zu, fakeableLeptons %zu, tightLeptonsFull %zu, fakeableLeptonsFull %zu \n",selLeptons.size(),tightLeptons.size(),fakeableLeptons.size(),tightLeptonsFull.size(),fakeableLeptonsFull.size());
    if (fakeableLeptonsFull.size() > 3) {
      cutFlowTable.update(Form("pass all selection, nakeableLeptonsFull > 3, genMatchIdx %d",genMatchIdx_0), evtWeightRecorder.get(central_or_shift_main));
    }
    
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



   
    if (isWjjBoosted) {
      cutFlowTable.update("After all cuts: evt category isWjjBoosted", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("After all cuts: evt category isWjjBoosted", evtWeightRecorder.get(central_or_shift_main));
    }
    if (isWjjResolved) {
      cutFlowTable.update("After all cuts: evt category isWjjResolved", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("After all cuts: evt category isWjjResolved", evtWeightRecorder.get(central_or_shift_main));
    }
    if (isWjjHasOnly1j) {
      cutFlowTable.update("After all cuts: evt category isWjjHasOnly1j", evtWeightRecorder.get(central_or_shift_main));
      cutFlowHistManager->fillHistograms("After all cuts: evt category isWjjHasOnly1j", evtWeightRecorder.get(central_or_shift_main));
    }
    





    // SS: Yet to implement this for hh->wwww
    double dihiggsVisMass_sel = -1., dihiggsMass = -1.;
    double WTojjMass = -1.;

    if (selJet1_Wjj && selJet2_Wjj) {
      dihiggsVisMass_sel = (selLepton_lead->p4() + selLepton_sublead->p4() + selLepton_third->p4() + selJet1_Wjj->p4() + selJet2_Wjj->p4()).mass();
      dihiggsMass        = (selLepton_lead->p4() + selLepton_sublead->p4() + selLepton_third->p4() + selJet1_Wjj->p4() + selJet2_Wjj->p4() + met.p4()).mass();
      WTojjMass = (selJet1_Wjj->p4() + selJet2_Wjj->p4()).mass();
    } else if (selJet1_Wjj) {
      dihiggsVisMass_sel = (selLepton_lead->p4() + selLepton_sublead->p4() + selLepton_third->p4() + selJet1_Wjj->p4()).mass();
      dihiggsMass        = (selLepton_lead->p4() + selLepton_sublead->p4() + selLepton_third->p4() + selJet1_Wjj->p4() + met.p4()).mass();
      WTojjMass = (selJet1_Wjj->p4()).mass();
    }    
    
    int numSameFlavor_OS_3l = 0;
    double mSFOS2l = 0.;
    for (int iLepton1 = 0; iLepton1 < 3; iLepton1++) {
      for (int iLepton2 = iLepton1+1; iLepton2 < 3; iLepton2++) {
	if ( selLeptons[iLepton1]->pdgId() == - selLeptons[iLepton2]->pdgId() ) { // pair of same flavor leptons of opposite charge
	  numSameFlavor_OS_3l++;
	  mSFOS2l = (selLeptons[iLepton1]->p4() + selLeptons[iLepton2]->p4()).mass();
	}
      }
    }
    int numSameFlavor_OS = numSameFlavor_OS_Full;

    int sumLeptonCharge_FullSel = 0;
    for (size_t iLepton1 = 0; iLepton1 < selLeptons.size(); iLepton1++) {
      sumLeptonCharge_FullSel += selLeptons[iLepton1]->charge();
    }

    double mTMetLepton1 = -1.;
    double mTMetLepton2 = -1.;
    for (int iLepton1 = 0; iLepton1 < 3; iLepton1++) {
      if (selLeptons[iLepton1]->charge() == sumLeptonCharge_3l) {
	//double e = (met.p4() + selLeptons[iLepton1]->p4()).E();
	//double z = (met.p4() + selLeptons[iLepton1]->p4()).Pz();
	//double mT = std::sqrt(e*e - z*z);
        double mT = comp_MT_met(selLeptons[iLepton1], met.pt(), met.phi());
	if (mT < 0.) std::cout << "analyze_hh_3l:: mT (MET+Lepton) < 0 \t\t *** ERROR ***" << std::endl;
	if (mTMetLepton1 < 0.) 			 mTMetLepton1 = mT;
	else if (mTMetLepton2 < 0.)  mTMetLepton2 = mT;
      }
    }

    
    // 		VBF, nonVBF categorization -----    
    std::vector<const RecoJetBase*> selJets_Wjj;
    if ( selJet1_Wjj) {
      selJets_Wjj.push_back(selJet1_Wjj);
    }
    if ( selJet2_Wjj) {
      selJets_Wjj.push_back(selJet2_Wjj);
    }
    
    
    //std::vector<const RecoJet*> cleanedJetsVBF = jetCleaner(cleanedJets, selJets_Wjj);
    //std::vector<const RecoJet*> cleanedJetsVBF = jetCleanerAK4_dR04(cleanedJetsAK4_wrtLeptons, selJets_Wjj);
    std::vector<const RecoJet*> cleanedJetsVBF = jetCleanerAK4_dR04(selJetsAK4, selJets_Wjj);
    std::vector<const RecoJet*> selJetsVBF = jetSelectorAK4_vbf(cleanedJetsVBF, isHigherPt);
    
    double vbf_dEta_jj = -1.;
    double vbf_m_jj = -1.;
    bool isVBF = false;
    const RecoJet* selJet_vbf_lead = nullptr;
    const RecoJet* selJet_vbf_sublead = nullptr;		
    for ( std::vector<const RecoJet*>::const_iterator selJetVBF1 = selJetsVBF.begin();
	  selJetVBF1 != selJetsVBF.end(); ++selJetVBF1 ) {
      for ( std::vector<const RecoJet*>::const_iterator selJetVBF2 = selJetVBF1 + 1;
	    selJetVBF2 != selJetsVBF.end(); ++selJetVBF2 ) {
	double dEta_jj = TMath::Abs((*selJetVBF1)->eta() - (*selJetVBF2)->eta());
	double m_jj = ((*selJetVBF1)->p4() + (*selJetVBF2)->p4()).mass();
	if ( dEta_jj > 4. && m_jj > 500. ) {
	  if ( m_jj    > vbf_m_jj    ) { // CV: in case of ambiguity, take the jet pair of highest mass
	    vbf_m_jj    = m_jj;
	    vbf_dEta_jj = dEta_jj;
	    selJet_vbf_lead = (*selJetVBF1);
	    selJet_vbf_sublead = (*selJetVBF2);
	    isVBF = true;			
	  }
	}
      }
    }
    
    std::vector<const RecoJet*> selJets_nonVBF;
    if ( selJet_vbf_lead && selJet_vbf_sublead ) {
      std::vector<const RecoJet*> overlaps = { selJet_vbf_lead, selJet_vbf_sublead };
      //std::vector<const RecoJet*> cleanedJets_wrtVBF = jetCleanerAK4_dR04(cleanedJetsAK4_wrtLeptons, overlaps);
      std::vector<const RecoJet*> cleanedJets_wrtVBF = jetCleanerAK4_dR04(selJetsAK4, overlaps);
      selJets_nonVBF = jetSelectorAK4(cleanedJets_wrtVBF, isHigherPt);      
    }

    int eventCategory = -1;
    if      (isWjjBoosted)   eventCategory = 1;
    else if (isWjjResolved)  eventCategory = 2;
    else if (isWjjHasOnly1j) eventCategory = 3;
    
    
    //int numSelJets_nonVBF = ( selJets_nonVBF.size() >= 1 ) ? selJets_nonVBF.size() : selJetsAK4.size();
    
    //--- compute output of BDTs used to discriminate ttH vs. ttV and ttH vs. ttbar
    //    in 3l category of ttH multilepton analysis
    const double lep1_conePt = comp_lep_conePt(*selLepton_lead);
    const double lep2_conePt = comp_lep_conePt(*selLepton_sublead);
    const double lep3_conePt = comp_lep_conePt(*selLepton_third);
    const double mindr_lep1_jet = comp_mindr_jet(*selLepton_lead, selJetsAK4);
    const double mindr_lep2_jet = comp_mindr_jet(*selLepton_sublead, selJetsAK4);
    const double mindr_lep3_jet = comp_mindr_jet(*selLepton_third, selJetsAK4);
    const double avg_dr_jet = comp_avg_dr_jet(selJetsAK4);

    double dr_l12 = deltaR(selLepton_lead -> p4(),    selLepton_sublead -> p4());
    double dr_l23 = deltaR(selLepton_sublead -> p4(), selLepton_third -> p4());
    double dr_l13 = deltaR(selLepton_lead -> p4(),    selLepton_third -> p4());
    double dr_lss  = -1.;
    double dr_los_min = -1.;
    double dr_los_max = -1.;
    // it does not assume mis-charge identification
    if (selLepton_lead->charge()*selLepton_sublead->charge() > 0){
      dr_lss  = deltaR(selLepton_lead -> p4(), selLepton_sublead -> p4());
      double dr1 = deltaR(selLepton_lead -> p4(),    selLepton_third -> p4());
      double dr2 = deltaR(selLepton_sublead -> p4(), selLepton_third -> p4());
      if (dr1 < dr2) {
	dr_los_min = dr1;
	dr_los_max = dr2;
      } else {
	dr_los_min = dr2;
	dr_los_max = dr1;
      }	
    } else if (selLepton_sublead->charge()*selLepton_third->charge() > 0){
      dr_lss  = deltaR(selLepton_sublead -> p4(), selLepton_third -> p4());
      double dr1 = deltaR(selLepton_lead -> p4(),    selLepton_sublead -> p4());
      double dr2 = deltaR(selLepton_lead -> p4(), selLepton_third -> p4());
      if (dr1 < dr2) {
	dr_los_min = dr1;
	dr_los_max = dr2;
      } else {
	dr_los_min = dr2;
	dr_los_max = dr1;
      }	
    } else if (selLepton_lead->charge()*selLepton_third->charge() > 0){
      dr_lss  = deltaR(selLepton_lead -> p4(), selLepton_third -> p4());
      double dr1 = deltaR(selLepton_lead -> p4(),    selLepton_sublead -> p4());
      double dr2 = deltaR(selLepton_sublead -> p4(), selLepton_third -> p4());
      if (dr1 < dr2) {
	dr_los_min = dr1;
	dr_los_max = dr2;
      } else {
	dr_los_min = dr2;
	dr_los_max = dr1;
      }	
    } else {
      std::cout << "analyze_hh_3l: Error in calculating dr_os " << std::endl;
      throw cmsException("analyze_hh_3l", __LINE__) << "Error in calculating dr_os \n";
    }


    double dr_WjjLepIdx3 = -1.;
    double dr_Wjet1LepIdx3 = -1.;
    double dr_Wjet2LepIdx3 = -1.;
    double dr_LepIdx3WjetNear = -1.;
    double dr_LepIdx3WjetFar  = -1.;
    double dr_Wjj = -1.;
    dr_Wjet1LepIdx3 = (selJet1_Wjj && selLepton_H_WW_ljj) ? deltaR((selJet1_Wjj->p4()), selLepton_H_WW_ljj->p4()) : -1.;
    dr_Wjet2LepIdx3 = (isWjjBoosted && selJet2_Wjj && selLepton_H_WW_ljj) ? deltaR((selJet2_Wjj->p4()), selLepton_H_WW_ljj->p4()) : -1.;
    if (dr_Wjet1LepIdx3 < dr_Wjet2LepIdx3) {
      dr_LepIdx3WjetNear = dr_Wjet1LepIdx3;
      dr_LepIdx3WjetFar  = dr_Wjet2LepIdx3;      
    } else {
      dr_LepIdx3WjetNear = dr_Wjet2LepIdx3;
      dr_LepIdx3WjetFar  = dr_Wjet1LepIdx3; 
    }
    if (isWjjBoosted) {
      dr_WjjLepIdx3 = (selJetAK8_Wjj && selLepton_H_WW_ljj) ? deltaR((selJetAK8_Wjj->p4()), selLepton_H_WW_ljj->p4()) : -1.;
    } else if (isWjjResolved) {
      dr_WjjLepIdx3 = (selJet1_Wjj && selJet2_Wjj && selLepton_H_WW_ljj) ? deltaR((selJet1_Wjj->p4() + selJet2_Wjj->p4()), selLepton_H_WW_ljj->p4()) : -1.;
    } else {
      dr_WjjLepIdx3 = (selJet1_Wjj && selLepton_H_WW_ljj) ? deltaR((selJet1_Wjj->p4()), selLepton_H_WW_ljj->p4()) : -1.;
    }
    if (selJet1_Wjj && selJet2_Wjj) dr_Wjj = deltaR(selJet1_Wjj->p4(), selJet2_Wjj->p4());


    double jet1_pt = selJet1_Wjj ? selJet1_Wjj->pt() : 0.;
    double jet2_pt = selJet2_Wjj ? selJet2_Wjj->pt() : 0.;
    double jet1plus2pt;
    double jet1_m = selJet1_Wjj ? selJet1_Wjj->p4().mass() : 0.;
    double jet2_m = selJet2_Wjj ? selJet1_Wjj->p4().mass() : 0.;
    if (selJetAK8_Wjj) {
      jet1plus2pt = selJetAK8_Wjj->pt();
    } else if (selJet1_Wjj && selJet2_Wjj) {
      jet1plus2pt = (selJet1_Wjj->p4() + selJet2_Wjj->p4()).pt();
    } else {
      jet1plus2pt = (selJet1_Wjj->p4()).pt();
    }

    // just to avoid 'variables defined but not used' error
    TString sTmp123 = Form("selLepton1_H_WW_ll pt: %f,  selLepton2_H_WW_ll: %f,  vbf_dEta_jj: %f",selLepton1_H_WW_ll->pt(),selLepton2_H_WW_ll->pt(), vbf_dEta_jj);
    sTmp123 += "";
    sTmp123 += Form(" isVBF: %i, ",(int)isVBF); 

    // Variables using lepton1/2/3 indexed following Approach-0
    const RecoLepton* selLepton_H_WW_ljj_Approach0 = selLepton_H_WW_ljj;
    const RecoLepton* selLepton1_H_WW_ll_Approach0 = selLepton1_H_WW_ll;
    const RecoLepton* selLepton2_H_WW_ll_Approach0 = selLepton2_H_WW_ll;
    //
    double mT_LeptonIdx1_Met_Approach0 = comp_MT_met(selLepton1_H_WW_ll_Approach0, met.pt(), met.phi());
    double mT_LeptonIdx2_Met_Approach0 = comp_MT_met(selLepton2_H_WW_ll_Approach0, met.pt(), met.phi());
    double mT_LeptonIdx3_Met_Approach0 = comp_MT_met(selLepton_H_WW_ljj_Approach0, met.pt(), met.phi());
    //
    double m_LeptonIdx1_LeptonIdx2_Approach0 = (selLepton1_H_WW_ll_Approach0->p4() + selLepton2_H_WW_ll_Approach0->p4()).mass();
    double m_LeptonIdx2_LeptonIdx3_Approach0 = (selLepton2_H_WW_ll_Approach0->p4() + selLepton_H_WW_ljj_Approach0->p4()).mass();
    double m_LeptonIdx1_LeptonIdx3_Approach0 = (selLepton1_H_WW_ll_Approach0->p4() + selLepton_H_WW_ljj_Approach0->p4()).mass();
    //
    double dPhi_LeptonIdx1_LeptonIdx2_Approach0 = std::abs(selLepton1_H_WW_ll_Approach0->phi() - selLepton2_H_WW_ll_Approach0->phi());
    double dPhi_LeptonIdx2_LeptonIdx3_Approach0 = std::abs(selLepton2_H_WW_ll_Approach0->phi() - selLepton_H_WW_ljj_Approach0->phi());
    double dPhi_LeptonIdx1_LeptonIdx3_Approach0 = std::abs(selLepton1_H_WW_ll_Approach0->phi() - selLepton_H_WW_ljj_Approach0->phi());
    //
    double dr_LeptonIdx1_LeptonIdx2_Approach0 = deltaR(selLepton1_H_WW_ll_Approach0->p4(), selLepton2_H_WW_ll_Approach0->p4());
    double dr_LeptonIdx2_LeptonIdx3_Approach0 = deltaR(selLepton2_H_WW_ll_Approach0->p4(), selLepton_H_WW_ljj_Approach0->p4());
    double dr_LeptonIdx1_LeptonIdx3_Approach0 = deltaR(selLepton1_H_WW_ll_Approach0->p4(), selLepton_H_WW_ljj_Approach0->p4());
    //
    double m_LeptonIdx3_Jet1_Approach0  = (selLepton_H_WW_ljj_Approach0->p4() + selJet1_Wjj->p4()).mass();
    double dr_LeptonIdx3_Jet1_Approach0 = deltaR(selLepton_H_WW_ljj_Approach0->p4(), selJet1_Wjj->p4());
    double m_LeptonIdx3_JetNear_Approach0;
    double dr_LeptonIdx3_JetNear_Approach0;
    if (selJet2_Wjj) { 
      if (deltaR(selLepton_H_WW_ljj_Approach0->p4(), selJet1_Wjj->p4()) <
	  deltaR(selLepton_H_WW_ljj_Approach0->p4(), selJet2_Wjj->p4()) ) {
	dr_LeptonIdx3_JetNear_Approach0 = deltaR(selLepton_H_WW_ljj_Approach0->p4(), selJet1_Wjj->p4());
	m_LeptonIdx3_JetNear_Approach0  = (selLepton_H_WW_ljj_Approach0->p4() + selJet1_Wjj->p4()).mass();
      } else {
	dr_LeptonIdx3_JetNear_Approach0 = deltaR(selLepton_H_WW_ljj_Approach0->p4(), selJet2_Wjj->p4());
	m_LeptonIdx3_JetNear_Approach0  = (selLepton_H_WW_ljj_Approach0->p4() + selJet2_Wjj->p4()).mass();
      }
    } else {
      dr_LeptonIdx3_JetNear_Approach0 = dr_LeptonIdx3_Jet1_Approach0;
      m_LeptonIdx3_JetNear_Approach0 = m_LeptonIdx3_Jet1_Approach0;
    }
    //--------------------------------

    
    // Assume event topology deciding variable labels: H->WW->l1(+) l2(-) and other H->WW->l3(+) qq
    size_t idxLepton_H_WW_ljj_Approach2 = 9999;
    size_t idxLepton1_H_WW_ll_Approach2 = 9999;
    size_t idxLepton2_H_WW_ll_Approach2 = 9999;
    const RecoLepton* selLepton_H_WW_ljj_Approach2 = nullptr;
    const RecoLepton* selLepton1_H_WW_ll_Approach2 = nullptr;
    const RecoLepton* selLepton2_H_WW_ll_Approach2 = nullptr;

    for (size_t iLepton1 = 0; iLepton1 < 3; iLepton1++) {
      if ((selLeptons[iLepton1]->charge() * sumLeptonCharge_3l) < 0.) {
	idxLepton2_H_WW_ll_Approach2 = iLepton1;
	selLepton2_H_WW_ll_Approach2 = selLeptons[iLepton1];
      }
    }
    for (size_t iLepton1 = 0; iLepton1 < 3; iLepton1++) {
      if (iLepton1 == idxLepton2_H_WW_ll_Approach2) continue;
      size_t iLepton3 = 0;
      if (iLepton3 == iLepton1)                     iLepton3++;
      if (iLepton3 == idxLepton2_H_WW_ll_Approach2) iLepton3++;
      if (iLepton3 == iLepton1)                     iLepton3++;
      
      if ((selLepton2_H_WW_ll_Approach2->p4() + selLeptons[iLepton1]->p4()).mass() <
	  (selLepton2_H_WW_ll_Approach2->p4() + selLeptons[iLepton3]->p4()).mass() ) { // assume m(l1+l2) < m(l2+l3)
	idxLepton1_H_WW_ll_Approach2 = iLepton1;
	idxLepton_H_WW_ljj_Approach2 = iLepton3;
      } else { 
	idxLepton1_H_WW_ll_Approach2 = iLepton3;
	idxLepton_H_WW_ljj_Approach2 = iLepton1;
      }
    }
    selLepton1_H_WW_ll_Approach2 = selLeptons[idxLepton1_H_WW_ll_Approach2];
    selLepton_H_WW_ljj_Approach2 = selLeptons[idxLepton_H_WW_ljj_Approach2];

    // Complain if there is a mistake in picking leptons in Approach 2
    if ((selLepton2_H_WW_ll_Approach2->p4() + selLepton1_H_WW_ll_Approach2->p4()).mass() >
	(selLepton2_H_WW_ll_Approach2->p4() + selLepton_H_WW_ljj_Approach2->p4()).mass() ) { // mistake in picking leptons in Approach 2
      std::cout << "analyze_hh_3l: mistake in picking leptons in Approach 2" << std::endl;
      throw cmsException("analyze_hh_3l", __LINE__) << "Error in calculating dr_os n";
    }
    
    double mT_LeptonIdx1_Met_Approach2 = comp_MT_met(selLepton1_H_WW_ll_Approach2, met.pt(), met.phi());
    double mT_LeptonIdx2_Met_Approach2 = comp_MT_met(selLepton2_H_WW_ll_Approach2, met.pt(), met.phi());
    double mT_LeptonIdx3_Met_Approach2 = comp_MT_met(selLepton_H_WW_ljj_Approach2, met.pt(), met.phi());
    //
    double m_LeptonIdx1_LeptonIdx2_Approach2 = (selLepton1_H_WW_ll_Approach2->p4() + selLepton2_H_WW_ll_Approach2->p4()).mass();
    double m_LeptonIdx2_LeptonIdx3_Approach2 = (selLepton2_H_WW_ll_Approach2->p4() + selLepton_H_WW_ljj_Approach2->p4()).mass();
    double m_LeptonIdx1_LeptonIdx3_Approach2 = (selLepton1_H_WW_ll_Approach2->p4() + selLepton_H_WW_ljj_Approach2->p4()).mass();
    //
    double dPhi_LeptonIdx1_LeptonIdx2_Approach2 = std::abs(selLepton1_H_WW_ll_Approach2->phi() - selLepton2_H_WW_ll_Approach2->phi());
    double dPhi_LeptonIdx2_LeptonIdx3_Approach2 = std::abs(selLepton2_H_WW_ll_Approach2->phi() - selLepton_H_WW_ljj_Approach2->phi());
    double dPhi_LeptonIdx1_LeptonIdx3_Approach2 = std::abs(selLepton1_H_WW_ll_Approach2->phi() - selLepton_H_WW_ljj_Approach2->phi());
    //
    double dr_LeptonIdx1_LeptonIdx2_Approach2 = deltaR(selLepton1_H_WW_ll_Approach2->p4(), selLepton2_H_WW_ll_Approach2->p4());
    double dr_LeptonIdx2_LeptonIdx3_Approach2 = deltaR(selLepton2_H_WW_ll_Approach2->p4(), selLepton_H_WW_ljj_Approach2->p4());
    double dr_LeptonIdx1_LeptonIdx3_Approach2 = deltaR(selLepton1_H_WW_ll_Approach2->p4(), selLepton_H_WW_ljj_Approach2->p4());
    //
    double m_LeptonIdx3_Jet1_Approach2  = (selLepton_H_WW_ljj_Approach2->p4() + selJet1_Wjj->p4()).mass();
    double dr_LeptonIdx3_Jet1_Approach2 = deltaR(selLepton_H_WW_ljj_Approach2->p4(), selJet1_Wjj->p4());
    double m_LeptonIdx3_JetNear_Approach2;
    double dr_LeptonIdx3_JetNear_Approach2;
    if (selJet2_Wjj) { 
      if (deltaR(selLepton_H_WW_ljj_Approach2->p4(), selJet1_Wjj->p4()) <
	  deltaR(selLepton_H_WW_ljj_Approach2->p4(), selJet2_Wjj->p4()) ) {
	dr_LeptonIdx3_JetNear_Approach2 = deltaR(selLepton_H_WW_ljj_Approach2->p4(), selJet1_Wjj->p4());
	m_LeptonIdx3_JetNear_Approach2  = (selLepton_H_WW_ljj_Approach2->p4() + selJet1_Wjj->p4()).mass();
      } else {
	dr_LeptonIdx3_JetNear_Approach2 = deltaR(selLepton_H_WW_ljj_Approach2->p4(), selJet2_Wjj->p4());
	m_LeptonIdx3_JetNear_Approach2  = (selLepton_H_WW_ljj_Approach2->p4() + selJet2_Wjj->p4()).mass();
      }
    } else {
      dr_LeptonIdx3_JetNear_Approach2 = dr_LeptonIdx3_Jet1_Approach2;
      m_LeptonIdx3_JetNear_Approach2 = m_LeptonIdx3_Jet1_Approach2;
    }
    //--------------------------------
    
     
    const std::map<std::string, double>  mvaInputVariables_hh_3l_SUMBk_HH = {
      {"lep1_conePt",         lep1_conePt},
      {"lep1_eta",            selLepton_lead -> eta()},
      {"mindr_lep1_jet",      TMath::Min(10., mindr_lep1_jet)},
      {"mT_lep1",             comp_MT_met(selLepton_lead, met.pt(), met.phi())},
      {"lep2_conePt",         lep2_conePt},
      {"lep2_eta",            selLepton_sublead -> eta()},
      {"mindr_lep2_jet",      TMath::Min(10., mindr_lep2_jet)},
      {"mT_lep2",             comp_MT_met(selLepton_sublead, met.pt(), met.phi())},
      {"lep3_conePt",         lep3_conePt},
      {"lep3_eta",            selLepton_third -> eta()},
      {"mindr_lep3_jet",      TMath::Min(10., mindr_lep3_jet)},
      {"mT_lep3",             comp_MT_met(selLepton_third, met.pt(), met.phi())},
      {"avg_dr_jet",          avg_dr_jet},
      {"dr_leps",             deltaR(selLepton_lead -> p4(), selLepton_sublead -> p4())},
      {"dr_lss",              dr_lss},
      {"dr_los1",             dr_los_min},
      {"dr_los2",             dr_los_max},
      {"met_LD",              met_LD},
      {"m_jj",                WTojjMass},
      {"diHiggsMass",         dihiggsMass},
      {"mTMetLepton1",        mTMetLepton1},
      {"mTMetLepton2",        mTMetLepton2},
      {"nJet",                selJetsAK4.size()},
      {"nElectron",           selElectrons.size()},
      {"sumLeptonCharge",     sumLeptonCharge_3l},
      {"numSameFlavor_OS",    numSameFlavor_OS}
    };
    //const double mvaOutput_xgb_hh_3l_SUMBk_HH_1 = 100; //mva_xgb_hh_3l_SUMBk_HH(mvaInputVariables_hh_3l_SUMBk_HH);
    const double mvaOutput_tmva_hh_3l_SUMBk_HH = (*mva_tmva_hh_3l_SUMBk_HH)(mvaInputVariables_hh_3l_SUMBk_HH);
    const double mvaOutput_xgb_hh_3l_SUMBk_HH = mvaOutput_tmva_hh_3l_SUMBk_HH; // #### IMPORTANT ************
    
    /*
    printf("mvaInputVariables_hh_3l_SUMBk_HH:: \n");
    for (std::map<std::string, double>::const_iterator it=mvaInputVariables_hh_3l_SUMBk_HH.begin(); it != mvaInputVariables_hh_3l_SUMBk_HH.end(); it++) {
      std::cout << "\t" << it->first << " \t\t  " << it->second << std::endl;      
    }
    std::cout << "mvaOutput_xgb_hh_3l_SUMBk_HH_1 " << mvaOutput_xgb_hh_3l_SUMBk_HH_1 << std::endl;
    std::cout << "mvaOutput_tmva_hh_3l_SUMBk_HH " << mvaOutput_tmva_hh_3l_SUMBk_HH << std::endl;
    std::cout << "mvaOutput_xgb_hh_3l_SUMBk_HH " << mvaOutput_xgb_hh_3l_SUMBk_HH << std::endl;
    */
    
//--- retrieve gen-matching flags    
    //std::vector<const GenMatchEntry*> genMatches = genMatchInterface.getGenMatch(selLeptons);
    //std::cout << "siddh here 10" << std::endl;
    
//--- fill histograms with events passing final selection
     
    double lep1_genLepPt = ( selLepton_lead->genLepton()    ) ? selLepton_lead->genLepton()->pt()    : 0.;
    double lep2_genLepPt = ( selLepton_sublead->genLepton() ) ? selLepton_sublead->genLepton()->pt() : 0.;
    double lep3_genLepPt = ( selLepton_third->genLepton()   ) ? selLepton_third->genLepton()->pt()   : 0.;

    //FR weights for bdt ntuple
    double prob_fake_lepton_lead, prob_fake_lepton_sublead, prob_fake_lepton_third;
    /*
    // Run-time error: weights_FR_lepton_lead_.empty()
    //std::cout << "Siddh here12_4" << std::endl;
    double prob_fake_lepton_lead = evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main) ? evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main) : -1;
    //std::cout << "Siddh here12_5" << std::endl;
    double prob_fake_lepton_sublead = evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main) ? evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main) : -1;
    //std::cout << "Siddh here12_6" << std::endl;
    double prob_fake_lepton_third = evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main) ? evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main) : -1;
    //std::cout << "Siddh here13" << std::endl;
    
    std::cout << "evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main): " << evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main) <<  std::endl;
    std::cout << "evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main): " << evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main) <<  std::endl;
    std::cout << "evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main): " << evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main) <<  std::endl;
    */
    prob_fake_lepton_lead = prob_fake_lepton_sublead = prob_fake_lepton_third = -1.;
    
    for(const std::string & central_or_shift: central_or_shifts_local)
    {
      const double evtWeight = evtWeightRecorder.get(central_or_shift);
      const bool skipFilling = central_or_shift != central_or_shift_main;
      for (const GenMatchEntry* genMatch : genMatches)
      {
	//std::cout << "genMatch Idx: " << genMatch->getIdx() << ", name: " << genMatch->getName() << std::endl;
        selHistManagerType* selHistManager = selHistManagers[central_or_shift][genMatch->getIdx()];
        assert(selHistManager);
        if(! skipFilling)
        {
          selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
          selHistManager->muons_->fillHistograms(selMuons, evtWeight);
          selHistManager->hadTaus_->fillHistograms(selHadTaus, evtWeight);
          selHistManager->jetsAK4_->fillHistograms(selJetsAK4, evtWeight);
          selHistManager->leadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
          selHistManager->subleadJetAK4_->fillHistograms(selJetsAK4, evtWeight);
          selHistManager->BJetsAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
          selHistManager->leadBJetAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
          selHistManager->subleadBJetAK4_loose_->fillHistograms(selBJetsAK4_loose, evtWeight);
          selHistManager->BJetsAK4_medium_->fillHistograms(selBJetsAK4_medium, evtWeight);
          selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);
          selHistManager->metFilters_->fillHistograms(metFilters, evtWeight);
        }
	
	
	for(const auto & kv: reWeightMapHH)
        {
	  //std::cout << "\t kv: " << kv.first << std::endl;
          selHistManager->evt_[kv.first]->fillHistograms(
		selElectrons.size(),
		selMuons.size(),
		selLeptons.size(),
		sumLeptonCharge_3l,
		sumLeptonCharge_FullSel,
		numSameFlavor_OS_3l,
		numSameFlavor_OS_Full,
		selJetsAK4.size(),
		selBJetsAK4_loose.size(),
		selBJetsAK4_medium.size(),
		jet_ptrs_ak8_Wjj.size(),
		selJetsAK8_Wjj_wSelectorAK8_Wjj.size(),
		//
		selLepton_lead -> pt(),
		lep1_conePt,
		selLepton_lead -> eta(),
		TMath::Min(10., mindr_lep1_jet),
		comp_MT_met(selLepton_lead, met.pt(), met.phi()),
		//
		selLepton_sublead -> pt(),
		lep2_conePt,
		selLepton_sublead -> eta(),
		TMath::Min(10., mindr_lep2_jet),
		comp_MT_met(selLepton_sublead, met.pt(), met.phi()),
		//
		selLepton_third -> pt(),
		lep3_conePt,
		selLepton_third -> eta(),
		TMath::Min(10., mindr_lep3_jet),
		comp_MT_met(selLepton_third, met.pt(), met.phi()),
		//
		jet1_pt,
		jet2_pt,
		jet1plus2pt,
		jet1_m,
		jet2_m,
		//
		avg_dr_jet,
		dr_Wjj,
		//
		dr_l12,
		dr_l23,
		dr_l13,
		dr_lss,
		dr_los_min,
		dr_los_max,
		//
		dr_WjjLepIdx3,
		dr_Wjet1LepIdx3,
		dr_Wjet2LepIdx3,
		dr_LepIdx3WjetNear,
		dr_LepIdx3WjetFar,
		//
		met.pt(),
		mht_p4.pt(),
		met_LD,
		HT,
		STMET,
		//
		mSFOS2l,
		WTojjMass,
		dihiggsVisMass_sel,
		dihiggsMass,
		mTMetLepton1,
		mTMetLepton2,
		//
		int(selLepton_lead -> isTight()),
		int(selLepton_sublead -> isTight()),
		int(selLepton_third -> isTight()),
		//
		lep1_genLepPt,
		lep2_genLepPt,
		lep3_genLepPt,
		lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead,
		lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead,
		lep3_genLepPt > 0 ? 1.0 : prob_fake_lepton_third,
		prob_fake_lepton_lead,
		prob_fake_lepton_sublead,
		prob_fake_lepton_third,
		//
		mT_LeptonIdx1_Met_Approach0,
		mT_LeptonIdx2_Met_Approach0,
		mT_LeptonIdx3_Met_Approach0,
		//
		m_LeptonIdx1_LeptonIdx2_Approach0,
		m_LeptonIdx2_LeptonIdx3_Approach0,
		m_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach0,
		dPhi_LeptonIdx2_LeptonIdx3_Approach0,
		dPhi_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach0,
		dr_LeptonIdx2_LeptonIdx3_Approach0,
		dr_LeptonIdx1_LeptonIdx3_Approach0,
		//
		m_LeptonIdx3_Jet1_Approach0,
		dr_LeptonIdx3_Jet1_Approach0,
		//
		m_LeptonIdx3_JetNear_Approach0,
		dr_LeptonIdx3_JetNear_Approach0,
		//
		mT_LeptonIdx1_Met_Approach2,
		mT_LeptonIdx2_Met_Approach2,
		mT_LeptonIdx3_Met_Approach2,
		//
		m_LeptonIdx1_LeptonIdx2_Approach2,
		m_LeptonIdx2_LeptonIdx3_Approach2,
		m_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach2,
		dPhi_LeptonIdx2_LeptonIdx3_Approach2,
		dPhi_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach2,
		dr_LeptonIdx2_LeptonIdx3_Approach2,
		dr_LeptonIdx1_LeptonIdx3_Approach2,
		//
		m_LeptonIdx3_Jet1_Approach2,
		dr_LeptonIdx3_Jet1_Approach2,
		//
		m_LeptonIdx3_JetNear_Approach2,
		dr_LeptonIdx3_JetNear_Approach2,		
		//
		eventCategory,
		//
                mvaOutput_xgb_hh_3l_SUMBk_HH,
                kv.second
              );

          if(isSignal && !skipHHDecayModeHistograms)
          {
            const std::string decayModeStr = eventInfo.getDiHiggsDecayModeString();
	    //std::cout << "\t\t decayModeStr: " <<  decayModeStr << std::endl;
            if(! decayModeStr.empty())
            {
              selHistManager -> evt_in_decayModes_[kv.first][decayModeStr] -> fillHistograms(
		selElectrons.size(),
		selMuons.size(),
		selLeptons.size(),
		sumLeptonCharge_3l,
		sumLeptonCharge_FullSel,
		numSameFlavor_OS_3l,
		numSameFlavor_OS_Full,
		selJetsAK4.size(),
		selBJetsAK4_loose.size(),
		selBJetsAK4_medium.size(),
		jet_ptrs_ak8_Wjj.size(),
		selJetsAK8_Wjj_wSelectorAK8_Wjj.size(),
		//
		selLepton_lead -> pt(),
		lep1_conePt,
		selLepton_lead -> eta(),
		TMath::Min(10., mindr_lep1_jet),
		comp_MT_met(selLepton_lead, met.pt(), met.phi()),
		//
		selLepton_sublead -> pt(),
		lep2_conePt,
		selLepton_sublead -> eta(),
		TMath::Min(10., mindr_lep2_jet),
		comp_MT_met(selLepton_sublead, met.pt(), met.phi()),
		//
		selLepton_third -> pt(),
		lep3_conePt,
		selLepton_third -> eta(),
		TMath::Min(10., mindr_lep3_jet),
		comp_MT_met(selLepton_third, met.pt(), met.phi()),
		//
		jet1_pt,
		jet2_pt,
		jet1plus2pt,
		jet1_m,
		jet2_m,
		//
		avg_dr_jet,
		dr_Wjj,
		//
		dr_l12,
		dr_l23,
		dr_l13,
		dr_lss,
		dr_los_min,
		dr_los_max,
		//
		dr_WjjLepIdx3,
		dr_Wjet1LepIdx3,
		dr_Wjet2LepIdx3,
		dr_LepIdx3WjetNear,
		dr_LepIdx3WjetFar,
		//
		met.pt(),
		mht_p4.pt(),
		met_LD,
		HT,
		STMET,
		//
		mSFOS2l,
		WTojjMass,
		dihiggsVisMass_sel,
		dihiggsMass,
		mTMetLepton1,
		mTMetLepton2,
		//
		int(selLepton_lead -> isTight()),
		int(selLepton_sublead -> isTight()),
		int(selLepton_third -> isTight()),
		//
		lep1_genLepPt,
		lep2_genLepPt,
		lep3_genLepPt,
		lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead,
		lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead,
		lep3_genLepPt > 0 ? 1.0 : prob_fake_lepton_third,
		prob_fake_lepton_lead,
		prob_fake_lepton_sublead,
		prob_fake_lepton_third,
		//
		mT_LeptonIdx1_Met_Approach0,
		mT_LeptonIdx2_Met_Approach0,
		mT_LeptonIdx3_Met_Approach0,
		//
		m_LeptonIdx1_LeptonIdx2_Approach0,
		m_LeptonIdx2_LeptonIdx3_Approach0,
		m_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach0,
		dPhi_LeptonIdx2_LeptonIdx3_Approach0,
		dPhi_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach0,
		dr_LeptonIdx2_LeptonIdx3_Approach0,
		dr_LeptonIdx1_LeptonIdx3_Approach0,
		//
		m_LeptonIdx3_Jet1_Approach0,
		dr_LeptonIdx3_Jet1_Approach0,
		//
		m_LeptonIdx3_JetNear_Approach0,
		dr_LeptonIdx3_JetNear_Approach0,
		//
		mT_LeptonIdx1_Met_Approach2,
		mT_LeptonIdx2_Met_Approach2,
		mT_LeptonIdx3_Met_Approach2,
		//
		m_LeptonIdx1_LeptonIdx2_Approach2,
		m_LeptonIdx2_LeptonIdx3_Approach2,
		m_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach2,
		dPhi_LeptonIdx2_LeptonIdx3_Approach2,
		dPhi_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach2,
		dr_LeptonIdx2_LeptonIdx3_Approach2,
		dr_LeptonIdx1_LeptonIdx3_Approach2,
		//
		m_LeptonIdx3_Jet1_Approach2,
		dr_LeptonIdx3_Jet1_Approach2,
		//
		m_LeptonIdx3_JetNear_Approach2,
		dr_LeptonIdx3_JetNear_Approach2,		
		//
		eventCategory,
		//
                mvaOutput_xgb_hh_3l_SUMBk_HH,
                kv.second
              );
            }
          }
        }

        for(const std::string & category: evtCategories)
        {
	  //std::cout << "\t category: " << category << std::endl;
          ElectronHistManager* selHistManager_electrons_category = selHistManager->electrons_in_categories_[category];
          if ( selHistManager_electrons_category ) {
            selHistManager_electrons_category->fillHistograms(selElectrons, evtWeight);
          }
          MuonHistManager* selHistManager_muons_category = selHistManager->muons_in_categories_[category];
          if ( selHistManager_muons_category ) {
            selHistManager_muons_category->fillHistograms(selMuons, evtWeight);
          }
	  for(const auto & kv: reWeightMapHH)
          {
	    //std::cout << "\t\t kv: " << kv.first << std::endl;
            EvtHistManager_hh_3l* selHistManager_evt_category = selHistManager->evt_in_categories_[kv.first][category];
            if ( selHistManager_evt_category ) { // CV: pointer is zero when running on OS control region to estimate "charge_flip" background
              selHistManager_evt_category->fillHistograms(
		selElectrons.size(),
		selMuons.size(),
		selLeptons.size(),
		sumLeptonCharge_3l,
		sumLeptonCharge_FullSel,
		numSameFlavor_OS_3l,
		numSameFlavor_OS_Full,
		selJetsAK4.size(),
		selBJetsAK4_loose.size(),
		selBJetsAK4_medium.size(),
		jet_ptrs_ak8_Wjj.size(),
		selJetsAK8_Wjj_wSelectorAK8_Wjj.size(),
		//
		selLepton_lead -> pt(),
		lep1_conePt,
		selLepton_lead -> eta(),
		TMath::Min(10., mindr_lep1_jet),
		comp_MT_met(selLepton_lead, met.pt(), met.phi()),
		//
		selLepton_sublead -> pt(),
		lep2_conePt,
		selLepton_sublead -> eta(),
		TMath::Min(10., mindr_lep2_jet),
		comp_MT_met(selLepton_sublead, met.pt(), met.phi()),
		//
		selLepton_third -> pt(),
		lep3_conePt,
		selLepton_third -> eta(),
		TMath::Min(10., mindr_lep3_jet),
		comp_MT_met(selLepton_third, met.pt(), met.phi()),
		//
		jet1_pt,
		jet2_pt,
		jet1plus2pt,
		jet1_m,
		jet2_m,
		//
		avg_dr_jet,
		dr_Wjj,
		//
		dr_l12,
		dr_l23,
		dr_l13,
		dr_lss,
		dr_los_min,
		dr_los_max,
		//
		dr_WjjLepIdx3,
		dr_Wjet1LepIdx3,
		dr_Wjet2LepIdx3,
		dr_LepIdx3WjetNear,
		dr_LepIdx3WjetFar,
		//
		met.pt(),
		mht_p4.pt(),
		met_LD,
		HT,
		STMET,
		//
		mSFOS2l,
		WTojjMass,
		dihiggsVisMass_sel,
		dihiggsMass,
		mTMetLepton1,
		mTMetLepton2,
		//
		int(selLepton_lead -> isTight()),
		int(selLepton_sublead -> isTight()),
		int(selLepton_third -> isTight()),
		//
		lep1_genLepPt,
		lep2_genLepPt,
		lep3_genLepPt,
		lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead,
		lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead,
		lep3_genLepPt > 0 ? 1.0 : prob_fake_lepton_third,
		prob_fake_lepton_lead,
		prob_fake_lepton_sublead,
		prob_fake_lepton_third,
		//
		mT_LeptonIdx1_Met_Approach0,
		mT_LeptonIdx2_Met_Approach0,
		mT_LeptonIdx3_Met_Approach0,
		//
		m_LeptonIdx1_LeptonIdx2_Approach0,
		m_LeptonIdx2_LeptonIdx3_Approach0,
		m_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach0,
		dPhi_LeptonIdx2_LeptonIdx3_Approach0,
		dPhi_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach0,
		dr_LeptonIdx2_LeptonIdx3_Approach0,
		dr_LeptonIdx1_LeptonIdx3_Approach0,
		//
		m_LeptonIdx3_Jet1_Approach0,
		dr_LeptonIdx3_Jet1_Approach0,
		//
		m_LeptonIdx3_JetNear_Approach0,
		dr_LeptonIdx3_JetNear_Approach0,
		//
		mT_LeptonIdx1_Met_Approach2,
		mT_LeptonIdx2_Met_Approach2,
		mT_LeptonIdx3_Met_Approach2,
		//
		m_LeptonIdx1_LeptonIdx2_Approach2,
		m_LeptonIdx2_LeptonIdx3_Approach2,
		m_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach2,
		dPhi_LeptonIdx2_LeptonIdx3_Approach2,
		dPhi_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach2,
		dr_LeptonIdx2_LeptonIdx3_Approach2,
		dr_LeptonIdx1_LeptonIdx3_Approach2,
		//
		m_LeptonIdx3_Jet1_Approach2,
		dr_LeptonIdx3_Jet1_Approach2,
		//
		m_LeptonIdx3_JetNear_Approach2,
		dr_LeptonIdx3_JetNear_Approach2,		
		//
		eventCategory,
		//
                mvaOutput_xgb_hh_3l_SUMBk_HH,
                kv.second
              );
            }

            if(isSignal && !skipHHDecayModeHistograms) {
              const std::string decayModeStr = eventInfo.getDiHiggsDecayModeString();
	      //std::cout << "\t\t\t decayModeStr: " <<  decayModeStr << std::endl;
              if (! decayModeStr.empty()) {

                EvtHistManager_hh_3l* selHistManager_evt_category_decMode = selHistManager->evt_in_categories_and_decayModes_[kv.first][category][decayModeStr];
                if ( selHistManager_evt_category_decMode ) { // CV: pointer is zero when running on OS control region to estimate "charge_flip" background
                  selHistManager_evt_category_decMode->fillHistograms(
		selElectrons.size(),
		selMuons.size(),
		selLeptons.size(),
		sumLeptonCharge_3l,
		sumLeptonCharge_FullSel,
		numSameFlavor_OS_3l,
		numSameFlavor_OS_Full,
		selJetsAK4.size(),
		selBJetsAK4_loose.size(),
		selBJetsAK4_medium.size(),
		jet_ptrs_ak8_Wjj.size(),
		selJetsAK8_Wjj_wSelectorAK8_Wjj.size(),
		//
		selLepton_lead -> pt(),
		lep1_conePt,
		selLepton_lead -> eta(),
		TMath::Min(10., mindr_lep1_jet),
		comp_MT_met(selLepton_lead, met.pt(), met.phi()),
		//
		selLepton_sublead -> pt(),
		lep2_conePt,
		selLepton_sublead -> eta(),
		TMath::Min(10., mindr_lep2_jet),
		comp_MT_met(selLepton_sublead, met.pt(), met.phi()),
		//
		selLepton_third -> pt(),
		lep3_conePt,
		selLepton_third -> eta(),
		TMath::Min(10., mindr_lep3_jet),
		comp_MT_met(selLepton_third, met.pt(), met.phi()),
		//
		jet1_pt,
		jet2_pt,
		jet1plus2pt,
		jet1_m,
		jet2_m,
		//
		avg_dr_jet,
		dr_Wjj,
		//
		dr_l12,
		dr_l23,
		dr_l13,
		dr_lss,
		dr_los_min,
		dr_los_max,
		//
		dr_WjjLepIdx3,
		dr_Wjet1LepIdx3,
		dr_Wjet2LepIdx3,
		dr_LepIdx3WjetNear,
		dr_LepIdx3WjetFar,
		//
		met.pt(),
		mht_p4.pt(),
		met_LD,
		HT,
		STMET,
		//
		mSFOS2l,
		WTojjMass,
		dihiggsVisMass_sel,
		dihiggsMass,
		mTMetLepton1,
		mTMetLepton2,
		//
		int(selLepton_lead -> isTight()),
		int(selLepton_sublead -> isTight()),
		int(selLepton_third -> isTight()),
		//
		lep1_genLepPt,
		lep2_genLepPt,
		lep3_genLepPt,
		lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead,
		lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead,
		lep3_genLepPt > 0 ? 1.0 : prob_fake_lepton_third,
		prob_fake_lepton_lead,
		prob_fake_lepton_sublead,
		prob_fake_lepton_third,
		//
		mT_LeptonIdx1_Met_Approach0,
		mT_LeptonIdx2_Met_Approach0,
		mT_LeptonIdx3_Met_Approach0,
		//
		m_LeptonIdx1_LeptonIdx2_Approach0,
		m_LeptonIdx2_LeptonIdx3_Approach0,
		m_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach0,
		dPhi_LeptonIdx2_LeptonIdx3_Approach0,
		dPhi_LeptonIdx1_LeptonIdx3_Approach0,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach0,
		dr_LeptonIdx2_LeptonIdx3_Approach0,
		dr_LeptonIdx1_LeptonIdx3_Approach0,
		//
		m_LeptonIdx3_Jet1_Approach0,
		dr_LeptonIdx3_Jet1_Approach0,
		//
		m_LeptonIdx3_JetNear_Approach0,
		dr_LeptonIdx3_JetNear_Approach0,
		//
		mT_LeptonIdx1_Met_Approach2,
		mT_LeptonIdx2_Met_Approach2,
		mT_LeptonIdx3_Met_Approach2,
		//
		m_LeptonIdx1_LeptonIdx2_Approach2,
		m_LeptonIdx2_LeptonIdx3_Approach2,
		m_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dPhi_LeptonIdx1_LeptonIdx2_Approach2,
		dPhi_LeptonIdx2_LeptonIdx3_Approach2,
		dPhi_LeptonIdx1_LeptonIdx3_Approach2,
		//
		dr_LeptonIdx1_LeptonIdx2_Approach2,
		dr_LeptonIdx2_LeptonIdx3_Approach2,
		dr_LeptonIdx1_LeptonIdx3_Approach2,
		//
		m_LeptonIdx3_Jet1_Approach2,
		dr_LeptonIdx3_Jet1_Approach2,
		//
		m_LeptonIdx3_JetNear_Approach2,
		dr_LeptonIdx3_JetNear_Approach2,		
		//
		eventCategory,
		//
                mvaOutput_xgb_hh_3l_SUMBk_HH,
                kv.second
              );
                }
              }
            }
          }
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

    if ( bdt_filler ) {
      /*
      double lep1_genLepPt = ( selLepton_lead->genLepton()    ) ? selLepton_lead->genLepton()->pt()    : 0.;
      double lep2_genLepPt = ( selLepton_sublead->genLepton() ) ? selLepton_sublead->genLepton()->pt() : 0.;
      double lep3_genLepPt = ( selLepton_third->genLepton()   ) ? selLepton_third->genLepton()->pt()   : 0.;
      */
      //FR weights for bdt ntuple
      prob_fake_lepton_lead = evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main);
      prob_fake_lepton_sublead = evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main);
      prob_fake_lepton_third = evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main);
      /*
      std::cout << "evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main): " << evtWeightRecorder.get_jetToLepton_FR_lead(central_or_shift_main) <<  std::endl;
      std::cout << "evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main): " << evtWeightRecorder.get_jetToLepton_FR_sublead(central_or_shift_main) <<  std::endl;
      std::cout << "evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main): " << evtWeightRecorder.get_jetToLepton_FR_third(central_or_shift_main) <<  std::endl;
      */
      double evtWeight_BDT = evtWeightRecorder.get(central_or_shift_main);
      double lep1_frWeight = lep1_genLepPt > 0 ? 1.0 : prob_fake_lepton_lead;
      double lep2_frWeight = lep2_genLepPt > 0 ? 1.0 : prob_fake_lepton_sublead;
      double lep3_frWeight = lep3_genLepPt > 0 ? 1.0 : prob_fake_lepton_third;
      evtWeight_BDT *= lep1_frWeight*lep2_frWeight*lep3_frWeight;
      bdt_filler -> operator()({ eventInfo.run, eventInfo.lumi, eventInfo.event })
	("nElectron",           selElectrons.size())
	("nMuon",               selMuons.size())
	("nLepton",             selLeptons.size())
	("sumLeptonCharge_3l",     sumLeptonCharge_3l)
	("sumLeptonCharge_FullSel",     sumLeptonCharge_FullSel)
	("numSameFlavor_OS_3l",         numSameFlavor_OS_3l)
	("numSameFlavor_OS_FullPresel", numSameFlavor_OS_Full)
	("nJetAK4",             selJetsAK4.size())
	("nBJetLoose",          selBJetsAK4_loose.size())
	("nBJetMedium",         selBJetsAK4_medium.size())
	("nJetAK8",             jet_ptrs_ak8_Wjj.size())
	("nJetAK8_wSelectorAK8_Wjj", selJetsAK8_Wjj_wSelectorAK8_Wjj.size())
	//
	("lep1_pt",             selLepton_lead -> pt())
	("lep1_conePt",         lep1_conePt)
	("lep1_eta",            selLepton_lead -> eta())
	("mindr_lep1_jet",      TMath::Min(10., mindr_lep1_jet))
        ("mT_MEtLep1",             comp_MT_met(selLepton_lead, met.pt(), met.phi()))
	//
	("lep2_pt",             selLepton_sublead -> pt())
	("lep2_conePt",         lep2_conePt)
	("lep2_eta",            selLepton_sublead -> eta())
	("mindr_lep2_jet",      TMath::Min(10., mindr_lep2_jet))
        ("mT_MEtLep2",             comp_MT_met(selLepton_sublead, met.pt(), met.phi()))
	//
	("lep3_pt",             selLepton_third -> pt())
	("lep3_conePt",         lep3_conePt)
	("lep3_eta",            selLepton_third -> eta())
	("mindr_lep3_jet",      TMath::Min(10., mindr_lep3_jet))
        ("mT_MEtLep3",             comp_MT_met(selLepton_third, met.pt(), met.phi()))
	//
	("jet1_pt",             jet1_pt)
	("jet2_pt",             jet2_pt)
	("jet1plus2pt",         jet1plus2pt)
	("jet1_m",              jet1_m)
	("jet2_m",              jet2_m)
	//
	("avg_dr_jet",          avg_dr_jet)
	("dr_Wjj",              dr_Wjj)
	//
	("dr_l12",            dr_l12)
	("dr_l23",            dr_l23)
	("dr_l13",            dr_l13)	
	("dr_lss",              dr_lss)	
	("dr_los_min",          dr_los_min)
	("dr_los_max",          dr_los_max)
	//
	("dr_WjjLepIdx3",          dr_WjjLepIdx3)
	("dr_Wjet1LepIdx3",        dr_Wjet1LepIdx3)
	("dr_Wjet2LepIdx3",        dr_Wjet2LepIdx3)
	("dr_LepIdx3WjetNear",     dr_LepIdx3WjetNear)
	("dr_LepIdx3WjetFar",      dr_LepIdx3WjetFar)
	//
	("met",                 met.pt())	
	("mht",                 mht_p4.pt())
	("met_LD",              met_LD)
	("HT",                  HT)
	("STMET",               STMET)
	//
	("mSFOS2l",             mSFOS2l)	
	("m_jj",                WTojjMass)	
	("diHiggsVisMass",      dihiggsVisMass_sel)
	("diHiggsMass",         dihiggsMass)
	("mTMetLepton1",        mTMetLepton1)
	("mTMetLepton2",        mTMetLepton2)
	//
	("lep1_isTight",        int(selLepton_lead -> isTight()))
	("lep2_isTight",        int(selLepton_sublead -> isTight()))
	("lep3_isTight",        int(selLepton_third -> isTight()))
	//
	("lep1_genLepPt",       lep1_genLepPt)
	("lep2_genLepPt",       lep2_genLepPt)
	("lep3_genLepPt",       lep3_genLepPt)
	("lep1_frWeight",       lep1_frWeight)
	("lep2_frWeight",       lep2_frWeight)
	("lep3_frWeight",       lep3_frWeight)
	("lep1_fake_prob",      prob_fake_lepton_lead)
	("lep2_fake_prob",      prob_fake_lepton_sublead)
	("lep3_fake_prob",      prob_fake_lepton_third)
	//
	("mT_LeptonIdx1_Met_Approach0", mT_LeptonIdx1_Met_Approach0)
	("mT_LeptonIdx2_Met_Approach0", mT_LeptonIdx2_Met_Approach0)
	("mT_LeptonIdx3_Met_Approach0", mT_LeptonIdx3_Met_Approach0)
	//
	("m_LeptonIdx1_LeptonIdx2_Approach0", m_LeptonIdx1_LeptonIdx2_Approach0)
	("m_LeptonIdx2_LeptonIdx3_Approach0", m_LeptonIdx2_LeptonIdx3_Approach0)
	("m_LeptonIdx1_LeptonIdx3_Approach0", m_LeptonIdx1_LeptonIdx3_Approach0)
	//
	("dPhi_LeptonIdx1_LeptonIdx2_Approach0", dPhi_LeptonIdx1_LeptonIdx2_Approach0)
	("dPhi_LeptonIdx2_LeptonIdx3_Approach0", dPhi_LeptonIdx2_LeptonIdx3_Approach0)
	("dPhi_LeptonIdx1_LeptonIdx3_Approach0", dPhi_LeptonIdx1_LeptonIdx3_Approach0)
	//
	("dr_LeptonIdx1_LeptonIdx2_Approach0", dr_LeptonIdx1_LeptonIdx2_Approach0)
	("dr_LeptonIdx2_LeptonIdx3_Approach0", dr_LeptonIdx2_LeptonIdx3_Approach0)
	("dr_LeptonIdx1_LeptonIdx3_Approach0", dr_LeptonIdx1_LeptonIdx3_Approach0)
	//
	("m_LeptonIdx3_Jet1_Approach0", m_LeptonIdx3_Jet1_Approach0)
	("dr_LeptonIdx3_Jet1_Approach0", dr_LeptonIdx3_Jet1_Approach0)
	//
	("m_LeptonIdx3_JetNear_Approach0", m_LeptonIdx3_JetNear_Approach0)
	("dr_LeptonIdx3_JetNear_Approach0", dr_LeptonIdx3_JetNear_Approach0)
	//
	("mT_LeptonIdx1_Met_Approach2", mT_LeptonIdx1_Met_Approach2)
	("mT_LeptonIdx2_Met_Approach2", mT_LeptonIdx2_Met_Approach2)
	("mT_LeptonIdx3_Met_Approach2", mT_LeptonIdx3_Met_Approach2)
	//
	("m_LeptonIdx1_LeptonIdx2_Approach2", m_LeptonIdx1_LeptonIdx2_Approach2)
	("m_LeptonIdx2_LeptonIdx3_Approach2", m_LeptonIdx2_LeptonIdx3_Approach2)
	("m_LeptonIdx1_LeptonIdx3_Approach2", m_LeptonIdx1_LeptonIdx3_Approach2)
	//
	("dPhi_LeptonIdx1_LeptonIdx2_Approach2", dPhi_LeptonIdx1_LeptonIdx2_Approach2)
	("dPhi_LeptonIdx2_LeptonIdx3_Approach2", dPhi_LeptonIdx2_LeptonIdx3_Approach2)
	("dPhi_LeptonIdx1_LeptonIdx3_Approach2", dPhi_LeptonIdx1_LeptonIdx3_Approach2)
	//
	("dr_LeptonIdx1_LeptonIdx2_Approach2", dr_LeptonIdx1_LeptonIdx2_Approach2)
	("dr_LeptonIdx2_LeptonIdx3_Approach2", dr_LeptonIdx2_LeptonIdx3_Approach2)
	("dr_LeptonIdx1_LeptonIdx3_Approach2", dr_LeptonIdx1_LeptonIdx3_Approach2)
	//
	("m_LeptonIdx3_Jet1_Approach2", m_LeptonIdx3_Jet1_Approach2)
	("dr_LeptonIdx3_Jet1_Approach2", dr_LeptonIdx3_Jet1_Approach2)
	//
	("m_LeptonIdx3_JetNear_Approach2", m_LeptonIdx3_JetNear_Approach2)
	("dr_LeptonIdx3_JetNear_Approach2", dr_LeptonIdx3_JetNear_Approach2)
	//
	("eventCategory",       eventCategory)
	//
        ("lumiScale",           evtWeightRecorder.get_lumiScale(central_or_shift_main))
	("genWeight",           eventInfo.genWeight)
        ("evtWeight",           evtWeight_BDT)
	("lheWeight" , evtWeightRecorder.get_lheScaleWeight(central_or_shift_main))
	("pileupWeight", evtWeightRecorder.get_puWeight(central_or_shift_main))
	("triggerWeight", evtWeightRecorder.get_sf_triggerEff(central_or_shift_main))
	("btagWeight", evtWeightRecorder.get_btag(central_or_shift_main))
	("leptonEffSF", evtWeightRecorder.get_leptonSF())
	("data_to_MC_correction", evtWeightRecorder.get_data_to_MC_correction(central_or_shift_main))
	("FR_Weight", evtWeightRecorder.get_FR(central_or_shift_main))
	(weightMapHH)
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
    if (isSignal && !skipHHDecayModeHistograms) {
      std::string decayMode_and_genMatch = process_string;
      decayMode_and_genMatch += ("_DecayMode_" + eventInfo.getDiHiggsDecayModeString());
      ++selectedEntries_byDecayModeType[decayMode_and_genMatch];
      for(const std::string & central_or_shift: central_or_shifts_local)
	{
	  selectedEntries_weighted_byDecayModeType[central_or_shift][decayMode_and_genMatch] += evtWeightRecorder.get(central_or_shift);
	}
    }
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
    std::cout << "Lepton genMatch-wise:\n";
    for(const leptonGenMatchEntry & leptonGenMatch_definition: leptonGenMatch_definitions)
    {
      std::string process_and_genMatch = process_string;
      process_and_genMatch += leptonGenMatch_definition.name_;
      std::cout << " " << process_and_genMatch << " = " << selectedEntries_byGenMatchType[process_and_genMatch]
                << " (weighted = " << selectedEntries_weighted_byGenMatchType[central_or_shift][process_and_genMatch] << ")\n";
    }

    if (isSignal && !skipHHDecayModeHistograms) {
      std::cout << "Lepton DecayMode-wise:\n";
      const vstring decayModes_evt = eventInfo.getDiHiggsDecayModes();
      for(const std::string & decayMode_evt: decayModes_evt)
	{
	  std::string decayMode_and_genMatch = process_string;      
	  decayMode_and_genMatch += ("_DecayMode_" + decayMode_evt);
	  std::cout << " " << decayMode_and_genMatch << " = " << selectedEntries_byDecayModeType[decayMode_and_genMatch]
		    << " (weighted = " << selectedEntries_weighted_byDecayModeType[central_or_shift][decayMode_and_genMatch] << ")\n";
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

  delete run_lumi_eventSelector;

  delete selEventsFile;

  delete muonReader;
  delete electronReader;
  delete hadTauReader;
  delete jetReaderAK4;
  delete metReader;
  delete metFilterReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genPhotonReader;
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

  clock.Show("analyze_hh_3l");

  return EXIT_SUCCESS;
}
