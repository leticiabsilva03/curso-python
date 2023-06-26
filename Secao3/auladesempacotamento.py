"""
Introdução ao empacotamento e desempacotamento
"""
nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes #nº de variáveis deve ser igual ao de elementos da lista
print(nome2)

nome1, *resto = ['Maria', 'Helena', 'Laura', 'Bianca', 'Ana'] # resto guarda o restante da lista que não será utilizado
print (nome1, resto)

nome1, *_ = ['Maria', 'Helena', 'Laura', 'Bianca', 'Ana'] # _ utilizado para não criar variável que não será utilizada posteriormente
print (nome1, resto)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome)