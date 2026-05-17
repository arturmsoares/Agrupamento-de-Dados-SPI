
# É a soma das diferenças absolutas entre os atributos
# Se a Euclidiana mede a diagonal, a Manhattan mede o deslocamento por eixos, 
# como se você andasse por quarteirões em uma cidade.

def distancia_manhattan(ponto1, ponto2):
    soma = 0
    for i in range(len(ponto1)):
        soma += abs(ponto1[i] - ponto2[i])
    return soma
a = [1, 2]
b = [4, 6]
print("Distância Manhattan:", distancia_manhattan(a, b))