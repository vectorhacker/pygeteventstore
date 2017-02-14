from . import event, client as c
import aiohttp
import json
import uuid


class Writer(object):
    """Creates a Stream Writer"""

    def __init__(self, stream, client, aiohttp=aiohttp):
        self._stream = stream
        self._client = client
        self._http = aiohttp

    async def write(self,
                    event_type,
                    event_id=str(uuid.uuid4()),
                    event_data={},
                    event_metadata={}):
        url = self._client.stream_path(self._stream)
        async with self._http.ClientSession(loop=self._client.loop) as session:
            headers = {
                'Content-Type': 'application/json',
                'ES-EventId': event_id,
                'ES-EventType': event_type
            }
            async with session.post(url, data=json.dumps(event_data), headers=headers) as response:
                if response.status != 201:
                    raise Exception
