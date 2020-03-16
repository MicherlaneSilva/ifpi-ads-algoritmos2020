#Leia data atual (dia, mês e ano) e data de nascimento 
#(dia, mês e ano) de uma pessoa, calcule e escreva
#sua idade exata (em anos).

def main():
    
    print("-"*10 + " CÁLCULO IDADE "+"-"*10+"\n")
    
    leitor_data = input("Digite a data de hoje(dd/mm/aaaa): ").split("/")
    leitor_aniversario = input("\nDigite a data do seu aniversário(dd/mm/aaa): ").split("/")
    
    dia_h, mes_h, ano_h = int(leitor_data[0]), int(leitor_data[1]), int(leitor_data[2])
    dia_a, mes_a, ano_a = int(leitor_aniversario[0]), int(leitor_aniversario[1]), int(leitor_aniversario[2])
    
    idade = calc_idade(dia_h, mes_h, ano_h, dia_a, mes_a, ano_a)
    
    print(f'Sua idade é {idade} .')


def calc_idade(dia_h, mes_h, ano_h, dia_a, mes_a, ano_a):
    
    total_dias_hoje = ano_h * 365 + mes_h * 30 + dia_h
    total_dias_aniversario = ano_a * 365 + mes_a * 30 + dia_a
    if total_dias_aniversario< total_dias_hoje:    
        idade = (total_dias_hoje - total_dias_aniversario)//365
    else:
        idade = "0, pois você não nasceu."          
    
    return idade

main()
    