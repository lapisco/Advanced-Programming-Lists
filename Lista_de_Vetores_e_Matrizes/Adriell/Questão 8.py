# Criar um algoritmo que leia os elementos de uma matriz inteira de 3x3 e imprimir outra matriz multiplicando cada
# elemento da primeira matriz por 2.
import numpy as np
def montar_mat_nxn(linhas,colunas):
    mat = np.zeros(shape=(linhas,colunas),dtype=int)
    for i in range(linhas):
        for j in range(colunas):
            mat[i,j] = int(input("Diga o valor {:}x{:} da matriz:".format(i,j)))
    return mat

if __name__ == '__main__':
    print("Vamos preencher a matriz nxn")
    linhas = int(input("Diga as dimensões da matriz: {linhas}:"))
    colunas = int(input("Diga as dimensões da matriz: {colunas}:"))
    print("A matriz a ser montada é de dimensões {:}:{:}".format(linhas, colunas))
    mat = montar_mat_nxn(linhas, colunas)
    print("A matriz formada é:\n\n{:} \n\nx 2 \n= \n\n{:}".format(mat, (2 * mat)))