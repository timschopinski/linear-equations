from typing import List
from vector import Vector


class Matrix:

    def __init__(self, matrix: List[List[float]]):
        self.matrix = matrix

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.shape() != other.shape():
                raise ValueError("Matrices must have the same shape to be added.")
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(other.matrix))])
        else:
            raise TypeError("Cannot add a non-matrix object to a matrix.")

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.shape() != other.shape():
                raise ValueError("Matrices must have the same shape to be subtracted.")
            return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(len(self.matrix[0]))] for i in range(len(self.matrix))])
        else:
            raise TypeError("Cannot subtract a non-matrix object from a matrix.")

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.shape()[1] != other.shape()[0]:
                raise ValueError("Number of columns in left matrix must equal number of rows in right matrix.")
            result = self.zeros(self.shape()[0], other.shape()[1])
            for i in range(self.shape()[0]):
                for j in range(other.shape()[1]):
                    for k in range(self.shape()[1]):
                        result.matrix[i][j] += self.matrix[i][k] * other.matrix[k][j]
            return result
        elif isinstance(other, Vector):
            if self.shape()[1] != len(other):
                raise ValueError("Number of columns in matrix must equal length of vector.")
            result = other.zeros(self.shape()[0])
            for i in range(self.shape()[0]):
                for j in range(self.shape()[1]):
                    result[i] += self.matrix[i][j] * other[j]
            return result
        elif isinstance(other, (int, float)):
            return Matrix([[other * elem for elem in row] for row in self.matrix])
        else:
            raise TypeError("Cannot multiply a matrix by a non-matrix or non-vector object.")

    def __len__(self):
        return len(self.matrix)

    def __eq__(self, other):
        if isinstance(other, Matrix):
            return self.matrix == other.matrix
        else:
            return False

    def __getitem__(self, index: int) -> List[float]:
        return self.matrix[index]

    def __copy__(self):
        return type(self)([[elem for elem in row] for row in self.matrix])

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in row]) for row in self.matrix])

    def shape(self):
        return len(self.matrix), len(self.matrix[0])

    def transpose(self):
        return Matrix([[self.matrix[j][i] for j in range(self.shape()[0])] for i in range(self.shape()[1])])

    def trace(self):
        if self.shape()[0] != self.shape()[1]:
            raise ValueError("Matrix must be square to have a trace.")
        return sum([self.matrix[i][i] for i in range(self.shape()[0])])

    def diagonal(self):
        if self.shape()[0] != self.shape()[1]:
            raise ValueError("Matrix must be square to have a diagonal.")
        return [self.matrix[i][i] for i in range(self.shape()[0])]

    @staticmethod
    def zeros(x, y):
        return Matrix([[0 for _ in range(x)] for _ in range(y)])

    @staticmethod
    def diagonal_to_square_matrix(vector):
        return Matrix([[vector[i] if i == j else 0 for j in range(len(vector))] for i in range(len(vector))])

    @staticmethod
    def identity(size):
        return Matrix([[1 if i == j else 0 for j in range(size)] for i in range(size)])

if __name__ == "__main__":
    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])
    m = Matrix([[1, 2], [3, 4]])
    v = Vector([1, 2])
    result = m * v
    print(result)
    print(type(result))
