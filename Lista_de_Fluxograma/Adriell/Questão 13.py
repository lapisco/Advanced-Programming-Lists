# Fazer um fluxograma para ler 100 números, calcular a média e o maior valor lido.
import numpy as np
def maiornum_e_media(array):
    maior = array[1]
    for i in range(len(array)):
        if array[i]>maior:
            maior = array[i]
    return maior,np.mean(array)

if __name__ == '__main__':
    num_array = list()
    num = input("Digite o total de números a serem digitados no vetor:")
    print('Digite os números um a um: ')
    for i in range(int(num)):
        n = input("num{:} :".format(i))
        num_array.append(int(n))
    print('ARRAY: ', num_array)
    maior_num,media = maiornum_e_media(num_array)
    print("Para a matriz {:}, a média é: {:},o maior número é: {:}".format(num_array,media,maior_num))