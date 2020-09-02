
def impares(limite_s, limite_i):
    
    for i in range(limite_i, limite_s + 1):
        
        if i % 2 != 0:
            print(i, end = " ")
                  


def main():
    
    print("Ímpares no intervalo")
    
    limite_i = int(input("\nDigite o limite inferior: "))
    limite_s = int(input("Digite o limite superior: "))
    
    impares(limite_s, limite_i)

main()