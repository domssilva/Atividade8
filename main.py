# Function that calculates a person's IMC
def get_imc(altura: float, peso: float):
    return peso / (altura ** 2)

altura = float(input('Insira a sua altura (exemplo - 1.70, 1.56, 1.82): '))
peso = float(input('Insira o seu peso: '))

imc = get_imc(altura, peso)
print(f'IMC = {imc}')