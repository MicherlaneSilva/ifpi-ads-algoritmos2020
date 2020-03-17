def main():
    
    valor_hora = float(input('Valor da hora R$ '))
    quant_hora = int(input('Quantidade de horas trabalhadas: '))
    
    salario = calc_sal(valor_hora, quant_hora)
    percen = calc_per(salario)
    desconto_ir = calc_ir(salario, percen)
    fgts = calc_fgts(salario)
    inss  = calc_inss(salario)
    total_descontos = calc_descontos(desconto_ir, inss)
    sal_liquido = salario_liquido(salario, total_descontos)
    
    print(f'\nSalário Bruto:({valor_hora} * {quant_hora})   :R$ {salario}')
    print(f'(-)IR ({percen}%)   :R$ {desconto_ir}')
    print(f'(-)INSS(10%) :R$ {inss}')
    print(f'FGTS  : R${fgts}')
    print(f'Total de descontos: R$ {total_descontos}')
    print(f'Salário líquido: R$ {sal_liquido}')
    
    
def salario_liquido(salario, total_descontos):
    return salario - total_descontos

def calc_descontos(desconto_ir, inss):
    return desconto_ir + inss

def calc_inss(salario):
    return salario * 10/ 100

def calc_sal(valor_hora, quant_hora):
    return valor_hora * quant_hora

def calc_ir(salario, percen):
    return salario * percen/100

def calc_fgts(salario):
    return salario * 11 /100

def calc_per(salario):
    
    if salario <= 900:
        return 0
    elif salario <= 1500:
        return 5
    elif salario < 2500:
        return 10
    else:
        return 20

main()
