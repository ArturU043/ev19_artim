name="exercise_Ver_1"

filepath ="/home/t3cms/ev19u045/LSTORE/ev19_artim/StopNN/test/{}/".format(name)


with open(filepath+"accuracy/acc_"+name+".pickle",'rb') as f
    f_acc = pickle.load(f)
