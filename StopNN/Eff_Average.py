import os
import localConfig as cfg
import numpy as np
import matplotlib.pyplot as plt
from commonFunctions import assure_path_exists
from shutil import copyfile


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Chose models to plot fom")
    parser.add_argument('-i', '--version', type=str, required=True, help="Select the models to average and plot e.g ( -i '14.01 14.02 14.03')")

    args = parser.parse_args()
    paul = args.version
    list = paul.split()
    modelpath = cfg.lgbk+"Models/"
    averagepath = modelpath + "Model_Ver_" + paul[:2] + "_average/plots_Model_Ver_" + paul[:2] + "_average/"

    #With paul[:2] we get the two first digits of the models we are comparing , only compare models with
    #the same 2 first digits ; for more than 2 digits name change the arg
    #Creating a list with filepaths:
    modelpath = cfg.lgbk+"test/"
    i = 0
    path = []
    while (i < len(list)) :
        path.append(modelpath+"Model_Ver_"+str(list[i])+"/plots_Model_Ver_"+str(list[i])+"/")
        i = i + 1

    #Initializing empty lists to compute efficiency average:
    bkgEff = []
    sigEff = []

    #Importing data
    i = 0
    while (i < len(path)):
        bkgEff.append(np.loadtxt(path[i]+"bkg_eff_data.txt",delimiter="\n"))
        sigEff.append(np.loadtxt(path[i]+"sig_eff_data.txt",delimiter="\n"))
        i = i + 1

    #Initializing average list:
    i = 0
    bkgEff_ave = []
    sigEff_ave = []
    while (i < len(bkgEff[1])):
        bkgEff_ave.append(0.0)
        sigEff_ave.append(0.0)
        i = i + 1

    #Computing average
    i = 0
    while (i < len(bkgEff[1])):
        a = 0
        b_ave = 0
        s_ave = 0
        while (a < len(list)):
            b_ave = b_ave + bkgEff[a][i]
            s_ave = s_ave + sigEff[a][i]
            a = a + 1
        bkgEff_ave[i] = b_ave/len(list)
        sigEff_ave[i] = s_ave/len(list)
        i = i + 1

    #Storing data used to draw the efficiency
    f = open(averagepath + "bkgEff_ave_data.txt","w+")
    f.write("\n".join(map(str,bkgEff_ave)))
    f.close()

    f = open(averagepath + "sigEff_ave_data.txt","w+")
    f.write("\n".join(map(str,sigEff_ave)))
    f.close()

    print("Efficiency data saved in Model_Ver_" + paul[:2] + "_average/" +":-O")
