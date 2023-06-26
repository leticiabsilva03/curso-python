"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3
lista = [10, 20, 30, 40]
lista.append('Leticia')
print(lista)
nome = lista.pop()
print(lista, nome)
lista.append(1233)
print(lista)
del lista[-1] #-1 sempre vai ser o último item da lista
print(lista)
# lista.clear() # limpa toda a lista
lista.insert(100, 5) # insere o número 5 na posição 100 da lista porém, neste caso, como o índice 100 não existe, o número é inserido na última posição existente = 4
print(lista)
print(lista[4])

lista_a = [1,2,3]
lista_b = [4,5,6]
lista_c = lista_a + lista_b # concatenação
print(lista_c)
lista_a.extend(lista_b) # método
print(lista_a)
