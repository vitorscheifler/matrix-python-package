from random import random
from itertools import starmap
from operator import mul


class Matrix:

    def __init__(self, m=2, n=2):
        """Class used to represent matrices.

        Attributes:
        m (int) -> number of rown of the matrix.
        n (int) -> number of columns of the matrix.
        data (list) -> list of lists containing numeric values
        """

        self.m = m
        self.n = n
        self.data = []

    def make_rand_mtx(self, m, n):
        """Make a random matrix of m rows and n columns.
            Containing values between 0 and 1."""

        self.m = m
        self.n = n

        mtx = [[round(random(), 3) for col in range(n)] for row in range(m)]
        self.data = mtx

        return mtx

    def to_mtx(self, list_of_lists):
        """ Convert a list of numeric lists into a matrix object"""

        check_sizes = [len(list) for list in list_of_lists]
        set1 = set(check_sizes)

        if len(set1) > 1:
            raise ValueError('The matrix input has lists of different shapes! Please check the input')

        self.m = len(list_of_lists)
        self.n = len(list_of_lists[0])
        self.data = list_of_lists

    def T(self):
        """Return the transposed matrix object."""

        self.data = list(map(list, zip(*self.data)))
        self.m = len(self.data)
        self.n = len(self.data[0])

        return self.data

    def shape(self):
        """Returns the shape of the matrix object."""

        return self.m, self.n

    def __repr__(self):
        "Representation of matrix object."
        return "Matrix with {} rows and {} columns.".format(self.m, self.n)

    def __add__(self, other):
        """Make the addition operation of matrix with the + operator"""
        result = Matrix()

        if self.shape() != other.shape():
            raise ValueError("The matrices have different orders!")

        result.data = [list(map(sum, zip(*t)))
                       for t in zip(self.data, other.data)]
        result.m = self.m
        result.n = self.n
        return result.data

    def __sub__(self, other):
        """Make the subtraction operation of matrix with the - operator"""
        result = Matrix()

        if self.shape() != other.shape():
            raise ValueError("The matrices have different orders!")

        negative_other = [[-1* i for i in t] for t in other.data]

        result.data = [list(map(sum, zip(*t)))
                       for t in zip(self.data, negative_other)]
        result.m = self.m
        result.n = self.n
        return result.data

    def __mul__(self, other):
        """Make the multiplication operation of matrix with the * operator"""
        if self.n != other.m:
            raise ValueError("The number of columns of the first matrix is different of the number of rows of the second.")

        result = Matrix()

        zip_b = list(zip(*other.data))

        result.m = self.m
        result.n = other.n

        result.data = [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b))
                    for col_b in zip_b] for row_a in self.data]

        return result.data
