#Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
# maior quadrado menor que 38 é 36 (quadrado de 6).


def maior_quadrado(n):
    
    c = 0
    
    while True:   
        
        if c ** 2 > n:
            break
        
        c += 1
    
    return (c - 1)**2

def main():
    
    print("Número quadrado perfeito mais próximo")
    
    n = int(input("\nDigite o número inteiro: "))
    
    print(f"\nO número quadrado perfeito mais próximo é {maior_quadrado(n)}.")


main()