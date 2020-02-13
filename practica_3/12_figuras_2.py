'''
Nombre: Yonathan L�pez Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo 
que muestre el siguiente patr�n 
en la pantalla:

*                 *
***           ***
*****      *****
**************


El tama�o del patr�n estar� 
determinado por un n�mero 
entero impar que ingrese el 
usuario. En el ejemplo mostrado, 
el tama�o de la figura es 7.



An�lisis: 
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
cantidad m�xima de figuras
que aparecen, siempre impar


salida: se imprimen los
asteriscos y espacios en blanco
desde la instrucci�n
de salida
'''
while True:
    n = int(input('Digite un n�mero impar positivo '))
    if n % 2 and n >= 0:
        break
    print('N�mero no v�lido')


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
