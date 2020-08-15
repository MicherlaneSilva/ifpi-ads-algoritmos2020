# Leia N e uma lista de N números e escreva o maior número da lista.


def maior_numero(n):
    
    contador = 1
    print()
    
    if n > 0:
        n1 = int(input("1º número: "))
        maior = n1
        
        while contador < n:
            
            n1 = int(input(f"{contador + 1}º número: "))
            
            if maior < n1:
                maior  = n1
            
            contador += 1
            
        return maior
    
    else:
        return "nenhum"


def main():
    
    print("Maior número")
    
    n = int(input("\nQuantidade de vezes: "))
    
    print(f'\nO maior número é {maior_numero(n)}.')


main()