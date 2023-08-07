import pytest
from src.data_class import Data



def test_get_date():
    a = Data("2019-01-05T00:52:30.108534", 'test', 'test', 'test', 'test')
    assert a.get_date() == '5.1.2019'


def test_get_hide_account():
    a = Data('test', 'Счет 35737585785074382265', 'test', 'test', 'test')
    assert a.get_hide_account() == 'Счет **2265'


def test_get_hide_card_number_1():
    a = Data('test', 'test', 'test', 'test', 'test', 'Maestro 1308795367077170')
    assert a.get_hide_card_number() == 'Maestro 1308 79** **** 7170'

def test_get_hide_card_number_2():
    a = Data('test', 'test', 'test', 'test', 'test', 'Visa Gold 1308795367077170')
    assert a.get_hide_card_number() == 'Visa Gold 1308 79** **** 7170'


def test_get_hide_card_number_3():
    a = Data('test', 'test', 'test', 'test', 'test', 'Счет 26406253703545413262')
    assert a.get_hide_card_number() == 'Счет 2640 62** **** **** 3262'







