"""
enumerate - enumera iteráveis (índices) 
"""
lista_a = ['Maria', 'Helena', 'Leticia', 'Mariana', 'Laura', 'Bianca', 'Ana']
lista_a.append('Olga')

lista_enumerada = enumerate(lista_a)

for item in lista_enumerada:
    print(item) # quando finaliza o for, a variável é zerada e um outro for não funcionaria

# a melhor forma de contornar isso é não colocar o enumerate em uma variável, e sim direto no for

lista_b = ['Mariana', 'Laura', 'Bianca', 'Ana']

for item in enumerate(lista_b):
    print(item)

for indice, nome in enumerate(lista_b):
    print(indice, nome)


lista = ['Mariana', 'Laura', 'Bianca', 'Ana']
lista_enumeradas_a = list(enumerate(lista, start=36)) #cria uma tupla/lista com (índice, valor)
print(lista_enumeradas_a)