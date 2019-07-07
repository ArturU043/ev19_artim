#include<stdio.h>
#include<string.h>

void plotim(){

// find files

TChain uno("bdttre");
 uno.Add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19/T2DegStop_550_520.root");
 //uno.Add("/home/t3cms/dbastos/LSTORE/Stop4Body/nTuples16_v2017-10-19/T2DegStop_deltaM30.root");

// lists
string newname[20]={"new_XS", "new_Jet1Pt", "new_Met", "new_mt", "new_LepEta", "new_LepChg", "new_HT", "new_NbLoose", "new_Njet", "new_JetHBpt", "new_DrJetHBLep","new_JetHBCSV"};
string oldname[20]= {"XS", "Jet1Pt", "Met", "mt", "LepEta", "LepChg", "HT", "NbLoose", "Njet", "JetHBpt", "DrJetHBLep","JetHBCSV"};

printf("%s", newname[20].str(3));


//new graphs
/*int i=0;

do

while (i<12; i++){
  //TH1D* newname[i] = new TH1D("newname[i]", "oldname[i]", 200,0,200);
  //bdttree->Draw("oldname[i]>>newname[i]");
  string a = newname[i];
  string b = oldname [i];

  printf("%s \n", &a) ;
  printf("%s \n", &b) ;

}*/



}
