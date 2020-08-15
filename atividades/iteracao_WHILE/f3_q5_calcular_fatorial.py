# Leia um número, calcule e escreva seu fatorial.

def calc_fatorial(n):
    
    fatorial = 1
    
    while 1 <= n:
        fatorial  *= n
        n -= 1

    return fatorial


def main():
    
    print("CALCULAR FATORIAL")
    
    n = int(input("\nDigite um número inteiro: "))
    
    print(f'{n}! = {calc_fatorial(n)}')

main()