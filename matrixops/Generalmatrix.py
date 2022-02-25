from random import random

class Matrix:

    def __init__(self, m=2, n=2):

        self.m = m
        self.n = n
        self.data = []

    def make_rand_mtx(self, m, n):

        self.m = m
        self.n = n

        mtx = [[round(random(), 3) for col in range(n)] for row in range(m)]
        self.data = mtx

        return mtx

    
