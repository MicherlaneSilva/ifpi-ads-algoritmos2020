#Leia valores inteiros em duas variáveis distintas e se o resto 
# da divisão da primeira pela segunda for 1
#escreva a soma dessas variáveis mais o resto da divisão; 
# se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos 
# pelo primeiro; se for igual a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero.
#Em qualquer outra situação
#escreva o quadrado dos números lidos.

def main():
    
    num1 = int(input("1º número: "))
    num2 = int(input("2º número: "))
    
    calculo(num1, num2)
    

def paridade(numero):
    
    if numero % 2 == 0:
        return 'par'
    else:
        return 'ímpar'
    
    
def calculo(num1, num2):
    
    resto = num1 % num2
    if resto == 1:
        print("\nSoma dos número com o resto: ", num1 + num2 + resto)
    elif resto == 2:
        print(f'\nO número {num1} é {paridade(num1)}\nO número {num2} é {paridade(num2)}.') 
    elif resto == 3:
        print("\nSoma dos números multiplicada pelo primeiro: ",(num1+num2) * num1)
    elif resto == 4:
        if num2 != 0:
            print("\nDivisão: ", num1 / num2)
        else:
            print("Impossível divisão por zero.")
    else:
        print(f'Quadrado de {num1} = {num1 ** 2}\nQuadrado de {num2} = {num2 ** 2}')


main()
        