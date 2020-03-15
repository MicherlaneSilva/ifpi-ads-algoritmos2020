#Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

def main():
    
    print("PRIMO OU NÃO PRIMO?\n")
    
    numero = int(input("Digite um número inteiro: "))
    
    resposta = eh_primo(numero)
        
    print(f'\nO número {numero} é primo? {resposta}')

def eh_primo(numero):
  
    if numero % 2 == 0 and numero != 2:
        return 'Sim.'
    else:
        if numero %3 == 0 and numero !=3 or numero %5 == 0 and numero != 5 or numero % 7==0 and numero != 7:
            return 'Não'
        else:
            return 'Sim.'

main()