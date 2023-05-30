'''Exercicio surpresa:

  Receba ou declare o nome completo de uma pessoa e em seguida mostre as seguintes informações:
  1- Nome em letras maiusculas
  2- Nome em letras minusculas
  3- Quantas letras tem no nome (Sem considerar os espaços)
  4- Quantas letras tem no primeiro nome

 '''

nome = input("Escreva seu nome completo: ")

print ("\n", "Seu nome completo é:", nome.strip()) #strip remove espaços iniciais e finais em branco
print ("\n", "Seu nome completo em letras maiúsculas é:", nome.upper().strip())
print ("\n", "Seu nome completo em letras minúsculas é:", nome.lower().strip())
print ("\n", "Seu nome é:", nome.strip(), "e ele tem", len(nome)-nome.count(" "), "letras, sem contar os espaços.") 
print ("\n", "Seu nome é:", nome, "e ele tem", nome.__len__(), "letras.")

primeiro_nome = nome.split()[0] # .split() separa a string em uma lista de acordo com os espaços da string

print ("\n", "Seu primeiro nome é:", primeiro_nome, "e ele tem", primeiro_nome.__len__(), "letras.")