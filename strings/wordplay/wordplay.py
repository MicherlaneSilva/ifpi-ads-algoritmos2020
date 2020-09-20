def palavras_20_caracteres():
    '''Palavras que possuem mais
    de 20 caracteres.'''
    
    arquivo = open('words.txt')
    
    for linha in arquivo:
        
        palavra = linha.strip()
        if len(palavra) > 20:
            print(palavra)
    
    arquivo.close()


def palavras_sem_E():
    '''Palavras que não possuem a letra E.'''
    qtd_palavras = 0
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if has_no_e(palavra):
            qtd_palavras += 1
    
    return qtd_palavras


def has_no_e(palavra):
    '''Verifica se a palavra possue a letra E.'''
    
    for letra in palavra:
        if letra ==  'e':
            return False

    return True


def tem_letra_proibida(palavra, letras_proibidas):
    '''Verifica se a palavra digitada possui uma ou mais letras proibidas.'''
    
    for letra in letras_proibidas:
        if letra in palavra:
            return True
    
    return False
        

def avoids(letras_proibidas):
    qtd_palavras_inofensivas = 0
    
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if tem_letra_proibida(palavra, letras_proibidas) == False:
            qtd_palavras_inofensivas += 1
    
    return qtd_palavras_inofensivas


def usa_letras(palavra, letras):
    for letra in letras:
        if letra not in palavra:
            return False
        
    return True


def uses_all(letras):
    qtd_palavras = 0
    
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if usa_letras(palavra, letras):
            qtd_palavras += 1
    
    return qtd_palavras


def usa_somente(palavra, letras):
    for letra in palavra:
        if letra not in letras:
            return False
        
    return True


def uses_only(letras):
    qtd_palavras = 0
    
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if usa_somente(palavra, letras):
            qtd_palavras += 1
    
    return qtd_palavras



def is_abecedarian(palavra):
    
    for i in range(1, len(palavra)):
        if palavra[i - 1] > palavra[i]:
            return False
    
    return True


def qtd_abecedarian():
    qtd_palavras = 0
    
    arquivo = open('words.txt')
    
    for linha in arquivo:
        palavra = linha.strip()
        if is_abecedarian(palavra):
            qtd_palavras += 1
    
    return qtd_palavras

print(avoids('a'))


    