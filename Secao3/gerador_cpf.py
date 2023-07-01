import random # Este módulo implementa geradores de números pseudoaleatórios para várias distribuições.

nove_digitos = ''

for i in range(9):
  nove_digitos += str(random.randint(0, 9)) #cria os nove primeiros dígitos do cpf
  # para cada posição no range 9, será criado um número aleatório entre 0 e 9
  # a variável nove_digitos receberá os dígitos gerados aleatoriamente para cada posição
  # randint: Retorna um inteiro aleatório N de forma que a <= N <= b. Apelido para randrange(a, b+1).

# Após gerar os 9 primeiros dígitos, criaremos o resto do CPF a partir da validação:

contador_9 = 10
contador_10 = 11
mult_9 = 0
mult_10 = 0

for digitos in nove_digitos:
    mult_9 += int(digitos) * contador_9
    contador_9 -= 1

digito_1 = (mult_9 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)

for digitos in dez_digitos:
    mult_10 += int(digitos) * contador_9
    contador_10 -= 1

digito_2 = (mult_10 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

print(f'Cpf: {cpf_gerado}')