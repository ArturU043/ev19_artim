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


void plot_sb_weight(){
  TChain plot_30("bdttree");
  TChain plot_30_Background("bdttree");

  // access bdtt
  plot_30.Add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19_test/T2DegStop_deltaM30.root");
  plot_30_Background.Add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19_test/TT_pow.root");

  // plot create signal
  TH1D* pl_lepPt = new TH1D("pl_lepPt", "lepPT", 200,0,200);
  TH1D* pl_xs = new TH1D("pl_xs", "XS", 200,0,25);
  TH1D* pl_jet_pt = new TH1D("pl_jet_pt", "Jet1PT", 800,0,800);
  TH1D* pl_met = new TH1D("pl_met", "Met", 1500,0,1500);
  TH1D* pl_mt = new TH1D("pl_mt", "mt", 200,0,200);
  TH1D* pl_Lep_Eta = new TH1D("pl_Lep_Eta", "lepEta", 100,-2.5,2.500);
  TH1D* pl_lep_chg = new TH1D("pl_lep_chg", "lepChg", 4,-1.50,1.50);
  TH1D* pl_ht = new TH1D("pl_ht", "ht", 800,200,1000);
  TH1D* pl_Nb = new TH1D("pl_Nb", "Nbloose", 6,0,6);
  TH1D* pl_Njet = new TH1D("pl_Njet", "Njet", 10,0,10);
  TH1D* pl_jet_HB = new TH1D("pl_jet_HB", "JetHBpt", 700,0,700);
  TH1D* pl_dr = new TH1D("pl_dr", "DrJetHblep", 100,0,4);
  TH1D* pl_jet_HB_csv = new TH1D("pl_jet_HB_csv", "JetHBCSV", 100,0,1);


  // plot create Background
  TH1D* pl_lepPt_Background = new TH1D("pl_lepPt_Background", "lepPT", 200,0,200);
  TH1D* pl_xs_Background = new TH1D("pl_xs_Background", "XS", 200,0,25);
  TH1D* pl_jet_pt_Background = new TH1D("pl_jet_pt_Background", "Jet1PT", 800,0,800);
  TH1D* pl_met_Background = new TH1D("pl_met_Background", "Met", 1500,0,1500);
  TH1D* pl_mt_Background = new TH1D("pl_mt_Background", "mt", 200,0,200);
  TH1D* pl_Lep_Eta_Background = new TH1D("pl_Lep_Eta_Background", "lepEta", 100,-2.5,2.500);
  TH1D* pl_lep_chg_Background = new TH1D("pl_lep_chg_Background", "lepChg", 4,-1.50,1.50);
  TH1D* pl_ht_Background = new TH1D("pl_ht_Background", "ht", 800,200,1000);
  TH1D* pl_Nb_Background = new TH1D("pl_Nb_Background", "Nbloose", 6,0,6);
  TH1D* pl_Njet_Background = new TH1D("pl_Njet_Background", "Njet", 10,0,10);
  TH1D* pl_jet_HB_Background = new TH1D("pl_jet_HB_Background", "JetHBpt", 700,0,700);
  TH1D* pl_dr_Background = new TH1D("pl_dr_Background", "DrJetHblep", 100,0,4);
  TH1D* pl_jet_HB_csv_Background = new TH1D("pl_jet_HB_csv_Background", "JetHBCSV", 100,0,1);



  //Draw histograms signal
  plot_30.Draw("LepPt>>pl_lepPt","weight");
  pl_lepPt->SetLineColor(1);

  //Normalising
  int se= pl_lepPt->GetEntries();
  pl_lepPt->Scale(1./se);


  plot_30.Draw("XS>>pl_xs","weight");
  pl_xs->SetLineColor(1);
  pl_xs->Scale(1./se);

  plot_30.Draw("Jet1Pt>>pl_jet_pt","weight");
  pl_jet_pt->SetLineColor(1);
  pl_jet_pt->Scale(1./se);

  plot_30.Draw("Met>>pl_met","weight");
  pl_met->SetLineColor(1);
  pl_met->Scale(1./se);

  plot_30.Draw("mt>>pl_mt","weight");
  pl_mt->SetLineColor(1);
  pl_mt->Scale(1./se);

  plot_30.Draw("LepEta>>pl_Lep_Eta","weight");
  pl_Lep_Eta->SetLineColor(1);
  pl_Lep_Eta->Scale(1./se);

  plot_30.Draw("LepChg>>pl_lep_chg","weight");
  pl_lep_chg->SetLineColor(1);\
  pl_lep_chg->Scale(1./se);

  plot_30.Draw("HT>>pl_ht","weight");
  pl_ht->SetLineColor(1);
  pl_ht->Scale(1./se);

  plot_30.Draw("NbLoose>>pl_Nb","weight");
  pl_Nb->SetLineColor(1);
  pl_Nb->Scale(1./se);

  plot_30.Draw("Njet>>pl_Njet","weight");
  pl_Njet->SetLineColor(1);
  pl_Njet->Scale(1./se);

  plot_30.Draw("JetHBpt>>pl_jet_HB","weight");
  pl_jet_HB->SetLineColor(1);
  pl_jet_HB->Scale(1./se);

  plot_30.Draw("DrJetHBLep>>pl_dr","weight");
  pl_dr->SetLineColor(1);
  pl_dr->Scale(1./se);

  plot_30.Draw("JetHBCSV>>pl_jet_HB_csv","weight");
  pl_jet_HB_csv->SetLineColor(1);
  pl_jet_HB_csv->Scale(1./se);


  //Draw histograms background
  plot_30_Background.Draw("LepPt>>pl_lepPt_Background","weight");
  pl_lepPt_Background->SetLineColor(2);

  // Background normalisation
    int be = pl_lepPt_Background->GetEntries();
    pl_lepPt_Background->Scale(1./be);


  plot_30_Background.Draw("XS>>pl_xs_Background","weight");
  pl_xs_Background->SetLineColor(2);
  pl_xs_Background->Scale(1./be);

  plot_30_Background.Draw("Jet1Pt>>pl_jet_pt_Background","weight");
  pl_jet_pt_Background->SetLineColor(2);
  pl_jet_pt_Background->Scale(1./be);

  plot_30_Background.Draw("Met>>pl_met_Background","weight");
  pl_met_Background->SetLineColor(2);
  pl_met_Background->Scale(1./be);

  plot_30_Background.Draw("mt>>pl_mt_Background","weight");
  pl_mt_Background->SetLineColor(2);
  pl_mt_Background->Scale(1./be);

  plot_30_Background.Draw("LepEta>>pl_Lep_Eta_Background","weight");
  pl_Lep_Eta_Background->SetLineColor(2);
  pl_Lep_Eta_Background->Scale(1./be);

  plot_30_Background.Draw("LepChg>>pl_lep_chg_Background","weight");
  pl_lep_chg_Background->SetLineColor(2);
  pl_lep_chg_Background->Scale(1./be);

  plot_30_Background.Draw("HT>>pl_ht_Background","weight");
  pl_ht_Background->SetLineColor(2);
  pl_ht_Background->Scale(1./be);

  plot_30_Background.Draw("NbLoose>>pl_Nb_Background","weight");
  pl_Nb_Background->SetLineColor(2);
  pl_Nb_Background->Scale(1./be);

  plot_30_Background.Draw("Njet>>pl_Njet_Background","weight");
  pl_Njet_Background->SetLineColor(2);
  pl_Njet_Background->Scale(1./be);

  plot_30_Background.Draw("JetHBpt>>pl_jet_HB_Background","weight");
  pl_jet_HB_Background->SetLineColor(2);
  pl_jet_HB_Background->Scale(1./be);

  plot_30_Background.Draw("DrJetHBLep>>pl_dr_Background","weight");
  pl_dr_Background->SetLineColor(2);
  pl_dr_Background->Scale(1./be);

  plot_30_Background.Draw("JetHBCSV>>pl_jet_HB_csv_Background","weight");
  pl_jet_HB_csv_Background->SetLineColor(2);
  pl_jet_HB_csv_Background->Scale(1./be);


  //Create and divide TCanvas
  TCanvas *c1 = new TCanvas("c1","",8000,8000);
  c1->Divide(4,4) ;

  //Plot those graphs!
  c1->cd(1);
  pl_lepPt->Draw("");
  pl_lepPt_Background->Draw("same");

  c1->cd(2);
  pl_dr_Background->Draw("");
  pl_dr->Draw("same");

  c1->cd(3);
  pl_ht_Background->Draw("");
  pl_ht->Draw("same");

  c1->cd(4);
  pl_xs->Draw("");
  pl_xs_Background->Draw("same");

  c1->cd(5);
  pl_Nb_Background->Draw("");
  pl_Nb->Draw("same");

  c1->cd(6);
  pl_mt_Background->Draw("");
  pl_mt->Draw("same");

  c1->cd(7);
  pl_met_Background->Draw("");
  pl_met->Draw("same");

  c1->cd(8);
  pl_Njet_Background->Draw("");
  pl_Njet->Draw("same");

  c1->cd(9);
  pl_jet_pt_Background->Draw("");
  pl_jet_pt->Draw("same");

  c1->cd(10);
  pl_jet_HB_Background->Draw("");
  pl_jet_HB->Draw("same");

  c1->cd(11);
  pl_Lep_Eta_Background->Draw("");
  pl_Lep_Eta->Draw("same");

  c1->cd(12);
  pl_lep_chg_Background->Draw("");
  pl_lep_chg->Draw("same");

  c1->cd(13);
  pl_jet_HB_csv->Draw("");
  pl_jet_HB_csv_Background->Draw("same");

  //SAVE
  c1->SaveAs("compare_histograms_Delta_30_Weights.pdf");


}
