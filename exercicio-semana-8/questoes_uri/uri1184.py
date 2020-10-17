def gerarMatriz(ordem):
    
    matriz = []
    for linhas in range(ordem):
        linha = []
        for colunas in range(ordem):
            n = int(input())
            linha.append(n)
        matriz.append(linha)
    
    return matriz


def somaElementos(matriz, ordem, operacao):
    soma = 0
    quant = 0
    
    for i in range(ordem):
        for j in range(ordem):
            if i > j:
                soma += matriz[i][j]
                quant += 1
    
    if operacao == 'M':
        return soma, quant
    else:
        return soma


def calcularMedia(matriz, ordem, operacao):
    soma, quant = somaElementos(matriz, ordem, operacao)
    return soma / quant


def main():
    operacao = input()
    ordem = 12
    matriz = gerarMatriz(ordem)
    if  operacao == 'M':
        print('%.1f'%calcularMedia(matriz, ordem, operacao))
    else:
        print('%.1f'%somaElementos(matriz, ordem, operacao))


main()