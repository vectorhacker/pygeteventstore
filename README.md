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
    client = geteventstore.Client(loop=loop)
    reader = client.stream_reader('hello')

    async for event in reader:
        print(event)
    else:
        print('done')

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop=loop))
```
