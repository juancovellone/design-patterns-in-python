import logging
import time
from abc import ABC, abstractmethod
from types import MethodType

from requests.exceptions import TooManyRedirects

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')


class BaseRequestDecorator(ABC):
    WAIT_TIME: int = 2

    def __init__(self, func):
        self.func = func
        self.recovered: bool = False
        self.logger = logging.getLogger(__name__)

    @abstractmethod
    def __call__(self, *args, **kwargs):
        """
        You need to implement this method.
        """
        pass

    def __get__(self, instance, cls):
        """
        Returns a method if called on an instance.
        """
        return self if instance is None else MethodType(self, instance)


class CatchesTooManyRequests(BaseRequestDecorator):
    """
    This decorator catches the exception if it TooManyRequests.
    """

    def __call__(self, *args, **kwargs):
        """
        if you get the exception to too many requests.
        Wait a few seconds and try again.
        """
        while True:
            try:
                func = self.func(*args, **kwargs)
                if self.recovered:
                    self.recovered = False
                return func
            except TooManyRedirects as error:
                logger.info(error)
                self.recovered = True
                time.sleep(self.WAIT_TIME)
            except Exception as e:
                logger.info(e)
                self.recovered = True
                time.sleep(self.WAIT_TIME)



