#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 16:53:36 2020

@author: yonathan
"""
import re
archivo = open('registros.txt')
for linea in archivo:
    if "[" in linea:
        limites = linea
        
limites = limites.split(';')
valores = []
for limite in limites:
        valores.append(re.split('\[|\]|,|\:', limite)[:-1])
        
print(valores)
        
