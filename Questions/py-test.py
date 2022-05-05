from math import floor
import unittest

class Generator:
    def __init__(self):
        pass

    # Calculates the sum of all positive integers upto and including range that are divisible by factor
    def get_sum_of_multiples_in_range(self, range: int, factor: int) -> int:
        sum = 0
        n = floor(range/factor)
        if range > 0 and factor > 0 and n > 0:
            sum = floor(factor*((n * (n +1))/2))
        return sum


class GeneratorTest(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

    def test_negative_integers(self):
        input_ranges = [10, -18]
        input_factors = [-2, 6]
        expected_output = [0, 0]
        sub_test_count = len(input_factors)
        generator = Generator()
        for i in range(sub_test_count):
            input_range = input_ranges[i]
            input_factor = input_factors[i]
            output = generator.get_sum_of_multiples_in_range(input_range, input_factor)
            self.assertEqual(output, expected_output[i])
    
    def test_small_postive_integers(self):
        input_ranges = [10, 18, 17]
        input_factors = [2, 6, 5]
        expected_output = [30, 36, 30]
        sub_test_count = len(input_factors)
        generator = Generator()
        for i in range(sub_test_count):
            input_range = input_ranges[i]
            input_factor = input_factors[i]
            output = generator.get_sum_of_multiples_in_range(input_range, input_factor)
            self.assertEqual(output, expected_output[i])

    def test_large_postive_integers(self):
        generator = Generator()
        input_range = 102030 - 1
        input_factor = 3
        # Generated answer using excel
        expected_output = 1734969135
        output = generator.get_sum_of_multiples_in_range(input_range, input_factor)
        print("Generated answer", output)
        self.assertEqual(output, expected_output)

    def test_factor_larger_than_range(self):
        input_ranges = [400, 45, 12]
        input_factors = [500, 600, 500]
        expected_output = [0, 0, 0]
        sub_test_count = len(input_factors)
        generator = Generator()
        for i in range(sub_test_count):
            input_range = input_ranges[i]
            input_factor = input_factors[i]
            output = generator.get_sum_of_multiples_in_range(input_range, input_factor)
            self.assertEqual(output, expected_output[i])


class SublistListFactory:
    def get_sublist(self, n: int) -> list:
        result = []
        if n > 0:
            result = [ [i+1 for i in range(0, j)] for j in range(1, n+1)]
        return result

class SublistFactoryTest(unittest.TestCase):
    def test_sublists_generated(self):
        sublist_factory = SublistListFactory()

        input_n = [0, 1, 2, 3, -1]
        expected_output = [[], [[1]], [[1], [1,2]], [[1], [1,2], [1,2,3]], []]
        
        for i in range(len(input_n)):
            output = (sublist_factory.get_sublist(input_n[i]))
            self.assertListEqual(expected_output[i], output)


if __name__ == "__main__":
    unittest.main()

