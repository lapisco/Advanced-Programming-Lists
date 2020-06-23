#6. Fazer uma função para ler três notas (sistema do IFCE), Calcular a média (ponderada), dizer se foi aprovado por média
# (7,0). Deve-se retornar desta função valor 1 se for aprovado e 0 se for reprovado.

# 7. Faça uma função que calcule quanto o aluno precisaria tirar na final quando a função da questão 5 retornar 0

def media_ponderada_condicional(nota1,peso1,nota2,peso2,nota3,peso3):
    mediaponderada = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1 + peso2 + peso3)
    if mediaponderada >= 7:
        return 1,mediaponderada
    else:
        return 0,mediaponderada
def complemento(nota):
    return 10-nota

if __name__ == '__main__':
    print("Digite as notas e seus respectivos pesos:\nNota 1:")
    nota1 = float(input())
    print("Peso 1:")
    peso1 = float(input())
    print("Nota 2:")
    nota2 = float(input())
    print("Peso 2:")
    peso2 = float(input())
    print("Nota 3")
    nota3 = float(input())
    print("Peso 3:")
    peso3 = float(input())
    resultado, nota = media_ponderada_condicional(nota1, peso1, nota2, peso2, nota3, peso3)
    if resultado == 1:
        print("Com as notas e pesos dados, o aluno foi aprovado, com média final {:}".format(nota))
    else:
        print("Com as notas e pesos dados, o aluno foi reprovado, com média final {:}".format(nota))
        recuperacao = complemento(nota)  # questão 7
        print("será nescessário tirar {:} na média final para passar".format(recuperacao))