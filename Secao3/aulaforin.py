# Iniciando os estudos com for

texto = 'Python'
novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')

# For + Range
# range -> range (start, stop, step)
# Iterável -> str, range, etc..  -> são objetos (___iter___)
# Iterador -> quem sabe entregar um valor por vez
# next -> me entregue o próximo valor
# iter -> me entrege seu iterador

texto = iter('Leticia') #iterável

print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))
print(next(texto))

iteratador = iter(texto) #iterator

#for letra in texto:
while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

numeros = range(0,100,8)

for numero in numeros:
    print(numero)

 