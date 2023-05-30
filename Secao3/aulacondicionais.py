#### Coleta de dados com "input"

nome = input ('Qual o seu nome? ') # se não declarar tipo, ela sempre pegará string 
print(f'O seu nome é {nome}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)

print(f'A soma dos números é: {int_numero_1+int_numero_2}')

################################
### Condicionais if / elif / else
 
entrada = input('Você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('Você entrou no sistema')
elif entrada == 'sair': ## pode se repetir várias vezes
    print('Você saiu no sistema')
else: ## é sempre a última opção
    print('Você não digitou nem entrar e nem sair.')

## Operadores de comparação (relacionais)
'''
OP    Significado       Exemplo (True)
>     maior              2 > 1
>=    maior ou igual     2 >= 2
<     menor              1 < 2
<=    menor ou igual     2<=2
==    igual              'a' == 'a'
!=    diferente          'a' != 'b'
'''

print(2>1)
print(2 >= 2)
print(1 < 2)
print(2>1)
print(2<=2)
print('a' == 'a')
print('a' != 'b')
