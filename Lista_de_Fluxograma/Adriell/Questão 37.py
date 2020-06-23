# Fazer um fluxograma para ler um número e escrever o somatório dos seus dígitos. Ex.: 217 → 2+1+7 = 9
def som_digit(n):
    vet_string = []
    som = "+"
    var=""
    tot = 0
    string = str(n)
    vet_string = list(string)
    # int_list = int(vet_string)
    for i in range(len(vet_string)):
        var = var+vet_string[i] + som# sum strings
        tot +=int(vet_string[i])
    var = var[:-1]# remove the las character
    return tot,var

if __name__ == '__main__':
    print("Digite o número com a finalidade de obter a soma de seus dígitos:")
    n = int(input())
    val, somados = som_digit(n)
    print("A soma dos dígitos do algarismo {:} é {:} = {:}".format(n, somados, val))
