import time
from matrix import Matrix
from vector import Vector


def gauss_seidel_method(a: Matrix, b: Vector, tolerance: int = 1e-9, max_iterations: int = 10) -> tuple[int, float]:
    start_time = time.time()
    n = len(a)
    x = b.zeros(n)
    for iterations in range(max_iterations):
        for i in range(n):
            value = b[i]
            for j in range(n):
                if i != j:
                    value -= a[i][j] * x[j]
            x[i] = value / a[i][i]
        res = a * x - b
        if res.norm() < tolerance:
            break
        iterations += 1
    else:
        raise ValueError(f"Gauss-Seidel failed to converge after {max_iterations} iterations")
    elapsed_time = time.time() - start_time
    return iterations + 1, elapsed_time
