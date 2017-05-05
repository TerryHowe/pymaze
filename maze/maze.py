import models

MAZE_VIEW = """
 \                              /
  \                            /
   +--------------------------+
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
   +--------------------------+
  /                            \\
 /                              \\
"""

class Maze(object):
	def __init__(self):
		self.passages = models.Passage.objects.all()

	def render(self, room_x, room_y, direction):
		return MAZE_VIEW;

theMaze = Maze()
