# As coordenadas de um ponto (X,Y) estão disponíveis em uma unidade
# de entrada. Ler estes valores (até quando um flag ocorrer) e escrever
# "INTERIOR" se o ponto estiver dentro da região hachurada mostrada
# abaixo (y2 < |y| < y1); caso contrário, escrever "EXTERIOR".
def analizar_coordenadas(x,y):
    if (y<=(3*x)) and (y>=(x/3)):
        return 1
    else:
        return 0

if __name__ == '__main__':
    print("Digite a coordenada X:")
    x = int(input())
    print("Digite a coordenada Y:")
    y = int(input())
    val = analizar_coordenadas(x, y)
    if val == 1:
        print(
            "O ponto formado pelas coordenadas X e Y dadas está dentro região INTERIOR formada pelas linhas y=3x e y=x/3")
    elif val == 0:
        print(
            "o ponto formado pelas coordenadas X e Y dadas está dentro da região EXTERIOR formada pelas linhas y=3x e y=x/3")