"""
Lista de listas e seus índices
"""
salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[1][0])
# print(salas[0][1])
# print(salas[2][2])
# print(salas[2][3][3])

for i, fileira in enumerate(salas):
    print(f'A fileira {i+1} é composta por {fileira}')
    for aluno in fileira:
        print(f'Aluno(a): {aluno}')