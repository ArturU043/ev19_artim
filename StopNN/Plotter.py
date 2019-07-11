import os
import matplotlib.pyplot as plt
import sys
import pickle


def plotter(path,Ylabel,Title):
    open_= open(path,'rb')
    plot_= pickle.load(open_)
    plt.plot(plot_)
    plt.ylabel(Ylabel)
    plt.xlabel("Epochs")
    plt.legend()
    plt.title(Title)
