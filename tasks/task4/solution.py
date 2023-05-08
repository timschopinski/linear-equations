from linear_system import LinearSystem
from lu_factorization import LUFactorization


if __name__ == "__main__":
    a1 = 3
    a2 = a3 = -1
    system = LinearSystem(a1, a2, a3)
    print("=" * 40)
    lu_method = LUFactorization(system.A, system.b)
    lu_method.solve()
    print("LU Factorization")
    print(f"Residuum norm: {lu_method.residuum_norm}")
    print(f"Time: {lu_method.elapsed_time}s")


