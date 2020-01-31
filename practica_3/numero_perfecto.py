
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
