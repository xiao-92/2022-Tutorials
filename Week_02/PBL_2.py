# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 17:09:28 2022

@author: henry
"""

import numpy as np
import matplotlib.pyplot as plt


def cool_func(x,y):
    return np.log(x**2+y**2)

def cool_func_approx(x,y,h,k):
    return np.log(x**2+y**2) + 2*(h/x+k/y) - 2* (h**2/x**2 + k**2/y**2)

def main():
    x = np.linspace(0.9,1.1,40)
    y = np.linspace(0.9,1.1,40)
    
    x_1 = 1
    y_1 = 1
    h = x-x_1
    k = y-y_1
    
    f_1 = cool_func(x,y)
    f_2 = cool_func_approx(x_1, y_1,h,k)
    
    print(f_1)
    print(f_2)
    
    plt.plot(x,f_1, "r")
    plt.scatter(x,f_2)
    plt.show()

if __name__ == "__main__":
    main()