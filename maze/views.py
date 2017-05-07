# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Passage
import maze
import text_view


def index(request):
	return HttpResponse("Welcome to the maze.")

def room(request, room_x, room_y, direction):
	room_x = int(room_x)
	room_y = int(room_y)
	template = loader.get_template('maze/room.html')
	passages = Passage.objects.all()
	theMaze = maze.Maze(passages)
	room = theMaze.get_room(room_x, room_y)
	destination = room.go_forward(direction)
	maze_view = text_view.TextView().render(room, direction)
	context = {
		'room_x': room_x,
		'room_y': room_y,
		'direction': direction,
		'direction_long': Passage.get_direction(direction),
		'destination': destination,
		'maze_view': maze_view,
		'left_direction': theMaze.get_left_direction(direction),
		'right_direction': theMaze.get_right_direction(direction),
	}
	return HttpResponse(template.render(context, request))
