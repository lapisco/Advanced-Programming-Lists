# Escrever um fluxograma para ler um número e dizer se ele é primo ou não

def detect_primo(n):
    val = n
    cont=0
    for i in range(1,n+1):
        if n%i == 0:
            cont=cont+1
    if cont == 2:
        return 1
    else:
        return 0

if __name__ == '__main__':
    print("Digite o número com a finalidade de se saber se esse é primo ou não:")
    n = int(input())
    val = detect_primo(n)
    if val == 1:
        print("O número {:} é primo".format(n))
    elif val == 0:
        print("O número {:} não é primo".format(n))