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

    @staticmethod
    def _is_valid_number_of_sim(number_of_sim):
        """
        Стаический метод для проверки корректности количества сим-карт
        """
        return type(number_of_sim) == int and number_of_sim > 0

    def __setattr__(self, key, value):
        """
        Проверяет валидность параметра numbers_of_sim
        """
        if key == 'number_of_sim' and not self._is_valid_number_of_sim(value):
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        super().__setattr__(key, value)

    def __repr__(self):
        return f"Phone('{self.name}\', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return super().__str__()

    def __add__(self, other):
        return self.quantity + other.quantity
