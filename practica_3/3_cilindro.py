#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:59:38 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Determinar el área y volumen de un cilindro, dada su altura y su radio.

Análisis:
Entradas: radio (numero 
que representa el radio del cilindro)
altura: (número que representa la altura del cilindro)

salida: area (número que representa el área del cilindro)
volumen (número que representa el volumen del cilindro)
"""
from math import pi

while True:
    radio = float(input('Digite el valor del radio del cilindro: '))
    if radio >= 0:
        break
    print('El radio representa una distancia y no puede ser negativo')
    
while True:
    altura = float(input('Digite el valor de la altura del cilindro: '))
    if altura >= 0:
        break
    print('La altura representa una distancia y no puede ser negativa: ')
    
area = (2*pi* radio)*(radio + altura)
volumen = pi *(radio ** 2)* altura

print('''El área del cilindro es: {} unidades cuadradas
El volúmen del cilindro es: {} unidades cúbicas'''.format(area, volumen))