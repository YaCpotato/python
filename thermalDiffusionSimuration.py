#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  9 15:47:10 2019

@author: shoichi & secret
"""
import numpy as np
import math

column = 5
row = 5

k = 1 #熱拡散係数
h = 1 #点と点の距離
delt = 0.1#時間

x = 1-(4 * k*delt / (h*h))

y =(k*delt / (h*h))

print(x)
print(y)
T = np.zeros(column * row)
Tdual = np.zeros((column,row))
T[12] = 100

one = np.ones(column * row)
netu_kakusan_map = np.diagflat(one)



temp = np.zeros(column * 2 + 1)
temp[0] = y
temp[ math.floor((len(temp)/2)) ] = x
temp[ math.floor((len(temp)/2))-1 ] = y
temp[ math.floor((len(temp)/2))+1 ] =y
temp[-1] = y



for i in range(1,row - 1):
    for j in range(1,column - 1):
        for k in range(len(temp)):
            #pass
            netu_kakusan_map[i * column + j][((i-1) * column + j) + k] = temp[k]
        


for i in range(5):
    np.dot(netu_kakusan_map,T,T)
    print(T[0:5])
    print(T[5:10])
    print(T[10:15])
    print(T[15:20])
    print(T[20:25])
    print("")




