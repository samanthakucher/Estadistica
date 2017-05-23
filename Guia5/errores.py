# -*- coding: utf-8 -*-
"""
Created on Tue May 23 15:17:01 2017

@author: SAMI
"""

import numpy as np


#ej6
fmax, efmax = 2384.00, np.sqrt(2384.00)
fmin, efmin = 992.00, np.sqrt(992.00)
c, ec = 69.00, np.sqrt(69.00)
e, ee = 0.1, 0.006
t = 600.00
bmax, bmin = (1/e)*(fmax/t-c/t), (1/e)*(fmin/t-c/t)
dbmaxdc, dbmindc = -1/(e*t), -1/(e*t)
dbmaxde, dbminde = -bmax/e, -bmin/e
dbmaxdfmax, dbmindfmin  =1/(e*t), 1/(e*t)
cov_bmax_bmin = dbmaxdc*dbmindc*(ec**2)+dbmaxde*dbminde*(ee**2)
var_bmax = (dbmaxdfmax**2)*(efmax**2)+(dbmaxdc**2)*(ec**2)+(dbmaxde**2)*(ee**2)
var_bmin = (dbmindfmin**2)*(efmin**2)+(dbmindc**2)*(ec**2)+(dbminde**2)*(ee**2)
matriz_cov_B = np.matrix([[var_bmax, cov_bmax_bmin], [cov_bmax_bmin, var_bmin]])
print(matriz_cov_B)
correlacion = cov_bmax_bmin/(np.sqrt(var_bmax)*np.sqrt(var_bmin))
print('correlacion = {}').format(correlacion)
a = (np.log(bmax))/(np.log(bmin)) #item c
delta_a = 1.4-a
dadbmax, dadbmin = 1/(bmax*np.log(bmin)), -np.log(bmax)/(bmin*((np.log(bmin))**2))
ea_concov = dadbmax*dadbmin*cov_bmax_bmin+(dadbmax**2)*var_bmax+(dadbmin**2)*var_bmin
ea_sincov = (dadbmax**2)*var_bmax+(dadbmin**2)*var_bmin
sigma_a_concov, sigma_a_sincov = np.sqrt(ea_concov), np.sqrt(ea_sincov)
delta_concov, delta_sincov = delta_a/sigma_a_concov, delta_a/sigma_a_sincov
#OBS: sigma_a_concov me da 0.03 y en clase dio 0.02, y eso cambia MUCHO cuanto difieren los a
print('Teniendo en cuenta la covarianza, delta a es {} sigmas a. Sin tener en cuenta la covarianza, es {} sigmas a.').format(delta_concov, delta_sincov)
