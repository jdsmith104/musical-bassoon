import unittest


class FibonacciNumberGenerator:
    def __init__(self) -> None:
        pass

    def get_number(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n > 1:
            # Array used to store _fib(n) at index n. Saves recalculating unnecessarily.
            self.calculated_result = [-1]*(n+1)
            return self._fib(n)
        else:
            # n < 0
            return 0

    # Private method to recusively calculate the next fibonacci number
    def _fib(self, x: int):
        if x == 0:
            return 0
        if x == 1:
            return 1
        else:
            # If _fib(x) has not already been found, recursively calculate it
            if self.calculated_result[x-1] == -1:
                self.calculated_result[x-1] = self._fib(x-1)
            if self.calculated_result[x-2] == -1:
                self.calculated_result[x-2] = self._fib(x-2)
            self.calculated_result[x] = self.calculated_result[x -
                                                               1] + self.calculated_result[x-2]
            return self.calculated_result[x]


class FibonacciNumberGeneratorTest(unittest.TestCase):
    def test_case_1(self):
        fng = FibonacciNumberGenerator()
        n = 1
        expected_output = 1
        self.assertEqual(expected_output, fng.get_number(n))

    def test_case_2(self):
        fng = FibonacciNumberGenerator()
        n = -10
        expected_output = 0
        self.assertEqual(expected_output, fng.get_number(n))

    def test_case_3(self):
        fng = FibonacciNumberGenerator()
        n = 10
        expected_output = 55
        self.assertEqual(expected_output, fng.get_number(n))

    def test_case_4(self):
        fng = FibonacciNumberGenerator()
        n = 20
        expected_output = 6765
        self.assertEqual(expected_output, fng.get_number(n))

    def test_case_5(self):
        fng = FibonacciNumberGenerator()
        n = 0
        expected_output = 0
        self.assertEqual(expected_output, fng.get_number(n))

    def test_case_6(self):
        fng = FibonacciNumberGenerator()
        n = 1
        expected_output = 1
        self.assertEqual(expected_output, fng.get_number(n))


if __name__ == "__main__":
    unittest.main()
