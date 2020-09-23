def reverse(s):

    revertida = ''
    for i in range(len(s) - 1, -1, -1):
        revertida += s[i]
        
    return revertida


def calcDiferenca(s):

    dif = ''
    for i in range(len(s)):
        dif += str(abs(ord(s[i]) - ord(s[i-1])))
        
    return dif
    
    
def funnyString(s):
    revertida = reverse(s)

    if calcDiferenca(s) == calcDiferenca(revertida):
        return 'Funny'
    else:
        return 'Not Funny'
    
    
def main():
    
    print("It is funny?\n\n")
    conjStrings = []
    n = int(input("Quantas palavras: "))
    
    for i in range(n):
        s = input('Escreva: ')
        conjStrings.append(s)
    
    for j in range(n):
        print(funnyString(conjStrings[j]))


main()