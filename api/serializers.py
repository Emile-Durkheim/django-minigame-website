from django.urls import reverse

from rest_framework import serializers

from games.models import Game

class GameSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    uri = serializers.SerializerMethodField()

    def get_uri(self, object: Game):
        return reverse(object.view_name)