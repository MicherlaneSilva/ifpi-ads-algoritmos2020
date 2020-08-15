# Escreva a tabuada dos números de 1 a 10.

def tabuada():
    i = 1
    j = 1
    
    while i <= 10:
        print(f"\nTABUADA {i}\n")
        while j <= 10:
            print(f'{i} X {j} = {i * j}')
            j += 1

        j = 1
        i += 1

def main():
    
    tabuada()

main()