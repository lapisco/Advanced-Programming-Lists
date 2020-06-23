# Faça um programa para ler 10 números diferentes a serem armazenados em um vetor. Os números deverão ser
# armazenados no vetor na ordem em que forem lidos, sendo que, caso o usuário digite um número que já foi digitado
# anteriormente, o programa deverá pedir a ele para digitar outro número. Note que cada valor digitado pelo usuário
# deve ser pesquisado no vetor, verificando se ele existe entre os números que já foram fornecidos. Exiba na tela o
# vetor final que foi digitado.

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
    for i in range(0, num):
        n = input("num {:}:".format(i))
        if len(num_array) == 0:
            num_array.append(int(n))
        else:
            position, val = detect_num_array(int(n), num_array)
            if val == 1:
                print("tente novamente")
                z = cont
                k = 1
                while k != 0:
                    numero = input("num {:}:".format(i))
                    if numero != n:
                        k = 0
                        num_array.append(int(numero))
                    else:
                        print("tente novamente, algarismo igual")

            else:
                num_array.append(int(n))
                cont = cont + 1
    print('ARRAY: ', num_array)