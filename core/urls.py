from django.urls import path
from .views import home, register_page, room, create_room, update_room, delete_room, login_page, logout_page


urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>/', room, name='room'),
    path('create-room/', create_room, name='create-room'),
    path('update-room/<str:pk>/', update_room, name='update-room'),
    path('delete-room/<str:pk>/', delete_room, name='delete-room'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout')
]