# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 16:07:07 2022

@author: henry
"""

import numpy as np
import matplotlib.pyplot as plt

def make_m_matrix(n, sigma):
    ones = [1]*(n-2)
    m_1 = np.diag(ones+[0],-1) + np.diag([0] + ones, 1)
    diag = [1] + [sigma] * (n-2) + [1]
    M = np.diag(diag) + m_1
    return M

def solve_anemometer(boundary, n, l, d, k, h):
    P = np.pi * d
    A = np.pi * d**2 / 4
    ss2 = h*P/(k*A)
    delta_x = l/(n-1)
    sigma = -2 - ss2 * delta_x**2
    
    ta, t0, tn = boundary
    M = make_m_matrix(n, sigma)
    B = np.zeros(n)
    B[0] = t0-ta
    B[-1] = tn-ta
    
    return np.linalg.solve(M, B)
    
def analytical(boundary, x, l, d, k, h):
    P = np.pi * d
    A = np.pi * d**2 / 4
    ss = np.sqrt(h*P/(k*A))
    ta, t0, tl = boundary
    theta_l = tl-ta
    theta_0 = t0-ta
    
    return (theta_l*np.sinh(ss*x) + theta_0*np.sinh(ss*(l-x)))/np.sinh(ss*l)
    
    
def main():
    n = 50
    n_2 = 50
    l = 1e-3
    d = 5e-6
    k = 200
    h = 1000
    
    boundary = (293.15, 353.15, 343.15)
    sln = solve_anemometer(boundary, n_2, l, d, k, h)
    x = np.linspace(0,l,n)
    a = analytical(boundary, x, l, d, k, h)
    
    plt.plot(x, a, "r")
    plt.scatter(np.linspace(0,l,n_2), sln)
    plt.show()



if __name__ == "__main__":
    main()