from strategies.base_strategy import BaseStrategy


class ConsoleStrategy(BaseStrategy):

    # just print all to console
    def write(self, file, data_to_write):
        for line in data_to_write:
            print(line)

