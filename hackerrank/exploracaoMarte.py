ajuda = 'SOS'

def qtdLetras(MSG, ajuda):
    qtdD = 0
    for i in range(len(MSG)):
        if MSG[i] != ajuda[i]:
            qtdD += 1 
        
    return qtdD


def marsExploration(mensagem):
    
    qtdDTotal = 0
    
    for c in range(len(mensagem) + 1):
        
        if c%3 == 0:
             qtdDTotal += qtdLetras(mensagem[(c - 3):c], ajuda)
     
    return qtdDTotal
       
            
def main():
    
    mensagem = input('Escreva a mensagem: ')
    
    while len(mensagem) % 3 != 0:
        print("Por favor complete a mensagem.")
        mensagem = input('Escreva aqui: ')
        
        
    print(f"{marsExploration(mensagem)} letra(s) foi/foram alterada(s).")
    
    
main()   