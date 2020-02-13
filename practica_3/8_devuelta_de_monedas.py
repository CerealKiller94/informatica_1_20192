#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:05:50 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Una máquina 
dispensadora de productos 
requiere un algoritmo para calcular las devueltas en monedas. 
El objetivo del algoritmo es que 
dada una cantidad a devolver se 
debe calcular la combinación 
que genere la mínima cantidad 
de monedas, utilizando denominaciones de $1.000, $500, $200, $100 y $50. 
Si es imposible lograr la 
cantidad exacta, el sistema deberá decir lo que resta para lograrla.

Análisis: 
Entrada:
cambio: esta variable representa
cuánto es el valor a devolver

salidas:
moneda1000: el número de 
monedas de 1000 a devolver

moneda500: el número de 
monedas de 500 a devolver

moneda200: el número de
monedas de 200 a devolver

moneda100: el número de
monedas de 100 a devolver

moneda50: el numero de 
monedas de 50 a devolver
"""

moneda1000 = 0
moneda500 = 0
moneda200 = 0
moneda100 = 0
moneda50 = 0

while True:
    cambio  = float(input('¿Cuánto es la devuelta? '))
    if cambio >= 0:
        break
    print('Devuelta no válida. Es una devuelta negativa. ¿Le sale a deber?')

if cambio == 0:
    print('No hay nada que devolver')
else:
    moneda1000 = cambio // 1000
    cambio = cambio % 1000
    moneda500 = cambio // 500
    cambio = cambio % 500
    moneda200 = cambio // 200
    cambio = cambio % 200
    moneda100 = cambio // 100
    cambio = cambio % 100
    moneda50 = cambio // 50
    cambio = cambio % 50
    
    print('---------------------- Cambio -----------------------')
    print('''
          Monedas de $1000: |  {0}
          Monedas de $500:  |  {1}
          Monedas de $200:  |  {2}
          Monedas de $100:  |  {3}
          Monedas de $50:   |  {4}
          Resto:            |  {5}
    '''.format(moneda1000, moneda500, moneda200, moneda100, moneda50, cambio))

