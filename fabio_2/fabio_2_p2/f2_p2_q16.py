def main():
    
    tipo = input('Qual carne? ')
    quantidade = float(input('Quantidade: '))
    pagamento = input('Forma de pagamento: ')
    
    preco_total, desconto, preco_pagar = realizar_compra(tipo, quantidade, pagamento)
    
    print('\nNOTA FISCAL')
    print(f'Produto {tipo} - Quantidade {quantidade} kg')
    print(f'Valor do desconto R${desconto}\nTOTAL: R$ {preco_pagar}')


def  realizar_compra(tipo, quantidade, pagamento):
    
    if tipo == 'file':
        if quantidade <= 5:
            preco = 4.90
        else:
            preco = 5.80
    elif tipo == 'alcatra':
        if quantidade <= 5:
            preco = 5.90
        else:
            preco = 6.80
    else:
        if quantidade <= 5:
            preco = 6.90
        else:
            preco = 7.80
            
    valor_total =  calc_preco(preco, quantidade)
    
    if pagamento == 'cartao' or pagamento == 'cartão':
        desconto = valor_total * 5 /100
    else:
        desconto = 0
    return valor_total, desconto, valor_total - desconto 

def  calc_preco(preco, quantidade):
    return  preco * quantidade

main()