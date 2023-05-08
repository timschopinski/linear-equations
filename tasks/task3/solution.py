from linear_system import LinearSystem
from jacobi import jacobi_method
from gauss_seidl import gauss_seidel_method


if __name__ == "__main__":
    a1 = 3
    a2 = a3 = -1
    matrix = LinearSystem(a1, a2, a3)
    print("=" * 40)
    iterations, elapsed_time = jacobi_method(matrix.A, matrix.b)
    print("Jacobi's method")
    print("Time:", elapsed_time)
    print("Iterations:", iterations)
    iterations, elapsed_time = gauss_seidel_method(matrix.A, matrix.b)
    print("=" * 40)
    print("Gauss-Seidel's method")
    print("Time:", elapsed_time)
    print("Iterations:", iterations)
    print("=" * 40)

#   Output:
#     raise ValueError(f"Jacobi failed to converge after {max_iterations} iterations")
# ValueError: Jacobi failed to converge after 10 iterations
#     raise ValueError(f"Gauss-Seidel failed to converge after {max_iterations} iterations")
# ValueError: Gauss-Seidel failed to converge after 10 iterations
