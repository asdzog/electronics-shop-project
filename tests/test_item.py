"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


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
