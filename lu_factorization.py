import time
from matrix import Matrix
from vector import Vector


class LUFactorization:
    def __init__(self, a: Matrix, b: Vector):
        self.A = a
        self.b = b
        self.m = len(a)
        self.L = None
        self.U = None
        self.y = None
        self.x = None
        self.res = None
        self.elapsed_time = None
        self.residuum_norm = None

    def factorize(self):
        self.L = Matrix.identity(self.m)
        self.U = Matrix.zeros(self.m, self.m)

        # LUx = b
        for j in range(self.m):
            for i in range(j + 1):
                self.U[i][j] += self.A[i][j]
                for k in range(i):
                    self.U[i][j] -= self.L[i][k] * self.U[k][j]

            for i in range(j + 1, self.m):
                for k in range(j):
                    self.L[i][j] -= self.L[i][k] * self.U[k][j]
                self.L[i][j] += self.A[i][j]
                self.L[i][j] /= self.U[j][j]

    def solve(self):
        start_time = time.time()
        self.factorize()
        self.y = Vector.zeros(self.m)
        self.x = Vector.zeros(self.m)
        self.res = Vector.zeros(self.m)

        # Ly = b
        for i in range(self.m):
            value = self.b[i]
            for j in range(i):
                value -= self.L[i][j] * self.y[j]
            self.y[i] = value / self.L[i][i]

        # Ux = y
        for i in range(self.m - 1, -1, -1):
            value = self.y[i]
            for j in range(i + 1, self.m):
                value -= self.U[i][j] * self.x[j]
            self.x[i] = value / self.U[i][i]

        # Residuum
        self.res = self.A * self.x - self.b
        self.residuum_norm = self.res.norm()
        self.elapsed_time = time.time() - start_time
