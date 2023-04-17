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

4. URL-Routing einrichten: 
  - In `/noodle_grounds/urls.py` zunächst view importieren. (`from games.views import sampleGame, <spielname>`)
  - Dann in urlpatterns Liste speichern: `path('<spielname', <spielname>, name="<spielname>")` (urlpattern zeigt nun auf View, und View verarbeitet die Request des Clients)

4. Spiel in Datenbank anlegen. Am einfachsten zu erledigen im Admin-Panel: http://127.0.0.1:8000/admin (email: root@root.root, pw: adminadmin). 

# Allgemein

- models.py: Hier wird das Datenbankschema definiert. Jede Klasse = Ein Table, jedes Attribut = Eine Spalte. https://docs.djangoproject.com/en/4.2/intro/tutorial02/
