# Fazer uma função que calcule o valor de N! (Fatorial de N), sendo que o valor inteiro de N é passado como entrada da
# função. O programa deverá retornar um valor que identifique que aconteceu um erro quando entrar um valor negativo e
# tratar adequadamente para 0! e 1!.

def factorial(num):
    val = num
    # numfact = num
    if num == 0 or num == 1:
        return 1
    else:
        for i in range(1,num):
            val = val-1
            num=num*(val)
        return num

if __name__ == '__main__':
    print("Digite o número, a fim de se cálcular o seu fatorial")
    num = int(input())
    fact = factorial(num)
    print("{:}! = {:}".format(num, fact))