# Preencher um vetor com números inteiros (8unidades); solicitar um número do teclado. Pesquisar se esse número
# existe no vetor. Se existir, imprimir em qual posição do vetor. Se não existir, imprimir MSG que não existe

def detect_num_array(n,array):
    val = 0
    position = None
    for i in range(len(array)):
        num = array[i]
        if int(num) == int(n):
            position = array.index(n)
            print("o número Digitado já se encontra na matriz, está localizado na posição {:}".format(position))
            val = 1
    return position,val

if __name__ == '__main__':
    num_array = list()
    num = int(input("Digite o total de números a serem digitados no vetor:"))
    print('Digite os números um a um: ')
    z = 0
    cont = 0
    err = 1
    for i in range(num):
        n = input("num {:}:".format(i))
        if len(num_array) == 0:
            num_array.append(int(n))
        else:
            position, val = detect_num_array(int(n), num_array)
            if val == 1:
                num_array.append(int(n))
            else:
                num_array.append(int(n))
                print("o algarismo ainda não existe no vetor")