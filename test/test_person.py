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
        knife = Knife()

        attacker.attack(defender, knife)

        self.assertEqual(9, defender.get_hp())

    def test_attack_twice_less_2_hp(self):
        attacker = Person()
        defender = Person()
        knife = Knife()

        attacker.attack(defender, knife)
        attacker.attack(defender, knife)

        self.assertEqual(8, defender.get_hp())

    def test_person_is_dead_at_zero_hp(self):
        attacker = Person()
        defender = Person()
        gun = Gun()

        for _ in range(2):
            attacker.attack(defender, gun)

        self.assertEqual(0, defender.get_hp())
        self.assertTrue(defender.is_dead)

    def test_resurect_person(self):
        attacker = Person()
        defender = Person()
        gun = Gun()

        for _ in range(2):
            attacker.attack(defender, gun)

        defender.resurect()

        self.assertEqual(10, defender.get_hp())
        self.assertFalse(defender.is_dead)

    def test_attack_with_knife(self):
        attacker = Person()
        defender = Person()
        knife = Knife()
        gun = Gun()

        initial_hp = defender.get_hp()
        attacker.attack(defender, knife)
        self.assertEqual(defender.get_hp(), initial_hp - knife.damage)

    def test_attack_with_gun(self):
        attacker = Person()
        defender = Person()
        knife = Knife()
        gun = Gun()
    
        initial_hp = defender.get_hp()
        attacker.attack(defender, gun)
        self.assertEqual(defender.get_hp(), initial_hp - gun.damage)

    def test_defender_dies_with_weapon(self):
        attacker = Person()
        defender = Person()
        gun = Gun()

        attacker.attack(defender, gun)
        attacker.attack(defender, gun)
        self.assertTrue(defender.check_if_dead())

if __name__ == '__main__':
    unittest.main()
