from abc import ABC, abstractmethod
from typing import Set, Any


class Observer(ABC):
    """
    Abstract Base Class
    """

    @abstractmethod
    def update(self, **kwargs):
        pass


class Observable(ABC):
    """
    Abstract Base Class.
    """

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, **kwargs):
        pass


class Subscriber(Observer):

    def __init__(self, name: str):
        self.__name: str = name

    def update(self, title: str, description: str, url: str) -> None:
        """
        Receive the notification and perform an action.
        """
        print(f"""
        I am {self.__name}
        A new magazine note received.
        Title: {title}
        Description: {description}
        Url: {url}
        """)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        self.__name = name


class DigitalMagazine(Observable):

    def __init__(self):
        self.__subscribers: Set[Subscriber] = set()

    def attach(self, subscribe: Subscriber) -> None:
        """
        Add subscriber to Digital Magazine.
        """
        self.__subscribers.add(subscribe)

    def detach(self, subscribe: Subscriber) -> None:
        """
        Remove subscriber to Digital Magazine.
        """
        self.__subscribers.remove(subscribe)

    def notify(self, title: str, description: str, url: str) -> None:
        """
        Notify subscribers of a new post.
        """
        for subscribe in self.__subscribers:
            subscribe.update(title, description, url)

    def count_subscribers(self) -> int:
        """
        Count total subscribers.
        """
        return len(self.__subscribers)


if __name__ == '__main__':
    user1 = Subscriber('John')
    user2 = Subscriber('Smit')
    digital_magazine = DigitalMagazine()
    digital_magazine.attach(user1)
    digital_magazine.attach(user2)
    digital_magazine.notify(
        title='The World Cup begins',
        description='The world cup is a competition where the countries compete to know who is the best.',
        url='http://localhost'
    )
