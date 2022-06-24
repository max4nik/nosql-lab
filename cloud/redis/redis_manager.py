import os

import redis
from settings import REDIS_HOST, REDIS_PASSWORD, REDIS_PORT


class FileStatus:
    STARTED = 'STARTED'
    LOADED = 'LOADED'
    IGNORED = 'IGNORED'


class Redis:

    def __init__(self, filename):
        self.filename = filename
        self.redis_instance = redis.StrictRedis(host=REDIS_HOST, password=REDIS_PASSWORD, port=REDIS_PORT, ssl=True)

    def get_status(self):
        status_encoded = self.redis_instance.get(self.filename)
        if not status_encoded:
            return
        return status_encoded.decode("utf-8")

    def is_file_loaded(self):
        status = self.get_status()
        return status in [FileStatus.LOADED, FileStatus.IGNORED]

    def ignore_file(self):
        self.redis_instance.set(self.filename, FileStatus.IGNORED)

    def start_loading_file(self):
        self.redis_instance.set(self.filename, FileStatus.STARTED)

    def finish_loading_file(self):
        self.redis_instance.set(self.filename, FileStatus.LOADED)
