#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:28:23 2020

@author: yonathan
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Implemente el algoritmo de búsqueda de raíces para la 
función usando el método de Newthon-Raphson.

auxiliares:
    iterations: contador de las veces que se repiten los ciclos
    a: límite inferior del intervalo de 
    b: límite superior del intervalo de búsqueda
    epsilon: tolerancia al error
    encontrada: variable booleana que dice si se encontró (True)
    o no (False) la aproximación de la raíz
    xn: variable que almacena cada aproximación
    del valor de la función
    f: variable que almacena el valor de la función
    evaluada en la posible raíz
    f_prime: variable que almacena el valor de la derivada
    de la función evaluada en un punto
    
salidas:
    xn: en caso de encontrar la raíz, se muestra
    su valor aproximado
    iterations: siempre se muestra al final el número
    de ciclos hechos por el algoritmo
"""
def f(x):
    """Esta función retorna el valor de F(x) evaluado
    en un punto"""
    f = x**3 + 2*(x**2) - 4*x + 3 
    return f

def f_prime(x):
    """Esta función retorna el valor de F'(x) (la derivada
    de F(x)) evaluada en un punto"""
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
        

