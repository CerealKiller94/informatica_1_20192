from random import uniform

def loadFromFile(name):
    ''' 
        Recibe el nombre de un archivo (str)
        Retorna una lista de floats con cada uno 
        de los números extraídos del archivo name
    '''
    lista = []
    with open(name, "r") as file:
        for number in file:
            lista.append(float(number.strip("\n")))
        
    return lista

def sortBurbuja(L, orden=0):
    ''' 
        Recibe una lista de floats y una entero que indica 
        si la lista se ordenará de mayor a menor
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de burbuja
        para ordenar la lista L
    '''
    is_unordered = True
    iter_number = 0
    final = 0
    tamanho = len(L)
    while is_unordered:
        iter_number += 1
        is_unordered = False
        i = 0
        final += 1
        while i < tamanho-final:
            iter_number += 1
            if orden == 1:
                if L[i] < L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    is_unordered = True
            else:
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    is_unordered = True
            i += 1
    
    return iter_number

def sortSeleccion(L, orden=0):
    ''' 
        Recibe una lista de floats y un número entero
        que si vale 1 ordena la lista de mayor a menor.
        Retorna la cantidad de ciclos (int)
        que se toma el algoritmo de selección
        para ordenar la lista L
    '''
    inicio = 0
    tamanho = len(L)
    iter_number = 0
    
    while inicio < tamanho-1:
        
        iter_number += 1
        i = inicio + 1
        indx = inicio
        while i < tamanho:
            iter_number += 1
            if orden == 1:
                if L[indx] < L[i]:
                    indx = i
            else:
                if L[indx] > L[i]:
                    indx = i
            i += 1
        L[inicio], L[indx] = L[indx], L[inicio]
        inicio += 1
    
    return iter_number
    

def createRandomList(size, minimo, maximo):
    '''
    Retorna un lista de size números aleatorios. Cada elemento de la lista debe 
    estar en el rango [minimo, maximo]
    
    Parámetros
        n: cantidad de elementos a poner en la lista
        minimo: número mínimo que puede haber en la lista
        maximo: número máximo que puede haber en la lista
    '''
    lista = []
    for i in range(size):
        number = uniform(minimo, maximo)
        lista.append(number)
    
    return lista


"""
lista = createRandomList(20, 10, 50)

print(sortSeleccion(lista[:], 1))
"""

