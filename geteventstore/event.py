class Event(object):
    def __init__(self, stream, id, event_type, number, data = {}):
        self._id = id
        self._stream = stream
        self._type = event_type
        self._data = data
        self._number = number

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def data(self):
        return self._data
    @property
    def stream(self):
        return self._stream