"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_calculate_total_price():
    item = Item("Смартфон", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    item = Item("Смартфон", 10000, 20)
    Item.discount = 0.8
    item.apply_discount()
    assert item.price == 10000.0

def test_name():
    item = Item("", 0, 0)
    item.name = "Смартфон"
    assert item.name == "Смартфон"
    with pytest.raises(Exception):
        item.name = "СуперСмартфон"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert type(Item.all[0]) is Item


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

