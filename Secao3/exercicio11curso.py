"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.

Faça a contagem de tentativas do seu usuário.
"""

import os

print('\n\n----------------Jogo da Forca!----------------\n\n')

palavra_secreta = 'ABACAXI'
tentativas_totais = 0
acerto_letra = 0
i = 0
palavra_acertada = ''

# Verificando se usuário digitou apenas uma letra
while True:

    letra_digitada = input('Digite letra: ').upper()
    tentativas_totais += 1

    verifica_numero = letra_digitada.isdigit()

    # Verificações
    if len(letra_digitada) > 1:
        print('Digite apenas uma letra')
    elif letra_digitada == ' ':
        print('Digite uma letra válida, espaço não conta!')
    elif letra_digitada.isdigit():
        print('Digite uma letra, números não valem.')
        continue

    # Verificando se letra digitada está na palavra secreta 

    if letra_digitada in palavra_secreta:
        palavra_acertada += letra_digitada
        acerto_letra +=1

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in palavra_acertada:
            palavra_formada += letra
        else:
            palavra_formada += '*'   

    print('Palavra formada: ', palavra_formada) 

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabéns, você acertou a palavra secreta!')
        print('A palavra era', palavra_secreta)
        print('Tentativas com letras certas:', acerto_letra)
        print('Tentativas totais:', tentativas_totais)
        tentativas = 0
        acerto_letra = 0
        palavra_acertada = ''
        palavra_formada = ''

    


