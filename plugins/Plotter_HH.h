#ifndef tthAnalysis_HiggsToTauTau_Plotter_HH_h
#define tthAnalysis_HiggsToTauTau_Plotter_HH_h

/** \class Plotter_HH
 *
 * Make control plots (prefit and postfit) for all channels of HH->4tau analysis.
 *
 * \author Christian Veelken, Tallinn
 *
 */

#include "tthAnalysis/HiggsToTauTau/interface/Plotter.h"
#include "tthAnalysis/HiggsToTauTau/interface/histogramAuxFunctions.h"
#include "tthAnalysis/HiggsToTauTau/interface/plottingAuxFunctions.h"

#include <vector>
#include <string>

class Plotter_HH : public Plotter
{
 public:
  // constructor 
  explicit Plotter_HH(const TFile* inputFile, const edm::ParameterSet& cfg);
  
  // destructor
  virtual ~Plotter_HH();

 private:
  virtual void makePlot(double canvasSizeX, double canvasSizeY,
			TH1* histogramData, TH1* histogramData_blinded,
			std::vector<histogramEntryType*>& histogramsBackground, 	
			//TH1* histogramSignal,
			std::vector<histogramEntryType*>& histogramsSignal,
			TH1* histogramUncertainty,
			double legendTextSize, double legendPosX, double legendPosY, double legendSizeX, double legendSizeY, 
			const std::string& labelOnTop,
			std::vector<std::string>& extraLabels, double labelTextSize,
			double labelPosX, double labelPosY, double labelSizeX, double labelSizeY,
			double xMin, double xMax, const std::string& xAxisTitle, double xAxisOffset,
			bool useLogScale, double yMin, double yMax, const std::string& yAxisTitle, double yAxisOffset,
			const std::string& outputFileName, 
			bool isRebinned, 
			bool divideByBinWidth);

  double scaleSignal_;
  bool sort_;
  std::string legendEntrySignal_;

  std::vector<std::string> legendEntriesSignal_;
  int optionToNormalizeSignalDistributions_;   // 0: don't normalize, 1: normalize w.r.t. area, 2: normalize w.r.t. height
  
};

#endif
