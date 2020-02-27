def f(x):
    f = x**3 + 2*(x**2) - 4*x + 3 
    return f

# Variables del programa
pasos = 0 # Numero de veces que se repite el ciclo
a = -4 # Limite inferior
b = -3 # Limite superio
epsilon = 0.01 # Tolerancia
encontrada = False

# Evaluacion de la funcion en los limites
f1 = f(a)
f2 = f(b)

# Verificar que existe raiz en los limites
# Hay 4 posibilidades:
# 1. Que la rai­z sea a. Si f1 == 0.
# 2. Que la rai­z sea b. Si f2 == 0.
# 3. Que no haya rai­z. Si f1*f2 > 0 (asumiendo que hay mximo una rai­z en el intervalo)
# 4. Que la rai­z se encuentre en el intervalo [a,b]. Si f1*f2 < 0

if f1 == 0:
    encontrada = True
    medio = a
elif f2 == 0:
    encontrada = True
    medio = b
elif f1*f2 > 0:
    encontrada = False  
else:
    while a < b:
        pasos += 1
        medio = (a + b)/2
        fx = f(medio)
        if abs(fx - 0) <= epsilon:
            encontrada = True
            break
        if fx > 0:
            b = medio
        else:
            a = medio

print('--------Raiz de la funcion x³ + 2x² - 4x + 3  -Binaria -----------')
if encontrada:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(medio))
    print('\nCantidad de iteraciones: {}'.format(pasos))
    

else:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
    print('\nCantidad de iteraciones: {}'.format(pasos))
print('---------------------------------------------------------------------')
# Despliegue de los resultados

