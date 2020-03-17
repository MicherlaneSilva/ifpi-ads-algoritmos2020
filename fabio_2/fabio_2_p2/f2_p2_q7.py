#As Organizações Tabajara resolveram dar um 
#  de salário aos seus colaboradores e lhe
#contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
#salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#o salários até R$ 280,00 (incluindo) : aumento de 20%
#o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#· o salário antes do reajuste;
#· o percentual de aumento aplicado;
#· o valor do aumento;
# o novo salário, após o aumento.

def main():
    print('REAJUSTE SALARIAL\n')
    
    nome = input('Nome do colaborador: ')
    salario = float(input('Salário(R$): '))
    
    percen = calc_percen(salario)
    aumento = calc_aumento(salario, percen)
    novo_salario = salario + aumento
    tabela_reajuste(nome, percen, aumento, novo_salario)
    
def calc_aumento(salario, percen):
    return salario * percen/100


def calc_percen(salario):
    
    if salario <= 280:
        return 20
    elif salario <= 700:
        return 15
    elif salario <= 1500:
        return 10
    else:
        return 5


def tabela_reajuste(nome, percen, aumento, novo_salario):
    
    epc = 16 - len(nome)
    epc2 = 6 - len(str(aumento))
    print('\n'+' '*15 +'TABELA REAJUSTE')
    print('='*55)
    print('|'+' '*6+'NOME'+6*' '+'|'+'PERCENTUAL |'+' AUMENTO |'+' NOVO SALÁRIO |')
    print('-'*55)
    print(f'|{nome}'+' '*epc +f'|{percen}%' + ' ' * 8+f'|R$ {aumento}'+' '*epc2+f'|R${novo_salario}'+' '*5+"|")
    print('='*55)

main()