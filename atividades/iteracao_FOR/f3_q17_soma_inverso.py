def mostrar(cont_crescente, cont_decrescente, n):
    if cont_crescente < n - 1:
        print(f'{1}/{cont_decrescente} +', end = " ") 
            
    else:
        print(f'{1}/{cont_decrescente} =')
        
def soma_inverso(n):

    somatorio = 0
    den = n
    
    for contador in range(n):
        
        somatorio += 1/ den
        mostrar(contador, den, n)            
        den -= 1
    
    return somatorio


def main():
    print("SOMA DOS INVERSOS")
    
    n = int(input('\nDigite o valor para N: '))
    print("S =", end = " ")
    
    print("\nS = %.2f"%soma_inverso(n))


main()