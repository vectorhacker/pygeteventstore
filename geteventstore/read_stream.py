import feedparser
import aiohttp
from .event import Event

class Reader(object):
    """Creates a stream reader"""

    def __init__(self, stream, client):
        self._stream = stream
        self._client = client
        self._version = -1
        self._next_version = 0
        self._page_size = 20
        self._last_event = None
        self._feed_page = None

    def __aiter__(self):
        return self

    async def __anext__(self):
        num_entries = 0

        if self._feed_page is feedparser.FeedParserDict:
            num_entries = len(self._feed_page.entries)

        if self._feed_page is not feedparser.FeedParserDict:
            self._index = -1
            path = self._client.feed_path(
                self._stream, 'forward', self._next_version, self._page_size)
            self._url = path

        if self._index < 0:
            if self._feed_page is not feedparser.FeedParserDict:
                for link in self._feed_page.links:
                    if link.rel == 'previous':
                        self._url = link.href

            self._feed_page = feedparser.parse(self._url)
            num_entries = len(self._feed_page.entries)
            self._index = num_entries - 1

        if num_entries <= 0:
            raise StopAsyncIteration

        entry = self._feed_page.entries[self._index]
        async with aiohttp.ClientSession() as session:
            headers = {
                'Accept': 'application/vnd.eventstore.atom+json'
            }
            async with session.get(entry.id, headers=headers) as response:
                data = await response.json()
                content = data['content']
                event = Event(stream=content['eventStreamId'],
                                    number=content['eventNumber'],
                                    event_type=content['eventType'],
                                    id=content['eventId'],
                                    data=content['data'],
                                    metadata=content['metadata'])
                self._version = self._next_version
                self._next_version += 1
                self._index -= 1
                return event