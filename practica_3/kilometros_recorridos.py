#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:35:31 2020

@author: Yonathan Lopez Mejia
"""

while True:
    km = float(input('Digite la cantidad de kilometros recorridos: '))
    if km >= 0:
        break
    print('Los kilometros representan distancia y no pueden ser negativos')

cambios = km // 6000
print('''Para {} kilometros el automóvil ha tenido {} cambios de aceite'''
      .format(km, cambios))