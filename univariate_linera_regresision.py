# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:35:27 2021

@author: mohammed batis - 18511160002
"""
import matplotlib.pyplot as plt
import numpy as np
x=np.array([41,45,51,52,59,62,69,72,78,80,90,92,98,103])
y=np.array([28,39,41,44,43,50,51,57,63,66,70,76,80,81])
xave=np.average(x)
print(xave)
yave=np.average(y)
xy=x*y
xyave=np.average(xy)

x2=x*x;
x2ave=np.average(x2) 

b=(xave*yave-xyave)/(xave*xave-x2ave)
a=yave-b*xave

##print(a,b)
x=np.array(x)
y=np.array(y)
y1=a+b*x
predict_y=y1[:,None]
print("PredictY=",predict_y)
print("*"*20)
sq_erros= pow(y1-y,2)[:, None]
mean_sq_erros = sum(sq_erros)/len(sq_erros)
print("SQUARE ERRORS\n=",sq_erros)
print("MEAN SQURE ERROS = ",mean_sq_erros)
##print(y1)
plt.scatter(x,y)
plt.plot(x,y1,"r.-")


