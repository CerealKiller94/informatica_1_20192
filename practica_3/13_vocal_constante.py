'''
Nombre: Yonathan López Mejia
Grupo: 10
Documento: 1017220389
Enunciado: Escriba un 
programa que tome un 
carácter (es decir, un string 
de longitud 1) y determine 
si el carácter es vocal o 
consonante.


Análisis: 
entrada
letter: es el caracter a 
evaluar


Auxiliares:
vowels: un string con vocales
mayusculas y minusculas 
para comparar

consonants: un string
con consonantes mayusculas
y minusculas para comparar


salida: se imprime el mensaje
de si la letra es vocal, consonante o ninguna
'''
while True:
    letter = input('Escriba un solo caracter: ')
    if len(letter) == 1:
        break
    print('Solo un caracter')


vowels = 'AaEeIiOoUu'
consonants = 'BbCcDdFfGgHhJjKkLlMmNnÑñPpQqRrSsTtUuVvWwXxYyZz'

if letter in vowels:
    print('El caracter "{}" es una vocal'.format(letter))
elif letter in consonants:
    print('El caracter "{}" es una consonante'.format(letter))
else:
    print('El caracter "{}" no es ni vocal ni consonante'.format(letter))
