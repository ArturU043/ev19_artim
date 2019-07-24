import os
import localConfig as cfg
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Chose models to plot fom")
    parser.add_argument('-i', '--version', type=str, required=True, help="Select the model to average and plot")

    args = parser.parse_args()
    list = args.version
    list = list.split()

    #Creating a list with filepaths:
    testpath = cfg.lgbk+"test/"
    i = 0
    path = []
    while i<len(list) :
        path.append(testpath+"Model_Ver_"+str(list[i])+"/plots_Model_Ver_"+str(list[i])+"/")
        i = i + 1

    #Importing data used to calculate average:
    i = 0
    list_Cut = []
    list_Evo = []
    while (i < len(path)):
        list_Cut.append(np.loadtxt(path[i]+"FOM_cut_data.txt",delimiter="\n"))
        list_Evo.append(np.loadtxt(path[i]+"FOM_evo_data.txt",delimiter="\n"))

        i = i + 1

    print(list_Cut[0,0], list_Cut[0,1])
    print(list_Evo[0,0] list_Evo[0,1])

    #Creating a new file where average will be stored:
#    f = open(filepath+"Average_of_FOM_evo_data.txt","w+")
