a = np.load("gyroidUniform.npy")

aa = a.reshape(200,40000)

b = sparse.csr_matrix(aa)

type(b)
Out[54]: scipy.sparse.csr.csr_matrix

a.nbytes
Out[55]: 64000000

aa.nbytes
Out[56]: 64000000

print(b.data.nbytes + b.indptr.nbytes + b.indices.nbytes)
96000636

ab = a.reshape(40000,200)

bb = sparse.csr_matrix(ab)

type(bb)
Out[60]: scipy.sparse.csr.csr_matrix

ab.nbytes
Out[61]: 64000000

print(bb.data.nbytes + bb.indptr.nbytes + bb.indices.nbytes)
96159836

bc = sparse.csc_matrix(ab)

type(bc)
Out[64]: scipy.sparse.csc.csc_matrix

print(bc.data.nbytes + bc.indptr.nbytes + bc.indices.nbytes)
96000636

np.count_nonzero(a)
Out[66]: 7999986

a50 = np.load("gyroid_50.npy")

np.count_nonzero(a50)
Out[68]: 4019991

a50.shape
Out[69]: (200, 200, 200)

aa50 = a50.reshape(200,40000)

b50 = sparse.csc_matrix(aa50)

aa50.nbytes
Out[72]: 64000000

print(b50.data.nbytes + b50.indptr.nbytes + b50.indices.nbytes)
48399896

aa50 = a50.reshape(40000,200)

b50 = sparse.csc_matrix(aa50)

aa50.nbytes
Out[76]: 64000000

print(b50.data.nbytes + b50.indptr.nbytes + b50.indices.nbytes)
48240696