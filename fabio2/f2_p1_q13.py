#  Leia 5 (cinco) números inteiros e escreva o maior e o menor deles.
#  Considere que todos os valores são
#  diferentes.

def main():
    
    print('Maior e Menor Número\n')
    
    n1 = int(input("1º número: "))
    n2 = int(input("2º número: "))
    n3 = int(input("3º número: "))
    n4 = int(input("4º número: "))
    n5 = int(input("5º número: "))
    
    maior_numero = maior(n1, n2, n3, n4, n5)
    menor_numero = menor(n1, n2, n3, n4, n5)
    
    print(f'\nO maior número é {maior_numero};\nO menor número é {menor_numero}.')

def maior(n1, n2, n3, n4, n5):
    
    if n1 > n2 and n1> n3 and n1 > n4 and n1>n5:
        return n1
    if n2 > n1 and n2> n3 and n2 > n4 and n2>n5:
        return n2
    if n3 > n2 and n3> n1 and n3 > n4 and n3>n5:
        return n3
    if n4 > n3 and n4> n1 and n4 > n2 and n1>n5:
        return n4
    else:
        return n5

def menor(n1, n2, n3, n4, n5):
    
    if n1 < n2 and n1< n3 and n1 < n4 and n1<n5:
        return n1
    if n2 < n1 and n2< n3 and n2 < n4 and n2<n5:
        return n2
    if n3 < n2 and n3< n1 and n3 < n4 and n3<n5:
        return n3
    if n4 < n3 and n4< n1 and n4 < n2 and n1<n5:
        return n4
    else:
        return n5
    
main()