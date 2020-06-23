# faça um Fluxograma para calcular o valor da série.
# M = (37*38)/1 + (36*37)/2 + (35*36)/3 + ... + (1*2)/37

def série_M():
    M = 0
    for i in range(36):
        M += ((38-i-1)*(38-i))/(i+1)
    return M

if __name__ == '__main__':
    val = série_M()
    print("O Resultado da série  M = (37*38)/1 + (36*37)/2 + (35*36)/3 + ... + (1*2)/37 é :{:} ".format(val))