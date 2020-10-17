# Leia um vetor A com N elementos, verifique e escreva se existem ou não elementos iguais no vetor.
def gerar_lista(n):
    A = []
    for i in range(n):
        elemento = input(f"{i + 1}º elemento: ")
        A.append(elemento)
        
    return A


def tem_repetidos(lista):
    for item in lista:
        if lista.count(item) > 1:
            return "Sim"
    return "Não"

    
def main():
    
    while True:
        try:
            n = int(input("Quantos elementos desejar armazenar? "))
            A = gerar_lista(n)
            print(f'\nExistem elementos repetidos na lista? {tem_repetidos(A)}')
            break
        except:
            print("\nPor favor, utilize apenas números inteiros.")
        
main()