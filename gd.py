# -*- coding: utf-8 -*-
"""
Linear regression test

Rabee Hanna
"""

import numpy as np
from sklearn.datasets.samples_generator import make_regression
import pylab
from scipy import stats
from random import randint
                    
'''
slope, intercept, r_value, p_value, slope_std_error = stats.linregress(x[:,0], y)
pylab.plot(x,y,'o')
pylab.plot(x,y_predict,'k-')
pylab.show()
'''                       
#x, y = make_regression(n_samples=50, n_features=1, n_informative=1, 
#                       random_state=0, noise=15)

x = np.array([1,5,8,7,4,6,3,2,9,5,2,1,3,4,5,6,9,8,7,4,5,2,1,6])
y = np.array([(x[i] * randint(0,5)) for i in range(x.shape[0])])


def h(th, x):
    return np.multiply(th.transpose(), x)

def gd_1(x,y,alpha,iterations):
    n_samples = x.shape[0]
    x = np.column_stack((np.ones(n_samples),x)) 
    n_features = x.shape[1]
    th = np.ones(n_features)

    for k in range(iterations):
        hx = np.array([sum(h(th,x)[i]) for i in range(n_samples)])    
        err = (hx - y)
        for j in range(n_features-1):
            err = np.column_stack((err,np.zeros(n_samples)))
            err[:,n_features-1] = err[:,0] * x[:,j+1]
        agrad = alpha * np.array([(sum(err[:,i])/n_samples) for i in range(n_features)])
        th -= agrad        
    print [sum(err[:,i])/n_samples for i in range(n_features)]
    r = []
    for i in range(n_features):
        r.append(str(th[i]) + 'x_' + str(i))
    return 'y = ' + ' + '.join(r)

print(gd_1(x,y,0.01,5000))

s = ''
for i in range(y.size):
    s += str((x[i],y[i])) + ','
s = s[:-1]    
