import random, scipy
import os
import numpy as np
from scipy import where, double, r_, c_, array, sign, dot, mean, randn
from pylab import demean


def test_errors(ws, data, labels):
#    error = {}
#    for v in ws:
    error = 100*abs(sum(map(lambda x: min(0,x), sign(dot(ws,data.T)) * labels)))/labels.shape[0]
    return error

def data2data(data, clfs):
    """
    Applies all classifiers to the data and returns their output as vectors
    """
    W=array([clfs[i] for i in range(0,len(clfs))])
    X = dot(data, W.T)
    X = demean(X,axis=1)
    return X

