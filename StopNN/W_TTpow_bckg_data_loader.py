'''
Functions used in different files are gathered here to avoid redundance.
'''
import os
import root_numpy
import pandas
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout, AlphaDropout
from keras.optimizers import Adam, Nadam
from keras.regularizers import l1,l2
from math import log

# Signal Dataset

signalMap = {
              "DM30" : ["T2DegStop_250_220",
                        "T2DegStop_275_245",
                        "T2DegStop_300_270",
                        "T2DegStop_325_295",
                        "T2DegStop_350_320",
                        "T2DegStop_375_345",
                        "T2DegStop_400_370",
                        "T2DegStop_425_395",
                        "T2DegStop_450_420",
                        "T2DegStop_475_445",
                        "T2DegStop_500_470",
                        "T2DegStop_525_495",
                        "T2DegStop_550_520",
                        "T2DegStop_575_545",
                        "T2DegStop_600_570",
                        "T2DegStop_625_595",
                        "T2DegStop_650_620",
                        "T2DegStop_675_645",
                        "T2DegStop_700_670",
                        "T2DegStop_725_695",
                        "T2DegStop_750_720",
                        "T2DegStop_775_745",
                        "T2DegStop_800_770"],
              "300_270" : ["T2DegStop_300_270"],
              "550_520" : ["T2DegStop_550_520"]
            }

# Background Dataset

bkgDatasets = [
                "Wjets_70to100",
                "Wjets_100to200",
                "Wjets_200to400",
                "Wjets_400to600",
                "Wjets_600to800",
                "Wjets_800to1200",
                "Wjets_1200to2500",
                "Wjets_2500toInf",
                #"TTJets_DiLepton",
                #"TTJets_SingleLeptonFromTbar",
                #"TTJets_SingleLeptonFromT",
                "TT_pow",
#                "ZJetsToNuNu_HT100to200",
#                "ZJetsToNuNu_HT200to400",
#                "ZJetsToNuNu_HT400to600",
#                "ZJetsToNuNu_HT600to800",
#                "ZJetsToNuNu_HT800to1200",
#                "ZJetsToNuNu_HT1200to2500",
#                "ZJetsToNuNu_HT2500toInf",
#                #Drell yan
#                "DYJetsToLL_M50_HT100to200",
#                "DYJetsToLL_M50_HT200to400",
#                "DYJetsToLL_M50_HT400to600",
#                "DYJetsToLL_M50_HT600to800",
#                "DYJetsToLL_M50_HT800to1200",
#                "DYJetsToLL_M50_HT1200to2500",
#                "DYJetsToLL_M5to50_HT100to200",
#                "DYJetsToLL_M5to50_HT200to400",
#                "DYJetsToLL_M50_HT400to600",
#                "DYJetsToLL_M5to50_HT600toInf",
                #QCD
#                "QCD_HT50to100",
#                "QCD_HT100to200",
#                "QCD_HT200to300",
#                "QCD_HT300to500",
#                "QCD_HT500to700",
#                "QCD_HT700to1000",
#                "QCD_HT1000to1500",
#                "QCD_HT1500to2000",
#                "QCD_HT2000toInf",
                #Single top
#                "TBar_tch_powheg",
#                "TBar_tWch_ext",
#                "T_tch_powheg",
#                "T_tWch_ext",
                #?
#                "TTGJets",
                #TTV
#                "TTW_LO",
#                "TTWToLNu",
#                "TTWToQQ",
#                "TTZ_LO",
#                "TTZToLLNuNu_m1to10",
#                "TTZToLLNuNu",
#                "TTZToQQ",
                #VV - di-boson
#                "WW",
#                "WZ",
#                "ZZ"


              ]

# Load the Data

def StopDataLoader(path, features, test="550_520", selection="", treename="bdttree", suffix="", signal="DM30", fraction=1.0, useSF=False):
  if signal not in signalMap:
    raise KeyError("Unknown training signal requested ("+signal+")")
  if test not in signalMap:
    raise KeyError("Unknown test signal requested ("+test+")")
  if fraction >= 1.0:
    fraction = 1.0
  if fraction < 0.0:
    raise ValueError("An invalid fraction was chosen")
  if "XS" not in features:
    features.append("XS")
  if "Nevt" not in features:
    features.append("Nevt")
  if "Event" not in features:
    features.append("Event")
  if "weight" not in features:
    features.append("weight")

  # Train and Test Data split for Signal

  sigDev = None
  sigVal = None


  testPath = "nTuples16_v2017-10-19_test"+suffix+"/"
  trainPath = "nTuples16_v2017-10-19_train"+suffix+"/"

  #testPath = "test/"
  #trainPath = "train/"

  for sigName_test in signalMap[test]:
    tmp = root_numpy.root2array(
                                path + testPath + sigName_test + suffix + ".root",
                                treename=treename,
                                selection=selection,
                                branches=features
                                )
    if fraction < 1.0:
      tmp = tmp[:int(len(tmp)*fraction)]
    if sigVal is None:
      sigVal = pandas.DataFrame(tmp)
    else:
      sigVal = sigVal.append(pandas.DataFrame(tmp), ignore_index=True)


  for sigName in signalMap[signal]:
    tmp = root_numpy.root2array(
                                path + trainPath + sigName + suffix + ".root",
                                treename=treename,
                                selection=selection,
                                branches=features
                                )
    if fraction < 1.0:
      tmp = tmp[:int(len(tmp)*fraction)]
    if sigDev is None:
      sigDev = pandas.DataFrame(tmp)
    else:
      sigDev = sigDev.append(pandas.DataFrame(tmp), ignore_index=True)

  # Train and Test Data split for Background

  bkgDev = None
  bkgVal = None
  for bkgName in bkgDatasets:
    tmp = root_numpy.root2array(
                                path + trainPath + bkgName + suffix + ".root",
                                treename=treename,
                                selection=selection,
                                branches=features
                                )
    if fraction < 1.0:
      tmp = tmp[:int(len(tmp)*fraction)]
    if bkgDev is None:
      bkgDev = pandas.DataFrame(tmp)
    else:
      bkgDev = bkgDev.append(pandas.DataFrame(tmp), ignore_index=True)

    tmp = root_numpy.root2array(
                                path + testPath + bkgName + suffix + ".root",
                                treename=treename,
                                selection=selection,
                                branches=features
                                )
    if fraction < 1.0:
      tmp = tmp[:int(len(tmp)*fraction)]
    if bkgVal is None:
      bkgVal = pandas.DataFrame(tmp)
    else:
      bkgVal = bkgVal.append(pandas.DataFrame(tmp), ignore_index=True)

  # Data Labelling

  sigDev["category"] = 1
  sigVal["category"] = 1
  bkgDev["category"] = 0
  bkgVal["category"] = 0
  sigDev["sampleWeight"] = 1
  sigVal["sampleWeight"] = 1
  bkgDev["sampleWeight"] = 1
  bkgVal["sampleWeight"] = 1

  if fraction < 1.0:
    sigDev.weight = sigDev.weight/fraction
    sigVal.weight = sigVal.weight/fraction
    bkgDev.weight = bkgDev.weight/fraction
    bkgVal.weight = bkgVal.weight/fraction

  if not useSF:
    sigDev.sampleWeight = sigDev.weight
    sigVal.sampleWeight = sigVal.weight
    bkgDev.sampleWeight = bkgDev.weight
    bkgVal.sampleWeight = bkgVal.weight
  else:
    scale = fraction if fraction < 1.0 else 1.0
    sigDev.sampleWeight = 1/(sigDev.Nevt*scale)
    sigVal.sampleWeight = 1/(sigVal.Nevt*scale)
    bkgDev.sampleWeight = bkgDev.XS/(bkgDev.Nevt*scale)
    bkgVal.sampleWeight = bkgVal.XS/(bkgVal.Nevt*scale)

  sigDev.sampleWeight = sigDev.sampleWeight/sigDev.sampleWeight.sum()
  sigVal.sampleWeight = sigVal.sampleWeight/sigVal.sampleWeight.sum()
  bkgDev.sampleWeight = bkgDev.sampleWeight/bkgDev.sampleWeight.sum()
  bkgVal.sampleWeight = bkgVal.sampleWeight/bkgVal.sampleWeight.sum()

  dev = sigDev.copy()
  dev = dev.append(bkgDev.copy(), ignore_index=True)
  val = sigVal.copy()
  val = val.append(bkgVal.copy(), ignore_index=True)

  return dev, val
