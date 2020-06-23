# . Leia uma matriz de tamanho 10x3 com as notas de 10 alunos em três provas. Em seguida, calcule e escreva na tela o
# número de alunos cuja pior nota foi na prova 1, o número de alunos cuja a pior nota foi na prova 2 e o número de
# alunos cuja pior nota foi na prova 3.
import numpy as np
def montar_mat_nxn_alunos(linhas,colunas):
    mat = np.zeros(shape=(linhas,colunas),dtype=int)
    for i in range(linhas):
        for j in range(colunas):
            mat[i,j] = int(input("Diga a nota {:} do aluno {:}:".format(j+1, i+1)))
    return mat

def piores_notas(mat):
    rows, cols = mat.shape[:2]
    pior1 = list()
    pior2 = list()
    pior3 = list()
    for i in range(rows):
        if (mat[i,0]<mat[i,1]) and (mat[i,0]<mat[i,2]):
            num = int(i+1)
            pior1.append(num)
        elif (mat[i,1]<mat[i,0]) and (mat[i,1]<mat[i,2]):
            num = int(i + 1)
            pior2.append(num)
        elif (mat[i,2]<mat[i,0]) and (mat[i,2]<mat[i,1]):
            num = int(i + 1)
            pior3.append(num)
    return pior1,pior2,pior3

if __name__ == '__main__':
    print("Vamos preencher a matriz 10x3 de notas dos alunos")
    linhas = 10
    colunas = 3
    # print("Diga a nota {:} do aluno{:}:".format(colunas, linhas))
    mat = montar_mat_nxn_alunos(linhas, colunas)
    print("A matriz de notas formadas é:")
    print(mat)
    pior1, pior2, pior3 = piores_notas(mat)
    print(
        "Os alunos {:} tiveram sua pior nota na prova 1\nOs alunos {:} tiveram sua pior nota na prova 2\nOs alunos {:} tiveram sua pior nota na prova 3".format(
            pior1, pior2, pior3))