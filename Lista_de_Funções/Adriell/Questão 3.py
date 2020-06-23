# Ler duas notas, passar estas como entrada de uma função que calcule a média e retornar 1 se for aprovado e zero se for
# reprovado, a média para aprovação é de no mínimo 5,0

def media_condicional(num1,num2):
    media = (num1+num2)/2
    if media >= 5 :
        return 1
    else:
        return 2

if __name__ == '__main__':
    print("diga as notas a serem cálculadas no sistema :")
    print("nota 1 :")
    nota1 = float(input())
    print("nota 2 :")
    nota2 = float(input())
    val = media_condicional(nota1, nota2)
    if val == 1:
        print("val = 1 :situação: Aprovado!")
    else:
        print("val = 0 :situação: reprovado!")