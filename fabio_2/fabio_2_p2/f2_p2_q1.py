#Leia um número e mostre na tela se o número é positivo ou negativo.

def main():
    
    print('POSITIVO OU NEGATIVO\n')
    
    numero = float(input("Digite um número: "))
    
    print("O número é ", eh_positivo(numero))
    

def eh_positivo(numero):
    
    if numero < 0:
        return "negativo"
    else:
        return "positivo"


main()