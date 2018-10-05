import numpy as np

sparse_m = np.zeros((4,5))
sparse_m[0][2] = 3
sparse_m[0][4] = 4
sparse_m[1][2] = 5
sparse_m[1][3] = 7
sparse_m[3][1] = 2
sparse_m[3][2] = 6

size = 0
for i in range(0, 4):
    for j in range(0, 5):
        if sparse_m[i][j] != 0:
            size = size + 1
            
compact = np.zeros((3, size))

# Making of new matrix 
k = 0; 
for i in range(0, 4):
    for j in range(0, 5):
            if sparse_m[i][j] != 0:
                compact[0][k] = i 
                compact[1][k] = j 
                compact[2][k] = sparse_m[i][j] 
                k = k + 1

data = compact[2]
row = compact[0]
col = compact[1]

from scipy import sparse
mtx = sparse.csr_matrix((data[0:3], (row[0:3], col[0:3])), shape=(2, 5))
dense = mtx.todense()