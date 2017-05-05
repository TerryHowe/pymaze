# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Passage


def index(request):
	return HttpResponse("Welcome to the maze.")

def room(request, room_x, room_y, direction):
	passages = Passage.objects.filter(room_x=int(room_x), room_y=int(room_y))
	template = loader.get_template('maze/room.html')
	context = {
		'room_x': room_x,
		'room_y': room_y,
		'direction': Passage.get_direction(direction),
		'passages': passages,
	}
	return HttpResponse(template.render(context, request))
