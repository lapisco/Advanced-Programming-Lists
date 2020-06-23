# Resolva as questões de 12 a 15, utilizando dentro do cálculo a função de fatorial feita questão 9
import math
def factorial(num):
    val = num
    # numfact = num
    if num == 0 or num == 1:
        return 1
    else:
        for i in range(1,num):
            val = val-1
            num=num*(val)
        return num
def serie_S():
    num=0
    for i in range(99):
        n = i
        z = i
        if n==0 or n==1:
            z=1
        else:
            for fact in range(1,i):
                n = n - 1
                z = z * (n)
        num+=(100-i)/(factorial(i))
    return num
def série_C(x):
    num = 0
    for i in range(13):
        n = 2*i+1
        # z = 2*i+1
        if n == 0 or n == 1:
            z = 1
        else:
            for fact in range(1, i):
                n = n - 1
                z = z * (n)
        if i%2 == 1:
            num -= (math.pow(x,2*i+1))/(factorial(2*i+1))
        if i%2 == 0:
            num+=(math.pow(x,2*i+1))/(factorial(2*i+1))
    return num
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
        num+= (math.pow(x,i))/(factorial(i))
    return num
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
            num-= (math.pow(x,2*i))/(factorial(2*i))
        elif i%2 == 0:
            num += (math.pow(x, 2 * i)) / (factorial(2*i))
    return num

if __name__ == '__main__':
    val = serie_S()
    print("O resultado da função  S = 100/0! + 99/1! + 98/2! + 97/3! + ... + 1/99! é {:}".format(val))
    print("Digite o valor de X:")
    x = float(input())
    val = série_C(x)
    print(
        "O resultado da equação C = X - (X^3)/3! + (X^5)/5! - (X^7)/7! + ... + (X^13)/13! para com x = {:}, é: {:}".format(
            x, val))
    print("Digite o valor de X:")
    x = float(input())
    val = função_e(x)
    print("O resultado da equação e^{:} = {:}".format(x, val))
    print("Digite o valor de X:")
    x = float(input())
    val = função_COSENO(x)
    print("O resultado da equação COSENO = {:}rad = {:}".format(x, val))
