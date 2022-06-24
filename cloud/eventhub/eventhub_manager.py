import json

from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData

from settings import EVENTHUB_CONNECTION_STRING, TEST_MODE


class EventHub:
    def __init__(self, data_to_write):
        self.data_to_write = data_to_write

    def divide_chunks(self, N):

        for index in range(0, len(self.data_to_write), N):
            yield self.data_to_write[index:index + N]

    async def process(self):
        producer = EventHubProducerClient.from_connection_string(conn_str=EVENTHUB_CONNECTION_STRING)
        async with producer:
            chunks = list(self.divide_chunks(150))

            if TEST_MODE:
                chunks = [chunks[0]]

            for chunk in chunks:
                print(len(chunk))
                event_data_batch = await producer.create_batch()
                for data in chunk:
                    event_data_batch.add(EventData(json.dumps(data)))
                await producer.send_batch(event_data_batch)
            print('CHUNK WRITTEN TO EVENTHUB\n')
