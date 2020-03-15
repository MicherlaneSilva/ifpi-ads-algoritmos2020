#Verifique a validade de uma senha fornecida pelo usuário. 
# A senha é 1234. O algoritmo deve escrever
# uma mensagem de permissão de acesso ou não.

def main():
    
    senha = '1234'
    senha_digitada = input("Digite a senha: ")
    
    print(validar_senha(senha, senha_digitada))

def validar_senha(senha, senha_digitada):
    
    if senha == senha_digitada:
        return "Acesso permitido."
    else:
        return "Acesso negado."

main()
