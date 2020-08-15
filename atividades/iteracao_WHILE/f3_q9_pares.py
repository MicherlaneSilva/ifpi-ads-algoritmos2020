# Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.

def pares(limite_s, limite_i):
    
    while limite_i != limite_s + 1:
        
        if limite_i % 2 == 0:
            print(limite_i, end = " ")
        
        limite_i += 1
        


def main():
    
    print("Pares no intervalo")
    
    limite_i = int(input("\nDigite o limite inferior: "))
    limite_s = int(input("Digite o limite superior: "))
    
    pares(limite_s, limite_i)

main()