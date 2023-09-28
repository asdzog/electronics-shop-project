"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_item():
    return Item("PC", 15_000, 8)


def test_item_init(test_item):
    assert len(test_item.all) == 1
    assert test_item.pay_rate == 1
    assert test_item.name == 'PC'
    assert test_item.price == 15_000
    assert test_item.quantity == 8


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 120_000


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 15_000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items.csv')
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number('not_number') is None


item1 = Item('Телевизор', 45_000, 4)


def test_str():
    assert str(item1) == 'Телевизор'


def test_repr():
    assert repr(item1) == "Item('Телевизор', 45000, 4)"


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


def test_add():
    assert item1 + phone1 == 9
    assert phone1 + phone1 == 10

