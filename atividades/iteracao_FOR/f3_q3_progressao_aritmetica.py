#Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
#Aritmética que tem por valor inicial A0 e razão R.

#a_n = a_0 + (n-1) * r
def mostrar_progressao(a0, r, limite):
    n = 2
    
    while limite > (a0 + (n-1) * r):
        print(a0 + (n-1) * r)
        n +=1

def main():
    print('PROGRESSÃO ARTMÉTICA')
    
    a0 = int(input("\nDigite o valor inicial da progressão: "))
    r = int(input("Digite a razão: "))
    limite = int(input("Digite o limite para a progressão: "))
    
    mostrar_progressao(a0, r, limite)


main()