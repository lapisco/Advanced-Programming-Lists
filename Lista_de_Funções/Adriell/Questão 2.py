# Faça as funções de matemática básica entre dois números: subtração, divisão, multiplicação e soma. Os dois números
# devem ser entrada da função e o resultado deve ser o retorno.
def sub(num1,num2):
    return num1-num2
def multi(num1,num2):
    return num1*num2
def sum(num1,num2):
    return num1+num2
def div(num1,num2):
    return num1/num2
if __name__ == '__main__':
    print("calculadora de questões\ndiga a operação que deseja realizar:"
          "\n1-subtração\n2-divisão\n3-multiplicação\n4-soma")
    val = input()
    if int(val) == 1:
        print("subtração\n digite o primeiro número :")
        x = input()
        print("\n digite o segundo número :")
        y = input()
        val = sub(float(x), float(y))
        print("o resultado da subtração para {:} - {:} = {:}".format(float(x), float(y), val))
    elif int(val) == 2:
        print("divisão\n digite o primeiro número :")
        x = input()
        print("\n digite o segundo número :")
        y = input()
        val = div(float(x), float(y))
        print("o resultado da subtração para {:} / {:} = {:}".format(float(x), float(y), val))
    elif int(val) == 3:
        print("multiplicação\n digite o primeiro número :")
        x = input()
        print("\n digite o segundo número :")
        y = input()
        val = multi(float(x), float(y))
        print("o resultado da subtração para {:} * {:} = {:}".format(float(x), float(y), val))
    elif int(val) == 4:
        print("soma \n digite o primeiro número :")
        x = input()
        print("\n digite o segundo número :")
        y = input()
        val = sum(float(x), float(y))
        print("o resultado da subtração para {:} + {:} = {:}".format(float(x), float(y), val))