#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:41:33 2020

@author: Yonathan Lopez Mejía
"""

number = int(input('Digite un número: '))

if number % 2:
    message = 'es impar'
else:
    message = 'es par'
    
print('El número {} {}'.format(number, message))