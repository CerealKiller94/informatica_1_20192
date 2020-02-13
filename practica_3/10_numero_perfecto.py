'''
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Haga un algoritmo que diga si un número ingresado es perfecto o no. 
Un número perfecto es un número que 
es igual a la suma de sus divisores 
propios positivos. De esta forma, 
6 es un número perfecto porque sus 
divisores propios son 
1, 2 y 3; y 6 = 1 + 2 + 3.

Análisis: 
Entradas: 
numero (entero para validar si es o no 
perfecto)

Auxiliares:
suma: variable acumuladora de la suma 
de divisores propios
i: variable controladora del ciclo


salida: mensaje (cadena de texto que 
dice si el número es o no perfecto)
'''

suma = 1
i = 1

while True:
    numero = int(input('Digite un número para saber si es perfecto o no: '))
    if numero >= 0:
        break
    print('Digite un entero positivo')


for i in range(2, numero):
    if numero % i == 0:
        suma += i

if suma == numero:
    print('Es perfecto')
else:
    print('No es perfecto')
