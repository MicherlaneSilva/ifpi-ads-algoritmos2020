# Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Geométrica que tem por valor inicial A0 e razão R.

def mostrar_progressao(a0, q, limite):
    n = 1
    
    while limite > (a0 * q **(n-1)):
        print(a0 * q **(n-1))
        n +=1

def main():
    print('PROGRESSÃO GEOMÉTRICA')
    
    a0 = int(input("\nDigite o valor inicial da progressão: "))
    q = int(input("Digite a razão: "))
    limite = int(input("Digite o limite para a progressão: "))
    
    mostrar_progressao(a0, q, limite)


main()