# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 11:37:45 2016
@author: Sandip Baishnab
"""
#importing module 
import nltk
import re
from nltk import word_tokenize
from nltk.corpus import stopwords

#preprocess
class clean():
    #functions for preprocessing    
    def preprocess(self,data):
	    #auxiliary array
		aux=[]
        #tokenization and lower case conversion
		tokens=nltk.word_tokenize(data.lower())
		#removing all except letters
		rm_all =[re.sub("[^a-zA-Z]"," ",x) for x in tokens]
		#removing stopwords
		rm_stopw=[x for x in rm_all if x not in stopwords.words("english")]
		#removing empty string
		rm_n=filter(lambda x: x!=(" " or "  "),rm_stopw)
		#making sentence
		aux.append(" ".join(rm_n))
		#returning sentence
		return aux
		
               
