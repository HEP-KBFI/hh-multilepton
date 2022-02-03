from hhAnalysis.multilepton.common import is_nonresonant

import collections
import itertools
import copy
import re

HH_DECAYMODES = [ 'wwww', 'wwtt', 'tttt', 'bbtt', 'bbvv_sl', 'bbvv' ]
HH_DECAYMODES_SUFFIX = [ '_{}'.format(hh_dm) for hh_dm in HH_DECAYMODES ]
HH_DECAYMODES_RE = re.compile('_({}$)'.format('|'.join(HH_DECAYMODES)))

from tthAnalysis.HiggsToTauTau.analysisSettings import systematics

def reclassifySamples(samples_era_hh, samples_era_bkg, samples_era_ttbar = None, separate_th = True):

  samples_era_hh_copy = copy.deepcopy(samples_era_hh)
  samples_era_bkg_copy = copy.deepcopy(samples_era_bkg)
  sum_events_hh  = copy.deepcopy(samples_era_hh_copy['sum_events'])
  sum_events_bkg = copy.deepcopy(samples_era_bkg_copy['sum_events'])
  sum_events_ttbar = []

  del samples_era_hh_copy['sum_events']
  del samples_era_bkg_copy['sum_events']

  if samples_era_ttbar:
    samples_era_ttbar_copy = copy.deepcopy(samples_era_ttbar)
    sum_events_ttbar = copy.deepcopy(samples_era_ttbar_copy['sum_events'])
    del samples_era_ttbar_copy['sum_events']

    samples = collections.OrderedDict(itertools.chain(
      samples_era_bkg_copy.items(), samples_era_hh_copy.items(), samples_era_ttbar_copy.items()
    ))
  else:
    samples = collections.OrderedDict(itertools.chain(samples_era_bkg_copy.items(), samples_era_hh_copy.items()))

  samples['sum_events'] = sum_events_hh + sum_events_bkg + sum_events_ttbar

  from collections import OrderedDict as OD

  duplicate_sfx = 'duplicate'
  duplicate_sfx_caps = '/{}'.format(duplicate_sfx.upper())

  # first we need to find the cross sections that we're going to assign to the duplicated NLO samples
  xsec_nonres = {}
  for sample_name, sample_info in samples.items():

    if not isinstance(sample_info, OD):
      continue

    sample_category = sample_info["sample_category"]
    if is_nonresonant(sample_category) and not sample_name.endswith(duplicate_sfx_caps):
      if sample_category not in xsec_nonres:
        xsec_nonres[sample_category] = sample_info['xsection']
      else:
        assert(xsec_nonres[sample_category] == sample_info['xsection'])

  # duplicate the NLO HH samples
  new_samples = []
  new_sums = {}
  for sample_name, sample_info in samples.items():

    if not isinstance(sample_info, OD):
      continue

    if sample_info["process_name_specific"].startswith('signal') and 'cHHH' in sample_info["sample_category"]:
      # this is to make sure that nexted calls of this function doesn't reduplicate the entries
      assert(not sample_name.endswith(duplicate_sfx_caps))
      sample_name_new = sample_name + duplicate_sfx_caps
      sample_category_split = sample_info["sample_category"].split('_')
      assert(sample_category_split[3].startswith('cHHH'))

      # remove cHHH since this piece of string tells the FW whether or not we want to reweight the samples
      sample_category_split[3] = 'nlo'
      sample_category_new = '_'.join(sample_category_split)
      process_name_new = sample_info["process_name_specific"] + '_{}'.format(duplicate_sfx)

      # normalize the cross section of duplicated samples to 1 pb (in HH production via ggF)
      sample_category_lo = sample_category_new.replace('_nlo', '')
      assert(sample_category_lo in xsec_nonres)
      xsec_new = xsec_nonres[sample_category_lo]

      entry_copy = copy.deepcopy(sample_info)
      entry_copy.update([
        ('sample_category', sample_category_new),
        ('process_name_specific', process_name_new),
        ('xsection', xsec_new),
      ])
      new_samples.append((sample_name_new, entry_copy))

      if sample_category_new not in new_sums:
        new_sums[sample_category_new] = []
      new_sums[sample_category_new].append(process_name_new)

  samples.update(new_samples)
  samples['sum_events'].extend(new_sums.values())

  for sample_name, sample_info in samples.items():

    if not isinstance(sample_info, OD):
      continue

    # do not use the extra 0.4/fb data in 2016
    if sample_name.endswith('/MINIAOD/EXTRA'):
      sample_info["use_it"] = False

    if 'CountWeightedLHEWeightScale' in sample_info["nof_events"] and \
        sample_info["nof_events"]['CountWeightedLHEWeightScale'] == [ 0 ]:
      sample_info["has_LHE"] = False

    if sample_info["process_name_specific"].startswith('signal') and 'hh' in sample_info["process_name_specific"]:
      sample_info["use_it"] = 'vbf_spin' not in sample_info["process_name_specific"]
      sample_info["sample_category_hh"] = copy.deepcopy(sample_info["sample_category"])
      if 'dipoleRecoilOn' not in sample_info["sample_category"]:
        assert(sample_info["sample_category"].endswith(tuple(HH_DECAYMODES_SUFFIX)))
      sample_info["sample_category"] = HH_DECAYMODES_RE.sub("", sample_info["sample_category_hh"])
      assert(sample_info["sample_category"] != sample_info["sample_category_hh"])

    if sample_info["sample_category"] == "Rares":
      sample_info["sample_category"] = "Other"
    elif sample_name.startswith('/ZZTo'):
      sample_info["sample_category"] = "qqZZ"
    elif sample_name.startswith('/GluGluToContinToZZTo'):
      sample_info["sample_category"] = "ggZZ"
    elif sample_name.startswith('/WZTo'):
      sample_info["sample_category"] = "WZ"
    elif sample_name.startswith('/WWTo'):
      sample_info["sample_category"] = "WW"
    elif sample_name.startswith('/DY'):
      sample_info["sample_category"] = "DY"
    elif sample_name.startswith('/W') and sample_name.find('JetsToLNu') != -1 and sample_name.find('JetsToLNu') < 10:
      sample_info["sample_category"] = "W"
    elif sample_name.startswith('/ttH'):
      sample_info["sample_category"] = "TTH"
    elif sample_info["sample_category"] in [ "tHq", "tHW" ]:
      if not separate_th:
        sample_info["sample_category"] = "TH"
    elif sample_name.startswith('/TTTo'):
      if sample_info["sample_category"].replace("TT_", "") not in systematics.ttbar:
        sample_info["sample_category"] = "TT"
      sample_info["use_it"] = True
    elif sample_name.startswith('/TTJets'):
      sample_info["sample_category"] = "TT"
      sample_info["use_it"] = False
    elif sample_name.startswith(('/TTZTo', '/ttZJets')):
      sample_info["sample_category"] = "TTZ"
    elif sample_name.startswith('/TTWW'):
      sample_info["sample_category"] = "TTWW"
    elif sample_name.startswith(('/TTWJets', '/ttWJets')):
      sample_info["sample_category"] = "TTW"
    elif sample_name.startswith(("/TTZH", "/TTWH")):
      sample_info["use_it"] = True

    # disable Tau PD by default -- to avoid double-counting the data events in all analysis channels but 0l+4tau and 1l+3tau
    # where the PD is the only one enabled
    elif sample_name.startswith('/Tau/'):
      sample_info["use_it"] = False

    if samples_era_ttbar and sample_name in samples_era_ttbar:
      sample_info["use_it"] = False

    if sample_name.startswith(('/TGJets', '/TTGJets', '/WGTo', '/ZGTo')):
      sample_info["sample_category"] = "XGamma"

    if sample_info["sample_category"] == "VH":
      if sample_name.startswith(("/WH", "/WplusH", "/WminusH")):
        sample_info["sample_category"] = "WH"
      elif sample_name.startswith(("/ZH", "/HZJ")):
        sample_info["sample_category"] = "ZH"
      else:
        assert(sample_name.startswith("/VH"))
        sample_info["use_it"] = False

  return samples
