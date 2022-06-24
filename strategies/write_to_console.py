from strategies.base_strategy import BaseStrategy


class ConsoleStrategy(BaseStrategy):

    def on_start(self):
        print('STARTED WRITING TO CONSOLE')

    def on_finish(self):
        print('FINISHED WRITING TO CONSOLE')

    # just print all to console
    async def write(self, data_to_write):
        for line in data_to_write:
            print(line)

