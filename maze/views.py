# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome to the maze.")

def room(request, room_x, room_y, direction):
    return HttpResponse("Looking %s from %s, %s." % (direction, room_x, room_y))
