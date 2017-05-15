import unittest

import room


class TestRoom(unittest.TestCase):

    def setUp(self):
		self.r10 = room.Room(1, 0)
		self.r01 = room.Room(0, 1)
		self.r00 = room.Room(0, 0)
		self.r00.passages['N'] = self.r01
		self.r00.passages['E'] = self.r10
		self.r10.passages['W'] = self.r00
		self.r01.passages['S'] = self.r00

    def test_go_forward(self):
        self.assertEqual(self.r01, self.r00.go_forward('N'))
        self.assertEqual(self.r10, self.r00.go_forward('E'))
        self.assertIsNone(self.r00.go_forward('S'))
        self.assertIsNone(self.r00.go_forward('W'))

    def test_go_left(self):
        self.assertIsNone(self.r00.go_left('N'))
        self.assertEqual(self.r01, self.r00.go_left('E'))
        self.assertEqual(self.r10, self.r00.go_left('S'))
        self.assertIsNone(self.r00.go_left('W'))

    def test_go_right(self):
        self.assertEqual(self.r10, self.r00.go_right('N'))
        self.assertIsNone(self.r00.go_right('E'))
        self.assertIsNone(self.r00.go_right('S'))
        self.assertEqual(self.r01, self.r00.go_right('W'))

    def test_get_left_direction(self):
        self.assertEqual('W', self.r00.get_left_direction('N'))
        self.assertEqual('N', self.r00.get_left_direction('E'))
        self.assertEqual('E', self.r00.get_left_direction('S'))
        self.assertEqual('S', self.r00.get_left_direction('W'))

    def test_get_right_direction(self):
        self.assertEqual('E', self.r00.get_right_direction('N'))
        self.assertEqual('S', self.r00.get_right_direction('E'))
        self.assertEqual('W', self.r00.get_right_direction('S'))
        self.assertEqual('N', self.r00.get_right_direction('W'))

    def test_get_backward_direction(self):
        self.assertEqual('S', self.r00.get_backward_direction('N'))
        self.assertEqual('W', self.r00.get_backward_direction('E'))
        self.assertEqual('N', self.r00.get_backward_direction('S'))
        self.assertEqual('E', self.r00.get_backward_direction('W'))

    def test_go_backward(self):
        self.assertIsNone(self.r00.go_backward('N'))
        self.assertIsNone(self.r00.go_backward('E'))
        self.assertEqual(self.r01, self.r00.go_backward('S'))
        self.assertEqual(self.r10, self.r00.go_backward('W'))

    def test_get_destinations(self):
        self.assertEqual({
				'forward': '0/1/N',
				'left': '0/0/W',
				'right': '0/0/E',
				'backward': None
			},
			self.r00.get_destinations('N'))
        self.assertEqual({
				'forward': '1/0/E',
				'left': '0/0/N',
				'right': '0/0/S',
				'backward': None
			},
			self.r00.get_destinations('E'))
        self.assertEqual({
				'forward': None,
				'left': '0/0/E',
				'right': '0/0/W',
				'backward': '0/1/S'
			},
			self.r00.get_destinations('S'))
        self.assertEqual({
				'forward': None,
				'left': '0/0/S',
				'right': '0/0/N',
				'backward': '1/0/W'
			},
			self.r00.get_destinations('W'))


if __name__ == '__main__':
    unittest.main()
