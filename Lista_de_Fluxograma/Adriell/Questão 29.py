# Fazer um fluxograma para ler a temperatura ambiente de uma cidade
# européia. As amostras serão lidas até ser digitado um valor 1000, e
# efetuar as seguintes estatísticas: A quantidade de amostras coletadas, a
# média das temperaturas, a maior e a menor temperatura lida.
import numpy as np
def maior_menor_dif(array):
    maior = array[1]
    menor = array[1]
    for i in range(len(array)):
        if array[i]>maior:
            maior = array[i]
        if array[i]<menor:
            menor=array[i]
    dif = maior-menor
    return maior,menor,dif
def ler_lista(array):
    arr = list()
    if len(array) == 1:
        return 0,0,0,0,0
    else:
        for i in range(len(array)):
            if array[i] == 1000:
                maior,menor,_ = maior_menor_dif(array[:-1])
                return len(array)-1,arr,np.mean(arr),maior,menor
            else:
                arr.append(array[i])

if __name__ == '__main__':
    num_array = list()
    print('Digite as temperaturas(em K) uma a uma: \npressione apenas enter sem ter digitado nada para sair da inserção de notas')
    n = 0
    cont = 1
    z = 0
    while z == 0:
        n = input("Temperatura{:} :".format(cont))
        if n == '':
            z = 1
        else:
            num_array.append(int(n))
            cont += 1
    num_array.append(1000)
    tam,arr,media,maior,menor = ler_lista(num_array)
    if tam == 0:
        print("A lista está vazia!!, não foram adicionadas temperaturas")
    else:
        print("Ao todo foram medidas {:} temperaturas\nAs temperaturas medidas são respectivamente:{:}K"
              "\nA média das emperaturas é {:}K\nA maior temperatura registada é {:}K\n"
              "A menor temperatura registada é {:}K".format(tam,arr,media,maior,menor))
