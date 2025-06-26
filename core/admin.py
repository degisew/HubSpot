from django.contrib import admin
from .models import Message, Room, Topic


admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Topic)

