import re
import sys

# cpf_enviado_usuario = '746.824.890-70' \
#     .replace('.', '') \ # modo de substituir algo digitado pelo usuário que não seja os numeros do cpf
#     .replace(' ', '') \
#     .replace('-', '')
entrada = input('CPF [746.824.890-70]: ')
cpf_enviado_usuario = re.sub( #substitui tudo que não for numero entre 0 e 9 na string de input
    r'[^0-9]',
    '',
    entrada
)

verifica_entrada = entrada == entrada[0] * len(entrada) #verifica se cpf digitado é uma sequência de números
# se o usuário digitar 11111111111 ou outra sequência, o cpf será validado mas não estará correto
# se o digito da primeira posição digitada pelo usuário (entrada[0]) for o mesmo em todas as posições da entrada len(entrada), o usuário terá digitado dados sequenciais

if verifica_entrada:
    print('Você enviou dados sequenciais.')
    sys.exit() #encerrará o programa caso o usuário tenha digitado dados sequenciais

nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_usuario} é válido')
else:
    print('CPF inválido')