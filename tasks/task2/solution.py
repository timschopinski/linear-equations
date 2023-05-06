from matrix import Matrix
from jacobi import jacobi
from gauss_seidl import gauss_seidel


if __name__ == "__main__":
    x = 5 + 7
    y = z = -1
    matrix = Matrix(x, y, z)
    print("=" * 40)
    iterations, elapsed_time = jacobi(matrix.A, matrix.b)
    print("Jacobi's method")
    print("Time:", elapsed_time)
    print("Iterations:", iterations)
    iterations, elapsed_time = gauss_seidel(matrix.A, matrix.b)
    print("=" * 40)
    print("Gauss-Seidel's method")
    print("Time:", elapsed_time)
    print("Iterations:", iterations)
    print("=" * 40)
