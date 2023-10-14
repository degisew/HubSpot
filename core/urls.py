from django.urls import path
from .views import home, room, create_room


urlpatterns = [
    path('', home, name='home'),
    path('<str:pk>', room, name='room'),
    path('create/', create_room, name='create_room'),
]