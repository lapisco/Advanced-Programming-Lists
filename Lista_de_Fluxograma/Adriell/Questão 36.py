# Fazer um fluxograma para gerar a série de Fibonacci com 20 elementos. A série de Fibonacci é formada pela seqüência
# 1, 1, 2, 3, 5, 8, 13, 21, ... . onde um termo é a soma dos dois anteriores.

def func_Fibonacci(n):
    fun = list()
    var = 1
    aux = 0
    for i in range(int(n/2)):
        aux =var+aux
        fun.append(var)
        var = var + aux
        fun.append(aux)
    return fun

if __name__ == '__main__':
    n = int(input("Digite o número de elemento desejados para a sequência de fibonacci: "))
    val = func_Fibonacci(n)
    print("Os {:} primeiros elementos da série de Fibonacci são: \n{:}".format(n,val))