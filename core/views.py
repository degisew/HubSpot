from django.shortcuts import render
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.all()
    return render(request, 'core/home.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'core/room.html', {'room': room})

def create_room(request):
    form = RoomForm()
    return render(request, 'core/room_form.html', {'form':form})