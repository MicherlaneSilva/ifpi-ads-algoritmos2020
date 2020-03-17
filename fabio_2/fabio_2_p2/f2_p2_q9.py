#Leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda etc.), se digitar outro valor deve aparecer valor inválido. 

def main():
    
    dia = int(input('Digite o número do dia: '))
    print(dia_da_semana(dia))

def dia_da_semana(dia):
    
    if dia == 1:
        return 'domingo'
    elif dia == 2:
        return 'segunda-feira'
    elif dia == 3:
        return 'terça-feira'
    elif dia == 4:
        return 'quarta-feira'
    elif dia == 5:
        return 'quinta-feira'
    elif dia == 6:
        return 'sexta-feira'
    elif dia == 7:
        return 'sábado'
    else:
        return 'número inválido'
    

main()
