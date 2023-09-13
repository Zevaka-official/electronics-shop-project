from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, num_sim_cards: int) -> None:
        super().__init__(name, price, quantity)
        self.number_of_sim = num_sim_cards

    def __repr__(self):
        return f"Phone('{self._name}', {self.price}, {self.quantity}, {self._num_sim_cards})"

    def __str__(self):
        return self._name

    @property
    def number_of_sim(self):
        return self._num_sim_cards

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self._num_sim_cards = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
