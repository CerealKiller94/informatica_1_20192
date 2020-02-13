#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:56:00 2020

@author: Yonathan López Mejía

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un programa que determine si una 
palabra ingresada 
por el usuario es palíndroma 
o no. Utilice la instrucción 
while.


Análisis:
Entradas
word: es la palabra a validar

Auxiliares:
i: es la variable del ciclo
con la que se accede los
elementos del string
is_palindrome: es una variable
booleana que dice si la
palabra es o no palindroma
size: almacena el tamaño
del string


salida: 
mensaje que indica si
la palabra ingresada es o no
palindroma
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