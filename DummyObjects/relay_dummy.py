from relay import Relay
from enum import Enum
class RelayState(Enum):
    OPEN = 0
    CLOSED = 1
""" mocks a relay which has two states: on and off"""

class RelayDummy(Compnonent):
    def set_state(self, new_state):
        assert type(new_state) is RelayState
        self._state = new_state

    def get_state(self):
        return self._state
