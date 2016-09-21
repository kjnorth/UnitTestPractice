import unittest
import SimpleOperations


class UnitTest(unittest.TestCase):

    def test_add_num(self):
        simple_operations = SimpleOperations.PerformOperations(5)
        result = simple_operations.add_num()
        expected = 10

        self.assertEquals(result, expected)

    def test_square_num(self):
        simple_operations = SimpleOperations.PerformOperations(5)
        result = simple_operations.square_num()
        expected = 25

        self.assertEquals(result, expected)

    def test_sqrt_num(self):
        simple_operations = SimpleOperations.PerformOperations(5)
        result = simple_operations.sqrt_num()
        expected = 2.23606797749979

        self.assertEquals(result, expected)

if __name__ == '__main__':
    unittest.main()
