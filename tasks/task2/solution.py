from linear_system import LinearSystem
from jacobi import jacobi_method
from gauss_seidl import gauss_seidel_method


if __name__ == "__main__":
    x = 5 + 7
    y = z = -1
    system = LinearSystem(x, y, z)
    print("=" * 40)
    iterations, elapsed_time = jacobi_method(system.A, system.b)
    print("Jacobi's method")
    print("Time:", elapsed_time)
    print("Iterations:", iterations)
    iterations, elapsed_time = gauss_seidel_method(system.A, system.b)
    print("=" * 40)
    print("Gauss-Seidel's method")
    print("Time:", elapsed_time)
    print("Iterations:", iterations)
    print("=" * 40)
