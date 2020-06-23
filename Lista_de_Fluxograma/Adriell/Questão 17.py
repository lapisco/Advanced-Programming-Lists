# faça um Fluxograma para calcular o valor da série.
# A = 1 + 3/2 + 5/3 + ...+ 99/50

def serie_A():
    A = 1
    for i in range(1,50):
        A += (2*i + 1)/(1+i)
    return A

if __name__ == '__main__':
    val = serie_A()
    print("O Resultado da série  A = 1 + 3/2 + 5/3 + ...+ 99/50 é :{:} ".format(val))