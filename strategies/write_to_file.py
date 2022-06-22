from strategies.base_strategy import BaseStrategy


class FileStrategy(BaseStrategy):

    # save data to file
    def write(self, filename, data_to_write):
        with open(f'files/{filename}.txt', 'w') as file:
            for line in data_to_write:
                file.write(f'{line}\n')
