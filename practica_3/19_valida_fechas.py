#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 19:39:05 2020

@author: yonathan

Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Haga un algoritmo que, dado un string ingresado por el usuario, determine si es una fecha válida o no. La fecha válida debe cumplir con el formato "yyyy-mm-dd". Por ejemplo:

    * 2010-12-12 es válida
    * 2000-1-1 es válida
    * 20-12 no es válida
    * 2010/23-12 no es válida
    * 220033 no es válida
    * 2010-12-32 no es válida
    * 2016-2-29  es válida
    * 2019-2-29 no es válida (no es año bisiesto).
Análisis:
    * fecha:  variable que almacena el string tipo fecha a validar
    * Salidas: mensaje que dice si la fecha es válida o no
    * auxiliares: contador_guiones (variable que valida que la cadena tenga exactamente 2 guiones)
    valida (variable booleana que dice si la fecha es valida o no)
"""


fecha = input('Escriba la fecha en formato yyyy-mm-dd: ')
contador_guiones = 0
valida = False

for caracter in fecha:
    if caracter == '-':
        contador_guiones += 1

if contador_guiones == 2:
    anho, mes, dia = fecha.split('-')

    if anho.isnumeric() and mes.isnumeric() and dia.isnumeric():
        anho = int(anho)
        mes = int(mes)
        dia = int(dia)
        
        if anho >= 0:
            if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or 
                mes == 8 or mes == 10 or mes == 12) and 1 <= dia <= 31:
                valida = True
            elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and 1 <= dia <= 30:
                valida = True
            elif mes == 2 and dia == 29:
                if anho % 4 == 0:
                    if anho % 100 == 0:
                        if anho % 400 == 0:
                            valida = True
                        else:
                            valida = False
                    else:
                        valida = True
                else:
                    valida = False
            elif mes == 2 and 1 <= dia <= 28:
                valida = True
            else:
                valida = False
        else:
            valida = False
            
    else:
        valida = False
else:
    valida = False
    
if valida:
    print('La fecha {} tiene un formato correcto'.format(fecha))
else:
    print('La fecha {} no es válida'.format(fecha))
    
