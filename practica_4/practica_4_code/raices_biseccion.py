"""
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Implemente el algoritmo de búsqueda de raíces para la 
función anterior usando el método de bisección. Para ello 
complete el archivo raices_biseccion_template.py guiándose 
por los comentarios en el código fuente.

auxiliares:
    pasos: contador de las veces que se repiten los ciclos
    a: límite inferior del intervalo de 
    b: límite superior del intervalo de búsqueda
    epsilon: tolerancia al error
    encontrada: variable booleana que dice si se encontró (True)
    o no (False) la aproximación de la raíz
    f: variable que almacena el valor de la función
    evaluada en la posible raíz
    f1: valor de la función en el extremo inferior del intervalo
    f2: valor de la función en el extremo superior del intervalo
    medio: almacena el valor de la posible raíz
    
salidas:
    medio: en caso de encontrar la raíz, se muestra
    su valor aproximado
    pasos: siempre se muestra al final el número
    de ciclos hechos por el algoritmo
"""

def f(x):
    """Esta función evalúa y retorna el valor de F(x)
    es un punto determinado, este punto es el parámetro de la función"""
    f = x**3 + 2*(x**2) - 4*x + 3 
    #f = x**(x**x) - 5
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
else:
    print('\nLa raíz de la función x³ + 2x² - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
print('\nCantidad de iteraciones: {}'.format(pasos))
print('---------------------------------------------------------------------')
# Despliegue de los resultados

