import math
def distancia_euclidiana(ponto1, ponto2):
    soma = 0
    for i in range(len(ponto1)):
        soma += (ponto1[i] - ponto2[i])**2
    return math.sqrt(soma)

a = [1, 2]
b = [4, 6]

print(distancia_euclidiana(a, b))

# Essa função já funciona para qualquer número de atributos, desde que os vetores tenham o mesmo tamanho.