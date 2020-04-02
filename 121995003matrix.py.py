import random
from random import random
import numpy as np

A = [[1,1,1],[1,1,1],[1,1,1]]
B = [[1,1,1],[1,1,1],[1,1,1]]

for i in range(3):
    for j in range(3):
        A[i][j] = round(random()*3+2)

for i in range(3):
    for j in range(3):
        B[i][j] = round(random()*4+5)

C = np.matmul(np.array(A),np.array(B))

print (A)
print (B)
print (C)