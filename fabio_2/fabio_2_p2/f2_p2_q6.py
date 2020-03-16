#Leia o turno em que um aluno estuda
#  sendo M para matutino, V para Vespertino ou N para Noturno e
#escreva a mensagem "Bom Dia!", "Boa Tarde!"
# ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def main():
    
    print('Saudação\n')
    turno = input('Turno (M/V/N): ').upper()
    print(saudacao(turno))
    
def saudacao(turno):
    
    if turno == 'M':
        return 'Bom dia!'
    elif turno == 'V':
        return 'Boa tarde!'
    elif turno == 'N':
        return 'Boa Noite!'
    else:
        return 'Turno inválido'

main()