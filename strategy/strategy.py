import logging
from abc import ABC, abstractmethod


logger = logging.getLogger(__name__)


class Operation(ABC):
    """
    Abstract Base Class
    """

    @abstractmethod
    def calculate(self, number_1, number_2):
        pass


class SumOperation(Operation):

    def calculate(self, number_1, number_2):
        return number_1 + number_2


class SubtractionOperation(Operation):

    def calculate(self, number_1, number_2):
        return number_1 - number_2


class MultiplicationOperation(Operation):

    def calculate(self, number_1, number_2):
        return number_1 * number_2


class DivisionOperation(Operation):

    def calculate(self, number_1, number_2):
        try:
            return number_1 / number_2
        except ZeroDivisionError as e:
            logger.error("You can't divide by zero.")
            logger.exception(e)


class CalculatorStrategy:
    OPERATION_TYPE = {
        'sum': SumOperation(),
        'subtraction': SubtractionOperation(),
        'multiplication': MultiplicationOperation(),
        'division': DivisionOperation()
    }

    def __init__(self):
        self.__operation = None
        self.__last_result = None

    def calculate(self, number_1, number_2):
        if self.__operation is not None:
            self.__last_result = self.__operation.calculate(number_1, number_2)
            return self.__last_result

    def get_last_result(self):
        return self.__last_result

    def set_operation(self, operation_type):
        try:
            self.__operation = self.OPERATION_TYPE[operation_type]
        except KeyError:
            self.__operation = None
            logger.error(f"The {operation_type} operation can't be resolved.")

    def calculate_operation(self, operation_type, number_1, number_2):
        self.set_operation(operation_type)
        return self.calculate(number_1, number_2)


if __name__ == '__main__':
    calculator = CalculatorStrategy()
    number_1 = 15
    number_2 = 5
    operation = 'sum'
    print(f'The result of {operation} operation between {number_1} and {number_2} '
          f'is: {calculator.calculate_operation(operation, number_1, number_2)}.')

    operation = 'subtraction'
    print(f'The result of {operation} operation between {number_1} and {number_2} '
          f'is: {calculator.calculate_operation(operation, number_1, number_2)}.')

    operation = 'multiplication'
    print(f'The result of {operation} operation between {number_1} and {number_2} '
          f'is: {calculator.calculate_operation(operation, number_1, number_2)}.')

    operation = 'division'
    print(f'The result of {operation} operation between {number_1} and {number_2} '
          f'is: {calculator.calculate_operation(operation, number_1, number_2)}.')

    operation = 'logarithm'
    print(f'The result of {operation} operation between {number_1} and {number_2} '
          f'is: {calculator.calculate_operation(operation, number_1, number_2)}.')
