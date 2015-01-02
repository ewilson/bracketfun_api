from rest_framework import serializers

from tournament.models import Player, Tournament


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id','name',)


class TournamentSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Player.objects.all()
    )

    class Meta:
        model = Tournament
        fields = ('id', 'title', 'event_date', 'state', 'players')
