import pytest
from src.item import Item
from src.phone import Phone


phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init():
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_phone_str():
    assert str(phone1) == 'iPhone 14'


def test_phone_repr():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


item1 = Item('Телевизор', 45_000, 4)


def test_add():
    assert item1 + phone1 == 9
    assert phone1 + phone1 == 10


def test_number_of_sim():
    with pytest.raises(ValueError) as excinfo:
        phone1.number_of_sim = 0
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "Количество физических SIM-карт должно быть целым числом больше нуля."
