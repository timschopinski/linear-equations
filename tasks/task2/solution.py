from linear_system import LinearSystem
from iterative_methods import Jacobi, GaussSeidel


if __name__ == "__main__":
    x = 5 + 7
    y = z = -1
    system = LinearSystem(x, y, z)
    print("=" * 40)
    jacobi_method = Jacobi(system.A, system.b)
    jacobi_method.solve()
    print("Jacobi's method")
    print(f"Time: {jacobi_method.elapsed_time}s")
    print("Iterations: ", jacobi_method.number_of_iterations)
    gauss_seidel_method = GaussSeidel(system.A, system.b)
    gauss_seidel_method.solve()
    print("=" * 40)
    print("Gauss-Seidel's method")
    print(f"Time: {gauss_seidel_method.elapsed_time}s")
    print("Iterations: ", gauss_seidel_method.number_of_iterations)
    print("=" * 40)
