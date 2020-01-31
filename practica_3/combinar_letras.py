#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:27:37 2020

@author: Yonathan López Mejía
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