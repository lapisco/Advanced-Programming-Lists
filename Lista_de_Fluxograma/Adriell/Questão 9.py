#Ler 20 números e escrever a diferença entre o maior e o menor valor lido
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

if __name__ == '__main__':
    num_array = list()
    num = input("Digite o total de números a serem digitados no vetor:")
    print('Digite os números um a um: ')
    for i in range(int(num)):
        n = input("num{:} :".format(i))
        num_array.append(int(n))
    print('ARRAY: ', num_array)
    maior_num, menor_num, dif = maior_menor_dif(num_array)
    print("Para a matriz {:}, o maior número é: {:}, o menor número é: {:} e a diferença entre eles é: {:}".format(
        num_array, maior_num, menor_num, dif))