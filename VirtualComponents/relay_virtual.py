from relay import Relay, RelayState
import sys, os
sys.path.append(os.getcwd() + '\\..\\CommonFunctions')
from event import Event

""" mocks a relay which has two states: on and off"""
class RelayVirtual(Relay):
    def __init__(self, guid, name, initial_state = RelayState.OPEN, *args, **kwargs):
        return super().__init__(guid, name, -1, initial_state, **kwargs)

    def set_state(self, new_state):
        assert type(new_state) is RelayState
        if self.state != new_state:
            self._state = new_state
            self.state_changed(new_state)

    def get_state(self):
        return self._state

    def get_gpio_pin():
        return -1
