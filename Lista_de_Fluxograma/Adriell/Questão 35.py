# . Fazer um fluxograma para ler dois tempos (hora, minuto e segundo) e escrever a diferença de tempo entre eles.
import numpy as np
import math
def dif_temp(tempo1,tempo2):
    total = []
    # total = np.asarray()
    tempo1 = tempo1[0]*3600 + tempo1[1]*60 + tempo1[2]
    tempo2 = tempo2[0] * 3600 + tempo2[1] * 60 + tempo2[2]
    if tempo1>tempo2:
        total = tempo1-tempo2
        maior = 1
        menor = 2
    elif tempo2>tempo1:
        total = tempo2-tempo1
        maior = 2
        menor = 1
    horas = total/3600
    hr,HORAS = math.modf(horas)
    minutos = hr*60
    min, MINUTOS = math.modf(minutos)
    segundos = min*60
    # total.append(int(HORAS))
    # total.append(int(MINUTOS))
    # total.append(int(segundos))
    return (int(HORAS),int(MINUTOS),int(segundos)),maior,menor

if __name__ == '__main__':
    t1 = list()
    t2 = list()
    print("Digite o tempo 1:")
    t1.append(int(input("Digite as horas:")))
    t1.append(int(input("Digite os minútos:")))
    t1.append(int(input("Digite os segundos:")))
    print("Digite o tempo 2:")
    t2.append(int(input("Digite as horas:")))
    t2.append(int(input("Digite os minútos:")))
    t2.append(int(input("Digite os segundos:")))
    temp_seg,maior,menor = dif_temp(t1,t2)
    if maior == 1:
        print("{:} horas,{:} minutos,{:} segundos\n-\n{:} horas,{:} minutos,{:} segundos"
          "\n=\n{:} horas,{:} minutos,{:} segundos".format(t1[0],t1[1],t1[2],t2[0],t2[1],t2[2],temp_seg[0],temp_seg[1],temp_seg[2]))
    else:
        print("{:} horas,{:} minutos,{:} segundos\n-\n{:} horas,{:} minutos,{:} segundos"
              "\n=\n{:} horas,{:} minutos,{:} segundos".format(t2[0], t2[1], t2[2], t1[0], t1[1], t1[2], temp_seg[0],
                                                               temp_seg[1], temp_seg[2]))
