from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    # participants = 
    updated_at =  models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Message(models.Model):

    room = models.Foreignkey(Room, on_delete = models.SET_NULL)