from django.forms import ModelForm, fields
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ['host', 'topic', 'name', 'description']
        labels = {'name': 'RoomName'}