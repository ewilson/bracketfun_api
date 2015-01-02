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

    def __str__(self):
        return "Match: %d, Tournament: %s" % (self.id, self.tournament.name)

    class Meta:
        verbose_name_plural = "matches"


# Join table between Player and Match, stores both scores for convenience.
class Attempt(models.Model):
    player = models.ForeignKey(Player)
    match = models.ForeignKey(Match)
    score = models.SmallIntegerField(null=True, blank=True)
    opponent_score = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return "%s in Match: %s" % (self.player, str(self.match))
