import matplotlib.pyplot as plt

def main():
    print("\n"+"="*60)
    print("IMPOSTO DE RENDA")
    
    renda = float(input("Renda (R$): "))
    
    tributo = calc_tributo_atual(renda)
    tributo2 = calc_tributo_certo(renda)
    
    imposto1 = calc_imposto(tributo, renda)
    imposto2 = calc_imposto(tributo2, renda)
    
    arquivo = open('imposto.txt','w')
    
    arquivo.write(str(tributo)+'% (Tabela Atual)'+',')
    arquivo.write(str(imposto1))
    arquivo.write('\n')
    arquivo.write(str(tributo2)+'% (Tabela Corrigida)'+',')
    arquivo.write(str(imposto2))
    arquivo.write('\n')
    
    arquivo.close()
    
    x = ['0']
    y = ['0']
    
    dataset = open('imposto.txt','r')
    
    for line in dataset:
        line = line.strip()
        X, Y = line.split(',')
        x.append(X)
        y.append(Y)
        
    x.sort()
    y.sort()
    dataset.close()
    
    plt.bar(x, y,color ='red')
    plt.title('Comparação dos Impostos Pagos')
    plt.xlabel('Percentual imposto')
    plt.ylabel('Valor')
    plt.show()
        
    
    #print("\n"+"="*60)
    #print("RESULTADO")
    #print("Imposto tabela atual: R$ %.2f"%(imposto1))
    #print("Imposto tabela corrigida: R$ %.2f"%(imposto2))


def calc_tributo_atual(renda):
    
    if renda <= 1903.98:
        return 0
    elif renda <= 2826.66:
        return 7.5
    elif renda <= 3751.05:
        return 15
    elif renda <= 4664.68:
        return 22.5
    else:
        return 27.5

def calc_tributo_certo(renda):
    
    if renda <= 3881.65:
        return 0
    elif renda <= 5714.11:
        return 7.5
    elif renda <= 7654.67:
        return 15
    elif renda <= 9564.42:
        return 22.5
    else:
        return 27.5


def calc_imposto(tributo, renda):
    
    return renda * tributo/100
      

    
main()