# Na matemática, a Sucessão de Fibonacci (ou Sequência de Fibonacci),
#  é uma sequência de números inteiros, começando normalmente
#  por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores. 


# Leia um número N, calcule e escreva os N primeiros termos de seqüência de Fibonacci
# (0,1,1,2,3,5,8,...). O valor lido para N sempre será maior ou igual a 2.


def seq_fibonacci(n):
    
    f1 = 0
    f2 = 1
    f3 = 0
    
    
    print(f1, f2 , end = " ")
    
    for i in range(2, n):
        
        f3 = f1 + f2
        
        print(f3, end = " ")
        f1 = f2 
        f2 = f3
        


def main():
    
    print("SEQUÊNCIA DE FIBONACCI")
    
    n = int(input("Quantos elementos da sequência você quer que seja exibida? "))
    seq_fibonacci(n)
    
    
main()