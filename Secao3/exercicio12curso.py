'''
Exercício: Exiba os índices da lista
0 Maria
1 Helena
2 Leticia
etc - deve ser dinâmico
'''

lista_a = ['Maria', 'Helena', 'Leticia', 'Mariana', 'Laura', 'Bianca', 'Ana']
indice = 0

for nome in lista_a:
    print(indice, nome, type(nome))
    indice += 1

lista_b = ['João', 'José', 'Leo', 'Pedro', 'Luiz', 'Paulo', 'Alex']
indices_b = range(len(lista_b)) # tamanho da lista b

for indices in indices_b:
    print(indices, lista_b[indices], type(lista_b[indices]))