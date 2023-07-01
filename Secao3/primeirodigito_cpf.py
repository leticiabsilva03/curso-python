"""
Cálculo do primeiro dígito do CPF
Colete a soma dos 9 primeiros dígitos do CPF multiplicando cada um dos valores por uma contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301

Multiplicar o resultado anterior por 10:
301 * 10 = 3010

Obter o resto da divisão da conta anterior por 11:
3010 % 11 = 7

Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
    
O primeiro dígito do CPF é 7
"""

cpf_input = input('Digite um cpf válido: ').strip()
cpf_numero = cpf_input.isdigit() # verifica se CPF foi digitando com . e - ou apenas números
contador = 10

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
mult = 0

for digitos in cpf_nove_digitos:
    mult += int(digitos) * contador
    contador -= 1

digito = (mult * 10) % 11
digito = digito if digito <= 9 else 0

print (f'Dígito: {digito}')

digito = print('Dígito válido, CPF validado!') if str(digito) == cpf_int [9] else print('Dígito incorreto, CPF inválido!')