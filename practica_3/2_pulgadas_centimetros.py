#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:55:04 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo que convierta de pulgadas a centímetros.

Análisis:
Entradas: inch (numero 
que representa las pulgadas a 
convertir)

salida: centimetres (el valor 
en centímetros de las 
pulgadas 
usando los valores del SI)
"""

while True:
    inch = float(input('Digite el valor de las pulgadas a convertir: '))
    if inch >= 0:
        break
    print('Digite un valor válido para las pulgadas. No existen distancias negativas')
    
centimetres = inch * 2.54
print('{} pulgadas equivalen a {} centímetros'.format(inch, centimetres))