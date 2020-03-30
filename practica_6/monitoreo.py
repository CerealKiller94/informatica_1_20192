#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 11:28:35 2020

@author: yonathan
Nombre: Yonathan López Mejía
Documento: 1017220389
Programa: sistema de monitoreo de la calidad del aire. Práctica 6
users: diccionario donde se almacenarán los usuarios registrados. Su clave es
el documento
municipios: tupla donde están almacenados los nombres de los municipios del
valle de aburrá
estaciones: diccionario donde están almacenadas las estaciones de monitoreo, su clave
es la clave de la estación
limites = esta lista almacena los valores máximos y mínimos de las variables
de medición
mediciones = esta lista almacena los históricos de las mediciones
"""

users = {}
municipios = ()
estaciones = {}
limites = []
mediciones = []

def procesar_linea(linea, separador, inicio='', final=''):
    """Esta función recibe una línea, un separador y opcionalmente
    un caracter de inicio y final, luego, elimina los espacios en blanco,
    los caracteres de inicio y final y retorna una lista con
    la línea separada por el caracter separador"""
    linea = linea.strip()
    linea = linea.strip(inicio)
    linea = linea.strip(final)
    return linea.split(separador)

def leer_datos():
    """
    Esta función se encarga de leer y almacenar
    los datos guardados en el archivo plano,
    para luego retornar las estructuras de datos correspondientes
    a cada tipo de elemento dentro del archivo de texto.
    Users: Diccionario para almacenar los usuarios, su clave es la cedula
    municipios: tupla donde se almacenan los municipios
    estaciones: diccionario donde se almacenan las estaciones, su clave es el código
    de la estacion
    limites: lista que almacena los valores de referencia para las mediciones
    mediciones: lista donde está almacenado el histórico de mediciones
    """
    users = {}
    municipios = ()
    estaciones = {}
    limites = []
    mediciones = []
    with open('registros.txt', encoding='utf-8-sig') as bd:
        for registro in bd:
            if registro != '\n':
                if registro.startswith('<'):
                    user = procesar_linea(registro, ';', '<', '>')
                    users[user[0]] = user[1:]
                elif registro.startswith(':'):
                    municipios = tuple(procesar_linea(registro, ',', ':'))
                elif registro[1] == ',':
                    estacion = procesar_linea(registro, ',')
                    estaciones[estacion[0]] = estacion[1:]
                elif registro.startswith('PM10'):
                    limites = procesar_linea(registro, ';')
                else:
                    mediciones.append(procesar_linea(registro, ';'))
                
    return (users, municipios, estaciones, limites, mediciones)

def cargar_estructuras():
    """Esta función carga los valores de las estructuras de datos
    dentro de variables globales para que sean utilizables por todo el programa cuando 
    se les necesite"""
    global users, municipios, estaciones, limites, mediciones
    users, municipios, estaciones, limites, mediciones = leer_datos()

def crear_usuario(documento, nombre, password, perfil):
    """Esta función recibe los strings correspondientes
    a los datos que tiene cada usuario y los asigna dentro del diccionario
    de usuarios. En caso de que el usuario exista retorna un False pues
    no se puede crear, en caso contrario crea el usuario y retorna True"""
    global users
    if documento in users:
        return False
    users[documento] = [nombre, password, perfil]
    return True

def consultar_usuario(documento):
    """Esta función retorna un usuario que exista dentro del diccionario.
    Si el usuario no existe retorna -1 """
    global users
    if documento not in users:
        return -1
    return users[documento]

def editar_usuario(documento, nombre, password, perfil):
    """Esta función recibe los strings correspondientes
    a los datos que tiene cada usuario y los asigna dentro del diccionario
    de usuarios. Luego, edita el usuario y devuelve True"""
    users[documento] = [nombre, password, perfil]
    return True

def eliminar_usuario(documento):
    """Esta función recibe un string que representa el documento de un usuario,
    luego, elimina el registro asociado a ese documento dentro del diccionario y retorna True"""
    global users 
    del users[documento]
    return True

def iniciar_sesion(usuario, password):
    """Esta función implementa el algoritmo de inicio de sesión dentro de
    la aplicación. La función valida si el usuario y contraseña se corresponde
    con un usuario y contraseña almacenado dentro de los usuarios, de ser así,
    retorna el documento del usuario, sino, retorna -1"""
    global users
    for key, value in users.items():
        if value[0] == usuario and value[1] == password:
            return key, value[2]
    return -1

def escribir_usuarios(archivo):
    """
    Esta función recibe el archivo a escribir y dentro de él
    escribe todos los datos de los usuarios registrados dentro del aplicativo
    respetando el formato predefinido.
    la variable key representa la clave de cada entrada en el diccionario (documento)
    y la variable value representa los valores almacenados en forma de 
    lista para los usuarios
    """
    global users
    for key, value in users.items():
        user = '''<{0};{1};{2};{3}>'''.format(key, *value)
        archivo.write(user)
        archivo.write('\n')

def escribir_archivo():
    """
    Esta función abre el archivo para escribir y luego llama a cada 
    función que escribe cada una de las estructuras de datos,
    con su respectivo formato
    """
    with open('escribir_prueba.txt', 'w') as archivo:
        escribir_usuarios(archivo)

                
                
                


