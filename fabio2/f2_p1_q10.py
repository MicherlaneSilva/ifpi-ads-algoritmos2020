#Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.

def main():
    
    print("VERIFICAR DATA\n")
    
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    
    resultado = validar_data(dia, mes, ano)
    
    print(f'A data é {resultado}.')
    

def validar_data(dia, mes, ano):
    
    if ano>0:
        if dia in range(1,31) and mes in (4,6,9,11):
            return "válida"
        elif dia in range(1,32) and mes not in (4,6,9,11) and mes != 2:
            return "válida"
        elif dia in range(1,29) and mes == 2:
            return "valida"
        else:
            return "inválida"            
    else:
        return "inválida"

main()