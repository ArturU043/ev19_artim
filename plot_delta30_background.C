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


void plot_delta30_background(){
  TChain plot_30_bg("bdttree");

  // access bdtt WJets, TTbar, ZInv
  plot_30_bg.Add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19_test/T2DegStop_deltaM30.root");

  // plot create
  TH1D* pl_Wjet = new TH1D("pl_Wjet", "Wjet", 200,0,200);
  TH1D* pl_tt = new TH1D("pl_tt", "TTbar", 200,0,200);
  TH1D* pl_Z = new TH1D("pl_Z", "ZInv", 200,0,200);


  //Draw histograms
  plot_30_bg.Draw("WJets>>pl_Wjet");
  plot_30_bg.Draw("TTbar>>pl_tt");
  plot_30_bg.Draw("ZInv>>Z");

  //Create and divide TCanvas

  TCanvas *c1 = new TCanvas("c1","",8000,8000);
  c1->Divide(3,1) ;


  //Plot those graph!
  c1->cd(1);
  pl_Wjet->Draw("");
  c1->cd(2);
  pl_tt->Draw("");
  c1->cd(3);
  pl_Z->Draw("");

  //SAVE
  c1->SaveAs("compare_histograms_Delta_30_background.pdf");


}
