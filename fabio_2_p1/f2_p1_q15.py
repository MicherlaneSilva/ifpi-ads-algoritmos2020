#  Leia a quantidade de horas aula dadas por dois professores e
#  o valor por hora recebido por cada um.
#  Escreva na tela qual dos professores tem salário total maior.

def main():
    
    print("CÁLCULO SÁLARIO\n")
    
    nome1 = input("Nome 1º professor: ")
    valor_hora1 = float(input("Valor da hora(R$): "))
    quant_hora1 = int(input("Quantidade de horas trabalhadas: "))
    
    nome2 = input("\nNome 2º professor: ")
    valor_hora2 = float(input("Valor da hora(R$): "))
    quant_hora2= int(input("Quantidade de horas trabalhadas: "))
    
    salario1 = calc_salario(valor_hora1, quant_hora1)
    salario2 = calc_salario(valor_hora2, quant_hora2)
    
    nome_maior_salario, salario = maior_salario(salario1, nome1, salario2, nome2)
    
    print(f'\nO professor de maior salário- R$ {salario}- é {nome_maior_salario}')


def calc_salario(valor_hora, quant_hora):
    return valor_hora * quant_hora

def maior_salario(salario1, nome1, salario2, nome2):
    
    if salario1 > salario2:
        return nome1, salario1
    else:
        return nome2, salario2

main()