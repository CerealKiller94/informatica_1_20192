"""
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Implemente el algoritmo de búsqueda de raíces 
para la función x³ + 2x² - 4x + 3 usando el método exhaustivo. 
Para ello complete el archivo raices_exhaustivo_template.py 
guiándose por los comentarios en el código fuente y usando
delta = 0.0001.

auxiliares:
    f: variable que representa el valor
    de la función en un punto, recibe el valor de X
    a evaluar y devuelve un número. 
    pasos: cantidad de veces que se repite el ciclo
    a: límite inferior del intervalo de búsqueda
    b: límite superior del intervalo de búsqueda
    epsilon: tolerancia al error respecto al valor buscado
    delta: tamaño de paso
    xl = variable que contiene el valor de la posible raíz
    f_xl = variable que contiene el valor de la función
    en la posible raíz
Salidas:
    xl: en caso de que el valor aproximado de la raíz
    sea encontrado, se muestra dicho número
    pasos: aunque se encuentre o no la raíz de la función, se 
    muestra el número de iteraciones realizadas por el algoritmo
"""

# Funcion
def f(x):
    """Esta función evalúa y retorna el valor de F(x)
    es un punto determinado, este punto es el parámetro de la función"""
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

while abs(f_xl - 0) > epsilon and xl < b:
    pasos += 1
    xl += delta
    f_xl = f(xl)
    
# Despliegue de los resultados
print('-------------- Raiz de la funcion x³ + 2x² - 4x + 3 --------------')
if abs(f_xl - 0) <= epsilon:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(xl))
else:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
print('\nCantidad de iteraciones: {}'.format(pasos))
print('------------------------------------------------------------------')
        
