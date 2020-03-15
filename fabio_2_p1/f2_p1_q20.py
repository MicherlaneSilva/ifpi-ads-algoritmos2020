#Leia a medida de um ângulo (entre 0 e 360°) e 
# escreva o quadrante (primeiro, segundo, terceiro ou
#quarto) em que o ângulo se localiza.

def main():
    
    print("QUADRANTE\n")
    
    angle = int(input("Digite o ângulo: "))
    quadrante = quadra(angle)
    print("O ângulo se encontra no ", quadrante)


def quadra(angle):
    
    if angle < 91:
        return "1º quadrante"
    elif angle < 181:
        return "2º quadrante"
    elif angle< 271:
        return "3º quadrante" 
    else:
        return "4º quadrante"
    

main()