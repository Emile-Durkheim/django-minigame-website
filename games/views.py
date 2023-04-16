# Funktionsweise von Views: https://docs.djangoproject.com/en/4.2/intro/tutorial03/


from django.shortcuts import render
from django.http import HttpRequest

from .models import Game


# Create your views here.
def sampleGame(request: HttpRequest):
    # Äquivalent zu game = SELECT * FROM games WHERE internal_name = "sampleGAME"
    # game hat nun Attribute .title, .description, .internal_name
    game = Game.objects.get(internal_name="sampleGame")  # <- internal_name auf <spielname> anpassen

    # Wenn auf das game Objekt in sampleGame.html zugegriffen soll, muss es in einem dict definiert und an render() weitergegeben werden
    context = {'game': game}

    # Gibt dem Server die Anweisung, ein gerendertes HTML-Dokument als HTTPResponse zu schicken.
    return render(request, 'games/sampleGame.html', context)  # <- .html auf <spielname>.html ausbessern
