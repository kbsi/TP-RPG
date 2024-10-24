import unittest


class MainTest(unittest.TestCase):
    def test_10_hp_init(self):
        self.assertEqual(10, person.get_hpp())


if __name__ == '__main__':
    unittest.main()
