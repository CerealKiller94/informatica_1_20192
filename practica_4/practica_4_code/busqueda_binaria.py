# Busqueda binaria

# Variables a emplear
L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]
iteraciones = 0 # Contador de iteraciones
''' 
Variable que indica si se encontró la clave en la lista tal que:
- Ban = False, la clave no esta en la lista
- Ban = True, la clave esta en la lista
'''
ban = False 

num = 57  # Valor de prueba para buscar en la lista
bajo = 0 # Índice inferior
alto = len(L) - 1 # Índice superior

#num = int(input('Digite un número para buscar en la lista: '))
"""La línea anterior se puede "descomentar" para hacer que el algoritmo
busque un número entero ingresado por el usuario""" 

print('************************* Búsqueda binaria *********************')
print('Número: {}\n'.format(num))

while bajo <= alto:
    iteraciones += 1
    central = (alto + bajo)//2
    
    print('Iteración: {}, central = {}, L[central] = {}, Intervalo: {}'.format(
        iteraciones, central, L[central], L[bajo:alto+1]))
    
    if L[central] == num:
        ban = True
        break
    
    if L[central] > num:
        alto = central - 1
    else:
        bajo = central + 1
    

''' Imprima el mensaje en el cual se informe la posición
en la que se encontró el número, o un mensaje indicando que no se encontró'''

if ban:
    print('\nNúmero encontrado en la posición {}'.format(central))
else:
    print('\nNúmero no encontrado')
    
print('\nCantidad de iteraciones: {}'.format(iteraciones))

print('************************* Búsqueda binaria *********************')



