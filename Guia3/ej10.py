# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 01:29:24 2017

@author: SAMI
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 02:14:19 2017

@author: SAMI
"""

import numpy as np
from scipy.stats import uniform, cauchy
import matplotlib.pyplot as plt

M = 10000
x = uniform.rvs(size=M, loc=-np.pi/2, scale=np.pi) #numeros aleatorios con distribucion uniforme
A = 0.35
B  = 0.1
y = A*np.tan(x)+B
bines = np.linspace(-1,1,80)


fig, ax = plt.subplots(1, 1)
n, bins, patches = ax.hist(y, bins = bines, color = 'c', alpha=0.3, normed=True)
plt.plot(bines,cauchy.pdf(bines, B, A), 'r--', label = 'Cauchy')
#ax.set_xlim([-1,1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.set_title('Histograma')
ax.grid()
plt.legend(loc=1, borderaxespad=0.)
fig.tight_layout()
plt.show()
