"""����� ���� �������� ����� � �������������� pytest ��� ������ item."""
import pytest

from src.item import Item, InstantiateCSVError


def test_calculate_total_price():
    item = Item("��������", 10000, 20)
    assert item.calculate_total_price() == 200000


def test_apply_discount():
    item = Item("��������", 10000, 20)
    Item.discount = 0.8
    item.apply_discount()
    assert item.price == 10000.0


def test_name():
    item = Item("", 0, 0)
    item.name = "��������"
    assert item.name == "��������"

    item.name = "�������������"
    assert item.name == "����������"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert type(Item.all[0]) is Item


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item('��������', 10000, 20)
    assert repr(item1) == "Item('��������', 10000, 20)"


def test_str():
    item1 = Item('��������', 0, 0)
    assert str(item1) == '��������'


def test_add():
    item1 = Item('��������', 10000, 20)
    item2 = Item('��������', 10000, 20)
    assert item1 + item2 == 40
    with pytest.raises(TypeError):
        item1 + '��������'


def test_instantiate_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('src/items.csv')


def test_instantiate_csv_file_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('src/items.csv1')
