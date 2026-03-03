
# Dataset bruto (lista de dicionários)
dados_pesquisa = [
    {'id_cliente': 1, 'idade': 35, 'genero': 'Feminino', 'escolaridade':
    'Superior', 'renda_mensal': 5200.0, 'avaliacao': 4, 'cidade': 'Uberlândia'},
    {'id_cliente': 2, 'idade': -42, 'genero': 'Masculino', 'escolaridade':
    'Médio', 'renda_mensal': 4800.0, 'avaliacao': 5, 'cidade': 'Uberlândia'}, #idade inválida (ruído)
    {'id_cliente': 3, 'idade': '28','genero': 'Feminino', 'escolaridade':
    None, 'renda_mensal': None, 'avaliacao': None, 'cidade': 'Ituiutaba'}, #ausentes
    {'id_cliente': 4, 'idade': 55, 'genero': 'Masculino', 'escolaridade':
    'Superior', 'renda_mensal': 12000.0, 'avaliacao': 3, 'cidade': 'Patos de Minas'},
    {'id_cliente': 5, 'idade': 150, 'genero': 'Feminino', 'escolaridade':
    'Mestrado', 'renda_mensal': 999999.0, 'avaliacao': 5, 'cidade': 'Uberaba'}, #idade e renda outlier
    {'id_cliente': 6, 'idade': 45, 'genero': 'Não-binário','escolaridade':
    'Superior', 'renda_mensal': 6500.0, 'avaliacao': 4, 'cidade': 'Uberlândia'},
    {'id_cliente': 7, 'idade': 33, 'genero': 'Masculino', 'escolaridade':
    'Fundamental','renda_mensal': 2100.0, 'avaliacao': None, 'cidade': 'Araguari'}, #avaliação ausente
    {'id_cliente': 8, 'idade': 68, 'genero': 'Feminino', 'escolaridade':
    'Médio', 'renda_mensal': 3200.0, 'avaliacao': 2, 'cidade': 'Uberlândia'},
    {'id_cliente': 9, 'idade': 22, 'genero': 'Feminino', 'escolaridade':
    'Superior', 'renda_mensal': -100.0, 'avaliacao': 4, 'cidade': 'Uberlândia'}, #renda inválida
    {'id_cliente':10, 'idade': None,'genero': 'Masculino', 'escolaridade':
    'Médio', 'renda_mensal': 4100.0, 'avaliacao': 3, 'cidade': 'Ituiutaba'}, # idade ausente
    {'id_cliente':11, 'idade': 41, 'genero': 'Masculino', 'escolaridade': 'Doutorado',
    'renda_mensal': 18000.0, 'avaliacao': 5, 'cidade': 'Uberlândia'},
    {'id_cliente':12, 'idade': 29, 'genero': 'Feminino', 'escolaridade':
    'Superior', 'renda_mensal': 5600.0, 'avaliacao': 4, 'cidade': 'Uberaba'},
]

### 1) Inspeção e diagnóstico

## 1. Imprima os registros.

for registro in dados_pesquisa:
    print(registro)

## 2. liste **pelo menos 5 problemas** encontrados e classifique como: ruído, outlier, ausente, tipo incorreto.

# ruído - idade inválida -42 na linha 6
# outlier - idade e renda na linha 12 e 13
# ausente - idade na linha 23
# tipo incorreto - idade como string '28' na linha 8

## 3. Classifique os atributos (nominal/ordinal/numérico) e diga **qual seria o impacto** de representar errado em uma análise de dados.

# id_cliente nominal, pois tentar somar ou tirar média gera valores sem sentido
# idade: numérico, para realizar calculos de média e mediana, o que não seria possível se tratada como string
# genero: nominal, pois representar como numero pode tornar a interpretação sem sentido
# escolaridade: ordinal, pois é possível fazer correlação com renda, por exemplo. Se tratada como nominal, perde-se a hierarquia
# renda_mensal: numerico. O erro diante desse tipo impede calculos para identificar padrão econômico
# avaliacao: ordinal, para classificar corretamente observando a hierarquia de avaliações
# cidade: nominal, pois tentar somar ou tirar média gera valores sem sentido


### 2) Funções de conversão e validação (obrigatório)

def to_int_safe(x):
    """Tenta converter x para inteiro. Retorna None se falhar"""
    try:
        if x is None:
            return None
        return int(x)
    except (ValueError, TypeError):
        return None

def to_float_safe(x):
    """Tenta converter x para float. Retorna None se falhar"""
    try:
        if x is None:
            return None
        return float(x)
    except (ValueError, TypeError):
        return None


def registro_valido(registro):
    idade = to_int_safe(registro.get('idade'))
    renda = to_float_safe(registro.get('renda_mensal'))
        
    if (idade is not None and 0 <= idade <= 120) and \
       (renda is not None and 0 <= renda <= 50000):
        return True  
    else:
        return False

### 3) Limpeza (obrigatório)

dados_limpos = []
removidos_idade = 0
removidos_renda = 0
removidos_outros = 0

for registro in dados_pesquisa:
    idade = to_int_safe(registro.get('idade'))
    renda = to_float_safe(registro.get('renda_mensal'))
    
    if registro_valido(registro):
        # Se True, o registro entra na lista limpa
        dados_limpos.append(registro)
    else:
        # Se False, identifica o motivo
        if idade is None or not (0 <= idade <= 120):
            removidos_idade += 1
        elif renda is None or not (0 <= renda <= 50000):
            removidos_renda += 1
        else:
            removidos_outros += 1


total_removidos = removidos_idade + removidos_renda + removidos_outros
print(f"--- Relatório de Limpeza ---")
print(f"Registros válidos: {len(dados_limpos)}")
print(f"Registros removidos: {total_removidos}")
print(f" - Motivo Idade (ruído/outlier): {removidos_idade}")
print(f" - Motivo Renda (ruído/outlier): {removidos_renda}")


### 4) Tratamento de ausentes (obrigatório)

avaliacoes_validas = [d['avaliacao'] for d in dados_limpos if d.get('avaliacao') is not None]
escolaridades_validas = [d['escolaridade'] for d in dados_limpos if d.get('escolaridade') is not None]
rendas_validas = sorted([d['renda_mensal'] for d in dados_limpos if d.get('renda_mensal') is not None])

## Preencha `avaliacao = None` com a **média** das avaliações válidas.
media_av = sum(avaliacoes_validas) / len(avaliacoes_validas) if avaliacoes_validas else 0

## Preencha `escolaridade = None` com a **moda** (valor mais frequente).
contagem = {}
for esc in escolaridades_validas:
    contagem[esc] = contagem.get(esc, 0) + 1
moda_esc = max(contagem, key=contagem.get) if contagem else "Superior"

# Preencha `renda_mensal = None` (se existir em `dados_limpos`) com a **mediana** das rendas válidas.
n = len(rendas_validas)
if n % 2 == 1:
    mediana_renda = rendas_validas[n // 2]
else:
    mediana_renda = (rendas_validas[n // 2 - 1] + rendas_validas[n // 2]) / 2


for d in dados_limpos:
    if d.get('avaliacao') is None:
        d['avaliacao'] = media_av
    
    if d.get('escolaridade') is None:
        d['escolaridade'] = moda_esc
        
    if d.get('renda_mensal') is None:
        d['renda_mensal'] = mediana_renda

#A média é sensível a outliers, o que pode distorcer o resultado se houver rendas muito altas ou baixas. 
#A mediana é uma medida de tendência central mais robusta, pois representa o valor central da amostra ordenada, sendo preferível para dados com assimetria


### 5) Transformação: discretização + ordinal (obrigatório)


# Crie um campo novo `escolaridade_nivel` (ordinal) usando o mapeamento:
map_escolaridade = {
    'Fundamental': 1,
    'Médio': 2,
    'Superior': 3,
    'Mestrado': 4,
    'Doutorado': 5,
}

# Crie um campo novo `faixa_idade` com as faixas: `0-17`, `18-25`, `26-35`, `36-50`,`51+`.
for registro in dados_limpos:
    idade = registro.get('idade')
    if idade <= 17:
        registro['faixa_idade'] = '0-17'
    elif idade <= 25:
        registro['faixa_idade'] = '18-25'
    elif idade <= 35:
        registro['faixa_idade'] = '26-35'
    elif idade <= 50:
        registro['faixa_idade'] = '36-50'
    else:
        registro['faixa_idade'] = '51+'

    esc_texto = registro.get('escolaridade')
    registro['escolaridade_nivel'] = map_escolaridade.get(esc_texto, 0)


### 6) Amostragem (obrigatório)

import random

# Amostra aleatória com 5 registros
# random.sample para garantir que não haja repetição do mesmo registro
if len(dados_limpos) >= 5:
    amostra_aleatoria = random.sample(dados_limpos, k=5)
else:
    amostra_aleatoria = dados_limpos[:] 

print("--- Amostra Aleatória (5 registros) ---")
for r in amostra_aleatoria:
    print(r)


# Amostra estratificada por gênero**
amostra_estratificada = []

# Identificar os gêneros únicos 
generos_unicos = set(d['genero'] for d in dados_limpos)

# Para cada gênero, selecionar aleatoriamente um registro
for gen in generos_unicos:
    # Filtra os registros que pertencem ao gênero atual
    estrato = [d for d in dados_limpos if d['genero'] == gen]
    0
    if estrato:
        # Escolhe um registro aleatório deste estrato
        registro_escolhido = random.choice(estrato)
        amostra_estratificada.append(registro_escolhido)

print("\n--- Amostra Estratificada por Gênero ---")
for r in amostra_estratificada:
    print(f"Gênero {r['genero']}: {r}")



### 7) Resumo exploratório (obrigatório)

idades = [d['idade'] for d in dados_limpos]
idade_media = sum(idades) / len(idades) if idades else 0

# Para a renda medianas
rendas = sorted([d['renda_mensal'] for d in dados_limpos])
n = len(rendas)
if n % 2 == 1:
    renda_mediana = rendas[n // 2]
else:
    renda_mediana = (rendas[n // 2 - 1] + rendas[n // 2]) / 2

# Distribuições 
dist_genero = {}
dist_faixa_etaria = {}

for d in dados_limpos:
    # Contagem por Gênero
    g = d['genero']
    dist_genero[g] = dist_genero.get(g, 0) + 1
    
    # Contagem por Faixa Etária
    f = d['faixa_idade']
    dist_faixa_etaria[f] = dist_faixa_etaria.get(f, 0) + 1

# Impressão dos Resultados
print("--- RESUMO EXPLORATÓRIO (DADOS LIMPOS) ---")
print(f"Idade Média: {idade_media:.2f} anos")
print(f"Renda Mediana: R$ {renda_mediana:.2f}")

print("\nDistribuição por Gênero:")
for gen, qtd in dist_genero.items():
    print(f" - {gen}: {qtd}")

print("\nDistribuição por Faixa Etária:")
for faixa, qtd in sorted(dist_faixa_etaria.items()):
    print(f" - {faixa}: {qtd}")

### 8) Exportação (obrigatório)

import csv

# Definindo cabeçalhos  do CSV
campos = [
    'id_cliente', 'idade', 'genero', 'escolaridade', 
    'renda_mensal', 'avaliacao', 'cidade', 
    'faixa_idade', 'escolaridade_nivel'
]

nome_arquivo = 'dados_limpos.csv'

try:
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as f:
        escritor = csv.DictWriter(f, fieldnames=campos)
        
        escritor.writeheader()
        
        escritor.writerows(dados_limpos)
        
    print(f"Sucesso! Arquivo '{nome_arquivo}' exportado com {len(dados_limpos)} registros.")

except Exception as e:
    print(f"Erro ao exportar o arquivo: {e}")





