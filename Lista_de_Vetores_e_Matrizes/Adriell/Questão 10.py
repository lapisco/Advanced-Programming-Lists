# . Criar um algoritmo que leia os elementos de uma matriz inteira de 4 x 4 e imprimir os elementos da diagonal
# principal
import numpy as np
def montar_mat_nxn(linhas,colunas):
    mat = np.zeros(shape=(linhas,colunas),dtype=int)
    for i in range(linhas):
        for j in range(colunas):
            mat[i,j] = int(input("Diga o valor {:}x{:} da matriz:".format(i,j)))
    return mat

def diagonal_principal(mat):
    rows,cols = mat.shape[:2]
    for i in range(rows):
        for j in range(cols):
            if i!=j:
                mat[i,j]=0
    return mat

if __name__ == '__main__':
    print("Vamos preencher a matriz nxn")
    linhas = int(input("Diga as dimensões da matriz: {linhas}:"))
    colunas = int(input("Diga as dimensões da matriz: {colunas}:"))
    print("A matriz a ser montada é de dimensões {:}:{:}".format(linhas, colunas))
    mat = montar_mat_nxn(linhas, colunas)
    print("A matriz formada é:")
    print(mat)
    diagonal = diagonal_principal(mat)
    print("A diagonal principal formada é:")
    print(diagonal)