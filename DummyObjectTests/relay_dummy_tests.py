from relay_dummy import RelayDummy, RelayState
import unittest

class RelayDummyTestCase(unittest.TestCase):
    def setUp(self):
        self.initially_open_relay = RelayMock(RelayState.OPEN)
        self.initially_closed_relay = RelayMock(RelayState.CLOSED)

    def test_relay_creation(self):

        self.assertEqual(self.initially_closed_relay.state, RelayState.CLOSED)
        self.assertNotEqual(self.initially_closed_relay.state, RelayState.OPEN)

        self.assertEqual(self.initially_open_relay.state, RelayState.OPEN)
        self.assertNotEqual(self.initially_open_relay.state, RelayState.CLOSED)

    def test_toggle(self):
        self.initially_open_relay.toggle()
        self.assertEqual(initially_open_relay.state, RelayState.CLOSED)
        self.initially_open_relay.toggle()
        self.assertEqual(initially_open_relay.state, RelayState.OPEN)

        self.initially_closed_relay.toggle()
        self.assertEqual(initially_open_relay.state, RelayState.OPEN)
        self.initially_closed_relay.toggle()
        self.assertEqual(initially_open_relay.state, RelayState.CLOSED)

        
if __name__ == '__main__':
    unittest.main()

