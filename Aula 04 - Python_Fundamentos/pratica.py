idades = [17, 22, 28, 35, 44, 68, None, 150]
# 1) filtrar inválidos
validas = [i for i in idades if i is not None and 0 <= i <= 120]
# 2) discretizar
faixas = []
for i in validas:
    if i <= 25:
        faixas.append('18-25')
    elif i <= 35:
        faixas.append('26-35')
    elif i <= 50:
        faixas.append('36-50')
    else:
        faixas.append('51+')

print(validas)
print(faixas)
