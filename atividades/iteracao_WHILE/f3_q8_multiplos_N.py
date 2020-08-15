# Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

def multiplos_n(limite_s, limite_i, n):

    while limite_i != limite_s + 1:
        
        if limite_i % n == 0:
            print(limite_i, end = " ")
        
        limite_i += 1
        


def main():
    
    print("Múltiplos em um intervalo")
    
    limite_i = int(input("\nDigite o limite inferior: "))
    limite_s = int(input("Digite o limite superior: "))
    n = int(input("Digite o número o qual quer ver os múltiplos: "))
    
    multiplos_n(limite_s, limite_i, n)

main()