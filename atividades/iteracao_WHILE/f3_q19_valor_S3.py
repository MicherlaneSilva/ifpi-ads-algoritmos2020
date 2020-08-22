def mostrar(contador, auxiliar, c):
    if contador == 1 and c == "c":
        print(f"S = {contador}/{auxiliar}", end = " ")
    else:
        print(f"+ {contador}/{auxiliar}", end = " ")
    
def soma_s(n):
    
    contador = 1
    auxiliar = n
    s = 0
    
    while contador < n + 1:
        
        if contador % 2 == 1:            
            s += contador / auxiliar            
            mostrar(contador, auxiliar, 'c')
                
        else:            
            s += auxiliar / contador
            mostrar(auxiliar, contador, 'a')
            
    
        auxiliar -= 1
        contador += 1
        
    return s

def main():
    print("SOMA\n")
    
    n = int(input("Digite o valor para N: "))
    
    print()
    print("\nS = %.2f"%soma_s(n))
    
    
main()