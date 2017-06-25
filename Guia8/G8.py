# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:49:38 2017

@author: SAMI
"""

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import t, chi2

'''
#1)
y = np.linspace(0,10,100)
tita1 = y
tita2 = 1.58*y

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('Cinturon de confianza 90% CL para y~U[0,tita]')
ax1.plot(y, tita1,'k--', y, tita2,'k--')
ax1.fill_between(y,tita2, tita1, facecolor='m', alpha = 0.5, label = '90%')
ax1.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

#2)
x = [128, 281, 291, 238, 155, 148, 154, 232, 316, 96, 146, 151, 100, 213, 208, 157, 48, 217]
prom = np.mean(x)
s2 = np.sum((x-prom)**2)/(len(x)-1)
a = t.interval(alpha = 0.95, df = 17, loc=0, scale=1)
inf, sup = prom+a[0]*np.sqrt(s2/len(x)), prom+a[1]*np.sqrt(s2/len(x))
print(a[1])
print(inf, sup)

#3)
x = [ 1002, 1000, 997, 1001, 1001, 999, 998, 999, 1000, 1003]
prom = np.mean(x)
N  =len(x)
s2 = np.sum((x-prom)**2)/(N-1)
a = chi2.interval(alpha=0.95, df=(N-1), loc=0, scale=1)
inf, sup = s2*(N-1)/a[1], s2*(N-1)/a[0]  #intervalo 95% CL centrado
a1 = chi2.ppf(q=0.05, df=(N-1), loc=0, scale=1)
lim = s2*(N-1)/a1 #cota superior

#5)
x = [ 4.2, 1.0, 0.1, 2.0, 1.5]
N = len(x)
a = chi2.ppf(q=0.90, df=2*N, loc=0, scale=1)
lim = a/(2*np.sum(x)) #cota superior

#6)
P = np.array([18.71, 2.79, 13.61, 12.08, 1.89])
F = np.array([4854.00, 2586.00, 3752.00, 3753.00, 2605.00])
ti = np.array([200.00, 100.00, 150.00, 150.00, 100.00]) #t se llama la t-student
tc, Fc = 100.00, 1021.00
B = []
sigmab2 = []
for i in range(0,5):
    B.append((F[i])/(ti[i])-Fc/tc)
    sigmab2.append((F[i])/((ti[i])**2)+Fc/(tc**2))
A = np.matrix([[1, m.log(P[0],10)],[1, m.log(P[1],10)], [1, m.log(P[2],10)], [1, m.log(P[3],10)], [1, m.log(P[4],10)] ])
At = A.getT()
cb = Fc/(tc**2) #covarianza de B
V = np.matrix([[sigmab2[0], cb, cb, cb, cb], [cb, sigmab2[1], cb, cb, cb], [cb, cb, sigmab2[2], cb, cb], [cb, cb, cb, sigmab2[3], cb], [cb, cb, cb, cb, sigmab2[4]]])
Vi = V.getI()
mult = At*Vi*A
Cov = mult.getI()
Bm = np.matrix(B)
Bt = Bm.getT()
tita = Cov*At*Vi*Bt
alfa, beta = tita[1], tita[0]
ealfa, ebeta = np.sqrt(Cov[0,0]), np.sqrt(Cov[1,1])
cab = Cov[0,1]
print(alfa, ealfa, beta, ebeta, cab)

#8)
x = np.linspace(0,0.01,500)
alfa, betanum, n, k = 1.00, 1.00, 12341.00, 50.00
alfaprima, betaprima = alfa+k, betanum+n-k
pestimado = (alfa+k)/(alfa+betanum+n)
funcion = []
for y in x:
    funcion.append(beta.pdf(x,alfaprima, betaprima))
maximo = np.max(funcion) #para dividir en las lineas
intervalo = beta.interval(alpha=0.9, a=alfaprima, b=betaprima, loc=0, scale=1)
xint = np.linspace(intervalo[0],intervalo[1],200)
plt.plot(x,beta.pdf(x,alfaprima,betaprima),'m', lw=2)
plt.plot(pestimado, beta.pdf(pestimado,alfaprima,betaprima),'go', label = 'p estimado')
for x in xint:
    plt.axvline(x, ymin=0, ymax=beta.pdf(x,alfaprima,betaprima)/700.00, color = 'c', alpha = 0.5)
plt.axvline(intervalo[0], ymin=0, ymax=beta.pdf(intervalo[0],alfaprima,betaprima)/maximo, color = 'c', label = 'intervalo 90% CL')
plt.axvline(intervalo[1], ymin=0, ymax=beta.pdf(intervalo[1],alfaprima,betaprima)/maximo, color ='c')
plt.legend(loc=1, borderaxespad=0.)
plt.xlabel('x')
plt.ylabel('Beta(51, 12292)')
plt.xticks(np.arange(0,0.01,0.001))
plt.grid()
plt.show()
'''
#10)
pminfrec = beta.ppf(q=0.1, a=9, b=2, loc=0, scale=1)
pminbayes = beta.ppf(q=0.1, a=10, b=2, loc=0, scale=1)
