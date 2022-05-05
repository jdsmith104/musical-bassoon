import math
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

    # Answer to Q1. Every third fibonacci number from f(1) is even
    def solve_question(self, n: int = 100) -> int:

        # 100th even fibonacci number index
        step = 3
        end_index = n * 3

        # Pre calculate all answers
        self.get_number(end_index)

        fib_sum = 0

        # _fib() should resolve in O(1)
        for i in range(0, end_index, step):
            fib_sum += self._fib(i)

        return fib_sum


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

    def test_case_7(self):
        fng = FibonacciNumberGenerator()
        n = 5
        expected_output = 188
        output = fng.solve_question(n)
        self.assertEqual(expected_output, output)

    def test_case_8(self):
        fng = FibonacciNumberGenerator()
        n = 10
        expected_output = 257114
        output = fng.solve_question(n)
        self.assertEqual(expected_output, output)

    def test_case_9(self):
        fng = FibonacciNumberGenerator()
        n = 20
        expected_output = 478361013020
        output = fng.solve_question(n)
        self.assertEqual(expected_output, output)

    def test_question_1(self):
        fng = FibonacciNumberGenerator()
        n = 100
        # Calculated manually using excel
        expected_output: int = 68673540288581500000000000000000000000000000000000000000000000
        expected_output_scaled: float = expected_output / math.pow(10, 61)
        output = fng.solve_question(n)
        output_scaled: float = output / math.pow(10, 61)
        self.assertAlmostEqual(expected_output_scaled, output_scaled, 7)


class DuplicateNumberFinder:
    def __init__(self) -> None:
        pass

    # Assumes lists are sorted in ascending order
    def get_duplicates(self, list_1: list, list_2: list) -> list:
        result = list()

        if list_1 and list_2:

            ptr_1: int = 0
            ptr_2: int = 0

            duplicate_values = set()

            while ptr_1 < len(list_1) and ptr_2 < len(list_2):
                val_1 = list_1[ptr_1]
                val_2 = list_2[ptr_2]

                if val_1 == val_2:
                    duplicate_values.add(val_1)
                    ptr_1 += 1
                    ptr_2 += 1
                elif val_1 < val_2:
                    ptr_1 += 1
                elif val_2 < val_1:
                    ptr_2 += 1

            result = list(duplicate_values)
        return result

# Answer to General Question 2


class DuplicateNumberFinderTest(unittest.TestCase):
    def test_case_1(self):
        dnf = DuplicateNumberFinder()

        list_1 = [1, 2, 4]
        list_2 = [1, 3, 4]
        expected_output = [1, 4]
        output = dnf.get_duplicates(list_1=list_1, list_2=list_2)

        self.assertListEqual(expected_output, output)

    # Test empty inputs
    def test_case_2(self):
        dnf = DuplicateNumberFinder()

        list_1 = []
        list_2 = [1, 3, 4]
        expected_output = []
        output = dnf.get_duplicates(list_1=list_1, list_2=list_2)

        self.assertListEqual(expected_output, output)

    # Test empty inputs
    def test_case_3(self):
        dnf = DuplicateNumberFinder()

        list_1 = [1, 3, 4]
        list_2 = []
        expected_output = []
        output = dnf.get_duplicates(list_1=list_1, list_2=list_2)

        self.assertListEqual(expected_output, output)

    # No matches
    def test_case_4(self):
        dnf = DuplicateNumberFinder()

        list_1 = [10, 20, 40]
        list_2 = [1, 3, 4]
        expected_output = []
        output = dnf.get_duplicates(list_1=list_1, list_2=list_2)

        self.assertListEqual(expected_output, output)

    # Test list_2 is longer
    def test_case_5(self):
        dnf = DuplicateNumberFinder()

        list_1 = [4]
        list_2 = [1, 3, 4]
        expected_output = [4]
        output = dnf.get_duplicates(list_1=list_1, list_2=list_2)

        self.assertListEqual(expected_output, output)

    # Test list_1 is longer and the first value is a match
    def test_case_6(self):
        dnf = DuplicateNumberFinder()

        list_1 = [1, 2, 4]
        list_2 = [1]
        expected_output = [1]
        output = dnf.get_duplicates(list_1=list_1, list_2=list_2)

        self.assertListEqual(expected_output, output)

    # Test multiple matches aren't counted
    def test_case_7(self):
        dnf = DuplicateNumberFinder()

        list_1 = [1, 1, 4]
        list_2 = [1, 1, 1]
        expected_output = [1]
        output = dnf.get_duplicates(list_1=list_1, list_2=list_2)

        self.assertListEqual(expected_output, output)


class Question4:
    def __init__(self) -> None:
        pass

    def solve(self, n: int) -> int:
        # Worked out this formula by hand
        # e.g.
        # n + nn + nnn + nnnn
        # = n + (10n+n) + (100n+10n+n) + (1000n+100n+10n+n)
        # = 4n + 30n + 200n + 1000n
        # = 1234n
        return 1234*n

# Answer to general question 4


class Question4Test(unittest.TestCase):
    def test_case_1(self):
        q4 = Question4()

        q4_input = 3
        expected_output = 3702
        output = q4.solve(q4_input)

        self.assertEqual(expected_output, output)

    def test_case_2(self):
        q4 = Question4()

        q4_input = 1
        expected_output = 1234
        output = q4.solve(q4_input)

        self.assertEqual(expected_output, output)

    def test_case_3(self):
        q4 = Question4()

        q4_input = 9
        expected_output = 11106
        output = q4.solve(q4_input)

        self.assertEqual(expected_output, output)


if __name__ == "__main__":
    unittest.main()
