# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 02:14:19 2017

@author: SAMI
"""

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt


def fy(t):
    return 1.00/t
M = 10000000
x = uniform.rvs(size=M) #numeros aleatorios con distribucion uniforme
y = np.exp(x)
bines = np.linspace(1,np.e,80)

fig, ax = plt.subplots(1, 1)
#plt.plot(x,y,'r-')
n, bins, patches = ax.hist(y, bins = bines, range=[0,np.e], color = 'c', alpha=0.5, normed=True)
plt.plot(bines,fy(bines), 'r--', label = 'Distribucion 1/t')
ax.set_xlim([1,np.e])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Histograma')
ax.grid()
plt.legend(loc=1, borderaxespad=0.)
fig.tight_layout()
plt.show()
