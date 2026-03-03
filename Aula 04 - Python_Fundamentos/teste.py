avaliacoes = [4, None, 5, 3]
soma = 0
n = 0
for v in avaliacoes:
    if v is None:
        continue
    soma += v
    n += 1
    
media = soma / n if n > 0 else None
print(media)