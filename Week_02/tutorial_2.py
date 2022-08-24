# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 13:10:22 2022

@author: henry
"""
import math
import numpy as np
import matplotlib.pyplot as plt

def fact(n):
    # Return n!
    if n == 1 or n == 0: 
        return 1
    else:
        return n * fact(n-1)
    
def exptaylor(n, x):
    # Return Taylor series of exp(x) using n terms
    #exp(x) = 1 + x + x**2/2 ...
    
    terms = [x**i / fact(i) for i in range(n)]
    return sum(terms)
        
def better_exp(n, x):
    # Return Taylor series of exp(x) using n terms
    term = 1
    output = term
    for i in range(1, n+1):
        term *= x/i
        output += term
    return output

def main():
    n = 10
    x = np.linspace(-2,1, 20)
    actual = np.exp(x)
    approx = better_exp(n, x)
    
    plt.plot(x, actual, "r")
    plt.scatter(x, approx)
    plt.show()

if __name__ == "__main__":
    main()
    