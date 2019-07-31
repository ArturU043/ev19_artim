import matplotlib.pyplot as plt
import os
import localConfig as cfg
import numpy as np



if __name__ == "__main__":
    import argparse


    parser=argparse.ArgumentParser(description="Chose models to plot fom")
    parser.add_argument('-i', '--version', type=str, required=True, help="Select the models to plot together in same plot graphic with differents plots foms ")
    args = parser.parse_args()
    paul = args.version
    list = paul.split()
    testpath = cfg.lgbk+"test/"
    averagepath = testpath + "Model_Ver_" + paul[:2] + "_average/plots_Model_Ver_" + paul[:2] + "_average/"

    ##Creating list with file path
    testpath=cfg.lgbk+"test/"
    i=0
    path=[]
    while i<len(list) :
        path.append(testpath+"Model_Ver_"+str(list[i])+"/plots_Model_Ver_"+str(list[i])+"/")
        i=i+1

    fom_Cut = np.loadtxt(averagepath+"FOM_cut_data.txt",delimiter="\n")
    bkgEff_ave = np.loadtxt(averagepath+"bkgEff_ave_data.txt",delimiter="\n")
    sigEff_ave = np.loadtxt(averagepath+"sigEff_ave_data.txt",delimiter="\n")
    plt.figure()
    plt.plot(fom_Cut,bkgEff_ave , label="Background efficiency")
    plt.plot(fom_Cut,sigEff_ave , label="Signal efficiency")

    plt.title("Efficiency Average")
    plt.ylabel("Eff")
    plt.xlabel("NN output")
    plt.legend()
    plt.show()
