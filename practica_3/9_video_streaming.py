#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:24:18 2020

@author: Yonathan Lopez Mejia

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo 
para calcular el costo de un 
servicio de video streaming por 
demanda. El algoritmo recibirá 
el momento en que inició y terminó la reproducción de videos, 
mediante dos números enteros 
de máximo 6 dígitos que 
representan las horas (00-23), 
los minutos (00-59) y los 
segundos (00-59). 
El costo del servicio es de $2 
pesos por segundo, 
con un cobro mínimo 
de $1.000 pesos. 
Por ejemplo, si los tiempos de
inicio y fin son 23754 y 130231, 
el costo del servicio será de 
$74.954 pesos..

Análisis: 
Entradas: 
inicial (entero que representa el 
inicio del streaming)

final(entero que representa el final 
del streaming)


Auxiliares:
segundos_inicial: valor de los 
segundos iniciales
minutos_inicial: valor de los minutos 
iniciales
hora_inicial: valor de la hora inicial

segundos_final: valor de los segundos finales
minutos_final: valor de los minutos
finales
hora_final: valor de la hora final

segundos_transcurridos: valor en segundos entre las dos horas



salida: pago (es el valor en pesos a pagar)
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
