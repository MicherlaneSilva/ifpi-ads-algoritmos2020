#Leia o preço de três produtos e informe qual 
# produto deve ser comprado, sabendo que a decisão é
#sempre pelo mais barato.

def main():
    print('MELHOR PREÇO')
    
    nome_p1 = input('Nome do produto 1: ')
    preco_p1 = float(input('Preço: '))
    
    nome_p2 = input('\nNome do produto 2: ')
    preco_p2 = float(input('Preço: '))
    
    nome_p3 = input('\nNome do produto 3: ')
    preco_p3 = float(input('Preço: '))
    
    nome, preco = mais_barato(nome_p1, preco_p1, nome_p2, preco_p2, nome_p3, preco_p3)
    
    print('\nO produto mais barato é %s com o preço de R$ %.2f'%(nome, preco))

def mais_barato(nome_p1, preco_p1, nome_p2, preco_p2, nome_p3, preco_p3):
    
    if preco_p1< preco_p2 and preco_p1 < preco_p3:
        return nome_p1, preco_p1
    elif preco_p2< preco_p1 and preco_p2 < preco_p3:
        return nome_p2, preco_p2
    else:
        return nome_p3, preco_p3

main()