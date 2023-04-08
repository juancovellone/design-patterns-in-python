from abc import ABC, abstractmethod

__all__ = [
    'ANY_DESCRIPTION',
    'OldLibrary',
    'Target',
    'NewLibrary',
    'Adapter'
]


ANY_DESCRIPTION: str = "Any description"


class OldLibrary:

    @staticmethod
    def get_description() -> str:
        return ANY_DESCRIPTION


class Target(ABC):
    """
    Interface to be met.
    """

    @abstractmethod
    def get_description(self) -> str:
        pass


class NewLibrary:
    """
    New class tu use.
    """

    @staticmethod
    def description() -> dict[str, str]:
        return {
            'description': ANY_DESCRIPTION
        }


class Adapter(Target, NewLibrary):
    """
    Adapt the new library to work like the old library.
    """

    def get_description(self) -> str:
        description_dict = self.description()
        return description_dict.get('description', '')


if __name__ == '__main__':
    old_library = OldLibrary()
    print(old_library.get_description())

    adapter = Adapter()
    print(adapter.get_description())
