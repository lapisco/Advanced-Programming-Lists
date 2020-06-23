# Desenvolva um algoritmo que recebe 6 valores numéricos inteiros numa matriz 2x3 e mostre a soma destes 6
# números.

def montar_mat_nxn(linhas,colunas):
    mat = np.zeros(shape=(linhas,colunas),dtype=int)
    for i in range(linhas):
        for j in range(colunas):
            mat[i,j] = int(input("Diga o valor {:}x{:} da matriz:".format(i,j)))
    return mat

def somar_elements_mats(mat):
    rows,cols = mat.shape[:2]
    num = 0
    for i in range(rows):
        for j in range(cols):
            num += mat[i,j]
    return num

if __name__ == '__main__':
    print("Vamos preencher a matriz nxn")
    linhas = int(input("Diga as dimensões da matriz: {linhas}:"))
    colunas = int(input("Diga as dimensões da matriz: {colunas}:"))
    print("A matriz a ser montada é de dimensões {:}:{:}".format(linhas, colunas))
    mat = montar_mat_nxn(linhas, colunas)
    print("A matriz formada é:")
    print(mat)
    sum = somar_elements_mats(mat)
    print("A soma dos elementos da matriz é:", sum)