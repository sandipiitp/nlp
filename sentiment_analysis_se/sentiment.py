# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 11:23:43 2016

@author: Sandip Baishnab
"""

#importing modules
import pandas as pd
from preprocessing import clean 
from sklearn.feature_extraction.text import TFIDFVectorizer

#reading data
training_data=pd.read_csv("train.txt",header=0,sep='\t')

#preprocessing

#creating object for clean
cl=clean()

for i in range(0,len(training_data['tweet'])):
   prp=cl.preprocess(training_data['tweet'][i])

#vectorization and feature extraction
feature_extract=TfidfVectorizer(analyzer="word",ngram_range=(1,6),max_features=3000,max_df=1.0,min_df=1)