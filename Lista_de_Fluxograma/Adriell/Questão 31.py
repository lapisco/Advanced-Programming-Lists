# Fazer um para calcular a raiz quadrada de um número positivo, usando o roteiro abaixo, baseado no método de
# aproximações sucessivas de Newton:

def raiz_metodo_newton(y):
    num  = y/2
    for i in range(20):
        num=((num * num) + y)/(2 * num)
    return num

if __name__ == '__main__':
    print("Digite o número na qual se deseja saber a sua raiz:")
    y = float(input())
    raiz = raiz_metodo_newton(y)
    print("A raiz do número {:} é {:}".format(y, raiz))