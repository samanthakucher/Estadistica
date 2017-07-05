import numpy as np
from scipy.stats import binom, poisson, norm
from matplotlib import pyplot as plt

#a) Binomial
x1 = np.arange(1,6) #para graficar la primera binomial
xpdf1 = np.linspace(0,6,100) #para graficar la primera gaussiana
x2 = np.arange(1,30) #segunda binomial
xpdf2 = np.linspace(0,30,100) #segunda gaussiana
mu1, mu2, sigma1, sigma2 = 5.00*0.2, 30.00*0.4, np.sqrt(5.00*0.2*0.8), np.sqrt(30.00*0.4*0.6) #de las gaussianas

#b) Poisson
x3, xpdf3  = np.arange(0,15), np.linspace(0,15,500)
x4, xpdf4 = np.arange(0,30), np.linspace(0,30,500)
x5, xpdf5 = np.arange(0,70), np.linspace(0,70,500)
mu3, mu4, mu5, sigma3, sigma4, sigma5 = 4, 10, 40, np.sqrt(4), np.sqrt(10), np.sqrt(40) #de las gaussianas

#Graficos
fig = plt.figure()

ax1 = fig.add_subplot(2, 3, 1)
ax2 = fig.add_subplot(2, 3, 2)
ax3 = fig.add_subplot(2, 3, 4)
ax4 = fig.add_subplot(2, 3, 5)
ax5 = fig.add_subplot(2, 3, 6)

ax1.plot(x1,binom.pmf(x1,5.00,0.20), 'bo', label = 'B(5,0.2)')
ax1.plot(xpdf1, norm.pdf(xpdf1,mu1,sigma1), 'm-', label ='Gaussiana' )
ax1.legend(loc=1, borderaxespad=0.)
ax1.set_xlabel('k')
ax1.set_ylabel('B(k)')
#ax1.set_title('Grafico 1')
ax1.grid()

ax2.plot(x2,binom.pmf(x2,30.00,0.40), 'bo', label = 'B(30,0.4)')
ax2.plot(xpdf2,norm.pdf(xpdf2,mu2,sigma2), 'm-', label ='Gaussiana')
ax2.set_xlabel('k')
ax2.set_ylabel('B(k)')
#ax2.set_title('Grafico 2')
ax2.legend(loc=1, borderaxespad=0.)
ax2.grid()

ax3.plot(x3,poisson.pmf(x3,4), 'bo', label = 'P(4)')
ax3.plot(xpdf3, norm.pdf(xpdf3,mu3, sigma3), 'm-', label ='Gaussiana' )
ax3.legend(loc=1, borderaxespad=0.)
ax3.set_xlabel('k')
ax3.set_ylabel('P(k)')
#ax3.set_title('Grafico 3')
ax3.grid()

ax4.plot(x4,poisson.pmf(x4,10), 'bo', label = 'P(10)')
ax4.plot(xpdf4, norm.pdf(xpdf4,mu4, sigma4), 'm-', label ='Gaussiana' )
ax4.legend(loc=1, borderaxespad=0.)
ax4.set_xlabel('k')
ax4.set_ylabel('P(k)')
#ax4.set_title('Grafico 4')
ax4.grid()

ax5.plot(x5,poisson.pmf(x5,40), 'bo', label = 'P(40)')
ax5.plot(xpdf5, norm.pdf(xpdf5,mu5, sigma5), 'm-', label ='Gaussiana' )
ax5.legend(loc=1, borderaxespad=0.)
ax5.set_xlabel('k')
ax5.set_ylabel('P(k)')
#ax5.set_title('Grafico 5')
ax5.grid()
