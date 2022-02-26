
from MtxOps import Matrix

class Operations(Matrix):

    def __init__(self, m, n):

        Matrix.__init__(self, m, n)

m1 = Matrix()
m1.to_mtx([[1,2], [3, 3], [4,6]])
m2 = Matrix()
m2.to_mtx([[1,1], [2, 2], [3, 3]])
print(m1)
print(m2.shape())
print(m1 + m2)
