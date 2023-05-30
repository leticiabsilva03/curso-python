print("\t 123")

# \r\n -> CRLF
# \n -> LF
print(12, 34, 1011, sep="", end='#')
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
str -> string -> texto
Strings são textos que estão dentro de aspas
"""
print(1234)

# Aspas simples
print('Leticia')
print(1, 'Leticia \n"Batista"')

# Aspas duplas
print("Leticia Batista")
print(2, "Leticia 'Batista'")

# Escape
print("Leticia \"Batista\"")

# r
print(r"Leticia \"Batista\"")

name = 'letixia'

for letra in name:
    print("\t\nLetícia é muito inteligente no python")