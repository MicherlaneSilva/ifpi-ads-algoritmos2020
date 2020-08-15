# Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

def somatoria(n):
    soma = 0
    
    while n > 0:
        soma += n
        n -= 1
    
    return soma


def main():
    
    print("Somátoria dos elementos de uma  unitária")
    
    n = int(input("\nDigite o valor de N: "))
    
    print(f"\nA soma dos elementos é {somatoria(n)}.")


main()