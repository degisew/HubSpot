from django.db import models
from django.contrib.auth.models import User
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.Foreignkey(Room, on_delete = models.CASCADE)
    body = models.TextField()

    updated_at =  models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
