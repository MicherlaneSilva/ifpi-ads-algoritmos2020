# Leia uma matriz quadrada de ordem N e 
# encontre a linha que possui a maior e a menor soma dos
# elementos.


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


def mostrarMatriz(matriz, linhas):
    for i in range(linhas):
        print(matriz[i][:])
        
        
def encontrarSomas(matriz):
    soma_maior = sum(matriz[0])
    soma_menor = sum(matriz[0])
        
    for celula in matriz:
        if sum(celula) > soma_maior:
            soma_maior = sum(celula) 
        if sum(celula) < soma_menor:
            soma_menor = sum(celula) 
    
    return soma_maior, soma_menor


def main():
    ordem  = int(input("Ordem da matriz quadrada: "))
    matriz = gravarMatriz(ordem)
    mostrarMatriz(matriz, ordem)
    maior_soma, menor_soma = encontrarSomas(matriz)
    print(f'A maior soma é {maior_soma}.\nA menor soma do elementos é {menor_soma}.')
    
    
main()
    