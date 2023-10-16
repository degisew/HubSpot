from django.shortcuts import redirect, render
from .models import Room
from .forms import RoomForm

def home(request):
    rooms = Room.objects.order_by('-created_at').all()
    return render(request, 'core/home.html', {'rooms': rooms})


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'core/room.html', {'room': room})

def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'core/room_form.html', {'form':form})