#Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
#(IMC = peso / altura2

#). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso

#(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

def main():
    
    print(' '*50+'IMC\n')
    altura = float(input("Digite sua altura: "))
    peso = float(input("Digite seu peso: "))
    
    imc = calc_imc(altura, peso)
    
    print('\nIMC: %.2f'%imc)
    print('Classificação: ',clas_imc(imc))
    

def calc_imc(altura, peso):
    return peso / altura ** 2

def clas_imc(imc):
    
    if imc< 25:
        return "peso normal"
    elif imc<30:
        return "obeso"
    else:
        return "obesidade mórbida"


main()
    