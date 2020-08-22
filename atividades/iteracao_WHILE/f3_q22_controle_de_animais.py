# Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
# nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
# numero de identificação e o peso do boi mais magro e do boi mais gordo.
 
def relatorio(id_animal, nome_animal, peso_animal):
    
    print("+-------------------------------- -----+")
    print("| ID do animal |    Nome   | Peso(KG)  |")
    print("+--------------+-----------+-----------+")
    print("|{:^14}|{:^11}|{:^11}|".format(id_animal, nome_animal, peso_animal))
    print("+--------------+-----------+-----------+")
    
def main():
    
    peso_gordo = 0
    peso_magro = 0
    id_gordo = ""
    nome_gordo = ""
    nome_magro = ""
    id_magro = ""
    cont = 0
    
    print("***** Cadastro dos Bois *******")
    
    n = int(input("Digite o número de fichas: "))
    
    while cont < n:
        
        id_animal = input(f"\nDigite a identificação do {cont+1}º animal: ")
        nome_animal = input("Nome do animal: ")
        peso_animal = float(input("Peso em kg: "))

        if cont == 0:
            peso_gordo = peso_animal
            id_gordo = id_animal
            nome_gordo = nome_animal
            
            peso_magro = peso_animal
            id_magro = id_animal
            nome_magro = nome_animal
            
        if peso_animal > peso_gordo:
            peso_gordo = peso_animal
            id_gordo = id_animal
            nome_gordo = nome_animal
        
        if peso_animal < peso_magro:
            peso_magro = peso_animal
            id_magro = id_animal
            nome_magro = nome_animal
        
        
        cont += 1
        
        
    print(" "*20 +"RELATÓRIO")
    
    print("\n\n"+" "*10+"Animal mais Gordo\n")
    relatorio(id_gordo, nome_gordo, peso_gordo)

    print("\n\n"+" "*10+"Animal mais Magro\n")
    relatorio(id_magro, nome_magro, peso_magro)    
    
    
main()    
    
    
    
            