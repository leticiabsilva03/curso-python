"""
Tipo tupla (tuple) - Uma lista imutável
"""
nomes = 'Maria', 'Helena', 'Leticia' #basta tirar os [] para ter uma tupla, ou colocar () no lugar dos []
print(nomes[-1]) #último índice da tupla
print(nomes)

# convertendo lista em tuplas e tuplas em lista:

lista_a = ['Maria', 'Helena', 'Leticia', 'Mariana', 'Laura', 'Bianca', 'Ana']
print(lista_a, type(lista_a))
nomes_a = tuple(lista_a)
print(nomes_a, type(nomes_a))

lista_b = ('João', 'José', 'Leo', 'Pedro', 'Luiz', 'Paulo', 'Alex')
print(lista_b, type(lista_b))
nomes_b = list (lista_b)
print(nomes_b, type(nomes_b))