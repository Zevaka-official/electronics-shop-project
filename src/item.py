from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """

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
    def instantiate_from_csv(cls, filename, delimiter=","):
        cls.all.clear()
        with open(filename, encoding="windows-1251") as f:
            reader = DictReader(f, delimiter=delimiter)
            for row in reader:
                cls(row["name"], float(row["price"]), cls.string_to_number(row["quantity"]))

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
