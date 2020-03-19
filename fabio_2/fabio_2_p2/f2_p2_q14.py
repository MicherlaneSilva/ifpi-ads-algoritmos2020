#Um posto está vendendo combustíveis com a seguinte tabela de descontos:
#1. Álcool:
#· até 20 litros, desconto de 3% por litro
#· acima de 20 litros, desconto de 5% por litro
#2. Gasolina:
#· até 20 litros, desconto de 4% por litro
#· acima de 20 litros, desconto de 6% por litro.
# um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da
#seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que
#o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

def main():
    
    print('POSTO DE GASOLINA\n')
    
    combustivel = input('Álcool ou gasolina? A ou G? ').upper()
    litros = float(input("Quantos litros? "))
    
    preco = calc_preco(combustivel, litros)
    
    print(f'O preço com o desconto é R$ {preco}')


def calc_preco(combustivel, litros):
    if combustivel == 'A':
        preco = 1.90
        if litros<= 20:
            percen = 3
        else:
            percen = 5
    elif combustivel ==  'G':
        preco = 2.50
        if litros<= 20:
            percen = 4
        else:
            percen = 6            

    return calc_desconto(litros, percen, preco)

def calc_desconto(litros, percen, preco):
    return (litros * preco) * (1 - percen/100)


main()