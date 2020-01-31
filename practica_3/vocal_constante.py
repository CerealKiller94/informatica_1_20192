
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
