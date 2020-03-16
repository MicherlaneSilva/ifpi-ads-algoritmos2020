#Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.

def main():
    print('SEXO\n')    
    sexo = input("Digite o sexo(F/M): ").upper()
    print(validar_sexo(sexo))
    

def validar_sexo(sexo):
    
    if sexo == 'F':
        return 'F - feminino'
    elif sexo == 'M':
        return 'M - masculino'
    else:
        return 'Sexo inválido'


main()
