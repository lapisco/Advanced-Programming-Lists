# Supondo que a população da cidade A é de 50.000 habitantes com uma taxa anual de crescimento de 3% e que a
# população de uma cidade B é de 200.000 habitantes com uma taxa de crescimento de 1,5%. Fazer um fluxograma que
# calcule e escreva o número de anos necessários para que a população da cidade A ultrapasse a da cidade B, mantidas
# essas taxas de crescimento

def cidades(A,crescA,B,crescB):
    n =1
    if A>B:
        while B<A:
            A = A+(A*crescA*0.01)
            B = B+(B*crescB*0.01)
            n+=1
        return "A","B",n
    elif B>A:
        while A<B:
            A = A+(A*crescA*0.01)
            B = B+(B*crescB*0.01)
            n+=1
        return "B","A",n

if __name__ == '__main__':
    print("Coloque a população da cidade A(em milhões de habitantes)")
    A = float(input())
    print("coloque a taxa de crescimento da população da cidade A(de 0 a 100 por cento)")
    aux_A = float(input())
    print("Coloque a população da cidade B(em milhões de habitantes)")
    B = float(input())
    print("coloque a taxa de crescimento da população da cidade A(de 0 a 100 por cento)")
    aux_B = float(input())
    cidmaior, cidmenor, anos = cidades(A, aux_A, B, aux_B)
    print(
        "serão nescessários {:} anos para que a população da cidade {:} seja maior que a população da cidade {:}".format(
            anos, cidmenor, cidmaior))