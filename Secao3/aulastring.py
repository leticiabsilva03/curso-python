"""
Interpolação e Formatação básica de strings
s - string
d e i - int
f - float
.<número de dígitos>f
x e X - Hexadecimal (ABCDEF0123456789)
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
Conversion flags - !r !s !a
"""

nome = 'Leticia'
preco = 1000.95897643
variavel1 = '%s, o preço é E$%.2f' % (nome, preco)
print(variavel1)
print('O hexadecimal de %d é %04X' % (1235,1235))

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.72612612763:.1f}')

"""
Fatiamento de strins
012345678
Olá Mundo
Fatiamento [i:f:p] inicio:fim:passo
"""

variavel2 = 'Olá Mundo'
print(variavel2[:5])
print(variavel2[0:5:2])
print(variavel2[::-1])
print(len(variavel2)) 