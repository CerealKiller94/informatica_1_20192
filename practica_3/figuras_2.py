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
