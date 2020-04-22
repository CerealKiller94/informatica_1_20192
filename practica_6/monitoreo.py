#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import re

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

def obtener_usuarios():
    """Esta función retorna una copia del diccionario de usuarios"""
    global users
    return users.copy()

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
                elif '[' in registro:
                    linea = registro.split(';')
                    for limite in linea:
                        limites.append(re.split('\[|\]|,|\:', limite))
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
    archivo.write('\n')   

def escribir_estaciones(archivo):
    """
    Esta función recibe el archivo a escribir y dentro de él
    escribe todos los datos de las estaciones registradas dentro del aplicativo
    respetando el formato predefinido.
    la variable key representa la clave de cada entrada en el diccionario (clave de estacion, autoincremental)
    y la variable value representa los valores almacenados en forma de 
    lista para cada estacion
    """
    global estaciones
    for key, value in estaciones.items():
        estacion = '''{0},{1},{2}'''.format(key, *value)
        archivo.write(estacion)
        archivo.write('\n')
    archivo.write('\n') 

def escribir_municipios(archivo):
    """
    Esta función recibe el archivo a escribir y dentro de él
    escribe todos los datos de las estaciones registradas dentro del aplicativo
    respetando el formato predefinido.
    la variable key representa la clave de cada entrada en el diccionario (clave de estacion, autoincremental)
    y la variable value representa los valores almacenados en forma de 
    lista para cada estacion
    """
    global municipios
    municipio = ':'
    municipio += ','.join(municipios)
    archivo.write(municipio)
    archivo.write('\n\n')

def escribir_limites(archivo):
    """Esta función recibe el archivo a escribir
    y escribe en el, el string correspondiente a los limites.
    No retorna"""
    global limites
    escribir = ""
    for limite in limites:
        escribir += limite[0]+"["+limite[1]+":"+limite[2]+","+limite[3]+"]"+";"
    archivo.write(escribir.strip(';'))
    archivo.write('\n\n') 


def escribir_medidas(archivo):
    """Esta función recibe el archivo a escribir
    y escribe en el las cadenas correspondientes a los
    límites"""
    
    global mediciones
    for medicion in mediciones:
        archivo.write(";".join(medicion))
        archivo.write('\n')

def escribir_archivo():
    """
    Esta función abre el archivo para escribir y luego llama a cada 
    función que escribe cada una de las estructuras de datos,
    con su respectivo formato
    """
    with open('registros.txt', 'w') as archivo:
        escribir_usuarios(archivo)
        escribir_municipios(archivo)
        escribir_estaciones(archivo)
        escribir_limites(archivo)
        escribir_medidas(archivo)
        

def obtener_municipios():
    """
    Esta función retorna la tupla de municipios
    """
    global municipios
    return municipios

def crear_estacion(nombre, municipio):
    """Esta función agrega una nueva estación al diccionario de estaciones.
    Recibe un nombre para la estación y el municipio en el que está,
    luego, valida si esa estación ya está en el municipio, en caso
    de que se cumpla la condición retorna False y no se crea una estación,
    en caso contrario crea la estación y retorna True"""
    global estaciones
    clave = str(len(estaciones)+1)
    for values in estaciones.values():
        if values[0] == nombre and values[1] == municipio:
            return False
    estaciones[clave] = [nombre, municipio]
    return True

def obtener_estaciones():
    """Esta función retorna una copia del diccionario de estaciones"""
    global estaciones
    return estaciones.copy()

def editar_estacion(clave, nombre, municipio):
    """
    Esta función actualiza una entrada en el diccionario de estaciones.
    Edita una estación si los nuevos datos no hacen referencia
    a una estación ya existente en cuyo caso retorna False indicando
    que no se actualizó ninguna entrada o retorna True si se actualizó
    alguna estación
    """
    global estaciones
    for values in estaciones.values():
        if values[0] == nombre and values[1] == municipio:
            return False
    estaciones[clave] = [nombre, municipio]
    return True

def validar_estacion(clave):
    """
    Esta función recibe la clave de una estación.
    Valida si una estación tiene medidas asignadas.
    En caso de que las tenga retorna False en caso contrario, 
    retorna True
    """
    global mediciones
    for medida in mediciones:
        if clave == medida[1]:
            return False
    return True
    
def eliminar_estacion(clave):
    """
    Esta función recibe la clave de la estación que se quiere eliminar.
    Luego, llama a la función encargada de validar si la estación
    tiene medidas asociadas. Si la estación no tiene medidas asociadas
    se elimina la entrada y se retorna un True, en caso contrario, se
    retorn un False
    """
    global estaciones
    if validar_estacion(clave):
        del estaciones[clave]
        return True
    else:
        return False
    
def consultar_estaciones_municipio(municipio):
    """Esta función retorna todas las estaciones
    dentro del diccionario de estaciones que correspondan
    con el municipio deseado"""
    global estaciones
    return {key:value for (key, value) in estaciones.items() if value[1] == municipio}

def obtener_limites():
    """Esta función retorna una copia
    de la lista de límites"""
    global limites
    return limites.copy()

def agregar_medida(estacion, medidas):
    """
    Esta función recibe el código de la estación en forma de string asociada
    a las medidas y una tupla con las medidas ingresadas
    por el usuario ya validadas y las agrega a la lista de mediciones
    """
    global mediciones
    fecha = str(datetime.datetime.now().replace(microsecond=0))
    medida = '{'
    for valores in medidas:
        medida += valores+","
    medida = medida.strip(',')
    medida += '}'
    medida = medida.replace("ND", "-999.0")
    mediciones.append([fecha, str(estacion), medida])
    return True

def consultar_medidas_estaciones(codigo):
    """
    Esta función recibe el código de la estación y consulta
    las medidas asociadas a dicha estación. Luego, retorna un iterable
    con las medidas asociadas a la estación y su nombre
    """
    global mediciones
    return (medida for medida in mediciones if medida[1] == codigo)

def obtener_estaciones_municipio(municipio):
    """
    Esta función obtiene el municipio de una estación
    y retorna todas las estaciones asociadas a ese municipio
    dentro un diccionario llamado consulta que contendrá
    las estaciones de ese municipio
    """
    global estaciones
    consulta = {}
    for key, values in estaciones.items():
        if values[1] == municipio:
            consulta[key] = values
            
    return consulta
        

def validar_rango_fecha(fecha, inicio=None, fin=None, dias=0):
    """
    Esta función valida que fechas están en un rango determinado.
    Recibe una fecha inicial o final en forma de string que son opcionales
    o un valor numérico de dias si se quiere analizar una fecha
    sobre un rango determinado, además de la fecha a analizar que es 
    obligatoria. Devuelve True o False si la fecha está en el rango
    """
    fecha = datetime.datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
    if inicio is None:
        limite = datetime.datetime.now() - datetime.timedelta(days=dias)
        if limite <= fecha:
            return True
        return False
    else:
        inicio = datetime.datetime.strptime(inicio, '%Y-%m-%d')
        fin = datetime.datetime.strptime(fin, '%Y-%m-%d')
        if inicio > fin:
            aux = inicio
            inicio = fin
            fin = aux
        elif inicio == fin:
            fin = inicio + datetime.timedelta(days=1)
        if inicio <= fecha <= fin:
            return True
        return False
        
def obtener_resultados(valores):
    """
    Esta función recibe una lista con
    las medidas a las que se les va a sacar
    el mínimo, el máximo y el promedio. 
    Retorna una tupla con los tres valores
    """
    minimo = min(valores)
    maximo = max(valores)
    promedio = sum(valores)/len(valores)
    
    return minimo,maximo,promedio
    
def procesar_datos(variable, analisis):
    """
    Esta función recibe las medidas a analizar y la variable sobre
    la que se realizará el analisis. La variable es un string
    que representa la posición dentro
    de la lista de limites, y las medidas de analisis son una lista
    con todos los datos de las medidas.
    La función retorna una lista 
    """
    global limites
    global estaciones
    medidas = []
    valores = []
    resultados = []
    medidas_minimo = []
    medidas_maximo = []
    
    for medicion in analisis:
        aux = re.split('\{|\}|,',medicion[2][1:-1])
        medidas.append([medicion[0:2]]+[aux])
    
    for medida in medidas:
        valor = medida[1][int(variable)]
        valor = float(valor)
        if valor != -999.0:
            valores.append(float(valor))
    if not valores:
        return False
    minimo, maximo, promedio = obtener_resultados(valores)
    
    for medida in medidas:
        valor = medida[1][int(variable)]
        if float(valor) == minimo:
            cod_estacion = medida[0][1]
            nombre = estaciones[cod_estacion][0]
            fecha = medida[0][0]
            medida_nombre = limites[int(variable)][0]
            medidas_minimo = [nombre, fecha, medida_nombre, valor, 'Minimo', promedio]
            resultados.append(medidas_minimo[:])      
        if float(valor) == maximo:
            cod_estacion = medida[0][1]
            nombre = estaciones[cod_estacion][0]
            fecha = medida[0][0]
            medida_nombre = limites[int(variable)][0]
            medidas_maximo = [nombre, fecha, medida_nombre, valor, 'Maximo', promedio]
            resultados.append(medidas_maximo[:])
    return resultados
            

def analizar_medidas(municipio, variables, dias):
    """
    Esta función recibe un string con el código de un municipio,
    la medida a procesar, las fechas de analisis que pueden ser
    un string numerico que representa la cantidad de dias para analizar,
    o un string con dos fechas separadas por punto y coma ; 
    en caso de que el usuario quiera usar fechas propias y la variable
    a analizar.
    Primero: la función obtiene las estaciones asociadas a un municipio
    Segundo: si hay estaciones asociadas a ese municipio, la función obtiene las medidas
    de esas estaciones
    Tercero: la función filtra las mediciones que estén en el 
    rango de tiempo determinado.
    False si el municipio no tiene medidas asociadas o si las estaciones de ese
    municipio no tiene medidas asociadas
    Una lista con los valores de las medidas minimas, máximas y promedio 
    de la medida asociada a la estación de ese municipio
        -1
    """

    medidas_estacion = []
    medidas_analisis = []
    estaciones_municipio = obtener_estaciones_municipio(municipio)
    if not estaciones_municipio:
        print('{} no tiene estaciones asociadas'.format(municipio))
        return False
    
    codigos_estaciones = tuple(estaciones_municipio.keys())
    for medida in mediciones:
        if medida[1] in codigos_estaciones:
            medidas_estacion.append(medida)
    
    if not medidas_estacion:
        print('{} no tiene estaciones con medidas asociadas'.format(municipio))
        return False
    
    for medida in medidas_estacion:
        if dias.isnumeric():
            if validar_rango_fecha(fecha=medida[0], dias=int(dias)):
                medidas_analisis.append(medida)
        else:
            inicio, final = dias.split(';')
            if validar_rango_fecha(fecha=medida[0], inicio=inicio, fin=final):
                medidas_analisis.append(medida)
                
                
    if not medidas_analisis:
        print('No se encontraron medidas para ese periodo de tiempo en las estaciones de {}'.format(municipio))
        return False
    
    resultados = procesar_datos(variables, medidas_analisis)
    if not resultados:
        global limites
        print('''Las estaciones del municipio: {0} no tienen valores validos para la medida {1}
              '''.format(municipio, limites[int(variables)][0]))
        return -1
    return resultados
    
    
    
    
    
    
    
