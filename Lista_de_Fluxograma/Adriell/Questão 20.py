# faça um Fluxograma para calcular o valor da série.
# B = (x^25)/1 - (x^24)/2 + (x^23)/3 - (X^22)/4 + ... + x/25
import math
def questao_11(X):
    term = 0
    for i in range(0,25):
        if i%2 == 1:
            term -= (math.pow(X,X-i))/(1+i)
        elif i%2 == 0:
            term += (math.pow(X, X - i)) / (1 + i)
    return term

if __name__ == '__main__':
    print("Digite o valor de X:")
    x = float(input())
    val = questao_11(x)
    print("O resultado da equação B = (x^25)/1 - (x^24)/2 + (x^23)/3 - (X^22)/4 + ... + x/25 para com x = {:}, é: {:}".format(x,val))