#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:56:00 2020

@author: yonathan
"""


while True:
    word = input('Escriba una palabra de al menos dos letras: ').lower()
    if len(word) > 1:
        break
    
    print('Escriba una palabra válida')
    
is_palindrome = True
size = len(word)
i = 0

while i < size:
    if word[i] != word[-(i+1)]:
        is_palindrome = False
        break
    i += 1

if is_palindrome:
    print('La palabra {} es palíndroma'.format(word))
else:
    print('La palabra {} no es palíndroma'.format(word))