from random import random

class Matrix:

    def __init__(self, m=2, n=2):
        """
        """

        self.m = m
        self.n = n
        self.data = []

    def make_rand_mtx(self, m, n):
        """
        """

        self.m = m
        self.n = n

        mtx = [[round(random(), 3) for col in range(n)] for row in range(m)]
        self.data = mtx

        return mtx

    def to_mtx(self, list_of_lists):
        """
        """

        check_sizes = [len(list) for list in list_of_lists]
        set1 = set(check_sizes)

        if len(set1) > 1:
            raise ValueError('The matrix input has lists of different shapes! Please check the input')

        self.m = len(list_of_lists)
        self.n = len(list_of_lists[0])
        self.data = list_of_lists

    def T(self):
        """
        """

        self.data = list(map(list, zip(*self.data)))
        self.m = len(self.data)
        self.n = len(self.data[0])

        return self.data

    def shape(self):

        return self.m, self.n

    def __repr__(self):
        return "Matrix with {} rows and {} columns.".format(self.m, self.n)

    def __add__(self, other):

        result = Matrix()

        if self.shape() != other.shape():
            raise ValueError("The matrices have different orders!")

        result.data = [list(map(sum, zip(*t)))
                       for t in zip(self.data, other.data)]
        result.m = self.m
        result.n = self.n
        return result.data