# Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

def media_soma(n):
    
    somatorio = 0
    
    print()
    for contador in range(n):
        
        n1 = int(input(f"{contador + 1}º número: "))
        
        somatorio += n1
        
        
    return somatorio/ contador, somatorio


def main():
    
    print("Soma e Média")
    
    n = int(input("Quantidade de vezes: "))
    
    media, soma = media_soma(n)
    
    print(f"\nSoma dos elementos: {soma}")
    print(f"Média dos elementos: {media}")


main()