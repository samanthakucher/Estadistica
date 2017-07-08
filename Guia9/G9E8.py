# -*- coding: utf-8 -*-
"""
Created on Sat Jul 08 03:38:19 2017

@author: SAMI
"""

import numpy as np
from scipy.stats import ks_2samp, ranksums
from matplotlib import pyplot as plt

#8)
A = np.array([ 81, 82, 87, 93, 102, 104, 108, 112, 116, 122, 125, 131, 131, 133, 134, 139, 139, 142, 144, 146, 152, 156, 182, 202, 206, 216, 226, 270], dtype=float)
B= np.array([ 50, 64, 68, 76, 79, 83, 88, 96, 97, 98, 99, 103, 105, 107, 113, 114, 115, 126, 128, 130, 132, 138, 150, 169, 171 ], dtype=float)
Aord, Bord  = np.sort(A), np.sort(B)
x = np.linspace(0,280,500)
#Test de Kolmogorov Smirnov
def S(V,t):
    for i in range(0,len(V)-1):   
        if t<V[0]:
            S = 0
        elif t>V[len(V)-1]:
            S =1
        elif (V[i]<=t and t<V[i+1]):
            S = (i+1.00)/float(len(V))
    return S
    
SA, SB = [], []
for xi in x:
    SA.append(S(Aord, xi)) 
    SB.append(S(Bord, xi))

AvsB = []
for i in range(0,len(x)):
    AvsB.append(abs(SA[i]-SB[i]))

T_AvsB= np.max(AvsB)
indiceAB = np.where(AvsB == T_AvsB)
iAB = int(np.mean(indiceAB))

plt.plot(x, SA, 'g-', label = 'SA')
plt.plot(x, SB, 'b-', label = 'SB')
plt.axvline(x=x[iAB], ymin=SA[iAB], ymax = SB[iAB], linewidth=2, color='m', label = 'dif AB')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

testAB, pAB = ks_2samp(A,B) #esto hace el test directo, me da T y el pvalue (a 2 colas)
#Resultados
alpha = 0.05
if pAB>=alpha:
    print('KS: A y B provienen de la misma distribucion, con alfa=5%')
else:
    print('KS: A y B no provienen de la misma distribucion, con alfa=5%')
#Obs: 1-pAB = 0.98 --> Nivel de confianza en el resultado del test???
#Hasta donde puedo mover el alfa y todavia no rechazar

#test de Wilcoxon
N, M = len(B), len(A)
lista = sorted(np.concatenate((A,B))) #Obs: no hay numeros repetidos
rango = 0
i = 1
while i<=len(lista):
    if lista[i-1] in B:
        rango = i + rango #porque empieza a contar desde 0
    else:
        rango = rango
    i = i+1

j = 1
wmin = 0
while j<=N:
    wmin = j + wmin
    j = j+1
    
k = M+1
wmax = 0
while k<=(M+N):
    wmax = k + wmax
    k = k+1

Tw, pvalueW = ranksums(A,B) #me da el pvalue a 2 colas
if pvalueW>=alpha:
    print('W: A y B provienen de la misma distribucion, con alfa=5%')
else:
    print('W: A y B no provienen de la misma distribucion, con alfa=5%')
#1-pvalueW = 0.99
