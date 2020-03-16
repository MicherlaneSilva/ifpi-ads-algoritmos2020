#Leia uma letra e verifique se a letra digitada é vogal ou consoante.

def main():
    
    print('CONSOANTE OU VOGAL\n')
    letra = input("Digite uma letra: ").upper()
    print(f'O caractere {letra} ', eh_vogal(letra))

def eh_vogal(letra):
    
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if letra in abc:
        if letra in 'AEIOU':
            return 'é vogal'
        else:
            return 'é consoante'
    else:
        return 'não é letra'
main()