from django.shortcuts import render


rooms = [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'JavaScript'},
    {'id': 3, 'name': 'Django'}
]

def home(request):
   return render(request, 'core/home.html', {'rooms': rooms})


def room(request, pk):
    name = None
    for room in rooms:
        if room['id'] == int(pk):
            name = room['name']
    return render(request, 'core/room.html', {'room': name})