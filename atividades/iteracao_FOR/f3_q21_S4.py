def mostrar(numerador, denominador, n):
    
    if denominador != n:
        print(f'{numerador}/{denominador} +', end = " ")
    else:
        print(f'{numerador}/{denominador}')
    
def soma_s(n):
    
    contador = 0
    s = 0
    
    while contador < n:
        
        numerador = 2 * contador + 1
        contador += 1
        s += numerador / contador
        mostrar(numerador, contador, n)
    
    return s    

def main():
    
    print("Soma S")
    
    n = int(input("\nDigite o valor para N: "))
    print()
    print("\nS = %.2f"%soma_s(n))


main()

    