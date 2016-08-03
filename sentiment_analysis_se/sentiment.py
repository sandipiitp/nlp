# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 11:23:43 2016

@author: Sandip Baishnab
"""

#importing modules
import pandas as pd
from preprocessing import clean 
from feature_extract import feature_class
from classifier import classification

#reading data
training_data=pd.read_csv("C:/Sandip_Debjani/Sandip/Git/program/data/Sem_Eval/train.txt",header=0,sep='\t')
test_data=pd.read_csv("C:/Sandip_Debjani/Sandip/Git/program/data/Sem_Eval/test.txt",header=0,sep='\t')

#creating object for clean,feature generation,
cl=clean()
ft=feature_class()
clf=classification()

#preprocess
preprocessed_train=cl.preprocess(training_data['tweet'])
preprocessed_test=cl.preprocess(test_data['tweet'])
features=ft.feature_function(preprocessed_train)
clf.model_svm()

