# Ler um número, calcular o dobro e retornar seu valor
def dobro(num):
    return 2*num


if __name__ == '__main__':
    print('digite o número\n')
    num = input()
    print('o número digitado foi {:}, já seu dobro é {:}:'.format(num, dobro(int(num))))