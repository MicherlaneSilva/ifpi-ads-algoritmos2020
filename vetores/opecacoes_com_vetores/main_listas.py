from funcoes import *

def main():
    
    menu = '\n\n*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Remover do Final'
    menu += '\n 4 - Remover do Início'
    menu += '\n 5 - Remover de Posição Específica'
    menu += '\n 6 - Quantidade de números pares e ímpares'
    menu += '\n 7 - Números primos na lista'
    menu += '\n 8 - Quantidade de números positivos e negativos'
    menu += '\n 9 - Média dos valores '
    menu += '\n 10 - Quantidade de ocorrências de um valor'
    menu += '\n 11 - Remover todos os elementos da lista'
    menu += '\n 12 - Dobrar valores múltiplos de N'
    menu += '\n 13 - Mostrar números quadrados perfeitos'
    menu += '\n 14 - Mostrar lista de números'
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:  # Condição sempre verdadeira, só irá para em caso de break ou error
        opcao = int(input(menu))

        # Verificar operacao a fazer de acordo com a opcao
        if opcao == 1:
            inserir_valores(lista)
            
        elif opcao == 2:
            mostra_valor(lista)
            
        elif opcao == 3:
            remover_elemento(lista)
            
        elif opcao == 4:
            remover_elemento(lista, 0)
            
        elif opcao == 5:
            posicao = int(input(f"\nPosição(0 - {len(lista)}): "))
            remover_elemento(lista, posicao)
            
        elif opcao == 6:
            qtd_pares, qtd_impares = contar_paridades(lista)
            print(f'\nQuantidade de pares: {qtd_pares}')
            print(f'Quantidade de ímpares: {qtd_impares}')
            
        elif opcao == 7:
            mostrar_lista(verificar_primos(lista))
            
        elif opcao == 8:
            qtd_positivos, qtd_negativos = contar_positivos_negativos(lista)
            print(f"\nQuantidade de números positivos: {qtd_positivos}")
            print(f'Quantidade de números negativos: {qtd_negativos}')
            
        elif opcao == 9:
            print('\nMédia dos valores: %.2f'%media_valores(lista))
            
        elif opcao == 10:
            valor = int(input("\nValor: "))
            print(f'O valor {valor} aparece {contar_ocorrencias(valor, lista)} vezes.')
            
        elif opcao == 11:
            remover_elemento(lista,'todos')
            print(f'\nElementos removidos com sucesso!\n{lista}')
            
        elif opcao == 12:
            n = int(input("\nValor de N: "))
            dobrar_valores_N(n, lista)
            mostrar_lista(lista)
            
        elif opcao == 13:
            print("\nQuadrados Perfeitos Encontrados:")
            mostrar_lista(quadrados_perfeitos(lista))
        
        elif opcao == 14:
            mostrar_lista(lista)
            
        elif opcao == 0:  # sair do while
            break
        else:
            print('Opção Inválida')
        
        input('\n<enter> to continue...')


main()