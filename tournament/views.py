from rest_framework import generics

from tournament.models import Player, Tournament, Match
from tournament.serializers import PlayerSerializer, TournamentSerializer, MatchSerializer


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class TournamentList(generics.ListCreateAPIView):
    serializer_class = TournamentSerializer

    def get_queryset(self):
        queryset = Tournament.objects.all()
        state = self.request.query_params.get('state', None)
        if state is not None:
            queryset = queryset.filter(state=state)
        return queryset


class TournamentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tournament.objects.all()
    serializer_class = TournamentSerializer


class MatchList(generics.ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer


class MatchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
