# Busqueda lineal

# Variables a emplear
L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]

''' 
Variable que indica si se encontró la clave en la lista tal que:
- Ban = False, la clave no esta en la lista
- Ban = True, la clave esta en la lista
'''
ban = False 
iteraciones = 0
num = 57  # Valor de prueba para buscar en la lista

#num = int(input('Digite un número para buscar en la lista: '))
"""La línea anterior se puede "descomentar" para hacer que el algoritmo
busque un número entero ingresado por el usuario""" 

print('************************* Búsqueda lineal *********************')
print('Número: {}\n'.format(num))

while iteraciones < len(L):
    print('Iteración: {}, L[{}] = {}'.format(iteraciones, iteraciones, 
                                             L[iteraciones]))
    if L[iteraciones] == num:
        ban = True
        break
    
    iteraciones += 1
    
if ban:
    print('\nNúmero encontrado en la posición: {}'.format(iteraciones))
else:
    print('\nNúmero no encontrado')
    
print('\nCantidad de iteraciones: {}'.format(iteraciones))

print('************************* Fin búsqueda lineal *******************')


