def eh_letra(codigo):
    return 97 <= codigo <= 122 or 65 <= codigo <= 90


def codify1(texto):
    
    resultado = ""
    
    for i in range(len(texto)):
        if eh_letra(ord(texto[i])):
            resultado += chr(ord(texto[i]) + 3)
        else:
            resultado += texto[i]
    
    return resultado
            

def codify2(texto):
    
    resultado = ""
    
    for i in range(len(texto) - 1, -1, -1):
        resultado += texto[i]
    
    return resultado

def codify3(texto):
    resultado = ""
    
    for i in range(len(texto)):
        if i >= (len(texto) // 2):
                resultado += chr(ord(texto[i]) - 1)
        else:
            resultado += texto[i]
    
    return resultado


def criptografar(texto):
       
    return codify3(codify2(codify1(texto)))

    
def main():
    print("CRITOGRAFAR TEXTO\n")
    
    texto = input("Texto: ")
    print(f"Resultado da criptografia do texto '{texto}'  é '{criptografar(texto)}'.")
    
main()