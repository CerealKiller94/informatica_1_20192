#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:24:18 2020

@author: Yonathan Lopez Mejia
"""

while True:
    inicial = int(input('Digite la hora inicial '))

    if inicial >= 0 and inicial <= 235959:
        break

    print('Hora inicial no válida')

while True:
    final = int(input('Digite la hora final '))

    if final >= 0 and inicial <= 235959:
        break
    print('Hora final no válida. Negativa')

segundos_inicial = inicial % 100
minutos_inicial = ((inicial - segundos_inicial) % 10000)//100
hora_inicial = (inicial // 10000) - ((inicial % 10000)//10000)

segundos_final = final % 100
minutos_final = ((final - segundos_final) % 10000)//100
hora_final = (final // 10000) - ((final % 10000)//10000)

if segundos_final < segundos_inicial:
    segundos_final += 60
    minutos_final -= 1

if minutos_final < minutos_inicial:
    minutos_final += 60
    hora_final -= 1

if hora_final < hora_inicial:
    hora_final += 24

segundos_transcurridos = (segundos_final - segundos_inicial) + (
    (minutos_final - minutos_inicial) * 60) + ((hora_final - hora_inicial) * 3600)

if segundos_transcurridos <= 500:
    print('El valor a pagar son: $1000 pesos')
else:
    pago = segundos_transcurridos * 2
    print('El valor a pagar son: ${} pesos'.format(pago))
