# . Fazer um fluxograma que calcule e escreva o número de grãos de milho que se pode colocar num tabuleiro de xadrez,
# colocando 1 no primeiro quadro e nos quadros seguintes o dobro do quadro anterior.

def grãos_nos_quadrados():
    grãos_totais = 0
    aux = 1
    for i in range(64):
        grãos_totais += aux
        aux = 2*aux
    return grãos_totais

if __name__ == '__main__':
    grãos = grãos_nos_quadrados()
    print("Em um tabuleiro de xadrez, em seus 64 quadrados, adicionando 1 grão no primeiro quadrado"
          "e nos quadrados consecutivos o dobro a cada quadrado, foram possíveis adicionar o total de {:} grãos ".format(grãos))