import math


class PerformOperations:

    def __init__(self, num):
        self._num = num

    def add_num(self):
        return self._num + self._num

    def square_num(self):
        return math.pow(self._num, 2)

    def sqrt_num(self):
        return math.sqrt(self._num)

if __name__ == '__main__':
    simple_operations = PerformOperations(5)

    print(simple_operations.add_num())
    print(simple_operations.square_num())
    print(simple_operations.sqrt_num())
