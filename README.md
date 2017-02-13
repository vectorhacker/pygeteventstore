geteventstore
========================

This is a simple implementation of the Event Store client for the HTTP interface. It uses asyncio to asyncly parse events

Simple exmaple for reading events

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

`Learn more <http://www.kennethreitz.org/essays/repository-structure-and-python>`_.
