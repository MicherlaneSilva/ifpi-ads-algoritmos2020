#Leia um número e escreva se o número é inteiro ou decimal.

def main():
    
    print('INTEIRO OU DECIMAL?\n')
    numero = float(input('Número: '))
    result = eh_racional(numero)
    print(f'O número {numero} é {result}')

def eh_racional(numero):
    
    p_decimal = numero % 1
    if p_decimal == 0:
        return 'inteiro'
    else:
        return 'decimal'

main()