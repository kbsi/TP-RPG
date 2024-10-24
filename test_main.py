import unittest

from person import Person

class MainTest(unittest.TestCase):
    def test_10_hp_init(self):
        person = Person()
        
        self.assertEqual(10, person.get_hp())


if __name__ == '__main__':
    unittest.main()
