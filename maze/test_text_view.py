import unittest

import room
import text_view

R01_NORTH = """
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
R00_NORTH = """
 \                               
  \                              
   +                          +--
   |\                        /|  
   | \                      / |  
   |  +--------------------+  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  +--------------------+  |  
   | /                      \ |  
   |/                        \|  
   +                          +--
  /                              
 /                               
"""
R00_EAST = """
                                /
                               / 
 --+                          +  
   |\                        /|  
   | \                      / |  
   |  +--------------------+  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  +--------------------+  |  
   | /                      \ |  
   |/                        \|  
 --+                          +  
                               \\ 
                                \\
"""
R00_SOUTH = """
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
R00_WEST = """
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
   |                         /|  
   |                        / |  
   |--+--------------------+  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |--+--------------------+  |  
   |                        \ |  
   |                         \|  
   +                          +  
  /                            \\ 
 /                              \\
"""
R10_WEST = """
 \                              /
  \                            / 
   +                          +  
   |\                         |  
   | \                        |  
   |  +--------------------+--|  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  |                    |  |  
   |  +--------------------+--|  
   | /                        |  
   |/                         |  
   +                          +  
  /                            \\ 
 /                              \\
"""

class TestTextView(unittest.TestCase):

	def setUp(self):
		self.r10 = room.Room(1, 0)
		self.r01 = room.Room(0, 1)
		self.r00 = room.Room(0, 0)
		self.r00.passages['N'] = self.r01
		self.r00.passages['E'] = self.r10
		self.r10.passages['W'] = self.r00
		self.r01.passages['S'] = self.r00

	def test_render_dead_end(self):
		sut = text_view.TextView()
		self.assertEqual(R01_NORTH, sut.render(self.r01, 'N'))

	def test_render_r00_north(self):
		sut = text_view.TextView()
		self.assertEqual(R00_NORTH, sut.render(self.r00, 'N'))

	def test_render_r00_east(self):
		sut = text_view.TextView()
		self.assertEqual(R00_EAST, sut.render(self.r00, 'E'))

	def test_render_r00_south(self):
		sut = text_view.TextView()
		self.assertEqual(ROO_SOUTH, sut.render(self.r00, 'S'))

	def test_render_r00_west(self):
		sut = text_view.TextView()
		self.assertEqual(R00_WEST, sut.render(self.r00, 'W'))

	def test_render_r01_south(self):
		sut = text_view.TextView()
		self.assertEqual(R01_SOUTH, sut.render(self.r01, 'S'))

	def test_render_r10_west(self):
		sut = text_view.TextView()
		self.assertEqual(R10_WEST, sut.render(self.r10, 'W'))

if __name__ == '__main__':
	unittest.main()
