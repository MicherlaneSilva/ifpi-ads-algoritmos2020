# Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

def primos(limite_s, limite_i):
    contador = 1
    divisores = 0
    
    while limite_i < limite_s + 1:
        
        while contador < limite_i + 1:
            
            if limite_i % contador == 0:
                divisores += 1
                
            contador += 1 
        
        
        if divisores == 2:
            print(limite_i)
            
        divisores = 0
        contador = 1
                        
        limite_i += 1


def main():
    
    print("Números primos")
    
    limite_i = int(input("\nDigite o limite inferior: "))
    limite_s = int(input("Digite o limite superior: "))
    
    primos(limite_s, limite_i)

main()