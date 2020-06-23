# Passe quatro números como parâmetro de entrada de uma função, retorne a diferença entre o maior e o menor valor lido

def sub_max_min(num1,num2,num3,num4):
    refmax = num1
    refmin = num1
    # if num1 >refmax:
    #     refmax = num1
    if num2 >refmax:
        refmax = num2
    if num3 >refmax:
        refmax = num3
    if num4 >refmax:
        refmax = num4
    if num2 <refmin:
        refmin = num2
    if num3 <refmin:
        refmin = num3
    if num4 <refmin:
        refmin = num4
    return refmax,refmin,refmax-refmin

if __name__ == '__main__':
    print("Digite os 4 algarismos para a comparação:")
    print("Algarismo 1")
    num1 = float(input())
    print("Algarismo 2")
    num2 = float(input())
    print("Algarismo 3")
    num3 = float(input())
    print("Algarismo 4")
    num4 = float(input())
    maxval, minval, result = sub_max_min(num1, num2, num3, num4)
    print("o maior valor dos 4 algarismos é: {:}, já o menor valor dos 4 algarismos é: {:}, e por fim "
          "a diferença entre eles é de {:}".format(maxval, minval, result))