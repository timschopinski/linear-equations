from linear_system import LinearSystem
from iterative_methods import Jacobi, GaussSeidel

if __name__ == "__main__":
    a1 = 3
    a2 = a3 = -1
    system = LinearSystem(a1, a2, a3)
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


#   Output:
#     raise ValueError(f"Jacobi failed to converge after {max_iterations} iterations")
# ValueError: Jacobi failed to converge after 10 iterations
#     raise ValueError(f"Gauss-Seidel failed to converge after {max_iterations} iterations")
# ValueError: Gauss-Seidel failed to converge after 10 iterations
