def distancia_minkowski(ponto1, ponto2, r=2):
    soma = 0
    for i in range(len(ponto1)):
        soma += abs(ponto1[i] - ponto2[i]) ** r
    return soma ** (1 / r)
    
a = [1, 2]
b = [4, 6]

print("Minkowski r=1:", distancia_minkowski(a, b, r=1))
print("Minkowski r=2:", distancia_minkowski(a, b, r=2))
print("Minkowski r=3:", distancia_minkowski(a, b, r=3))