from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=30)    

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class State(Place):
    pass


class TownHall(Place):
    state = models.ForeignKey(State, on_delete=models.CASCADE)

