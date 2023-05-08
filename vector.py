from typing import List


class Vector:
    def __init__(self, data: List[float]):
        self.data = data

    def __repr__(self):
        return f"Vector({self.data})"

    def __str__(self):
        return f"{self.data}"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector([self.data[i] + other.data[i] for i in range(len(self.data))])
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector([self.data[i] - other.data[i] for i in range(len(self.data))])
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector([self.data[i] * other.data[i] for i in range(len(self.data))])
        elif isinstance(other, (int, float)):
            return Vector([self.data[i] * other for i in range(len(self.data))])
        else:
            raise TypeError("Unsupported operand type for *")

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector([self.data[i] * other for i in range(len(self.data))])
        else:
            raise TypeError("Unsupported operand type for *")

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector([self.data[i] / other for i in range(len(self.data))])
        else:
            raise TypeError("Unsupported operand type for /")

    def __getitem__(self, index: int) -> float:
        return self.data[index]

    def __setitem__(self, index: int, value: float):
        self.data[index] = value

    def __copy__(self):
        return type(self)([elem for elem in self.data])

    def __len__(self):
        return len(self.data)

    @staticmethod
    def zeros(length: int) -> 'Vector':
        return Vector([0.0 for _ in range(length)])

    @staticmethod
    def ones(length: int) -> 'Vector':
        return Vector([1.0 for _ in range(length)])

    def norm(self) -> float:
        counter = 0.0
        for elem in self.data:
            counter += elem ** 2
        return counter ** 0.5


if __name__ == "__main__":
    v1 = Vector([1, 2])
    v2 = Vector([2, 3])

