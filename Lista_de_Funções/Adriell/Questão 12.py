# Para cada série abaixo, faça uma função para calcular o valor da série
# S = 100/0! + 99/1! + 98/2! + 97/3! + ... + 1/99!

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
        num+=(100-i)/(z)
    return num

if __name__ == '__main__':
    val = serie_S()
    print("O resultado da função  S = 100/0! + 99/1! + 98/2! + 97/3! + ... + 1/99! é {:}".format(val))