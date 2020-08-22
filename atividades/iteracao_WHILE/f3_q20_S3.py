def mostrar(cont_crescente, cont_decrescente, n, sinal):
    if cont_crescente < n - 1:
        print(f'{1}/{cont_decrescente} ' + sinal, end = " ") 
            
    else:
        print(f'{1}/{cont_decrescente} =')
        
def soma_inverso(n):

    somatorio = 0
    contador = 0
    den = n
    
    while contador < n:
        
        if contador % 2 == 1:
            somatorio += 1/ den
            mostrar(contador, den, n, "+")
            
        else:
            mostrar(contador, den, n, "-")   
            
        contador += 1
        den -= 1
    
    return somatorio


def main():
    print("SOMA DOS INVERSOS")
    
    n = int(input('\nDigite o valor para N: '))
    print("S =", end = " ")
    
    print("\nS = %.2f"%soma_inverso(n))


main()