from relay_virtual import RelayVirtual, RelayState
import unittest
import uuid

class RelayVirtualTestCase(unittest.TestCase):
    def setUp(self):
        self.initially_open_relay = RelayVirtual(uuid.uuid4(), 'Initially Open Relay', RelayState.OPEN)
        self.initially_closed_relay = RelayVirtual(uuid.uuid4(), 'Initially Closed Relay', RelayState.CLOSED)

    def test_relay_creation(self):

        self.assertEqual(self.initially_closed_relay.state, RelayState.CLOSED)
        self.assertNotEqual(self.initially_closed_relay.state, RelayState.OPEN)

        self.assertEqual(self.initially_open_relay.state, RelayState.OPEN)
        self.assertNotEqual(self.initially_open_relay.state, RelayState.CLOSED)

    def test_set_closed_state_to_closed_stays_closed(self):
        self.assertEqual(self.initially_closed_relay.state, RelayState.CLOSED)
        self.initially_closed_relay.state = RelayState.CLOSED
        self.assertEqual(self.initially_closed_relay.state, RelayState.CLOSED)

    def test_set_open_state_to_open_stays_open(self):
        self.assertEqual(self.initially_open_relay.state, RelayState.OPEN)
        self.initially_open_relay.state = RelayState.OPEN
        self.assertEqual(self.initially_open_relay.state, RelayState.OPEN)

    def test_set_closed_state_to_open_is_open(self):
        self.assertEqual(self.initially_closed_relay.state, RelayState.CLOSED)
        self.initially_closed_relay.state = RelayState.OPEN
        self.assertEqual(self.initially_closed_relay.state, RelayState.OPEN)

    def test_set_open_state_to_closed_is_closed(self):
        self.assertEqual(self.initially_open_relay.state, RelayState.OPEN)
        self.initially_open_relay.state = RelayState.CLOSED
        self.assertEqual(self.initially_open_relay.state, RelayState.CLOSED)
        
    def test_toggle(self):
        self.initially_open_relay.toggle()
        self.assertEqual(self.initially_open_relay.state, RelayState.CLOSED)
        self.initially_open_relay.toggle()
        self.assertEqual(self.initially_open_relay.state, RelayState.OPEN)

        self.initially_closed_relay.toggle()
        self.assertEqual(self.initially_closed_relay.state, RelayState.OPEN)
        self.initially_closed_relay.toggle()
        self.assertEqual(self.initially_closed_relay.state, RelayState.CLOSED)

    def test_is_open(self):
        self.assertTrue(self.initially_open_relay.is_open())
        self.assertFalse(self.initially_closed_relay.is_open())

    def test_is_closed(self):
        self.assertTrue(self.initially_closed_relay.is_closed())
        self.assertFalse(self.initially_open_relay.is_closed())
        
if __name__ == '__main__':
    unittest.main()

