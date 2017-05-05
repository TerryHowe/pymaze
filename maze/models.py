# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
DIRECTION = (
	('N', 'North'),
	('E', 'East'),
	('S', 'South'),
	('W', 'West'),
)

class Passage(models.Model):
	room_x = models.IntegerField(primary_key=True)
	room_y = models.IntegerField(primary_key=True)
	direction = models.CharField(max_length=1, choices=DIRECTION, primary_key=True)
	destination = models.ForeignKey('self')
