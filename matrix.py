import math
from typing import List


def last_digit(num):
    return int(num - (10 * int(num / 10)))


def copy_matrix(matrix):
    return [[elem for elem in row] for row in matrix]


def matrix_sub_matrix(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_add_matrix(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def matrix_zeros(x, y):
    return [[0 for _ in range(x)] for _ in range(y)]


def diagonal_to_square_matrix(vector):
    return [[vector[i] if i == j else 0 for j in range(len(vector))] for i in range(len(vector))]


def vector_zeros(length: int) -> List[float]:
    return [0.0 for _ in range(length)]


def vector_ones(length: int) -> List[float]:
    return [1.0 for _ in range(length)]


def diagonal(a: List[List[float]]) -> List[float]:
    return [a[i][i] for i in range(len(a))]


def copy_vector(vector: List[float]) -> List[float]:
    return [elem for elem in vector]


def vector_sub_vector(a: List[float], b: List[float]) -> List[float]:
    tmp = copy_vector(a)
    for i in range(len(tmp)):
        tmp[i] -= b[i]
    return tmp


def vector_add_vector(a: List[float], b: List[float]) -> List[float]:
    tmp = copy_vector(a)
    for i in range(len(tmp)):
        tmp[i] += b[i]
    return tmp


def norm(vector: List[float]) -> float:
    counter = 0.0
    for elem in vector:
        counter += elem ** 2
    return counter ** 0.5


def matrix_vector_multiply(a: List[List[float]], b: List[float]) -> List[float]:
    copy_a = copy_matrix(a)
    copy_b = copy_vector(b)
    m = len(copy_a)
    n = len(copy_a[0])
    c = vector_zeros(m)

    for i in range(m):
        for l in range(n):
            c[i] += copy_a[i][l] * copy_b[l]
    return c


class Matrix:

    def __init__(self, a1: int, a2: int, a3: int, index: int = 188749):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.d = last_digit(index)
        self.c = last_digit(index//10)
        self.e = last_digit(index//100)
        self.f = last_digit(index//1000)
        self.N = int(f"9{self.c}{self.d}")
        self.A = self.create_matrix()
        self.b = self.create_vector()

    def create_matrix(self) -> List[List[float]]:
        A = [[0] * self.N for _ in range(self.N)]
        for i in range(self.N):
            A[i][i] = self.a1
            if i > 0:
                A[i][i - 1] = self.a2
            if i < self.N - 1:
                A[i][i + 1] = self.a2
            if i > 1:
                A[i][i - 2] = self.a3
            if i < self.N - 2:
                A[i][i + 2] = self.a3

        return A

    def create_vector(self) -> List[float]:
        b = [math.sin(n * (self.f + 1)) for n in range(1, self.N + 1)]
        return b

    def __str__(self):
        matrix_str = ''
        for i in range(min(self.N, 10)):
            matrix_str += f'{self.A[i][:10]} ... {self.A[i][-10:]}\n'
        if self.N > 10:
            matrix_str += '...\n'
        matrix_str += f'{self.A[-1][:10]} ... {self.A[-1][-10:]}'
        return matrix_str

    def __repr__(self):
        return f'Matrix(a1={self.a1}, a2={self.a2}, a3={self.a3}, index={int(str(self.f) + str(self.e) + str(self.c) + str(self.d))})'


if __name__ == "__main__":
    x = 5 + 7
    y = z = -1
    m = Matrix(x, y, z)
    print(m)
