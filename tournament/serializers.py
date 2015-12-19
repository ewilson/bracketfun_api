from rest_framework import serializers

from tournament.models import Player, Tournament, Match, Entry


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Player
        fields = ('id', 'name')


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    player = serializers.PrimaryKeyRelatedField(
        queryset=Player.objects.all()
    )
    tournament = serializers.PrimaryKeyRelatedField(
        queryset=Tournament.objects.all()
    )

    class Meta:
        model = Entry
        fields = ('id', 'player', 'tournament', 'pool')


class TournamentSerializer(serializers.ModelSerializer):
    entries = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Entry.objects.all(),
        required=False
    )
    matches = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Match.objects.all(),
        required=False
    )

    class Meta:
        model = Tournament
        fields = ('id', 'title', 'event_date', 'state', 'entries', 'matches', 'type')


class MatchSerializer(serializers.ModelSerializer):
    home_player = serializers.PrimaryKeyRelatedField(
        queryset=Entry.objects.all()
    )
    away_player = serializers.PrimaryKeyRelatedField(
        queryset=Entry.objects.all()
    )
    tournament = serializers.PrimaryKeyRelatedField(
        queryset=Tournament.objects.all()
    )

    class Meta:
        model = Match
        fields = ('id', 'tournament', 'completed',
                  'home_player', 'away_player', 'home_score', 'away_score')