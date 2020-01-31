
while True:
    n = int(input('Digite un número impar: '))
    if n % 2 and n >= 0:
        break
    print('Digite un número impar positivo')

for i in range(1, n+1, 2):
    for k in range(1, i+1):
        print('#', end='')
    print('')
