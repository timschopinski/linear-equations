from matrix import *
import time


def jacobi(a: List[List[float]], b: List[float], tolerance: int = 1e-9, max_iterations: int = 1000) -> tuple[int, float]:
    start_time = time.time()
    n = len(a)
    x = vector_zeros(n)
    tmp_x = vector_zeros(n)

    for k in range(max_iterations):
        for i in range(n):
            value = b[i]
            for j in range(n):
                if i != j:
                    value -= a[i][j] * x[j]
            tmp_x[i] = value / a[i][i]
        x = copy_vector(tmp_x)
        res = vector_sub_vector(matrix_vector_multiply(a, x), b)

        if norm(res) < tolerance:
            break
        k += 1
    else:
        raise ValueError(f"Jacobi failed to converge after {max_iterations} iterations")
    elapsed_time = time.time() - start_time
    return k, elapsed_time
