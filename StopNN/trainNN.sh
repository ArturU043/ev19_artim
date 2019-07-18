#!/bin/bash

#...$ -cwd
#$ -pe mcore 3

#$ -l container=True
#...$ -v CONTAINER=CENTOS7
#$ -v CONTAINER=UBUNTU16

#...$ -v SGEIN=script.py
#...$ -v SGEIN=pima-indians-diabetes.data

#$ -v SGEIN=trainNN.py
#$ -v SGEIN=prepareDATA.py
#$ -v SGEIN=localConfig.py
#$ -v SGEIN=commonFunctions.py

#$ -v SGEOUT=test:/home/t3cms/ev19u043/LSTORE/ev_artim/StopNN

#...$ -v SGEOUT=accuracy.pickle
#...$ -v SGEOUT=loss.pickle

#...$ -l gpu,release=el7

#cd /home/t3cms/ev19u043/LSTORE/ev_artim/StopNN

module load root-6.10.02

[ -d test ] || mkdir test

python trainNN.py -a 3000 -b 0.01 -e 100 -i 7 -l "24 18 12 6"
