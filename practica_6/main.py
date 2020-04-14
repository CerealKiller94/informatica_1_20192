#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import monitoreo as mn
import utilidades as utils
import re
user_actual = ""


"""
Created on Mon Mar 30 11:28:19 2020

@author: yonathan

Nombre: Yonathan López Mejía
Documento: 1017220389
Programa: sistema de monitoreo de la calidad del aire. Práctica 6
Variables:
    opc = variable que almacena la opción en el menú principal
    documento = variable que almacena el documento de un usuario
    nombre = variable que almacena el nombre de un usuario
    password = variable que almacena el password de un usuario
    re_password = variable que almacena la confirmación del password
    perfil = variable que almacena si el perfil es de operador o administrador
    user = variable que almacena un usuario consultado por cedula
    user_actual = variable que almacena el id del usuario actual
    municipios = variable que guarda el diccionario de municipios
"""
def validar_documento(documento):
    """Esta función recibe un string y valida que sea numérico y 
    tenga 10 caracteres"""
    if documento.isnumeric() and len(documento) == 10:
        return True
    return False

def validar_nombre(nombre):
    """Esta función valida que un nombre ingresado contenga
    solo letras y espacios. Valida además que el nombre no esté en blanco. 
    Retorna True si la validación es correcta y False en cualquier otro caso"""
    if nombre.isspace() or not nombre:
        return False
    for secuencia in nombre.split(' '):
        if not secuencia.isalpha():
            return False
    return True

def validar_password(password, re_password):
    """Esta función recibe dos strings que representan
    las contraseñas y valida que no estén en blanco,
    que sean iguales y que el tamaño sea como mínimo 4 caracteres"""
    if password.isspace() or not password:
        return False
    if password != re_password:
        return False
    if len(password) < 4:
        return False
    return True

def nuevo_usuario():
    """
    En esta función se leen los datos para crear un nuevo usuario.
    Luego, hace llamadas a las funciones de validación de los datos y finalmente,
    llama a la función crear_usuario del módulo para tratar de crear un usuario
    Si se ha creado un usuario con éxito retorna True y en caso contrario False.
    """
    print(' --------  Crear usuario ---------')
    print('Escriba: -1 en cualquier momento para salir')
    while True:
        documento = input('ID usuario: ')
        if documento == '-1':
            return False
        if validar_documento(documento):
            break
        print('ID ingresado no valido')
        
    while True:
        nombre = input('Nombre de usuario: ')
        if nombre == '-1':
            return False
        if validar_nombre(nombre):
            break
        print('Nombre no valido')
        
    while True:
        password = input('Password del usuario de mínimo 4 caracteres: ')
        re_password = input('Vuelva a digitar el password: ')
        if password == '-1':
            return False
        if validar_password(password, re_password):
            break
        print('Password no valido. Reintente')
        
    while True:
        opc = input('''Seleccione el perfil del usuario:
        1. Operador
        2. Administrador
        -1. Salir''')
        if opc == '1':
            perfil = 'Operador'
            break
        elif opc == '2':
            perfil = 'Administrador'
            break
        elif opc == '-1':
            return False
        else:
            print('Opción no valida. Verifique')
            
    if not mn.crear_usuario(documento, nombre.title(), password, perfil):
        print('El documento ya está asociado a un usuario')
        return False
    
    return True
             
def editar_usuario():
    
    """Esta función permite editar el nombre,
    la contraseña o el perfil de un usuario registrado. En caso de poder
    editarlo devuelve True, sino, devuelve False"""
    print(' --------  Editar usuario ---------')
    print('Digite -1 en cualquier momento para salir: ')
    documento = input('Escriba el ID del usuario: ').strip()
    
    if documento == '-1':
        return False
    user = mn.consultar_usuario(documento)
    if user == -1:
        print('El usuario no puede editarse pues no existe')
        return False
 
    while True:
        print('Nombre de usuario actual: {}'.format(user[0]))
        nombre = input('Nuevo nombre de usuario o presione enter para no modificar: ').strip()
        if nombre == '-1':
            return False
        if nombre.isspace() or nombre == '':
            nombre = user[0]
            break
        if validar_nombre(nombre):
            break
        print('Nombre no valido')
        
    while True:
        print('Contraseña de usuario actual: {}'.format(user[1]))
        password = input('Password del usuario de mínimo 4 caracteres o presione enter para no modificar: ').strip()
        re_password = input('Vuelva a digitar el password o presione enter: ')
        if password == '-1':
            return False
        if password.isspace() or password == '':
            password = user[1]
            break
        if validar_password(password, re_password):
            break
        print('Password no valido. Reintente')
        
    while True:
        print('Perfil de usuario actual: {}'.format(user[2]))
        opc = input('''Seleccione el nuevo perfil del usuario o enter para no modificar:
        1. Operador
        2. Administrador
        -1. Salir''')
        if opc.isspace() or opc == '':
            perfil = user[2]
            break
        if opc == '1':
            perfil = 'Operador'
            break
        elif opc == '2':
            perfil = 'Administrador'
            break
        elif opc == '-1':
            return False
        else:
            print('Opción no valida. Verifique')
            
    if not mn.editar_usuario(documento, nombre.title(), password, perfil):
        print('El documento ya está asociado a un usuario')
        return False
    
    return True
    
def eliminar_usuario():
    """Esta función elimina un usuario registrado. Primero, valida que
    el usuario a eliminar exista, en caso de no existir no permite borrar. Luego,
    valida si el usuario a borrar es el actual, en caso de que sea el actual
    no lo permite borrar, y finalmente, borra el usuario si ninguna
    de las condiciones anteriores se cumplió y retorna True, en cualquier otro caso
    retorna False"""
    
    global user_actual
    documento = input('Escriba el documento del usuario a eliminar: ').strip()
    user = mn.consultar_usuario(documento)
    if user == -1:
        print('El usuario no existe y por tanto no se eliminará: ')
        return False
    if documento == user_actual:
        print('El usuario actual no puede eliminarse')
        return False
    
    while True:
        print('''
              Nombre: {0}
              Password: {1}
              Perfil: {2}'''.format(*user))
        conf = input('¿Está seguro de que quiere eliminar al usuario? s/n ').lower()
        if conf == 's':
            mn.eliminar_usuario(documento)
            break
        elif conf == 'n':
            print('No se eliminará')
            return False
        
def nueva_estacion():
    """
    Esta función, que no recibe argumentos, es la encargada de
    leer los datos para crear una nueva estación, validar su formato, enviarlos al módulo
    monitoreo para validar si la estación ya existe o no y en caso
    de que no exista, crea una nueva estación agregándola al diccionario
    que se encuentra en el módulo.
    """
    
    municipios = mn.obtener_municipios()
    while True:
        print('Seleccione un municipio de la lista o escriba -1 para salir: ')
        for numero, municipio in enumerate(municipios, 1):
            print(numero, municipio)
        opc = input()
        
        if opc == "-1":
            return False
        
        if opc.isnumeric():
            opc = int(opc)
            if opc > 10 or opc < 1:
                print('Digitó una opción no valida. Vuelva a intentar')
            else:
                seleccion = municipios[opc-1]
                break
        else:
            print('Digitó una opción no valida. Vuelva a intentar')
            
    while True:
        nombre_estacion = input('Escriba el nombre de la nueva estacion o -1 para salir: ').strip()
        if nombre_estacion == "-1":
            return False
        if nombre_estacion.isspace() or not nombre_estacion:
            print('El nombre no puede estar vacío. Intente nuevamente')
        else:
            break
    
    if mn.crear_estacion(nombre_estacion.title(), seleccion):
        print('Estacion creada satisfactoriamente')
        return True
    print('La estación ya existe. No se creará una nueva')
    return False

def seleccionar_estacion():
    """
    Esta función no recibe argumentos. La función se encarga
    de listar las estaciones guardadas en el diccionario de estaciones,
    luego permite al usuario seleccionar una estación y retorna
    la clave y los valores de la estación seleccionada. Si el usuario
    decide salir retorna una tupla dos elementos con valor False
    """
    estaciones = mn.obtener_estaciones()
    print('''Seleccione un numero o -1 para salir''')
    for key, value in estaciones.items():
        print('''{0}: Nombre: {1} Municipio: {2}     
        '''.format(key, *value))
        
    while True:
        opc = input().strip()
        if opc == '-1':
            return (False, False)
    
        if opc.isnumeric():
            opc = int(opc)
            if opc > len(estaciones) or opc < 0:
                print('No seleccionó una estación valida. Reintente')
            else:
                opc = str(opc)
                return opc, estaciones[opc]
        else:
            print('No eligió una opción valida. Reintente')
            
def listar_municipios():
    """
    Esta función permite listar los municipios almacenados
    en el sistema y seleccionar un municipio de la lista.
    Si el usuario decide salir retonar un valor False, o sino
    retorna el valor del municipio seleccionado.
    La función no recibe argumentos
    """
    municipios = mn.obtener_municipios()
    while True:
        print('Seleccione un municipio de la lista o escriba -1 para salir: ')
        for numero, municipio in enumerate(municipios, 1):
            print(numero, municipio)
        opc = input()
        
        if opc == "-1":
            return False
        
        if opc.isnumeric():
            opc = int(opc)
            if opc > len(municipios) or opc < 1:
                print('Digitó una opción no valida. Vuelva a intentar')
            else:
                seleccion = municipios[opc-1]
                break
        else:
            print('Digitó una opción no valida. Vuelva a intentar')
    
    return seleccion
  
def editar_estacion():
    """
    Esta función no recibe argumentos. 
    Permite al usuario seleccionar una estación y agregar nuevos valores
    para el nombre y el municipio de la estación, luego de tener estos valores
    se hace una llamada a la función editar_estacion del modulo monitoreo
    y actualiza los nombres, si el usuario no quiere editar ningún valor
    la estación se actualiza con los mismos datos
    """
    estacion_id, datos = seleccionar_estacion()
    if not estacion_id:
        return False
    
    nuevo_municipio = datos[1]
    
    print('--- Editar estacion ---')
    print('Municipio actual:', datos[1])
    resp = listar_municipios()
    if resp:
        nuevo_municipio = resp
        
    while True:
        print('Nombre actual:', datos[0])
        nuevo_nombre = input('Escriba el nuevo nombre de la estacion o presione enter si no quiere modificarlo ').strip()
        if nuevo_nombre.isspace() or not nuevo_nombre:
            nuevo_nombre = datos[0]
        else:
            nuevo_nombre = nuevo_nombre.title()
        break
    
    if mn.editar_estacion(estacion_id, nuevo_nombre, nuevo_municipio):
        return True
    print(''''Ya existe otra estación con el mismo nombre en el mismo municipio.
          No se editará la estación actual''')
    return False

def eliminar_estacion():
    """Esta función es la encargadad de eliminar una estación
    primero obtiene los valores de la estación a eliminar,
    luego, llama a la función elimiar estación del módulo
    y si esta función retorna True significa que pudo
    eliminar la estación y la función finaliza retornando True"""
    estacion_id, valores = seleccionar_estacion()
    if not estacion_id:
        return False
    if not mn.eliminar_estacion(estacion_id):
        return False
    return True

def gestionar_estaciones():
    """Esta función presenta el menú correspondiente
    a la opción de gestionar estaciones de los adminsitradores.
    El usuario puede gestionar 4 opciones, las primeras 3 hacen
    referencia a una operación sobre las estaciones (crear, modificar o eliminar)
    y para cada una de ellas 3 hace una llamada de función según corresponda
    y la última permite retornar al menú de administrador. Esta función retorna el valor None"""
    while True:
        opc = input('''
        Seleccione una opción para gestionar estaciones:
            1. Agregar nueva estacion
            2. Editar una estacion
            3. Eliminar una estacion
            4. Salir
            ''')
        if opc == '1':
            if nueva_estacion():
                print('Estacion agregada con éxito')
            else:
                print('No se pudo agregar la estacion')
        elif opc == '2':
            if editar_estacion():
                print('Estacion editada con éxito')
            else:
                print('No se editó ninguna estacion')
        elif opc == '3':
            if eliminar_estacion():
                print('Estación eliminada exitosamente')
            else:
                print('Estación con medidas asociadas. No se eliminará')
        elif opc == '4':
            return
        else:
            print('Seleccionó una opción no valida. Reintente')

def gestionar_usuarios():
    """Esta función presenta el menú correspondiente
    a la opción de gestionar usuarios de los adminsitradores.
    El usuario puede gestionar 4 opciones, las primeras 3 hacen
    referencia a una operación sobre los usuarios (crear, modificar o eliminar)
    y para cada una de ellas 3 hace una llamada de función según corresponda
    y la última permite retornar al menú de administrador. Esta función retorna el valor None"""
    while True:
        opc = input('''
        Seleccione una opción para gestionar usuarios:
            1. Agregar nuevo usuario
            2. Editar un usuario
            3. Eliminar un usuario
            4. Salir
            ''')
        if opc == '1':
            if nuevo_usuario():
                print('Usuario agregado con éxito')
            else:
                print('No se pudo agregar un usuario')
        elif opc == '2':
            if editar_usuario():
                print('Usuario editado con éxito')
            else:
                print('No se pudo editar un usuario')
        elif opc == '3':
            if eliminar_usuario():
                print('Usuario eliminado con éxito')
            else:
                print('No se pudo eliminar un usuario')
        elif opc == '4':
            return
        else:
            print('Seleccionó una opción no valida. Reintente')

def seleccionar_estacion_municipio(municipio):
    """
    Esta función recibe el código del municipio de donde
    se quieren extraer las estaciones de medición.
    Si en el municipio no hay estaciones se muestra un mensaje y se retorna
    Falso.
    Si en el municipio hay estaciones se listan las estaciones
    y se le pide ingresar al usuario el código de la estación o -1
    para volver al menú de municipios. Si el usuario selecciona
    una estación, se retorna la estación, si el usuario selecciona -1
    la función retorna False.
    """
    print('Municipio seleccionado: {}'.format(municipio))
    estaciones = mn.consultar_estaciones_municipio(municipio)
    if not estaciones:
        print('En este municipio no hay estaciones registradas')
        return False
    else:
        for key, value in estaciones.items():
            print('''
            Código estacion: {0}
            Nombre:          {1}
            Municipio:       {2}
                  '''.format(key, *value))
        while True:
            opc = input('Seleccione el código de la estacion o -1 para seleccionar municipio: ').strip()
            if opc == '-1':
                return False
            if opc not in estaciones:
                print('Seleccionó un código no valido')
                continue
            return {opc:estaciones[opc]}

def validar_medidas(valor, minimo, maximo):
    """Esta función recibe el valor de las medidas
    que se quieren ingresar y los valores máximos y mínimos de la medida. Si el valor
    es ND o está entre los límites retorna True, sino, False"""
    if valor == 'ND':
        return True
    valor = float(valor)
    minimo = float(minimo)
    maximo = float(maximo)
    if minimo <= valor <= maximo:
        return True
    
    return False
    
    
def ingresar_medidas(estacion):
    """
    Esta función recibe el código de la estación a la que
    se le quiere asignar la medida, la función
    crea una lista con los límites para cada medida y permite
    ingresar cada valor de la medida, si cada valor ingresado
    no cumple con la validación hace que el usuario tenga que volver
    a ingresar la medida, si el usuario escribe -1 en cualquier momento
    la función retorna None.
    """
    
    valores = mn.obtener_limites()
    medidas = []
    
    for medida in valores:
        while True:
            print('Escriba el valor numérico de {0} o ND si no está disponible. -1 para salir'.format(medida[0]))
            lectura = input().strip()
            if lectura == '-1':
                return
            resp = validar_medidas(lectura.upper(), medida[1], medida[2])
            if resp:
                medidas.append(lectura)
                break
            else:
                print('Valor ingresado no valido')
            
    mn.agregar_medida(estacion, medidas)
    return True
   
def listar_medidas(codigo, estacion):
    """
    Esta función recibe un string correspondiente al código de la estación
    y un diccionario con los datos de la estación
    sobre la que se van a listar las medidas. Luego, hace un llamado
    a la función consultar_medidas_estaciones la cual le retorna
    un iterable donde cada elemento son las medidas de la estación correspondiente
    """
    medidas = mn.consultar_medidas_estaciones(codigo)
    nombre, municipio = estacion[codigo]
    limites = mn.obtener_limites()
    encabezados = ["Fecha"]
    datos = []
    tamanho = [19]
    print("""
    Nombre estacion:    {0}
    Municipio estacion: {1}
    """.format(nombre, municipio), end="")
    
    for i in limites:
        encabezados.append(i[0]+ " " + i[3])
    for i in range(len(limites)):
        tamanho.append(7)
    for medida in medidas:
        aux = [medida[0]]
        aux += re.split(';|{|}|,', medida[2])[1:-1]
        datos.append(aux)
    
        
    utils.imprimir_tabla(datos, tamanho, encabezados)
    
def menu_operador():
    """
    Esta función representa el menú del operador,
    en ella se selecciona la acción a realizar entre las tres
    posibles: ingresar medidas, listar medidas o salir.
    Si el usuario decide salir
    la función retorna None, si el usuario elige alguna
    de las operaciones como usuario operador, 
    la función se encarga de redirigirlo a cada subprograma
    del aplicativo principal.
    """
    print('----- Operador -----')
    
    while True:
        print('''
        Seleccione:
        1: Ingresar medidas
        2: Listar medidas
        3: Salir
          ''')
        opc = input()
        if opc == '3':
            return
        if opc != "1" and opc != "2":
            print('Digitó una opción no valida. Reintente')
            continue

            
        while True:
            municipio = listar_municipios()
            if not municipio:
                return
            estacion = seleccionar_estacion_municipio(municipio)
            if estacion:
                break
            
        for key in estacion.keys():
            codigo_estacion = key
            
        if opc == "1":
            if(ingresar_medidas(codigo_estacion)):
                print('Se agregaron las medidas satisfactoriamente')
            else:
                print('No se agregaron medidas nuevas')
        else:
            listar_medidas(codigo_estacion, estacion)

def menu_administrador():
    """
    Esta función presenta el menú básico de administrador del aplicativo.
    No recibe argumentos y retorna el valor None. Existen 3 opciones de menú,
    la primera correspondiente a volver al menú principal,
    y las otras dos a las operaciones básicas que puede realizar
    un administrador: gestionar estaciones y usuarios.
    Para cada una de estas operaciones hace una llamada de función
    """
    print('--- Administrador ----')
    while True:
        opc = input('''
        Seleccione una opción como administrador:
            1. Volver al menu inicial
            2. Gestionar estaciones
            3. Gestionar usuarios
            ''')
        if opc == '1':
            return
        if opc == '2':
            gestionar_estaciones()
        elif opc == '3':
            gestionar_usuarios()
        else:
            print('Seleccionó una opción no valida. Reintente asdasd')


def usuario_visitante():
    """
    Esta función es el menu principal de los usuarios no registrados.
    Primero se debe elegir la fecha entre las tres opciones posibles
    ultimos 7 días, últimos 30 días o manualmente
    """
    while True:
        opc = input('''
    Seleccione las fechas para ver los datos:
    1. Últimos 7 días
    2. Últimos 30 días
    3. Manualmente
    4. Salir            
    ''')
        if opc.isnumeric():
            opc = int(opc)
            if 1 <= opc <= 3:
                break
            if opc == 4:
                return
        print('No ha seleccionado una opción valida')
        
    variables = set()
    nombres_medidas = mn.obtener_limites()
    municipios = set()
    
    while True:
        i = 1
        for nombre in nombres_medidas:
            print(i,'',nombre[0])
            i += 1
        print(i,"Seleccionar todo")
        print(0,"Terminar la selección")
        print(-1,"Salir sin seleccionar")
        opc = input("Seleccione las variables que quiere visualizar\n")
        
        if opc == '-1':
            return
        if opc.isnumeric():
            opc = int(opc)
            if opc == 0:
                break
            if opc == i:
                variables = {i for i in range(len(nombres_medidas))}
                break
            if 1 <= opc <= len(nombres_medidas):
                variables.add(opc-1)
                continue
        print('Seleccionó una opción no valida')
        
    while True:
        opc = input("""
        1. Para agregar un municipio
        2. Para agregar todos los municipios
        3. Para ir al siguiente paso
        4. Para salir sin hacer nada            
        """).strip()
        if opc == "1":
            municipio = listar_municipios()
            if not municipio:
                continue
            municipios.add(municipio)
            continue
        if opc == "2":
            municipios = set(mn.obtener_municipios())
            break
        if opc == "4":
            return
        if opc == "3":
            break
        else:
            print('Opción no valida')
        
            
    
    print(variables)
    print(municipios)

def inicio_sesion():
    """
    Esta función permite en primer lugar leer los datos de inicio de
    sesión si es la primera vez que se usa el sistema.
    Luego de una respuesta True del módulo monitoreo para el inicio
    de sesión, actualiza la variable global user_actual con
    el documento del usuario que inició sesión y retorna en
    la variable perfil el rol del usuario en el sistema,
    si no se pudo iniciar sesión la variable perfil se retorna
    con el valor False. 
    """
    global user_actual
    print('Digite -1 en cualquier momento para salir')
    if user_actual == '':
        print('Inicio de sesión')
        usuario = input('Digite su nombre: ')
        if usuario == '-1':
            return False
        password = input('Digite su contraseña: ')
        if password == '-1':
            return False
        resp = mn.iniciar_sesion(usuario, password)
        if resp == -1:
            print('Usuario o contraseña no validos')
            return False
        user_actual, perfil = resp
        return perfil
    
def usuario_registrado():
    """
    Esta función se encarga de validar si ya se inición sesión,
    si no se ha iniciado sesión hace una llamada a la función
    inicio_sesion y actualiza la variable perfil con el valor
    retornado. Si el valor retornado es False significa
    que no se pudo iniciar sesión y devuelve al usuario al menu principal,
    sino, valida qué valor de rol de usuario tiene y redirige al usuario
    según.
    """
    global user_actual
    user_actual = ""
    
    
    perfil = inicio_sesion()
    
    if not perfil:
        return
    elif perfil == 'Administrador':
        menu_administrador()
    else:
        menu_operador()
    

def menu():
    """
    Esta función se encarga de mostrar el menú del programa
    y de redirigir al usuario a cada una de las partes principales
    del programa según si es usuario visitante, registrado o quiere salir
    """
    while True:
        print('--- Bienvenido al servicio de monitoreo de la calidad del aire del Valle de Aburrá ---')
        opc = input('''
        Seleccione:
            1: Usuario visitante
            2: Usuario registrado
            3: Salir
        ''')
        if opc == '1':
            usuario_visitante()
        elif opc == '2':
            usuario_registrado()
        elif opc == '3':
            return
        else:
            print('Seleccionó una opción no valida')
            
              

if __name__ == '__main__':
    mn.cargar_estructuras()
    menu()
    mn.escribir_archivo()

