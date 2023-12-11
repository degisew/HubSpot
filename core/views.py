from django.shortcuts import redirect, render
from .models import Room, Topic
from .forms import RoomForm

def home(request):
    rooms = Room.objects.order_by('-created_at').all()
    topics = Topic.objects.all()
    return render(request, 'core/home.html', {'rooms': rooms, 'topics': topics})


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


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'core/room_form.html', {'form': form})


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    print(room)
    
    if request.method == 'POST':
        print('Hello')
        room.delete()
        return redirect('home')
    return render(request, 'core/delete.html', {'room': room})
