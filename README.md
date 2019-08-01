                                        HOW TO USE THIS GITHUB PAGE
                 
 
* In the "Plots" folder, there is only basic plots we did the first week or so, and interesting results (or so we thought).

* In the "StopNN" folder, there is all the codes we used and on which we did minor changes. There is also the "Models" folder, in which you'll find all the different models we tried. The most promissing being the 10th, and Diogo's the 19th. Each model has its own folder (for exemple Model_Ver_10.01) in which you'll find a .pdf of Loss's and Accuracy's curves, .json and .h5 files and three folders. Two of those are dedicated to store Loss's and Accuracy's pickle file. The third one, "Model_Ver_XX" contains all the interesting curves such as FOM, ROC and signal-backgroung splitting histogram (sometimes the histogram isn't good as we didn't replotted all of them, just use plotNN.py with testpoint=DM30 in prepareData if you are interested in the good histogram).
Futhermore, for each model we ran five times, there is a Model_Ver_XX_average folder, containing a plots_Model_Ver_XX_average folder in which there is all the .txt files used to plot the curves of average FOM and average efficiency. For that, you'll need to run respectively the FOM_Summary.py and the Eff_Summary.py. 
The last update of PlotNN.py is saving efficiency data in .txt files, latter used to plot efficiency curves. But we have only applied it to a small number of models (the most promissing ones and the 19th). It is why it is not possible to used Eff_Average.py for some models. In order to do so, you will have to replot them.
    
    
    
    
    
    
    
    
                                                  
                                                  
                                                  
                                        INFOS ET SITES UTILES 
                                                         
    To DO LIST:
    * improve: -Regulazers (dropouts)
               - Softmax
               -Kernel initializers (he_normal, see Keras.io)  
               -argument de L2 proportionnel a scale loss
    ROOT:                                                   
    * Explication complete histogrammes root : https://root.cern.ch/root/htmldoc/guides/users-guide/Histograms.html
      
    Wiki LIP:
    * https://wiki-lip.lip.pt/Computing/LIP_Lisbon_Farm
    
    NN:
    * Optimisation 
      https://arxiv.org/ftp/arxiv/papers/1808/1808.05979.pdf
      https://www.dlology.com/blog/one-simple-trick-to-train-keras-model-faster-with-batch-normalization/
    * Site de Giles Strong NN: https://amva4newphysics.wordpress.com/tag/neural-networks/
    * Un livre sur le Machine Learning: http://www.deeplearningbook.org/
    * Les amphi de Standfort sur le Machine Learning: https://www.youtube.com/watch?v=NfnWJUyUJYU&list=PLkt2uSq6rBVctENoVBg1TpCC7OQi31AlC
                             et leurs notes de cours : http://cs231n.github.io/
                             et le GitHub: https://github.com/cs231n/cs231n.github.io
    *Plot with keras: https://keras.io/visualization
          with mathplotlib: https://matplotlib.org/3.1.1/tutorials/index.html#introductory
    *Fropout et autres trucs utiles : https://machinelearningmastery.com/dropout-regularization-deep-learning-models-keras/
                                      http://jmlr.org/papers/volume15/srivastava14a.old/srivastava14a.pdf
                             
    Questions
    https://www.youtube.com/watch?v=Ql8QPcp8818
    
                             
      
