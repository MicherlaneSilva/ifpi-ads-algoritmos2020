def listar_inteiros(n):
    for i in range(1, n):
        print(i)
        
        


def main():
    
    print("LISTA DE NÚMEROS INTEIROS")
    
    while True:
        try:
            n = int(input('\nDigite um número inteiro: '))
            listar_inteiros(n)
            break
        
        except:
            print("Erro. Por favor, digite apenas números inteiros.")
    
    print("Fim do programa.")

main()