#include <TFile.h>
#include <TString.h>
#include <TH1.h>
#include <TMath.h>
#include <TROOT.h>
#include <TStyle.h>

#include <string>
#include <vector>
#include <map>
#include <iostream>
#include <iomanip>
#include <assert.h>

#include <boost/algorithm/string/replace.hpp>

using namespace std;

// Example call:
// root "dumpEventYields_Stage2_1l_3tau.C(\"hh_1l_3tau\", 2017, \"deepVSjLoose\")"


void eraseSubStr(std::string & mainStr, const std::string & toErase)
{
  // Search for the substring in string
  size_t pos = mainStr.find(toErase);
 
  if (pos != std::string::npos)
    {
      // If found then erase it from string
      mainStr.erase(pos, toErase.length());
    }
}


TH1* loadHistogram(TFile* inputFile, const std::string& histogramName)
{
  TH1* histogram = dynamic_cast<TH1*>(inputFile->Get(histogramName.data()));
  if ( !histogram ) {
    //std::cerr << "Failed to load histogram = " << histogramName << " from file = " << inputFile->GetName() << " !!" << std::endl;
    //assert(0);
    return 0;
  }
  if ( !histogram->GetSumw2N() ) histogram->Sumw2();
  return histogram;
}

double
compIntegral(const TH1 * histogram,
             bool includeUnderflowBin = false,
             bool includeOverflowBin = false)
{
  const int numBins  = histogram->GetNbinsX();
  const int firstBin = includeUnderflowBin ? 0           : 1;
  const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;

  double sumBinContent = 0.;
  for(int iBin = firstBin; iBin <= lastBin; ++iBin)
  {
    sumBinContent += histogram->GetBinContent(iBin);
  }
  return sumBinContent;
}

double 
square(double x)
{
  return x*x;
}

double
compIntegralErr(const TH1 * histogram,
    bool includeUnderflowBin = false,
    bool includeOverflowBin = false)
{
  const int numBins  = histogram->GetNbinsX();
  const int firstBin = includeUnderflowBin ? 0           : 1;
  const int lastBin  = includeOverflowBin  ? numBins + 1 : numBins;

  double sumBinErr2 = 0.;
  for(int iBin = firstBin; iBin <= lastBin; ++iBin)
  {
    sumBinErr2 += square(histogram->GetBinError(iBin));
  }
  return std::sqrt(sumBinErr2);
}

void dumpEventYields_Stage2_1l_3tau(const char* channel, int Era, const char* tauID)
{
  gROOT->SetBatch(true);

  std::cout << "Channel: " << channel << std::endl;
  std::cout << "Era: " << Era << std::endl;
  std::cout << "tauID: " << tauID << std::endl;
  TH1::AddDirectory(false);

  bool showDataYield = false;
  typedef std::vector<std::string> vstring;
  vstring channels;

  channels.push_back(channel);

  double lumi_SF;
  std::string inputFilePath;

  if(Era == 2016) {
    double lumi_datacard_2016 = 35.9;
    double lumi_projection_2016 = 35.9;
    lumi_SF = lumi_projection_2016/lumi_datacard_2016;
    std::cout << "scaling (Era: "<< Era  << ")  signal and background yields to L=" << lumi_projection_2016 << "fb^-1 @ 13 TeV." << std::endl;
  }

  if(Era == 2017) {
    double lumi_datacard_2017 = 41.5;
    double lumi_projection_2017 = 41.5;
    lumi_SF = lumi_projection_2017/lumi_datacard_2017;
    std::cout << "scaling (Era: "<< Era  << ")  signal and background yields to L=" << lumi_projection_2017 << "fb^-1 @ 13 TeV." << std::endl;
  }


  if(Era == 2018) {
    double lumi_datacard_2018 = 59.7;
    double lumi_projection_2018 = 59.7;
    lumi_SF = lumi_projection_2018/lumi_datacard_2018;
    std::cout << "scaling (Era: "<< Era  << ")  signal and background yields to L=" << lumi_projection_2018 << "fb^-1 @ 13 TeV." << std::endl;
  }


  // 1l_3tau file path

  if(Era == 2016) {
    if (strcmp(tauID, "deepVSjLoose") == 0){
      inputFilePath = "/hdfs/local/veelken/hhAnalysis/2016/2020Sep29_deepVsjLoose/histograms/hh_1l_3tau/";
    }
    if (strcmp(tauID, "deepVSjMedium") == 0){
      inputFilePath = "/hdfs/local/veelken/hhAnalysis/2016/2020Oct02_deepVsjMedium/histograms/hh_1l_3tau/";
    }
  }

  if(Era == 2017) {
    if (strcmp(tauID, "deepVSjLoose") == 0){
      inputFilePath = "/hdfs/local/veelken/hhAnalysis/2017/2020Sep29_deepVsjLoose/histograms/hh_1l_3tau/";
    }
    if (strcmp(tauID, "deepVSjMedium") == 0){
      inputFilePath = "/hdfs/local/veelken/hhAnalysis/2017/2020Oct02_deepVsjMedium/histograms/hh_1l_3tau/";
    }
  }

  if(Era == 2018) {
    if (strcmp(tauID, "deepVSjLoose") == 0){
      inputFilePath = "/hdfs/local/veelken/hhAnalysis/2018/2020Sep29_deepVsjLoose/histograms/hh_1l_3tau/";
    }
    if (strcmp(tauID, "deepVSjMedium") == 0){
      inputFilePath = "/hdfs/local/veelken/hhAnalysis/2018/2020Oct02_deepVsjMedium/histograms/hh_1l_3tau/";
    }
  }

  // SS file paths 
  // std::string inputFilePath = "/hdfs/local/acwarden/hhAnalysis/2017/2020June22_SS_L/histograms/hh_1l_3tau/";
  std::string strEra = std::to_string(Era);


  std::map<std::string, std::string> inputFileNames; // key = channel
  inputFileNames["hh_1l_3tau"] = "Tight_OS/hadd/hadd_stage2_Tight_OS.root";
  // inputFileNames["hh_1l_3tau"] = "Tight_SS/hadd/hadd_stage2_Tight_SS.root";
  // inputFileNames["hh_1e_3tau"] = "Fakeable_wFakeRateWeights_OS/hadd/hadd_stage2_Fakeable_wFakeRateWeights_OS.root";
  // inputFileNames["hh_1mu_3tau"] = "Fakeable_wFakeRateWeights_OS/hadd/hadd_stage2_Fakeable_wFakeRateWeights_OS.root";
  // inputFileNames["hh_1e_3tau"] = "Tight_OS/hadd/hadd_stage2_Tight_OS.root";
  // inputFileNames["hh_1mu_3tau"] = "Tight_OS/hadd/hadd_stage2_Tight_OS.root";
  
  std::map<std::string, std::string> directories; // key = channel
  // directories["hh_1e_3tau"] = "hh_1e_3tau_OS_Fakeable_wFakeRateWeights/sel/evt";
  // directories["hh_1mu_3tau"] = "hh_1mu_3tau_OS_Fakeable_wFakeRateWeights/sel/evt";
  directories["hh_1l_3tau"] = "hh_1l_3tau_OS_Tight/sel/evt";
  // directories["hh_1l_3tau"] = "hh_1l_3tau_SS_Tight/sel/evt";
  // directories["hh_1e_3tau"] = "hh_1e_3tau_OS_Tight/sel/evt";
  // directories["hh_1mu_3tau"] = "hh_1mu_3tau_OS_Tight/sel/evt";
  
  std::map<std::string, vstring> signal_processes; // key = channel

  if(strcmp(channel, "hh_1l_3tau") == 0){
    signal_processes["hh_1l_3tau"].push_back("signal_ggf_spin0_400_hh_tttt");
    signal_processes["hh_1l_3tau"].push_back("signal_ggf_spin0_400_hh_wwtt");
    signal_processes["hh_1l_3tau"].push_back("signal_ggf_spin0_400_hh_wwww");
    signal_processes["hh_1l_3tau"].push_back("signal_spin0_400_hh");
    signal_processes["hh_1l_3tau"].push_back("signal_ggf_nonresonant_hh_wwww");
    signal_processes["hh_1l_3tau"].push_back("signal_ggf_nonresonant_hh_wwtt");
    signal_processes["hh_1l_3tau"].push_back("signal_ggf_nonresonant_hh_tttt");
  }

  if(strcmp(channel, "hh_1e_3tau") == 0){
    signal_processes["hh_1e_3tau"].push_back("signal_ggf_spin0_400_hh_tttt");
    signal_processes["hh_1e_3tau"].push_back("signal_ggf_spin0_400_hh_wwtt");
    signal_processes["hh_1e_3tau"].push_back("signal_ggf_spin0_400_hh_wwww");
    signal_processes["hh_1e_3tau"].push_back("signal_spin0_400_hh");
    signal_processes["hh_1e_3tau"].push_back("signal_ggf_nonresonant_hh_wwww");
    signal_processes["hh_1e_3tau"].push_back("signal_ggf_nonresonant_hh_wwtt");
    signal_processes["hh_1e_3tau"].push_back("signal_ggf_nonresonant_hh_tttt");
  }

  if(strcmp(channel, "hh_1mu_3tau") == 0){
    signal_processes["hh_1mu_3tau"].push_back("signal_ggf_spin0_400_hh_tttt");
    signal_processes["hh_1mu_3tau"].push_back("signal_ggf_spin0_400_hh_wwtt");
    signal_processes["hh_1mu_3tau"].push_back("signal_ggf_spin0_400_hh_wwww");
    signal_processes["hh_1mu_3tau"].push_back("signal_spin0_400_hh");
    signal_processes["hh_1mu_3tau"].push_back("signal_ggf_nonresonant_hh_wwww");
    signal_processes["hh_1mu_3tau"].push_back("signal_ggf_nonresonant_hh_wwtt");
    signal_processes["hh_1mu_3tau"].push_back("signal_ggf_nonresonant_hh_tttt");
  }


  std::vector<std::string> signal_process_parts;
  signal_process_parts.push_back("");
  signal_process_parts.push_back("_Convs");
  signal_process_parts.push_back("_fake");

  std::map<std::string, vstring> background_processes; // key = channel

  if(strcmp(channel, "hh_1l_3tau") == 0){
    background_processes["hh_1l_3tau"].push_back("VH");
    background_processes["hh_1l_3tau"].push_back("TT");
    background_processes["hh_1l_3tau"].push_back("ZZ");
    background_processes["hh_1l_3tau"].push_back("WZ");
    background_processes["hh_1l_3tau"].push_back("WW");
    background_processes["hh_1l_3tau"].push_back("DY");
    background_processes["hh_1l_3tau"].push_back("W");
    background_processes["hh_1l_3tau"].push_back("TTWW");
    background_processes["hh_1l_3tau"].push_back("TTW");
    background_processes["hh_1l_3tau"].push_back("TTZ");
    background_processes["hh_1l_3tau"].push_back("TTH");
    background_processes["hh_1l_3tau"].push_back("TH");
    background_processes["hh_1l_3tau"].push_back("qqH");
    background_processes["hh_1l_3tau"].push_back("ggH");
    background_processes["hh_1l_3tau"].push_back("XGamma");
    background_processes["hh_1l_3tau"].push_back("Other");
    background_processes["hh_1l_3tau"].push_back("Convs");
    background_processes["hh_1l_3tau"].push_back("fakes_mc");
    background_processes["hh_1l_3tau"].push_back("data_fakes");
    background_processes["hh_1l_3tau"].push_back("flips_mc");
    if(showDataYield){
      background_processes["hh_1l_3tau"].push_back("data_obs");
    }
  }

  if(strcmp(channel, "hh_1e_3tau") == 0){
    background_processes["hh_1e_3tau"].push_back("VH");
    background_processes["hh_1e_3tau"].push_back("TT");
    background_processes["hh_1e_3tau"].push_back("ZZ");
    background_processes["hh_1e_3tau"].push_back("WZ");
    background_processes["hh_1e_3tau"].push_back("WW");
    background_processes["hh_1e_3tau"].push_back("DY");
    background_processes["hh_1e_3tau"].push_back("W");
    background_processes["hh_1e_3tau"].push_back("TTWW");
    background_processes["hh_1e_3tau"].push_back("TTW");
    background_processes["hh_1e_3tau"].push_back("TTZ");
    background_processes["hh_1e_3tau"].push_back("TTH");
    background_processes["hh_1e_3tau"].push_back("TH");
    background_processes["hh_1e_3tau"].push_back("qqH");
    background_processes["hh_1e_3tau"].push_back("ggH");
    background_processes["hh_1e_3tau"].push_back("XGamma");
    background_processes["hh_1e_3tau"].push_back("Other");
    background_processes["hh_1e_3tau"].push_back("Convs");
    background_processes["hh_1e_3tau"].push_back("fakes_mc");
    background_processes["hh_1e_3tau"].push_back("data_fakes");
    background_processes["hh_1e_3tau"].push_back("flips_mc");
    if(showDataYield){
      background_processes["hh_1e_3tau"].push_back("data_obs");
    }
  }

  if(strcmp(channel, "hh_1mu_3tau") == 0){
    background_processes["hh_1mu_3tau"].push_back("VH");
    background_processes["hh_1mu_3tau"].push_back("TT");
    background_processes["hh_1mu_3tau"].push_back("ZZ");
    background_processes["hh_1mu_3tau"].push_back("WZ");
    background_processes["hh_1mu_3tau"].push_back("WW");
    background_processes["hh_1mu_3tau"].push_back("DY");
    background_processes["hh_1mu_3tau"].push_back("W");
    background_processes["hh_1mu_3tau"].push_back("TTWW");
    background_processes["hh_1mu_3tau"].push_back("TTW");
    background_processes["hh_1mu_3tau"].push_back("TTZ");
    background_processes["hh_1mu_3tau"].push_back("TTH");
    background_processes["hh_1mu_3tau"].push_back("TH");
    background_processes["hh_1mu_3tau"].push_back("qqH");
    background_processes["hh_1mu_3tau"].push_back("ggH");
    background_processes["hh_1mu_3tau"].push_back("XGamma");
    background_processes["hh_1mu_3tau"].push_back("Other");
    background_processes["hh_1mu_3tau"].push_back("Convs");
    background_processes["hh_1mu_3tau"].push_back("fakes_mc");
    background_processes["hh_1mu_3tau"].push_back("data_fakes");
    background_processes["hh_1mu_3tau"].push_back("flips_mc");
    if(showDataYield){
      background_processes["hh_1mu_3tau"].push_back("data_obs");
    }
  }

  std::vector<std::string> background_process_parts;
  background_process_parts.push_back("");
  background_process_parts.push_back("_Convs");
  background_process_parts.push_back("_fake");

  for ( vstring::const_iterator channel = channels.begin();
        channel != channels.end(); ++channel ) {
    std::cout << "channel = " << (*channel) << std::endl;

    TString inputFileName_full = inputFilePath.data();
    if ( !inputFileName_full.EndsWith("/") ) inputFileName_full.Append("/");
    inputFileName_full.Append(inputFileNames[*channel].data());
    std::cout << "channel = " << inputFileName_full.Data() << std::endl;
    TFile* inputFile = new TFile(inputFileName_full.Data());
    if ( !inputFile ) {
      std::cerr << "Failed to open input file = " << inputFileName_full.Data() << " !!" << std::endl;
      assert(0);

    }
    std::cout<< "\\begin{frame}{ Event Yields: " << tauID << "(" << Era << ")" "} " << std::endl;
    std::cout<< "\\fontsize{7pt}{8}\\selectfont  " << std::endl;
    std::cout << "\\begin{table}[htbp]" << std::endl;
    std::string category_name = directories[*channel];
    eraseSubStr(category_name, "/sel/evt");
    boost::replace_all(category_name, "_", "\\_");
    std::cout << "\\caption{" << category_name << "}" << std::endl;
    std::cout << "\\centering" << std::endl;
    std::cout << "\\resizebox{0.60\\textwidth}{!}{\\begin{tabular}{|l|c|c|c|c|}\\hline " << std::endl;
    std::cout << "Process & Total & Non Fakes & Fakes & Conversions \\\\ \\hline" << std::endl; 
    for ( vstring::const_iterator signal_process = signal_processes[*channel].begin();
          signal_process != signal_processes[*channel].end(); ++signal_process ) {
      std::map<std::string, double> integral_parts;
      std::map<std::string, double> integralErr_parts;
      double integral_sum = 0.;
      double integralErr2_sum = 0.;
      double Unwt_evts = 0.;
      for ( std::vector<std::string>::const_iterator signal_process_part = signal_process_parts.begin();
            signal_process_part != signal_process_parts.end(); ++signal_process_part ) {
        std::string histogramName = Form("%s/%s%s/EventCounter", 
          directories[*channel].data(), signal_process->data(), signal_process_part->data());
        TH1* histogram = loadHistogram(inputFile, histogramName);

        if ( histogram ) {
          Unwt_evts += histogram->GetEntries();
          histogram->Scale(lumi_SF);
          double integral = compIntegral(histogram);
          integral_parts[*signal_process_part] = integral;
          integral_sum += integral;
          double integralErr = compIntegralErr(histogram);
          integralErr_parts[*signal_process_part] = integralErr;
          integralErr2_sum += square(integralErr); 
        }
      }
      /*
      double integralErr_sum = TMath::Sqrt(integralErr2_sum);
      std::cout << (*signal_process) << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
      if ( integral_parts.size() > 1 ) {
        std::cout << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
                  << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
                  << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
      }
      */

      std::string ProcessName = (std::string)(*signal_process);
      boost::replace_all(ProcessName, "_", "\\_");
      std::cout << std::fixed;
      std::cout << std::setprecision(2);
      std::cout << ProcessName << " & " << integral_sum << "(" << Unwt_evts << ")" << " & " << integral_parts[""] << " & " << integral_parts["_fake"] << " & " << integral_parts["_Convs"] << " \\\\ \\hline" << std::endl;
    }

    double data_fakes = 0;
    std::string histogramName_data_fakes = Form("%s/%s/EventCounter",
      directories[*channel].data(), "data_fakes");
    TH1* histogram_data_fakes = loadHistogram(inputFile, histogramName_data_fakes);
    if ( histogram_data_fakes ) {
      histogram_data_fakes->Scale(lumi_SF);
      data_fakes = compIntegral(histogram_data_fakes);
      //std::cout << "Fakes Data : " << data_fakes << " \\\\" << std::endl;
    }

    double Total = 0;
    double Non_Fake = 0;
    double Fake = 0;
    double Conversion = 0;
    for ( vstring::const_iterator background_process = background_processes[*channel].begin();
          background_process != background_processes[*channel].end(); ++background_process ) {
      std::map<std::string, double> integral_parts;
      std::map<std::string, double> integralErr_parts;
      double integral_sum = 0.;
      double integralErr2_sum = 0.;
      double Unwt_evts = 0.;
      for ( std::vector<std::string>::const_iterator background_process_part = background_process_parts.begin();
            background_process_part != background_process_parts.end(); ++background_process_part ) {
        std::string histogramName = Form("%s/%s%s/EventCounter", 
          directories[*channel].data(), background_process->data(), background_process_part->data());
        TH1* histogram = loadHistogram(inputFile, histogramName);
        if ( histogram ) {
          Unwt_evts += histogram->GetEntries();
          histogram->Scale(lumi_SF);
          double integral = compIntegral(histogram);
          integral_parts[*background_process_part] = integral;
          integral_sum += integral;
          double integralErr = compIntegralErr(histogram);
          integralErr_parts[*background_process_part] = integralErr;
          integralErr2_sum += square(integralErr); 
        }
      }
      /*
      double integralErr_sum = TMath::Sqrt(integralErr2_sum);
      std::cout << (*background_process) << ": " << integral_sum << " +/- " << integralErr_sum << std::endl;
      if ( integral_parts.size() > 1 ) {
        std::cout << " (non-fake = " << integral_parts[""] << " +/- " << integralErr_parts[""] << ","
                  << " fake = " << integral_parts["_fake"] << " +/- " << integralErr_parts["_fake"] << ","
                  << " conversion = " << integral_parts["_Convs"] << " +/- " << integralErr_parts["_Convs"] << ")" << std::endl;
      }
      */

      std::string ProcessName = (std::string)(*background_process);

      if( !( (ProcessName == "fakes_mc") || (ProcessName == "Convs") || (ProcessName == "data_fakes") || (ProcessName == "flips_mc") || ( ProcessName == "data_obs")) ){
        boost::replace_all(ProcessName, "_", "\\_");
        std::cout << std::fixed;
        std::cout << std::setprecision(2);
        std::cout << ProcessName << " & " << integral_sum << "(" << Unwt_evts << ")" << " & " << integral_parts[""] << " & " << integral_parts["_fake"] << " & " << integral_parts["_Convs"] << " \\\\ \\hline" << std::endl;
      }else{
        boost::replace_all(ProcessName, "_", "\\_");
        std::cout << std::fixed;
        std::cout << std::setprecision(2);
        std::cout << ProcessName << " & " << integral_sum << " & " << integral_parts[""] << " & " << integral_parts["_fake"] << " & " << integral_parts["_Convs"] << " \\\\ \\hline" << std::endl;

      }

      //std::cout << (*background_process) << " & " << integral_sum << "(" << Unwt_evts << ")" << " & " << integral_parts[""] << " & " << integral_parts["_fake"] << " & " << integral_parts["_Convs"] << " \\\\ " << std::endl;
 
      if(((*background_process) == "fakes_mc") || ((*background_process) == "data_obs")|| ((*background_process) == "data_fakes")){continue;} // Do not add fakes_mc or data to the total bg yield and do not add data_fakes to non_fake mc bg

      Total += integral_sum;
      Non_Fake += integral_parts[""];
      Fake += integral_parts["_fake"];
      Conversion += integral_parts["_Convs"];
    }
    std::cout << "Total Bg (MC only): " << " & " << Total << " & " << Non_Fake << " & " << Fake << " & " << Conversion << " \\\\ " << "\\hline " << std::endl;
    std::cout << "Total Bg (w data\\_fakes): " << " & " << (Total-Fake+data_fakes) << " & " << Non_Fake << " & " << data_fakes << " & " << Conversion << " \\\\ " << "\\hline " << std::endl;
    std::cout << "\\end{tabular}} " << std::endl;
    std::cout << "\\end{table} " << std::endl;
    std::cout << "\\end{frame} " << std::endl;
       


    double Fakes_MC = 0;
    std::string histogramName_fakes_mc = Form("%s/%s/EventCounter",
      directories[*channel].data(), "fakes_mc");
    TH1* histogram_fakes_mc = loadHistogram(inputFile, histogramName_fakes_mc);
    if ( histogram_fakes_mc ) {
      histogram_fakes_mc->Scale(lumi_SF);
      double Fakes_MC = compIntegral(histogram_fakes_mc);
      //      std::cout << "Fakes MC : " << Fakes_MC << std::endl;
    }

    double Convs = 0;
    std::string histogramName_Convs = Form("%s/%s/EventCounter",
      directories[*channel].data(), "Convs");
    TH1* histogram_Convs = loadHistogram(inputFile, histogramName_Convs);
    if ( histogram_Convs ) {
      histogram_Convs->Scale(lumi_SF);
      Convs = compIntegral(histogram_Convs);
      //      std::cout << "Convs : " << Convs << std::endl;
    }


    double data_flips = 0;
    std::string histogramName_data_flips = Form("%s/%s/EventCounter",
     directories[*channel].data(), "data_flips");
    TH1* histogram_data_flips = loadHistogram(inputFile, histogramName_data_flips);
    if ( histogram_data_flips ) {
      histogram_data_flips->Scale(lumi_SF);
      data_flips = compIntegral(histogram_data_flips);
      std::cout << "Flips Data : " << data_flips << " \\\\" << std::endl;
    }

    double Data_Observed = 0;
    std::string histogramName = Form("%s/%s/EventCounter", 
      directories[*channel].data(), "data_obs");
    TH1* histogram = loadHistogram(inputFile, histogramName);
    if ( histogram ) {
      histogram->Scale(lumi_SF);
      Data_Observed = compIntegral(histogram);
      if(showDataYield){
      std::cout << "Data Observed : " << Data_Observed << " \\\\" << std::endl;
      }
    }

    double Total_Background = Non_Fake + Convs + data_fakes +data_flips ;
    std::cout << "Total Background = Non Fake + Conversion + Fakes Data + Flips Data = " << Total_Background << std::endl;



    delete inputFile;
  }
}
