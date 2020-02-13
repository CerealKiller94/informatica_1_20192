#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 08:20:04 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: En un sistema de 
bicicletas públicas se cobra 
a los usuarios $10 pesos
por minuto de uso hasta un 
máximo de 2 horas. 
El tiempo adicional se cobra con 
un sobrecargo de $50 pesos por 
minuto, pero si supera las 
24 horas se cobra un sobrecargo 
fijo de $100.000 pesos. 
Haga un algoritmo que calcule el monto a cobrar a un usuario dado el tiempo que usó la bicicleta.

Análisis:
Entradas: tiempo (numero de minutos en que la bicicleta estuvo en el parqueadero)


salida: cobro (el dinero a pagar según las reglas del enunciado)
"""


while True:
    tiempo = float(input('Escriba la cantidad de minutos que se usó la bicicleta: '))
    if tiempo >= 0:
        break
    print('Escriba un tiempo válido, no existen los tiempos negativos: ')
    
if tiempo > 1440:
    cobro = ((tiempo * 10) + 100000)
elif tiempo <= 120:
    cobro = tiempo * 10
else:
    cobro = 1200 + ((tiempo - 120) * 60)
    
print('''El valor a pagar por usar {} minutos la bicicleta es: {} pesos'''
      .format(tiempo, cobro))

