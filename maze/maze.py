import room


class Maze(object):
	def __init__(self, passages):
		self.map = {}
		for p in passages:
			t = (p.room_x, p.room_y)
			if t not in self.map:
				self.map[t] = room.Room(*t)
			from_room = self.map[t]
			t = (p.destination.room_x, p.destination.room_y)
			if t not in self.map:
				self.map[t] = room.Room(*t)
			to_room = self.map[t]
			from_room.passages[p.direction] = to_room

	def get_room(self, room_x, room_y):
		return self.map.get((room_x,room_y), None)
