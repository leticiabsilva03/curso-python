"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""
# Soma valor atual (da variável) com valor atribuido

contador = 10
while contador < 100:
  contador += 5 # 10+5=20 20+5=25 etc
  print(contador)

print('Acabou')

#Subtração do valor atual

contador = 100
while contador > 5:
  contador -= 5 
  print(contador)

print('Acabou')

# Multiplicação (Funciona com Strings)

contador = 'a'
contador *= 10
print(contador)

contador = 2
while contador <100:
  contador *= 6 
  print(contador)

print('Acabou')

# Divisão - retorna número de ponto flutuante 

contador = 16
contador /= 3
print(contador) #16/3=5.333

# Divisão inteira 

contador = 23
contador //= 3
print(contador) #23/3=7 - não mostra resto nem casas decimais

# Potenciação

contador = 2
contador **= 10
print(contador)

#Resto da Divisão 

contador = 20
contador %= 6
print(contador)