import unittest
from src.person import Person
from src.weapon import Knife, Gun


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

        for _ in range(10):
            attacker.attack(defender)

        self.assertEqual(0, defender.get_hp())
        self.assertTrue(defender.is_dead)

    def test_resurect_person(self):
        attacker = Person()
        defender = Person()

        for _ in range(10):
            attacker.attack(defender)

        defender.resurect()

        self.assertEqual(10, defender.get_hp())
        self.assertFalse(defender.is_dead)

    def test_attack_with_gun(self):
        attacker = Person()
        defender = Person()
        gun = Gun()

        initial_hp = defender.get_hp()
        attacker.attack(defender, gun)
        self.assertEqual(defender.get_hp(), initial_hp - gun.damage)

    def test_attack_person_with_armor(self):
        attacker = Person()
        defender_with_armor = Person(with_armor=True)

        attacker.attack(defender_with_armor)
        # armor should reduce damage by 1
        self.assertEqual(10, defender_with_armor.get_hp())


if __name__ == '__main__':
    unittest.main()
