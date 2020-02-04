anho = int(input('Digite el año: '))
es_bisiesto = False
proximo_bisiesto = 0

if anho % 4 == 0:
    if anho % 100 == 0:
        if anho % 400 == 0:
            es_bisiesto = True
        else:
            es_bisiesto = False
            proximo_bisiesto += anho + 4
    else:
        es_bisiesto = True
else:
    proximo_bisiesto = anho + (4 - (anho % 4))
    es_bisiesto = False

if es_bisiesto:
    print('El año {} es bisiesto'.format(anho))
else:
    if proximo_bisiesto % 100 == 0:
        if proximo_bisiesto % 400 != 0:
            proximo_bisiesto += 4
    print('El año {} no es bisiesto pero el próximo bisiesto será en el año {}'
          .format(anho, proximo_bisiesto))
