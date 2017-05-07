# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Passage(models.Model):
	DIRECTIONS = (
		('N', 'North'),
		('E', 'East'),
		('S', 'South'),
		('W', 'West'),
		('U', 'Up'),
		('D', 'Down'),
	)
	room_x = models.IntegerField()
	room_y = models.IntegerField()
	direction = models.CharField(max_length=1, choices=DIRECTIONS)
	destination = models.OneToOneField('self',
		null=True, blank=True,
		on_delete=models.CASCADE)

	@classmethod
	def get_direction(cls, direction):
		return dict(cls.DIRECTIONS).get(direction, 'Nowhere')

	def __str__(self):
		return(self.__repr__())

	def __repr__(self):
		dest = str(self.destination.id) if self.destination else 'None'
		return('Passage(id=%d, room_x=%d, room_y=%d, direction=%s, destination=%s)' % (self.id, self.room_x, self.room_y, self.direction, dest))

	class Meta:
		unique_together = (('room_x', 'room_y', 'direction'),)
