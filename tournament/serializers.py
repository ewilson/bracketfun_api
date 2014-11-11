from rest_framework import serializers

from models import Player, Tournament


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id','name',)


class TournamentSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = Tournament
        fields = ('id', 'name', 'event_date', 'state', 'players')

