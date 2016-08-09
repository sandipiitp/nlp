# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 02:23:23 2016

@author: Sandip Baishnab
"""

#import modules
from sklearn.svm import SVC

class classification:
    
    def model_svm(self,features,label,test):
        clf=SVC(kernel="linear")
        clf.fit(features,label)
        result=clf.predict(test)
        return result
        