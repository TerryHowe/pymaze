
class Room(object):
	COMPASS = ['N','E','S','W']

	def __init__(self, room_x, room_y):
		self.room_x = room_x
		self.room_y = room_y
		self.passages = {}

	def go_forward(self, direction):
		return(self.passages.get(direction, None))

	def get_left_direction(self, direction):
		idx = (self.COMPASS.index(direction) - 1) % len(self.COMPASS)
		return(self.COMPASS[idx])

	def go_left(self, direction):
		return(self.passages.get(self.get_left_direction(direction), None))

	def get_right_direction(self, direction):
		idx = (self.COMPASS.index(direction) + 1) % len(self.COMPASS)
		return(self.COMPASS[idx])

	def go_right(self, direction):
		return(self.passages.get(self.get_right_direction(direction), None))

	def get_destinations(self, direction):
		left_direction = self.get_left_direction(direction)
		right_direction = self.get_right_direction(direction)
		forward = self.go_forward(direction)
		if forward:
			forward = ("%d/%d/%s" % (forward.room_x, forward.room_y, direction))
		return {
			'left': ("%d/%d/%s" % (self.room_x, self.room_y, left_direction)),
			'forward': forward,
			'right': ("%d/%d/%s" % (self.room_x, self.room_y,  right_direction))
		}
