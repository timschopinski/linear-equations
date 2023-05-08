import time
from matrix import Matrix
from vector import Vector


class GaussSeidel:
    def __init__(self, a: Matrix, b: Vector, tolerance: int = 1e-9, max_iterations: int = 10):
        self.a = a
        self.b = b
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.elapsed_time = None
        self.number_of_iterations = 0

    def solve(self) -> None:
        start_time = time.time()
        n = len(self.a)
        x = self.b.zeros(n)
        for iterations in range(self.max_iterations):
            for i in range(n):
                value = self.b[i]
                for j in range(n):
                    if i != j:
                        value -= self.a[i][j] * x[j]
                x[i] = value / self.a[i][i]
            res = self.a * x - self.b
            if res.norm() < self.tolerance:
                break
            iterations += 1
        else:
            raise ValueError(f"Gauss-Seidel failed to converge after {self.max_iterations} iterations")
        self.elapsed_time = time.time() - start_time
        self.number_of_iterations = iterations + 1
