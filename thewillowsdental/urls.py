from django.urls import path
from thewillowsdental import views

urlpatterns = [
    path('', views.home, name='thewillowsdental'),
]