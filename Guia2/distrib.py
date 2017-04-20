import math as m
import numpy as np

def stirling(a):
	#aprox de ln(n!) para n grande
	return a*(m.log(a))-a+0.5*(m.log(2*np.pi*a))+1/(12*a)

def combinatoria(n,k):
	return float(m.factorial(n)/(m.factorial(n-k)*m.factorial(k)))

def combinatoria_grande(n,k):
	return float(m.exp(float(stirling(n)-stirling(k)-stirling(n-k))))

def binomial(k, n, p):
	#Variable aleatoria = k (cantidad de exitos)
	#p = cte
	return combinatoria(n,k)*(p**k)*((1-p)**(n-k))

def binomial_neg(k, n, p):
	#Variable aleatoria = n (cantidad de intentos)
	#El ultimo es un exito, k no es aleatorio
	return combinatoria(n-1, k-1)*(p**k)*((1-p)**(n-k))

def hipergeometrica(k, t, n, q):
	#p =! cte
	#k exitos, t cosas en total, q cosas que quiero, n intentos
	return (combinatoria(q,k)*combinatoria(t-q,n-k))/combinatoria(t,n)

def hipergeometrica_grande(k,t,n,q):
	return (combinatoria_grande(q,k)*combinatoria_grande(t-q,n-k))/combinatoria_grande(t,n)

def poisson(k,mu):
	#k exitos, mu=n*p
	return (m.exp(-mu)*(mu**k))/m.factorial(k)




#GUIA 2
'''
ej1 = binomial(3,10,1.00/6.00) 
#OBS: si pongo 1/6 python los interpreta como enteros y me devuelve un entero

ej2 = hipergeometrica(5, 100, 10, 80)

i = 1
ej6 = 0
while (i<=25):
	ej6 = binomial(i,25,1.00/36.00) + ej6
	i = i+1

j = 3
ej7 = 0
while (j<=5):
	ej7 = hipergeometrica(j,10,5,5) + ej7
	j = j+1

ej9c2i = hipergeometrica(6,10,8,6)
ej9c2ii = hipergeometrica(5,10,8,6)
ej9c3 = hipergeometrica(6,10,7,6)
ej9c4 = hipergeometrica(6,10,6,6)

r = 0
sumej14a = 0
while (r<=7):
  sumej14a = poisson(r,2) + sumej14a
  r = r+1
ej14a = 1 - sumej14a
ej14b = 1 - binomial(0,365,0.0011)

ej17bsuma = 0
h = 100
while (h<130):
  ej17bsuma = binomial_neg(100,h,0.80) + ej17bsuma
  h = h+1
ej17b = 1-ej17bsuma


for n in range(130,150):
    ej17csum = 0
    i = 0
    while (i<100):
        ej17csum = binomial(i,n,0.80) + ej17csum #AL MENOS 100 exitos
        ej17c = 1- ej17csum
        i = i+1
    print(n,ej17c)

for n in range(700,780):
    rapida = (binomial_neg(1,n,1.00/120))**4
    lenta = binomial_neg(1,n,1.00/360)
    print(n,rapida,lenta)

for i in range(4,9):
    afa = hipergeometrica(i,20,8,16)
    print("#hombres=",i,afa)

i=0
ej8asum=0
ej8bsum=0
while(i<10):
    ej8asum = binomial(i,500,0.01)+ej8asum
    ej8bsum = hipergeometrica_grande(i,5000,1000,500)+ej8bsum #ERROR!
    i=i+1
ej8a = 1-ej8asum
ej8b = 1-ej8bsum

ej13 = m.degrees(m.acos(m.sqrt(9.43/16.53))) #da =! que la guia
'''
for n in range(2,30):
    ej10asum = 0
    i = 0
    while (i<2):
        ej10asum = binomial(i,n,0.182) + ej10asum
        ej10a = 1- ej10asum
        i = i+1
    if ej10a>0.90:
	print(n,ej10a)

for k in range(0,10):
	pgol = binomial(k,20,0.182) #prob de meter k goles
	print(k, pgol)
golprom = 20*0.182

#print(golprom)
