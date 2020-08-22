def mostrar(cont_crescente, cont_decrescente, n):
    if cont_crescente > n - 1:
        print(f'{cont_crescente}/{cont_decrescente} =') 
            
    else:
        print(f'{cont_crescente}/{cont_decrescente} +', end = " ")
        

def sequencia(n):
    
    cont_crescente = 1
    cont_decrescente = n
    s = 0
    
    while cont_crescente < n + 1:
        
        s += cont_crescente / cont_decrescente         
        mostrar(cont_crescente, cont_decrescente, n)   
        cont_decrescente -= 1
        cont_crescente += 1
        
    return s

    

def main():
    
    print("SEQUÊNCIA\n")
    
    n = int(input("Digite o valor para N: "))
    
    print("S = %.2f"%sequencia(n))
    
    
main()