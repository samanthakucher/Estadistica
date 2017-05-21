import math as m

def combinatoria(n,k):
	return float(m.factorial(n)/(m.factorial(n-k)*m.factorial(k)))

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

#GUIA 2
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

l = 0
suma = 0
while (l<=2):
	suma = binomial(l,10,0.20) +suma
	l = l+1
ej9a = 1 - suma
ej9b = binomial(1,6,0.20)

print(ej9b)