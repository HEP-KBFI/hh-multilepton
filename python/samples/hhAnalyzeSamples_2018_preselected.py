from tthAnalysis.HiggsToTauTau.samples.tthAnalyzeSamples_2018_preselected_base import samples_2018 as samples_2018_bkg
from hhAnalysis.multilepton.samples.hhAnalyzeSamples_2018_hh import samples_2018 as samples_2018_hh

from hhAnalysis.multilepton.samples.reclassifySamples import reclassifySamples
samples_2018 = reclassifySamples(samples_2018_hh, samples_2018_bkg)
