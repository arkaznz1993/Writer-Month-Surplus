import os

SURPLUS_LIST = '6200d4f29afdb28ae4b8dcbe'

PARAMS = {
    "key": os.environ.get("TRELLO_API_KEY"),
    "token": os.environ.get("TRELLO_TOKEN"),
}

HEADERS = {
    "Accept": "application/json"
}