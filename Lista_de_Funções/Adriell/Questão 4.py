# Dados três valores A, B e C de uma equação do segundo grau (Ax2
# +Bx+C=0), faça uma função para calcular o valor das
# raízes, se para os valores fornecidos for possível determinar raízes reais. O retorno da função deve ser a quantidade de
# raízes, e as possíveis raízes devem ser colocadas como variável de entrada da função.
import math
def calc_eq(A,B,C):
    delta = ((B*B)-(4*A*C))
    if delta > 0:
        x1 = ((-B)-(math.sqrt((float(delta)))))/(2*A)
        x2 = ((-B)+(math.sqrt(float(delta))))/(2*A)
    else:
        x1 = None
        x2 = None
    return x1,x2

if __name__ == '__main__':
    print("\n Vamos montar a função: Ax² + Bx + C\nDiga o valor de A:")
    A = float(input())
    print("\nDiga o valor de B:")
    B = float(input())
    print("\nDiga o valor de C:")
    C = float(input())
    print("a equação montada é: ({:})x² + ({:})x + ({:})".format(A, B, C))
    raiz1, raiz2 = calc_eq(A, B, C)
    if raiz1 == None and raiz2 == None:
        print("não possui raízes no plano real")
    else:
        print("as raizes da equação são: {:} e {:}".format(raiz1, raiz2))