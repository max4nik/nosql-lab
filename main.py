import requests
import uvicorn

from fastapi import FastAPI

from cloud.elasticsearch.elasticsearch_manager import ElasticSearch
from models import Link
from strategies.write_to_cloud import CloudStrategy
from strategies.write_to_console import ConsoleStrategy
from strategies.write_to_file import FileStrategy
from settings import STRATEGY

# init webhook
app = FastAPI()

# init elastic
es_manager = ElasticSearch()


def get_strategy(file):
    if STRATEGY == 'console':
        return ConsoleStrategy(file)
    elif STRATEGY == 'file':
        return FileStrategy(file)
    elif STRATEGY == 'cloud':
        return CloudStrategy(file)


@app.get('/top_animals')
def get_top_animals(size: int = 5):
    top_animals = es_manager.get_top_animals(size)
    return {'top_animals': top_animals}


@app.get('/top_streets')
def get_top_streets(size: int = 5):
    top_streets = es_manager.get_top_streets(size)
    return {'top_streets': top_streets}


@app.post('/load')
async def load_file_from_link(item: Link):
    file_link = item.file
    strategy = get_strategy(file_link)

    if not strategy:
        return {'message': f'No strategy specified'}

    if isinstance(strategy, CloudStrategy) and strategy.is_ignored():
        return {'message': 'Ignoring file because it was already processed'}

    limit = 6000
    offset = 0
    has_next_chunk = True

    strategy.on_start()
    while has_next_chunk:
        file_response = requests.get(f'{file_link}?$limit={limit}&$offset={offset}')
        file_json = file_response.json()
        if len(file_json) != 0:
            print('PROCESSING NEXT CHUNK...')
            await strategy.write(file_json)
            offset += limit
        else:
            has_next_chunk = False
    strategy.on_finish()
    return {'message': f'File processed with{strategy}'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
