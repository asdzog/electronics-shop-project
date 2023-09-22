from csv import DictReader
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

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

    @classmethod
    def instantiate_from_csv(cls, csv_file):
        """
        Инициализирует экземпляры класса данными из файла items.csv
        """
        Item.all = []
        current_dir = os.path.dirname(os.path.realpath(__file__))
        items_file_path = os.path.join(current_dir, csv_file)
        with open(items_file_path, 'r', encoding='windows-1251') as csv:
            items = DictReader(csv)
            for product in items:
                name = product['name']
                price = Item.string_to_number(product['price'])
                count = Item.string_to_number(product['quantity'])
                Item(name, price, count)

    @staticmethod
    def string_to_number(text_line):
        """
        Возвращает число из строки, если возможно, иначе - None
        """
        try:
            return int(float(text_line))
        except ValueError:
            return None
