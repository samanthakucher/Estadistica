# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 01:08:47 2017

@author: SAMI
"""

import numpy as np
import random as rd
from matplotlib import pyplot as plt
from scipy.stats import poisson
from datetime import datetime
rd.seed(datetime.now())
plt.ion()

#EXPERIMENTO
mu = 15
prob = 15.00/1000.00 #input("Probabilidad = ") 
M = 1000 #cantidad de dt's que suman un Deltat
intentos = np.arange(1,M+1,1)
T = 1000 #input("Cantidad de iteraciones  = ") 
exitos_vector=[]
fracasos_vector=[]
for i in range(0,T):
    exitos = 0
    fracasos = 0
    for n in range(0,M):
        num = rd.random()
        if num<=prob:
            exitos = exitos+1 #cantidad de numeros abajo de prob
        else:
            fracasos = fracasos+1 #cantiadd de numeros arriba de prob
    exitos_vector.append(exitos) #voy juntando la cantidad de numeros que salen abajo de p en cada experimento
    fracasos_vector.append(fracasos)

x = np.arange(0,30) #eje x del histograma
bines = 30
#GRAFICOS  
fig, ax = plt.subplots(1, 1)
#ax.hist(exitos_vector,bins = 30,range=[0,30], color = 'r', alpha=0.5, normed=True)
n, bins, patches = ax.hist(exitos_vector,bins = bines,range=[0,bines], color = 'c', alpha=0.5, normed=True)  
#plt.plot(intentos,exitos_esperados_b, 'r-', label = "Distribucion binomial")
#plt.plot(intentos,exitos_esperados_p, 'g-', label = "Poisson")
ax.plot(x, poisson.pmf(x, mu), 'bo', ms=8, label='poisson')
ax.vlines(x, 0, poisson.pmf(x, mu), colors='b', lw=5, alpha=0.5)
plt.xticks(range(0,bines,5))
plt.legend(loc=2, borderaxespad=0.)
ax.set_xlabel('Numero de fotones detectados')
ax.set_ylabel('Cantidad de ocurrencias (normalizada)')
ax.set_title('Histograma')
fig.tight_layout()
plt.show()
