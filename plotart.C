#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <sstream>

#include "TROOT.h"
#include "TFile.h"
#include "TTree.h"
#include "TCut.h"
#include "TChain.h"
#include "TH1D.h"
#include "TCanvas.h"
#include "TGraphErrors.h"
#include "string"
#include "vector"


void plotLepPt(){
  TChain plot_550_520("bdttree");

  // access bdtt
  plot_550_520.add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19_test/T2DegStop_550_520.root");

  // plot create
  TH1D* pl_lepPt = new TH1D("pl_lepPt", "lepPT", 200,0,200);
  TH1D* pl_xs = new TH1D("pl_xs", "XS", 200,0,200);
  TH1D* pl_jet_pt = new TH1D("pl_jet_pt", "Jet1PT", 200,0,200);
  TH1D* pl_met = new TH1D("pl_met", "Met", 200,0,200);
  TH1D* pl_mt = new TH1D("pl_mt", "mt", 200,0,200);
  TH1D* pl_Lep_Eta = new TH1D("pl_Lep_Eta", "lepEta", 200,0,200);
  TH1D* pl_lep_chg = new TH1D("pl_lep_chg", "lepChg", 200,0,200);
  TH1D* pl_ht = new TH1D("pl_ht", "ht", 200,0,200);
  TH1D* pl_Nb = new TH1D("pl_Nb", "Nbloose", 200,0,200);
  TH1D* pl_Njet = new TH1D("pl_Njet", "Njet", 200,0,200);
  TH1D* pl_jet_HB = new TH1D("pl_jet_HB", "JetHBpt", 200,0,200);
  TH1D* pl_dr = new TH1D("pl_dr", "DrJetHblep", 200,0,200);
  TH1D* pl_jet_HB_csv = new TH1D("pl_jet_HB_csv", "JetHBCSV", 200,0,200);

  //Draw histograms
  plot_550_520.Draw("LepPT>>pl_lepPt");
  plot_550_520.Draw("XS>>pl_xs");
  plot_550_520.Draw("Jet1Pt>>pl_jet_pt");
  plot_550_520.Draw("Met>>pl_met");
  plot_550_520.Draw("mt>>pl_mt");
  plot_550_520.Draw("LepEta>>pl_Lep_Eta");
  plot_550_520.Draw("LepChg>>pl_lep_chg");
  plot_550_520.Draw("HT>>pl_ht");
  plot_550_520.Draw("NbLoose>>pl_Nb");
  plot_550_520.Draw("Njet>>pl_Njet");
  plot_550_520.Draw("JetHBpt>>pl_jet_HB");
  plot_550_520.Draw("DrJetHBLep>>pl_dr");
  plot_550_520.Draw("JetHBCSV>>pl_jet_HB_csv");


  //COMPARE TCanvas

  TCanvas *comp = new TCanvas("comp",8000,8000);
  comp.divide(4,4) ;

  pl_lepPt->Draw("");
  pl_dr->Draw("same");
  pl_ht->Draw("same");
  pl_xs->Draw("same");
  pl_Nb->Draw("same");
  pl_mt->Draw("same");
  pl_met->Draw("same");
  pl_Njet->Draw("same");
  pl_lepPt->Draw("same");
  pl_jet_HB->Draw("same");
  pl_Lep_Eta->Draw("same");
  pl_lep_chg->Draw("same");
  pl_jet_HB_csv->Draw("same");

  //SAVE
  comp->SaveAS("compare_histograms_550_520.pdf");

}
