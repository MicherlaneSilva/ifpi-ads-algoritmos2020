def gera_contraCheque(id, qtd_horas_trabalhadas, qtd_dependentes, salario_bruto, INSS, IR, salario_liquido):
    
    print("+" + 121 * "-" + "+")
    print("|    ID   |  QTD HORAS TRABALHADAS | QTD DEPENDENTES | SALÁRIO BRUTO(R$) |    INSS    |     IR     | SALÁRIO LÍQUIDO(R$)  |")
    print("+" + 121 * "-" + "+")
    print("| {:^8}| {:^22} | {:^15} | {:^17} | {:^10} | {:^10} | {:^20} |".format(id, qtd_horas_trabalhadas, qtd_dependentes, round(salario_bruto,2), round(INSS, 2), round(IR, 2), round(salario_liquido, 2)))
    print("+" + 121 * "-" + "+")


def calc_salario_bruto(qtd_horas_trabalhadas, qtd_dependentes):
    return 12 * qtd_horas_trabalhadas + 40 * qtd_dependentes


def calc_INSS(salario_bruto):
    return 8.5 / 100 * salario_bruto


def calc_IR(salario_bruto):
    return 5/100 * salario_bruto


def calc_salario_liquido(salario_bruto, INSS, IR):
    return salario_bruto - INSS - IR


def main():
    
    print("CONTRA-CHEQUES FUNCIONÁRIOS\n")
    
    n = int(input("Digite a quantidade de funcionários: "))
    controler = 0
    while controler < n:
        
        print(f"\n{controler + 1}º FUNCIONÁRIO\n")
        
        id = input("Identificação do funcionário: ")
        qtd_horas_trabalhadas = int(input("Quantidades de horas trabalhadas: "))
        qtd_dependentes = int(input("Número de dependentes: "))


        salario_bruto = calc_salario_bruto(qtd_horas_trabalhadas, qtd_dependentes)
        INSS = calc_INSS(salario_bruto)
        IR = calc_IR(salario_bruto)
        salario_liquido = calc_salario_liquido(salario_bruto, INSS, IR)
        
        print("\n")
        gera_contraCheque(id, qtd_horas_trabalhadas, qtd_dependentes, salario_bruto, INSS, IR, salario_liquido)
        
        
        controler += 1
        
main()