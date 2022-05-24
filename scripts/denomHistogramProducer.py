#!/usr/bin/env python

from tthAnalysis.HiggsToTauTau.common import SmartFormatter, logging
from tthAnalysis.HiggsToTauTau.safe_root import ROOT

from rootpy.plotting import Hist2D

import argparse
import os
import array

ROOT.gROOT.SetBatch(True)

os.environ["MKL_NUM_THREADS"] = "1"

BINNING_COSTHETASTAR = [ 0.0, 0.4, 0.6, 0.8, 1.0 ]
BINNING_MHH = {
  'lo' : [
    250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,
    540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,750,800,850,900,950,1000,1100,1200,1300,1400,1500.,1750,2000,50000
  ],
  'nlo' : [
    250, 270, 290, 310, 330, 350, 370, 390, 410, 430, 450, 470, 490, 510, 530, 550, 570, 590, 610, 630, 650, 670, 700,
    750, 800, 850, 900, 950, 1000, 1100, 1200, 1300, 1400, 1500, 1750, 2000, 5000.
  ],
}

MHH_BR_NAME = 'mHH_lhe'
COST_BR_NAME = 'cosThetaStar_lhe'
GENWEIGHT_BR_NAME = 'genWeight'

def comp_genweight(genweight_br, genweight_ref, use_genweight):
  weight = 1. if genweight_br[0] > 0 else -1.
  if use_genweight:
    weight *= min(abs(genweight_br[0]), 3 * genweight_ref)
  return weight

parser = argparse.ArgumentParser(
  formatter_class = lambda prog: SmartFormatter(prog, max_help_position = 55)
)
parser.add_argument('-i', '--input',
  type = str, dest = 'input', metavar = 'file', required = True,
  help = 'R|Input Ntuple',
)
parser.add_argument('-o', '--output',
  type = str, dest = 'output', metavar = 'file', required = True,
  help = 'R|Output Ntuple',
)
parser.add_argument('-p', '--process',
  type = str, dest = 'process', metavar = 'name', required = True,
  help = 'R|Process name',
)
parser.add_argument('-c', '--category',
  type = str, dest = 'category', metavar = 'name', required = True,
  help = 'R|Process name',
)
parser.add_argument('-g', '--gen-weight',
  type = float, dest = 'gen_weight', metavar = 'number', required = False, default = 0.,
  help = 'R|Use generator level weight to fill the histograms',
)
parser.add_argument('-b', '--binning',
  type = str, dest = 'binning', metavar = 'binning', required = True, choices = list(BINNING_MHH.keys()),
  help = 'R|Binning',
)
parser.add_argument('-v', '--verbose',
  dest = 'verbose', action = 'store_true', default = False, required = False,
  help = 'R|Verbose output',
)
args = parser.parse_args()

input_fn = args.input
output_fn = os.path.abspath(args.output)
process_name = args.process
category_name = args.category
binning_choice = args.binning
genweight_ref = args.gen_weight

use_genweight = genweight_ref != 0.

if args.verbose:
  logging.getLogger().setLevel(logging.DEBUG)

if not os.path.isfile(input_fn):
  raise ValueError("No such file: %s" % input_fn)

output_dir = os.path.dirname(output_fn)
if not os.path.isdir(output_dir):
  logging.warning("Creating directory: {}".format(output_dir))
  os.makedirs(output_dir)

input_file = ROOT.TFile.Open(input_fn, 'read')
assert(input_file)
input_tree = input_file.Get('Events')

denominator_process = Hist2D(BINNING_MHH[binning_choice], BINNING_COSTHETASTAR, name = process_name)
denominator_category = Hist2D(BINNING_MHH[binning_choice], BINNING_COSTHETASTAR, name = category_name)

nof_events = input_tree.GetEntries()
logging.debug("Input file {} has {} events".format(input_fn, nof_events))

has_evt_brs = not bool({MHH_BR_NAME, COST_BR_NAME} - set(br.GetName() for br in input_tree.GetListOfBranches()))
if has_evt_brs:
  logging.debug("Input file {} already contains necessary event-level branches".format(input_fn))

  mhh_br = array.array('f', [0.])
  cost_br = array.array('f', [0.])
  genweight_br = array.array('f', [0.])

  input_tree.SetBranchAddress(MHH_BR_NAME, mhh_br)
  input_tree.SetBranchAddress(COST_BR_NAME, cost_br)
  if use_genweight:
    input_tree.SetBranchAddress(GENWEIGHT_BR_NAME, genweight_br)

  input_tree.SetBranchStatus('*', 0)
  input_tree.SetBranchStatus(MHH_BR_NAME, 1)
  input_tree.SetBranchStatus(COST_BR_NAME, 1)
  if use_genweight:
    input_tree.SetBranchStatus(GENWEIGHT_BR_NAME, 1)

  for idx in range(nof_events):
    input_tree.GetEntry(idx)

    mhh = mhh_br[0]
    cost = cost_br[0]
    weight = comp_genweight(genweight_br, genweight_ref, use_genweight)

    denominator_process.Fill(mhh, cost, weight)
    denominator_category.Fill(mhh, cost, weight)
else:
  logging.debug(
    "Input file {} does not contain necessary event-level branches -> we need to compute them".format(input_fn)
  )

  collection_max_size = 32
  collection_name = 'LHEPart'
  collection_sz_name = 'n{}'.format(collection_name)
  collection_pt_name = '{}_pt'.format(collection_name)
  collection_eta_name = '{}_eta'.format(collection_name)
  collection_phi_name = '{}_phi'.format(collection_name)
  collection_mass_name = '{}_mass'.format(collection_name)
  collection_pdgId_name = '{}_pdgId'.format(collection_name)

  sz_br = array.array('I', [0])
  pt_br = array.array('f', [0.] * collection_max_size)
  eta_br = array.array('f', [0.] * collection_max_size)
  phi_br = array.array('f', [0.] * collection_max_size)
  mass_br = array.array('f', [0.] * collection_max_size)
  pdgId_br = array.array('i', [0] * collection_max_size)
  genweight_br = array.array('f', [0.])

  input_tree.SetBranchAddress(collection_sz_name, sz_br)
  input_tree.SetBranchAddress(collection_pt_name, pt_br)
  input_tree.SetBranchAddress(collection_eta_name, eta_br)
  input_tree.SetBranchAddress(collection_phi_name, phi_br)
  input_tree.SetBranchAddress(collection_mass_name, mass_br)
  input_tree.SetBranchAddress(collection_pdgId_name, pdgId_br)
  if use_genweight:
    input_tree.SetBranchAddress(GENWEIGHT_BR_NAME, genweight_br)

  input_tree.SetBranchStatus('*', 0)
  input_tree.SetBranchStatus(collection_sz_name, 1)
  input_tree.SetBranchStatus(collection_pt_name, 1)
  input_tree.SetBranchStatus(collection_eta_name, 1)
  input_tree.SetBranchStatus(collection_phi_name, 1)
  input_tree.SetBranchStatus(collection_mass_name, 1)
  input_tree.SetBranchStatus(collection_pdgId_name, 1)
  if use_genweight:
    input_tree.SetBranchStatus(GENWEIGHT_BR_NAME, 1)

  for idx in range(nof_events):
    input_tree.GetEntry(idx)
    higgses = []
    for partIdx in range(sz_br[0]):
      if pdgId_br[partIdx] == 25:
        p4 = ROOT.TLorentzVector()
        p4.SetPtEtaPhiM(pt_br[partIdx], eta_br[partIdx], phi_br[partIdx], mass_br[partIdx])
        higgses.append(p4)
    if len(higgses) != 2:
      logging.warning("Event #{} did not contain two LHE parton-level Higgses!".format(idx))
      continue

    leading_idx = 0 if higgses[0].E() > higgses[1] else 1
    leading_higgs = higgses[leading_idx]
    subleading_higgs = higgses[1 - leading_idx]
    higgs_sum = leading_higgs + subleading_higgs

    mhh = higgs_sum.M()
    leading_higgs.Boost(-higgs_sum.BoostVector())
    cost = abs(leading_higgs.CosTheta())
    weight = comp_genweight(genweight_br, genweight_ref, use_genweight)

    denominator_process.Fill(mhh, cost, weight)
    denominator_category.Fill(mhh, cost, weight)

output_file = ROOT.TFile.Open(output_fn, 'recreate')
output_file.cd()
denominator_process.Write()
denominator_category.Write()

output_file.Close()
input_file.Close()

logging.debug("Saved histograms {} and {} to {}".format(process_name, category_name, output_fn))
