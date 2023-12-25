from django.shortcuts import redirect, render
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm

def home(request):
    QS = request.GET.get('qs')
    query_string = QS if QS != None else ''
    rooms = Room.objects.order_by('-created_at').select_related('topic').filter(
        Q(topic__name__icontains=query_string) |
        Q(name__icontains=query_string) |
        Q(description__icontains=query_string)
        )
    topics = Topic.objects.all()
    room_count = rooms.count()
    return render(request, 'core/home.html', {'rooms': rooms, 'topics': topics, 'room_count': room_count})



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
