def gerar_vetor(tamanho):
    return [-1]  * tamanho

def eh_par(numero):
    return numero % 2 == 0


def cont_pares(vetor):
    
    qtdPares = 0
    for item in vetor:
        if eh_par(item):
            qtdPares += 1
    
    return qtdPares



def cont_impares(vetor):
    qtdImpares = 0
    for item in vetor:
        if not(eh_par(item)):
            qtdImpares += 1
    
    return qtdImpares
    


def cont_negativos(vetor):
    qtdNegativos = 0
    for item in vetor:
        if not(eh_positivo(item)):
            qtdNegativos += 1
    
    return qtdNegativos



def cont_positivos(vetor):
    qtdPositivos = 0
    for item in vetor:
        if eh_positivo(item):
            qtdPositivos += 1
    
    return qtdPositivos


def eh_positivo(numero):
    return numero > 0


def media(vetor):
    soma = 0
    
    for numero in vetor:
        soma += numero
    
    return soma/ len(vetor)
    
    

def alterar_vetor(vetor):
    for i in range(len(vetor)):
        
        if eh_positivo(vetor[i]):
            vetor[i] = 2 * vetor[i]
        else:
            vetor[i] = vetor[i] / 2
    
    return vetor
    
    

def mostrar_vetor(vetor):
    
    for item in vetor:
        print(item, end = " ")
        
        

def relacao_numerica(qtdPares, qtdImpares, qtdPositivos, qtdNegativos):
    
    print("\n\n{:^60}".format("RELAÇÃO NUMÉRICA"))
    print("+----------------------------------------------------------+")
    print("| QTD PARES | QTD ÍMPARES | QTD POSITIVOS  | QTD NEGATIVOS |")
    print("+-----------+-------------+----------------+---------------+")
    print("|{:^11}|{:^13}|{:^16}|{:^15}|".format(qtdPares, qtdImpares, qtdPositivos, qtdNegativos))
    print("+-----------+-------------+----------------+---------------+")
    
    

def main():
    print("VETORES\n\n")
    
    tamanho = int(input("Digite a quantidade de números: "))
    
    v = gerar_vetor(tamanho)
    print("\nLEITURAS DOS NÚMEROS\n")
    
    for i in range(tamanho):
        numero = int(input(f"{i + 1}º número: "))
        v[i] = numero
    

    print("\nColeção de números criadas com sucesso!\n")
    mostrar_vetor(v)
    relacao_numerica(cont_pares(v), cont_impares(v), cont_positivos(v), cont_negativos(v))
    
    print("\nNova coleção numérica criada!")
    mostrar_vetor(alterar_vetor(v))
    
    relacao_numerica(cont_pares(v), cont_impares(v), cont_positivos(v), cont_negativos(v))
    print(f'\nMédia dos valores da nova coleção: {media(v)}')
    
    
main()  
    
    