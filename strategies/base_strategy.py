from abc import ABC, abstractmethod
from utils.helper_functions import split_class_name


class BaseStrategy(ABC):

    @abstractmethod
    def write(self, filename, data_to_write):
        pass

    def __str__(self):
        return split_class_name(self.__class__.__name__)
