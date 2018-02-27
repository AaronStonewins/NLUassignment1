# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 00:14:57 2018

@author: abhishek
"""
import NLUAssignment1 as nlu
import math
from nltk.corpus import gutenberg
from nltk.corpus import brown 
import nltk


x=gutenberg.sents()
y=brown.sents()
Tr=int(math.floor(len(x)*0.95))
train=x[0:Tr]+y
test=x[Tr:len(x)]

N=4
d={};dtemp={};L1=0
for i in range(1,N+1):
    dtemp=nlu.get_probability(train,i)[0]
    if i==1:
        L1=nlu.get_probability(train,i)[1]
    for k,v in dtemp.items():
        d[k]=v
    
F=nlu.perplexity(test,d,N,L1)
print(F)


