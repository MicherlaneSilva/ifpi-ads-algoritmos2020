# Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

def somatoria(n):
    soma = 0
    
    for i in range(1, n + 1):
        soma += i      
    
    return soma


def main():
    
    print("Somátoria dos elementos de uma  unitária")
    
    n = int(input("\nDigite o valor de N: "))
    
    print(f"\nA soma dos elementos é {somatoria(n)}.")


main()