from datetime import date

from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    title = models.CharField(max_length=30)
    event_date = models.DateField(default=date.today)
    state = models.SmallIntegerField(default=0)
    players = models.ManyToManyField(Player)

    def __str__(self):
        return self.title


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='matches')
    completed = models.BooleanField(default=False)
    home_player = models.ForeignKey(Player, related_name='home_matches')
    away_player = models.ForeignKey(Player, related_name='away_matches')
    home_score = models.SmallIntegerField(default=0)
    away_score = models.SmallIntegerField(default=0)

    def __str__(self):
        return "Match: %d, Tournament: %s -- %s vs %s" % (self.id, self.tournament.title,
                                                          self.home_player.name, self.away_player.name)

    class Meta:
        verbose_name_plural = "matches"


