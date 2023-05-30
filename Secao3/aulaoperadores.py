# Operadores Lógicos
## and (e) or (ou) not (não)

# and: todas as condições precisam ser verdadeiras, se qualquer valor for considerado falsy - 0 0.0 '' False - a expressão
# inteira será avaliada naquele valor
## None: usado para representar u não valor

entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrada permitida')
else:
    print('Entrada não permitida')

# Avaliação de curto circuito
print(True and False and True)
print(True and True and True)
print(True and 0.0 and True)