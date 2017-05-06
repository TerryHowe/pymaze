import models

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
LEFT_FORWARD_RIGHT = """
                                 
                                 
 --+                             
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
 --+                             
                                 
                                 
"""
RIGHT_FORWARD_LEFT = """
                                 
                                 
                              +--
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
                              +--
                                 
                                 
"""
FORWARD_FORWARD = """
                                 
                                 
                                 
                                 
                                 
      +--------------------+     
      |                    |     
      |                    |     
      |                    |     
      |                    |     
      |                    |     
      |                    |     
      |                    |     
      +--------------------+     
                                 
                                 
                                 
                                 
                                 
"""
FORWARD_LEFT = """
                                 
                                 
   +                             
   |\                            
   | \                           
   |  +                          
   |  |                          
   |  |                          
   |  |                          
   |  |                          
   |  |                          
   |  |                          
   |  |                          
   |  +                          
   | /                           
   |/                            
   +                             
                                 
                                 
"""
FORWARD_RIGHT = """
                                 
                                 
                              +  
                             /|  
                            / |  
                           +  |  
                           |  |  
                           |  |  
                           |  |  
                           |  |  
                           |  |  
                           |  |  
                           |  |  
                           +  |  
                            \ |  
                             \|  
                              +  
                                 
                                 
"""
FORWARD_LEFT_FORWARD_RIGHT = """
                                 
                                 
                                 
                                 
                                 
    --+                          
      |                          
      |                          
      |                          
      |                          
      |                          
      |                          
      |                          
    --+                          
                                 
                                 
                                 
                                 
                                 
"""
FORWARD_RIGHT_FORWARD_LEFT = """
                                 
                                 
                                 
                                 
                                 
                           +--   
                           |     
                           |     
                           |     
                           |     
                           |     
                           |     
                           |     
                           +--   
                                 
                                 
                                 
                                 
                                 
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

	def get_room(self, room_x, room_y):
		return self.map.get(room_x, {}).get(room_y, {})

	def get_forward_room(self, room_x, room_y, direction):
		if (direction == 'N'):
			return(self.get_room(room_x, room_y+1))
		elif (direction == 'E'):
			return(self.get_room(room_x+1, room_y))
		elif (direction == 'S'):
			return(self.get_room(room_x, room_y-1))
		return(self.get_room(room_x-1, room_y))

	def get_forward_right_room(self, room_x, room_y, direction):
		if (direction == 'N'):
			return(self.get_room(room_x+1, room_y+1))
		elif (direction == 'E'):
			return(self.get_room(room_x+1, room_y-1))
		elif (direction == 'S'):
			return(self.get_room(room_x-1, room_y-1))
		return(self.get_room(room_x-1, room_y+1))

	def get_forward_left_room(self, room_x, room_y, direction):
		if (direction == 'N'):
			return(self.get_room(room_x-1, room_y+1))
		elif (direction == 'E'):
			return(self.get_room(room_x+1, room_y+1))
		elif (direction == 'S'):
			return(self.get_room(room_x+1, room_y-1))
		return(self.get_room(room_x-1, room_y-1))

	def get_right_room(self, room_x, room_y, direction):
		if (direction == 'N'):
			return(self.get_room(room_x+1, room_y))
		elif (direction == 'E'):
			return(self.get_room(room_x, room_y-1))
		elif (direction == 'S'):
			return(self.get_room(room_x-1, room_y))
		return(self.get_room(room_x, room_y+1))

	def get_left_room(self, room_x, room_y, direction):
		if (direction == 'N'):
			return(self.get_room(room_x-1, room_y))
		elif (direction == 'E'):
			return(self.get_room(room_x, room_y+1))
		elif (direction == 'S'):
			return(self.get_room(room_x+1, room_y))
		return(self.get_room(room_x, room_y-1))

	def render(self, room_x, room_y, direction):
		room_x = int(room_x)
		room_y = int(room_y)
		room = self.get_room(room_x, room_y)
		t = [VIEW]
		if room.get(self.LEFT_DIRECTION[direction], None):
			left_room = self.get_left_room(room_x, room_y, direction)
			if not left_room.get(direction, None):
				t.append(LEFT_FORWARD_RIGHT)
		else:
			t.append(LEFT)
		if room.get(direction, None):
			forward_room = self.get_forward_room(room_x, room_y, direction)
			if forward_room.get(self.LEFT_DIRECTION[direction], None):
				left_room = self.get_forward_left_room(room_x, room_y, direction)
				if not left_room.get(direction, None):
					t.append(FORWARD_LEFT_FORWARD_RIGHT)
			else:
				t.append(FORWARD_LEFT)
			if not forward_room.get(direction, None):
				t.append(FORWARD_FORWARD)
			if forward_room.get(self.RIGHT_DIRECTION[direction], None):
				right_room = self.get_forward_right_room(room_x, room_y, direction)
				if not right_room.get(direction, None):
					t.append(FORWARD_RIGHT_FORWARD_LEFT)
			else:
				t.append(FORWARD_RIGHT)
		else:
			t.append(FORWARD)
		if room.get(self.RIGHT_DIRECTION[direction], None):
			right_room = self.get_right_room(room_x, room_y, direction)
			if not right_room.get(direction, None):
				t.append(RIGHT_FORWARD_LEFT)
		else:
			t.append(RIGHT)
		return ''.join([max(x) for x in zip(*t)])

	def get_left_direction(self, direction):
		return self.LEFT_DIRECTION[direction]

	def get_right_direction(self, direction):
		return self.RIGHT_DIRECTION[direction]

	def get_destination(self, room_x, room_y, direction):
		room_x = int(room_x)
		room_y = int(room_y)
		passages = models.Passage.objects.filter(room_x=room_x, room_y=room_y)
		for passage in passages:
			if passage.direction == direction:
					return passage.destination
		return None
