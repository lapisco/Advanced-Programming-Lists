# Calcular e imprimir na tela uma matriz de tamanho 10x10, em que seus elementos estão na forma:
# A[i][j] = 2i + 7j – 2 se i < j
# A[i][j] = 3i2 - 1 se i = j
# A[i][j] = 4i3 + 5j2 + 1 se i > j

def montar_mat_condicional(linhas,colunas):
    mat = np.zeros(shape=(linhas,colunas),dtype=int)
    for i in range(linhas):
        for j in range(colunas):
            if i<j:
                mat[i,j] = 2*i + 7*j
            elif i == j:
                mat[i,j] = 3*i*i - 1
            elif i>j:
                mat[i,j] = 4*i*i*i + 5*j*j + 1
    return mat
if __name__ == '__main__':
    print("Vamos preencher a matriz nxn")
    linhas = int(input("Diga as dimensões da matriz: {linhas}:"))
    colunas = int(input("Diga as dimensões da matriz: {colunas}:"))
    print("A matriz a ser montada é de dimensões {:}:{:}".format(linhas, colunas))
    mat = montar_mat_condicional(linhas, colunas)
    print("A matriz formada é:")
    print(mat)