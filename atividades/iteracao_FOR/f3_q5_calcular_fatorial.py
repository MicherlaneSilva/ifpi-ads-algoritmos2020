# Leia um número, calcule e escreva seu fatorial.

def calc_fatorial(n):
    
    fatorial = 1
    
    for i in range(1, n + 1):
        fatorial  *= i

    return fatorial


def main():
    
    print("CALCULAR FATORIAL")
    
    n = int(input("\nDigite um número inteiro: "))
    
    print(f'{n}! = {calc_fatorial(n)}')

main()