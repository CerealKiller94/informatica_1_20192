#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:43:30 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Dado el valor del 
lado de un triángulo 
equilátero, 
haga un algoritmo que calcule su perímetro, su altura 
y su área.

Análisis:
Entradas: lado (numero que 
representa el valor del lado 
del triángulo)

salida: perimetro (el perímetro del triángulo)
altura (la altura del triángulo)
area (el área del triángulo)
"""

while True:
    lado = float(input('Digite el valor del lado del triángulo equilatero: '))
    if lado > 0:
        break
    print('Digite una longitud mayor que 0')

perimetro = 3*lado
altura = lado * ((3 ** 0.5)/2)
area = (lado ** 2) * ((3 ** 0.5)/4)

print('''El área del triangulo es: {0}, 
su altura es: {1} 
y su perímetro es: {2}'''.format(area, altura, perimetro))