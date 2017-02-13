from . import event, client as c
import aiohttp
import json


class Writer(object):
    """Creates a Stream Writer"""

    def __init__(self, stream, client, aiohttp=aiohttp):
        if client is not c.Client:
            raise TypeError

        self._stream = stream
        self._client = client
        self._http = aiohttp

    async def write(self, event_type, event_id, event_data, event_metadata):
        url = self._http.stream_path(self._stream)
        async with self._aiohttp.ClientSession(loop=self._client.loop) as session:
            headers = {
                'Content-Type': 'application/json',
                'ES-EventId': id,
                'ES-EventType': event_type
            }
            async with session.post(url, data=json.dumps(data), headers=headers) as response:
                if response.status != 201:
                    raise Exception
