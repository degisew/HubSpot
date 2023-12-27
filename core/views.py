from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
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

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    return render(request, 'core/login.html')

def logout_page(request):     
    logout(request)
    return redirect('login')


def room(request, pk):
    room = Room.objects.get(id=pk)
    return render(request, 'core/room.html', {'room': room})

@login_required
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'core/room_form.html', {'form':form})

@login_required
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse("You're not allowed")
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'core/room_form.html', {'form': form})

@login_required
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    print(room)
    
    if request.method == 'POST':
        print('Hello')
        room.delete()
        return redirect('home')
    return render(request, 'core/delete.html', {'room': room})
