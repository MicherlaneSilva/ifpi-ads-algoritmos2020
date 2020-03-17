def main():
    
    numero = int(input('Digite um número: '))
    
    print(escrever_extenso(numero))
    
def escrever_extenso(numero):
    cent = numero // 100
    resto = numero % 100
    dez = resto // 10
    unid = resto % 10
    
    if cent == 0:
        return escrever_dezenas(dez, unid)
    else:
        if cent == 1:
            return f'{cent} centena e '+ escrever_dezenas(dez, unid)
        else:
            return f'{cent} centenas e '+ escrever_dezenas(dez, unid)

def escrever_dezenas(dez, unid):
    if dez == 1:
        if unid == 1:
            return f'{dez} dezena e {unid} unidade'
        else:
            return f'{dez} dezena e {unid} unidades'
    else:
        if unid == 1:
            return f'{dez} dezenas e {unid} unidade'
        else:
            return f'{dez} dezenas e {unid} unidades'
        
        
main()