#  Escreva uma função chamada right_justify, que receba uma string chamada s como parâmetro e exiba
#  a string com espaços suficientes à frente para que a última letra da string esteja na coluna 70 da tela:

def main():
    
    print("*"*7 + "JUSTIFICAR TEXTO" + "*" * 7)
    
    palavra = input("Digite uma palavra: ")
    print(right_justify(palavra))

def right_justify(s):
    
    nova_palavra = " " * (70 - len(s)) + s
    return nova_palavra

main()