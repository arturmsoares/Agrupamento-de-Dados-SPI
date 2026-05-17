idades = [18, 24, 30, 42, 60]
min_idade = min(idades)
max_idade = max(idades)

idades_rescaladas = []
    
for x in idades:
        x_norm = (x - min_idade) / (max_idade - min_idade)
        idades_rescaladas.append(x_norm)

print("Idades originais:", idades)
print("Idades re-escaladas:", idades_rescaladas)