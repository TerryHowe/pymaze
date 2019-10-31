# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
from .models import Passage
from maze import text_view
from maze import maze


def index(request):
	return redirect('0/0/N', True)


def room(request, room_x, room_y, direction):
	room_x = int(room_x)
	room_y = int(room_y)

	passages = Passage.objects.all()
	theMaze = maze.Maze(passages)
	room = theMaze.get_room(room_x, room_y)
	if room is None:
		raise Http404("Room %d,%d does not exist" % (room_x, room_y))
	destinations = room.get_destinations(direction)
	maze_view = text_view.TextView().render(room, direction)
	context = {
		'room_x': room_x,
		'room_y': room_y,
		'direction': direction,
		'maze_view': maze_view,
		'direction_long': Passage.get_direction(direction),
	}
	context.update(destinations)
	return render(request, 'maze/room.html', context)
