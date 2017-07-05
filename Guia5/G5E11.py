import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

def cuadradosmin(x,y): #solo con error en y
    delta = len(y)*np.sum(x**2) - np.sum(x)**2
    a1 = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/delta
    a2 = (len(y)*np.sum(x*y) - np.sum(x)*np.sum(y))/delta
    return [a1, a2, delta]

def generador(a1,a2):
    y = []
    for x in x_dat:
        yi = norm.rvs(a1+a2*x, sigmay)
        y.append(yi)
    return y  
    
x_dat = [2.00, 2.10, 2.20, 2.30, 2.40, 2.50, 2.60, 2.70, 2.80, 2.90, 3.00]
y_dat = [2.78, 3.29, 3.29, 3.33, 3.23, 3.69, 3.46, 3.87, 3.62, 3.40, 3.99]
sigmay = 0.3 
x_array, y_array = np.array(x_dat), np.array(y_dat) #los convierto en array para poder usarlos en la funcion
parametros = cuadradosmin(x_array,y_array)
a1, a2 = parametros[0], parametros[1]
var_a1 = ((sigmay**2)/parametros[2])*np.sum(x_array**2)
var_a2 = ((sigmay**2)/parametros[2])*len(y_array)
cov_a1a2 = -((sigmay**2)/parametros[2])*np.sum(x_array)
ya_esperado = a1 + a2*0.50
sigmaya_esperado = np.sqrt(var_a1 + (0.50**2)*var_a2 + 2*0.50*cov_a1a2)

ya_vector = []
a1_vector = []
a2_vector = []
for i in range(0,1000):
    ygenerado = generador(a1,a2)
    parametros = cuadradosmin(np.array(x_dat),np.array(ygenerado))
    ya  = parametros[0] + parametros[1]*0.50 #(xa=0.50)
    a1_vector.append(parametros[0])
    a2_vector.append(parametros[1])
    ya_vector.append(ya)
    
puntosb = np.linspace(0,4.5,100) #puntos para graficar la distribución
binesb = np.linspace(0,4.5,50)
numerob, binsb = np.histogram(ya_vector, bins = binesb) 
errorb = np.sqrt(numerob) / (np.diff(binsb)* np.sum(numerob)) #error poissoniano (normalizado)
numerob = numerob / (np.diff(binsb) * np.sum(numerob)) #Normalizo a 1

puntosa1 = np.linspace(0,3.5,100) #puntos para graficar la distribución
binesa1 = np.linspace(0,3.5,35)
numeroa1, binsa1 = np.histogram(a1_vector, bins = binesa1) 
errora1 = np.sqrt(numeroa1) / (np.diff(binsa1)* np.sum(numeroa1)) #error poissoniano (normalizado)
numeroa1 = numeroa1 / (np.diff(binsa1) * np.sum(numeroa1)) #Normalizo a 1

puntosa2 = np.linspace(0,3.5,100) #puntos para graficar la distribución
binesa2 = np.linspace(0,3.5,50)
numeroa2, binsa2 = np.histogram(a2_vector, bins = binesa2) 
errora2 = np.sqrt(numeroa2) / (np.diff(binsa2)* np.sum(numeroa2)) #error poissoniano (normalizado)
numeroa2 = numeroa2 / (np.diff(binsa2) * np.sum(numeroa2)) #Normalizo a 1

fig = plt.figure()
ax1 = fig.add_subplot(1, 3, 1)
ax2 = fig.add_subplot(1, 3, 2)
ax3 = fig.add_subplot(1, 3, 3)

ax1.bar(binsb[:-1], numerob, width = np.diff(binsb), yerr = errorb, ecolor="b", color='c', alpha=0.5)
ax1.plot(puntosb,norm.pdf(puntosb, ya_esperado,sigmaya_esperado), 'm-', ms=8, label='Gaussiana', alpha=0.9)
ax1.legend(loc=1, borderaxespad=0.)
ax1.set_xlabel('Valor de y obtenido')
ax1.set_ylabel('Numero de ocurrencias (normalizado)')
ax1.grid()

ax2.bar(binsa1[:-1], numeroa1, width = np.diff(binsa1), yerr = errora1, ecolor="b", color='c', alpha=0.5)
ax2.plot(puntosa1,norm.pdf(puntosa1, a1,np.sqrt(var_a1)), 'm-', ms=8, label='Gaussiana', alpha=0.9)
ax2.legend(loc=1, borderaxespad=0.)
ax2.set_xlim([0,3.5])
ax2.set_xlabel('Valor de a1 obtenido')
ax2.set_ylabel('Numero de ocurrencias (normalizado)')
ax2.grid()

ax3.bar(binsa2[:-1], numeroa2, width = np.diff(binsa2), yerr = errora2, ecolor="b", color='c', alpha=0.5)
ax3.plot(puntosa2,norm.pdf(puntosa2, a2,np.sqrt(var_a2)), 'm-', ms=8, label='Gaussiana', alpha=0.9)
ax3.legend(loc=1, borderaxespad=0.)
ax3.set_xlim([0,2])
ax3.set_xlabel('Valor de a2 obtenido')
ax3.set_ylabel('Numero de ocurrencias (normalizado)')
ax3.grid()
