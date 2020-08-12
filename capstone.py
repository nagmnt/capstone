from scipy.stats import mvn
import numpy as np

def knock_in_barrier(h_x, h_y, m_x, m_y, rho):
    INF = 100000
    m = np.array([m_x, m_y]) #means
    s = np.array([[1, rho],[rho, 1]]) #variance-covariance
    low = np.array([h_x, -1 * INF]) #integral lower
    upp = np.array([INF, h_y]) #integral upper
    p, i = mvn.mvnun(low, upp, m, s)
    return p

print(knock_in_barrier(0, 0, 0, 0, 0))
