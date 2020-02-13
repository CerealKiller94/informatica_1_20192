#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:35:31 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Teniendo en cuenta 
que un carro necesita cambio de 
aceite cada 6.000 km, haga un 
algoritmo que calcule cuántos 
cambios de aceite ha tenido un 
carro según el total de kilómetros 
que ha recorrido.

Análisis: 
Entradas: km (kilometros recorridos)

salida: cambios (el número de cambios de aceite según el kilometraje)
"""

while True:
    km = float(input('Digite la cantidad de kilometros recorridos: '))
    if km >= 0:
        break
    print('Los kilometros representan distancia y no pueden ser negativos')

cambios = km // 6000
print('''Para {} kilometros el automóvil ha tenido {} cambios de aceite'''
      .format(km, cambios))