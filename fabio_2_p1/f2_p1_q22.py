#Leia a hora do início de um jogo e a hora de fim do
# jogo (cada hora é composta por 2 variáveis inteiras:
#hora e minuto). Calcule e escreva a duração do jogo
# (horas e minutos), sabendo-se que o tempo
#máximo de duração do jogo é de 24 horas e que ele 
# pode iniciar-se em um dia e terminar no dia
#seguinte.

def main():
    print('DURAÇÃO DO JOGO\n')
    
    leitor1 = input("Horário do início do jogo(HH:MM)>> ").split(':')
    hora_i = int(leitor1[0])
    min_i = int(leitor1[1])
    
    leitor1 = input("Horário do fim do jogo(HH:MM)>> ").split(':')
    hora_f = int(leitor1[0])
    min_f = int(leitor1[1])
    
    horas, minutos = duracao_par(hora_i, min_i, hora_f, min_f)
    
    print(f"O jogo durou {horas}h {minutos}min.")

def duracao_par(hora_i, min_i, hora_f, min_f):
    
    if hora_f > hora_i:
        duracao = (hora_f * 60 + min_f) - (hora_i * 60 + min_i)
    elif hora_f == hora_i:
        if min_f > min_i:
            duracao = min_f - min_i
        else:
            duracao = 60 * 24
            
    else:
        duracao = (hora_f * 60 +min_f) + (24 * 60 - (hora_i * 60 + min_i))       
    
    horas = duracao // 60
    minutos = duracao % 60
    
    return horas, minutos    
    

main()