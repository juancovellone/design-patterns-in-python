import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class OperationStrategy(ABC):
    """
    Abstract Base Class
    """

    @abstractmethod
    def calculate(self, number_1, number_2):
        pass


class SumOperationStrategy(OperationStrategy):

    def calculate(self, number_1, number_2):
        return number_1 + number_2


class SubtractionOperationStrategy(OperationStrategy):

    def calculate(self, number_1, number_2):
        return number_1 - number_2


class MultiplicationOperationStrategy(OperationStrategy):

    def calculate(self, number_1, number_2):
        return number_1 * number_2


class DivisionOperationStrategy(OperationStrategy):

    def calculate(self, number_1, number_2):
        try:
            return number_1 / number_2
        except ZeroDivisionError as e:
            logger.error("You can't divide by zero.")
            logger.exception(e)


class Calculator:
    OPERATION_TYPE = {
        'sum': SumOperationStrategy(),
        'subtraction': SubtractionOperationStrategy(),
        'multiplication': MultiplicationOperationStrategy(),
        'division': DivisionOperationStrategy()
    }

    def __init__(self):
        self.__operation = None
        self.__last_result = None

    def calculate(self, number_1, number_2):
        """
        Performs the calculation according to the chosen operation.
        :return: None
        """
        if self.__operation is not None:
            self.__last_result = self.__operation.calculate(number_1, number_2)
            return self.__last_result

    def get_last_result(self):
        """
        Returns the value of the last calculated operation.
        :return: Int
        """
        return self.__last_result

    def set_operation(self, operation_type):
        """
        Configures the operation to be performed to calculate.
        :return: None"""
        try:
            self.__operation = self.OPERATION_TYPE[operation_type]
        except KeyError:
            self.__operation = None
            logger.error(f"The {operation_type} operation can't be resolved.")

    def calculate_operation(self, operation_type, number_1, number_2):
        """
        Perform the calculation of the operation.
        :return: int
        """
        self.set_operation(operation_type)
        return self.calculate(number_1, number_2)


if __name__ == '__main__':
    calculator = Calculator()
    number_1 = 15
    number_2 = 5
    operations = ['sum', 'subtraction', 'multiplication', 'division']
    for operation in operations:
        print(f'The result of {operation} operation between {number_1} and {number_2} '
              f'is: {calculator.calculate_operation(operation, number_1, number_2)}.')
