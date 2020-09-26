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
#include <TMatrixD.h> // TMatrixD
#include <TError.h> // gErrorAbortLevel, kError
#include <TMath.h> // TMath::
#include <TH2.h> // TH2

#include "tthAnalysis/HiggsToTauTau/interface/RecoLepton.h" // RecoLepton
#include "tthAnalysis/HiggsToTauTau/interface/RecoJet.h" // RecoJet
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTau.h" // RecoHadTau
#include "tthAnalysis/HiggsToTauTau/interface/GenLepton.h" // GenLepton
#include "tthAnalysis/HiggsToTauTau/interface/GenJet.h" // GenJet
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTau.h" // GenHadTau
#include "tthAnalysis/HiggsToTauTau/interface/Particle.h" // Particle::LorentzVector
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEt.h" // RecoMEt
#include "tthAnalysis/HiggsToTauTau/interface/RecoElectronReader.h" // RecoElectronReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMuonReader.h" // RecoMuonReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoHadTauReader.h" // RecoHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoJetReader.h" // RecoJetReader
#include "tthAnalysis/HiggsToTauTau/interface/RecoMEtReader.h" // RecoMEtReader
#include "tthAnalysis/HiggsToTauTau/interface/GenLeptonReader.h" // GenLeptonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenHadTauReader.h" // GenHadTauReader
#include "tthAnalysis/HiggsToTauTau/interface/GenPhotonReader.h" // GenPhotonReader
#include "tthAnalysis/HiggsToTauTau/interface/GenJetReader.h" // GenJetReader
#include "tthAnalysis/HiggsToTauTau/interface/GenParticleReader.h" // GenParticleReader
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
#include "tthAnalysis/HiggsToTauTau/interface/ElectronHistManager.h" // ElectronHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MuonHistManager.h" // MuonHistManager
#include "tthAnalysis/HiggsToTauTau/interface/HadTauHistManager.h" // HadTauHistManager
#include "tthAnalysis/HiggsToTauTau/interface/JetHistManager.h" // JetHistManager
#include "tthAnalysis/HiggsToTauTau/interface/MEtHistManager.h" // MEtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/WeightHistManager.h" // WeightHistManager
#include "tthAnalysis/HiggsToTauTau/interface/GenEvtHistManager.h" // GenEvtHistManager
#include "tthAnalysis/HiggsToTauTau/interface/leptonTypes.h" // getLeptonType, kElectron, kMuon
#include "tthAnalysis/HiggsToTauTau/interface/analysisAuxFunctions.h" // isHigherPt, isMatched
#include "tthAnalysis/HiggsToTauTau/interface/sysUncertOptions.h" // getHadTauPt_option, getMET_option
#include "tthAnalysis/HiggsToTauTau/interface/HistManagerBase.h" // HistManagerBase
#include "tthAnalysis/HiggsToTauTau/interface/TTreeWrapper.h" // TTreeWrapper
#include "tthAnalysis/HiggsToTauTau/interface/EvtWeightManager.h" // EvtWeightManager

#include "hhAnalysis/multilepton/interface/EvtHistManager_SVfit4tau.h" // EvtHistManager_SVfit4tau
#include "hhAnalysis/multilepton/interface/SVfit4tauHistManager_MarkovChain.h" // SVfit4tauHistManager_MarkovChain
#include "hhAnalysis/multilepton/interface/SVfit4tauResolutionHistManager_MarkovChain.h" // SVfit4tauResolutionHistManager_MarkovChain
#include "hhAnalysis/multilepton/interface/SVfit4tauHistManager_VAMP.h" // SVfit4tauHistManager_VAMP
#include "hhAnalysis/multilepton/interface/SVfit4tauResolutionHistManager_VAMP.h" // SVfit4tauResolutionHistManager_VAMP
#include "hhAnalysis/multilepton/interface/SVfit4tauDisambiguationHistManager.h" // SVfit4tauDisambiguationHistManager
#include "hhAnalysis/multilepton/interface/GenHadTauSmearer.h" // GenHadTauSmearer
#include "hhAnalysis/multilepton/interface/GenMEtSmearer.h" // GenMEtSmearer
#include "hhAnalysis/multilepton/interface/mySVfit4tauAuxFunctions.h" // SVfit4tauResult, getMeasuredTauLeptonType, getHadTauDecayMode
#include "tthAnalysis/HiggsToTauTau/interface/EventInfo.h" // EventInfo
#include "tthAnalysis/HiggsToTauTau/interface/EventInfoReader.h" // EventInfoReader

#include "TauAnalysis/ClassicSVfit4tau/interface/ClassicSVfit4tau.h" // ClassicSVfit4tau
#include "TauAnalysis/ClassicSVfit/interface/MeasuredTauLepton.h" // classic_svFit::MeasuredTauLepton
#include "TauAnalysis/ClassicSVfit4tau/interface/svFitHistogramAdapter4tau.h" // HistogramAdapterDiHiggs, HistogramAdapterHiggs

#include "hhAnalysis/multilepton/interface/RecoElectronCollectionSelectorFakeable_hh_multilepton.h"
#include "hhAnalysis/multilepton/interface/RecoMuonCollectionSelectorFakeable_hh_multilepton.h"

#include <boost/math/special_functions/sign.hpp> // boost::math::sign()

#include <iostream> // std::cerr, std::fixed
#include <iomanip> // std::setprecision(), std::setw()
#include <string> // std::string
#include <vector> // std::vector<>
#include <cstdlib> // EXIT_SUCCESS, EXIT_FAILURE
#include <algorithm> // std::sort
#include <fstream> // std::ofstream
#include <assert.h> // assert

typedef std::vector<std::string> vstring;
typedef std::vector<double> vdouble;

enum { kMode_undefined, kMode_rec, kMode_gen, kMode_genSmeared };

enum { k4lepton, k3lepton_1tau, k2lepton_2tau, k1lepton_3tau, k4tau };

int get_idxCategory(const std::string& category) 
{
  if      ( category == "4lepton"      ) return k4lepton;
  else if ( category == "3lepton_1tau" ) return k3lepton_1tau;
  else if ( category == "2lepton_2tau" ) return k2lepton_2tau;
  else if ( category == "1lepton_3tau" ) return k1lepton_3tau;
  else if ( category == "4tau"         ) return k4tau;
  else assert(0);
}

int get_idxCategory(int numLeptons, int numHadTaus) 
{
  if      ( numLeptons >= 4 && numHadTaus >= 0 ) return k4lepton;
  else if ( numLeptons == 3 && numHadTaus >= 1 ) return k3lepton_1tau;
  else if ( numLeptons == 2 && numHadTaus >= 2 ) return k2lepton_2tau;
  else if ( numLeptons == 1 && numHadTaus >= 3 ) return k1lepton_3tau;
  else if ( numLeptons == 0 && numHadTaus >= 4 ) return k4tau;
  else assert(0);
}

const GenParticle* findGenTau(const ChargedParticle & measuredTau, const std::vector<GenParticle>& genTaus)
{
  const GenParticle* bestMatch = nullptr;
  double dR_min = 1.e+3;
  for ( std::vector<GenParticle>::const_iterator genTau = genTaus.begin();
        genTau != genTaus.end(); ++genTau ) {
    double dR = deltaR(measuredTau.p4(), genTau->p4());
    if ( dR < 0.3 && dR < dR_min ) {
      bestMatch = &(*genTau);
      dR_min = dR;
    }
  }
  return bestMatch;
}

const GenParticle* getGenMeasuredTau(const ChargedParticle& measuredTau)
{
  const GenParticle* measuredTau_gen = nullptr;
  if ( dynamic_cast<const RecoLepton*>(&measuredTau) ) {
    const RecoLepton* measuredLepton = dynamic_cast<const RecoLepton*>(&measuredTau);
    if      ( measuredLepton->genLepton() ) measuredTau_gen = measuredLepton->genLepton();
    else if ( measuredLepton->genHadTau() ) measuredTau_gen = measuredLepton->genHadTau();
  } else if ( dynamic_cast<const RecoHadTau*>(&measuredTau) ) {
    const RecoHadTau* measuredHadTau = dynamic_cast<const RecoHadTau*>(&measuredTau);
    if      ( measuredHadTau->genLepton() ) measuredTau_gen = measuredHadTau->genLepton();
    else if ( measuredHadTau->genHadTau() ) measuredTau_gen = measuredHadTau->genHadTau();
  } else assert(0);
  return measuredTau_gen;
}

double square(double x)
{
  return x*x;
}

const GenParticle* findGenHiggs(const Particle::LorentzVector& p4, const std::vector<GenParticle>& genHiggsBosons)
{
  const GenParticle* bestMatch = nullptr;
  double d_min = 1.e+3;
  for ( std::vector<GenParticle>::const_iterator genHiggsBoson = genHiggsBosons.begin();
        genHiggsBoson != genHiggsBosons.end(); ++genHiggsBoson ) {
    double d = TMath::Sqrt(square(genHiggsBoson->p4().px() - p4.px()) + square(genHiggsBoson->p4().py() - p4.py()) + square(genHiggsBoson->p4().pz() - p4.pz()));
    if ( d < 5. && d < d_min ) {
      bestMatch = &(*genHiggsBoson);
      d_min = d;
    }
  }
  return bestMatch;
}

struct SVfit4tauResult_wPtrs : public SVfit4tauResult
{
  SVfit4tauResult_wPtrs(const SVfit4tauResult& result)
    : SVfit4tauResult(result)
    , isCorrectAssoc_(false)
  {}
  ~SVfit4tauResult_wPtrs() {}
  Particle::LorentzVector measuredTau1Higgs1P4_;
  Particle::LorentzVector measuredTau2Higgs1P4_;
  Particle::LorentzVector measuredTau1Higgs2P4_;
  Particle::LorentzVector measuredTau2Higgs2P4_;
  Particle::LorentzVector genDiHiggsP4_;
  Particle::LorentzVector genDiTau1P4_;
  Particle::LorentzVector genDiTau2P4_;
  bool isCorrectAssoc_;
};

typedef std::vector<SVfit4tauResult_wPtrs> vSVfit4tauResult_wPtrs;

const int hadTauSelection_antiElectron = 1; // vLoose
const int hadTauSelection_antiMuon = 1; // Loose

/**
 * @brief Produce resolution plots of pT, eta, phi, and mass of di-Higgs system reconstructed by ClassicSVfit4tau algorithm
 */
int main(int argc, char* argv[])
{
//--- throw an exception in case ROOT encounters an error
  gErrorAbortLevel = kError;

//--- parse command-line arguments
  if ( argc < 2 ) {
    std::cout << "Usage: " << argv[0] << " [parameters.py]" << std::endl;
    return EXIT_FAILURE;
  }

  std::cout << "<analyze_SVfit4tau>:" << std::endl;

//--- keep track of time it takes the macro to execute
  TBenchmark clock;
  clock.Start("analyze_SVfit4tau");

//--- read python configuration parameters
  if ( !edm::readPSetsFrom(argv[1])->existsAs<edm::ParameterSet>("process") )
    throw cms::Exception("analyze_SVfit4tau")
      << "No ParameterSet 'process' found in configuration file = " << argv[1] << " !!\n";

  edm::ParameterSet cfg = edm::readPSetsFrom(argv[1])->getParameter<edm::ParameterSet>("process");

  edm::ParameterSet cfg_analyze = cfg.getParameter<edm::ParameterSet>("analyze_SVfit4tau");

  std::string treeName = cfg_analyze.getParameter<std::string>("treeName");

  std::string process_string = cfg_analyze.getParameter<std::string>("process");

  std::string histogramDir = cfg_analyze.getParameter<std::string>("histogramDir");

  std::string era_string = cfg_analyze.getParameter<std::string>("era");
  const Era era = get_era(era_string);

  std::string mode_string = cfg_analyze.getParameter<std::string>("mode");
  int mode = kMode_undefined;
  if      ( mode_string == "rec"         ) mode = kMode_rec;
  else if ( mode_string == "gen"         ) mode = kMode_gen;
  else if ( mode_string == "gen_smeared" ) mode = kMode_genSmeared;
  else throw cms::Exception("analyze_SVfit4tau")
    << "Invalid Configuration parameter 'mode' = " << mode_string << " !!\n";

  std::string leptonSelection_string = cfg_analyze.getParameter<std::string>("leptonSelection").data();
  std::cout << "leptonSelection_string = " << leptonSelection_string << std::endl;
  int leptonSelection = -1;
  if      ( leptonSelection_string == "Loose"                                                      ) leptonSelection = kLoose;
  else if ( leptonSelection_string == "Fakeable" || leptonSelection_string == "Fakeable_mcClosure" ) leptonSelection = kFakeable;
  else if ( leptonSelection_string == "Tight"                                                      ) leptonSelection = kTight;
  else throw cms::Exception("analyze_SVfit4tau")
    << "Invalid Configuration parameter 'leptonSelection' = " << leptonSelection_string << " !!\n";

  TString hadTauSelection_string = cfg_analyze.getParameter<std::string>("hadTauSelection").data();
  TObjArray* hadTauSelection_parts = hadTauSelection_string.Tokenize("|");
  assert(hadTauSelection_parts->GetEntries() >= 1);
  std::string hadTauSelection_part1 = (dynamic_cast<TObjString*>(hadTauSelection_parts->At(0)))->GetString().Data();
  int hadTauSelection = -1;
  if      ( hadTauSelection_part1 == "Loose"                                                     ) hadTauSelection = kLoose;
  else if ( hadTauSelection_part1 == "Fakeable" || hadTauSelection_part1 == "Fakeable_mcClosure" ) hadTauSelection = kFakeable;
  else if ( hadTauSelection_part1 == "Tight"                                                     ) hadTauSelection = kTight;
  else throw cms::Exception("analyze_SVfit4tau")
    << "Invalid Configuration parameter 'hadTauSelection' = " << hadTauSelection_string << " !!\n";
  std::string hadTauSelection_part2 = ( hadTauSelection_parts->GetEntries() == 2 ) ? (dynamic_cast<TObjString*>(hadTauSelection_parts->At(1)))->GetString().Data() : "";
  delete hadTauSelection_parts;

  const double lep_mva_cut_mu = cfg_analyze.getParameter<double>("lep_mva_cut_mu");
  const double lep_mva_cut_e  = cfg_analyze.getParameter<double>("lep_mva_cut_e");
 
  edm::ParameterSet cfgSVfit4tau = cfg_analyze.getParameter<edm::ParameterSet>("SVfit4tau");
  vdouble logM_wMassConstraint_MarkovChain = cfgSVfit4tau.getParameter<vdouble>("logM_wMassConstraint_MarkovChain");
  vdouble logM_woMassConstraint_MarkovChain = cfgSVfit4tau.getParameter<vdouble>("logM_woMassConstraint_MarkovChain");
  vdouble logM_wMassConstraint_VAMP = cfgSVfit4tau.getParameter<vdouble>("logM_wMassConstraint_VAMP");

  bool use_HIP_mitigation_mediumMuonId = cfg_analyze.getParameter<bool>("use_HIP_mitigation_mediumMuonId");
  std::cout << "use_HIP_mitigation_mediumMuonId = " << use_HIP_mitigation_mediumMuonId << std::endl;

  bool isMC = cfg_analyze.getParameter<bool>("isMC");
  std::string central_or_shift = cfg_analyze.getParameter<std::string>("central_or_shift");
  double lumiScale = ( process_string != "data_obs" ) ? cfg_analyze.getParameter<double>("lumiScale") : 1.;
  bool apply_genWeight = cfg_analyze.getParameter<bool>("apply_genWeight");

  const edm::ParameterSet additionalEvtWeight = cfg_analyze.getParameter<edm::ParameterSet>("evtWeight");
  const bool applyAdditionalEvtWeight = additionalEvtWeight.getParameter<bool>("apply");
  EvtWeightManager * eventWeightManager = nullptr;
  if(applyAdditionalEvtWeight)
  {
    eventWeightManager = new EvtWeightManager(additionalEvtWeight);
  }

  bool isDEBUG = ( cfg_analyze.exists("isDEBUG") ) ? cfg_analyze.getParameter<bool>("isDEBUG") : false;
  if ( isDEBUG ) std::cout << "Warning: DEBUG mode enabled -> trigger selection will not be applied for data !!" << std::endl;

  const int hadTauPt_option = getHadTauPt_option(central_or_shift);
  const int met_option = getMET_option(central_or_shift, isMC);

  bool fillGenEvtHistograms = cfg_analyze.getParameter<bool>("fillGenEvtHistograms");

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

  std::string branchName_genTaus = cfg_analyze.getParameter<std::string>("branchName_genTaus");
  std::string branchName_genHiggsBosons = cfg_analyze.getParameter<std::string>("branchName_genHiggsBosons");

  edm::ParameterSet cfgGenHadTauSmearing = cfg_analyze.getParameter<edm::ParameterSet>("genHadTauSmearing");
  GenHadTauSmearer genHadTauSmearer(cfgGenHadTauSmearing);
  edm::ParameterSet cfgGenMEtSmearing = cfg_analyze.getParameter<edm::ParameterSet>("genMEtSmearing");
  GenMEtSmearer genMEtSmearer(cfgGenMEtSmearing);
  double sigmaX = cfgGenMEtSmearing.getParameter<double>("sigmaX");
  double sigmaY = cfgGenMEtSmearing.getParameter<double>("sigmaY");

  std::string selEventsFileName_input = cfg_analyze.getParameter<std::string>("selEventsFileName_input");
  std::cout << "selEventsFileName_input = " << selEventsFileName_input << std::endl;
  RunLumiEventSelector* run_lumi_eventSelector = 0;
  if ( selEventsFileName_input != "" ) {
    edm::ParameterSet cfgRunLumiEventSelector;
    cfgRunLumiEventSelector.addParameter<std::string>("inputFileName", selEventsFileName_input);
    cfgRunLumiEventSelector.addParameter<std::string>("separator", ":");
    run_lumi_eventSelector = new RunLumiEventSelector(cfgRunLumiEventSelector);
  }

  fwlite::InputSource inputFiles(cfg);
  int maxEvents = inputFiles.maxEvents();
  std::cout << " maxEvents = " << maxEvents << std::endl;
  unsigned reportEvery = inputFiles.reportAfter();

  fwlite::OutputFiles outputFile(cfg);
  fwlite::TFileService fs = fwlite::TFileService(outputFile.file().data());

  TTreeWrapper* inputTree = new TTreeWrapper(treeName.data(), inputFiles.files(), maxEvents);
  std::cout << "Loaded " << inputTree->getFileCount() << " file(s).\n";

//--- declare event-level variables
  EventInfo eventInfo(isMC);
  EventInfoReader eventInfoReader(&eventInfo);
  inputTree->registerReader(&eventInfoReader);

  if(eventWeightManager)
  {
    inputTree->registerReader(eventWeightManager);
  }

//--- declare particle collections
  const bool readGenObjects = isMC && !redoGenMatching;
  RecoMuonReader* muonReader = new RecoMuonReader(era, branchName_muons, isMC, readGenObjects);
  inputTree->registerReader(muonReader);
  RecoMuonCollectionGenMatcher muonGenMatcher;
  RecoMuonCollectionSelectorLoose preselMuonSelector(era);
  //RecoMuonCollectionSelectorFakeable fakeableMuonSelector(era);
  RecoMuonCollectionSelectorFakeable_hh_multilepton fakeableMuonSelector(era, -1, isDEBUG);
  RecoMuonCollectionSelectorTight tightMuonSelector(era);
  muonReader->set_mvaTTH_wp(lep_mva_cut_mu);

  RecoElectronReader* electronReader = new RecoElectronReader(era, branchName_electrons, isMC, readGenObjects);
  inputTree->registerReader(electronReader);
  RecoElectronCollectionGenMatcher electronGenMatcher;
  RecoElectronCollectionCleaner electronCleaner(0.3);
  RecoElectronCollectionSelectorLoose preselElectronSelector(era);
  //RecoElectronCollectionSelectorFakeable fakeableElectronSelector(era);
  RecoElectronCollectionSelectorFakeable_hh_multilepton fakeableElectronSelector(era, -1, isDEBUG);
  RecoElectronCollectionSelectorTight tightElectronSelector(era);
  electronReader->set_mvaTTH_wp(lep_mva_cut_e);

  RecoHadTauReader* hadTauReader = new RecoHadTauReader(era, branchName_hadTaus, isMC, readGenObjects);
  hadTauReader->setHadTauPt_central_or_shift(hadTauPt_option);
  inputTree->registerReader(hadTauReader);
  RecoHadTauCollectionGenMatcher hadTauGenMatcher;
  RecoHadTauCollectionCleaner hadTauCleaner(0.3);
  RecoHadTauCollectionSelectorFakeable fakeableHadTauSelector(era);
  fakeableHadTauSelector.set_if_looser(hadTauSelection_part2);
  fakeableHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  fakeableHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);
  RecoHadTauCollectionSelectorTight tightHadTauSelector(era);
  tightHadTauSelector.set(hadTauSelection_part2);
  tightHadTauSelector.set_min_antiElectron(hadTauSelection_antiElectron);
  tightHadTauSelector.set_min_antiMuon(hadTauSelection_antiMuon);

  RecoJetReader* jetReader = new RecoJetReader(era, isMC, branchName_jets, readGenObjects);
  inputTree->registerReader(jetReader);
  RecoJetCollectionGenMatcher jetGenMatcher;
  RecoJetCollectionCleaner jetCleaner(0.4);
  RecoJetCollectionCleanerByIndex jetCleanerByIndex(isDEBUG);
  RecoJetCollectionSelector jetSelector(era);
  RecoJetCollectionSelectorBtagLoose jetSelectorBtagLoose(era);
  RecoJetCollectionSelectorBtagMedium jetSelectorBtagMedium(era);

//--- declare missing transverse energy
  RecoMEtReader* metReader = new RecoMEtReader(era, isMC, branchName_met);
  metReader->setMEt_central_or_shift(met_option);
  inputTree -> registerReader(metReader);

//--- declare generator level information
  GenLeptonReader * genLeptonReader = nullptr;
  GenHadTauReader * genHadTauReader = nullptr;
  GenPhotonReader * genPhotonReader = nullptr;
  GenJetReader * genJetReader = nullptr;
  GenParticleReader * genTauReader = nullptr;
  GenParticleReader * genHiggsBosonReader = nullptr;

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
    genTauReader = new GenParticleReader(branchName_genTaus);
    inputTree->registerReader(genTauReader);
    genHiggsBosonReader = new GenParticleReader(branchName_genHiggsBosons);
    inputTree->registerReader(genHiggsBosonReader);
  }

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
    JetHistManager* leadJet_;
    JetHistManager* subleadJet_;
    JetHistManager* BJets_loose_;
    JetHistManager* BJets_medium_;
    MEtHistManager* met_;
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_wMassConstraint_MarkovChain_correctAssoc_chosen_;                           // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_chosen_;       // key = logM_wMassConstraint
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_wMassConstraint_MarkovChain_correctAssoc_discarded_;                        // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_discarded_;    // key = logM_wMassConstraint
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_chosen_;                         // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_chosen_;     // key = logM_wMassConstraint
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_discarded_;                      // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_discarded_;  // key = logM_wMassConstraint
    std::map<double, SVfit4tauDisambiguationHistManager*> svFit4tauDisambiguation_wMassConstraint_MarkovChain_;                               // key = logM_wMassConstraint
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_woMassConstraint_MarkovChain_correctAssoc_chosen_;                          // key = logM_woMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_chosen_;      // key = logM_woMassConstraint
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_woMassConstraint_MarkovChain_correctAssoc_discarded_;                       // key = logM_woMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_discarded_;   // key = logM_woMassConstraint
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_chosen_;                        // key = logM_woMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_chosen_;    // key = logM_woMassConstraint
    std::map<double, SVfit4tauHistManager_MarkovChain*> svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_discarded_;                     // key = logM_woMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_MarkovChain*> svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_discarded_; // key = logM_woMassConstraint
    std::map<double, SVfit4tauHistManager_VAMP*> svFit4tau_wMassConstraint_VAMP_correctAssoc_chosen_;                                         // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_VAMP*> svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_chosen_;                     // key = logM_wMassConstraint
    std::map<double, SVfit4tauHistManager_VAMP*> svFit4tau_wMassConstraint_VAMP_correctAssoc_discarded_;                                      // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_VAMP*> svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_discarded_;                  // key = logM_wMassConstraint
    std::map<double, SVfit4tauHistManager_VAMP*> svFit4tau_wMassConstraint_VAMP_incorrectAssoc_chosen_;                                       // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_VAMP*> svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_chosen_;                   // key = logM_wMassConstraint
    std::map<double, SVfit4tauHistManager_VAMP*> svFit4tau_wMassConstraint_VAMP_incorrectAssoc_discarded_;                                    // key = logM_wMassConstraint
    std::map<double, SVfit4tauResolutionHistManager_VAMP*> svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_discarded_;                // key = logM_wMassConstraint
    std::map<double, SVfit4tauDisambiguationHistManager*> svFit4tauDisambiguation_wMassConstraint_VAMP_;                                      // key = logM_wMassConstraint
    EvtHistManager_SVfit4tau* evt_;
    WeightHistManager* weights_;
  };
  std::map<int, selHistManagerType*> selHistManagers;

  vstring categories = { "4lepton", "3lepton_1tau", "2lepton_2tau", "1lepton_3tau", "4tau" };
  for ( vstring::const_iterator category = categories.begin();
        category != categories.end(); ++category ) {

    TString histogramDir_category = histogramDir.data();
    histogramDir_category.ReplaceAll("SVfit4tau", Form("SVfit4tau_%s", category->data()));

    selHistManagerType* selHistManager = new selHistManagerType();
    selHistManager->electrons_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/electrons", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->electrons_->bookHistograms(fs);
    selHistManager->leadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadElectron", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 0));
    selHistManager->leadElectron_->bookHistograms(fs);
    selHistManager->subleadElectron_ = new ElectronHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadElectron", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 1));
    selHistManager->subleadElectron_->bookHistograms(fs);
    selHistManager->muons_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/muons", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->muons_->bookHistograms(fs);
    selHistManager->leadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadMuon", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 0));
    selHistManager->leadMuon_->bookHistograms(fs);
    selHistManager->subleadMuon_ = new MuonHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadMuon", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 1));
    selHistManager->subleadMuon_->bookHistograms(fs);
    selHistManager->hadTaus_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/hadTaus", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->hadTaus_->bookHistograms(fs);
    selHistManager->leadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadHadTau", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 0));
    selHistManager->leadHadTau_->bookHistograms(fs);
    selHistManager->subleadHadTau_ = new HadTauHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadHadTau", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 1));
    selHistManager->subleadHadTau_->bookHistograms(fs);
    selHistManager->jets_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/jets", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->jets_->bookHistograms(fs);
    selHistManager->leadJet_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/leadJet", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 0));
    selHistManager->leadJet_->bookHistograms(fs);
    selHistManager->subleadJet_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/subleadJet", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift, 1));
    selHistManager->subleadJet_->bookHistograms(fs);
    selHistManager->BJets_loose_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/BJets_loose", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->BJets_loose_->bookHistograms(fs);
    selHistManager->BJets_medium_ = new JetHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/BJets_medium", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->BJets_medium_->bookHistograms(fs);
    selHistManager->met_ = new MEtHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/met", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->met_->bookHistograms(fs);
    for ( vdouble::const_iterator logM = logM_wMassConstraint_MarkovChain.begin();
          logM != logM_wMassConstraint_MarkovChain.end(); ++logM ) {
      std::string logM_string = TString(Form("logM%1.1f", *logM)).ReplaceAll(".", "p").Data();
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_chosen_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_MarkovChain_correctAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_chosen_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_chosen_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_MarkovChain_correctAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_discarded_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_MarkovChain_correctAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_discarded_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_discarded_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_MarkovChain_correctAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_MarkovChain_incorrectAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_MarkovChain_incorrectAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_MarkovChain_incorrectAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_MarkovChain_incorrectAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tauDisambiguation_wMassConstraint_MarkovChain_[*logM] = new SVfit4tauDisambiguationHistManager(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauDisambiguation_wMassContraint_%s_MarkovChain", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauDisambiguation_wMassConstraint_MarkovChain_[*logM]->bookHistograms(fs);
    }
    for ( vdouble::const_iterator logM = logM_woMassConstraint_MarkovChain.begin();
          logM != logM_woMassConstraint_MarkovChain.end(); ++logM ) {
      std::string logM_string = TString(Form("logM%1.1f", *logM)).ReplaceAll(".", "p").Data();
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_correctAssoc_chosen_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_woMassContraint_%s_MarkovChain_correctAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_correctAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_chosen_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_woMassContraint_%s_MarkovChain_correctAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_correctAssoc_discarded_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_woMassContraint_%s_MarkovChain_correctAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_correctAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_discarded_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_woMassContraint_%s_MarkovChain_correctAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_woMassContraint_%s_MarkovChain_incorrectAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_woMassContraint_%s_MarkovChain_incorrectAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM] = new SVfit4tauHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_woMassContraint_%s_MarkovChain_incorrectAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM] = new SVfit4tauResolutionHistManager_MarkovChain(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_woMassContraint_%s_MarkovChain_incorrectAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM]->bookHistograms(fs);
    }
    for ( vdouble::const_iterator logM = logM_wMassConstraint_VAMP.begin();
          logM != logM_wMassConstraint_VAMP.end(); ++logM ) {
      std::string logM_string = TString(Form("logM%1.1f", *logM)).ReplaceAll(".", "p").Data();
      selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_chosen_[*logM] = new SVfit4tauHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_VAMP_correctAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_chosen_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_chosen_[*logM] = new SVfit4tauResolutionHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_VAMP_correctAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_discarded_[*logM] = new SVfit4tauHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_VAMP_correctAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_discarded_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_discarded_[*logM] = new SVfit4tauResolutionHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_VAMP_correctAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_chosen_[*logM] = new SVfit4tauHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_VAMP_incorrectAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_chosen_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_chosen_[*logM] = new SVfit4tauResolutionHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_VAMP_incorrectAssoc_chosen", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_chosen_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_discarded_[*logM] = new SVfit4tauHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tau_wMassContraint_%s_VAMP_incorrectAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_discarded_[*logM]->bookHistograms2d(fs);
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_discarded_[*logM] = new SVfit4tauResolutionHistManager_VAMP(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauResolution_wMassContraint_%s_VAMP_incorrectAssoc_discarded", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_discarded_[*logM]->bookHistograms(fs);
      selHistManager->svFit4tauDisambiguation_wMassConstraint_VAMP_[*logM] = new SVfit4tauDisambiguationHistManager(makeHistManager_cfg(process_string,
        Form("%s/%s/svFit4tauDisambiguation_wMassContraint_%s_VAMP", histogramDir_category.Data(), mode_string.data(), logM_string.data()), era_string, central_or_shift));
      selHistManager->svFit4tauDisambiguation_wMassConstraint_VAMP_[*logM]->bookHistograms(fs);
    }
    selHistManager->evt_ = new EvtHistManager_SVfit4tau(makeHistManager_cfg(process_string,
      Form("%s/%s/evt", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->evt_->bookHistograms(fs);
    selHistManager->weights_ = new WeightHistManager(makeHistManager_cfg(process_string,
      Form("%s/%s/weights", histogramDir_category.Data(), mode_string.data()), era_string, central_or_shift));
    selHistManager->weights_->bookHistograms(fs, { "genWeight", "pileupWeight" });
    int idxCategory = get_idxCategory(*category);
    selHistManagers[idxCategory] = selHistManager;
  }

  GenEvtHistManager* genEvtHistManager_beforeCuts = 0;
  GenEvtHistManager* genEvtHistManager_afterCuts = 0;
  if ( isMC ) {
    genEvtHistManager_beforeCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/unbiased/genEvt", histogramDir.data()), era_string, central_or_shift));
    genEvtHistManager_beforeCuts->bookHistograms(fs);
    genEvtHistManager_afterCuts = new GenEvtHistManager(makeHistManager_cfg(process_string,
      Form("%s/sel/genEvt", histogramDir.data()), era_string, central_or_shift));
    genEvtHistManager_afterCuts->bookHistograms(fs);
  }

  int analyzedEntries = 0;
  int selectedEntries = 0;
  double selectedEntries_weighted = 0.;
  TH1* histogram_analyzedEntries = fs.make<TH1D>("analyzedEntries", "analyzedEntries", 1, -0.5, +0.5);
  TH1* histogram_selectedEntries = fs.make<TH1D>("selectedEntries", "selectedEntries", 1, -0.5, +0.5);

  while ( inputTree->hasNextEvent() && (!run_lumi_eventSelector || (run_lumi_eventSelector && !run_lumi_eventSelector->areWeDone())) ) {
    if ( inputTree->canReport(reportEvery) ) {
      std::cout << "processing Entry " << inputTree->getCurrentMaxEventIdx() << " or " << inputTree->getCurrentEventIdx() << " entry" 
                << " in #" << (inputTree -> getProcessedFileCount() - 1) << " (" << eventInfo << ") file (" << selectedEntries << " Entries selected)\n";
    }
    ++analyzedEntries;
    histogram_analyzedEntries->Fill(0.);
    
    if ( isDEBUG ) {
      std::cout << "event #" << inputTree -> getCurrentMaxEventIdx() << ' ' << eventInfo << '\n';
    }

    if ( run_lumi_eventSelector && !(*run_lumi_eventSelector)(eventInfo) ) {
      continue;
    }

    if ( run_lumi_eventSelector ) {
      std::cout << "processing Entry " << inputTree->getCurrentMaxEventIdx() << ": " << eventInfo << '\n';
      if ( inputTree -> isOpen() ) {
        std::cout << "input File = " << inputTree->getCurrentFileName() << '\n';
      }
    }

//--- build collections of generator level particles (before any cuts are applied, to check distributions in unbiased event samples)
    std::vector<GenLepton> genLeptons;
    std::vector<GenLepton> genElectrons;
    std::vector<GenLepton> genMuons;
    std::vector<GenHadTau> genHadTaus;
    std::vector<GenPhoton> genPhotons;
    std::vector<GenJet> genJets;
    std::vector<GenParticle> genTaus;
    std::vector<GenParticle> genHiggsBosons;

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
      if(genHadTauReader)     genHadTaus = genHadTauReader->read();
      if(genPhotonReader)     genPhotons = genPhotonReader->read();
      if(genJetReader)        genJets = genJetReader->read();
      if(genTauReader)        genTaus = genTauReader->read();
      if(genHiggsBosonReader) genHiggsBosons = genHiggsBosonReader->read();

      if(genMatchToMuonReader)     muonGenMatch = genMatchToMuonReader->read();
      if(genMatchToElectronReader) electronGenMatch = genMatchToElectronReader->read();
      if(genMatchToHadTauReader)   hadTauGenMatch = genMatchToHadTauReader->read();
      if(genMatchToJetReader)      jetGenMatch = genMatchToJetReader->read();
    }

//--- compute event-level weight
    double evtWeight = 1.;
    if ( isMC ) {
      evtWeight *= lumiScale;
      if ( apply_genWeight ) evtWeight *= boost::math::sign(eventInfo.genWeight);
      evtWeight *= eventInfo.pileupWeight;
      if ( isDEBUG ) {
        std::cout << "lumiScale = " << lumiScale << std::endl;
        if ( apply_genWeight ) std::cout << "genWeight = " << boost::math::sign(eventInfo.genWeight) << std::endl;
        std::cout << "pileupWeight = " << eventInfo.pileupWeight << std::endl;
        std::cout << "evtWeight = " << evtWeight << std::endl;
      }
    }

    genEvtHistManager_beforeCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight);
    
//--- build collections of electrons, muons and hadronic taus;
//    resolve overlaps in order of priority: muon, electron,
    const std::vector<RecoMuon> muons = muonReader->read();
    const std::vector<const RecoMuon*> muon_ptrs = convert_to_ptrs(muons);
    const std::vector<const RecoMuon*> cleanedMuons = muon_ptrs; // CV: no cleaning needed for muons, as they have the highest priority in the overlap removal
    const std::vector<const RecoMuon*> preselMuons = preselMuonSelector(cleanedMuons, isHigherPt);
    const std::vector<const RecoMuon*> fakeableMuons = fakeableMuonSelector(preselMuons, isHigherConePt);
    const std::vector<const RecoMuon*> tightMuons = tightMuonSelector(preselMuons, isHigherPt);
    const std::vector<const RecoMuon*> selMuons = selectObjects(leptonSelection, preselMuons, fakeableMuons, tightMuons);
    if ( isDEBUG ) {
      printCollection("preselMuons", preselMuons);
      printCollection("selMuons", selMuons);
    }

    const std::vector<RecoElectron> electrons = electronReader->read();
    const std::vector<const RecoElectron*> electron_ptrs = convert_to_ptrs(electrons);
    const std::vector<const RecoElectron*> cleanedElectrons = electronCleaner(electron_ptrs, selMuons);
    const std::vector<const RecoElectron*> preselElectrons = preselElectronSelector(cleanedElectrons, isHigherPt);
    const std::vector<const RecoElectron*> fakeableElectrons = fakeableElectronSelector(preselElectrons, isHigherConePt);
    const std::vector<const RecoElectron*> tightElectrons = tightElectronSelector(preselElectrons, isHigherPt);
    const std::vector<const RecoElectron*> selElectrons = selectObjects(leptonSelection, preselElectrons, fakeableElectrons, tightElectrons);
    if ( isDEBUG ) {
      printCollection("preselElectrons", preselElectrons);
      printCollection("selElectrons", selElectrons);
    }
    const std::vector<const RecoLepton*> selLeptons = mergeLeptonCollections(selElectrons, selMuons, isHigherConePt);

    const std::vector<RecoHadTau> hadTaus = hadTauReader->read();
    const std::vector<const RecoHadTau*> hadTau_ptrs = convert_to_ptrs(hadTaus);
    const std::vector<const RecoHadTau*> cleanedHadTaus = hadTauCleaner(hadTau_ptrs, preselMuons, preselElectrons);
    const std::vector<const RecoHadTau*> fakeableHadTaus = fakeableHadTauSelector(cleanedHadTaus);
    const std::vector<const RecoHadTau*> tightHadTaus = tightHadTauSelector(cleanedHadTaus);
    const std::vector<const RecoHadTau*> selHadTaus = selectObjects(hadTauSelection, fakeableHadTaus, tightHadTaus);
    if ( isDEBUG ) {
      printCollection("selHadTaus", selHadTaus);
    }

//--- build collections of jets and select subset of jets passing b-tagging criteria
    const std::vector<RecoJet> jets = jetReader->read();
    const std::vector<const RecoJet*> jet_ptrs = convert_to_ptrs(jets);
    if ( isDEBUG ) {
      printCollection("uncleanedJets", jet_ptrs);
    }
    const std::vector<const RecoJet*> cleanedJets = jetCleaningByIndex ?
      jetCleanerByIndex(jet_ptrs, fakeableElectrons, fakeableMuons, fakeableHadTaus) :
      jetCleaner       (jet_ptrs, fakeableElectrons, fakeableMuons, fakeableHadTaus)
    ;
    const std::vector<const RecoJet*> selJets = jetSelector(cleanedJets);
    const std::vector<const RecoJet*> selBJets_loose = jetSelectorBtagLoose(cleanedJets);
    const std::vector<const RecoJet*> selBJets_medium = jetSelectorBtagMedium(cleanedJets);

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
      if(genHadTauReader)     genHadTaus = genHadTauReader->read();
      if(genPhotonReader)     genPhotons = genPhotonReader->read();
      if(genJetReader)        genJets = genJetReader->read();
      if(genTauReader)        genTaus = genTauReader->read();
      if(genHiggsBosonReader) genHiggsBosons = genHiggsBosonReader->read();

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

    RecoMEt met = metReader->read();
    std::vector<const RecoLepton*> fakeableLeptons = mergeLeptonCollections(fakeableElectrons, fakeableMuons);
    Particle::LorentzVector mht_p4 = compMHT(fakeableLeptons, selHadTaus, selJets);
    double met_LD = compMEt_LD(met.p4(), mht_p4);

    if ( !((selLeptons.size() + selHadTaus.size()) >= 4) ) continue;

    double minPt_lead = 25.;
    double minPt_sublead = 15.;
    if ( selLeptons.size() >= 1 ) {
      const RecoLepton* selLepton_lead = selLeptons[0];
      if ( !(selLepton_lead->pt() > minPt_lead) ) continue;
    }
    if ( selLeptons.size() >= 2 ) {
      const RecoLepton* selLepton_sublead = selLeptons[1];
      if ( !(selLepton_sublead->pt() > minPt_sublead) ) continue;
    }

    int idxCategory = get_idxCategory(selLeptons.size(), selHadTaus.size());
    selHistManagerType* selHistManager = selHistManagers[idxCategory];
    assert(selHistManager != 0);
    selHistManager->electrons_->fillHistograms(selElectrons, evtWeight);
    selHistManager->leadElectron_->fillHistograms(selElectrons, evtWeight);
    selHistManager->subleadElectron_->fillHistograms(selElectrons, evtWeight);
    selHistManager->muons_->fillHistograms(selMuons, evtWeight);
    selHistManager->leadMuon_->fillHistograms(selMuons, evtWeight);
    selHistManager->subleadMuon_->fillHistograms(selMuons, evtWeight);
    selHistManager->hadTaus_->fillHistograms(selHadTaus, evtWeight);
    selHistManager->leadHadTau_->fillHistograms(selHadTaus, evtWeight);
    selHistManager->subleadHadTau_->fillHistograms(selHadTaus, evtWeight);
    selHistManager->jets_->fillHistograms(selJets, evtWeight);
    selHistManager->leadJet_->fillHistograms(selJets, evtWeight);
    selHistManager->subleadJet_->fillHistograms(selJets, evtWeight);
    selHistManager->BJets_loose_->fillHistograms(selBJets_loose, evtWeight);
    selHistManager->BJets_medium_->fillHistograms(selBJets_medium, evtWeight);
    selHistManager->met_->fillHistograms(met, mht_p4, met_LD, evtWeight);        
    selHistManager->weights_->fillHistograms("genWeight", eventInfo.genWeight);
    selHistManager->weights_->fillHistograms("pileupWeight", eventInfo.pileupWeight);

    std::vector<const ChargedParticle*> measuredTaus;
    std::vector<const RecoLepton*> selLeptons_toAdd = pickFirstNobjects(selLeptons, 4);
    measuredTaus.insert(measuredTaus.end(), selLeptons_toAdd.begin(), selLeptons_toAdd.end());
    if ( selLeptons_toAdd.size() < 4 ) {
      std::vector<const RecoHadTau*> selHadTaus_toAdd = pickFirstNobjects(selHadTaus, 4 - selLeptons_toAdd.size());
      measuredTaus.insert(measuredTaus.end(), selHadTaus_toAdd.begin(), selHadTaus_toAdd.end());
    }    
    if ( measuredTaus.size() >= 4 ) {   
      std::map<double, vSVfit4tauResult_wPtrs> results_wMassConstraint_MarkovChain;  // key = logM_wMassConstraint
      std::map<double, vSVfit4tauResult_wPtrs> results_woMassConstraint_MarkovChain; // key = logM_woMassConstraint
      std::map<double, vSVfit4tauResult_wPtrs> results_wMassConstraint_VAMP;         // key = logM_wMassConstraint
      for ( std::vector<const ChargedParticle*>::const_iterator measuredTau1 = measuredTaus.begin();
            measuredTau1 != measuredTaus.end(); ++measuredTau1 ) {
        for ( std::vector<const ChargedParticle*>::const_iterator measuredTau2 = measuredTau1 + 1;
              measuredTau2 != measuredTaus.end(); ++measuredTau2 ) {
          // require decay products of 1st Higgs boson to have opposite charge
          if ( ((*measuredTau1)->charge() + (*measuredTau2)->charge()) != 0 ) continue;
          for ( std::vector<const ChargedParticle*>::const_iterator measuredTau3 = measuredTaus.begin();
                measuredTau3 != measuredTaus.end(); ++measuredTau3 ) {
            for ( std::vector<const ChargedParticle*>::const_iterator measuredTau4 = measuredTau3 + 1;
                  measuredTau4 != measuredTaus.end(); ++measuredTau4 ) {
              // require decay products of 2nd Higgs boson to have opposite charge
              if ( ((*measuredTau3)->charge() + (*measuredTau4)->charge()) != 0 ) continue;

              // require that all taus are different
              if ( (*measuredTau3) == (*measuredTau1) || (*measuredTau3) == (*measuredTau2) ) continue;
              if ( (*measuredTau4) == (*measuredTau1) || (*measuredTau4) == (*measuredTau2) ) continue;

              // require charge of all decay products to sum to zero
              if ( ((*measuredTau1)->charge() + (*measuredTau2)->charge() + (*measuredTau3)->charge() + (*measuredTau4)->charge()) != 0 ) continue;

              // require that tau1 has higher pT than tau3,
              // in order prevent that SVfit mass is computed for both combinations (tau1,..,tau3,..) and (tau3,..,tau1,..)
              if ( !((*measuredTau1)->pt() > (*measuredTau3)->pt()) ) continue;
      
              // match reconstructed tau decay products to generator-level ones
              const GenParticle* genTau1 = findGenTau(**measuredTau1, genTaus);
              const GenParticle* genTau2 = findGenTau(**measuredTau2, genTaus);
              const GenParticle* genTau3 = findGenTau(**measuredTau3, genTaus);
              const GenParticle* genTau4 = findGenTau(**measuredTau4, genTaus);

              // require that no generator-level tau decay product is matched twice
              if ( genTau2 == genTau1 || genTau3 == genTau1 || genTau4 == genTau1 ||
                   genTau3 == genTau2 || genTau4 == genTau2 || genTau4 == genTau3 ) continue;
      
              // require that no generator-level tau decay product is unmatched
              if ( !(genTau1 && genTau2 && genTau3 && genTau4) ) continue;

              //std::cout << "measuredTau1: pT = " << (*measuredTau1)->pt() << ", eta = " << (*measuredTau1)->eta() << ", phi = " << (*measuredTau1)->phi() << std::endl;
              //std::cout << "genTau1: pT = " << genTau1->pt() << ", eta = " << genTau1->eta() << ", phi = " << genTau1->phi() << std::endl;
              //std::cout << "measuredTau2: pT = " << (*measuredTau2)->pt() << ", eta = " << (*measuredTau2)->eta() << ", phi = " << (*measuredTau2)->phi() << std::endl;
              //std::cout << "genTau2: pT = " << genTau2->pt() << ", eta = " << genTau2->eta() << ", phi = " << genTau2->phi() << std::endl;
              //std::cout << "measuredTau3: pT = " << (*measuredTau3)->pt() << ", eta = " << (*measuredTau3)->eta() << ", phi = " << (*measuredTau3)->phi() << std::endl;
              //std::cout << "genTau3: pT = " << genTau3->pt() << ", eta = " << genTau3->eta() << ", phi = " << genTau3->phi() << std::endl;
              //std::cout << "measuredTau4: pT = " << (*measuredTau4)->pt() << ", eta = " << (*measuredTau4)->eta() << ", phi = " << (*measuredTau4)->phi() << std::endl;
              //std::cout << "genTau4: pT = " << genTau4->pt() << ", eta = " << genTau4->eta() << ", phi = " << genTau4->phi() << std::endl;

              const GenParticle* genHiggs1 = nullptr;
              const GenParticle* genHiggs2 = nullptr;
              bool isCorrectAssoc = false;
              if ( (genTau1->charge() + genTau2->charge()) == 0 &&
                   (genTau3->charge() + genTau4->charge()) == 0 ) {
                genHiggs1 = findGenHiggs(genTau1->p4() + genTau2->p4(), genHiggsBosons);
                genHiggs2 = findGenHiggs(genTau3->p4() + genTau4->p4(), genHiggsBosons);
                //if ( genHiggs1 && genHiggs2 ) {
                //  std::cout << "genHiggs1: pT = " << genHiggs1->pt() << ", eta = " << genHiggs1->eta() << ", phi = " << genHiggs1->phi() << " (matches genTau1+genTau2)" << std::endl;
                //  std::cout << "genHiggs2: pT = " << genHiggs2->pt() << ", eta = " << genHiggs2->eta() << ", phi = " << genHiggs2->phi() << " (matches genTau3+genTau4)" << std::endl;
                //}
                if ( genHiggs1 && genHiggs2 ) {
                  isCorrectAssoc = true;
                }
                if ( !(genHiggs1 && genHiggs2) ) {
                  genHiggs1 = findGenHiggs(genTau1->p4() + genTau3->p4(), genHiggsBosons);
                  genHiggs2 = findGenHiggs(genTau2->p4() + genTau4->p4(), genHiggsBosons);
                  //if ( genHiggs1 && genHiggs2 ) {
                  //  std::cout << "genHiggs1: pT = " << genHiggs1->pt() << ", eta = " << genHiggs1->eta() << ", phi = " << genHiggs1->phi() << " (matches genTau1+genTau3)" << std::endl;
                  //  std::cout << "genHiggs2: pT = " << genHiggs2->pt() << ", eta = " << genHiggs2->eta() << ", phi = " << genHiggs2->phi() << " (matches genTau2+genTau4)" << std::endl;
                  //}
                }
                if ( !(genHiggs1 && genHiggs2) ) {
                  genHiggs1 = findGenHiggs(genTau1->p4() + genTau4->p4(), genHiggsBosons);
                  genHiggs2 = findGenHiggs(genTau2->p4() + genTau3->p4(), genHiggsBosons);
                  //if ( genHiggs1 && genHiggs2 ) {
                  //  std::cout << "genHiggs1: pT = " << genHiggs1->pt() << ", eta = " << genHiggs1->eta() << ", phi = " << genHiggs1->phi() << " (matches genTau1+genTau4)" << std::endl;
                  //  std::cout << "genHiggs2: pT = " << genHiggs2->pt() << ", eta = " << genHiggs2->eta() << ", phi = " << genHiggs2->phi() << " (matches genTau2+genTau3)" << std::endl;
                  //}
                }
              }
              if ( !(genHiggs1 && genHiggs2) ) continue;
              //std::cout << "isCorrectAssoc = " << isCorrectAssoc << std::endl;
              Particle::LorentzVector genDiTau1P4 = genHiggs1->p4();
              Particle::LorentzVector genDiTau2P4 = genHiggs2->p4();

              Particle::LorentzVector genDiHiggsP4 = genDiTau1P4 + genDiTau2P4;

              const GenParticle* measuredTau1_gen = getGenMeasuredTau(**measuredTau1);
              const GenParticle* measuredTau2_gen = getGenMeasuredTau(**measuredTau2);
              const GenParticle* measuredTau3_gen = getGenMeasuredTau(**measuredTau3);
              const GenParticle* measuredTau4_gen = getGenMeasuredTau(**measuredTau4);

              bool isGenMatched = (measuredTau1_gen && measuredTau2_gen && measuredTau3_gen && measuredTau4_gen);
              if ( !isGenMatched ) continue;

              Particle::LorentzVector measuredTau1P4_gen = measuredTau1_gen->p4();
              Particle::LorentzVector measuredTau2P4_gen = measuredTau2_gen->p4();
              Particle::LorentzVector measuredTau3P4_gen = measuredTau3_gen->p4();
              Particle::LorentzVector measuredTau4P4_gen = measuredTau4_gen->p4();

              double metPx_gen =
                  (genTau1->p4().px() - measuredTau1P4_gen.px())
               + (genTau2->p4().px() - measuredTau2P4_gen.px()) 
               + (genTau3->p4().px() - measuredTau3P4_gen.px()) 
               + (genTau4->p4().px() - measuredTau4P4_gen.px());
              double metPy_gen =
                 (genTau1->p4().py() - measuredTau1P4_gen.py()) 
               + (genTau2->p4().py() - measuredTau2P4_gen.py()) 
               + (genTau3->p4().py() - measuredTau3P4_gen.py()) 
               + (genTau4->p4().py() - measuredTau4P4_gen.py());

              Particle::LorentzVector measuredTau1P4_rec;
              int measuredTau1Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
              int measuredHadTau1DecayMode = -1;
              Particle::LorentzVector measuredTau2P4_rec;
              int measuredTau2Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
              int measuredHadTau2DecayMode = -1;
              Particle::LorentzVector measuredTau3P4_rec;
              int measuredTau3Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
              int measuredHadTau3DecayMode = -1;
              Particle::LorentzVector measuredTau4P4_rec;
              int measuredTau4Type_rec = classic_svFit::MeasuredTauLepton::kUndefinedDecayType;
              int measuredHadTau4DecayMode = -1;
              double metPx_rec, metPy_rec;
              TMatrixD metCov(2,2);
              if ( mode == kMode_rec ) {
                measuredTau1P4_rec = (*measuredTau1)->p4();
                measuredTau1Type_rec = getMeasuredTauLeptonType(**measuredTau1);
                if ( measuredTau1Type_rec == classic_svFit::MeasuredTauLepton::kTauToHadDecay ) measuredHadTau1DecayMode = getHadTauDecayMode(**measuredTau1);
                measuredTau2P4_rec = (*measuredTau2)->p4();
                measuredTau2Type_rec = getMeasuredTauLeptonType(**measuredTau2);
                if ( measuredTau2Type_rec == classic_svFit::MeasuredTauLepton::kTauToHadDecay ) measuredHadTau2DecayMode = getHadTauDecayMode(**measuredTau2);
                measuredTau3P4_rec = (*measuredTau3)->p4();
                measuredTau3Type_rec = getMeasuredTauLeptonType(**measuredTau3);
                if ( measuredTau3Type_rec == classic_svFit::MeasuredTauLepton::kTauToHadDecay ) measuredHadTau3DecayMode = getHadTauDecayMode(**measuredTau3);
                measuredTau4P4_rec = (*measuredTau4)->p4();
                measuredTau4Type_rec = getMeasuredTauLeptonType(**measuredTau4);
                if ( measuredTau4Type_rec == classic_svFit::MeasuredTauLepton::kTauToHadDecay ) measuredHadTau4DecayMode = getHadTauDecayMode(**measuredTau4);
                metPx_rec = met.pt()*TMath::Cos(met.phi());
                metPy_rec = met.pt()*TMath::Sin(met.phi());
                metCov[0][0] = met.covXX();
                metCov[1][0] = met.covXY();
                metCov[0][1] = met.covXY();
                metCov[1][1] = met.covYY();
              } else if ( mode == kMode_gen || mode == kMode_genSmeared ) {
                assert(isGenMatched);
                if ( mode == kMode_gen ) {
                  measuredTau1P4_rec = measuredTau1P4_gen;
                  measuredTau2P4_rec = measuredTau2P4_gen;
                  measuredTau3P4_rec = measuredTau3P4_gen;
                  measuredTau4P4_rec = measuredTau4P4_gen;
                  metPx_rec = metPx_gen;
                  metPy_rec = metPy_gen;
                } else if ( mode == kMode_genSmeared ) {
                  measuredTau1P4_rec = ( isGenHadTau(*measuredTau1_gen) ) ? genHadTauSmearer(measuredTau1P4_gen) : measuredTau1P4_gen;
                  measuredTau2P4_rec = ( isGenHadTau(*measuredTau2_gen) ) ? genHadTauSmearer(measuredTau2P4_gen) : measuredTau2P4_gen;
                  measuredTau3P4_rec = ( isGenHadTau(*measuredTau3_gen) ) ? genHadTauSmearer(measuredTau3P4_gen) : measuredTau3P4_gen;
                  measuredTau4P4_rec = ( isGenHadTau(*measuredTau4_gen) ) ? genHadTauSmearer(measuredTau4P4_gen) : measuredTau4P4_gen;
                  std::pair<double, double> metPxPy_rec = genMEtSmearer(metPx_gen, metPy_gen);
                  metPx_rec = metPxPy_rec.first;
                  metPy_rec = metPxPy_rec.second;
                } else assert(0);
                measuredTau1Type_rec = getMeasuredTauLeptonType(*measuredTau1_gen);
                if ( isGenHadTau(*measuredTau1_gen) ) measuredHadTau1DecayMode = getHadTauDecayMode(*measuredTau1_gen);
                measuredTau2Type_rec = getMeasuredTauLeptonType(*measuredTau2_gen);
                if ( isGenHadTau(*measuredTau2_gen) ) measuredHadTau2DecayMode = getHadTauDecayMode(*measuredTau2_gen);
                measuredTau3Type_rec = getMeasuredTauLeptonType(*measuredTau3_gen);
                if ( isGenHadTau(*measuredTau3_gen) ) measuredHadTau3DecayMode = getHadTauDecayMode(*measuredTau3_gen);
                measuredTau4Type_rec = getMeasuredTauLeptonType(*measuredTau4_gen);
                if ( isGenHadTau(*measuredTau4_gen) ) measuredHadTau4DecayMode = getHadTauDecayMode(*measuredTau4_gen);
                metCov[0][0] = square(sigmaX);
                metCov[1][0] = 0.;
                metCov[0][1] = 0.;
                metCov[1][1] = square(sigmaY);
              } else assert(0);

              //-------------------------------------------------------------------------------------
              // CV: run ClassicSVfit4tau algorithm
              for ( vdouble::const_iterator logM = logM_wMassConstraint_MarkovChain.begin();
                    logM != logM_wMassConstraint_MarkovChain.end(); ++logM ) {
                if ( isDEBUG ) {
                  if ( (*logM) > 0. ) {
                    std::cout << "running SVfit4tau algorithm with Markov-Chain integration, with mH=125 GeV mass constraint and with logM = " << (*logM) << "..." << std::endl;
                  } else {
                    std::cout << "running SVfit4tau algorithm with Markov-Chain integration, with mH=125 GeV mass constraint and without logM term..." << std::endl;
                  }
                }
                SVfit4tauResult_wPtrs result(compSVfit4tau(
                  measuredTau1P4_rec, measuredTau1Type_rec, measuredHadTau1DecayMode,
                  measuredTau2P4_rec, measuredTau2Type_rec, measuredHadTau2DecayMode,
                  measuredTau3P4_rec, measuredTau3Type_rec, measuredHadTau3DecayMode,
                  measuredTau4P4_rec, measuredTau4Type_rec, measuredHadTau4DecayMode,
                  metPx_rec, metPy_rec, metCov,
                  125., *logM, ClassicSVfit4tau::kAlgoMarkovChain, isDEBUG ? 1 : 0
                ));
                result.measuredTau1Higgs1P4_ = measuredTau1P4_rec;
                result.measuredTau2Higgs1P4_ = measuredTau2P4_rec;
                result.measuredTau1Higgs2P4_ = measuredTau3P4_rec;
                result.measuredTau2Higgs2P4_ = measuredTau4P4_rec;
                result.genDiHiggsP4_ = genDiHiggsP4;
                result.genDiTau1P4_ = genDiTau1P4;
                result.genDiTau2P4_ = genDiTau2P4;
                result.isCorrectAssoc_ = isCorrectAssoc;
                results_wMassConstraint_MarkovChain[*logM].push_back(result);
              }

              for ( vdouble::const_iterator logM = logM_woMassConstraint_MarkovChain.begin();
                    logM != logM_woMassConstraint_MarkovChain.end(); ++logM ) {
                if ( isDEBUG ) {
                  if ( (*logM) > 0. ) {
                    std::cout << "running SVfit4tau algorithm with Markov-Chain integration, without mass constraint and with logM = " << (*logM) << "..." << std::endl;
                  } else {
                    std::cout << "running SVfit4tau algorithm with Markov-Chain integration, without mass constraint and without logM term..." << std::endl;
                  }
                }
                SVfit4tauResult_wPtrs result(compSVfit4tau(
                  measuredTau1P4_rec, measuredTau1Type_rec, measuredHadTau1DecayMode,
                  measuredTau2P4_rec, measuredTau2Type_rec, measuredHadTau2DecayMode,
                  measuredTau3P4_rec, measuredTau3Type_rec, measuredHadTau3DecayMode,
                  measuredTau4P4_rec, measuredTau4Type_rec, measuredHadTau4DecayMode,
                  metPx_rec, metPy_rec, metCov,
                  -1., *logM, ClassicSVfit4tau::kAlgoMarkovChain, isDEBUG ? 1 : 0
                ));
                result.measuredTau1Higgs1P4_ = measuredTau1P4_rec;
                result.measuredTau2Higgs1P4_ = measuredTau2P4_rec;
                result.measuredTau1Higgs2P4_ = measuredTau3P4_rec;
                result.measuredTau2Higgs2P4_ = measuredTau4P4_rec;
                result.genDiHiggsP4_ = genDiHiggsP4;
                result.genDiTau1P4_ = genDiTau1P4;
                result.genDiTau2P4_ = genDiTau2P4;
                result.isCorrectAssoc_ = isCorrectAssoc;
                results_woMassConstraint_MarkovChain[*logM].push_back(result);
              }

              for ( vdouble::const_iterator logM = logM_wMassConstraint_VAMP.begin();
                    logM != logM_wMassConstraint_VAMP.end(); ++logM ) {
                if ( isDEBUG ) {
                  if ( (*logM) > 0. ) {
                    std::cout << "running SVfit4tau algorithm with VAMP integration, with mH=125 GeV mass constraint and with logM = " << (*logM) << "..." << std::endl;
                  } else {
                    std::cout << "running SVfit4tau algorithm with VAMP integration, with mH=125 GeV mass constraint and without logM term..." << std::endl;
                  }
                }
                SVfit4tauResult_wPtrs result(compSVfit4tau(
                  measuredTau1P4_rec, measuredTau1Type_rec, measuredHadTau1DecayMode,
                  measuredTau2P4_rec, measuredTau2Type_rec, measuredHadTau2DecayMode,
                  measuredTau3P4_rec, measuredTau3Type_rec, measuredHadTau3DecayMode,
                  measuredTau4P4_rec, measuredTau4Type_rec, measuredHadTau4DecayMode,
                  metPx_rec, metPy_rec, metCov,
                  125., *logM, ClassicSVfit4tau::kAlgoVAMP, isDEBUG ? 1 : 0
                ));
                result.measuredTau1Higgs1P4_ = measuredTau1P4_rec;
                result.measuredTau2Higgs1P4_ = measuredTau2P4_rec;
                result.measuredTau1Higgs2P4_ = measuredTau3P4_rec;
                result.measuredTau2Higgs2P4_ = measuredTau4P4_rec;
                result.genDiHiggsP4_ = genDiHiggsP4;
                result.genDiTau1P4_ = genDiTau1P4;
                result.genDiTau2P4_ = genDiTau2P4;
                result.isCorrectAssoc_ = isCorrectAssoc;
                results_wMassConstraint_VAMP[*logM].push_back(result);
              }
              //-------------------------------------------------------------------------------------

              if ( isCorrectAssoc ) {
                SVfit4tauResult_wPtrs* result_MarkovChain;
                if ( results_wMassConstraint_MarkovChain.find(0.) != results_wMassConstraint_MarkovChain.end() ) result_MarkovChain = &results_wMassConstraint_MarkovChain[0.].front();
                else result_MarkovChain = &results_wMassConstraint_MarkovChain.begin()->second.front();
                assert(result_MarkovChain);
                SVfit4tauResult_wPtrs* result_VAMP;
                if ( results_wMassConstraint_VAMP.find(0.) != results_wMassConstraint_VAMP.end() ) result_VAMP = &results_wMassConstraint_VAMP[0.].front();
                else result_VAMP = &results_wMassConstraint_VAMP.begin()->second.front();
                assert(result_VAMP);
                selHistManager->evt_->fillHistograms(
                  *result_MarkovChain, *result_VAMP,
                  &genDiHiggsP4,
                  &genDiTau1P4,
                  &genDiTau2P4,
                  measuredTau1P4_rec, measuredTau1P4_gen, 
                  measuredTau2P4_rec, measuredTau2P4_gen,
                  measuredTau3P4_rec, measuredTau3P4_gen,
                  measuredTau4P4_rec, measuredTau4P4_gen,
                  metPx_rec, metPy_rec, metCov, metPx_gen, metPy_gen,
                  evtWeight);
              }
            }
          }
        }
      }
      for ( vdouble::const_iterator logM = logM_wMassConstraint_MarkovChain.begin();
            logM != logM_wMassConstraint_MarkovChain.end(); ++logM ) {
        vSVfit4tauResult_wPtrs& results = results_wMassConstraint_MarkovChain[*logM];
/*
        //-----------------------------------------------------------------------
        // CV: sort results obtained with Markov-Chain integration by decreasing "disambiguation score" (Lmax) computed with VAMP integration
        if ( results_wMassConstraint_VAMP.find(*logM) != results_wMassConstraint_VAMP.end() ) {;
          std::cout << "sorting Markov-Chain integration results for logM = " << (*logM) << " by decreasing 'disambiguation score' (Lmax) computed with VAMP integration" << std::endl;
          vSVfit4tauResult_wPtrs& results_VAMP = results_wMassConstraint_VAMP[*logM];
          for ( size_t idxResult = 0; idxResult < results.size(); ++idxResult ) {
            SVfit4tauResult_wPtrs& result_MarkovChain = results[idxResult]; // results computed by Markov-Chain and by VAMP integration are "parallel"
            const SVfit4tauResult_wPtrs& result_VAMP = results_VAMP[idxResult];
            if ( result_VAMP.isValidSolution_ ) {
              result_MarkovChain.Lmax_ = result_VAMP.Lmax_;
            }
          }
        }
        //-----------------------------------------------------------------------
 */
        std::sort(results.begin(), results.end(), isHigherLmax);
        for ( size_t idxResult = 0; idxResult < results.size(); ++idxResult ) {
          const SVfit4tauResult_wPtrs& result = results[idxResult];
          //std::cout << "logM = " << (*logM) << " (wMassConstraint), result #" << idxResult << ":"
          //              << " mass = " << result.dihiggs_mass_ << " +/- " << result.dihiggs_massErr_
          //          << " (isValidSolution = " << result.isValidSolution_ << ", probMax = " << result.probMax_ << ", isCorrectAssoc = " << result.isCorrectAssoc_ << ")" << std::endl;
          SVfit4tauHistManager_MarkovChain* histograms_svFit4tau = nullptr;
          SVfit4tauResolutionHistManager_MarkovChain* histograms_svFit4tauResolution = nullptr;
          if ( result.isCorrectAssoc_ ) {
            if ( idxResult == 0 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_chosen_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_chosen_[*logM];
            } else if ( idxResult == 1 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_MarkovChain_correctAssoc_discarded_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_correctAssoc_discarded_[*logM];
            } else assert(0);
          } else {
            if ( idxResult == 0 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM];
            } else if ( idxResult == 1 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM];
            } else assert(0);
          }
          assert(histograms_svFit4tau && histograms_svFit4tauResolution);
          if ( result.isValidSolution_ ) {
            histograms_svFit4tau->fillHistograms(
              { result },
              evtWeight);
            histograms_svFit4tauResolution->fillHistograms(
              { result },
              &result.genDiHiggsP4_,
              &result.genDiTau1P4_,
              &result.genDiTau2P4_,
              evtWeight);
          }
        }
        if ( results.size() >= 2 ) {
          const SVfit4tauResult_wPtrs* result_correctAssoc = nullptr;
          const SVfit4tauResult_wPtrs* result_incorrectAssoc = nullptr;
          for ( vSVfit4tauResult_wPtrs::const_iterator result = results.begin();
                result != results.end(); ++result ) {
            if ( result->isCorrectAssoc_ ) {
              if ( !result_correctAssoc ) result_correctAssoc = &(*result);
            } else {
              if ( !result_incorrectAssoc ) result_incorrectAssoc = &(*result);
            }
          }
          if ( result_correctAssoc && result_incorrectAssoc ) {
            selHistManager->svFit4tauDisambiguation_wMassConstraint_MarkovChain_[*logM]->fillHistograms(
              *result_correctAssoc,
              result_correctAssoc->measuredTau1Higgs1P4_, result_correctAssoc->measuredTau2Higgs1P4_,
              result_correctAssoc->measuredTau1Higgs2P4_, result_correctAssoc->measuredTau2Higgs2P4_,
              *result_incorrectAssoc,
              result_incorrectAssoc->measuredTau1Higgs1P4_, result_incorrectAssoc->measuredTau2Higgs1P4_,
              result_incorrectAssoc->measuredTau1Higgs2P4_, result_incorrectAssoc->measuredTau2Higgs2P4_,
              evtWeight);
          }
        }
      }
      for ( vdouble::const_iterator logM = logM_woMassConstraint_MarkovChain.begin();
            logM != logM_woMassConstraint_MarkovChain.end(); ++logM ) {
        vSVfit4tauResult_wPtrs& results = results_woMassConstraint_MarkovChain[*logM];
        std::sort(results.begin(), results.end(), isHigherLmax);
        for ( size_t idxResult = 0; idxResult < results.size(); ++idxResult ) {
          const SVfit4tauResult_wPtrs& result = results[idxResult];
          //std::cout << "logM = " << (*logM) << " (woMassConstraint), result #" << idxResult << ":"
          //              << " mass = " << result.dihiggs_mass_ << " +/- " << result.dihiggs_massErr_
          //              << " (isValidSolution = " << result.isValidSolution_ << ", Lmax = " << result.Lmax_ << ", isCorrectAssoc = " << result.isCorrectAssoc_ << ")" << std::endl;
          SVfit4tauHistManager_MarkovChain* histograms_svFit4tau = nullptr;
          SVfit4tauResolutionHistManager_MarkovChain* histograms_svFit4tauResolution = nullptr;
          if ( result.isCorrectAssoc_ ) {
            if ( idxResult == 0 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_woMassConstraint_MarkovChain_correctAssoc_chosen_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_chosen_[*logM];
            } else if ( idxResult == 1 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_woMassConstraint_MarkovChain_correctAssoc_discarded_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_correctAssoc_discarded_[*logM];
            } else assert(0);
          } else {
            if ( idxResult == 0 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_chosen_[*logM];
            } else if ( idxResult == 1 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_woMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_woMassConstraint_MarkovChain_incorrectAssoc_discarded_[*logM];
            } else assert(0);
          }
          assert(histograms_svFit4tau && histograms_svFit4tauResolution);
          if ( result.isValidSolution_ ) {
            histograms_svFit4tau->fillHistograms(
              { result },
              evtWeight);
            histograms_svFit4tauResolution->fillHistograms(
              { result },
              &result.genDiHiggsP4_,
              &result.genDiTau1P4_,
              &result.genDiTau2P4_,
              evtWeight);
          }
        }
      }
      for ( vdouble::const_iterator logM = logM_wMassConstraint_VAMP.begin();
            logM != logM_wMassConstraint_VAMP.end(); ++logM ) {
        vSVfit4tauResult_wPtrs& results = results_wMassConstraint_VAMP[*logM];
        std::sort(results.begin(), results.end(), isHigherLmax);
        for ( size_t idxResult = 0; idxResult < results.size(); ++idxResult ) {
          const SVfit4tauResult_wPtrs& result = results[idxResult];
          //std::cout << "logM = " << (*logM) << " (wMassConstraint), result #" << idxResult << ":"
          //              << " mass = " << result.dihiggs_mass_ << " +/- " << result.dihiggs_massErr_
          //          << " (isValidSolution = " << result.isValidSolution_ << ", Lmax = " << result.Lmax_ << ", isCorrectAssoc = " << result.isCorrectAssoc_ << ")" << std::endl;
          SVfit4tauHistManager_VAMP* histograms_svFit4tau = nullptr;
          SVfit4tauResolutionHistManager_VAMP* histograms_svFit4tauResolution = nullptr;
          if ( result.isCorrectAssoc_ ) {
            if ( idxResult == 0 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_chosen_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_chosen_[*logM];
            } else if ( idxResult == 1 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_VAMP_correctAssoc_discarded_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_VAMP_correctAssoc_discarded_[*logM];
            } else assert(0);
          } else {
            if ( idxResult == 0 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_chosen_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_chosen_[*logM];
            } else if ( idxResult == 1 ) {
              histograms_svFit4tau = selHistManager->svFit4tau_wMassConstraint_VAMP_incorrectAssoc_discarded_[*logM];
              histograms_svFit4tauResolution = selHistManager->svFit4tauResolution_wMassConstraint_VAMP_incorrectAssoc_discarded_[*logM];
            } else assert(0);
          }
          assert(histograms_svFit4tau && histograms_svFit4tauResolution);
          if ( result.isValidSolution_ ) {
            histograms_svFit4tau->fillHistograms(
              { result },
              evtWeight);
            histograms_svFit4tauResolution->fillHistograms(
              { result },
              &result.genDiHiggsP4_,
              evtWeight);
          }
        }
        if ( results.size() >= 2 ) {
          const SVfit4tauResult_wPtrs* result_correctAssoc = nullptr;
          const SVfit4tauResult_wPtrs* result_incorrectAssoc = nullptr;
          for ( vSVfit4tauResult_wPtrs::const_iterator result = results.begin();
                result != results.end(); ++result ) {
            if ( result->isCorrectAssoc_ ) {
              if ( !result_correctAssoc ) result_correctAssoc = &(*result);
            } else {
              if ( !result_incorrectAssoc ) result_incorrectAssoc = &(*result);
            }
          }
          if ( result_correctAssoc && result_incorrectAssoc ) {
            selHistManager->svFit4tauDisambiguation_wMassConstraint_VAMP_[*logM]->fillHistograms(
              *result_correctAssoc,
              result_correctAssoc->measuredTau1Higgs1P4_, result_correctAssoc->measuredTau2Higgs1P4_,
              result_correctAssoc->measuredTau1Higgs2P4_, result_correctAssoc->measuredTau2Higgs2P4_,
              *result_incorrectAssoc,
              result_incorrectAssoc->measuredTau1Higgs1P4_, result_incorrectAssoc->measuredTau2Higgs1P4_,
              result_incorrectAssoc->measuredTau1Higgs2P4_, result_incorrectAssoc->measuredTau2Higgs2P4_,
              evtWeight);
          }
        }
      }
    }    

    if ( isMC ) {
      genEvtHistManager_afterCuts->fillHistograms(genElectrons, genMuons, genHadTaus, genPhotons, genJets, evtWeight);
    }
    
    ++selectedEntries;
    selectedEntries_weighted += evtWeight;
    histogram_selectedEntries->Fill(0.);
  }
  
  std::cout << "max num. Entries = " << inputTree->getCumulativeMaxEventCount()
            << " (limited by " << maxEvents << ") processed in "
            << inputTree->getProcessedFileCount() << " file(s) (out of "
            << inputTree->getFileCount() << ")\n"
            << " analyzed = " << analyzedEntries << '\n'
            << " selected = " << selectedEntries << " (weighted = " << selectedEntries_weighted << ")\n\n";

  delete run_lumi_eventSelector;

  delete muonReader;
  delete electronReader;
  delete hadTauReader;
  delete jetReader;
  delete metReader;
  delete genLeptonReader;
  delete genHadTauReader;
  delete genJetReader;
  delete genPhotonReader;
  delete genTauReader;
  delete genHiggsBosonReader;

  delete genEvtHistManager_beforeCuts;
  delete genEvtHistManager_afterCuts;
  delete eventWeightManager;

  delete inputTree;

  clock.Show("analyze_SVfit4tau");

  return EXIT_SUCCESS;
}
