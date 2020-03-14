#Leia 1 (um) número inteiro e escreva se este número é par ou impar.

def main():
    
    numero = int(input("Digite um número inteiro:  "))
    print(f'O número {numero} é {paridade(numero)}.')

def paridade(numero):
    
    if numero % 2  == 0:
        return "par"
    else:
        return "ímpar"


main()