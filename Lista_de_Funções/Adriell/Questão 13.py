# Para cada série abaixo, faça uma função para calcular o valor da série
# C = X - (X^3)/3! + (X^5)/5! - (X^7)/7! + ... + (X^13)/13!
import math
def série_C(x):
    num = 0
    for i in range(13):
        n = 2*i+1
        z = 2*i+1
        if n == 0 or n == 1:
            z = 1
        else:
            for fact in range(1, i):
                n = n - 1
                z = z * (n)
        if i%2 == 1:
            num -= (math.pow(x,2*i+1))/(z)
        if i%2 == 0:
            num+=(math.pow(x,2*i+1))/(z)
    return num

if __name__ == '__main__':
    print("Digite o valor de X:")
    x = float(input())
    val = série_C(x)
    print("O resultado da equação C = X - (X^3)/3! + (X^5)/5! - (X^7)/7! + ... + (X^13)/13! para com x = {:}, é: {:}".format(x,val))