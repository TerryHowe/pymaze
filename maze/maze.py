import models

MAZE_VIEW = """
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
VIEW = """
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
                                 
"""
LEFT = """
 \                               
  \                              
   +                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   |                             
   +                             
  /                              
 /                               
"""
RIGHT = """
                                /
                               / 
                              +  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              |  
                              +  
                               \\ 
                                \\
"""
FORWARD = """
                                 
                                 
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
                                 
                                 
"""


class Maze(object):
	LEFT_DIRECTION = {
		'N': 'W',
		'E': 'N',
		'S': 'E',
		'W': 'S',
	}
	RIGHT_DIRECTION = {
		'N': 'E',
		'E': 'S',
		'S': 'W',
		'W': 'N',
	}
	def __init__(self):
		self.map = {}
		for p in models.Passage.objects.all():
			if p.room_x not in self.map:
				self.map[p.room_x] = {}
			x = self.map[p.room_x]
			if p.room_y not in x:
				x[p.room_y] = {}
			y = x[p.room_y]
			if p.direction not in y:
				y[p.direction] = {}
			y[p.direction] = p.destination

	def render(self, room_x, room_y, direction):
		room = self.map.get(int(room_x), {}).get(int(room_y), {})
		left_room = room.get(self.LEFT_DIRECTION[direction], None)
		forward_room = room.get(direction, None)
		right_room = room.get(self.RIGHT_DIRECTION[direction], None)
		t = [VIEW]
		if not left_room:
			t.append(LEFT)
		if not forward_room:
			t.append(FORWARD)
		if not right_room:
			t.append(RIGHT)
		return ''.join([max(x) for x in zip(*t)]) + str(left_room) + str(forward_room) + str(right_room)

	def get_left_direction(self, direction):
		return self.LEFT_DIRECTION[direction]

	def get_right_direction(self, direction):
		return self.RIGHT_DIRECTION[direction]

theMaze = Maze()
