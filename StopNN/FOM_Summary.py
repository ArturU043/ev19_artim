import matplotlib.pyplot as plt
import os
from commonFunctions import assure_path_exists
import localConfig as cfg
import numpy as np



if __name__ == "__main__":
    import argparse


    parser=argparse.ArgumentParser(description="Chose models to plot fom")
    parser.add_argument('-i', '--version', type=str, required=True, help="Select the models to plot together in same plot graphic with differents plots foms ")

    args=parser.parse_args()
    list=args.version
    list=list.split()

    ##Creating list with file path

    testpath=cfg.lgbk+"test/"
    i=0
    path=[]
    while i<len(list) :
        path.append(testpath+"Model_Ver_"+str(list[i])+"/plots_Model_Ver_"+str(list[i])+"/")
        i=i+1


    #Importing data file
    i=0
    while (i<len(path)):

        fom_Cut = np.loadtxt(path[i]+"FOM_cut_data.txt",delimiter="\n")
        fom_Evo = np.loadtxt(path[i]+"FOM_evo_data.txt",delimiter="\n")
        max_FOM=0
	
	for k in fom_Evo:
	     if k>max_FOM:
       	     	max_FOM=k
	print("Model"+list[i]+" With max fom {}".format(max_FOM))

        plt.plot(fom_Cut, fom_Evo, label="Model_{}".format(i))
  
        i=i+1

    plt.title("FOM Comparing")
    plt.ylabel("FOM")
    plt.xlabel("NN output")
    plt.show()
    
