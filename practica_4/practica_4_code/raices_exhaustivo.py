# Funcion
def f(x):
    f = x**3 + 2*(x**2) - 4*x + 3 
    return f

# Variables del programa
pasos = 0 # Numero de veces que se repite el ciclo
a = -4 # Limite inferior
b = -3 # Limite superior
epsilon = 0.01 # Tolerancia al error
delta = 0.0001 # Tamanho de paso

# Inicializacion de la variable que contendra el valor de la rai­z
xl = a
f_xl = f(xl)
# Evaluacion iterativa de la funcion en la rai­z sospechada

while abs(f_xl - 0) > epsilon:
    pasos += 1
    xl += delta
    f_xl = f(xl)
    
# Despliegue de los resultados
print('-------------- Raiz de la funcion x³ + 2x² - 4x + 3 --------------')
print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(xl))
print('\nCantidad de iteraciones: {}'.format(pasos))
print('------------------------------------------------------------------')
