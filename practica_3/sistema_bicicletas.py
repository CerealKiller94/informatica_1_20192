#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:20:04 2020

@author: Yonathan Lopez Mejia
"""


while True:
    tiempo = float(input('Escriba la cantidad de minutos que se usó la bicicleta: '))
    if tiempo >= 0:
        break
    print('Escriba un tiempo válido, no existen los tiempos negativos: ')
    
if tiempo > 1440:
    cobro = ((tiempo * 10) + 100000)
elif tiempo <= 120:
    cobro = tiempo * 10
else:
    cobro = 1200 + ((tiempo - 120) * 60)
    
print('''El valor a pagar por usar {} minutos la bicicleta es: {} pesos'''
      .format(tiempo, cobro))

