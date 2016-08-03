# -*- coding: utf-8 -*-
"""
Created on Tue Aug  2 13:43:37 2016

@author: haicen
"""

import hashlib


def compressor(in_var, out):
    i=0
    j=0
    
    while i<len(in_var):
       
    
        out[j] = (in_var[i] + in_var[i+1]) % 62;
        if (out[j] < 10):
            out[j] += 48
        elif (out[j] < 36):
          out[j] += 55;
        else:
            out[j] += 61        

        i=i+2
        j=j+1
        

m = hashlib.md5()
m.update("123456".encode("ascii"))

s=m.digest()
print(type(s))
crypt=[]
for b in s:
    crypt.append(b)




out2=['']*8
compressor(crypt,out2)
result=''.join([chr(a) for a in out2])
print(result)
