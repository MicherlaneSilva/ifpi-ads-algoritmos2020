#Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

def main():
    
    print("="*10 + " MAIOR E MENOR NÚMERO "+10*"="+"\n")
    num1 = int(input("Digite o 1º número: "))
    num2 = int(input("Digite o 2º número: "))
    
    maior, menor = maior_e_menor(num1, num2)
    
    print('\n'+"="*16 +" RESULTADO "+15*"=")
    print(f'\nO maior número é {maior}.\nO menor número é {menor}.')

def maior_e_menor(num1, num2):
    
    if num1 > num2:
        return num1, num2
    else:
       return num2, num1

main()

    
