#Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

def main():
    
    n1 = int(input("1º número: "))
    n2 = int(input("2º número: "))
    n3 = int(input("3º número: "))
    
    quant_igual = quant_iguais(n1, n2, n3)
    
    print(f'Existem {quant_igual} números iguais.')


def quant_iguais(n1, n2, n3):
    
    if n1 == n2 == n3:
        return 3
    elif n1 != n2 != n3:
        return 0
    else:
        return 2

main()