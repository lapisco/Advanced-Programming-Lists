#Fazer um fluxograma para ler as notas de um concurso, inicialmente não se sabe o número de candidatos. Ler as notas
# até encontrar um valor negativo, o “flag”. Ao final, informar o número de candidatos, a média aritmética, a maior nota
# lida e a menor nota lida. Tratar adequadamente quando for lista vazia, o primeiro valor for negativo
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
    print('Digite as notas um a um: \npressione apenas enter sem ter digitado nada para sair da inserção de notas')
    n = 0
    cont = 1
    z = 0
    while z == 0:
        n = input("nota{:} :".format(cont))
        if n == '':
            z = 1
        else:
            num_array.append(int(n))
            cont += 1
    num_array.append(-1)
    tam,arr,media,maior,menor = ler_lista(num_array)
    if tam == 0:
        print("A lista está vazia!!, não foram adicionadas notas")
    else:
        print("Ao todo foram {:} candidatos\nSuas notas são respectivamente :{:}"
              "\nA média das notas é {:}\nA maior nota é {:}\nA menor nota é {:}".format(tam,arr,media,maior,menor))
