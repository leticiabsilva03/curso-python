"""
Listas em Python
Tipo list - Mutável - podemos mudar elementos de lugar
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
"""
#        +01234
#        -54321
string = 'ABCDE'  # 5 caracteres (len), é apenas uma string

lista1 = []
print(lista1, type(lista1), len(lista1))
lista2 = list(string) # forma menos usual de utilizar listas, apenas se quiser converter algo em lista
print (lista2, type(lista2), len(lista2))

print(bool([lista1]))  # falsy, se lista estiver vazia, retorna falso

#         0     1       2                      3    4   5
#        -6    -5      -4                     -3   -2  -1

lista = [123, True, 'Leticia Batista Silva',  1.2, 'a', []]
print(lista)
lista[-3] = 'Maria'
print(lista)
print(lista[2], lista[2].upper, type(lista[2]))