# Leia uma matriz quadrada de ordem N e 
# escreva se ela é ou não simétrica. Uma matriz quadrada é dita
# simétrica se A[i,j] =A[j,i].

def gravarMatriz(n):
    matriz = []
    
    for i in range(n):
        linha = []
        for j in range(n):
            numero = int(input(f"A[{i}][{j}] = "))
            linha.append(numero)
        matriz.append(linha)
        print()
    
    return matriz


def criarMatriz(linhas, colunas):
    matriz = [0] * linhas
    for i in range(linhas):
        matriz[i] = [0] * colunas
        
    return matriz


def criarTransposta(matriz, ordem):
    transposta = criarMatriz(ordem, ordem)
       
    for i in range(ordem):
        for j in range(ordem):
            transposta[i][j] = matriz[j][i]
        
    return transposta


def mostrarMatriz(matriz, linhas):
    
    for i in range(linhas):
        print(matriz[i][:])
    
    
def main():
    print("MATRIZES SIMÉTRICAS")    
    
    ordem = int(input('\nOrdem da matriz quadrada: '))
    matriz = gravarMatriz(ordem)
    print('\n--- Matriz ---\n')
    mostrarMatriz(matriz, ordem)
    print('\n---Matriz Transposta ---')
    transposta = criarTransposta(matriz, ordem)
    mostrarMatriz(transposta, ordem)
    eh_simetrica = lambda matriz, transposta: matriz == transposta
    print('\nAnálise \nAs matrizes são simétricas: ',eh_simetrica(matriz, transposta))

main()
