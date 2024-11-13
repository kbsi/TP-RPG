import unittest
from src.person import Person


class TestPerson(unittest.TestCase):
    def test_10_hp_init(self):
        person = Person()

        self.assertEqual(10, person.get_hp())

    def test_attack_less_1_hp(self):
        attacker = Person()
        defender = Person()

        attacker.attack(defender)

        self.assertEqual(9, defender.get_hp())

    def test_attack_twice_less_2_hp(self):
        attacker = Person()
        defender = Person()

        attacker.attack(defender)
        attacker.attack(defender)

        self.assertEqual(8, defender.get_hp())

    def test_person_is_dead_at_zero_hp(self):
        attacker = Person()
        defender = Person()

        for _ in range(11):
            attacker.attack(defender)

        self.assertEqual(0, defender.get_hp())
        self.assertTrue(defender.is_dead)


if __name__ == '__main__':
    unittest.main()
