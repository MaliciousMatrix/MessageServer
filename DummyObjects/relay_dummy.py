
from enum import Enum
class RelayState(Enum):
    OPEN = 0
    CLOSED = 1
""" mocks a relay which has two states: on and off"""

class RelayDummy:
    def __init__(self, initial_state = RelayState.OPEN):
        self.state = initial_state

    _state = RelayState.OPEN
    def get_state(self):
        return self._state
    def set_state(self, new_state):
        assert type(new_state) is RelayState
        self._state = new_state
    state = property(get_state, set_state)

    def toggle():
        pass

    def isOpen():
        pass

    def isClosed():
        pass
