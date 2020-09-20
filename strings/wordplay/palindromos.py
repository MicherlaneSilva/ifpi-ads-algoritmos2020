def reverse(s):
    
    nova_string = ''
    for i in range(len(s) -1, -1, -1):
        nova_string += s[i]


    return nova_string

def eh_palindromo(s):
    
    if s == reverse(s):
        return True
    else:
        return False



    