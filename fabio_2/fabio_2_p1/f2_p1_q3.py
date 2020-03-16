#Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

def main():
    
    print("\n=-=-=-=-=- MAIOR NÚMERO -=-=-=-=-=-=")
    num1 = int(input("\n1º número: "))
    num2 = int(input("2º número: "))
    num3 = int(input("3º número: "))
    
    maior = eh_maior(num1, num2, num3)
    
    print(f'\nO maior número é o {maior}.')
    
def eh_maior(num1, num2, num3):
    
    if num1 > num2 and num1> num3:
        return num1
    elif num2> num1 and num2> num3:
        return num2
    else:
        return num3
    
main()