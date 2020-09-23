def rotate_word(palavra, num_rotation):
    
    palavra_cifrada = ""
    
    for c in palavra:
        
        numero = ord(c) + num_rotation
        if  97 <= numero <= 122:
            codigo = ord(c) + num_rotation
            
        elif ord(c) + num_rotation > 122:
            dif = 122 - ord(c) 
            posi =  num_rotation - dif
            codigo =  97 + posi
        else:
            dif = ord(c) - 97
            posi =  -num_rotation - dif -1
            codigo =  122 - posi
        
        novo_caractere = chr(codigo)
        palavra_cifrada += novo_caractere
            
        
                
    
    return palavra_cifrada


def main():
    print("CIFRA DE CÉSAR")
    
    palavra = input("\nDigite a palavra: ").lower()
    rotacoes = int(input("Digite o número de rotações: "))
    
    print(f"\nA palavra {palavra} em código de César é {rotate_word(palavra, rotacoes)}")


main()