#Iterando strings com while

nome = input('Digite seu nome: ')

print (nome)
print ('O nome possui',len(nome),'letras')

posicao = 0
tamanho = len(nome)
novo_nome = ''
ounovo_nome = ''

while posicao < len(nome):
     novo_nome += '*' + nome [posicao]
     ounovo_nome += f'*{nome[posicao]}'
     posicao += 1

print (novo_nome)
print (ounovo_nome)