from django.urls import path
from .views import home, room, create_room

urlpatterns = [
    path('', home, name='home'),
    path('room/', room, name='room'),
    path('create-room/', create_room, name='create-room')
]