valor1 = float(input('digite um numero:'))
resultado = 0

while valor1 != -1:
    operador = input('escolha um operador:')
    valor2 = float(input('digite o segundo numero:'))

    if valor2 == -1:
        break

    if operador == '+':
        resultado = valor1 + valor2
    elif operador == '-':
        resultado = valor1 - valor2
    elif operador == '*':
        resultado = valor1 * valor2
    elif operador == '/':
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            print('erro; divisão por 0:')
    else:
        print('operador inválido')
        continue

    print(' resultado = ', resultado)

    valor1 = float(input('digite um numero :'))
print('> calculadora encerrada.')
