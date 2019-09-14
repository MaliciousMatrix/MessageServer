import unittest
from component import Component
import uuid
class ComponentTestCase(unittest.TestCase):
    def test_creation(self):
        valid_guids = [
            uuid.UUID('71720bcd-feed-499c-8305-8cf68c0fa95f'),
            uuid.UUID('cc89478d-99a3-4481-8618-d9d0ea497235'),
            uuid.UUID('502a625c-6b4e-483d-8572-ac01d300b2b8'),
            uuid.UUID('954d9866-83ea-456c-8c6e-f995e31994ed'),
        ]

        invalid_guids = [
            1,
            '954d9866-83ea-456c-8c6e-f995e31994ed',
            -23,
            5 + 6,
            'c',
            'My name',
            False,
            True,
            10j,
            '',
            ]

        for guid in valid_guids:
            c = Component(guid, "my component")
            self.assertEqual(guid, c.guid)
            self.assertEqual(guid, c.get_guid())

        for invalid in invalid_guids:
            self.assertRaises(AssertionError, Component, invalid, 'my compnonent')

        valid_names = [
            'My component',
            'c',
            'front light'
            'l',
            '12345',
            '##$@@#%helfgstnha',
            ]

        invalid_names = [
            '',
            '    ',
            '\n',
            '    \n',
            12,
            -10,
            ]

        for name in valid_names:
            c = Component(uuid.UUID('71720bcd-feed-499c-8305-8cf68c0fa95f'), name)
            self.assertEqual(c.name, name)
            self.assertEqual(c.get_name(), name)

        for name in invalid_names:
            self.assertRaises(AssertionError, Component, uuid.UUID('71720bcd-feed-499c-8305-8cf68c0fa95f'), name)

if __name__ == '__main__':
    unittest.main()