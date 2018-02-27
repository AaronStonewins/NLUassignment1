# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 11:44:24 2018

@author: abhishek
"""


import NLUAssignment1 as nlu
from nltk.corpus import brown
x=brown.sents()
f=open("probabilities.txt","w")
d=nlu.get_probability(x,4)[0]
f.write(str(d))




#import re
#import ast
#import random
#f=open("probabilities.txt","r")
#x=f.read()
#f.close()
#
#
#d=ast.literal_eval(x)
#init_string=str(random.sample(d,k=1)[0])
#S=re.findall(r'\w+',init_string)
#s=' '.join(S)
#s=''
#s=s+str(init_string)
#for i in range(4):
#    S=re.findall(r'\w+',s)
#    s_last=S[len(S)-1]
#    s_first=S[0]
#    if s_first=='<s>':
#        s=' '.join(S[1:len(S)])
#    if s_last=='</s>':
#        s=' '.join(S[0:len(S)-1])
#    p=-1
#    for k,v in d.items():
#        Z=re.findall(r'\w+',k)
#        Z_first=Z[0]
#        if Z_first==s_last:
#            if p==1.0:
#                if Z[len(Z)-1]=='</s>' or Z[len(Z)-1]=='<s>':
#                    Z1=Z[1:len(Z)-1]
#                else:
#                    Z1=Z[1:len(Z)]
#                break
#            elif p<v:
#                p=v
#                Z1=Z[1:len(Z)]
#    W=' '.join(Z1)
#    s=s+' '+W
#        
#print(s)     
##        
#    