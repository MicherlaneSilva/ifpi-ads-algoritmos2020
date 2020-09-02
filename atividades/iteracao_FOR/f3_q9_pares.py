# Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.

def pares(limite_s, limite_i):
    
    for i in range(limite_i, limite_s + 1):
        
        if i % 2 == 0:
            print(i, end = " ")
        
        


def main():
    
    print("Pares no intervalo")
    
    limite_i = int(input("\nDigite o limite inferior: "))
    limite_s = int(input("Digite o limite superior: "))
    
    pares(limite_s, limite_i)

main()