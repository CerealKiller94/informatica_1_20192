#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:41:33 2020

@author: Yonathan Lopez Mejía

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Diseñe un 
algoritmo que lea un número entero y determine si es par 
o impar.

Análisis: 
Entradas: number (numero a 
validar)

salida: message (contiene el mensaje de si es o no par)
"""

number = int(input('Digite un número: '))

if number % 2:
    message = 'es impar'
else:
    message = 'es par'
    
print('El número {} {}'.format(number, message))