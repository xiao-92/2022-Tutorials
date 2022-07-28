# -*- coding: utf-8 -*-
"""
Created on Wed Jul 27 13:32:16 2022

@author: henry
"""
import numpy as np

def forward_diff(f, x, h):
    approx = (f(x+h)-f(x)) / h
    return approx

def backward_diff(f, x, h):
    approx = (f(x)-f(x-h)) / h
    return approx

def central_diff(f, x, h):
    approx = (f(x+h)- f(x-h)) / (2*h)
    return approx

def func_a(x):
    return x**3

def func_b(x):
    return 3*x**2 - 2*x

def func_c(x):
    return np.sin(x)

