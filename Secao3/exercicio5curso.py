"""
Faça um programa que peça ao usuário para digitar um número inteiro,informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

numero_str = input ('Digite um número inteiro para saber se é par ou ímpar: ')
verifica = False

try:
    numero_int = int(numero_str)
    print (f'O número {numero_str} é um número inteiro')
    verifica = numero_int % 2 == 0
    if verifica:
      print (f'O número {numero_str} é par')
    else:
      print (f'O número {numero_str} é ímpar')
except ValueError:
    print ('O número digitado não é um número inteiro')

# Outra forma de verificar:

if numero_str.isdigit():
   entrada_int = int(numero_str)
   par_impar = entrada_int % 2 == 0
   par_impar_texto = 'ímpar'
   if par_impar:
     par_impar_texto = 'par'
   print(f'O numero {entrada_int} é {par_impar_texto}')
else: 
   print ('O número digitado não é um número inteiro')

