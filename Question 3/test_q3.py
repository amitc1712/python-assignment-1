import unittest
from main import f7


class TestF7(unittest.TestCase):
    def test_f7_1(self):
        input_list = [12, 24, 35, 24, 88, 120, 88, 120]
        expected_output = [12, 24, 35, 88, 120]
        self.assertEqual(f7(input_list), expected_output)

    def test_f7_2(self):
        input_list = [12, 24, 35, -1, 0, 24, 88, 120, 88, 120, -1]
        expected_output = [12, 24, 35, -1, 0, 88, 120]
        self.assertEqual(f7(input_list), expected_output)


if __name__ == "__main__":
    unittest.main()
