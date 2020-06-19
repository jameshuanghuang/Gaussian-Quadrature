#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 18:20:28 2020

@author: jameshuang
"""

import numpy as np
import matplotlib.pyplot as plt
import itertools
import math
from scipy import integrate
import sympy as sym
from scipy.interpolate import lagrange
from scipy.integrate import quad

a=-1;b=1;
n=2**(2);
h=(b-a)/n;
x = np.arange(a,b+h,h);


def L(x,j):
    
    y = np.array([0 for i in range(len(x))]);
    y[j]=1;
    return lagrange(x, y);

    
def H(X,j):
    h_legen = lambda x: 1*L(X,j)(x); #legen
    h_lague = lambda x: np.exp(-x)*L(X,j)(x); #lague
    h_hermite = lambda x: np.exp(-x**2)*L(X,j)(x); #Hermite 
    
    return quad(h_legen,min(X),max(X))[0] ;

def Gauss_Quard(f,a,b):
    
    w = np.array( [H(x,i) for i in range(len(x))] );   
    Xi = np.array( [f(s) for s in x] );
    
    ans = sum(w*Xi);
    print(ans)
    return ans;


f = lambda x: x**3-x**2;
f_exact1 = lambda x: np.exp(-x**2)*f(x) ;
f_exact2 = lambda x: np.exp(-x)*f(x) ;
f_exact3 = lambda x: 3*f(x) ;

print( quad(f_exact3,a,b)[0] );
Gauss_Quard(f,a,b)