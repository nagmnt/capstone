from scipy.stats import mvn
import numpy as np
import math

def knock_in_barrier(h_x, h_y, m_x, m_y, vol_x, vol_y, rho):
    INF = 100000
    m = np.array([m_x, m_y]) #means
    s = np.array([[vol_x, rho*math.sqrt(vol_x)*math.sqrt(vol_y)],[rho*math.sqrt(vol_x)*math.sqrt(vol_y), vol_y]]) #variance-covariance
    low = np.array([h_x, -1 * INF]) #integral lower
    upp = np.array([INF, h_y]) #integral upper
    p, i = mvn.mvnun(low, upp, m, s)
    return p

print(knock_in_barrier(0, 0, 0, 0, 1, 1, 0))
