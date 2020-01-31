#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:05:50 2020

@author: Yonathan Lopez Mejia
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

