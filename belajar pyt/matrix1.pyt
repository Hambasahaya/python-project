import numpy as np

Amatrix = np.array([
    [5, 6, 9],
    [1, 2, 4],
    [7, 8, 2]])
Bmatrix = np.array([
    [4, 6],
    [2, 3]])

determinan = np.linalg.det(Amatrix)
print(f"determinan adalah:\n{determinan}")
