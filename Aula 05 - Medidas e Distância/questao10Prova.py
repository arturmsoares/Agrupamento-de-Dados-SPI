# Questão 10 — Dissertativa: interpretação de resultados de agrupamento.  
# Um aluno aplicou K-Means em uma base de escolas após normalização dos atributos numero_alunos, gasto_por_aluno, percentual_execucao, taxa_aprovacao e nota_IDEB.

# Ele testou os valores de K presente na tabela abaixo. Ao observar os clusters para K = 3, encontrou:

# Cluster 1: escolas grandes, execução média, IDEB intermediário; 
# Cluster 2: escolas pequenas, alto gasto por aluno, IDEB variável; 
# Cluster 3: apenas uma escola, com gasto por aluno muito alto e taxa de aprovação muito baixa.
# Com base nesses resultados, responda:

# K = 3 parece uma escolha defensável? Justifique. 
# O Cluster 3 deve ser automaticamente aceito como um grupo real? Justifique. 
# Que análises complementares você faria antes de apresentar o resultado à gestão municipal?

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Exemplo de base (substitua pelos seus dados reais)
df = pd.DataFrame({
    'numero_alunos': [200, 500, 150, 800, 1200, 90],
    'gasto_por_aluno': [3000, 2000, 5000, 1800, 1500, 10000],
    'percentual_execucao': [0.8, 0.6, 0.9, 0.7, 0.65, 0.5],
    'taxa_aprovacao': [0.9, 0.85, 0.88, 0.8, 0.78, 0.4],
    'nota_IDEB': [6.0, 5.5, 6.5, 5.8, 5.2, 3.0]
})

# 🔹 1. Normalização
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

# 🔹 2. Testando diferentes valores de K
inercia = []
silhouette = []

K_range = range(2, 6)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    
    inercia.append(kmeans.inertia_)
    silhouette.append(silhouette_score(X_scaled, labels))

# 🔹 3. Modelo com K = 3
kmeans_final = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans_final.fit_predict(X_scaled)

# 🔹 4. Análise dos clusters
resumo = df.groupby('cluster').mean()
print(resumo)

# 🔹 5. Ver tamanho dos clusters
print(df['cluster'].value_counts())


# 3 é uma boa escolha a princípio, pois o silhouette médio é maior entre os demais (quanto maior, melhor), indicando uma melhor separação entre os clusters. Somado à isso, há uma redução relevante no SSE, o que indica pontos mais agrupados, próximos ao centro de seu cluster.

# Contudo, a existência de um cluster com apenas uma escola indica possível presença de outlier. Sendo assim, esse cluster não deve ser automaticamente interpretado como um grupo real, podendo representar um caso atípico e não um padrão.

# Desse modo, deve-se investigar a escola que compõe o cluster, além de gerar testes sem esse ponto ou mesmo com outros valores de k, além de visualizações para  verificar a separação entre os grupos. Outra possibilidade é  verificar se o silhouette de cada cluster individualmente é alto. Às vezes, a média é boa, mas um cluster específico está muito "fraco".