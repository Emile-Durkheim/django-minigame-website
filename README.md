Setup:

```pip install django```
```pip install djangorestframework```

Um den Server zu starten, in noodle_grounds/:

```py manage.py runserver 8000```

Lauffähige Seiten:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/admin (root@root.root, adminadmin)
- http://127.0.0.1:8000/login (testuser1@testuser1.com, testuser1)
- http://127.0.0.1:8000/game1
- http://127.0.0.1:8000/game2
- http://127.0.0.1:8000/api/games

Die Frontend HTML-Files befinden sich jeweils in core/templates/core und games/templates/games, und alle weiteren Files (.css, .js, .png) befinden sich in den respektiven core/static/core und games/static/games Ordnern.
