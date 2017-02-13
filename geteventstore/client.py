#!/bin/env python3


import uuid
import asyncio
import aiohttp

import read_stream

class Client(object):
    """Creates an Event Store Client"""

    def __init__(self, host='localhost', port=2113):
        self._host = host
        self._port = port

    def stream_reader(self, stream):
        return read_stream.Reader(stream, self)

    def stream_write(self, stream):
        pass

    def feed_path(self, stream, fw_bw, version, page_size):
        # example: 'http://localhost:2113/streams/hello/0/forward/20'
        return 'http://{0}:{1}/streams/{2}/{3}/{4}/{5}'.format(self._host, self._port, stream, version, fw_bw, page_size)