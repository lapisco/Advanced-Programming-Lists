# As coordenadas de um ponto (X,Y) deve ser a entrada de uma função.
# Deve-se retornar 1 quando este ponto estiver dentro das linhas abaixo, na
# região "INTERIOR" destas. Deve-se retorna 0 caso contrário, quando este
# ponto for exterior à estas linhas.
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