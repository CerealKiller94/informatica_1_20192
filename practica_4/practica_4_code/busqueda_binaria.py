# Busqueda binaria

"""
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Implemente el algoritmo de búsqueda binaria, 
completando el archivo busqueda_binaria_template.py y 
guiándose por las indicaciones que aparecen en los comentarios. 
Asuma que la lista de datos está ordenada.

Análisis:
Entradas: num (si se elimina el comentario
se puede usar la variable para obtener un valor numérico
ingresado por el usuario y buscarlo)
auxiliares:
ban: variable booleana que indica si se encontró (True) o
        no (False) el valor buscado
bajo: índice inferior del segmento de búsqueda
alto: índice superior del segmento de búsqueda
iteraciones: contador de iteraciones
L: lista ordenada con valores numéricos para buscar
central: variable que almacena el valor medio del segmento
de búsqueda y se usa para comparar con el valor buscado
num: por defecto es una variable que tiene un valor
        fijo, este valor se puede cambiar manualmente
        desde el código fuente o hacer que se lea desde entrada

salida: central (en caso de encontrar el valor dentro
de la lista, se muestra el índice en que fue encontrado)
iteraciones: muestra el número total de iteraciones
que hizo el algoritmo

"""

# Variables a emplear
L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]
iteraciones = 0 # Contador de iteraciones
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



