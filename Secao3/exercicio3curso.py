# Utilizando os operadores de comparação e condicionais e com inputs do usuário, faça checagem de qual é o maior valor

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

valor_1 = int(primeiro_valor)
valor_2 = int(segundo_valor)

if valor_1 > valor_2:
    print("\n",valor_1,'é maior que', valor_2)
elif valor_1 < valor_2:
    print("\n",valor_2,'é maior que', valor_1)
elif valor_1 == valor_2: 
    print("\n",valor_1, 'é igual à',valor_2)  

    

