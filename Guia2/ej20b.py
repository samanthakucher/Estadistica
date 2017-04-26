# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:54:44 2017

@author: SAMI
"""

import numpy as np
import random as rd
from matplotlib import pyplot as plt
from scipy.stats import binom
from datetime import datetime
rd.seed(datetime.now())
plt.ion()

#EXPERIMENTO
prob = 0.75 #input("Probabilidad = ") 
M = 15 #input("Cantidad de elementos = ") #cantidad de numeros aleatorios 
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

#GRAFICOS 
x1 = np.arange(0.5,15.5) 
fig, ax = plt.subplots(1, 1)
n, bins, patches = ax.hist(exitos_vector,bins = x1,range=[0,M], color = 'c', alpha=0.5, normed=True)
#plt.plot(intentos,exitos_esperados_b, 'r-', label = "Distribucion binomial")
#plt.plot(intentos,exitos_esperados_p, 'g-', label = "Poisson")
ax.plot(intentos, binom.pmf(intentos, M, prob), 'mo', ms=8, label='Binomial', alpha=0.9)
#ax.vlines(intentos, 0, binom.pmf(intentos, M, prob), colors='b', lw=5, alpha=0.5)
plt.xticks(range(0,M))
plt.legend(loc=2, borderaxespad=0.)
ax.set_xlabel('Numero de fotones detectados')
ax.set_ylabel('Cantidad de ocurrencias (normalizada)')
ax.set_title('Histograma')
plt.show()
