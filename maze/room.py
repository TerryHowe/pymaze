
class Room(object):
	COMPASS = ['N','E','S','W']

	def __init__(self, room_x, room_y, passages):
		self.room_x = room_x
		self.room_y = room_y
		self.passages = passages

	def go_forward(self, direction):
		return(self.passages.get(direction, None))

	def go_left(self, direction):
		idx = (self.COMPASS.index(direction) - 1) % len(self.COMPASS)
		return(self.passages.get(self.COMPASS[idx], None))

	def go_right(self, direction):
		idx = (self.COMPASS.index(direction) + 1) % len(self.COMPASS)
		return(self.passages.get(self.COMPASS[idx], None))
