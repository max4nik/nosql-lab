import os

from strategies.base_strategy import BaseStrategy


class FileStrategy(BaseStrategy):
    def __init__(self, file):
        super().__init__(file)
        self.path = f'files/{self.filename.split(".")[0]}.txt'

    def on_start(self):
        print('STARTED FILE WRITING')
        try:
            os.remove(self.path)
        except FileNotFoundError:
            pass

    def on_finish(self):
        print('FINISHED FILE WRITING')

    # save data to file
    async def write(self, data_to_write):
        with open(self.path, 'a') as file:
            for line in data_to_write:
                file.write(f'{line}\n')
