#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:28:23 2020

@author: yonathan
"""

def f(x):
    f = x**3 + 2*(x**2) - 4*x + 3 
    return f

def f_prime(x):
    f_prime = 3*(x**2) + 4*(x) - 4 
    return f_prime

a = -4
b = -3
xn = (a + b)/2 #Primera aproximación a la raíz
epsilon = 0.01 #Tolerancia al error
iterations = 0
encontrada = False

if f(a)== 0:
    encontrada = True
    xn = a
elif f(b) == 0:
    encontrada = True
    xn = b
elif f(a)*f(b) > 0:
    encontrada = False  
else:
    while abs(f(xn) - 0) > 0.01:
        iterations += 1
        xn = xn - ((f(xn))/f_prime(xn))
        
    encontrada = True

print('--------Raiz de la funcion x³ + 2x² - 4x + 3  -NR -----------')
if encontrada:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(xn))
    print('\nCantidad de iteraciones: {}'.format(iterations))
    
else:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
    print('\nCantidad de iteraciones: {}'.format(iterations))
print('--------------------------------------------------------------')
        

