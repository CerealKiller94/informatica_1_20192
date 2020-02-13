#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 18:42:34 2020
@author: yonathan

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo que determine si un string ,ingresado por el usuario, 
es un documento válido. 
Un documento válido tiene 10 dígitos (solo números).
Análisis:
    * Entradas: documento (variable que almacena el string a validar)
    * Salidas: mensaje que dice si el documento es válido o no
"""


documento = input('Escriba el documento: ')

if documento.isnumeric() and len(documento) == 10:
    print('Documento válido')
else:
    print('Documento no válido')