# Para cada série abaixo, faça uma função para calcular o valor da série
# COSENO = 1 - (x^2)/2! + (x^4)/4! - (x^6)/6! + ... + (x^20)/20!
import math
def função_COSENO(x):
    num = 0
    for i in range(20):
        n = 2*i
        z = 2*i
        if n == 0 or n == 1:
            z = 1
        else:
            for fact in range(1, i):
                n = n - 1
                z = z * (n)
        if i%2 == 1:
            num-= (math.pow(x,2*i))/(z)
        elif i%2 == 0:
            num += (math.pow(x, 2 * i)) / (z)
    return num

if __name__ == '__main__':
    print("Digite o valor de X:")
    x = float(input())
    val = função_COSENO(x)
    print("O resultado da equação COSENO = {:}rad = {:}".format(x,val))