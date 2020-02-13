#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:33:35 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Realice un algoritmo
 para la division entera usando solo operadores aritméticos
Análisis:
Entradas: number (es el numero que se va a dividir)
divider (es el numero entre el que se va a dividir)

salida: cociente (es la variable que irá 
acumulando las veces que se puede dividir el numero)

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