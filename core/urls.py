from django.urls import path
from .views import home, register_page, room, create_room, update_room, delete_room, delete_message, activities_page, topics_page, update_user, login_page, logout_page, user_profile


urlpatterns = [
    path('', home, name='home'),
    path('room/<str:pk>/', room, name='room'),
    path('create-room/', create_room, name='create-room'),
    path('update-room/<str:pk>/', update_room, name='update-room'),
    path('user-profile/<str:pk>/', user_profile, name='user-profile'),
    path('topics/', topics_page, name='topics'),
    path('activities/', activities_page, name='activities'),
    path('delete-room/<str:pk>/', delete_room, name='delete-room'),
    path('delete-message/<str:pk>/', delete_message, name='delete-message'),
    path('update-user/', update_user, name='update-user'),
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('logout/', logout_page, name='logout')
]