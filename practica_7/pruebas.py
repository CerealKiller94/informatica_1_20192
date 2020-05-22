# -*- coding: utf-8 -*-

from sortfunc import sortSeleccion, sortBurbuja
from random import uniform


def hacer_prueba_caja_negra_burbuja():
    
    """
    Se harán pruebas de caja negra para el
    algoritmos de ordenamiento burbuja. Se usará la función
    sort de python como función de control para validar que las
    listas queden ordenadas.
    La especificación de la función exige que la 
    función reciba una lista de números y un valor opcional
    que indica el orden de la lista.
    """
    
    #Ordenar una lista de forma creciente
    lista = [uniform(-15, 40) for i in range(50)] #Lista aleatoria de 50 valores float entre -15 y 40
    l_copy = lista.copy()
    sortBurbuja(lista)
    l_copy.sort()
    if lista == l_copy:
        print("""
        La prueba para una lista de 50 números flotantes negativos y positivos
        en orden ascendente fue superada
        para el algoritmo de ordenamiento de burbuja
              """)
    else:
        print("""
        La prueba para una lista de 50 números flotantes negativos y positivos
        en orden ascendente no fue superada
        para el algoritmo de ordenamiento de burbuja
              """)
    
    #Ordenar una lista de forma decreciente
    lista = [uniform(20, 57) for i in range(75)] #Lista aleatoria de 75 valores float entre 20 y 57
    l_copy = lista.copy()
    sortBurbuja(lista, 1)
    l_copy.sort(reverse=True)
    if lista == l_copy:
        print("""
        La prueba para una lista de 75 números flotantes positivos en orden decreciente fue superada
        para el algoritmo de ordenamiento de burbuja
              """)
    else:
        print("""La prueba para una lista de 75 números flotantes positivos en orden decreciente fue superada
        para el algoritmo de ordenamiento de burbuja
              """)
              
    #Ordenar una lista ya ordenada creciente
    lista = [-2,-1,0,1,5,7,8,15,20] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortBurbuja(lista)
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada en forma creciente de números para 
        el algoritmo de burbuja fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma creciente de números para 
        el algoritmo de burbuja no fue superada""")
        
    #Ordenar una lista ya ordenada decreciente
    lista = [1000,980,425,400,395,350,300,250,150,100,25] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortBurbuja(lista, 1)
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada  en forma decreciente de números para 
        el algoritmo de burbuja fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma decreciente de números para 
        el algoritmo de burbuja no fue superada""")
        
    #Ordenar una lista ya ordenada creciente de forma decreciente
    lista = [-100.1,-99.25,-25.36,-20.15,-19,-30,-2,-1,0,1,5,7,8,15,20] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortBurbuja(lista,1)
    l_copy.sort(reverse=True)
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada en forma creciente de forma decreciente de números para 
        el algoritmo de burbuja fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma creciente de forma decreciente de números para 
        el algoritmo de burbuja no fue superada""")
        
     #Ordenar una lista ya ordenada decreciente de forma creciente
    lista = [1000,980.26,425,400.25,395,350.15,300,250,150,100.3,25,15,5.6,-20,-22.1,25.1] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortBurbuja(lista)
    l_copy.sort()
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada en forma decreciente de forma creciente de números para 
        el algoritmo de burbuja fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma decreciente de forma creciente de números para 
        el algoritmo de burbuja no fue superada""")
    
    #Ordenar una lista vacía
    lista = []
    l_copy = lista.copy()
    sortBurbuja(lista)
    l_copy.sort()
    if lista == l_copy:
        print("""
        prueba de ordenamiento de lista vacía para 
        ordenamiento burbuja superada
              """)
    else:
        print("""
        Prueba de ordenamiento de lista vacía para 
        ordenamiento burbuja superada
              """)
    
def hacer_prueba_caja_negra_seleccion():
    """
    Se harán pruebas de caja negra para el
    algoritmo de ordenamiento por selección. Se usará la función
    sort de python como función de control para validar que las
    listas queden ordenadas.
    La especificación de la función exige que 
    reciba una lista de números y un valor opcional
    que indica el orden de la lista. 1 orden decreciente y cualquier otro o ninguno 
    para orden creciente
    """
    
    #Ordenar una lista de forma creciente
    lista = [uniform(-100, 73) for i in range(81)] #Lista aleatoria de 81 valores float entre -100 y 73
    l_copy = lista.copy()
    sortSeleccion(lista)
    l_copy.sort()
    if lista == l_copy:
        print("""
        La prueba para una lista de 81 números flotantes negativos y positivos
        en orden ascendente fue superada
        para el algoritmo de ordenamiento de seleccion
              """)
    else:
        print("""
        La prueba para una lista de 81 números flotantes negativos y positivos
        en orden ascendente no fue superada
        para el algoritmo de ordenamiento de seleccion
              """)
    
    #Ordenar una lista de forma decreciente
    lista = [uniform(-210, 457) for i in range(53)] #Lista aleatoria de 53 valores float entre -210 y 457
    l_copy = lista.copy()
    sortSeleccion(lista, 1)
    l_copy.sort(reverse=True)
    if lista == l_copy:
        print("""
        La prueba para una lista de 53 números flotantes positivos y negativos en orden decreciente fue superada
        para el algoritmo de ordenamiento de burbuja
              """)
    else:
        print("""La prueba para una lista de 53 números flotantes positivos y negativos en orden decreciente fue superada
        para el algoritmo de ordenamiento de burbuja
              """)
              
    #Ordenar una lista ya ordenada creciente
    lista = [-45,-12,0,123,522,714,875,1550,20000] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortSeleccion(lista)
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada en forma creciente de números para 
        el algoritmo de selección fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma creciente de números para 
        el algoritmo de seleccion no fue superada""")
        
    #Ordenar una lista ya ordenada decreciente
    lista = [9000,8800,4251,4001,3954,3500.2,3001.1,2512,1500,1002.1,251.12] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortSeleccion(lista, 1)
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada  en forma decreciente de números para 
        el algoritmo de seleccion fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma decreciente de números para 
        el algoritmo de seleccion no fue superada""")
        
    #Ordenar una lista ya ordenada creciente de forma decreciente
    lista = [-1002.122,-99.215,-25.236,-20.1511,-19.25,-26,-1,-0.99,0,12,6,10,15,152,200] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortSeleccion(lista,1)
    l_copy.sort(reverse=True)
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada en forma creciente de forma decreciente de números para 
        el algoritmo de seleccion fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma creciente de forma decreciente de números para 
        el algoritmo de seleccion no fue superada""")
        
     #Ordenar una lista ya ordenada decreciente de forma creciente
    lista = [1000,980.26,425,400.25,395,350.15,300,250,150,100.3,25,15,5.6,-20,-22.1,25.1] #Lista con valores ya ordenados
    l_copy = lista.copy()
    sortSeleccion(lista)
    l_copy.sort()
    if lista == l_copy:
        print("""
        La prueba para una lista ya ordenada en forma decreciente de forma creciente de números para 
        el algoritmo de seleccion fue superada""")
    else:
        print("""
        La prueba para una lista ya ordenada en forma decreciente de forma creciente de números para 
        el algoritmo de seleccion no fue superada""")
    
    #Ordenar una lista vacía
    lista = []
    l_copy = lista.copy()
    sortSeleccion(lista)
    l_copy.sort()
    if lista == l_copy:
        print("""
        prueba de ordenamiento de lista vacía para 
        ordenamiento seleccion superada
              """)
    else:
        print("""
        Prueba de ordenamiento de lista vacía para 
        ordenamiento burbuja superada
              """)


def pruebas_caja_blanca_burbuja():
    """
    Esta función hace pruebas de caja blanca al algoritmo
    de burbuja
    """
    #Prueba con un arreglo vacío que no entra al ciclo más interno
    lista = []
    sortBurbuja(lista)
    l_copy = lista.copy()
    l_copy.sort()
    assert lista == l_copy, "Las listas deben ser iguales. Falló el algortimo. Para listas vacías"
    #Misma prueba pero de mayor a menor
    lista = []
    sortBurbuja(lista, orden=1)
    l_copy = lista.copy()
    l_copy.sort(reverse=True)
    assert lista == l_copy, "Las listas deben ser iguales. Falló el algortimo. Para listas vacías en orden inverso"
    #Prueba con una lista con solo dos elementos desordenados para que solo entre una vez al if
    lista = [1,2,3,4,5,7,6,8,9,10]
    sortBurbuja(lista)
    l_copy = lista.copy()
    l_copy.sort()
    assert lista == l_copy, "Las listas deben ser iguales. Falló el algortimo para una lista con dos elementos desordenados"
    #Misma prueba con una lista con solo dos elementos desordenados para que solo entre una vez al if.
    #De mayor a menor
    lista = [10,9,8,7,5,6,4,3,2,1]
    sortBurbuja(lista, orden=1)
    l_copy = lista.copy()
    l_copy.sort(reverse=True)
    assert lista == l_copy, "Las listas deben ser iguales. Falló el algortimo para una lista con dos elementos desordenados en forma inversa"
    #Lista totalmente ordenada que nunca entra en las codiciones
    #de ordenamiento pero sí en los ciclos
    lista = [78,101,106,115,123,178]
    sortBurbuja(lista)
    l_copy = lista.copy()
    l_copy.sort()
    assert lista == l_copy, "Las listas deben ser iguales. Falló el algortimo para una lista totalmente ordenada"
    #Lista totalmente ordenada en sentido inverso que nunca entra en las codiciones
    #de ordenamiento pero sí en los ciclos
    lista = [78,101,106,115,123,178]
    sortBurbuja(lista)
    l_copy = lista.copy()
    l_copy.sort()
    assert lista == l_copy, "Las listas deben ser iguales. Falló el algortimo para una lista ordenada en sentido inverso"
    
# hacer_prueba_caja_negra_burbuja()
#hacer_prueba_caja_negra_seleccion()
#pruebas_caja_blanca_burbuja()

