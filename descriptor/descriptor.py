
__all__ = [
    'LowerDescriptor',
    'MyClass'
]


class LowerDescriptor:

    def __init__(self, attribute: str = '') -> None:
        self.attribute: str = attribute

    def __get__(self, instance, owner) -> str:
        return self.attribute

    def __set__(self, instance, value) -> None:
        self.attribute = value.lower()


class MyClass:
    __name: str = LowerDescriptor()

    def __init__(self, name) -> None:
        self.__name: str = name

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value


if __name__ == '__main__':
    my_class = MyClass('Juan')
    print(my_class.name)
