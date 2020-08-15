#Leia N e escreva todos os números inteiros pares de 1 a N.

def listar_inteiros(n):
    i = 1
    while i <= n:
        
        if i%2 == 0:
             print(i)
        i += 1


def main():
    
    print("LISTA DE NÚMEROS INTEIROS PARES")
    
    while True:
        try:
            n = int(input('\nDigite um número inteiro: '))
            listar_inteiros(n)
            break
        
        except:
            print("Erro. Por favor, digite apenas números inteiros.")
    
    print("Fim do programa.")

main()