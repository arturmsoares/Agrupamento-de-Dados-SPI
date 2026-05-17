# Questão 8 — Uma iteração do K-Means  
# Considerando os pontos abaixo, temos que inicialmente, o K-Means usa:
# Centroide 1 = A = (0, 0) Centroide 2 = C = (8, 0)
# Use distância Euclidiana. Em caso de empate, associe o ponto ao centroide de menor índice.

# Após a primeira etapa de associação e o recálculo dos centroides, quais serão os novos centroides?

 
# *
# 4 pontos
# Imagem sem legenda
# A) Centroide 1 = (1,33; 4,00) e Centroide 2 = (8,00; 1,00)
# B) Centroide 1 = (0,00; 1,00) e Centroide 2 = (6,67; 4,00)
# C) Centroide 1 = (4,00; 10,00) e Centroide 2 = (8,00; 1,00)
# D) Centroide 1 = (0,00; 0,00) e Centroide 2 = (8,00; 0,00)

import numpy as np

# Pontos
X = np.array([
    [0, 0],   # A
    [0, 2],   # B
    [8, 0],   # C
    [8, 2],   # D
    [4, 10]   # E
])

# Centroides iniciais
C1 = np.array([0, 0])
C2 = np.array([8, 0])

cluster1 = []
cluster2 = []

for p in X:
    d1 = np.linalg.norm(p - C1)
    d2 = np.linalg.norm(p - C2)
    
    if d1 <= d2:  # desempate vai para C1
        cluster1.append(p)
    else:
        cluster2.append(p)

# Recalcular centroides
C1_new = np.mean(cluster1, axis=0)
C2_new = np.mean(cluster2, axis=0)

print("Novo C1:", C1_new)
print("Novo C2:", C2_new)