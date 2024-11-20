import pytest
from model.person import Person
from model.weapon import Knife, Gun


def test_10_hp_init():
    person = Person()
    assert person.get_hp() == 10


def test_str_name():
    person = Person("John")
    assert str(person) == "John"


def test_attack_less_1_hp():
    attacker = Person()
    defender = Person()
    attacker.attack(defender)
    assert defender.get_hp() == 9


def test_attack_twice_less_2_hp():
    attacker = Person()
    defender = Person()
    attacker.attack(defender)
    attacker.attack(defender)
    assert defender.get_hp() == 8


def test_attack_with_weapon():
    attacker = Person()
    defender = Person()
    knife = Knife()
    attacker.attack(defender, knife)
    assert defender.get_hp() == 8  # Assuming knife does 2 damage


def test_attack_with_gun():
    attacker = Person()
    defender = Person()
    gun = Gun()
    attacker.attack(defender, gun)
    assert defender.get_hp() == 5  # Assuming gun does 5 damage


def test_attack_person_with_armor():
    attacker = Person()
    defender_with_armor = Person(with_armor=True)

    attacker.attack(defender_with_armor)
    # armor should reduce damage by 1
    assert defender_with_armor.get_hp() == 10


def test_resurect():
    attacker = Person()
    defender = Person()
    gun = Gun()
    attacker.attack(defender, gun)
    attacker.attack(defender, gun)
    defender.resurect()

    assert defender.get_hp() == 10
    assert defender.check_if_dead() == False
