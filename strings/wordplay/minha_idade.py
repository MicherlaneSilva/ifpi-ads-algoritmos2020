from palindromos import reverse

def qual_idade():
    
    qtd_reversiveis = 0
    minha_idade = 0
    idade_mae = 36
    
    while True:
        
        if reverse(parse_String(minha_idade)) == parse_String(idade_mae):
            qtd_reversiveis += 1
        
        if qtd_reversiveis == 6:
            return minha_idade
            break
        
        minha_idade += 1
        idade_mae += 1
        
        

def parse_String(inteiro):
    
    if inteiro < 10:
        return '0' + str(inteiro)
    else:
        return str(inteiro)
    

