#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:55:04 2020

@author: Yonathan Lopez Mejia
"""

while True:
    inch = float(input('Digite el valor de las pulgadas a convertir: '))
    if inch >= 0:
        break
    print('Digite un valor válido para las pulgadas. No existen distancias negativas')
    
centimetres = inch * 2.54
print('{} pulgadas equivalen a {} centímetros'.format(inch, centimetres))