http client/server for asyncio
==============================

.. image:: https://raw.github.com/KeepSafe/aiohttp/master/docs/_static/aiohttp-icon-128x128.png
  :height: 64px
  :width: 64px
  :alt: aiohttp logo

.. image:: https://travis-ci.org/KeepSafe/aiohttp.svg?branch=master
  :target:  https://travis-ci.org/KeepSafe/aiohttp
  :align: right

.. image:: https://codecov.io/gh/KeepSafe/aiohttp/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/KeepSafe/aiohttp

.. image:: https://badge.fury.io/py/aiohttp.svg
    :target: https://badge.fury.io/py/aiohttp

Features
--------

- Supports both client and server side of HTTP protocol.
- Supports both client and server Web-Sockets out-of-the-box.
- Web-server has middlewares and pluggable routing.


Getting started
---------------

Client
^^^^^^

To retrieve something from the web:

.. code-block:: python

  import aiohttp
  import asyncio

  async def fetch(session, url):
      with aiohttp.Timeout(10, loop=session.loop):
          async with session.get(url) as response:
              return await response.text()

  async def main(loop):
      async with aiohttp.ClientSession(loop=loop) as session:
          html = await fetch(session, 'http://python.org')
          print(html)

  if __name__ == '__main__':
      loop = asyncio.get_event_loop()
      loop.run_until_complete(main(loop))


Server
^^^^^^

This is simple usage example:

.. code-block:: python

    from aiohttp import web

    async def handle(request):
        name = request.match_info.get('name', "Anonymous")
        text = "Hello, " + name
        return web.Response(text=text)

    async def wshandler(request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        async for msg in ws:
            if msg.type == web.MsgType.text:
                ws.send_str("Hello, {}".format(msg.data))
            elif msg.type == web.MsgType.binary:
                ws.send_bytes(msg.data)
            elif msg.type == web.MsgType.close:
                break

        return ws


    app = web.Application()
    app.router.add_get('/echo', wshandler)
    app.router.add_get('/', handle)
    app.router.add_get('/{name}', handle)

    web.run_app(app)


Note: examples are written for Python 3.5+ and utilize PEP-492 aka
async/await.  If you are using Python 3.4 please replace ``await`` with
``yield from`` and ``async def`` with ``@coroutine`` e.g.::

    async def coro(...):
        ret = await f()

should be replaced by::

    @asyncio.coroutine
    def coro(...):
        ret = yield from f()

Documentation
-------------

https://aiohttp.readthedocs.io/

Discussion list
---------------

*aio-libs* google group: https://groups.google.com/forum/#!forum/aio-libs

Requirements
------------

- Python >= 3.4.2
- async-timeout_
- chardet_
- multidict_
- yarl_

Optionally you may install the cChardet_ and aiodns_ libraries (highly
recommended for sake of speed).

.. _chardet: https://pypi.python.org/pypi/chardet
.. _aiodns: https://pypi.python.org/pypi/aiodns
.. _multidict: https://pypi.python.org/pypi/multidict
.. _yarl: https://pypi.python.org/pypi/yarl
.. _async-timeout: https://pypi.python.org/pypi/async_timeout
.. _cChardet: https://pypi.python.org/pypi/cchardet

License
-------

``aiohttp`` is offered under the Apache 2 license.


Source code
------------

The latest developer version is available in a github repository:
https://github.com/KeepSafe/aiohttp

Benchmarks
----------

If you are interested in by efficiency, AsyncIO community maintains a
list of benchmarks on the official wiki:
https://github.com/python/asyncio/wiki/Benchmarks

CHANGES
=======

1.3.1 (2017-02-09)
------------------

- Handle CLOSING in WebSocketResponse.__anext__

- Fixed AttributeError 'drain' for server websocket handler #1613


1.3.0 (2017-02-08)
------------------

- Multipart writer validates the data on append instead of on a request send #920

- Multipart reader accepts multipart messages with or without their epilogue
  to consistently handle valid and legacy behaviors #1526 #1581

- Separate read + connect + request timeouts # 1523

- Do not swallow Upgrade header #1587

- Fix polls demo run application #1487

- Ignore unknown 1XX status codes in client #1353

- Fix sub-Multipart messages missing their headers on serialization #1525

- Do not use readline when reading the content of a part
  in the multipart reader #1535

- Add optional flag for quoting `FormData` fields #916

- 416 Range Not Satisfiable if requested range end > file size #1588

- Having a `:` or `@` in a route does not work #1552

- Added `receive_timeout` timeout for websocket to receive complete message. #1325

- Added `heartbeat` parameter for websocket to automatically send `ping` message. #1024 #777

- Remove `web.Application` dependency from `web.UrlDispatcher` #1510

- Accepting back-pressure from slow websocket clients #1367

- Do not pause transport during set_parser stage #1211

- Lingering close doesn't terminate before timeout #1559

- `setsockopt` may raise `OSError` exception if socket is closed already #1595

- Lots of CancelledError when requests are interrupted #1565

- Allow users to specify what should happen to decoding errors
  when calling a responses `text()` method #1542

- Back port std module `http.cookies` for python3.4.2 #1566

- Maintain url's fragment in client response #1314

- Allow concurrently close WebSocket connection #754

- Gzipped responses with empty body raises ContentEncodingError #609

- Return 504 if request handle raises TimeoutError.

- Refactor how we use keep-alive and close lingering timeouts.

- Close response connection if we can not consume whole http
  message during client response release

- Abort closed ssl client transports, broken servers can keep socket open un-limit time #1568

- Log warning instead of `RuntimeError` is websocket connection is closed.

- Deprecated: `aiohttp.protocol.HttpPrefixParser`
  will be removed in 1.4 #1590

- Deprecated: Servers response's `.started`, `.start()` and `.can_start()` method
  will be removed in 1.4 #1591

- Deprecated: Adding `sub app` via `app.router.add_subapp()` is deprecated
  use `app.add_subapp()` instead, will be removed in 1.4 #1592

- Deprecated: aiohttp.get(), aiohttp.options(), aiohttp.head(), aiohttp.post(),
  aiohttp.put(), aiohttp.patch(), aiohttp.delete(), and aiohttp.ws_connect()
  will be removed in 1.4 #1593

- Deprecated: `Application.finish()` and `Application.register_on_finish()`
  will be removed in 1.4 #1602

