#. Fazer um fluxograma para um comprador de melancias, a cada melancia que entra é medido o seu peso. Inicialmente
# não se sabe a quantidade de melancias a serem pesadas, e ao final é fornecido um valor negativo para o peso. A final
# informar a quantidade de melancias, o peso total, a média, o maior e o menor peso lido.
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
            if array[i] <0:
                maior,menor,_ = maior_menor_dif(array[:-1])
                return len(array)-1,arr,np.mean(arr),maior,menor
            else:
                arr.append(array[i])

if __name__ == '__main__':
    num_array = list()
    print('Digite os pesos das melancias(kg) um a um: \npressione apenas enter sem ter digitado nada para sair da inserção de notas')
    n = 0
    cont = 1
    z = 0
    while z == 0:
        n = input("peso{:} :".format(cont))
        if n == '':
            z = 1
        else:
            num_array.append(float(n))
            cont += 1
    num_array.append(-1)
    tam,arr,media,maior,menor = ler_lista(num_array)
    if tam == 0:
        print("A lista está vazia!!,não foram adicionadas melancias")
    else:
        print("Ao todo foram pesadas {:} melancias\nSeus pesos são respectivamente :{:}kg\n "
              "o peso médio das melancias é {:} kg\nA melancia mais pesada pesa {:}kg\n "
              "e a melancia mais pesada pesa {:}kg".format(tam,arr,media,maior,menor))
