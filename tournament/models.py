from datetime import date

from django.db import models


class Player(models.Model):
    managed = True
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Tournament(models.Model):
    managed = True
    title = models.CharField(max_length=30)
    event_date = models.DateField(default=date.today)
    players = models.ManyToManyField(Player)
    SETUP = 0
    PLAY = 1
    COMPLETE = 2
    STATE_CHOICES = ((SETUP, 'Setup'), (PLAY, 'Play'), (COMPLETE, 'Complete'))
    state = models.SmallIntegerField(default=SETUP, choices=STATE_CHOICES)
    ROUND_ROBIN = 0
    POOLS = 1
    TYPE_CHOICES = ((ROUND_ROBIN, 'Round-robin'), (POOLS, 'Pools'))
    type = models.SmallIntegerField(default=ROUND_ROBIN, choices=TYPE_CHOICES)

    def __str__(self):
        return self.title


class Match(models.Model):
    managed = True
    tournament = models.ForeignKey(Tournament, related_name='matches')
    completed = models.BooleanField(default=False)
    home_player = models.ForeignKey(Player, related_name='home_matches',
                                    on_delete=models.PROTECT)
    away_player = models.ForeignKey(Player, related_name='away_matches',
                                    on_delete=models.PROTECT)
    home_score = models.SmallIntegerField(default=0)
    away_score = models.SmallIntegerField(default=0)
    pool = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return "Match: %d, Tournament: %s, Pool: %s -- %s vs %s" % \
               (self.id, self.tournament.title, self.pool, self.home_player.name, self.away_player.name)

    class Meta:
        verbose_name_plural = "matches"


