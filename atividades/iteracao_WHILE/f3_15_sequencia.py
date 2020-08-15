# Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

def sequencia(n):
    
    c = 0
    elem_seq = 0
    
    while c < n:

        elem_seq += 1
        elem_seq += c
        
        print(elem_seq, end = " ")
        c += 1


def main():
    
    print("SEQUÊNCIA")
    
    n = int(input("Quantos elementos da sequência você quer que seja exibido? "))
    
    sequencia(n)
    

main()