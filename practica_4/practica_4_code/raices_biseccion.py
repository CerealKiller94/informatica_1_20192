"""
Nombre: Yonathan L�pez Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Implemente el algoritmo de b�squeda de ra�ces para la 
funci�n anterior usando el m�todo de bisecci�n. Para ello 
complete el archivo raices_biseccion_template.py gui�ndose 
por los comentarios en el c�digo fuente.

auxiliares:
    pasos: contador de las veces que se repiten los ciclos
    a: l�mite inferior del intervalo de 
    b: l�mite superior del intervalo de b�squeda
    epsilon: tolerancia al error
    encontrada: variable booleana que dice si se encontr� (True)
    o no (False) la aproximaci�n de la ra�z
    f: variable que almacena el valor de la funci�n
    evaluada en la posible ra�z
    f1: valor de la funci�n en el extremo inferior del intervalo
    f2: valor de la funci�n en el extremo superior del intervalo
    medio: almacena el valor de la posible ra�z
    
salidas:
    medio: en caso de encontrar la ra�z, se muestra
    su valor aproximado
    pasos: siempre se muestra al final el n�mero
    de ciclos hechos por el algoritmo
"""

def f(x):
    """Esta funci�n eval�a y retorna el valor de F(x)
    es un punto determinado, este punto es el par�metro de la funci�n"""
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
# 1. Que la rai�z sea a. Si f1 == 0.
# 2. Que la rai�z sea b. Si f2 == 0.
# 3. Que no haya rai�z. Si f1*f2 > 0 (asumiendo que hay mximo una rai�z en el intervalo)
# 4. Que la rai�z se encuentre en el intervalo [a,b]. Si f1*f2 < 0

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

print('--------Raiz de la funcion x� + 2x� - 4x + 3  -Binaria -----------')
if encontrada:
    print('\nLa ra�z de la funci�n x� + 2x� - 4x + 3 en el intervalo [-4, -3] es aproximadamente {}'.format(medio)) 
else:
    print('\nLa ra�z de la funci�n x� + 2x� - 4x + 3 en el intervalo [-4, -3] no fue encontrada')
print('\nCantidad de iteraciones: {}'.format(pasos))
print('---------------------------------------------------------------------')
# Despliegue de los resultados

