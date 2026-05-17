# Questão 5 — Interpretação de código com padronização.
# Analise o código código abaixo e, considerando os objetos A = [10, 1000]; B = [20, 1000] e C = [30, 5000], após a padronização, qual interpretação é mais adequada?
# *
# 4 pontos
# Imagem sem legenda
# A) A e C serão os mais próximos, pois possuem maior diferença compensada pela padronização.
# B) A e B serão os mais próximos, pois diferem apenas no primeiro atributo e possuem o mesmo valor no segundo atributo.
# C) B e C serão os mais próximos, pois B está no centro da distribuição.
# D) Todos terão a mesma distância entre si, pois a padronização transforma todos os atributos para média zero e desvio padrão um.


import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances

X = np.array([
    [10, 1000],
    [20, 1000],
    [30, 5000]
])

scaler = StandardScaler()
X_pad = scaler.fit_transform(X)

D = euclidean_distances(X_pad)

print(np.round(D, 3))


