Data_l=["XS","Jet1Pt","Met","mt","LepEta","LepChg","HT","NbLoose","Njet","JetHBpt","DrJetHBLep","JetHBCSV"]

i=0
import os
while (i<=len(Data_l)) :

    cmd_a="TH1D* t_{} = new TH1D(t_{},{},200,0,200)".format(i, i, Data_l[i])

    cmd_b="bbttree->Draw({}>>t_{})".format(Data_l[i],i)


    print("{}".format(cmd_a))
    print("{}\n\n".format(cmd_b))





    #os.system(cmd_a)


    #   os.system(cmd_b)

    i=i+1
