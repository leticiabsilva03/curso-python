"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

cpf_input = input('Digite um cpf válido: ').strip()
cpf_numero = cpf_input.isdigit() # verifica se CPF foi digitando com . e - ou apenas números
contador_9 = 10
contador_10 = 11

#Verificando a string
if cpf_numero:
    cpf_int = cpf_input
else:
    cpf_ponto = cpf_input.split('.')
    cpf_str = cpf_ponto[-1].split('-')
    p, s, *_ = cpf_ponto
    n, u = cpf_str
    cpf_int = p + s + n + u

#Verificando primeiro dígito
cpf_nove_digitos = cpf_int[:9]
mult_9 = 0
result_mult_9 = 0
for digitos in cpf_nove_digitos:
    mult_9 =+ int(digitos) * contador_9
    result_mult_9 += mult_9
    contador_9 -= 1

digito_1 = (result_mult_9 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

print (f'Dígito: {digito_1}')

print('Dígito válido, CPF validado!') if str(digito_1) == cpf_int [9] else print('Dígito incorreto, CPF inválido!')

#Verificando segundo dígito
if str(digito_1) == cpf_int [9]:
    cpf_dez_digitos = cpf_int[:10]
else:
    cpf_dez_digitos = cpf_int[:9] + str(digito_1)

mult_10 = 0
result_mult_10 = 0
for digitos in cpf_nove_digitos:
    mult_10 =+ int(digitos) * contador_9
    result_mult_10 += mult_10
    contador_9 -= 1

digito_2 = (result_mult_10 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0
cpf = cpf_int

print (f'Dígito: {digito_2}')
print(f'Dígito válido, CPF validado! CPF: {cpf}') if str(digito_2) == cpf_int [10] else print('Dígito incorreto, CPF inválido!')
