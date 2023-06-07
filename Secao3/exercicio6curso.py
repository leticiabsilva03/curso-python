"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. 
Ex. Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

horas = input('Que horas são? hh:mm ')
hora = horas[:2]
verifica_int = False

try:
    horas_int = int(hora)
    if horas_int >=0 and horas_int <= 11:
        print ('Bom dia!')
    elif horas_int >=12 and horas_int <= 17:
        print ('Boa tarde!')
    elif horas_int >=18 and horas_int <= 23:
        print ('Boa noite!')
    else:
        print ('Não conheço essa hora. Você tem certeza?')
except ValueError:
    print ('Horas inválidas. Por favor, digite apenas números inteiros.')