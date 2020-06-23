# Faça um fluxograma para gerar todas as possíveis combinações possíveis quando se é jogado dois dados
import numpy as np
def combinações():
    dado1 = [1,2,3,4,5,6]
    dado2 = [1,2,3,4,5,6]
    total = []
    # total = np.asarray(shape = (36,2),int)
    for i in range(36):
        val1 = np.random.randint(1,6)
        val2 = np.random.randint(1,6)
        if len(total) == 0:
            val = [val1,val2]
            total.append(val)
        if total[0:i] !=(val1,val2):
            val = [val1, val2]
            total.append(val)

    return total

if __name__ == '__main__':
    val = combinações()
    print("As possíveis combinações de lados de dois dados são: ")
    print(val)