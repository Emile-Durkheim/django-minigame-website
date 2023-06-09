# Funktionsweise von Views: https://docs.djangoproject.com/en/4.2/intro/tutorial03/


from django.shortcuts import render
from django.http import HttpRequest

from .models import Game


# Create your views here.
def sampleGame(request: HttpRequest):
    """
    Erklärung:

    "game = Game.objects.get(internal_name='sampleGame')" ist quasi äquivalent zu einem "SELECT * FROM games 
    WHERE internal_name = 'sampleGame'" Statement. Das Objekt game repräsentiert die Zeile mit dem internal_name
    'sampleGame', die Attribute (game.title, game.description...) repräsentieren die Spalten und den Inhalt der Zeile.

    "context = {'game': game}" wird später in render() verwendet, um zu bestimmen, welche Variablen im sampleGame.html zur Verfügung
    stehen sollen. So kann man den Spieltitel in der HTML Datei mit {{ game.title }} aufrufen. Würde { 'g': game } als context 
    definier werden, müsste man in der HTML-Datei {{ g.title }} aufrufen.

    "return render(request, 'games/sampleGame.html', context)" gibt dem Server die Anweisung, eine HTTPResponse mit einer gegebenen,
    gerenderten .html Datei zu versenden. Auch könnte hier etwa "return Http404" stehen, um einen 404 Fehlermeldung samt Fehlerseite
    zu senden.
    """
    game = Game.objects.get(internal_name='sampleGame')  # <- internal_name auf <spielname> anpassen

    context = {'game': game}

    return render(request, 'games/sampleGame.html', context)  # <- .html auf <spielname>.html ausbessern
