# -*- coding: utf-8 -*-
"""
Created on Sun May 28 17:08:37 2017

@author: SAMI
"""

from scipy.stats import norm, chi2, binom

#ej4
mu = 50.00
sigma = 10.00
#norm.interval(alpha, loc=0, scale=1) 
#Endpoints of the range that contains alpha percent of the distribution
b01 = norm.interval(0.95, loc=0, scale=1)
b = norm.interval(0.95, loc=50, scale=10)
bmusigma = [mu+b01[0]*sigma, mu-b01[0]*sigma] #ok, b = bmusigma
bchi = chi2.interval(0.95, 50, loc=0, scale=1)
#chi2.cdf(x, df, loc=0, scale=1)
#cdf is the probability that X will take a value less than or equal to x.
c = 1-chi2.cdf(80, 50, loc=0, scale=1)
d = binom.pmf(k=1, n=15, p=0.005, loc=0)

#ej5
i=0
ej5asum=0
while(i<10):
    ej5asum = binom.pmf(i,500,0.01)+ej5asum
    i=i+1
ej5a = 1-ej5asum
