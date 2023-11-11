import unittest
from main import question4


class TestSquares(unittest.TestCase):
    def test_get_squares(self):
        expected_output = [x**2 for x in range(1, 21)]
        self.assertEqual(question4(), expected_output)

    def test_get_squares_length(self):
        self.assertEqual(len(question4()), 20)


if __name__ == "__main__":
    unittest.main()
