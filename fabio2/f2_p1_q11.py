#Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; o
#valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
#possíveis para a variável opção são 1, 2 e 3.

def main():
    
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    num3 = int(input("Digite o 3º número: "))
    opc = int(input("\nOpção (1 a 3): "))
    
    numero = opcoes(num1, num2, num3, opc)
    
    print(f"O número escolhido foi {numero}")
    
def opcoes(num1, num2, num3, opc):
    
    if opc in (1, 2, 3):
        
        if opc == 1:
            return num1
        elif opc == 2:
            return num2
        else:
            return num3
    else:
        return "ERRO\nOpção inválida."


main()
