# Ler 10 números e escrever o maior valor lido.
def maiornum(array):
    maior = array[1]
    for i in range(len(array)):
        if array[i]>maior:
            maior = array[i]
    return maior

if __name__ == '__main__':
    num_array = list()
    num = input("Digite o total de números a serem digitados no vetor:")
    print('Digite os números um a um: ')
    for i in range(int(num)):
        n = input("num{:} :".format(i))
        num_array.append(int(n))
    print('ARRAY: ', num_array)
    maior_num = maiornum(num_array)
    print("Para a matriz {:}, o maior número é: {:}".format(num_array, maior_num))