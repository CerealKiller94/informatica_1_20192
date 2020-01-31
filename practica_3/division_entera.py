#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:33:35 2020

@author: Yonathan Lopez Mejia
"""

number = int(input('Digite un número para dividir: '))

while True:
    divider = int(input('Digite el número entre el cual quiere dividir: '))
    if divider != 0:
        break
    print('No se puede dividir entre 0')

cociente = 0

while number >= divider:
    cociente += 1
    number -= divider

print('El resultado de la división entera es: {}'.format(cociente))