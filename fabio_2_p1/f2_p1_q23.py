from  validar_data import validar_data
#Leia 2 datas (cada data é composta por 3 
# variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais
# recente.

def main():
    
    data1 = input("1º data(dd/mm/aaaa): ").split('/')
    dia1 = int(data1[0])
    mes1 = int(data1[1])
    ano1 = int(data1[2])
    
    data1 = input("2º data(dd/mm/aaaa): ").split('/')
    dia2 = int(data1[0])
    mes2 = int(data1[1])
    ano2 = int(data1[2])
    
    dia, mes, ano = maior_data(dia1, mes1, ano1, dia2, mes2, ano2)
    
    print(f'A maior data é {dia}/{mes}/{ano}.')

def maior_data(dia1, mes1, ano1, dia2, mes2, ano2):
    if validar_data(dia1, mes1, ano1) == "válida" and validar_data(dia2, mes2, ano2):
        total_dias1 = ano1 * 365 + mes1 * 30 + dia1
        total_dias2 = ano2 * 365 + mes2 * 30 + dia2
        
        if total_dias1 > total_dias2:
            return dia1, mes1, ano1
        else:
            return dia2, mes2, ano2
    else:
        return 0,0,0

main()
    