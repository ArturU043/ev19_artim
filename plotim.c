#include<stdio.h>

void redraw(){

// find files

TChain uno("bdttre");
 uno.Add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19/T2DegStop_550_520.root");
 //uno.Add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19/T2DegStop_deltaM30.root");

// lists
newname[]={"new_XS", "new_Jet1Pt", "new_Met", "new_mt", "new_LepEta", "new_LepChg", "new_HT", "new_NbLoose", "new_Njet", "new_JetHBpt", "new_DrJetHBLep","new_JetHBCSV"};
oldname[]= {"XS", "Jet1Pt", "Met", "mt", "LepEta", "LepChg", "HT", "NbLoose", "Njet", "JetHBpt", "DrJetHBLep","JetHBCSV"};

//new graphs
i=0

while (i<12){
  //TH1D* newname[i] = new TH1D("newname[i]", "oldname[i]", 200,0,200);
  //bdttree->Draw("oldname[i]>>newname[i]");
  printf("%s", newname[i]);
  printf("%s", oldname[i]);
  i=i+1
}



}
