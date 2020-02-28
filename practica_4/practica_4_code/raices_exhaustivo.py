"""
Nombre: Yonathan L�pez Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Implemente el algoritmo de b�squeda de ra�ces 
para la funci�n x� + 2x� - 4x + 3 usando el m�todo exhaustivo. 
Para ello complete el archivo raices_exhaustivo_template.py 
gui�ndose por los comentarios en el c�digo fuente y usando
delta = 0.0001.

auxiliares:
    f: variable que representa el valor
    de la funci�n en un punto, recibe el valor de X
    a evaluar y devuelve un n�mero. 
    pasos: cantidad de veces que se repite el ciclo
    a: l�mite inferior del intervalo de b�squeda
    b: l�mite superior del intervalo de b�squeda
    epsilon: tolerancia al error respecto al valor buscado
    delta: tama�o de paso
    xl = variable que contiene el valor de la posible ra�z
    f_xl = variable que contiene el valor de la funci�n
    en la posible ra�z
Salidas:
    xl: en caso de que el valor aproximado de la ra�z
    sea encontrado, se muestra dicho n�mero
    pasos: aunque se encuentre o no la ra�z de la funci�n, se 
    muestra el n�mero de iteraciones realizadas por el algoritmo
"""

# Funcion
def f(x):
    """Esta funci�n eval�a y retorna el valor de F(x)
    es un punto determinado, este punto es el par�metro de la funci�n"""
    f = x**3 + 2*(x**2) - 4*x + 3 
    return f

# Variables del programa
pasos = 0 # Numero de veces que se repite el ciclo
a = -4 # Limite inferior
b = -3 # Limite superior
epsilon = 0.01 # Tolerancia al error
delta = 0.0001 # Tamanho de paso

# Inicializacion de la variable que contendra el valor de la rai�z
xl = a
f_xl = f(xl)
# Evaluacion iterativa de la funcion en la rai�z sospechada

while abs(f_xl - 0) > epsilon and xl < b:
    pasos += 1
    xl += delta
    f_xl = f(xl)
    
# Despliegue de los resultados
print('-------------- Raiz de la funcion x� + 2x� - 4x + 3 --------------')
if abs(f_xl - 0) <= epsilon:
    print('\nLa ra�z de la funci�n x� + 2x� - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(xl))
else:
    print('\nLa ra�z de la funci�n x� + 2x� - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
print('\nCantidad de iteraciones: {}'.format(pasos))
print('------------------------------------------------------------------')
        
