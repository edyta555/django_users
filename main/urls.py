from django.urls import path
from .views import all_users, new_user, edit_user, delete_user, getfile

urlpatterns = [
    path('users/', all_users, name='all_users'),
    path('new/', new_user, name='new_user'),
    path('edit/<int:id>/', edit_user, name='edit_user'),
    path('delete/<int:id>/', delete_user, name='delete_user'),
    path('csv/',getfile, name='download'),
]