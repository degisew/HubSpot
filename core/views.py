from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import models, login, logout, authenticate
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

def login_page(request):
    post_data = request.POST
    username = post_data.get('username')
    password = post_data.get('password')

    try:
        user = models.User.objects.get(username=username)
    except:
        messages.error(request, "User not found.")
        
    auth_user = authenticate(request, username=username, password=password)
    if auth_user is not None:
            login(request, auth_user)
            messages.success(request, 'Login success.')
            return redirect('home')
    return render(request, 'core/login.html')

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
