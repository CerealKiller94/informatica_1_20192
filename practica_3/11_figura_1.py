'''
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo que 
muestre el siguiente patrón 
en la pantalla:

#
###
#####
#######
#########

El tamaño del patrón estará 
determinado por un número 
entero impar que ingrese el 
usuario. En el ejemplo mostrado, 
el tamaño de la figura es 9.


Análisis: 
Entradas: 
n (entero impar que controla
la cantidad de figuras)

Auxiliares:
i: variable controladora del ciclo
principal, de ella depende la 
cantidad de figuras por linea
k: variable controladora del ciclo
interno, de ella depende la
aparición de cada figura


salida: se imprimen los
numerales desde la instrucción
de salida
'''
while True:
    n = int(input('Digite un número impar: '))
    if n % 2 and n >= 0:
        break
    print('Digite un número impar positivo')

for i in range(1, n+1, 2):
    for k in range(1, i+1):
        print('#', end='')
    print('')
