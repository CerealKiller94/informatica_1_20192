#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 13:21:42 2020

@author: yonathan

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Integre los cuatro algoritmos en un solo programa, que al final imprima en pantalla lo siguiente:
------------------------------------
| Algoritmo | Iteraciones promedio |
------------------------------------
| Lineal    |          PL          |
| Binaria   |          PB          |
------------------------------------

 -------------------------------
| Algoritmo       | Iteraciones |
 -------------------------------
| Exhaustivo      |     IE      |
| Bisección       |     IB      |
| Newthon-Raphson |     INR     |
 --------------------------------
 
 Donde PL y PB deben ser los promedios de la cantidad de iteraciones 
 que cada algoritmo realiza para los valores de prueba
 mostrados en la tabla (excel). IE, IB, INR son el número total de 
 iteraciones para encontrar la raíz de la función en el 
 intervalo.
 
auxiliares:
    * L: es la lista de prueba para los algoritmos de búsqueda
    * pruebas: son los valores de prueba que busca cada algoritmo
    de búsqueda
    * iteraciones_lineal: acumula el valor máximo de iteraciones
    del algoritmo de búsqueda lineal
    * iteraciones_binaria: acumula el valor máximo de iteraciones
    del algoritmo de búsqueda binaria
    * encontrado: variable booleana que dice si se encontró (True)
    o no (False) un determinado valor buscado
    * prueba: variable dentro del ciclo for que almacena
    cada uno de los valores de prueba
    * i: variable que se usa para indicar los índices
    de la lista L a recorrer
    * start: índice del primer elemento en un algortimo de búsqueda binaria
    * end: índice del último elemento en un algortimo de búsqueda binaria
    * middle: posible índice del valor buscado en un algoritmo de búsqueda binaria
    * iter_exhaustiva: cantidad total de iteraciones en el método de búsqueda exhaustiva de raíces
    * iter_binario: cantidad total de iteraciones en el método de búsqueda por bisección de raíces
    * iter_nr: cantidad de iteraciones realizadas por el método de Newton-Raphson
    * a: límite inferior del intervalo de búsqueda de la raíz
    * b: límite superior del intervalo de búsqueda de la raíz
    * epsilon: tolerancia al error de los métodos aproximativos
    * delta: tamaño de paso de los métodos aproximativos de raíces
    * xl: posible raíz de la función
    * f_xl: valor de la función evaluada en la posible raíz
    * f1: valor de la función en el límite inferior
    * f2: valor de la función en el límite superior
    * xn: valor aproximado de la raíz de la función en el método de Newton-Raphson
    
    salidas: 
        * Para búsqueda lineal: Para cada iteración del ciclo se muestra el número total 
        de iteraciones hasta el momento, la posición actual en la lista
        y el valor de la lista en la posición actual, en caso
        de encontrar el valor se muestra la posición en la que se encuentra,
        y en cualquier caso se muestra el total de iteraciones hechas
        
        * para búsqueda binaria: Para cada iteración se muestra: el número de la iteración,
        el valor del índice central, el elemento en el índice central,
        y el intervalo de búsqueda. En caso de encontrarse el valor
        se muestra el índice en el que está y en cualquier caso 
        se muestra el número total de iteraciones realizadas por el algoritmo
        
        * Para búsqueda de raíz exhaustiva: en caso de ser encontrado
        se muestra el valor de la raíz aproximada y finalmente se muestra
        siempre el número total de iteraciones hechas por el algoritmo
        
        *Para bisección: en caso de encontrar la raíz la muestra
        y en cualquier caso muestra el número de iteraciones realizadas
        
        * Para Newton-Raphson: En caso de encontrar la raíz, muestra
        su aproximación xn, y en cualquier caso
        muestra el número de iteraciones realizadas
        
        * Para el reporte de resultados:
            *tabla 1: instrucción print con formato que muestra
            el número de iteraciones (iteraciones_lineal e iteraciones_binaria)
            realizadas por los métodos de búsqueda lineal y binario
            de la lista
            
            *tabla 2: instrucción print con formato que muestra
            el número de iteraciones (iter_exhaustiva, iter_binario,
            iter_nr) realizadas por los métodos de búsqueda de raíces
            exhaustivo, binario y de Newton-Raphson
        
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
while abs(f_xl - 0) > epsilon and xl < b:
    iter_exhaustiva += 1
    xl += delta
    f_xl = f(xl)
    
print('-------------- Raiz de la funcion x³ + 2x² - 4x + 3 --------------')
if abs(f_xl - 0) <= epsilon:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(xl))
else:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
print('\nCantidad de iteraciones: {}'.format(iter_exhaustiva))
print('------------------------------------------------------------------')
    
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
        if f(a)*fx < 0:
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
        