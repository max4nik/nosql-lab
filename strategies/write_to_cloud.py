from cloud.eventhub.eventhub_manager import EventHub
from cloud.redis.redis_manager import Redis
from strategies.base_strategy import BaseStrategy


class CloudStrategy(BaseStrategy):
    def __init__(self, file):
        super().__init__(file)
        self.redis = Redis(self.filename)

    def on_start(self):
        self.redis.start_loading_file()

    def on_finish(self):
        self.redis.finish_loading_file()

    def is_ignored(self):
        if is_loaded := self.redis.is_file_loaded():
            self.redis.ignore_file()
        return is_loaded

    async def write(self, data_to_write):
        eventhub = EventHub(data_to_write)
        await eventhub.process()
