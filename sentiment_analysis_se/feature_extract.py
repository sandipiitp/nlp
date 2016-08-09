# -*- coding: utf-8 -*-
"""
Created on Mon Aug 01 23:39:37 2016

@author: Sandip Baishnab
"""

#importing modules
from sklearn.feature_extraction.text import CountVectorizer

class feature_class():
    
    def feature_function(self, train_data,test_data):
        cv=CountVectorizer(analyzer="word",ngram_range=(1,2),max_features=10,max_df=1.0,min_df=1)
        ft=cv.fit(train_data)
        feat=ft.transform(train_data)
        features_train=feat.toarray()
        features_test=ft.transform(test_data)
        features_test=features_test.toarray()
        return (features_train,features_test)        
        