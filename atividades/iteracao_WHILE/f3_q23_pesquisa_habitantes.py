# A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
# número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
# escreva:
# a) média de salário da população;
# b) média de número de filhos;
# c) percentual de pessoas com salário de até R$ 1.000,00.

def media(x, n):
    return x / n


def main():
     
    cont = 0
    salarios_populacao = 0
    total_filhos = 0
    qtd_salarios_menores = 0
    
    n = int(input("Qual a quantidade de habitantes tem na cidade? "))
    
    while cont < n:
        
        print(f"\nHabitante Nº {cont + 1}")
        salario = float(input("\nQuanto é o seu salário? "))
        qtd_filhos = int(input("Quantos filhos você tem? "))
        
        salarios_populacao += salario
        total_filhos += qtd_filhos
        
        if salario < 1000:
            qtd_salarios_menores += 1
        
        cont += 1
    
    print("\nRESULTADOS")
    
    print("\nMédia salarial da população: %.2f"%media(salarios_populacao, n))
    print("Média de filhos por habitantes: %.1f"%media(total_filhos, n))
    print("Percentual de pessoas com salário abaixo de R$ 1000,00: %.2f"%(media(qtd_salarios_menores, n) * 100))
    

main()