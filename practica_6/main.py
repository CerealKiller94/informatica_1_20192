#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import monitoreo as mn
user_actual = ''

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
    if nombre.isspace():
        return False
    for secuencia in nombre.split(' '):
        if not secuencia.isalpha():
            return False
    return True

def validar_password(password, re_password):
    """Esta función recibe dos strings que representan
    las contraseñas y valida que no estén en blanco,
    que sean iguales y que el tamaño sea como mínimo 4 caracteres"""
    if password.isspace():
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
            
    if not mn.crear_usuario(documento, nombre, password, perfil):
        print('El documento ya está asociado a un usuario')
        return False
    
    return True
             
def editar_usuario():
    
    """Esta función permite editar el nombre,
    la contraseña o el perfil de un usuario registrado. En caso de poder
    editarlo devuelve True, sino, devuelve False"""
    print(' --------  Editar usuario ---------')
    print('Digite -1 en cualquier momento para salir: ')
    documento = input('Escriba el ID del usuario: ').strip(' ')
    
    if documento == '-1':
        return False
    user = mn.consultar_usuario(documento)
    if user == -1:
        print('El usuario no puede editarse pues no existe')
        return False
 
    while True:
        print('Nombre de usuario actual: {}'.format(user[0]))
        nombre = input('Nuevo nombre de usuario o presione enter para no modificar: ').strip(' ')
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
        password = input('Password del usuario de mínimo 4 caracteres o presione enter para no modificar: ').strip(' ')
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
            
    if not mn.editar_usuario(documento, nombre, password, perfil):
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
    documento = input('Escriba el documento del usuario a eliminar: ').strip(' ')
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

def gestionar_usuarios():
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

def menu_administrador():
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
            pass
        if opc == '3':
            gestionar_usuarios()
        else:
            print('Seleccionó una opción no valida. Reintente')

def usuario_visitante():
    pass

def usuario_registrado():
    global user_actual
    print('Digite -1 en cualquier momento para salir')
    if user_actual == '':
        print('Inicio de sesión')
        usuario = input('Digite su nombre: ')
        if usuario == '-1':
            return
        password = input('Digite su contraseña: ')
        if password == '-1':
            return
        resp = mn.iniciar_sesion(usuario, password)
        if resp == -1:
            print('Usuario o contraseña no validos')
            return
        user_actual, perfil = resp
    if perfil == 'Administrador':
        menu_administrador()
    else:
        pass

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

