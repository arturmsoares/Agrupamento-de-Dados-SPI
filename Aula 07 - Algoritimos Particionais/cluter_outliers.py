import numpy as np
import pandas as pd
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score

# 1. Gerar três grupos bem definidos
X, y = make_blobs(
    n_samples=60,
    centers=[(-5, -5), (0, 5), (5, -4)],
    cluster_std=0.8,
    random_state=42
)

# 2. Criar outliers manualmente
outliers = np.array([
    [10, 10],
    [12, -8],
    [-10, 8],
    [0, -12],
    [15, 3]
])

# 3. Juntar dados normais e outliers
X_com_outliers = np.vstack([X, outliers])

# 4. Criar rótulo apenas para fins didáticos
rotulos_reais = np.concatenate([
    y,
    [-1, -1, -1, -1, -1]   # -1 representa outlier
])

# 5. Montar DataFrame
df = pd.DataFrame(X_com_outliers, columns=["x", "y"])
df["rotulo_original"] = rotulos_reais
df["tipo"] = df["rotulo_original"].apply(lambda v: "outlier" if v == -1 else "normal")

df.head()

# * Código para salvar CSV

df.to_csv("dataset_blobs_com_outliers.csv", index=False)


# * Visualização Inicial


plt.figure(figsize=(8, 6))

normais = df[df["tipo"] == "normal"]
outliers_df = df[df["tipo"] == "outlier"]

plt.scatter(normais["x"], normais["y"], label="Pontos normais")
plt.scatter(outliers_df["x"], outliers_df["y"], marker="x", s=120, label="Outliers")

plt.title("Dataset sintético com 3 grupos e outliers")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()


from sklearn.cluster import KMeans

# Cenário 01: apenas os normais
# filtrando para ter apenas os 'normais'
# selecionadas apenas as colunas 'x' e 'y' para o treinamento
df_sem_outliers = df[df["tipo"] == "normal"][["x", "y"]]

# instanciando o K-Means
# random_state=42 para que os resultados sejam reproduzíveis
kmeans_limpo = KMeans(n_clusters=3, random_state=42, n_init=10)

# treinamento
kmeans_limpo.fit(df_sem_outliers)

# coleta de dados
sse_limpo = kmeans_limpo.inertia_
centroides_limpos = kmeans_limpo.cluster_centers_
labels_limpo = kmeans_limpo.labels_
sil_limpo = silhouette_score(df_sem_outliers, labels_limpo)

print(f"SSE (Inertia) sem outliers: {sse_limpo:.2f}")
print("Centroides encontrados:\n", centroides_limpos)
print(f"Silhouette Score (Sem Outliers): {sil_limpo:.4f}")


# Cenário 02: todos os dados (normais + outliers)
X_total = df[["x", "y"]]

# instanciado e treinando
kmeans_com_outliers = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_com_outliers.fit(X_total)

# coleta
sse_com_outliers = kmeans_com_outliers.inertia_
centroides_com_outliers = kmeans_com_outliers.cluster_centers_
labels_com_outliers = kmeans_com_outliers.labels_
sil_com_outliers = silhouette_score(X_total, labels_com_outliers)

print(f"SSE (Inertia) COM outliers: {sse_com_outliers:.2f}")
print("Novos Centróides:\n", centroides_com_outliers)
print(f"Silhouette Score (Com Outliers): {sil_com_outliers:.4f}")


# Criando a figura com dois gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# GRÁFICO 1: Cenário sem Outliers
ax1.scatter(df_sem_outliers["x"], df_sem_outliers["y"], c='dodgerblue', alpha=0.6, label="Pontos Normais")
ax1.scatter(centroides_limpos[:, 0], centroides_limpos[:, 1], marker='X', s=200, c='red', edgecolors='black', label="Centróides")
ax1.set_title(f"Cenário 1: Sem Outliers (SSE: {sse_limpo:.2f})")
ax1.legend()
ax1.grid(True)

# GRÁFICO 2: Cenário COM Outliers
# pontos normais
ax2.scatter(normais["x"], normais["y"], c='dodgerblue', alpha=0.6, label="Pontos Normais")
# outliers com um marcador
ax2.scatter(outliers_df["x"], outliers_df["y"], marker='o', c='orange', s=80, label="Outliers")
# novos centróides
ax2.scatter(centroides_com_outliers[:, 0], centroides_com_outliers[:, 1], marker='X', s=200, c='red', edgecolors='black', label="Centróides Puxados")

ax2.set_title(f"Cenário 2: Com Outliers (SSE: {sse_com_outliers:.2f})")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()
