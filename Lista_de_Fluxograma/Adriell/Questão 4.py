# Fazer um fluxograma para ler três números, estes números podem ser o comprimento dos lados de um triângulo. Dizer
# se estes números podem ser de um triângulo, caso positivo, classificar em eqüilátero, isóscele ou escaleno.

def triângulo(A,B,C):
    if (int(B - C) < A and A < B + C) and (int(A - C) < B and B < A + C) and (int(A - B) < C and C < A + B):
        if A == B and A == C and B == C:
            return 3
        elif (A == B and A != C) or (A == C and A != B) or (B == C and B != A) or (B == A and B != C )or (C == B and C != A) or (C == A and C != B):
            return 1
        else:
            return 2
    else:
        return 0

if __name__ == '__main__':
    print("diga os lados do triângulo:\nLado A:")
    A = float(input())
    print("lado B:")
    B = float(input())
    print("lado C")
    C = float(input())
    triângulo = triângulo(A, B, C)
    if triângulo == 0:
        print("Os valores dados não forman um triângulo")
    elif triângulo == 1:
        print("Os valores dados forman um triângulo isóceles")
    elif triângulo == 2:
        print("Os valores dados forman um triângulo escaleno")
    elif triângulo == 3:
        print("Os valores dados forman um triângulo equilátero")