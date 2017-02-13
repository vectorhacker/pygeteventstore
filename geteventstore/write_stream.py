from .event import Event
from .client import Client
import aiohttp
import json


class Writer(object):
    """Creates a Stream Writer"""
    def __init__(self, stream, client):
        if client is not Client:
            raise TypeError

        self._stream = stream
        self._client = client

    async def write(self, event):
        if event is not Event:
            raise TypeError
        url = self._client.stream_path(self._stream)
        async with aiohttp.ClientSession() as session:
            headers = {
                'Content-Type': 'application/json',
                'ES-EventId': event.id,
                'ES-EventType': event.type
            }
            async with session.post(url, data=json.dumps(event.data), headers=headers) as response:
                if response.status != 201:
                    raise Exception