from src.item import Item


class Phone(Item):
    """
    Создание экземпляра класса Phone.

    :param name: Название телефона.
    :param price: Цена за один телефон.
    :param quantity: Количество телефонов в магазине.
    :param number_of_sim: Количество поддерживаемых сим-карт в телефоне.
    """
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"Phone('{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        return self.quantity + other.quantity
