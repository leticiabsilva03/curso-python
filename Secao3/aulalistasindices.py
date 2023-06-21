"""
Listas em Python: Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete (CRUD)
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0      1   2   3   4   5   6   7   8   9
lista = ['10', 20, 30, 40, 50, 60, 70, 80, 90, 100]
print('Item na posição 2 (30): ',lista[2])
lista[2] = 300 # update
print(lista)
print(lista[2])
del lista[5] # delete, o indice 6 passa a ser o 5, e assim por diante
print(lista)
print(lista[5])

lista.append(50) #adiciona 50 no final da lista
print(lista)
lista.pop() # remove  o último item da lista (neste caso, é o 50)
lista.append(60)
lista.append('70')
print(lista)
ultimo_valor = lista.pop() # retorna o último valor removido da lista e "guarda" seu tipo
print(lista, 'Removido,', ultimo_valor, type(ultimo_valor))

remover_item = lista.pop(4) # remove o item na posição 4 da lista e retorna este item e seu valor
print(lista, 'Item removido,', remover_item, type(remover_item))
