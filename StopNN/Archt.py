def NNarch(act,list):

    i_max = len(list)

    model.add(Dense(list[0], input_dim=12, activation=str(act)))

    i=1
    while i < i_max :
        model.add(Dense(list[i], activation=str(act)))
        print(list[i])
        i=i+1
