from linear_system import LinearSystem
from lu_factorization import LUFactorization
from matplotlib import pyplot as plt
from iterative_methods import Jacobi, GaussSeidel
from lu_factorization import LUFactorization


if __name__ == "__main__":
    N = [100, 500, 1000, 2000, 3000]
    time_jacobi = []
    time_gauss_seidel = []
    time_lu = []
    x = 5 + 7
    y = z = -1
    for n in N:
        system = LinearSystem(x, y, z, n=n)
        jacobi_method = Jacobi(system.A, system.b)
        jacobi_method.solve()
        gauss_seidel_method = GaussSeidel(system.A, system.b)
        gauss_seidel_method.solve()
        lu_method = LUFactorization(system.A, system.b)
        lu_method.solve()
        time_jacobi.append(jacobi_method.elapsed_time)
        time_gauss_seidel.append(gauss_seidel_method.elapsed_time)
        time_lu.append(lu_method.elapsed_time)

    plt.plot(N, time_jacobi, label="Jacobi", color="red")
    plt.plot(N, time_gauss_seidel, label="Gauss-Seidel", color="blue")
    plt.plot(N, time_lu, label="LU", color="green")
    plt.legend()
    plt.grid(True)
    plt.ylabel('Time (s)')
    plt.xlabel('Number of unknowns')
    plt.title('Time dependence on the number of unknowns')
    plt.savefig('chart.png')
    plt.show()
