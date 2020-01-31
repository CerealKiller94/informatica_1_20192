#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:46:12 2020

@author: Yonathan Lopez Mejia
"""

while True:
    
    a = float(input('Digite el valor del coeficiente cuadrático de la ecuación: '))
    
    if a != 0:
        break
    print('El coeficiente cuadrático no puede ser igual a cero ')

b = float(input('Digite el coeficiente lineal de la ecuación: '))
c = float(input('Digite el valor constante de la ecuación: '))

discriminante = ((b ** 2) - (4 * a * c))

if discriminante == 0:
    sol1 = (-b)/(2 * a)
    sol2 = sol1
elif discriminante > 0:
    sol1 = ((-b) + (discriminante ** 0.5))/(2 * a)
    sol2 = ((-b) - (discriminante ** 0.5))/(2 * a)
else:
    sol1 = '''({} + {}i)/{}'''.format(-b, ((-discriminante) ** 0.5), 2*a)
    sol2 = '''({} - {}i)/{}'''.format(-b, ((-discriminante) ** 0.5), 2*a)
    
print('''Las soluciones para la ecuación son:
{} y {}'''.format(sol1, sol2))