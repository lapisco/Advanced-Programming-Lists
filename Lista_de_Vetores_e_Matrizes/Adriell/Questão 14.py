# Faça um programa que permita ao usuário entrar com um matriz de tamanho 3x3 de números inteiros. Em seguida,
# calcule um vetor contendo três posições, em que cada posição deverá armazenar a soma dos números de cada coluna
# da matriz. Exiba na tela esse array.

def montar_mat_nxn(linhas,colunas):
    mat = np.zeros(shape=(linhas,colunas),dtype=int)
    for i in range(linhas):
        for j in range(colunas):
            mat[i,j] = int(input("Diga o valor {:}x{:} da matriz:".format(i,j)))
    return mat

def soma_linhas(mat):
    rows,cols = mat.shape[:2]
    vet_sum = list()
    for j in range(cols):
        vet_sum.append(np.sum(mat[:,j]))
    return vet_sum

if __name__ == '__main__':
    print("Vamos preencher a matriz nxn")
    linhas = int(input("Diga as dimensões da matriz: {linhas}:"))
    colunas = int(input("Diga as dimensões da matriz: {colunas}:"))
    print("A matriz a ser montada é de dimensões {:}:{:}".format(linhas, colunas))
    mat = montar_mat_nxn(linhas, colunas)
    print("A matriz formada é:")
    print(mat)
    vet_soma = soma_linhas(mat)
    print("O vetor formado pela soma de todas as linhas de cada coluna é:")
    print(vet_soma)