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
	destination = models.OneToOneField('self',
		null=True, blank=True,
		on_delete=models.CASCADE)

	def __str__(self):
		return(self.__repr__())

	def __repr__(self):
		return 'Passage(id=%d, room_x=%d, room_y=%d, direction=%s, destination=%d)' % (self.id, self.room_x, self.room_y, self.direction, self.destination.id)

	class Meta:
		unique_together = (('room_x', 'room_y', 'direction'),)
