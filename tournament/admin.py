from django.contrib import admin
from tournament.models import Player, Tournament, Match, Entry

admin.site.register(Player)
admin.site.register(Tournament)
admin.site.register(Match)
admin.site.register(Entry)
