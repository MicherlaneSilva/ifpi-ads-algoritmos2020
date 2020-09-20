from wordplay import *
from minha_idade import qual_idade
from palindromos import eh_palindromo
from duplas_consecutivas import gerar_palavras

            
menu = '##### WordPplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem "e"\n' \
        + '3 - Palavras que não proibidas\n' \
        + '4 - Formar palavras com as seguintes letras\n' \
        + '5 - Palavras com letras obrigatórias\n' \
        + '6 - Verificar se está em ordem alfabética\n' \
        + '7 - Palavras com três letras dupla consecutivas\n'\
        + '8 - Números palíndromos\n' \
        + '9 - Minha idade\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

def main():
    opcao = int(input(menu))

    while opcao != 0:
            if opcao == 1:
                palavras_20_caracteres()
                
            elif opcao == 2:
                print(f"Existe {palavras_sem_E()} palavras que não possuem a letra E.")
                        
            elif opcao == 3:
                letras = input("Digite as letras que proíbidas(xxxxx): ")
                print(f"Existem {avoids(letras)} palavras que não são proíbidas.")
            
            elif opcao == 4:
                letras = input("Digite as letras(xxxxx): ")
                print(f'Existem {uses_only(letras)} que usam somente essas letras.')
            
            elif opcao == 5:
                letras = input("Digite as letras que devem aparecer: ")
                print(f"Há no total {uses_all(letras)} palavras com essas letras.")
            
            elif opcao == 6:
                print(f"Tem {qtd_abecedarian()} palavras em ordem alfabética.")
            
            elif opcao == 7:
                gerar_palavras()
            
            elif opcao == 8:
                
                for i in range(100000, 1000000):
                    numero = str(i)
                    
                    if eh_palindromo(numero):
                        print(numero)
    
            elif opcao == 9:
                print(f'Minha idade é {qual_idade()}.')
                
            else:
                print('Opção Inválida!')

            input('continuar <enter> ...')
            opcao = int(input('\n'+menu))

    print('Fim wordplay....')


main()
