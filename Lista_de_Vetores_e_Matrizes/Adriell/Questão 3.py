# Preencher um vetor com 10 números. Retorne quais são os números ímpares deste vetor.

def impares(array):
    impares = list()
    for i in range(len(array)):
        if array[i]%2 != 0:
            impares.append(array[i])
    return impares

if __name__ == '__main__':
    num_array = list()
    num = input("Digite o total de números a serem digitados no vetor:")
    print('Digite os números um a um: ')
    for i in range(int(num)):
        n = input("num{:} :".format(i))
        num_array.append(int(n))
    print('ARRAY: ', num_array)
    array_impares = impares(num_array)
    print("Para a matriz {:}, os números impares são: {:}".format(num_array, array_impares))
