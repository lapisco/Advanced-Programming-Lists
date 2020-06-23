# Preencher um vetor com 10 números. Retorne quais são os números primos deste vetor

def primos(array):
    primos = list()
    for i in range(len(array)):
        cont=0
        val = array[i]
        for k in range(1,array[i]+1):
            if val%k == 0:
                cont=cont+1
        if cont == 2:
            primos.append(array[i])
    return primos

if __name__ == '__main__':
    num_array = list()
    num = input("Digite o total de números a serem digitados no vetor:")
    print('Digite os números um a um: ')
    for i in range(int(num)):
        n = input("num{:} :".format(i))
        num_array.append(int(n))
    print('ARRAY: ', num_array)
    array_primos = primos(num_array)
    print("Para a matriz {:}, os números primos são: {:}".format(num_array, array_primos))