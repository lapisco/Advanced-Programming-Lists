#Escrever os quadrados dos números entre 1000 e 2000.
def quadrados(num):
    return (num*num)

if __name__ == '__main__':
    for i in range(1000,2001):
        quadrado = quadrados(i)
        print("O quadrado do número {:} é : {:}".format(i,quadrado))