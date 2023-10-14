from django.db import models


class Room(models.Model):
    #host
    #topic
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    #participants
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
    
class Message(models.Model):
    #user
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.body[:50]