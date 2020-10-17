# Leia um vetor com N elementos, encontre e escreva o
# maior e o menor elemento e suas respectivas
# posições no vetor.


def find_greater(listt):
    greater = listt[0]
    position = 0
    
    for i in range(len(listt)):
        if listt[i] > greater:
            greater = listt[i]
            position = i
    
    return greater, position


def find_smaller(listt):
    smaller = listt[0]
    position = 0
    
    for i in range(len(listt)):
        if listt[i] < smaller:
            smaller = listt[i]
            position = i
        
    return smaller, position


def register_values(n):
    print('\nLeitura de valores iniciadas\n')
    listt = []
    for i in range(n):
        value = int(input(f'{i + 1}º valor: '))
        listt.append(value)
        
    return listt


def main():
    print("\n{:^35}".format('*** MAIOR E MENOR VALOR ***'))
    print('\nQuantos valores quer cadastrar? ')
    n = int(input('>>> '))
    
    listt = register_values(n)
    
    greater, positionG = find_greater(listt)
    smaller, positionS = find_smaller(listt)
    
    print("\n{:^35}".format('RESULTADOS'))
    print(f'\nMaior valor: {greater} --> Posição: {positionG + 1}\nMenor valor: {smaller} --> Posição: {positionS + 1}')


main()