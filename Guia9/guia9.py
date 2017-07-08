# -*- coding: utf-8 -*-
"""
Created on Thu Jul 06 13:12:04 2017

@author: SAMI
"""

import numpy as np
from scipy.stats import chi2, ks_2samp
from scipy.special import factorial
from matplotlib import pyplot as plt

'''
#2)
masa = np.array([80.482, 80.423, 80.38, 80.61, 80.41])
sigma = np.array([0.091, 0.112, 0.12, 0.15, 0.18])
prom = np.average(masa, weights=1.00/sigma) #promedio pesado
S = np.sum(((masa-prom)/sigma)**2) #me da distinto a clase
pvalue = chi2.sf(x = S, df=4, loc=0, scale=1)

#4)
A = [0.80, 0.90, 1.05, 1.20, 1.30, 1.30] #ojo que hay dos iguales
B = [1.00, 1.40, 1.70, 1.90, 2.30]
N, M = len(B), len(A)
lista = sorted(np.concatenate((A,B)))
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

#5)
A = np.array([6.4, 6.8, 7.2, 8.3, 8.4, 9.1, 9.4, 9.7])
B = np.array([2.5, 3.7, 4.9, 5.4, 5.9, 8.1, 8.2])
C = np.array([1.3, 4.1, 4.9, 5.2, 5.5, 8.2])
Aord, Bord, Cord  = np.sort(A), np.sort(B), np.sort(C)
x = np.linspace(0,10,500)
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
    
SA, SB, SC = [], [], []
for xi in x:
    SA.append(S(Aord, xi)) 
    SB.append(S(Bord, xi))  
    SC.append(S(Cord, xi))  
    
AvsB, BvsC, CvsA = [], [], []
for i in range(0,len(x)):
    AvsB.append(abs(SA[i]-SB[i]))
    BvsC.append(abs(SB[i]-SC[i]))
    CvsA.append(abs(SC[i]-SA[i]))
    
T_AvsB, T_BvsC, T_CvsA = np.max(AvsB), np.max(BvsC), np.max(CvsA)
indiceAB = np.where(AvsB == T_AvsB)
indiceBC = np.where(BvsC == T_BvsC)
indiceCA = np.where(CvsA == T_CvsA)
iAB, iBC, iCA = int(np.mean(indiceAB)), int(np.mean(indiceBC)), int(np.mean(indiceCA))

plt.plot(x, SA, 'g-', label = 'SA')
plt.plot(x, SB, 'b-', label = 'SB')
plt.plot(x, SC, 'r-', label = 'SC')
plt.axvline(x=x[iAB], ymin=SA[iAB], ymax = SB[iAB], linewidth=2, color='m', label = 'dif AB')
plt.axvline(x=x[iBC], ymin=SB[iBC], ymax = SC[iBC], linewidth=2, color='c', label = 'dif BC')
plt.axvline(x=x[iCA], ymin=SA[iCA], ymax = SC[iCA], linewidth=2, color='k', label = 'dif CA')
plt.xticks(range(0,10))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

testAB, pAB = ks_2samp(A,B) #esto hace el test directo, me da T y el pvalue (a 2 colas)
testBC, pBC = ks_2samp(B,C) #lo uso solamente para tener el pvalue
testCA, pCA = ks_2samp(C,A)
#Resultados
alpha = 0.05
if pAB>=alpha:
    print('A y B provienen de la misma distribucion, con alfa=5%')
else:
    print('A y B no provienen de la misma distribucion, con alfa=5%')
if pBC>=alpha:
    print('B y C provienen de la misma distribucion, con alfa=5%')
else:
    print('B y C no provienen de la misma distribucion, con alfa=5%')
if pCA>=alpha:
    print('A y C provienen de la misma distribucion, con alfa=5%')
else:
    print('A y C no provienen de la misma distribucion, con alfa=5%')

#6)

def combinatoria(n,k):
	return float(factorial(n, exact=True)/(factorial(n-k, exact=True)*factorial(k, exact=True)))
 
def hipergeometrica(k, t, n, q):
	#p =! cte
	#k exitos, t cosas en total, q cosas que quiero, n intentos
	return (combinatoria(q,k)*combinatoria(t-q,n-k))/combinatoria(t,n)
 
a, b, c, d = np.arange(0,9), np.fliplr([np.arange(0,9)])[0], np.fliplr([np.arange(1,10)])[0], np.arange(3,12)
p = np.zeros(9)
# total = 20, a+b = 8 (total y), a+c = 9 (total x)
for i in range(0,9):
    p[i] = hipergeometrica(a[i], 20, 9, 8)
pceleste = np.concatenate((p[:6], np.zeros(3)))
pvalue = p[6]+p[7]+p[8]
prosa = np.concatenate((np.zeros(6), p[6:]))
plt.bar(a, pceleste, color='c', alpha = 0.5)
plt.bar(a, prosa, color='m', alpha = 0.5, label = 'pvalue')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
if pvalue<=0.05:
    print('Rechazamos la hipotesis de que X e y son independientes, con alfa=5%')
else:
    print('Aceptamos H0')
'''
