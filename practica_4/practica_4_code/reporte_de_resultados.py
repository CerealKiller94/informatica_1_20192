#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:21:42 2020

@author: yonathan
"""

def f(x):
    f = x**3 + 2*(x**2) - 4*x + 3 
    return f

def f_prime(x):
    f_prime = 3*(x**2) + 4*(x) - 4 
    return f_prime

L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]
pruebas = [-45, -21, 0, 92, 100]
iteraciones_lineal = 0
iteraciones_binaria = 0

for prueba in pruebas:
    encontrado = False
    i = 0
    print('\n************************* Búsqueda lineal *********************')
    print('Número: {}\n'.format(prueba))

    while i < len(L):
        print('Iteración: {}, L[{}] = {}'.format(i, i, 
                                             L[i]))
        if L[i] == prueba:
            encontrado = True
            break
    
        i += 1
        iteraciones_lineal += 1
    
    if encontrado:
        print('\nNúmero encontrado en la posición: {}'.format(i))
    else:
        print('\nNúmero no encontrado')
    
    print('\nCantidad de iteraciones: {}'.format(i))

    print('************************* Fin búsqueda lineal *******************')
    
    
for prueba in pruebas:
    print('\n************************* Búsqueda binaria *********************')
    print('Número: {}\n'.format(prueba))
    encontrado = False
    start = 0
    end = len(L) - 1
    i = 0
    while start <= end:
        middle = (start + end)//2
        i += 1
        print('Iteración: {}, central = {}, L[central] = {}, Intervalo: {}'.format(
        i, middle, L[i], L[start:end+1]))
        iteraciones_binaria += 1
        if L[middle] == prueba:
            encontrado = True
            break
        if L[middle] > prueba:
            end = middle - 1
        else:
            start = middle + 1
    if encontrado:
        print('\nNúmero encontrado en la posición {}'.format(middle))
    else:
        print('\nNúmero no encontrado')
    
    print('\nCantidad de iteraciones: {}'.format(i))
    
print('\n************************ Raices método exhaustivo ****************')
iter_exhaustiva = 0 
iter_binario = 0
a = -4
b = -3 
epsilon = 0.01 
delta = 0.0001
xl = a
f_xl = f(xl)
while abs(f_xl - 0) > epsilon:
    iter_exhaustiva += 1
    xl += delta
    f_xl = f(xl)
    
print('-------------- Raiz de la funcion x³ + 2x² - 4x + 3 --------------')
print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(xl))
print('\nCantidad de iteraciones: {}'.format(iter_exhaustiva))
    
print('\n************************ Raices método biseccion *******************')
a = -4
b = -3
encontrada = False
f1 = f(a)
f2 = f(b)
if f1 == 0:
    encontrada = True
    medio = a
elif f2 == 0:
    encontrada = True
    medio = b
elif f1*f2 > 0:
    encontrada = False  
else:
    while a < b:
        iter_binario += 1
        medio = (a + b)/2
        fx = f(medio)
        if abs(fx - 0) <= epsilon:
            encontrada = True
            break
        if fx > 0:
            b = medio
        else:
            a = medio
    print('--------Raiz de la funcion x³ + 2x² - 4x + 3  -Binaria -----------')
    if encontrada:
        print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(medio))
        print('\nCantidad de iteraciones: {}'.format(iter_binario))
    

    else:
        print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
        print('\nCantidad de iteraciones: {}'.format(iter_binario))
print('--------------------------------------------------------------------')
print('\n********************* Raices método Newton-Raphson ****************')
a = -4
b = -3
xn = (a + b)/2 #Primera aproximación a la raíz
iter_nr = 0

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
        iter_nr += 1
        xn = xn - ((f(xn))/f_prime(xn))
        
    encontrada = True

print('--------Raiz de la funcion x³ + 2x² - 4x + 3  -NR -----------')
if encontrada:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(xn))
    print('\nCantidad de iteraciones: {}'.format(iter_nr))
    
else:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
    print('\nCantidad de iteraciones: {}'.format(iter_nr))
print('--------------------------------------------------------------')
print('''
      ------------------------------------
      | Algoritmo | Iteraciones promedio |
      ------------------------------------
      | Lineal    |          {0}        |
      | Binaria   |          {1}         |
      ------------------------------------'''.format(iteraciones_lineal/len(pruebas), iteraciones_binaria/len(pruebas)))

print('''
      --------------------------------------
      | Algoritmo      |     Iteraciones   |
      --------------------------------------
      | Exhaustivo     |         {0}      |
      | Bisección      |           {1}       |
      | Newton-Raphson |           {2}       |
      --------------------------------------
'''.format(iter_exhaustiva, iter_binario, iter_nr))
        