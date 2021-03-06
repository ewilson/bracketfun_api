from rest_framework import generics
from rest_framework.response import Response
from django.db.models.deletion import ProtectedError

from tournament.models import Player, Tournament, Match, Entry
from tournament.serializers import PlayerSerializer, TournamentSerializer, MatchSerializer, EntrySerializer


class PlayerList(generics.ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def delete(self, request, *args, **kwargs):
        try:
            response = super(PlayerDetail, self).delete(self, request, *args, **kwargs)
        except ProtectedError as e:
            response = Response(status=409, data=str(e))
        return response


class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer


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
