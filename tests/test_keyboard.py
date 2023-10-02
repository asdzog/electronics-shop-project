import pytest
from src.keyboard import Keyboard

kb1 = Keyboard('Dark Project KD87A', 9600, 5)


def test_kb_init():
    assert str(kb1) == "Dark Project KD87A"
    assert kb1.language == "EN"
    assert kb1.quantity == 5
    assert kb1.price == 9600


def test_change_lang():
    kb1.change_lang()
    assert str(kb1.language) == "RU"
    kb1.change_lang()
    assert str(kb1.language) == "EN"


def test_language():
    with pytest.raises(AttributeError) as excinfo:
        kb1.language = 'CH'
    exception_msg = excinfo.value.args[0]
    assert exception_msg == "property 'language' of 'Keyboard' object has no setter"
