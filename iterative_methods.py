import time
from abc import ABC, abstractmethod
from copy import copy
from matrix import Matrix
from vector import Vector


class IterativeMethod(ABC):
    def __init__(self, a: Matrix, b: Vector, tolerance: int = 1e-9, max_iterations: int = 50):
        self._a = a
        self._b = b
        self._tolerance = tolerance
        self.max_iterations = max_iterations
        self.elapsed_time = None
        self.number_of_iterations = 0
        self.residuum_norm = None

    @abstractmethod
    def solve(self) -> None:
        ...

    def save_results(self, _time: float, number_of_iterations: int, residuum_norm: float):
        self.elapsed_time = _time
        self.number_of_iterations = number_of_iterations
        self.residuum_norm = residuum_norm


class GaussSeidel(IterativeMethod):

    def solve(self) -> None:
        start_time = time.time()
        n = len(self._a)
        x = self._b.zeros(n)
        for iterations in range(self.max_iterations):
            for i in range(n):
                value = self._b[i]
                for j in range(n):
                    if i != j:
                        value -= self._a[i][j] * x[j]
                x[i] = value / self._a[i][i]
            res = self._a * x - self._b
            if res.norm() < self._tolerance:
                break
            iterations += 1
        else:
            raise ValueError(f"Gauss-Seidel failed to converge after {self.max_iterations} iterations")
        self.save_results(time.time() - start_time, iterations + 1, res.norm())


class Jacobi(IterativeMethod):

    def solve(self) -> None:
        start_time = time.time()
        n = len(self._a)
        x = self._b.zeros(n)
        tmp_vector = self._b.zeros(n)

        for iterations in range(self.max_iterations):
            for i in range(n):
                value = self._b[i]
                for j in range(n):
                    if i != j:
                        value -= self._a[i][j] * x[j]
                tmp_vector[i] = value / self._a[i][i]
            x = copy(tmp_vector)
            res = self._a * x - self._b
            if res.norm() < self._tolerance:
                break
            iterations += 1
        else:
            raise ValueError(f"Jacobi failed to converge after {self.max_iterations} iterations")
        self.save_results(time.time() - start_time, iterations + 1, res.norm())
