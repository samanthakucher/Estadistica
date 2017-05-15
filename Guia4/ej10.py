# -*- coding: utf-8 -*-
"""
Created on Mon May 15 02:43:26 2017

@author: SAMI
"""

import numpy as np

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
x1m = np.mean(x1)
y1m = np.mean(y1)
x2m = np.mean(x2)
y2m = np.mean(y2)
x3m = np.mean(x3)
y3m = np.mean(y3)
x4m = np.mean(x4)
y4m = np.mean(y4)

print("Los valores medios son: \n x1m = {} \n y2m = {} \n x2m = {} \n y2m = {} \n x3m = {} \n y3m = {} \n x4m = {} \n y4m = {} \n".format(x1m, y1m, x2m, y2m, x3m, y3m, x4m, y4m))

#Varianzas
x1v = np.var(x1)
y1v = np.var(y1)
x2v = np.var(x2)
y2v = np.var(y2)
x3v = np.var(x3)
y3v = np.var(y3)
x4v = np.var(x4)
y4v = np.var(y4)

print("Las varianzas son: \n x1v = {} \n y2v = {} \n x2v = {} \n y2v = {} \n x3v = {} \n y3v = {} \n x4v = {} \n y4v = {} \n".format(x1v, y1v, x2v, y2v, x3v, y3v, x4v, y4v))

#Correlacion
ro1 = np.cov(x1, y1)/(np.sqrt(x1v)*np.sqrt(y1v))
print (ro1)
