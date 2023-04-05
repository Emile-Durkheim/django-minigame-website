from django.shortcuts import render
from django.http import HttpRequest

from .models import Game

# Create your views here.
def game2(request: HttpRequest):
    game = Game.objects.get(view_name="game2")
    
    context = {'game': game}

    return render(request, 'games/game2.html', context)

def game1(request: HttpRequest):
    game = Game.objects.get(view_name="game1")
    
    context = {'game': game}

    return render(request, 'games/game1.html', context)
