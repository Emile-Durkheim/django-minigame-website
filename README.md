# Installation

Packages installieren; in CMD: `pip install django` & `pip install djangorestframework`

VSCode Extension installieren: Django (Siehe Extension Beschreibung, um Django-HTML Highlighting in HTML-Dokumenten einzuschalten. Unter Umständen muss Django-HTML danach noch als Standard-Format für HTML Dateien eingestellt werden.)

## Lauffähige Seiten:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/admin (root@root.root, adminadmin)
- http://127.0.0.1:8000/login (testuser1@testuser1.com, testuser1)
- http://127.0.0.1:8000/register 
- http://127.0.0.1:8000/sampleGame
- http://127.0.0.1:8000/api/games

# Anleitungen

## Server starten

`py manage.py runserver [port]` (in noodle_grounds/)

## Spiel anlegen

1. HTML Template anlegen: Eine `/games/templates/games/<spielname>.html` Datei anlegen. Siehe sampleGame.html, Gerüst kann einfach kopiert werden.

2. Ordner für statische Dateien anlegen: Einen `/games/static/games/<spielname>` Ordner anlegen. Hier sollten alle .js, .css, .png... Dateien gespeichert werden, auf welche die \<spielname>.html verweist. 

3. View anlegen: `def <spielname>:` Funktion in games/views.py anlegen. Siehe `def sampleGame:`; Funktionsinhalt kann kopiert werden, nur der Spielname sollte in den Strings angepasst werden.
* Django sieht alle /static/ und /template/ Ordner als einen einzelnen Ordner. Gibt es also games/static/game.png und core/static/core.png, wird in einer HTML-Datei darauf immer über {% static 'game.png' %} und {% static 'core.png' %} zugegriffen, ohne auf Elternordner zu verweisen. Namespacing möglich über Unterordner: Wenn Pfad nun aussieht wie games/static/games/game.png und core/static/core/core.png, dann kann zugegriffen werden über {% static 'games/game.png' %} und {% static 'core/core.png' %}: Keine Kollisionsgefahr.
4. URL-Routing einrichten: 
  - In `/noodle_grounds/urls.py` zunächst view importieren. (`from games.views import sampleGame, <spielname>`)
  - Dann in urlpatterns Liste speichern: `path('<spielname', <spielname>, name="<spielname>")` (urlpattern zeigt nun auf View, und View verarbeitet die Client-Request und schickt über return eine Response)

4. Spiel in Datenbank anlegen. Am einfachsten zu erledigen im Admin-Panel: http://127.0.0.1:8000/admin (email: root@root.root, pw: adminadmin). 

# Allgemein

- Django HTML-Templating Language: https://docs.djangoproject.com/en/4.1/ref/templates/language/

- App: Jeder Ordner außer noodle_grounds (also /core/, /games/ und /api/) ist eine "App". Hilft, verschiedene Komponenten von einander separat zu halten.

- models.py: Hier wird das Datenbankschema definiert. Jede Klasse = Ein Table, jedes Attribut = Eine Spalte. models.py kann in jeder App existieren. Nachdem models.py angepasst wurde (also effektiv Datenbankschma verändert wurde), muss `py manage.py makemigrations` und `py manage.py migrate` ausgeführt werden. https://docs.djangoproject.com/en/4.2/intro/tutorial02/

- /templates/ Ordner: Für alle HTML-Dateien. Diese werden in views.py in render() geladen. /templates/ Ordner kann in jeder App existieren.*

- /static/ Ordner: Für alles, was nicht .html ist; daher .js, .css, .png... Wenn zB `static/games/noodleJump/thumb.png` Datei geladen werden soll, würde dies über `<img src="{% static 'games/noodleJump/thumb.png' %}">` geschehen. Der Template-Ausdruck wird vom Server dann durch den korrekten Pfad zur statischen Datei ersetzt. (Wichtig, da statische Dateien im Realfall oft auf eigene Server mit eigenen Pfadstrukturen ausgelagert werden) /static/ Ordner kann in jeder App existieren.* Notiz: Wird {% static '' %} Template-Funktion verwendet, muss in der ersten Zeile der .html-Datei {% load static %} aufgerufen werden.

\* Django sieht alle /static/ und /template/ Ordner als einen einzelnen Ordner. Gibt es also `games/static/game.png` und `core/static/core.png`, wird in einer HTML-Datei darauf immer über {% static 'game.png' %} und {% static 'core.png' %} zugegriffen, ohne auf Elternordner zu verweisen. Namespacing möglich über Unterordner: Wenn Pfad nun aussieht wie `games/static/games/game.png` und `core/static/core/core.png`, dann kann zugegriffen werden über {% static 'games/game.png' %} und {% static 'core/core.png' %}: Keine Kollisionsgefahr.
