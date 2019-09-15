import uuid

""" An individual sensor or actuator that does something"""
class Component:
    def __init__(self, guid, name, *args, **kwargs):
        assert type(guid) is uuid.UUID, 'guid must be a GUID'
        assert type(name) is str, 'name must be a string. Supplied: ' + str(name)
        assert not name.isspace(), 'name must not be empty space. Supplied: ' + str(name)
        assert name, 'name must not be an empty string.'
        self._guid = guid
        self._name = name

    def get_guid(self):
        return self._guid
    guid = property(get_guid)

    def get_name(self):
        return self._name
    name = property(get_name)





