#Existem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
#o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
#milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
#terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
#2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025.

def main():
    
    print("Números Especiais\n")
    
    numero = int(input("Número: "))
    
    print("O número é especial? ",especial(numero))
    

def especial(numero):
    
    n1 = numero // 100
    n2 = numero % 100
    
    if (n1 + n2) ** 2 == numero:
        return "Sim"
    else:
        return 'Não'


main()