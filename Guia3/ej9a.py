# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 00:32:12 2017

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

fig, ax = plt.subplots(1, 1)
lim = 15
x = np.arange(-lim,lim,0.01)
gamma = (0.75*np.sqrt(2*np.pi))/np.pi
#a ojo = 0.59911
ax.plot(x, cauchy.pdf(x,0,gamma), 'r-', lw=1, alpha=0.6, label='Cauchy')
ax.plot(x, norm.pdf(x, 0,0.75), 'g-', lw=1, alpha=0.6, label='Gaussiana')
maximo = norm.pdf(0,0,0.75)
print(gamma)
plt.xticks(range(-lim,lim,5))
ax.set_xlabel('x') #variable aleatoria
ax.set_ylabel('f(x)') #densidad de probabilidad
ax.set_title('Comparacion')
ax.grid()
plt.legend(loc=2, borderaxespad=0.)
fig.tight_layout()
plt.show()
