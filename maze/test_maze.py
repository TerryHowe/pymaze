import unittest
import mock

import maze


class TestMaze(unittest.TestCase):

	def create_passage(self, x, y, d):
		p = mock.Mock()
		p.room_x = x
		p.room_y = y
		p.direction = d
		return p

	def setUp(self):
		p1 = self.create_passage(0, 0, 'N')
		p2 = self.create_passage(0, 0, 'E')
		p3 = self.create_passage(1, 0, 'W')
		p4 = self.create_passage(0, 1, 'S')
		p1.destination = p4
		p2.destination = p3
		p3.destination = p1
		p4.destination = p1
		passages = [p1, p2, p3, p4]
		self.maze = maze.Maze(passages)

	def test_get_room_00(self):
		room = self.maze.get_room(0, 0)
		self.assertEqual(0, room.room_x)
		self.assertEqual(0, room.room_y)
		self.assertEqual(0, room.passages['N'].room_x)
		self.assertEqual(1, room.passages['N'].room_y)
		self.assertEqual(1, room.passages['E'].room_x)
		self.assertEqual(0, room.passages['E'].room_y)

	def test_get_room_10(self):
		room = self.maze.get_room(1, 0)
		self.assertEqual(1, room.room_x)
		self.assertEqual(0, room.room_y)
		self.assertEqual(0, room.passages['W'].room_x)
		self.assertEqual(0, room.passages['W'].room_y)

	def test_get_room_01(self):
		room = self.maze.get_room(0, 1)
		self.assertEqual(0, room.room_x)
		self.assertEqual(1, room.room_y)
		self.assertEqual(0, room.passages['S'].room_x)
		self.assertEqual(0, room.passages['S'].room_y)


if __name__ == '__main__':
	unittest.main()
