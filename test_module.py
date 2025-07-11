import unittest
from mean_var_std_calculator import calculate

class TestCalculator(unittest.TestCase):
    def test_valid_input(self):
        result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(result["sum"], [[9, 12, 15], [3, 12, 21], 36])

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3])

if __name__ == "__main__":
    unittest.main()