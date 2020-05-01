from random import uniform, randint

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

def sortBurbuja(L):
    ''' 
        Recibe una lista de floats
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
            if L[i] > L[i+1]:
                L[i], L[i+1] = L[i+1], L[i]
                is_unordered = True
            i += 1
    
    return iter_number

def sortSeleccion(L):
    ''' 
        Recibe una lista de floats
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
        menor_indx = inicio
        while i < tamanho:
            iter_number += 1
            if L[menor_indx] > L[i]:
                menor_indx = i
            i += 1
        L[inicio], L[menor_indx] = L[menor_indx], L[inicio]
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
        number = randint(minimo, maximo)
        lista.append(number)
    
    return lista

"""
lista = createRandomList(400, 21.1, 10.5)

print(sortBurbuja(lista[:]))
"""
