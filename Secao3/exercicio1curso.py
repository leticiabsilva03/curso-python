# inputs

nome_completo = input (str('Insira nome completo:'))
idade = int(input('Insira idade:'))
nascimento = input (str('Insira data de nascimento dd/mm/aaaa:'))
altura = float(input('Insira sua altura em cm:'))

# outputs

## nome
nome = nome_completo.split()[0]
n = len(nome_completo)
lista_sobrenome = nome_completo.split()[1:n]
sobrenome =" ".join(lista_sobrenome)

## idade
ano_nascimento = nascimento.split(sep="/")[-1]
ano = 2023
maior_de_idade = ano-int(ano_nascimento) >= 18

## altura
altura_metros = altura/100

print('Nome:', nome)
print('Sobrenome:', sobrenome) 
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_de_idade)
print('Altura em metro:', altura_metros, 'm')