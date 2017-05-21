# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 01:17:25 2017

@author: SAMI
"""

import numpy as np
from scipy.stats import cauchy, norm
import matplotlib.pyplot as plt

# cauchy.pdf(x) = 1 / (pi * (1 + x**2))
#cauchy.pdf(x, loc, scale) == cauchy.pdf(y) / scale with y = (x - loc) / scale

# norm.pdf(x) = exp(-x**2/2)/sqrt(2*pi)
# norm.pdf(x, loc, scale) == norm.pdf(y) / scale with y = (x - loc) / scale

#ver cuentas para sacar gamma en pag. 40 hojas borrador

a = 0.5
b = 0.5
sigma1 = 0.75
sigma2 = 3

def f(x):
        return a*norm.pdf(x,0,sigma1) + b*norm.pdf(x,0,sigma2)
fig, ax = plt.subplots(1, 1)
lim = 6
x = np.arange(-lim,lim,0.01)
gamma = (np.sqrt(2*np.pi)*sigma1*sigma2)/(np.pi*(a*sigma2+b*sigma1))
#a ojo = 0.59911
ax.plot(x, cauchy.pdf(x,0,gamma), 'r-', lw=1, alpha=0.6, label='Cauchy')
ax.plot(x, f(x), 'g-', lw=1, alpha=0.6, label='Gaussiana')
maximo = norm.pdf(0,0,0.75)
print(gamma)
plt.xticks(range(-lim,lim,1))
ax.set_xlabel('x') #variable aleatoria
ax.set_ylabel('f(x)') #densidad de probabilidad
ax.set_title('Comparacion')
ax.grid()
plt.legend(loc=2, borderaxespad=0.)
fig.tight_layout()
plt.show()
