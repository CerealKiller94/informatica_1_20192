#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:27:37 2020

@author: Yonathan López Mejía

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Reciba una 
palabra del usuario y un 
número entero menor 
que 26. El programa debe 
cambiar cada letra por la 
que le corresponda al dar 
saltos en el alfabeto de 
acuerdo al número 
especificado por el usuario.
La nueva palabra codificada 
deberá ser mostrada en 
pantalla.


Análisis:
Entradas
word: es la palabra a 
codificar
number: es el número
positivo menor que 26

Auxiliares:
i: es la variable del ciclo
con la que se accede a
cada letra de la palabra

index: es la variable que
almacena la posicion de
cada letra de la palabra
en el abecedario.

letters: son las letras del
abecedario

salida: 
new_word: es la nueva 
palabra codificada según
las reglas del enunciado

"""

while True:
    word = input('Escriba una palabra: ').lower()
    if len(word) > 0:
        break
    print('Escriba una palabra válida')

while True:
    number = int(input('Escriba un número entero positivo menor que 26: '))
    
    if number >= 0 and number < 26:
        break 
    print('Número no válido')

letters = 'abcdefghijklmnopqrstuvwxyz'
new_word = ''
for letter in word:
    index = letters.index(letter)
    index += number
    if index > 25:
        index = index - 26
        new_word += letters[index]
    else:
        new_word += letters[index]
        
print('La nueva palabra es: {}'.format(new_word))