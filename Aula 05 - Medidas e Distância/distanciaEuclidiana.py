import math
cliente_a = [25, 2000]
cliente_b = [35, 8000]
dist_euclidiana = math.sqrt((cliente_a[0] - cliente_b[0])**2 + (cliente_a[1] - cliente_b[1])**2)
print("Distância Euclidiana:", dist_euclidiana)

# É a distância “em linha reta” entre dois pontos.
# Neste exemplo, o salário domina a distância. 
# Isso mostra por que normalização é importante antes de usar medidas baseadas em distância.