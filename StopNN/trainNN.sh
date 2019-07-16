#!/bin/bash

#$ -cwd
#$ -pe mcore 3

#$ -l container=True
#$ -v CONTAINER=CENTOS7
#...$ -v CONTAINER=UBUNTU16

#...$ -v SGEIN=script.py
#...$ -v SGEIN=pima-indians-diabetes.data

#...$ -v SGEOUT=accuracy.pickle
#...$ -v SGEOUT=loss.pickle

#...$ -l gpu,release=el7

cd /home/t3cms/ev19u043/LSTORE/ev_artim/StopNN

module load root-6.10.02

python trainNN.py -a 3000 -b 0.001 -e 100 -i 3 -l "14 21 7"
