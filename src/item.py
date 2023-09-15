import csv
import os
from pathlib import Path


class InstantiateCSVError(Exception):
    pass


class Item:
    """
    Класс для представления товара в магазине.
    """
    CSV_PATH = os.path.join(os.path.dirname(__file__), "items.csv")
    pay_rate = 1.0
    all = []
    max_name_len = 20

    def __init__(self, name: str, price: float, quantity: int, **kwargs) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(**kwargs)
        self._name = name
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"Item('{self._name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self._name

    def __add__(self, other):
        if issubclass(other.__class__, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить не экземпляры класса Item")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > self.max_name_len:
            raise Exception(f'Длина наименования товара превышает {self.max_name_len} символов')

    @classmethod
    def instantiate_from_csv(cls):
        """класс-метод, инициализирующий экземпляры класса Item данными из файла src/items.csv"""

        if not os.path.exists(cls.CSV_PATH):
            raise FileNotFoundError("Отсутствует файл item.csv")
        try:
            with open(cls.CSV_PATH, encoding='cp1251') as file:
                reader = csv.DictReader(file)
                cls.all.clear()
                for line in reader:
                    item = cls(line['name'], float(line['price']), int(line['quantity']))
        except (KeyError, TypeError):
            raise InstantiateCSVError("Файл item.csv поврежден")

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def calculate_total_price(self) -> float:
        """
     Рассчитывает общую стоимость конкретного товара в магазине.
     :return: Общая стоимость товара.
     """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price *= Item.pay_rate
