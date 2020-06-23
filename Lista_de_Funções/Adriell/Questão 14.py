# Para cada série abaixo, faça uma função para calcular o valor da série
# e^x = x^0 + (X^1)/1! + (x^2)/2! + (x^3)/3! + ... + (x^20)/20!
import math
def função_e(x):
    num = 0
    for i in range(20):
        n = i
        z = i
        if n == 0 or n == 1:
            z = 1
        else:
            for fact in range(1, i):
                n = n - 1
                z = z * (n)
        num+= (math.pow(x,i))/(z)
    return num

if __name__ == '__main__':
    print("Digite o valor de X:")
    x = float(input())
    val = função_e(x)
    print("O resultado da equação e^{:} = {:}".format(x,val))