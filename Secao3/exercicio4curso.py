"""
Exercício
Peça ao usuário para digitar seu nome
Pela ao usuário para digitar sua idade
Se nome e idade forem digitados:
  Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Seu nome contém (ou não) n espaços
    Seu nome tem {n} letras
    A primeira letra do seu nome é {letra}
    A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
  Exiba:
    "Desculpe, você deixou campos vazios.)
"""

nome = input ('Escreva seu nome completo: ')
idade = input ('Qual a sua idade? ')

tamanho = len(nome)
letras = len(nome)-nome.count(" ")
espaco = tamanho-letras

if nome != '' and idade != '':
    print('Seu nome completo é: %s' % (nome.strip()))
    print('Seu nome invertido é: %s' % (nome.strip()[::-1]))
    if espaco != 0:
        print('Seu nome contém espaço')
    else:
        print('Seu nome NÃO contém espaço')
    print('Seu nome tem %d letras' % (letras))
    print('A primeira letra do seu nome é: %s' % nome [0])
    print('A última letra do seu nome é: %s' % nome [-1])
else: 
    print('Desculpe, você deixou campos vazios.')