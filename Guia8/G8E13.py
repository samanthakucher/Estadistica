import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def f(t, a1, a2, a3, a4, a5):
    funcion = a1+a2*np.exp(-t/a4)+a3*np.exp(-t/a5)
    return funcion

datos = np.loadtxt("Datos_G8P13.txt")
t, y = np.array(datos[:,0], dtype=float), np.array(datos[:,1], dtype=float)
n = len(t)



def cuadradosmin(t, y, a4, a5):
    #Defino la matriz A
    A = np.zeros((n,3))
    A[:,0] = 1
    for i in range(0, n):
        A[i,1] = np.exp(-t[i]/a4)
        A[i,2] = np.exp(-t[i]/a5)
    #Defino la matriz V
    V = np.zeros((n,n))
    for i in range(0,n):
        V[i,i] = y[i] #es asi?
    #Cuadrados minimos lineal
    Am, Vm, ym = np.matrix(A), np.matrix(V), np.matrix(y)
    At, Vi, yt = Am.getT(), Vm.getI(), ym.getT()
    mult = At*Vi*Am
    Cov_param_a = mult.getI()
    param_a = Cov_param_a*At*Vi*yt
    a1, a2, a3 = float(param_a[0]), float(param_a[1]), float(param_a[2])
    return a1, a2, a3

    
#a) Ajuste lineal
a4_a, a5_a = 209.69, 34.244
a1_a, a2_a, a3_a = cuadradosmin(t, y, a4_a, a5_a)

#b) Ajuste no lineal 
param_b, cov_b = curve_fit(f, t, y, p0=None, sigma=y)
print(cov_b) #matriz de covarianza
funcion_b = np.vectorize(f)
a1_b, a2_b, a3_b, a4_b, a5_b = param_b

#c) Elipses

    
chi2min = np.sum(((y-funcion_b(t, a1_b, a2_b, a3_b, a4_b, a5_b))**2)/y)
delta = 1
elvalor =chi2min+delta
tol = 0.1
L = 100
a4_valores = np.linspace(160,260,L)
a5_valores = np.linspace(31,37.5,L)

def elipse_punteada(valor, tolerancia):
    elipse = []
    for i in a4_valores:
        for j in a5_valores:
            def funcion_lineal(t, a1, a2, a3): #lineal en los parametros, porque a4 y a5 son dato
                funcion = a1+a2*np.exp(-t/i)+a3*np.exp(-t/j)
                return funcion
            minimizo, pcov = curve_fit(funcion_lineal, t, y, p0=None, sigma=y)
            a1_c, a2_c, a3_c = minimizo
            chi2aca = np.sum(((y-funcion_lineal(t, a1_c, a2_c, a3_c))**2)/y)
            estevalor = chi2aca+delta
            #if abs(estevalor-elvalor)<=tol:
            elipse.append(funcion_lineal(t, a1_c, a2_c, a3_c)-funcion_lineal(t, a1_a, a2_b, a3_b))
            m = len(elipse)
    #elipse1 = np.reshape(np.array(elipse), (L,L))
    return elipse

elipse_1 = elipse_punteada(elvalor, tol)



puntos = np.linspace(0,900,1000)
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
#a)
ax1.set_yscale("log")
ax1.plot(puntos,f(puntos,a1_a, a2_a, a3_a, a4_a, a5_a), 'm-', lw=2, label = 'Ajuste lineal') #item a
ax1.errorbar(t,y, fmt = 'bo', yerr = np.sqrt(y), label ='Datos')
ax1.set_xlabel('t')
ax1.set_ylabel('y')
ax1.legend(loc=1, borderaxespad=0.)
ax1.grid(which="both")
#b)
ax2.set_yscale("log")
ax2.plot(puntos, funcion_b(puntos, a1_b, a2_b, a3_b, a4_b, a5_b), 'm-', lw=2, label='Ajuste no lienal') #item b
ax2.errorbar(t,y, fmt = 'bo', yerr = np.sqrt(y), label ='Datos')
ax2.set_xlabel('t')
ax2.set_ylabel('y')
ax2.legend(loc=1, borderaxespad=0.)
ax2.grid(which="both")
#c)

ax3.contour(a5_valores, a4_valores, elipse_1)
#ax2.set_yscale("log")
#ax3.plot(ea5_c1, ea4_c1, 'g-')
#ax2.errorbar(t,y, fmt = 'bo', yerr = np.sqrt(y), label ='Datos')
ax3.set_xlabel('a5')
ax3.set_ylabel('a4')
ax3.legend(loc=1, borderaxespad=0.)
ax3.grid(which="both")
