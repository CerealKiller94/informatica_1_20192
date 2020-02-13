#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 15:30:15 2020

@author: yonathan

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Escriba un 
programa que le pida al 
usuario una palabra o 
frase y una letra. 
El programa deberá 
imprimir la misma frase 
o palabra ingresada, 
pero ocultando la letra
que ingresó el usuario 
con un asterisco.


Análisis:
Entradas
phrase: es la frase a la
que se le ocultarán
caracteres

letter_to_ocult: es la letra que
se ocultará

Auxiliares:
letter: es la variable del ciclo
con la que se accede los
elementos del string y se compara con la letra a ocultar


salida: 
new_phrase: es la frase inicial
con los caracteres ocultos
"""

while True:
    
    phrase = input('Escriba una frase: ')
    if len(phrase) > 0:
        break 
    print('Escriba una frase, por favor')


while True:
    
    letter_to_ocult = input('Digite la letra a ocultar: ')
    if len(letter_to_ocult) == 1:
        break
    print('No ha escrito una letra valida')
            

new_phrase = ''
for letter in phrase:
    if letter == letter_to_ocult:
        new_phrase += '*'
    else:
        new_phrase += letter

print('Esta es la nueva frase: {}'.format(new_phrase))