import keras
from keras import *
from keras.models import Sequential
from keras.layers import Dense

def NNarch(act,*args):

    i_max = len(list(args))
    
    model=Sequential()
    model.add(Dense(int(args[0][0]), input_dim=12, activation=str(act)))
    
    i=1
    while i < i_max :
        model.add(Dense(int(args[i]), activation=str(act)))
        print(args[i])
        i=i+1
