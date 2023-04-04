### Entradas do usuário

nome = input("Digite seu nome completo: ")
altura = int(input("Digite sua altura em cm: "))
peso = int(input("Digite seu peso em kg: "))
imc = peso / ((altura/100) ** 2)

if imc < 18.5:
    imc_ideal = "magreza"
else:
    if imc >= 18.5 and imc <= 24.9:
        imc_ideal = "normal"
    else:
        if imc >= 25 and imc <= 29.9:
            imc_ideal = "sobrepeso"
        else:
            if imc >= 30 and imc <= 34.9:
                imc_ideal = "obesidade grau 1"
            else:
                if imc >= 35 and imc <= 39.9:
                    imc_ideal = "obesidade grau 2"
                else:   
                    if imc >= 40:
                        imc_ideal = "obesidade"

if imc_ideal == "normal":
    indice = "Ótimo!"
else:
    indice = "Preciso consultar um médico ou nutricionista."

print("\n")
print("~~~"*35)
print("\n")
print(f'Olá! Meu nome é {nome.title()}, tenho {altura/100} metros de altura, peso {peso} kg, e meu IMC é: {imc:.2f} kg/m², de forma que meu índice é {imc_ideal}! {indice}')
print("\n")
print("~~~"*35)
print("\n")