# -*- coding: utf-8 -*-
"""
Created on Mon May 15 02:43:26 2017

@author: SAMI
"""

import numpy as np
from matplotlib import pyplot as plt

#Datos
x1 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
x2 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
x3 = [10.0, 8.0, 13.0, 9.0, 11.0, 14.0, 6.0, 4.0, 12.0, 7.0, 5.0]
y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
x4 = [8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 8.0, 19.0, 8.0, 8.0, 8.0] 
y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

#Promedios
x1m, x1v = np.mean(x1),  np.var(x1)
y1m, y1v = np.mean(y1),  np.var(y1)
x2m, x2v = np.mean(x2),  np.var(x2)
y2m, y2v = np.mean(y2),  np.var(y2)
x3m, x3v = np.mean(x3),  np.var(x3)
y3m, y3v = np.mean(y3),  np.var(y3)
x4m, x4v = np.mean(x4),  np.var(x4)
y4m, y4v = np.mean(y4),  np.var(y4)

print(" x1 = ({}+-{}), y1 = ({}+-{}) \n x2 = ({}+-{}), y2 = ({}+-{}) \n x3 = ({}+-{}), y3 = ({}+-{}) \n x4 = ({}+-{}), y4 = ({}+-{}) \n ").format(round(x1m,2), round(x1v,2), round(y1m,2), round(y1v,2), round(x2m,2), round(x2v,2), round(y2m,2), round(y2v,2), round(x3m,2), round(x3v,2), round(y3m,2), round(y3v,2), round(x4m,2), round(x4v,2), round(y4m,2), round(y4v,2))

#print("Los valores medios son: \n x1m = {} \n y2m = {} \n x2m = {} \n y2m = {} \n x3m = {} \n y3m = {} \n x4m = {} \n y4m = {} \n".format(x1m, y1m, x2m, y2m, x3m, y3m, x4m, y4m))
#print("Las varianzas son: \n x1v = {} \n y2v = {} \n x2v = {} \n y2v = {} \n x3v = {} \n y3v = {} \n x4v = {} \n y4v = {} \n".format(x1v, y1v, x2v, y2v, x3v, y3v, x4v, y4v))

#Correlacion
cov1 = np.cov(x1)
ro1 = np.cov(x1, y1)/(np.sqrt(x1v)*np.sqrt(y1v))
print(cov1, x1v) #deberian dar igual
#print ("Correlación  \n {}").format(ro1)

#Graficos
fig,sub = plt.subplots(4, figsize =(9,9))
fig.subplots_adjust(hspace=0.9)
sub[0].plot(x1,y1, 'ro', label = '1')
sub[0].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[0].set_xlabel('x1')
sub[0].set_ylabel('y1')
sub[0].grid()
sub[1].plot(x2, y2, 'go', label ='2')
sub[1].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[1].set_xlabel('x2')
sub[1].set_ylabel('y2')
sub[1].grid()
sub[2].plot(x3,y3,'mo', label = '3')
sub[2].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[2].set_xlabel('x3')
sub[2].set_ylabel('y3')
sub[2].grid()
sub[3].plot(x4, y4, 'co', label = '4')
sub[3].legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
sub[3].set_xlabel('x4')
sub[3].set_ylabel('y4')
sub[3].grid()
