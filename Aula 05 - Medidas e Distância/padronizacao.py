import numpy as np
idades = np.array([18, 24, 30, 42, 60]) 
media = np.mean(idades)
desvio = np.std(idades)
idades_padronizadas = (idades - media) / desvio
print("Média:", media)
print("Desvio padrão:", desvio)
print("Idades padronizadas:", idades_padronizadas)