import unittest
from main import Male, Female  # replace with the actual module name


class TestPerson(unittest.TestCase):
    def test_male_get_gender(self):
        male = Male()
        self.assertEqual(male.get_gender(), "Male")

    def test_female_get_gender(self):
        female = Female()
        self.assertEqual(female.get_gender(), "Female")


if __name__ == "__main__":
    unittest.main()
