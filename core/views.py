from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms  import UserCreationForm
from django.contrib import messages
from django.contrib.auth import models, login, logout, authenticate
from django.db.models import Q
from .models import Message, Room, Topic
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
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=query_string)).order_by('-created_at')
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count, 'room_messages': room_messages}
    return render(request, 'core/home.html', context)

def user_profile(request, pk):
    try:
        user = User.objects.get(id=pk)

    except User.DoesNotExist:
        raise ObjectDoesNotExist('User not found.')
    context = {'user': user}
    return render(request, 'core/user_profile.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
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


def register_page(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred.')

    context = {'form': form}
    return render(request, 'core/register.html', context)

def logout_page(request):     
    logout(request)
    return redirect('login')


def room(request, pk):
    try:
        room = Room.objects.get(id=pk)
        room_messages = room.messages.all().order_by('-created_at')
        participants = room.participants.all()
        print('###############', participants)
        context = {'room': room, 'room_messages': room_messages, 'participants': participants}
        if request.method == 'POST':
            Message.objects.create(
                user = request.user,
                room = room,
                body = request.POST.get('body')

            )
            return redirect('room', pk=room.id)
    except Room.DoesNotExist:
            raise ObjectDoesNotExist("Room doesn't exist")
    return render(request, 'core/room.html', context)

@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'core/room_form.html', {'form':form})

@login_required(login_url='login')
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

@login_required(login_url='login')
def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You're not allowed")
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'core/delete.html', {'data': room})


def delete_message(request, pk):
    try:
        message = Message.objects.get(id=pk)
        if request.method == 'POST':
            message.delete()
            return redirect('home')
    except Message.DoesNotExist:
        raise ObjectDoesNotExist('Message not found.')
    return render(request, 'core/delete.html', {'data': message})