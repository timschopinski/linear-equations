import math
from vector import Vector
from matrix import Matrix


def last_digit(num):
    return int(num - (10 * int(num / 10)))


class LinearSystem:

    def __init__(self, a1: int, a2: int, a3: int, index: int = 188749, n=None):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.d = last_digit(index)
        self.c = last_digit(index//10)
        self.e = last_digit(index//100)
        self.f = last_digit(index//1000)
        if n:
            self.N = n
        else:
            self.N = int(f"9{self.c}{self.d}")
        self.A = self.create_matrix()
        self.b = self.create_vector()

    def create_matrix(self) -> Matrix:
        data = [[0] * self.N for _ in range(self.N)]
        for i in range(self.N):
            data[i][i] = self.a1
            if i > 0:
                data[i][i - 1] = self.a2
            if i < self.N - 1:
                data[i][i + 1] = self.a2
            if i > 1:
                data[i][i - 2] = self.a3
            if i < self.N - 2:
                data[i][i + 2] = self.a3

        return Matrix(data)

    def create_vector(self) -> Vector:
        data = [math.sin(n * (self.f + 1)) for n in range(1, self.N + 1)]
        return Vector(data)

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
    m = LinearSystem(x, y, z)
    print(m)
