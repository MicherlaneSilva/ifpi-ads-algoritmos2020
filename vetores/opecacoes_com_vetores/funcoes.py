def mostrar_lista(lista):
    if lista != []:
        for i in range(len(lista)):
            print(lista[i], end = " ")
    else:
        print("Nenhum valor a ser exibido.")
        
        
def inserir_valores(lista):
    qtd = int(input('\nQuantos valores desejar inserir? '))

    for i in range(qtd):
        valor = int(input(f'{i + 1}º valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    mostrar_lista(lista)


def mostra_valor(lista):
    
    if lista != []:
        posicao = int(input(f'\nQual posição(0 - {len(lista) - 1})? '))
        print('Valor buscado:')
        print(lista[posicao])
    else:
        print("Lista vazia, para usar essa opção insira valores na lista.")


def remover_elemento(lista, posicao = None):
    if lista != []:
        if posicao == None:
            lista.pop()
        elif posicao == 'todos':
            del(lista[0:len(lista)])
        else:
            lista.pop(posicao)
    else:
        print("Lista vazia, para usar essa opção insira valores na lista.")
    
    mostrar_lista(lista)
                

def contar_paridades(lista):
    qtd_pares = 0
    qtd_impares = 0
    
    for i in lista:
        if i % 2 == 0:
            qtd_pares += 1
        else:
            qtd_impares += 1
    
    return qtd_pares, qtd_impares


def verificar_primos(lista):
    primos = []
    
    for n in lista:
        if eh_primo(n):
            primos.append(n)
    
    return primos


def eh_primo(numero):
    qtd_divisores = 0
    
    for i in range(2, numero + 1):
        if numero % i == 0:
            qtd_divisores += 1
    
    if qtd_divisores == 1:
        return True
    else:
        return False
    

def media_valores(lista):
    if lista != []:
        return sum(lista) / len(lista)
    else:
        print("Lista vazia, para usar essa opção insira valores na lista.")
        return 0
    


def contar_ocorrencias(valor, lista):
    return lista.count(valor)


def dobrar_valores_N(n, lista):
    for i in range(len(lista)):
        if lista[i] % n == 0:
            lista[i] = 2 * lista[i]
            

def quadrados_perfeitos(lista):
    square = []
    for n in lista:
        if eh_quadrado_perfeito(n):
            square.append(n)
    
    return square


def eh_quadrado_perfeito(n):
    
    for i in range(n):
        if i** 2 == n:
            return True
    
    return False

def contar_positivos_negativos(lista):
    qtd_positivos = 0
    qtd_negativos = 0
    
    for n in lista:
        if n >= 0:
            qtd_positivos += 1
        else:
            qtd_negativos += 1
    
    return qtd_positivos, qtd_negativos