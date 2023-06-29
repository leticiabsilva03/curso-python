# Desempacotamento em chamadas
# de métodos e funções

string = 'ABCD' # cada elemento possui uma posição, o * separa. posição 0 = A, posição 1 = B, posição 2 = C, etc
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda'] # posição 0 = Maria, posição 1 = Helena, posição 2 = 1, etc.
tupla = 'Python', 'é', 'legal'  # posição 0 = Python, posição 1 = é, posição 2 = legal, etc.
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

p, b, *_, ap, u = lista # ap pega o penultimo elemento, u pega o último elemento, *_ engloba todos os que nao foram vinculados
print(p, u, ap)

# print('Maria', 'Helena', 1, 2, 3, 'Eduarda')
print(*lista)
print(*string)
print(*tupla)

print(*salas, sep='\n')