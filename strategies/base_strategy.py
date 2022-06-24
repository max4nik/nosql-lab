import os
from abc import ABC, abstractmethod
from utils.helper_functions import split_class_name


class BaseStrategy(ABC):
    def __init__(self, file):
        self.file = file
        self.filename = os.path.basename(file)

    @abstractmethod
    async def write(self, data_to_write):
        pass

    @abstractmethod
    def on_start(self):
        pass

    @abstractmethod
    def on_finish(self):
        pass

    def __str__(self):
        return split_class_name(self.__class__.__name__)
