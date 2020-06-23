# Faça um fluxograma para ler um número e escrever todos os seus divisores.

def resto(x,y):
    return x%y
def buscar_divisores(x):
    divisores = list()
    for i in range(1,x+1):
        rest = resto(x,i)
        if rest == 0:
            divisores.append(i)
    return divisores

if __name__ == '__main__':
    print("Digite o número cujo interesse é descobrir seus divisores:")
    num = int(input("número:"))
    divisores = list()
    divisores = buscar_divisores(num)
    print("Os divisores do número {:} são: {:}".format(num,divisores))