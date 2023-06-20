#Qual letra, na frase a seguir, apareceu mais vezes?

frase = 'O Python é uma linguagem de programação'\
        'multiparadigma'\
        'Python foi criado por Guido van Rossum'

i=0
qntd_atual = 0
letra_atual = 0

while i < len(frase):
    letra = frase[i]
    qntd = frase.count(letra)

    if letra == ' ':
        i += 1
        continue

    if qntd_atual < qntd:
        qntd_atual = qntd
        letra_atual = letra
    
    i += 1

print(f'A letra que apareceu mais vezes foi ', {letra_atual}, ', que apareceu', {qntd_atual}, 'x')
