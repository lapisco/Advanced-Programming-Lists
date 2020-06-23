#Ler um número e cálcular o dobro
def dobro(num):
    return num*2

if __name__ == '__main__':
    print('digite o número\n')
    num = input()
    print('o número digitado foi {:}, já seu dobro é {:}:'.format(num, dobro(int(num))))