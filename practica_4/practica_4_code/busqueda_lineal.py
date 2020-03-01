# Busqueda lineal

"""
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Implemente el algoritmo de búsqueda lineal, 
completando el archivo 
busqueda_lineal_template.py y guiándose por las 
indicaciones que aparecen 
en los comentarios. Ayuda: recuerde el uso de la 
instrucción break.
Análisis:
    entradas:
        num: En caso de eliminar el comentario correspondiente
        esta variable permite almacenar un valor ingresado
        por el usuario
    auxiliares:
        ban: variable booleana que indica si se encontró (True) o
        no (False) el valor buscado
        iteraciones: cuenta la cantidad de iteraciones y va
        almacenando cada índice de búsqueda secuencial 
        num: por defecto es una variable que tiene un valor
        fijo, este valor se puede cambiar manualmente
        desde el código fuente o hacer que se lea desde entrada
    salidas:
        * iteraciones: en caso de encontrar el valor buscado,
        iteraciones muestra el valor del índice en que está
        localizado el valor, por otro lado, si no encuentra
        el valor, iteraciones muestra el número de veces
        que se repitió el ciclo de búsqueda
        * Para cada iteración del ciclo se muestra: el número total 
        de iteraciones hasta el momento, la posición actual en la lista
        y el valor de la lista en la posición actual
        

"""

# Variables a emplear
L = [-50, -45, -23, -21, -14, -9, -2, 0, 1, 3, 5, 16, 17, 24, 29, 30, 40, 52, 53, 92]

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


