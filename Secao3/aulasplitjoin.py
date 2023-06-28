"""
split e join com list e str
split - divide uma string (list)
join - une uma string
strip - remove espaços no começo e no final de uma string
"""
frase = '   Olha só que, coisa interessante          '

lista_palavras = frase.split()
print(lista_palavras)

lista_frase = frase.split(', ')
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].lstrip())
    print(lista_palavras[i].rstrip())
    print(lista_palavras[i].strip())

lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())
    print(lista_frases)

print(lista_frases_cruas)
print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)