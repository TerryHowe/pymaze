import unittest
import mock

import room
import text_view

DEAD_END = """
 \                              /
  \                            / 
   +--------------------------+  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   +--------------------------+  
  /                            \\ 
 /                              \\
"""
NORTH = """
 \                               
  \                              
   +                          +--
   |\                         |  
   | \                        |  
   |  +--------------------+  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  +--------------------+  |  
   | /                        |  
   |/                         |  
   +                          +--
  /                              
 /                               
"""
EAST = """
                                /
                               / 
 --+                          +  
   |\                         |  
   | \                        |  
   |  +--------------------+  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  +--------------------+  |  
   | /                        |  
   |/                         |  
 --+                          +  
                               \\ 
                                \\
"""
SOUTH = """
                                /
                               / 
 --+--------------------------+  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
 --+--------------------------+  
                               \\ 
                                \\
"""
WEST = """
 \                               
  \                              
   +--------------------------+--
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   |                          |  
   +--------------------------+--
  /                              
 /                               
"""
R01_SOUTH = """
 \                              /
  \                            / 
   +                          +  
   |                          |  
   |                          |  
   |--+--------------------+  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |--+--------------------+  |  
   |                          |  
   |                          |  
   +                          +  
  /                            \\ 
 /                              \\
"""

class TestTextView(unittest.TestCase):

	def setUp(self):
		self.r10 = room.Room(1, 0, {})
		self.r01 = room.Room(0, 1, {})
		self.r00 = room.Room(0, 0, {'N':self.r01,'E':self.r10})
		self.r10.passages['W'] = self.r00
		self.r01.passages['S'] = self.r00

	def test_render_dead_end(self):
		sut = text_view.TextView()
		self.assertEqual(DEAD_END, sut.render(self.r01, 'N'))

	def test_render_r00_north(self):
		sut = text_view.TextView()
		self.assertEqual(NORTH, sut.render(self.r00, 'N'))

	def test_render_r00_east(self):
		sut = text_view.TextView()
		self.assertEqual(EAST, sut.render(self.r00, 'E'))

	def test_render_r00_south(self):
		sut = text_view.TextView()
		self.assertEqual(SOUTH, sut.render(self.r00, 'S'))

	def test_render_r00_west(self):
		sut = text_view.TextView()
		self.assertEqual(WEST, sut.render(self.r00, 'W'))

	def test_render_r01_south(self):
		sut = text_view.TextView()
		self.assertEqual(R01_SOUTH, sut.render(self.r01, 'S'))

if __name__ == '__main__':
	unittest.main()

