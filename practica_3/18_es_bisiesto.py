#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:57:48 2020

@author: yonathan

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo que determine si un año es bisiesto o no
Análisis:
    * Entradas: anho (Variable entera que almacena el año a validar)
    * Salidas: mensaje que dice si un año es bisiesto o no
    * Auxiliares: es_bisiesto (variable booleana que almacena True si el año es bisiesto)
"""

anho = int(input('Escriba el año: '))
es_bisiesto = False

if anho % 4 == 0:
    if anho % 100 == 0:
        if anho % 400 == 0:
            es_bisiesto = True
    else:
        es_bisiesto = True
        
if es_bisiesto:
    print('El año {} es bisiesto'.format(anho))
else:
    print('El año {} no es bisiesto'.format(anho))