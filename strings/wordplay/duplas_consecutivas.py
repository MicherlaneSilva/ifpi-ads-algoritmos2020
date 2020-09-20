def duplas_consecutivas(palavra):
    
    cont_duplas = 0
    consecutivas = ""
    for i in range(len(palavra) - 1):
        
            if palavra[i + 1] == palavra[i]:
                consecutivas += palavra[i + 1] + palavra[i]
                cont_duplas += 1
    
    
    if cont_duplas == 3 and consecutivas in palavra:
           return True
                
    

def gerar_palavras():
    arquivo = open('words.txt')
    
    for linha in arquivo:
        word = linha.strip()
        if duplas_consecutivas(word):
            print(word)
        
    arquivo.close()

