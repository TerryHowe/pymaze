
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


class TextView(object):

	def render(self, room, direction):
		t = [VIEW]
		left_room = room.go_left(direction)
		forward_room = room.go_forward(direction)
		right_room = room.go_right(direction)
		if left_room:
			#left_room = self.go_left_room(room_x, room_y, direction)
			#if not left_room.get(direction, None):
			#	t.append(LEFT_FORWARD_RIGHT)
			pass
		else:
			t.append(LEFT)
		if forward_room:
			#forward_room = self.go_forward_room(room_x, room_y, direction)
			#if forward_room.get(self.LEFT_DIRECTION[direction], None):
			#	left_room = self.go_forward_left_room(room_x, room_y, direction)
			#	if not left_room.get(direction, None):
			#		t.append(FORWARD_LEFT_FORWARD_RIGHT)
			#else:
			#	t.append(FORWARD_LEFT)
			#if not forward_room.get(direction, None):
			#	t.append(FORWARD_FORWARD)
			#if forward_room.get(self.RIGHT_DIRECTION[direction], None):
			#	right_room = self.go_forward_right_room(room_x, room_y, direction)
			#	if not right_room.get(direction, None):
			#		t.append(FORWARD_RIGHT_FORWARD_LEFT)
			#else:
			#	t.append(FORWARD_RIGHT)
			pass
		else:
			t.append(FORWARD)
		if right_room:
			#right_room = self.go_right_room(room_x, room_y, direction)
			#if not right_room.get(direction, None):
			#	t.append(RIGHT_FORWARD_LEFT)
			pass
		else:
			t.append(RIGHT)
		print
		print ''.join([max(x) for x in zip(*t)])
		print
		return ''.join([max(x) for x in zip(*t)])
