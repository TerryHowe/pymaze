# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Passage
import maze


def index(request):
	return HttpResponse("Welcome to the maze.")

def room(request, room_x, room_y, direction):
	passages = Passage.objects.filter(room_x=int(room_x), room_y=int(room_y))
	destination = None
	for passage in passages:
		if passage.direction == direction:
			destination = passage.destination
	template = loader.get_template('maze/room.html')
	theMaze = maze.Maze()
	context = {
		'room_x': room_x,
		'room_y': room_y,
		'direction': direction,
		'destination': destination,
		'direction_long': Passage.get_direction(direction),
		'passages': passages,
		'maze_view': theMaze.render(room_x, room_y, direction),
		'left_direction': theMaze.get_left_direction(direction),
		'right_direction': theMaze.get_right_direction(direction),
	}
	return HttpResponse(template.render(context, request))
