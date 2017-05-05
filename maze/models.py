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
	room_x = models.IntegerField()
	room_y = models.IntegerField()
	direction = models.CharField(max_length=1, choices=DIRECTION)
	destination = models.OneToOneField('self', on_delete=models.CASCADE)
	class Meta:
		unique_together = (('room_x', 'room_y', 'direction'),)
