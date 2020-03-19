#Uma fruteira está vendendo frutas com a seguinte tabela de preços:

#        Até 5 Kg       Acima de 5 Kg
#Morango R$ 2,50 por kg   Kg R$ 2,20 por Kg
#Maçã R$ 1,80 por Kg    R$ 1,50 por Kg

#Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá
#ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de
#morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
def main():
    print('FRUTARIA DO SEU ZÉ\n')
    
    quant_maca = int(input('Quantas maçãs? '))
    quant_morango = int(input('Quantos morangos? '))
    
    total = calc_total(quant_maca, quant_morango)
    
    print(f'\nTotal: R$ {total}')

def calc_total(quant_maca, quant_morango):
    if quant_morango <= 5:
        preco_morango = 2.5
    else:
        preco_morango = 2.20
    
    if quant_maca <= 5:
        preco_maca = 2.5
    else:
        preco_maca = 2.20

    return calc_desconto(quant_maca, preco_maca, quant_morango, preco_morango)


def calc_desconto(quant_maca, preco_maca, quant_morango, preco_morango):
    total = quant_maca * preco_maca + quant_morango * preco_morango
    
    if total > 25 or (quant_maca+quant_morango)>8:
        total = total * (1 - 10/100)
    
    return total

main()