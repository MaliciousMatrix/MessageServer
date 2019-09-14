from component import Component
from enum import Enum

class RelayState(Enum):
    OPEN = 0
    CLOSED = 1

class Relay(Component):
    def __init__(self, guid, name, gpio_pin, initial_state = RelayState.OPEN, *args, **kwargs):
        self.state = initial_state
        self._gpio_pin = gpio_pin
        return super().__init__(guid, name, *args, **kwargs)

    #TODO: Change this method to use GPIO.
    _state = RelayState.OPEN
    def get_state(self):
        return self._state
    def set_state(self, new_state):
        assert type(new_state) is RelayState
        self._state = new_state
    state = property(get_state, set_state)

    _gpio_pin = -1
    def get_gpio_pin():
        return self._gpio_pin
    gpio_pin = property(get_gpio_pin)

    def toggle(self):
        if self.state == RelayState.OPEN:
            self.state = RelayState.CLOSED
        else: # Current state is closed
            self.state = RelayState.OPEN

    def is_open(self):
        return self.state == RelayState.OPEN

    def is_closed(self):
        return not self.is_open()

