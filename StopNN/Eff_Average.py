import os
import localConfig as cfg
import numpy as np
import matplotlib.pyplot as plt
from commonFunctions import assure_path_exists
from shutil import copyfile


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Chose models to plot fom")
    parser.add_argument('-i', '--version', type=str, required=True, help="Select the model to average and plot")

    args = parser.parse_args()
    paul = args.version
    list = paul.split()


    #Creating a list with filepaths:
    testpath = cfg.lgbk+"test/"
    i = 0
    path = []
    while (i < len(list)) :
        path.append(testpath+"Model_Ver_"+str(list[i])+"/plots_Model_Ver_"+str(list[i])+"/")
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
        bkgEff_ave = 0
        sigEff_ave = 0
        while (a < len(list)):
            bkgEff_ave = bkgEff_ave + bkgEff[a][i]
            sigEff_ave = sigEff_ave + sigEff[a][i]
            a = a + 1
        bkgEff_ave[i] = bkgEff_ave/len(list)
        bkgEff_ave[i] = bkgEff_ave/len(list)
        i = i + 1

    #Storing data used to draw the efficiency
    f = open(averagepath + "bkgEff_ave_data.txt","w+")
    f.write("\n".join(map(str,bkgEff_ave)))
    f.close()

    f = open(averagepath + "sigEff_ave_data.txt","w+")
    f.write("\n".join(map(str,sigEff_ave)))
    f.close()

    print("Efficiency curves saved in Model_Ver_" + paul[:2] + "_average/" +":-O")
