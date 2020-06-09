import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import keras
import pandas
import root_numpy
import numpy as np
from prepareDATA import *
import matplotlib.pyplot as plt
from keras.models import model_from_json
from commonFunctions import FOM1, FOM2, FullFOM, getYields


print("Write Model Version to calculate FOM ; example 2.01")
version = str(input())
name = "Model_Ver_"+version
filepath="Models/"+name+"/"

os.chdir(filepath)

with open(name+'.json', 'r') as json_file:
  loaded_model_json = json_file.read()
model = model_from_json(loaded_model_json)
model.load_weights(name+".h5")

dataVal["NN"]=model.predict(XVal)


fomEvo = []
fomCut = []

for cut in np.arange(0.0, 0.9999, 0.001):
    sig, bkg = getYields(dataVal, cut=cut, luminosity=luminosity)
    if sig[0] > 0 and bkg[0] > 0:
        fom, fomUnc = FullFOM(sig, bkg)
        fomEvo.append(fom)
        fomCut.append(cut)



#Plot fom

plt.plot(fomCut,fomEvo)
plt.title("FOM of Model_"+version)
plt.xlabel("NN output")
plt.ylabel("FOM")
plt.show()

#SAVE VALUES OF FOM EVO AND CUT TO DO A FOM SUMMARY
f= open("new_FOM_evo.txt","w+")
f.write("\n".join(map(str,fomEvo)))
f.close()

f= open("new_FOM_cut.txt","w+")
f.write("\n".join(map(str,fomCut)))
f.close()
