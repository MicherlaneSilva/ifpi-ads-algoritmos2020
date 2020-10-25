import os
import json

def main():
    
    # inicializar (recuperar do banco de dados)
    celulares = inicializar('celulares.bd')
    
    menu = tela_principal()
    opcao = int(input(menu))
    
    while opcao != 0:
        if opcao == 1:
            print('Criando novo celular')
            id_celular = len(celulares) + 1
            celular = novo_celular(id_celular)
            
            #salvar novo celular
            celulares.append(celular)
            print('Celular cadastrado com sucesso!')
            
        elif opcao == 2:
            # listar celulares
            mostrar_celulares(celulares)
        
        elif opcao == 3:
            nome = input('Digite o nome: ')
            buscar_celulares(celulares, nome)
            
            resposta = input('Deseja selecionar um celular?(s/n) ')
            
            if resposta in ('s', 'sim', 'y', 'yes'):
                gerenciar_dados(celulares)
                
            

        input('\n<enter> to continue...')
        opcao = int(input(menu))
    
    # finalizar (salva banco)
    finalizar('celulares.bd', celulares)


def gerenciar_dados(celulares):
    cod_celular = int(input('\nID: '))
    menu = menu_edicao()
    
    opcao = int(input(menu))
    while opcao != 0:
        for celular in celulares:
            if celular['id'] == cod_celular:
                if opcao == 1:
                    #Detalhes
                    mostrar_detalhes(celular)
                    
                elif opcao == 2:
                    #remover
                    del celulares[celulares.index(celular)]
                    print('Celular removido com sucesso!')
            
                elif opcao == 3:
                    #Edição dos dados
                    print("Campos:\nnome\nmarca\ntela\nvalor\ncam_frontal")
                    campo = input("Digite o nome do campo: ")
                    editar_celular(celular, campo) 
                    
                elif opcao == 4:
                    novo_celular = duplicar_registro(len(celulares) + 1, celular)
                    celulares.append(novo_celular)
                    print('Registro duplicado com sucesso!')
        
        input('<enter> to continue...')
        opcao = int(input(menu))
    

def editar_celular(celular, campo):
    
    if campo == 'nome':
        celular[campo] = input('Nome: ')
    elif campo == 'marca':
        celular[campo] = input('Marca: ')
    elif campo == 'tela':
        celular[campo] = input('Tela("): ')
    elif campo == 'valor':
        celular[campo] = float(input('Valor(R$): '))
    elif campo == 'cam_frontal':
        celular[campo] = input('Câmera frontal(sim/não): ')
    else:
        print('Não podemos editar o campo pedido.')
        

def duplicar_registro(id_celular, celular):
    
    celular = {
        'id': id_celular,
        'nome': celular['nome'],
        'marca': celular['marca'],
        'tela': celular['tela'],
        'valor': celular['valor'],
        'cam_frontal': celular['cam_frontal']
    }
    
    
    return celular

    
def menu_edicao():
    menu = '\n*** Editar dados ***\n'
    menu += '1 - Mostrar detalhes\n'
    menu += '2 - Remover\n'
    menu += '3 - Editar\n'
    menu += '4 - Duplicar registro\n'
    menu += '0 - Sair do Menu de Edição\n'
    menu += '\nOpção >>> '
    
    return menu


def finalizar(nome_arquivo, celulares):
    dados = json.dumps(celulares)
    arquivo = open(nome_arquivo, 'w')
    arquivo.write(dados)
    arquivo.close()
    
    
#Arquivo
def inicializar(nome_arquivo):
    celulares_carregados = []
    if os.path.exists(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        dados = arquivo.readline()
        arquivo.close()
        celulares_carregados = json.loads(dados)
    
    return celulares_carregados


def mostrar_detalhes(celular):
    print('id:', celular['id'])
    print('nome: ', celular['nome'])
    print('marca: ', celular['marca'])
    print('tela: ', celular['tela'])
    print('valor: ', celular['valor'])
    print('Câmera frontal: ', celular['cam_frontal'])
    print('-'*12)


def buscar_celulares(celulares, nome):
    
    print("\nResultados da pesquisa\n")
    celulares_encontrados = []
    
    for celular in celulares:
        if nome in celular['nome'] or nome in celular['marca']:
            celulares_encontrados.append(celular)
    
    if len(celulares_encontrados) == 0:
        print("Nenhum celular encontrado, tente outras chaves.")
    else:
        mostrar_celulares(celulares_encontrados)
    


def mostrar_celulares(celulares):
    qtd = len(celulares)
    print(f'\nTotal de celulares: {qtd} \n')
    
    for celular in celulares:
        print('-'*15)
        print('id', celular['id'])
        print('nome: ', celular['nome'])
        print('marca: ', celular['marca'])
        print('valor: ', celular['valor'])
        
    
    
def novo_celular(id_celular):
    # obter dados
    nome = input('Nome: ')
    marca = input('Marca: ')
    tela = input('Tela("): ')
    valor = float(input('Valor (R$): '))
    cam_frontal = input("Câmera frontal(sim/não): ")
    
    
    celular = {
        'id': id_celular,
        'nome': nome,
        'marca': marca,
        'tela': tela,
        'valor': valor,
        'cam_frontal': cam_frontal
    }
    
    return celular
    
    
def tela_principal():
    menu = '\n*** Apps Jobs ***\n'
    menu += '1 - Novo celular\n'
    menu += '2 - Listar celulares\n'
    menu += '3 - Buscar celular por nome\n'
    menu += '0 - Sair do App\n'
    menu += '\nOpção >>> '
    
    return menu


if __name__ == "__main__":
    main()