# Fazer um fluxograma para ler hora, minuto e segundo e converter tudo para segundos

def conversão(horas,minutos,segundos):
    return horas*3600 + minutos*60 + segundos

if __name__ == '__main__':
    hr = int(input("Digite as horas:"))
    min = int(input("Digite os minútos:"))
    seg = int(input("Digite os segundos:"))
    temp_seg = conversão(hr,min,seg)
    print("{:} horas,{:} minutos,{:} segundos = {:} segundos".format(hr,min,seg,temp_seg))
