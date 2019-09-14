import uuid

""" An individual sensor or actuator that does something"""
class Compnonent:
    def __init__(self, guid, name, *args, **kwargs):
        assert type(guid) is uuid.UUID
        self._guid = guid
        self._name = name

    def get_guid(self):
        return self._guid
    guid = property(get_guid)

    def get_name(self):
        return self._name
    name = property(get_name)




