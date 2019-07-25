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
    while (i < len(list)) :
        path.append(testpath+"Model_Ver_"+str(list[i])+"/plots_Model_Ver_"+str(list[i])+"/")
        i = i + 1

    #Importing data in lists used to calculate average:
    i = 0
    list_Evo = []
    while (i < len(path)):
        list_Evo.append(np.loadtxt(path[i]+"FOM_evo_data.txt",delimiter="\n"))
        i = i + 1

    i = 1
    list_ave_Evo = []
    while (i < len(list_Evo[1])):
        list_ave_Evo.append(0.0)
        i = i + 1
    i = 1
    while (i < 4):#len(list_Evo[1])):
        a = 0
        ave_Evo=0
        while (a < len(list)):
            ave_Evo = ave_Evo + list_Evo[a][i]
            a = a + 1
        list_ave_Evo[i] = ave_Evo/len(list)
        i = i + 1

    print(list_ave_Evo[1])
    print(list_ave_Evo[2])
    print(list_ave_Evo[3])

    #print(list_Evo[1][1], list_Evo [2][1], list_ave_Evo[1])

    #Creating a new file where average will be stored:
#    f = open(qqpart+"Average_of_FOM_evo_data.txt","w+")
