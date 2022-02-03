from tthAnalysis.HiggsToTauTau.configs.analyzeConfig import *
from hhAnalysis.multilepton.common import is_nonresonant, MASSPOINTS

import re

RR_PRODUCTION_MODE = 'production_mode'
RR_SPIN            = 'spin'
RR_MASS_POINT      = 'mass_point'
RR_DECAY_CHANNEL   = 'decay_channel' #NB! https://github.com/HEP-KBFI/hh-multilepton/issues/21
RESONANT_REGEX_PATTERN = r'signal_(?P<%s>[ggf|vbf]+)_spin(?P<%s>[0|2]{1})_(?P<%s>\d+)_hh_(?P<%s>[0-9A-Za-z]+)' % (
  RR_PRODUCTION_MODE, RR_SPIN, RR_MASS_POINT, RR_DECAY_CHANNEL
)
RESONANT_REGEX = re.compile(RESONANT_REGEX_PATTERN)

def get_signal_per_masspoint(samples):
  io_pairs = {}
  for sample_key, sample_info in samples.items():
    process_cat = sample_info['sample_category']
    if not sample_info['use_it']:
      continue
    resonant_match = RESONANT_REGEX.match(process_cat)
    if not resonant_match:
      continue
    signal_base = '_'.join(['signal', 'spin%s' % resonant_match.group(RR_SPIN), resonant_match.group(RR_MASS_POINT), 'hh'])
    if signal_base not in io_pairs:
      io_pairs[signal_base] = []
    if process_cat not in io_pairs[signal_base]:
      io_pairs[signal_base].append(process_cat)
  return io_pairs

class analyzeConfig_hh(analyzeConfig):

  def __init__(self, **kwargs):
    super(analyzeConfig_hh, self).__init__(**kwargs)
    self.signal_io = get_signal_per_masspoint(self.samples)

    # CV: switch top pT reweighting to new parametrization given on slide 12 of the presentation by Dennis Roy in the Higgs PAG meeting on 12/05/2020:
    #       https://indico.cern.ch/event/904971/contributions/3857701/attachments/2036949/3410728/TopPt_20.05.12.pdf
    self.topPtRwgtChoice = "HighPt"
    self.gen_mHH = MASSPOINTS

  def get_nonfake_backgrounds(self, split_th = True, split_ST = False):
    processes = [ "ggZZ", "qqZZ", "WZ", "WW", "TT", "TTW", "TTWW", "TTZ", "DY", "W", "Other", "ZH", "WH", "TTH", "ggH", "qqH" ]
    if split_th:
      processes.extend([ "tHq", "tHW" ])
    else:
      processes.append("TH")
    if split_ST:
      processes.extend([ "ST" ])
    return processes

  def get_makeplots_backgrounds(self, add_flips = ''):
    result = self.nonfake_backgrounds + [ "data_fakes" ]
    if '0l' not in self.channel:
      result.append("Convs")
    if add_flips:
      if add_flips == 'mc':
        result.append("flips_mc")
      elif add_flips == 'data':
        result.append("data_flips")
      else:
        raise RuntimeError("Invalid option: %s" % add_flips)
    return result

  def get_sample_categories(self):
    return self.nonfake_backgrounds

  def createCfg_makePlots(self, jobOptions):
    """Fills the template of python configuration file for making control plots

       Args:
         histogram_file: name of the input ROOT file
    """
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % jobOptions['inputFile'])
    lines.append("process.makePlots.outputFileName = cms.string('%s')" % jobOptions['outputFile'])
    lines.append("process.makePlots.processesBackground = cms.vstring(%s)" % jobOptions['make_plots_backgrounds'])
    lines.append("process.makePlots.categories = cms.VPSet(")
    lines.append("  cms.PSet(")
    lines.append("    name = cms.string('%s')," % jobOptions['histogramDir'])
    lines.append("    label = cms.string('%s')" % jobOptions['label'])
    lines.append("  )")
    lines.append(")")
    lines.append("process.makePlots.intLumiData = cms.double(%.1f)" % (self.lumi / 1000))
    if 'processSignal' in jobOptions:
      lines.append("process.makePlots.processSignal = cms.string('%s')" %jobOptions['processSignal'])
    create_cfg(self.cfgFile_make_plots, jobOptions['cfgFile_modified'], lines)

  def createCfg_makePlots_mcClosure(self, jobOptions): #TODO
    """Fills the template of python configuration file for making control plots

    Args:
      histogramFile: name of the input ROOT file
    """
    lines = []
    lines.append("process.fwliteInput.fileNames = cms.vstring('%s')" % jobOptions['inputFile'])
    lines.append("process.makePlots.outputFileName = cms.string('%s')" % jobOptions['outputFile'])
    lines.append("process.makePlots.processesBackground = cms.vstring(%s)" % self.make_plots_backgrounds)
    lines.append("process.makePlots.categories = cms.VPSet(")
    lines.append("  cms.PSet(")
    lines.append("    signal = cms.string('%s')," % self.histogramDir_prep_dcard)
    lines.append("    sideband = cms.string('%s')," % self.histogramDir_prep_dcard.replace("Tight", "Fakeable_mcClosure_wFakeRateWeights"))
    lines.append("    label = cms.string('%s')" % self.channel)
    lines.append("  )")
    lines.append(")")
    lines.append("process.makePlots.intLumiData = cms.double(%.1f)" % self.lumi)
    create_cfg(self.cfgFile_make_plots_mcClosure, jobOptions['cfgFile_modified'], lines)
