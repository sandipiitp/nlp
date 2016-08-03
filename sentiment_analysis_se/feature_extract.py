# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 23:39:37 2016

@author: Sandip Baishnab
"""

#importing modules
from sklearn.feature_extraction.text import CountVectorizer

class feature_class():
    
    def feature_function(self, data):
        cv=CountVectorizer()
        features=cv.fit_transform(data)
        features=features.toarray()
        return features        
        