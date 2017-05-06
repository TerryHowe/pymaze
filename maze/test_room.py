import unittest
import mock

import room


class TestRoom(unittest.TestCase):

    def setUp(self):
		self.r10 = room.Room(1, 0, {})
		self.r01 = room.Room(0, 1, {})
		self.r00 = room.Room(0, 0, {'N':self.r01,'E':self.r10})
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


if __name__ == '__main__':
    unittest.main()

