'''
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo 
que muestre el siguiente patrón 
en la pantalla:

*                 *
***           ***
*****      *****
**************


El tamaño del patrón estará 
determinado por un número 
entero impar que ingrese el 
usuario. En el ejemplo mostrado, 
el tamaño de la figura es 7.



Análisis: 
Entradas: 
n (entero que controla
la cantidad de figuras)

Auxiliares:
blancos: variable que controla,
la cantidad de espacios en blanco,
y el final de la secuencia.
j: variable controladora de los
ciclos que describen las
figuras y los espacios en blanco
figuras: variable controladora del ciclo
interno, de ella depende la
cantidad máxima de figuras
que aparecen, siempre impar


salida: se imprimen los
asteriscos y espacios en blanco
desde la instrucción
de salida
'''
while True:
    n = int(input('Digite un número impar positivo '))
    if n % 2 and n >= 0:
        break
    print('Número no válido')


k = 1
figuras = n * 2
blancos = figuras - (k * 2)

while blancos >= 0:

    for j in range(0, k):
        print('*', end='')
    for j in range(0, blancos):
        print(' ', end='')
    for j in range(0, k):
        print('*', end='')
    print('')
    k = k + 2
    blancos = figuras - (k * 2)
