from . import event, client
import aiohttp
import json


class Writer(object):
    """Creates a Stream Writer"""
    def __init__(self, stream, client):
        if client is not client.Client:
            raise TypeError

        self._stream = stream
        self._client = client

    async def write(self, e):
        if e is not event.Event:
            raise TypeError
        url = self._client.stream_path(self._stream)
        async with aiohttp.ClientSession() as session:
            headers = {
                'Content-Type': 'application/json',
                'ES-EventId': e.id,
                'ES-EventType': e.type
            }
            async with session.post(url, data=json.dumps(e.data), headers=headers) as response:
                if response.status != 201:
                    raise Exception