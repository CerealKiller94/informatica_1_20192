while True:
    horas_trabajadas = int(input('Digite la cantidad de horas trabajadas: '))
    if horas_trabajadas >= 0:
        break
    print('Número de horas no válido')

impuestos = 0

if horas_trabajadas <= 40:
    salario_bruto = horas_trabajadas * 7500
else:
    salario_bruto = 40 * 7500
    salario_bruto += ((horas_trabajadas - 40) * 12000)

if salario_bruto <= 250000:
    impuestos = salario_bruto * 0.1
else:
    impuestos = 250000 * 0.1
    impuestos += ((salario_bruto - 250000) * 0.2)

a_pagar = salario_bruto - impuestos
print('El salario a pagar es: ${} COP'.format(a_pagar))
