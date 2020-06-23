# Fazer um fluxograma estatístico para um clube. Os valores serão fornecidos na seguinte ordem para cada sócio, uma
# letra informativa do sexo (M ou F) e um número relativo à idade. O fim da lista será dado quando a letra do sexo não for
# um M ou F. Ao final, informar o total de sócios, o total de homens, o total de mulheres, e a média de idade para cada
# sexo.
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
                # maior,menor,_ = maior_menor_dif(array[:-1])
                return len(array)-1,np.mean(arr)
            else:
                arr.append(array[i])

if __name__ == '__main__':
    num_array_Masc = list()
    num_array_Fem = list()
    print("pressione apenas enter sem ter digitado nada para sair da inserção de notas")
    n = 0
    cont = 1
    z = 0
    while z == 0:
        print('Digite M ou F para o sexo do sócio:')
        sexo = input()
        if sexo == 'M':
            n = input("idade do sócio{:} :".format(cont))
            num_array_Masc.append(int(n))
            cont+=1
        elif sexo == 'F':
            n = input("idade do sócio{:} :".format(cont))
            num_array_Fem.append(int(n))
            cont+=1
        else:
            z = 1
    num_array_Masc.append(1000)
    num_array_Fem.append(1000)
    total1,mean1 = ler_lista(num_array_Masc)
    total2,mean2 = ler_lista(num_array_Fem)
    if (total1 == 0) and (total2 ==0):
        print("A lista está vazia!!, não foram adicionados nenhum candidato")
    else:
        print("Ao todo foram cadatrados {:} sócios, com um total de {:}"
              " sócios do sexo masculino e com uma média de idade de {:} anos,"
              " e {:} sócios do sexo feminino com uma média de idade de {:} "
              "anos".format(total1+total2,total1,mean1,total2,mean2))
