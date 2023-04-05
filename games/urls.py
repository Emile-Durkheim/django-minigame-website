from django.contrib import admin
from django.urls import path

from core.views import login

from .views import game1, game2

urlpatterns = [
    path('game1', game1, name="game1"),
    path('game2', game2, name="game2"),
]
