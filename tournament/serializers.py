from rest_framework import serializers

from tournament.models import Player, Tournament, Match


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name',)


class TournamentSerializer(serializers.ModelSerializer):
    players = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Player.objects.all()
    )
    matches = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Match.objects.all(),
        required=False
    )

    class Meta:
        model = Tournament
        fields = ('id', 'title', 'event_date', 'state', 'players', 'matches')


class MatchSerializer(serializers.ModelSerializer):
    home_player = serializers.PrimaryKeyRelatedField(
        queryset=Player.objects.all()
    )
    away_player = serializers.PrimaryKeyRelatedField(
        queryset=Player.objects.all()
    )
    tournament = serializers.PrimaryKeyRelatedField(
        queryset=Tournament.objects.all()
    )

    class Meta:
        model = Match
        fields = ('id', 'tournament', 'completed',
                  'home_player', 'away_player', 'home_score', 'away_score')