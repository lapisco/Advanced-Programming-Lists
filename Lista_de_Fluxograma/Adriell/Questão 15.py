# Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa inicial, em gramas,
# fazer um fluxograma que determine o tempo necessário para que essa massa se torne menor que 0,5 grama. Escreva a
# massa inicial, a massa final e o tempo calculado em segundos.

def calc_massa(massa):
    massa_final = 0.5
    tempo = 0
    while massa > massa_final:
        massa = massa/2
        tempo += 50
    return tempo
if __name__ == '__main__':
    print("Digite a massa do matérial radioativo em gramas :")
    massa = float(input())
    tempo = calc_massa(massa)
    print("Foram nescessários {:} segundos até que a massa de {:} gramas decaisse até um valor menor que 0.5 gramas".format(tempo, massa))