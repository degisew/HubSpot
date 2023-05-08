from django.shortcuts import render
from .models import Room
from .forms import RoomForm
# Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request):
    return render (request, 'base/room.html')

def create_room(request):
    form = RoomForm()
    context = {'form':form}
    return render(request, 'base/room_form.html', context)