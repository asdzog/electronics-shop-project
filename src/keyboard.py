from src.item import Item


class Keyboard(Item):

    def __init__(self, name: str, price: float, quantity: int, language='EN') -> None:
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def language(self):
        return self.__language

    def __str__(self):
        return f'{self.name}'

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
