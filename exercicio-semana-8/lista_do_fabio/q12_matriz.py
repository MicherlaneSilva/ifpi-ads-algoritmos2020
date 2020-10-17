def gravar_matriz(n):
    matriz = []
   
    for i in range(n):
        linha = []
        print(f'\nLinha {i + 1}\n')
        for j in range(n):
            numero = int(input(f'A[{i + 1}][{j + 1}] = '))
            linha.append(numero)
        matriz.append(linha)
        
    return matriz


def mostrar_matriz(matriz):
    
    print('\n*** MATRIZ ***')
    n = len(matriz)
    
    for linha in matriz:
        for j in range(n):
            print(linha[j], end = ' ')
        print()


def soma_elementos(matriz, tipo):
    
    n = len(matriz)
    soma = 0 
    
    for i in range(n):
        for j in range(n):
            if tipo == 'secundaria' and i + j == n - 1:
                soma += matriz[i][j]
            elif tipo == 'principal' and i == j:
                soma += matriz[i][j]
            elif tipo == 'demais' and i + j != n - 1 and i != j:
                soma += matriz[i][j]
    return soma


def main():
    print("*** Soma dos Elementos da Matriz Quadrada ***")
    
    n = int(input("\nOrdem da matriz: "))
    
    matriz = gravar_matriz(n)
    mostrar_matriz(matriz)
    
    print("\n*** RESULTADOS ***\n")
    print(f"Soma dos elementos da diagonal principal: {soma_elementos(matriz,'principal')}")
    print(f"Soma dos elementos da diagonal secundária: {soma_elementos(matriz, 'secundaria')}")
    print(f"Soma dos demais elementos: {soma_elementos(matriz, 'demais')}")


main()