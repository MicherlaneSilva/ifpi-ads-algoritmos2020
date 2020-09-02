# Escreva a tabuada dos números de 1 a 10.

def tabuada():
    i = 1
    j = 1
    
    for  i in range(1, 11):
        print(f"\nTABUADA {i}\n")
        for j in range(1, 11):
            print(f'{i} X {j} = {i * j}')

        j = 1
        

def main():
    
    tabuada()

main()