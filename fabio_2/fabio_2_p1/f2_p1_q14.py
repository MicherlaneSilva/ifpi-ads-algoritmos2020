#Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.
def main():
    
    print('MÉDIA\n')
    
    n1 = int(input("1º número: "))
    n2 = int(input("2º número: "))
    n3 = int(input("3º número: "))
    n4 = int(input("4º número: "))
    n5 = int(input("5º número: "))
    
    media = calc_media(n1, n2, n3, n4, n5)
    
    print('\nMédia: %.2f'%media)
    print("\nNúmeros acima da média")
    acima_media(n1,n2, n3, n4, n5, media)
    print("\n")
    
def calc_media(n1, n2, n3, n4, n5):
    
    return (n1+n2+n3+n4+n5)/5

def acima_media(n1,n2, n3, n4, n5, media):
    
    if n1 > media:
        print(n1, end=' ')
    if n2 > media:
        print(n2, end=' ')
    if n3 > media:
        print(n3, end=' ')
    if n4 > media:
        print(n4, end=' ')
    if n5 > media:
        print(n5, end=' ')
    if n1< media and n2 <media and n3 < media and n4<media and n5 <media:
        print("Nenhum número acima da média.")
        

main()
 