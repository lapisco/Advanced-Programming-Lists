# faça um Fluxograma para calcular o valor da série.
# π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ... + 4/29
def série_π():
    π = 0
    for i in range(15):
        if i%2 == 0:
            divisor = 2*i+1
            π = π + (4)/(divisor)
        elif i%2 == 1:
            divisor = 2 * i + 1
            π = π - (4)/(divisor)

    return π

if __name__ == '__main__':
    val = série_π()
    print("O Resultado da série  π = 4 - 4/3 + 4/5 - 4/7 + 4/9 - ... + 4/29 é :{:} ".format(val))