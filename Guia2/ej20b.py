# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 20:54:44 2017

@author: SAMI
"""

import numpy as np
import math as m
import random as rd
from matplotlib import pyplot as plt
from datetime import datetime
rd.seed(datetime.now())
plt.ion()

#DEFINICIONES
def combinatoria(n,k):
	return float(m.factorial(n)/(m.factorial(n-k)*m.factorial(k)))
def binomial(k, n, p):
	#Variable aleatoria = k (cantidad de exitos)
	#p = cte
	return combinatoria(n,k)*(p**k)*((1-p)**(n-k))
def poisson(k,mu):
	#k exitos, mu=n*p
	return (m.exp(-mu)*(mu**k))/m.factorial(k)
 
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
 
#TEORICO
exitos_esperados_b = []
exitos_esperados_p = []
for i in range(1,M+1):
    exito_i_b = binomial(i,M,prob)
    exito_i_p = poisson(i, prob*M)
    exitos_esperados_b.append(exito_i_b)
    exitos_esperados_p.append(exito_i_p)

#GRAFICOS  

plt.hist(exitos_vector,bins = M,range=[0,M], color = 'c', alpha=0.5, normed=True)  
plt.plot(intentos,exitos_esperados_b, 'r-', label = "Distribucion binomial")
plt.plot(intentos,exitos_esperados_p, 'g-', label = "Poisson")
plt.xticks(range(0,M))
plt.legend(loc=2, borderaxespad=0.)
plt.title('Histograma')
plt.show()

'''
fig, ax = plt.subplots()

# Histograma
n, bins, patches = ax.hist(exitos_vector,bins = M,range=[0,M], color = 'c', alpha=0.5, normed=True)

# Distribucion binomial
ax.plot(intentos, exitos_esperados, 'r-')
ax.set_xlabel('Numero de fotones detectados')
ax.set_ylabel('Cantidad de ocurrencias (normalizada)')
ax.set_title('Histograma')

# Ajusta el espaciado
fig.tight_layout()
plt.show()
'''
