import numpy as np
a = np.array([1, 2])
b = np.array([4, 6])
dist_e = np.sqrt(np.sum((a - b) ** 2))
dist_m = np.sum(np.abs(a - b))
print("Euclidiana:", dist_e)
print("Manhattan:", dist_m)