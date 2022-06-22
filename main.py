import os

import requests
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Request

from models import Link
from strategies.write_to_cloud import CloudStrategy
from strategies.write_to_console import ConsoleStrategy
from strategies.write_to_file import FileStrategy

# loading .env vars
load_dotenv()

# init webhook
app = FastAPI()


def get_strategy():
    strategy = os.environ.get('STRATEGY')
    if strategy == 'console':
        return ConsoleStrategy()
    elif strategy == 'file':
        return FileStrategy()
    elif strategy == 'cloud':
        return CloudStrategy()


@app.post('/load')
def load_file_from_link(item: Link):
    print(item.link)
    file = requests.get(item.link)
    strategy = get_strategy()

    if strategy:
        strategy.write(item.filename, file.json())
        return {'message': f'File processed with{strategy}'}
    else:
        return {'message': f'No strategy specified'}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
