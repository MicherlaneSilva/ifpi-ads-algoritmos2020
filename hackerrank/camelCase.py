def eh_maiscula(caractere):
    return 65 <= ord(caractere) <= 90

def camelCase(s):
    qtd_palavras = 1
    for i in range(len(s)):
        if eh_maiscula(s[i]) and i != 0:
            qtd_palavras += 1
    
    return qtd_palavras

def main():
    s = input()
    
    print(camelCase(s))


main()