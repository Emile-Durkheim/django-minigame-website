from django.db import models
from core.models import User

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1023)
    view_name = models.CharField(max_length=255, unique=True)  # what's in urls.py after name=; used to generate the game's URL
    
    def __str__(self):
        return self.title


class Achievement(models.Model):
    title = models.CharField('achievement title', max_length=50)
    description = models.CharField('achievement description', max_length=255)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    user = models.ManyToManyField(User, through="User_Has_Achievement")  # Initialize inbetween table
    
    def __str__(self):
        return self.game.title + ': ' + self.title


class User_Has_Achievement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    
    date_unlocked = models.DateField()