geteventstore
========================

This is a simple implementation of the Event Store client for the HTTP interface. It uses asyncio to asyncly parse events

## Reference

Accessing the Event Store

### Client

`Client(options) -> client`

Creates a new event store client. The keyword arguments are:

- `host`: host of the RethinkDB instance. The default value is `localhost`.
- `port`: the driver port, by default `2113`.
- `loop`: the asyncio event loop, by default `asyncio.get_event_loop()`

*Example*: Create a new client to the default event store

```python
loop=asyncio.get_event_loop()
client = geteventstore.Client(loop=loop)
```

### stream_reader

`client.stream_reader(options) -> Reader`

Creates a stream reader. The keyword arguments are:

- `stream`: the stream to read from.

*Example*: Create a new stream readers

```python
import geteventstore
import asyncio

async def test(loop):
    try:
        current = 0
        poll = 10
        while True:
            current = await get_events(loop, current, poll)
    except KeyboardInterrupt:
        return

async def get_events(loop, current=0, poll=0):
    client = geteventstore.Client(loop=loop)
    reader = client.stream_reader('flyers')
    reader.next_version = current
    if poll > 0:
        reader.long_poll(poll)

    async for event, meatadata, updated in reader:
        print(event)
        print(metadata)
        print(updated)
    return reader.next_version

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
```

### Reader

`geteventstore.Reader(options) -> Reader`

Creates a stream reader. The keyword arguments are:

- `stream`: the stream to read from
- `client`: the geteventstore client
- `feed_parser`: the feed parser to use, defaults to `feedparser`. Must be compatible with feedparser
- `http`: the http client to use, defaults to `aiohttp`. Must be compatible with aiohttp

*Example*: Create a new stream and read from *text*

```python
import geteventstore
import asyncio

async def test(loop):
    try:
        current = 0
        poll = 10
        while True:
            current = await get_events(loop, current, poll)
    except KeyboardInterrupt:
        return

async def get_events(loop, current=0, poll=0):
    client = geteventstore.Client(loop=loop)
    reader = geteventstore.Reader('flyers', client)
    reader.next_version = current
    if poll > 0:
        reader.long_poll(poll)

    async for event, _, updated in reader:
        print(event.id)
        print(updated)
    return reader.next_version

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
```

TODO:

- [-] Read from stream
    - [x] Catchup subscription
    - [x] Volatile Subscriptions
    - [ ] Persistent Subscription
- [x] Write to stream