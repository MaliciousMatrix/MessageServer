import datetime

class Chat:
    def __init__(self, message, sender):
        self._message = message
        self._sender = sender
        self._timestamp = datetime.datetime.now()

    _timestamp = ''
    def get_timestamp(self):
        return self._timestamp
    timestamp = property(get_timestamp)

    _message = ''
    def get_message(self):
        return self._message
    message = property(get_message)

    _sender = ''
    def get_sender(self):
        return self._sender
    sender = property(get_sender)