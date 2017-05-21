# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 03:28:45 2017

@author: SAMI
"""

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

g = 0.25
def fy(t):
    return g*np.exp(-g*t)
M = 500 #OBS: con M mas grande se ve mejor
x = uniform.rvs(size=M) #numeros aleatorios con distribucion uniforme
y = -(1/g)*np.log(1-x)
L = 40
bines = np.linspace(0,L,70)

fig, ax = plt.subplots(1, 1)
#plt.plot(x,y,'r-')
n, bins, patches = ax.hist(y, bins = bines, range=[0,L], color = 'c', alpha=0.5, normed=True)
plt.plot(bines,fy(bines), 'r-', lw = 3, alpha = 0.7, label = 'Exponencial')
ax.set_xlim([0,L])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Histograma')
ax.grid()
plt.legend(loc=1, borderaxespad=0.)
fig.tight_layout()
plt.show()
