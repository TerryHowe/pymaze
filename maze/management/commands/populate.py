from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Populate the database'

    def handle(self, *args, **options):
        from maze.models import Passage

        one = Passage(room_x=0,room_y=0,direction='N')
        two = Passage(room_x=0,room_y=1,direction='S')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()

        one = Passage(room_x=0,room_y=0,direction='E')
        two = Passage(room_x=1,room_y=0,direction='W')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()

        one = Passage(room_x=1,room_y=0,direction='E')
        two = Passage(room_x=2,room_y=0,direction='W')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()

        one = Passage(room_x=2,room_y=0,direction='N')
        two = Passage(room_x=2,room_y=1,direction='S')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()

        one = Passage(room_x=2,room_y=1,direction='N')
        two = Passage(room_x=2,room_y=2,direction='S')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()

        one = Passage(room_x=2,room_y=2,direction='W')
        two = Passage(room_x=1,room_y=2,direction='E')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()

        one = Passage(room_x=1,room_y=2,direction='W')
        two = Passage(room_x=0,room_y=2,direction='E')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()

        one = Passage(room_x=0,room_y=2,direction='S')
        two = Passage(room_x=0,room_y=1,direction='N')
        one.save()
        two.save()
        one.destination = two
        two.destination = one
        one.save()
        two.save()
