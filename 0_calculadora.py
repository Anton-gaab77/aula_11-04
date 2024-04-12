valor1 = float(input('digite um numero:'))
resultado = 0
def soma(valor1, valor2 ):
    return valor1 + valor2

def sub(valor1, valor2):
    return valor1 - valor2

def mult(valor1, valor2):
    return valor1 * valor2

def div(valor1, valor2):
    return valor1 / valor2

while valor1 != -1:
    operador = input('escolha um operador:')
    valor2 = float(input('digite o segundo numero:'))

    if valor2 == -1:
        break

    if operador == '+':
        resultado = soma(valor1, valor2)
    elif operador == '-':
        resultado = sub(valor1, valor2)
    elif operador == '*':
        resultado = mult(valor1, valor2)
    elif operador == '/':
        if valor2 != 0:
            resultado = div(valor1, valor2)
        else:
            print('erro; divisão por 0:')
    else:
        print('operador inválido')
        continue

    print(' resultado = ', resultado)

    valor1 = float(input('digite um numero :'))
print('> calculadora encerrada.')
