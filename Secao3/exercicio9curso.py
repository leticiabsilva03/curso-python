# Calculadora com while

while True:
    numero1 = input ('Digite o primeiro número: ')
    verifica_numero1 = None
    num1_float = 0
    num1_float = 0

    try:
        num1_float = float(numero1)
        verifica_numero1 = True
    except:
        verifica_numero1 = None

    if verifica_numero1 is None:
        print ('Você não digitou um número válido.')
        continue
    
    numero2 = input ('Digite o segundo número: ')
    verifica_numero2 = None
    try:
        num2_float = float(numero2)
        verifica_numero2 = True
    except:
        verifica_numero2 = None 
    if verifica_numero2 is None:
        print ('Você não digitou um número válido.')
        continue
    
    operador = input('Digite o operador (+-/*): ')
    verifica_operador = '+-/*'

    if len(operador) > 1:
        print ('Digite apenas 1 operador por vez.')
        continue

    if operador not in verifica_operador:
        print ('Operador inválido.')
        continue
    
    print ('Realizando sua conta. Resultado: ')
    if operador == '+':
        print(f'{num1_float}+{num2_float}=', num1_float + num2_float)
    elif operador == '-':
        print(f'{num1_float}-{num2_float}=', num1_float - num2_float)
    elif operador == '*':
        print(f'{num1_float}*{num2_float}=', num1_float * num2_float)        
    elif operador == '/':
        print(f'{num1_float}/{num2_float}=', num1_float / num2_float)
    else:
        print ('Algo deu errado. Repita a operação.')

    sair = input ('Deseja sair da calculadora? [s]im ').lower().startswith('s')
    if sair:
        break