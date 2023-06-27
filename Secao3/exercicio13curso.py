"""
Faça uma lista de compras com listas. O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista = []

while True:
    
    print('\nSelecione uma opção: \n')
    opcao = input('[i]nserir [a]pagar [l]istar\n').lower()

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)

    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Escolha qual índice será deletado: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Apenas número inteiro é válido.')
        except IndexError:
            print('Índice não existe na lista.')
        except Exception:
            print('Erro inexistente.')
    
    elif opcao == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Lista vazia.')
        
        for indice, valor in enumerate(lista):
            print(indice, valor)

    else:
        print('Por favor, escolha [i], [a] ou [l].')