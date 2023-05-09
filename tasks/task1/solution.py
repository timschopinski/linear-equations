from linear_system import LinearSystem


if __name__ == "__main__":
    x = 5 + 7
    y = z = -1
    system = LinearSystem(x, y, z)
    print(system.b)
