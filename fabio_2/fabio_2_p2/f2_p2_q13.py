def main():
    
    print('EM BUSCA DO ASSASSINO\n')
    print('Responda S para sim e N para não')
    
    r1 = input('Telefonou para a vítima? ').upper()
    r2 = input('Esteve no local do crime? ').upper()
    r3 = input('Mora perto da vítima? ').upper()
    r4 = input('Devia para a vítima? ').upper()
    r5 = input('Já trabalhou com a vítima? ').upper()
    
    resultado = poligrafo(r1, r2, r3, r4, r5)
    
    print('\nResultado da investigação: ', resultado)


def poligrafo(r1, r2, r3, r4, r5):
    respostas = [r1, r2, r3, r4, r5]
    
    if respostas.count('S') == 5:
        return 'Assassino(a)'
    elif respostas.count('S') == 4 or respostas.count('S') ==  3:
        return 'Cúmplice'
    elif respostas.count('S') == 2:
        return 'Suspeito(a)'
    else:
        return 'Inocente'

main()
    